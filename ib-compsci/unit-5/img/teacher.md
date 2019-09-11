
# 2D array: Student & assessments marksbook problem

* Average overall 68.56
* Average by row 67.2 70.2 86.4 57.6 61.4
* Average by column 68.4 52.4 85.0 81.4 55.6

```java
package com.pbaumgarten.teachingnotes;

public class TwoDimensionArrayFirstEx {
    public static void main(String[] args) {
        double[][] marks = {
            {67, 50, 93, 83, 43},
            {70, 52, 96, 85, 48},
            {90, 81, 100, 93, 68},
            {55, 32, 71, 72, 58},
            {60, 47, 65, 74, 61}
        };

        // Average overall
        System.out.println("Average overall");
        double tot = 0;
        int count = 0;
        for (double[] row : marks) {
            for (double cell : row) {
                tot += cell;
                count++;
            }
        }
        System.out.println( tot / count );

        // Average by row
        System.out.println("Average by row");
        for (double[] row : marks) {
            tot = 0;
            count = 0;
            for (double cell : row) {
                tot += cell;
                count++;
            }
            System.out.println( tot / count );
        }

        // Average by column
        System.out.println("Average by column");
        for (int col=0; col<marks[0].length; col++) {
            tot = 0;
            count = 0;
            for (int row=0; row<marks.length; row++) {
                tot += marks[row][col];
                count++;
            }
            System.out.println( tot / count );
        }
    }
}
```

# 2D Array: Pattern problems

```java
package com.pbaumgarten.teachingnotes;

public class TwoDimensionArrayReview {
    public static void printArray(int[][] arr) {
        for (int i=0; i<arr.length; i++) {
            for (int j=0; j<arr[i].length; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] arr = new int[9][9];
        System.out.println("Q1");
        arr = question1(arr);
        printArray(arr);
        System.out.println("\nQ2");
        arr = question2(arr);
        printArray(arr);
        System.out.println("\nQ3");
        arr = question3(arr);
        printArray(arr);
        System.out.println("\nQ4");
        arr = question4(arr);
        printArray(arr);
//        System.out.println("Q5");
//        arr = question5(arr);
//        printArray(arr);
//        System.out.println("Q6");
//        arr = question6(arr);
//        printArray(arr);
        System.out.println("\nQ7");
        arr = question7(arr);
        printArray(arr);
        System.out.println("\nQ8");
        arr = question8(arr);
        printArray(arr);
        System.out.println("\nQ9");
        arr = question9(arr);
        printArray(arr);
//        System.out.println("Q10");
//        arr = question10(arr);
//        printArray(arr);
        System.out.println("\nQ11");
        arr = question11(arr);
        printArray(arr);
//        System.out.println("Q12");
//        arr = question12(arr);
//        printArray(arr);
        System.out.println("\nQ13");
        arr = question13(arr);
        printArray(arr);
    }
    
    public static int[][] example(int[][] arr) {
        int counter = 1;
        for (int i=0; i<arr.length; i++) {
            for (int j=0; j<arr[i].length; j++) {
                arr[i][j] = counter++;
            }
        }
        return (arr);
    }

    public static int[][] question1(int[][] arr) {
        for (int i=0; i<arr.length; i++) {
            for (int j=0; j<arr[i].length; j++) {
                arr[i][j] = j;
            }
        }
        return (arr);
    }

    public static int[][] question2(int[][] a) {
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<a[i].length; j++) {
                a[i][j] = i;
            }
        }        
        return (a);
    }

    public static int[][] question3(int[][] a) {
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<a[i].length; j++) {
                a[i][j] = (i+1)*a.length - j;
            }
        }        
        return (a);
    }

    public static int[][] question4(int[][] a) {
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<a[i].length; j++) {
                a[i][j] = (a.length-i)*a.length+j-(a.length-1);
            }
        }        
        return (a);
    }

    public static int[][] question5(int[][] a) {
        return (a);
    }

    public static int[][] question6(int[][] a) {
        return (a);
    }

    public static int[][] question7(int[][] a) {
        int counter = 1;
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<a[i].length; j++) {
                int l = a.length;
                if (i % 2 == 0) {
                    a[i][j] = counter++;
                } else {
                    a[i][l-j-1] = counter++;
                }
            }
        }        
        return (a);
    }

    public static int[][] question8(int[][] a) {
        int counter = 1;
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<a[i].length; j++) {
                int l = a.length;
                if (i % 2 == 0) {
                    a[j][i] = counter++;
                } else {
                    a[l-j-1][i] = counter++;
                }
            }
        }        
        return (a);
    }

    public static int[][] question9(int[][] a) {
        int counter = 1;
        for (int i=0; i<a.length; i++) {
            for (int j=i; j<a.length; j++) {
                a[i][j] = counter++;
            }
        }
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<i; j++) {
                a[i][j] = counter++;
            }
        }
        return (a);
    }

    public static int[][] question10(int[][] a) {
        return (a);
    }

    public static int[][] question11(int[][] a) {
        int counter = 1;
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<=i; j++) {
                a[i-j][j] = counter++;
            }
        }        
        return (a);
    }

    public static int[][] question12(int[][] a) {
        return (a);
    }

    public static int[][] question13(int[][] a) {
        int center = (int)(a.length/(int)2);
        for (int i=0; i<a.length; i++) {
            for (int j=0; j<a.length; j++) {
                //System.out.println("center = "+center+" center-i="+Math.abs(center-i)+" center-j="+Math.abs(center-j));
                if (Math.abs(center-i) > Math.abs(center-j)) {
                    a[i][j] = Math.abs(center-i);
                } else {
                    a[i][j] = Math.abs(center-j);
                }
            }
        }        
        return (a);
    }

}
```

