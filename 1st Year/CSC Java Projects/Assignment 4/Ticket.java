// Creates ticket objects, which represent a car ticket, each with a unique ID and time of issue
// KDSMIL001
// 5 August 2019

import java.util.Scanner;

public class Ticket {

   public String id;
   public Time issueTime;
   
   public Ticket(Time issueTime){
      id = UIDGenerator.makeUID();
      this.issueTime = issueTime;
   }
   
   public String ID(){
      return id;
   }
   
   public Duration age(Time currentTime){
      return currentTime.subtract(issueTime);
   }
   
   public String toString(){
      return String.format("Ticket[id=%s, time=%s]", id, issueTime);
   }
   
}