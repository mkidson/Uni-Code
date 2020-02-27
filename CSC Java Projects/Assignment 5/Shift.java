

public class Shift{

   private CalendarTime start;
   private CalendarTime finish;
   
   public Shift(CalendarTime start, CalendarTime finish){
      this.start = start;
      this.finish = finish;
   }
   
   public CalendarTime start(){
      return this.start;
   }
   
   public CalendarTime finish(){
      return this.finish;
   }
   
   public boolean inWeek(Week w){
      boolean inWeek = false;
      if (w.includes(start.date()))
         inWeek = true;
      
      return inWeek;
   }
   
   public boolean includesDate(Date date){
      boolean includesDate = false;
      if ((start.date().equals(date))||(finish.date().equals(date)))
         includesDate = true;
         
      return includesDate;
   }
   
   public Duration length(){
      return this.finish.subtract(this.start);
   }
   
   public String toString(){
      String returnString = start.toString() + " - " + finish.toString();
      return returnString;
   }
}