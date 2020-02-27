// A clock that can advance by a certain amount of time and then display the new time
// KDSMIL001
// 5 August 2019


public class Clock{

   public Time currentTime;
   
   public Clock(Time time){
      currentTime = time;
   }

   public void advance(Duration timeAdd){
      currentTime = currentTime.add(timeAdd);
   }
   
   public Time examine(){
      return currentTime;
   }
}