

public class Tester{
 
  public static void main(String[] args){
      
      final TimePeriod pOne = new TimePeriod(new Duration("hour", 1), new Duration("hour", 2));
      final TimePeriod pTwo = new TimePeriod(new Duration("hour", 2), new Duration("hour", 3));
      final TimePeriod pThree = new TimePeriod(new Duration("hour", 3), new Duration("hour", 4));
      
      System.out.printf("%s\n%s\n%s\n", pOne, pTwo, pThree);
      
      System.out.println(pOne.includes(new Duration("minutes", 59)));
      System.out.println(pOne.includes(new Duration("minutes", 60)));
      System.out.println(pOne.includes(new Duration("minutes", 119)));
      System.out.println(pOne.includes(new Duration("minutes", 120)));
      
      System.out.println(pOne.precedes(pThree));
      System.out.println(pTwo.precedes(pOne));
      System.out.println(pTwo.adjacent(pOne));
      System.out.println(pOne.adjacent(pThree));
      
//       final Currency currency = new Currency("R", "ZAR", 100);
//       final TimePeriod pOne = new TimePeriod(new Duration("hour", 1), new Duration("hour", 2));
//       final TimePeriod pTwo = new TimePeriod(new Duration("hour", 2), new Duration("hour", 3));
//       final TariffTable tariffTable = new TariffTable(2);
//       
//       tariffTable.addTariff(pOne, new Money("R2", currency));
//       tariffTable.addTariff(pTwo, new Money("R5", currency));
//       
//       System.out.println(tariffTable);
//       System.out.println(tariffTable.getTariff(new Duration("minute", 65)));
//       System.out.println(tariffTable.getTariff(new Duration("hour", 2)));

   }
}