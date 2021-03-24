

public class TariffTable{

   private ParkingTariff[] table;
   private int currTablePosition = 0;

   public TariffTable(int maxSize){
      
      table = new ParkingTariff[maxSize];
   }
   
   public void addTariff(TimePeriod period, Money tariff){
      
      ParkingTariff currTariff = new ParkingTariff(period, tariff);
      
      
      // Checks if the entry directly follows the previous entry, if this is the first entry, it just enters it
      if (currTablePosition == 0){
         this.table[currTablePosition] = currTariff;
         currTablePosition++;
      }
      else if ((table[currTablePosition-1].getPeriod().precedes(currTariff.getPeriod()))&&(currTariff.getPeriod().adjacent(table[currTablePosition-1].getPeriod()))){
         this.table[currTablePosition] = currTariff;
         currTablePosition++;
         
      }
      else{
//          System.out.println("oopsie");
         throw new IllegalArgumentException("Tariff periods must be adjacent.");
      }
      
   }
   
   public Money getTariff(Duration lengthOfStay){
      
      Money x = new Money("R0", new Currency("R", "ZAR", 100));
      for (int i=0;i<currTablePosition;i++){
         if (this.table[i].getPeriod().includes(lengthOfStay)){
            x = this.table[i].getTariff();
         }
         else{
            continue;
         }
      }
      
      return x;
   }
   
   public String toString(){
   
      String output = "";
      for (int i=0;i<currTablePosition;i++){
         
         if (i==currTablePosition-1){
            output = output + this.table[i].toString();
         }
         else{
            output = output + this.table[i].toString() + "\n";
         }
         
      }
      
      return output;
   }
      
}