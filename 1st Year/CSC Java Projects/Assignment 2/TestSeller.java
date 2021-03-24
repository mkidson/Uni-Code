// KDSMIL001
// 28 July 2019

import java.util.Scanner;
/**
 * 
 */
public class TestSeller {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Seller sel = new Seller();
        String b = input.nextLine();
        
        System.out.println("Please enter the details of the seller.");
        System.out.print("ID: ");
        sel.ID = input.nextLine();
        
        System.out.print("Name: ");
        sel.name = input.nextLine();
        
        System.out.print("Location: ");
        sel.location = input.nextLine();
        
        System.out.print("Product: ");
        sel.product = input.nextLine();
        
        System.out.print("Price: ");
        sel.unit_price = input.nextLine();
        
        System.out.print("Units: ");
        sel.number_of_units = Integer.parseInt(input.nextLine());
        
        System.out.println("The seller has been succesfully created.");
        System.out.println("ID of the seller: " + sel.ID);
        System.out.println("Name of the seller: " + sel.name);
        System.out.println("Location of the seller: " + sel.location);
        System.out.println("The product to sell: " + sel.product);
        System.out.println("Product unit price: " + sel.unit_price);
        System.out.println("The number of available units: " + sel.number_of_units);
                
        input.close();
    }


}