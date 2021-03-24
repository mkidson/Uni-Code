

public class Plane extends Vehicle {
   
   private String company;
   private int modelNo;
   
   public Plane(String colour, int passengers, String company, int modelNo){
      
      super(passengers, colour);
      this.company = company;
      this.modelNo = modelNo;
   }
   
   public String toString(){
      
      return super.toString() + " " + this.company + " " + this.modelNo;
   }
}