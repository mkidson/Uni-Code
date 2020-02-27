// Sums a load of inputted Rand numbers and prints it
// KDSMIL001
// 24-07-19

import java.util.Scanner;

/**
 * Sums a bunch of inputted Rand values and outputs the final value
 */
public class SumCosts {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Currency rand = new Currency("R", "ZAR", 100);

        // Asks for input 
        System.out.println("Enter an amount or '[D]one' to print the sum and quit:");
        String str = input.next();
        
        // Initialises the Money object called totalAmount
        Money totalAmount = new Money("R0", rand);

        // Checks if the inputted string contains 'D and if it does, it runs the loop'
        while (!str.contains("D")) {

            
            // creates a Money object called amount that stores the current amount and then adds it to the totalAmount
            Money amount = new Money(str, rand);
            totalAmount = totalAmount.add(amount);
            
            // Asks for another input
            System.out.println("Enter an amount or '[D]one' to print the sum and quit:");
            str = input.next();
        }
        
        // Prints out the total and closes the input object
        System.out.println("Total: " + totalAmount);
        input.close();
    }
}