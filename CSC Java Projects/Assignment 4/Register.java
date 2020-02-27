// Creates an array which holds all the ticket objects
// KDSMIL001
// 6 August 2019


public class Register{
   
   Ticket[] tickets;
   int numTickets;
   
   public Register(){
      tickets = new Ticket[100];
      numTickets = 0;      
   }

   public void add(Ticket ticket){
      tickets[numTickets] = ticket;
      numTickets++;
   }
   
   public boolean contains(String ticketID){
      
      boolean doesContain = false;
      for (int i=0;i<numTickets;i++){
         if (tickets[i].ID().equals(ticketID)){
            doesContain = true;
            break;
         }
      }

      return doesContain;
   }
   
   public Ticket retrieve(String ticketID){
      
      int ticketIndex = 0;
      for (int c=0;c<=numTickets;c++){
         if (tickets[c].ID().equals(ticketID)){
            ticketIndex = c;
            break;
         }
      }
      
      return tickets[ticketIndex];
   }
}