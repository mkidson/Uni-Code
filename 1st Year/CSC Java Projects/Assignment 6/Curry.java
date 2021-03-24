

public class Curry extends MenuItem {
   
   private String size;
   private String type;
   
   public Curry(String itemNo, String size, String type){
      
      super(itemNo);
      this.size = size;
      this.type = type;
   }
   
   public String toString(){
      
      return "Curry: " + super.toString() + ", " + this.size + ", " + this.type;
   }
}