# Stacks & queues: Static implementation

```java
public class StaticStack {
    private int[] data = new int[100];
    private int position = 0;

    public MyStack() {
    }

    public void push(int element) {
        data[position] = element;
        position++;
    }

    public int pop() {
        position--;
        return data[position];
    }

    public boolean isEmpty() {
        return (position==0);
    }

    public boolean isFull() {
        return (position==100);
    }

    public static void main(String[] args) {
        StaticStack s = new StaticStack();
        s.push( 5 );
        s.push( 16 );
        s.push( 33 );
        s.push( 42 );
        while ( ! s.isEmpty() ) {
            System.out.println( s.pop() );
        }
    }
}
```

# Stacks & queues: Exercises

```java
public class StaticStackOfString {
    private String[] data = new String[100];
    private int position = 0;
    
    public MyStackStr() {
    }
    
    public void push(String element) {
        data[position] = element;
        position++;
    }
    
    public String pop() {
        position--;
        return data[position];
    }

    public boolean isEmpty() {
        return (position==0);
    }

    public boolean isFull() {
        return (position==100);
    }
    
    public static void main(String[] args) {
        StaticStackOfString s = new StaticStackOfString();
        String src = "Hello world!";
        for (int i=0; i<src.length(); i++) {
            s.push( src.substring(i,i+1));
        }
        String result = "";
        while ( ! s.isEmpty() ) {
            result = result + s.pop();
        }
        System.out.println( result );
    }
}
```



# Binary Tree: Roll your own

```java
package com.pbaumgarten.teachingnotes;

public class MyBinaryTree {
    public class Node {    
        Node left, right;
        int data;
    
        public Node() {
            left = null;
            right = null;
            data = 0;
        }
        public Node(int n) {
            left = null;
            right = null;
            data = n;
        }
        public void setLeft(Node n) { left = n; }
        public void setRight(Node n) { right = n; }
        public Node getLeft() { return left; }
        public Node getRight() { return right; }
        public void setData(int d) { data = d; }
        public int getData() { return data; }     
    }
    
    private Node root;
    
    public MyBinaryTree() {
        root = null;
    }

    public boolean isEmpty() { 
        return root == null; 
    }

    /* public facing function to insert */
    public void insert(int data) { 
        root = insert(root, data); 
    }

    /* prviate implementation of insert */
    private Node insert(Node node, int data)
    {
        if (node == null) {
            node = new Node(data);
        } else {
            if (node.getData() > data) {
            node.left = insert(node.left, data);
            } else {
            node.right = insert(node.right, data);
            }
        }
        return node;
    }     

    /* public facing function to count nodes */
    public int countNodes() { 
        return countNodes(root); 
    }

    /* private implementation of count */
    private int countNodes(Node r)
    {
        if (r == null) {
            return 0;
        } else {
            int l = 1;
            l += countNodes(r.getLeft());
            l += countNodes(r.getRight());
            return l;
        }
    }

    /* public facing search, returns boolean indicating if found */
    public boolean search(int val) { 
        return search(root, val); 
    }

    /* private implementation of search */
    private boolean search(Node r, int val) {
        if (r.getData() == val) {
            return true;
        }    
        if (r.getLeft() != null) {
            if (search(r.getLeft(), val)) {
                return true; 
            }
        }
        if (r.getRight() != null) {
            if (search(r.getRight(), val)) {
                return true;
            }
        }
        return false;         
    }

    /* Functions for inorder traversal */
    public void inorder() { 
        inorder(root); 
    }

    private void inorder(Node r) {
        if (r != null) {
            inorder(r.getLeft());
            System.out.print(r.getData() +" ");
            inorder(r.getRight());
        }
    }

    /* Functions for preorder traversal */
    public void preorder() { 
        preorder(root); 
    }

    private void preorder(Node r) {
        if (r != null) {
            System.out.print(r.getData() +" ");
            preorder(r.getLeft());             
            preorder(r.getRight());
        }
    }

    /* Functions for postorder traversal */
    public void postorder() { 
        postorder(root); 
    }

    private void postorder(Node r) {
        if (r != null) {
            postorder(r.getLeft());             
            postorder(r.getRight());
            System.out.print(r.getData() +" ");
        }
    }

    public static void main(String[] args) {
        MyBinaryTree bt = new MyBinaryTree();
        bt.insert( 13 );
        bt.insert( 4 );
        bt.insert( 2 );
        bt.insert( 15 );
        bt.insert( 100 );
        bt.insert( 1000 );
        bt.insert( 222 );
        bt.insert( 23 );
        bt.insert( 7 );
        bt.insert( 8 );
        System.out.println("Node count");
        System.out.println( bt.countNodes() );
        System.out.println("Pre order traversal");
        bt.preorder();
        System.out.println("In order traversal");
        bt.inorder();
        System.out.println("Post order traversal");
        bt.postorder();
    }
}
```
