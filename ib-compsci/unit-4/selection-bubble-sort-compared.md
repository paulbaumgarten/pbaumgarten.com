# Sort algorithm exercises (solutions)

## Question 1

Data set 1 Bubble sort

* comparisons: 1911
* writes: 1348

Data set 1 Selection sort

* comparisons: 1275
* writes: 100

Data set 2 Bubble sort

* comparisons: 100
* writes: 100

Data set 2 Selection sort

* comparisons: 1326
* writes: 102

```java
class Main {
  public static int[] bubbleSort(int[] data){
    int writes = 0;
    int comparisons = 0;
    boolean done = false;
    while(!done){
      done = true;
      for (int i=1; i<data.length; i++){
        comparisons++;
        if(data[i]<data[i-1]){
          done = false;
          int temp = data[i-1];
          data[i-1] = data[i];
          data[i] = temp;
          writes += 2;
        }
      }
    }
    System.out.println("comparisons: "+comparisons);
    System.out.println("writes: "+writes);
    return(data);
  };

    public static int[] selectionSort(int[] data){
        int writes = 0;
        int comparisons = 0;

        for (int i=0; i<data.length; i++){
            int indexOfLowest = i;
            for (int a=i; a<data.length; a++){
                comparisons++;
                if (data[a] < data[indexOfLowest]){
                    indexOfLowest = a;
                }
            }
            int temp = data[i];
            data[i]=data[indexOfLowest];
            writes++;
            data[indexOfLowest] = temp;
            writes++;
        }
        System.out.println("comparisons: "+comparisons);
        System.out.println("writes: "+writes);
        return(data);
    };



    public static void main(String[] args) {

      int data[] = {34, 43, 73, 88, 9, 91, 48, 10, 94, 3, 75, 87, 74, 63, 11, 36, 82, 100, 28, 68, 18, 60, 35, 81, 79, 23, 86, 41, 49, 2, 7, 83, 6, 58, 47, 39, 27, 54, 21, 12, 4, 5, 31, 46, 62, 55, 37, 57, 67, 93};
      int data2[] = {34, 43, 73, 88, 9, 91, 48, 10, 94, 3, 75, 87, 74, 63, 11, 36, 82, 100, 28, 68, 18, 60, 35, 81, 79, 23, 86, 41, 49, 2, 7, 83, 6, 58, 47, 39, 27, 54, 21, 12, 4, 5, 31, 46, 62, 55, 37, 57, 67, 93};
      int data3[] = {100, 1, 2, 3, 5, 9, 10, 11, 12, 17, 20, 23, 25, 31, 33, 35, 39, 40, 42, 43, 44, 45, 46, 47, 51, 52, 55, 56, 59, 61, 62, 63, 64, 66, 69, 70, 75, 77, 78, 79, 80, 81, 83, 86, 87, 88, 89, 92, 94, 96, 98};
      int data4[] = {100, 1, 2, 3, 5, 9, 10, 11, 12, 17, 20, 23, 25, 31, 33, 35, 39, 40, 42, 43, 44, 45, 46, 47, 51, 52, 55, 56, 59, 61, 62, 63, 64, 66, 69, 70, 75, 77, 78, 79, 80, 81, 83, 86, 87, 88, 89, 92, 94, 96, 98};
      int bubbleSortedData[] = bubbleSort(data);
      int selectionSortedData[] = selectionSort(data2);
      int bubbleSortedData2[] = bubbleSort(data3);
      int selectionSortedData2[] = selectionSort(data4);
  }

}
```

## Question 3

```java
"29/06/2009","06/06/1984","16/06/1993","23/11/1996","23/09/1986","07/07/2002","29/01/1999","13/06/1998","14/02/2005","29/08/2013","24/12/2009","04/09/2019","02/02/2020","22/10/2015","08/11/1987","23/10/2018","14/10/2015","19/02/2013","05/06/1989","21/08/1991","06/06/2005","03/02/1993","01/12/1993","01/09/1995","24/01/2018"
```

