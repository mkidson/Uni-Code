

public class TicketTester {
   
   public static void main(String[] args){
//       Time tOne = new Time("6:50");
//       Ticket ticket = new Ticket(tOne);
//       Time tTwo = new Time("7:19");
//       System.out.println(ticket.toString());
//       Duration d = ticket.age(tTwo);
//       System.out.println(d.intValue("minute"));
//       System.out.println(ticket.ID());
//       
//       Clock c = new Clock(new Time("13:00"));
//       Time t = c.examine();
//       System.out.println(t.toString());
//       c.advance(new Duration("minute", 75));
//       System.out.println(c.examine().toString());
      
      Register r = new Register();
      Ticket t = new Ticket(new Time("13:00"));
      String ID_One = t.ID();
      System.out.println(t.ID());
      r.add(t);
      t = new Ticket(new Time("13:18"));
      String ID_Two = t.ID();
      System.out.println(t.ID());
      r.add(t);
      System.out.println(r.contains(ID_Two));
      System.out.println(r.retrieve(ID_Two).toString());

   }
}