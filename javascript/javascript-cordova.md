<!-- TITLE: Cordova -->
<!-- SUBTITLE: A reference guide to using Cordova to make apps -->

# Install & setup
There are a lot of packages you need to install to get Cordova up and running. Rather than trying to recreate thorough instructions here that will be out of date as soon as I click save, I'll give you a checklist and links to the relevant setup guides.

## Further documentation

* https://cordova.apache.org/#getstarted
* https://cordova.apache.org/docs/en/latest/guide/platforms/android/index.html
* https://cordova.apache.org/docs/en/latest/guide/platforms/ios/index.html

## Installation checklist:

### Node.js

https://nodejs.org/en/download/

### Cordova

Open a command prompt or Terminal, and type 

```bash
$ sudo npm cache clean -f
$ sudo npm install -g n
$ sudo n stable
$ sudo npm install -g cordova
$ cordova -v
```

### Java SE Development Kit 8

https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

### Android Studio

https://developer.android.com/studio/

### Android SDK

After installing the Android SDK, you must also install the packages for whatever API level you wish to target. It is recommended that you install the highest SDK version that your version of cordova-android supports (see Requirements and Support).

Open the Android SDK Manager (run sdkmanager from the terminal) and make sure the following are installed:

* Android Platform SDK for your targeted version of Android
* Android SDK build-tools version 19.1.0 or higher
* Android Support Repository (found under "Extras")
* See Android's documentation on [Installing SDK Packages](https://developer.android.com/studio/intro/update) for more details.

### Cradle

I didn't have to install this manually. I think it came with Android Studio.

### Set environment variables

Cordova's CLI tools require some environment variables to be set in order to function correctly. The CLI will attempt to set these variables for you, but in certain cases you may need to set them manually. The following variables should be updated:

Set the `JAVA_HOME` environment variable to the location of your JDK installation

Set the `ANDROID_HOME` environment variable to the location of your Android SDK installation

It is also recommended that you add the Android SDK's tools, tools/bin, and platform-tools directories to your `PATH`

* For OS X and Linux

Modify the ~/.bash_profile file. To set an environment variable, add a line that uses export like so (substitute the path with your local installation):

```bash
$ export ANDROID_HOME=/Development/android-sdk/
```

