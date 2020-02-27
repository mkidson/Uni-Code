

public class TimePeriod{

   private Duration lowerBound;
   private Duration upperBound;
   
   public TimePeriod(Duration lowerBound, Duration upperBound){
      this.lowerBound = lowerBound;
      this.upperBound = upperBound;
   }
   
   public Duration lowerBound(){
      return lowerBound;
   }
   
   public Duration upperBound(){
      return upperBound;
   }
   
//    public void setLowerBound(Duration lowerBound){
//       this.lowerBound = lowerBound;
//    }
//    
//    public void setUpperBound(Duration upperBound){
//       this.upperBound = upperBound;
//    }
   
   public boolean includes(Duration duration){
      if ((this.lowerBound.compareTo(duration)<=0)&&(this.upperBound.compareTo(duration)>0)){
         return true;
      }
      else{
         return false;
      }
   }
   
   public boolean precedes(TimePeriod other){
   
      boolean bool = false;
      if (this.upperBound.intValue("minute") <= other.lowerBound.intValue("minute")){//this.upperBound().compareTo(other.lowerBound)<=0
         bool = true;
      }
      
      return bool;
   }
   
   public boolean adjacent(TimePeriod other){
   
      boolean bool = false;
      if ((this.upperBound.compareTo(other.lowerBound)==0)||(this.lowerBound.compareTo(other.upperBound)==0)){
         bool = true;
      }
      
      return bool;
   }
   
   public String toString(){
   
      String output = "[" + Duration.format(this.lowerBound, "minute") + " .. " + Duration.format(this.upperBound, "minute") + "]";
      return output;
   }
}