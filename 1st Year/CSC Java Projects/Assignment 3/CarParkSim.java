import java.util.Scanner;
/**
 * The CarParkSim class contains the main car park simulation method.
 * It creates and manipulates the main objects, and handles user I/O.
 *
 * @author Stephan Jamieson and Miles Kidson
 * @version 14/7/2019
 */
public class CarParkSim {
        
    public static void main(final String[] args) {
        final Scanner keyboard = new Scanner(System.in);
        // Declare variables to store a Clock and a Register object, create the relevant objects and assign them.
        Time timeStart = new Time("00:00");
        Clock clock = new Clock(timeStart);
        Register reg = new Register();
        
        System.out.println("Car Park Simulator");
        // Print current time.
        System.out.println("The current time is " + clock.examine() + ".");
        System.out.println("Commands: advance {minutes}, arrive, depart, quit.");
        System.out.print(">");
        String input = keyboard.next().toLowerCase();
        while (!input.equals("quit")) {
            if (input.equals("advance")) {
                // Advance the clock, print the current time. 
                int advanceDuration = Integer.parseInt(keyboard.next());
                clock.advance(new Duration("minute", advanceDuration));
                System.out.println("The current time is " + clock.examine() + ".");
            }
            else if (input.equals("arrive")) {
                // Create a new ticket, add it to the register, print details of ticket issued.
                Ticket ticket = new Ticket(clock.examine());
                reg.add(ticket);
                System.out.println("Ticket issued: " + ticket.toString() + ".");
            }
            else if (input.equals("depart")) {
                // Determine if ticket is valid, i.e. in the register.
                // If not, print error message.
                // If yes, retreive it, calculate duration of stay and print it.
                String inputID = keyboard.next();
                if (reg.contains(inputID)){
                    Ticket currTicket = reg.retrieve(inputID);
                    long totMinutes = currTicket.age(clock.examine()).intValue("minute");
                    int ageHours = (int)(totMinutes/60.0);
                    int ageMinutes = (int)(totMinutes-(ageHours*60));
                    System.out.println("Ticket details: " + currTicket.toString() + ".");
                    System.out.println("Current time: " + clock.examine() + ".");
                    System.out.println("Duration of stay: " + ageHours + " hours " + ageMinutes + " minutes.");
                }
                else{
                    System.out.println("Invalid ticket ID.");
                }
            }
            else {
                System.out.println("That command is not recognised.");
                System.out.println("Commands: advance <minutes>, arrive, depart, quit.");
            }            
            System.out.print(">");
            input = keyboard.next().toLowerCase();
        }            
        System.out.println("Goodbye.");
    }
    

}

