# Java: PDF creation

I've used the FPDF library before quite easily, so I suggest looking for something based on it. A quick search reveals the following:

https://github.com/nkiraly/Java-FPDF

## Old code

This is some code from 2015 I used to create PDFs of my classlists at a previous school. It used the FPDF library (a previous version that was hosted on sourceforge). It likely needs a new coat of paint but it should hopefully give some indications as to how to get started.

**net/paulbaumgarten/schoolutils/PhotoClassLists.java**

```java
package net.paulbaumgarten.schoolutils;
// PDF
import net.sourceforge.javafpdf.*;
import java.io.File;
import net.paulbaumgarten.helpers.FreePDF;
import java.io.FileNotFoundException;
// JSON
import java.util.Scanner;
import java.io.File;
import org.json.*;
// MYSQL
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;
// ReadInput
import net.paulbaumgarten.helpers.IO;

/*
PDF library methods:
* Set colours and coordinates etc
    pdf.setDrawColor(0,0,0);
    pdf.setFillColor(0,0,0);
    pdf.setTextColor(0,0,0);
    pdf.setFont("arial", null,10);
    pdf.setFontSize(10);
    pdf.setXY(10,10);       // units are millimetres?
    pdf.getX(); pdf.getY();
* Line break
    pdf.Ln();
* New page
    pdf.addPage();
* Insert an image file
    // type = PNG, JPEG (not quoted)
    pdf.Image( String file, x, y, width, height, type, 0 );
    pdf.Image("c:\\test.png", coordinate, 50, 50, ImageType.PNG, 0);
* Insert a text cell
    pdf.Cell( width, height, text, 0, 0, align ); // left = L
    pdf.MultiCell( width, height, spacing, text, border, align );
* Draw a line (two methods)
    pdf.Line( x1, y1, x2, y2 );
    pdf.Line(new Coordinate(x1, y1), new Coordinate(x2, y2));
* Draw a rectangle
    // F = fill
    pdf.Rect( x1, y1, addX, addY, 'F');
*/

public class PhotoClassLists {
  
  String dbType;
  String dbAddress;
  String dbUser;
  String dbPassword;
  String dbName;
  String photosFolder;
  String saveFolder;
  String connectionString;

  public PhotoClassLists(String settingsFilename) {
    photosFolder = new String("");
    saveFolder = new String("");
    connectionString = new String("");
    try {
      String jsonTxt = new Scanner(new File(settingsFilename)).useDelimiter("\\Z").next();
      JSONObject json = new JSONObject(jsonTxt);  

      String dbType = json.getJSONObject("database").getString("type");
      String dbAddress = json.getJSONObject("database").getString("address");
      String dbUser = json.getJSONObject("database").getString("user");
      String dbPassword = json.getJSONObject("database").getString("password");
      String dbName = json.getJSONObject("database").getString("name");
      connectionString = "jdbc:"+dbType+"://"+dbAddress+"/"+dbName+"?user="+dbUser+"&password="+dbPassword;

      photosFolder = json.getString("photos");
      saveFolder = json.getString("savefolder");
    } catch (Exception e) {
      System.out.println(e);
    }  
  }
  
  public void createPhotoClassLists(String teacherid, String pdfFileName) {
    boolean debug = true;
    
    try {
      Statement stmt = null;
      ResultSet rs = null;
      Connection conn = null;
      
      // Read database records
      conn = DriverManager.getConnection("jdbc:mysql://localhost/school?user=root&password=");
      String sql = "select classes.classid, enrolments.studentid, students.surname, students.firstname "
        + "from (( classes " 
        + "left join enrolments on classes.classid=enrolments.classid ) "
        + "left join students on enrolments.studentid=students.studentid ) "
        + "where classes.teacherid='"+teacherid.toUpperCase()+"' "
        + "order by classes.classid, enrolments.studentid;";
      stmt = conn.createStatement();
      rs = stmt.executeQuery(sql);
      
      // Create PDF
      FreePDF pdf = new FreePDF();
      pdf.open();
      pdf.setTopMargin(5);
      pdf.setCreator("Copyright (C) 2015 Paul Baumgarten");
      pdf.setDrawColor(0,0,0);
      pdf.setFillColor(0,0,0);
      pdf.setTextColor(0,0,0);
      pdf.setFont("arial", null,10);
      pdf.setFontSize(10);
      pdf.setXY(10,10);
      
      // Debugging grid
      if (debug) {
        pdf.setDrawColor(50,50,50);
        for (int i=0; i<30; i++) {
          pdf.Line(new Coordinate(0, i*10), new Coordinate(210, i*10)); 
        }
        for (int i=0; i<21; i++) {
          pdf.Line(new Coordinate(i*10, 0), new Coordinate(i*10, 295)); 
        }
        pdf.setDrawColor(0,0,0);
      }

      // Page Header
      String pageIdentifier = "";
      int col=0, x=0, y=0;
      
      // Process data rows      
      while (rs.next()) {
        if (! pageIdentifier.equals(rs.getString("classid"))) {
          System.out.println("Processing class: "+rs.getString("classid"));
          pdf.addPage();
          pdf.setXY(10,3);
          pdf.setFontSize(16);
          pdf.Cell(0,16,"Class " + rs.getString("classid"));
          pdf.setY( pdf.getY() + (int)(16*25.4/72.0));
          pdf.setY( pdf.getY() + 7 );
          col = 0;
          pdf.setFontSize(8);
          pageIdentifier = rs.getString("classid");
        }
        
        pdf.setX( 10+30*col );
        String imgFileName = photosFolder + "/" + rs.getString("studentid") + ".jpg.png";
        try {
          pdf.Image(imgFileName, new Coordinate(pdf.getX(), pdf.getY()), (int)(35*96/143), 35, ImageType.PNG, 0);
        } catch (FileNotFoundException e) {
          System.out.println(imgFileName);
          System.out.println("Error: "+e);
        }
        pdf.setY( pdf.getY() + 33 );
        pdf.setX( 10+30*col );
        pdf.Cell(0,10,rs.getString("surname")+", "+rs.getString("firstname"));
        pdf.setY( pdf.getY() - 33 );
        
        if (col < 5) {
          col++;
        } else if (col == 5) {
          col = 0;
          pdf.setY( pdf.getY()+43 );
        }
      }
      
      // Save PDF
      File pdfFile = new File(pdfFileName);
      pdf.output(pdfFile);
      
      // Close database
      rs.close();
      stmt.close();      
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
    
  public static void main(String[] args) {
    System.out.println("PhotoClassLists - By Paul Baumgarten 2015");
    System.out.println("Will generate photo class lists as PDF for a given teacher.");
    PhotoClassLists classListGenerator = new PhotoClassLists("photoclasslists.json");
    // Ask for teacherid
    String teacherid = IO.readInput("Enter teacherid: ").toUpperCase();
    String pdfFileName = classListGenerator.saveFolder + "/" + teacherid + ".pdf";
    System.out.println("Creating "+pdfFileName);
    classListGenerator.createPhotoClassLists(teacherid, pdfFileName);
  }

}
```

**net/paulbaumgarten/helpers/FreePDF.java**

```java
package net.paulbaumgarten.helpers;

// PDF
import net.sourceforge.javafpdf.*;
import java.io.File;
import java.io.FileNotFoundException;

public class FreePDF extends FPDF {
    public void Header() {
    }

    public void Footer() {
    }
}
```