// First Program that prints Hello World to the screen
// KDSMIL001
// 18 July 2019


public class Count {
    public int count;
    public Count(int c) {
    count = c;
    }
    public Count() {
    count = 1;
    }
   }
   class Test {
    public static void main(String[] args) {
    Count myCount = new Count();
    int times = 0;
    for (int i = 0; i < 100; i++)
    increment(myCount, times);
    System.out.println("count is " + myCount.count);
    System.out.println("times is " + times);
    }
    public static void increment(Count c, int times) {
    c.count++;
    times++;
    }
   }