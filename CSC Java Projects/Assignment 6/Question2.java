import java.util.Scanner;
import java.util.ArrayList;

public class Question2 {
   
   public static void main(String[] args){
   
      Scanner keyboard = new Scanner(System.in);
      
      System.out.println("Welcome to Great International Food Court");
      
      ArrayList<MenuItem> menu = new ArrayList<MenuItem>();
      char charInput;

      do {

         System.out.println("MENU: add (P)izza, add (C)urry, add (S)oft drink, (D)elete, (L)ist, (Q)uit");
         charInput = keyboard.nextLine().charAt(0);

         switch (charInput){
            
            case 'p':
               System.out.println("Enter the menu item number");
               String pizzaItemNo = keyboard.nextLine();
               System.out.println("Enter the size");
               String pizzaSize = keyboard.nextLine();
               System.out.println("Enter the base");
               String base = keyboard.nextLine();
               System.out.println("Enter extra cheese");
               String cheese = keyboard.nextLine();
               System.out.println("Enter extra garlic");
               String garlic = keyboard.nextLine();

               menu.add(new Pizza(pizzaItemNo, pizzaSize, base, cheese, garlic));
               System.out.println("Done");
               break;
               
            case 'c':
               System.out.println("Enter the menu item number");
               String curryItemNo = keyboard.nextLine();
               System.out.println("Enter the size");
               String currySize = keyboard.nextLine();
               System.out.println("Enter the curry type");
               String curryType = keyboard.nextLine();

               menu.add(new Curry(curryItemNo, currySize, curryType));
               System.out.println("Done");
               break;
               
            case 's':
               System.out.println("Enter the menu item number");
               String drinkItemNo = keyboard.nextLine();
               System.out.println("Enter the size");
               String drinkSize = keyboard.nextLine();
               System.out.println("Enter the flavour");
               String flavour = keyboard.nextLine();
               System.out.println("Enter whether it is a bottle or can");
               String drinkType = keyboard.nextLine();

               menu.add(new SoftDrink(drinkItemNo, drinkSize, flavour, drinkType));
               System.out.println("Done");
               break;
               
            case 'd':
               System.out.println("Enter the menu item number");
               String itemNo = keyboard.nextLine();
               int index;
               boolean removed = false;
               
               for (MenuItem i : menu){
                  
                  if (i.getItemNo().equals(itemNo)){
                     index = menu.indexOf(i);
                     menu.remove(index);
                     removed = true;
                     break;
                  }
               }
               
               if (removed){
                  System.out.println("Done");
               }
               else{
                  System.out.println("Not found");
               }
               
               break;
               
            case 'l':
               for (MenuItem c : menu){
                  
                  System.out.println(c.toString());
               }
               System.out.println("Done");
               break;
            
         }
      
      } while(charInput != 'q');
      
      keyboard.close();
   }
}