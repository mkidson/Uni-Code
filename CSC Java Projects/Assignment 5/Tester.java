import java.util.*;

public class Tester{
   
   public static void main(String[] args){
      
//       CalendarTime start = new CalendarTime("1/9/2019%22:00");
//       CalendarTime finish = new CalendarTime("2/9/2019%06:00");
//       Shift shift = new Shift(start, finish);
//       System.out.println(shift);
//       System.out.println(shift.start());
//       System.out.println(shift.finish());
//       System.out.println(shift.includesDate(new Date("31/8/2019")));
//       System.out.println(shift.includesDate(new Date("1/9/2019")));
//       System.out.println(shift.inWeek(new Week("35/2019")));
//       System.out.println(shift.inWeek(new Week("36/2019")));
//       System.out.println(shift.inWeek(new Week("37/2019")));
//       System.out.println(Duration.format(shift.length(), "minute"));

      Employee employee = new Employee("Sivuyile Ngesi", "01010125");
      System.out.println(employee.name());
      System.out.println(employee.UID());
      System.out.println(employee.present());
      //
      System.out.println();
      employee.signIn(new Date(1, 9, 2019), new Time(6,00));
      System.out.println(employee.present());
      employee.signOut(new Date(1, 9, 2019), new Time(18,00));
      System.out.println(employee.present());
      //
      System.out.println();
      employee.signIn(new Date(2, 9, 2019), new Time(16, 30));
      employee.signOut(new Date(3, 9, 2019), new Time(2, 30));
      //
      System.out.println();
      employee.signIn(new Date(3, 9, 2019), new Time(18,00));
      employee.signOut(new Date(4, 9, 2019), new Time(4,00));
      //
      System.out.println();
      System.out.println(employee.worked(new Date(31, 8, 2019)));
      System.out.println(employee.worked(new Date(1, 8, 2019)));
      //
      System.out.println();
      System.out.println(employee.worked(new Week(34, 2019)));
      System.out.println(employee.worked(new Week(35, 2019)));
      System.out.println(employee.worked(new Week(36, 2019)));
      //
      System.out.println();
      List<Shift> shifts = employee.get(new Date(1, 9, 2019));
      for(Shift shift : shifts) { System.out.println(shift); }
      System.out.println();
      shifts = employee.get(new Date(2, 9, 2019));
      for(Shift shift : shifts) { System.out.println(shift); }
      System.out.println();
      shifts = employee.get(new Date(3, 9, 2019));
      for(Shift shift : shifts) { System.out.println(shift); }
      //
      System.out.println();
      shifts = employee.get(new Week(35, 2019));
      for(Shift shift : shifts) { System.out.println(shift); }
      //
      System.out.println();
      System.out.println(Duration.format(employee.hours(new Week(35, 2019)), "minute"));
   }
}