To update your PATH, add a line resembling the following (substitute the paths with your local Android SDK installation's location):

```bash
$ export PATH=${PATH}:/Development/android-sdk/platform-tools:/Development/android-sdk/tools
```

Reload your terminal to see this change reflected or run the following command:

```bash
$ source ~/.bash_profile
```

* For Windows

These steps may vary depending on your installed version of Windows. Close and reopen any command prompt windows after making changes to see them reflected. Click on the Start menu in the lower-left corner of the desktop In the search bar, search for Environment Variables and select Edit the system Environment Variables from the options that appear. In the window that appears, click the Environment Variables button. To create a new environment variable: Click New... and enter the variable name and value To set your PATH: Select the PATH variable and press Edit. Add entries for the relevant locations to the PATH. For example (substitute the paths with your local Android SDK installation's location):

```
C:\Users\[your user]\AppData\Local\Android\Sdk\platform-tools
C:\Users\[your user]\AppData\Local\Android\Sdk\tools
```

# Sample Android app
### Create new project

Verify your Node and Cordova install:

```bash
$ node -v
$ cordova -v
```

Terminal commands: 

```bash
$ mkdir ~/projects/cordova.nfc-demo
$ cordova create nfc-demo 
$ cd nfc-demo
$ cordova platform add android
$ cordova platform ls
```

Example output:

```text
Installed platforms:
  android 6.2.3
```

Terminal commands:

```bash
$ cordova requirements
```

Example output:

```text
Requirements check results for android:
Java JDK: installed 1.8.0
Android SDK: installed true
Android target: installed android-25,android-23
Gradle: installed /Applications/Android Studio.app/Contents/gradle/gradle-3.2/bin/gradle
```

Terminal commands:

```bash
$ cordova plugin add phonegap-nfc
$ cordova plugin ls
```

Example output:

```text
cordova-plugin-whitelist 1.3.3 "Whitelist"
phonegap-nfc 1.0.3 "NFC"
```

### Fix Gradle for Java 8

As of 01.10.2018, the `phonegap-nfc` plugin has a [bug](https://github.com/chariotsolutions/phonegap-nfc/issues/332) that attempts to use Java 8 code with a Java 6 configuration. To fix, you need to edit the file `platforms/android/build.gradle`.

* Add the `jackOptions` and change the `compileOptions` to the relevant sections of the file as shown below:

```
android {
    defaultConfig {
        jackOptions {
            enabled true
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
```

### www/index.html

```html
<html>
    <head>
        <!--
        Customize this policy to fit your own app's needs. For more guidance, see:
            https://github.com/apache/cordova-plugin-whitelist/blob/master/README.md#content-security-policy
        Some notes:
            * gap: is required only on iOS (when using UIWebView) and is needed for JS->native communication
            * https://ssl.gstatic.com is required only on Android and is needed for TalkBack to function properly
            * Disables use of inline scripts in order to mitigate risk of XSS vulnerabilities. To change this:
                * Enable inline JS: add 'unsafe-inline' to default-src
        -->
        <meta http-equiv="Content-Security-Policy" content="default-src 'self' data: gap: https://ssl.gstatic.com 'unsafe-eval'; style-src 'self' 'unsafe-inline'; media-src *; img-src 'self' data: content:;">
        <meta name="format-detection" content="telephone=no">
        <meta name="msapplication-tap-highlight" content="no">
        <meta name="viewport" content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width">
        <link rel="stylesheet" type="text/css" href="css/index.css">
        <title>Hello World</title>
    </head>
    <body>
        <div class="app">
            <p>Welcome</p>
        </div>
        <script type="text/javascript" src="cordova.js"></script>
        <script type="text/javascript" src="js/index.js"></script>
    </body>
</html>
```

### www/js/index.js

```js
    
function toHexString(byteArray) {
  return byteArray.map(function(byte) {
    return ('0' + (byte & 0xFF).toString(16)).slice(-2);
  }).join('');
}    
    
function message( msg ) {
    document.querySelector(".app").innerHTML += "<p>"+msg+"</p>\n";
}

function onTagPresented(e) {
    message("[onTagPresented]");
    console.log("[onTagPresented]");
    if (e.tag) {
        var tagid = toHexString(e.tag.id);
        console.log("[tag id] "+tagid);
        console.log(e);
        message(tagid)
    } else {
        console.log("Error reading tag");
        message("Error reading tag");
    }
}

function main() {
    message("[main]");
    if (typeof nfc !== 'undefined') { // NFC is enabled on our device
        message("[listener added]");
        nfc.addNdefListener(
            onTagPresented, 
            function(){message("NDEF successful");}, 
            function(){message("failed");}
        );
        nfc.addTagDiscoveredListener(
            onTagPresented, 
            function(){message("non-NDEF successful");}, 
            function(){message("failed");}
        );
        nfc.addMimeTypeListener('text/pg',
            onTagPresented,
            function(){message("NDEF mime tags with type text/pg successful");},
            function(){message("failed");}
            );
    } else {
        message("nfc not enabled on this device");
    }
}
    
document.addEventListener('deviceready', main, false);
```

### www/css/index.css

(I cleaned out most of the default stuff that the "empty project" puts in and just used this)

```css
body {
    background-color:#E4E4E4;
    font-family:'HelveticaNeue-Light', 'HelveticaNeue', Helvetica, Arial, sans-serif;
    font-size:12px;
    height:100%;
    margin:0px;
    padding:0px;
}
```

### Build and run

On your phone:

* Enable developer mode ([source](https://www.digitaltrends.com/mobile/how-to-get-developer-options-on-android/))
  * If using stock Android, go to Settings > About phone > Build number. 
  * On a Samsung Galaxy device, go to Settings > About device > Build number. 
  * On an HTC device, go to Settings > About > Software information > More > Build number. 
  * On an LG device, go to Settings > About phone > Software info > Build number.
  * Tap Build number seven times. After the first few taps, you should see the steps counting down until you unlock the developer options. Once activated, you will see a message that reads, “You are now a developer!”
  * Go back to Settings, where you’ll find a Developer options entry in the menu.
* Open developer settings, enable USB debugging
* Open connection settings, enable NFC

```bash
$ cordova build android
$ cordova run android
```



