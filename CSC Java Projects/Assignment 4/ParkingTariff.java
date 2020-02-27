

public class ParkingTariff{

   private TimePeriod period;
   private Money tariff;
   
   public ParkingTariff(TimePeriod period, Money tariff){
      
      this.period = period;
      this.tariff = tariff;
   }
   
   public TimePeriod getPeriod(){
   
      return this.period;
   }
   
   public Money getTariff(){
      
      return this.tariff;
   }
   
   public String toString(){
      
      String output = this.period.toString() + " : " + this.tariff.toString();
      return output;
   }
}