//	KDSMIL001
//	31	July 2019

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class MarketPlace {

	public static void main(String[]	args) throws FileNotFoundException{
		Scanner input = new Scanner(System.in);
		
      
		//	takes	input	from user of CSV filename
		System.out.println("Enter the name of a \"Comma Separated Values\" (CSV) file: ");
		String filename =	input.nextLine();
		
		//	takes	input	of	CSV file	and creates	a Scanner object to scan through	it
		File fileToRead =	new File(filename);
		Scanner fileIn	= new	Scanner(fileToRead);
      Currency rand = new Currency("R", "ZAR", 100);
		
		
		int len = 0;
		//	checks if the file has anything in it and	then reads the	first	line and	assigns it to len
		if	(fileIn.hasNextLine()){
			len =	Integer.parseInt(fileIn.nextLine());
		}
      else{
         System.out.println("The file contains no seller data.");
         System.exit(0);
      }
      
      if (len == 0){
         System.out.println("The file contains no seller data.");
         System.exit(0);
      }
		
		//	creates an array of Seller	objects with length len
		Seller[]	sellers = new Seller[len];
		
		//	loops	and assigns	each line to a	Seller object in the	sellers array
		for (int	i=0; i<sellers.length; i++){
			String currLine =	null;
			
         // assigns the value of the next line to currLine
	   	if	(fileIn.hasNextLine()){
				currLine	= fileIn.nextLine();
			}

         // scans through the currently stored line
         Scanner lineScan = new Scanner(currLine).useDelimiter("\\s*,\\s*");
         
         // assigns each next value in the line to the corresponding Seller object
         Seller currSeller = new Seller();
         currSeller.ID = lineScan.next();
         currSeller.name = lineScan.next();
         currSeller.location = lineScan.next();
         currSeller.product = lineScan.next();
         currSeller.unit_price = new Money(lineScan.next(),	rand);
         currSeller.number_of_units = Integer.parseInt(lineScan.next());

         lineScan.close();
         
         // assigns the current Seller object to the ith entry of sellers
         sellers[i] = currSeller;
         
      }
		      
		fileIn.close();
      
      System.out.println("Enter the name of a product:");
      String prod = input.nextLine();
      
      System.out.println("Enter the number of units required:");
      int numUnits = input.nextInt();
      
      System.out.println("Enter the maximum unit price:");
      Money maxPrice = new Money(input.next(), rand);
//       String priceMax = input.nextLine();
//       maxPrice = new Money(priceMax, rand);

      int count = 0;
      
      for (int i=0; i<sellers.length; i++){
         if (prod.equals(sellers[i].product)){
            if (numUnits <= sellers[i].number_of_units){
               if ((maxPrice.compareTo(sellers[i].unit_price) >= 0)){
                  System.out.println(sellers[i].ID + " : " + sellers[i].name + " in " + sellers[i].location + " has " + sellers[i].number_of_units + " " + sellers[i].product + " for " + sellers[i].unit_price + " each.");
                  count += 1;
               }
            }
         }
      }
      
      if (count==0){
         System.out.println("None found.");
      }
      
      
      
//       catch(FileNotFoundException e){
//          System.out.println("The file contains no seller data.");
//       }
      

   input.close();
	}
}