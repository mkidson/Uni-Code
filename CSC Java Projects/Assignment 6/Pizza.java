

public class Pizza extends MenuItem {
   
   private String size;
   private String base;
   private String cheese;
   private String garlic;
   
   public Pizza(String itemNo, String size, String base, String cheese, String garlic){
      
      super(itemNo);
      this.size = size;
      this.base = base;
      this.cheese = cheese;
      this.garlic = garlic;
   }
   
   public String toString(){
   
      return "Pizza: " + super.toString() + ", " + this.size + ", " + this.base + ", " + this.cheese + ", " + this.garlic;
   }
}