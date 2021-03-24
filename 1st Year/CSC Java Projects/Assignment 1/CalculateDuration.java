// Takes two time inputs in 24 hour format and returns the amount of minutes after time A that time B occurs
// KDSMIL001
// 21 July 2019

import java.util.Scanner;


public class CalculateDuration {

    public static void main(String[] args) {

        // Creates the input object of the Scanner class that takes an input
        Scanner input = new Scanner(System.in);

        // Prints instructions and assigns the inputs to two variables
        System.out.println("Enter time A: ");
        String t1 = input.next();
        System.out.println("Enter time B: ");
        String t2 = input.next();
        
        // Declaring the variables using the Time and Duration classes
        Time time1 = new Time(t1);
        Time time2 = new Time(t2);
        Duration dur = time2.subtract(time1);

        // Prints the final message to screen
        System.out.println("The time " + time2 + " occurs " + dur.intValue("minute") + " minutes after the time " + time1 + ".");
        
        
        input.close();
    }
}
