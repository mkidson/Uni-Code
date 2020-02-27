

public class SoftDrink extends MenuItem {
   
   private String size;
   private String flavour;
   private String type;
   
   public SoftDrink(String itemNo, String size, String flavour, String type){
      
      super(itemNo);
      this.size = size;
      this.flavour = flavour;
      this.type = type;
   }
   
   public String toString(){
      
      return "Soft Drink: " + super.toString() + ", " + this.size + ", " + this.flavour + ", " + this.type;
   }
}