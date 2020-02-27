

public class Car extends Vehicle {

   private int doors;
   
   public Car(String colour, int passengers, int doors){
      
      super(passengers, colour);
      this.doors = doors;
   }
   
   public String toString(){
      
      return super.toString() + " " + this.doors + " doors";
   }
}