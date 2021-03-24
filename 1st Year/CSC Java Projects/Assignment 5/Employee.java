
import java.util.*;

public class Employee{
   
   private String name;
   private String uid;
   private CalendarTime shiftStart;
   private CalendarTime shiftFinish;
   private List<Shift> shiftList = new ArrayList<Shift>();
   private boolean isPresent = false;
   
   public Employee(String name, String uid){
      this.name = name;
      this.uid = uid;
   }
   
   public String name(){
      return this.name;
   }
   
   public String UID(){
      return this.uid;
   }
   
   public void signIn(Date d, Time t){
      this.shiftStart = new CalendarTime(d, t);
      this.isPresent = true;
   }
   
   public void signOut(Date d, Time t){
      this.shiftFinish = new CalendarTime(d, t);
      Shift newShift = new Shift(this.shiftStart, this.shiftFinish);
      shiftList.add(newShift);
      this.isPresent = false;
   }
   
   public boolean present(){
      return this.isPresent;
   }
   
   public boolean worked(Date d){
      boolean didWork = false;
      for (Shift i:shiftList){
         if (i.includesDate(d))
            didWork = true;
      }
      return didWork;
   }
   
   public boolean worked(Week w){
      boolean didWork = false;
      for (Shift i:this.shiftList){
         if (i.inWeek(w))
            didWork = true;
      
      }
      return didWork;
   }
   
   public List<Shift> get(Date d){
      List<Shift> shiftsWorked = new ArrayList<Shift>();
      // might need a check to see if there is a shift that fell on this date, using worked method
      for (Shift i:this.shiftList){
         if (i.includesDate(d))
            shiftsWorked.add(i);
      }
      return shiftsWorked;
   }
   
   public List<Shift> get(Week w){
      List<Shift> shiftsWorked = new ArrayList<Shift>();
      // again might need a check, aka using the worked methods
      for (Shift i:this.shiftList){
         if (i.inWeek(w))
            shiftsWorked.add(i);
      }
      return shiftsWorked;
   }
   
   public Duration hours(Week w){
      Duration dur = new Duration("minute", 0);
      
      for (Shift i:this.shiftList){
         if (i.inWeek(w)){
            dur = dur.add(i.length());
         }
      }
      return dur;
   }
}