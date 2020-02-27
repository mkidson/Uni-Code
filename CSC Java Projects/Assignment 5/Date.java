import java.util.regex.Pattern;
import java.util.Scanner;
/**
 * A simple representation of dates in the Gregorian calendar.
 * 
 * @author Stephan Jamieson
 * @version 27/3/2011
 */
public class Date implements Comparable<Date> {

    private final int day;
    private final int month;
    private final int year;
    
    public final static Date GREGORIAN_ADOPTION = new Date(15, 10, 1582);
    
    /**
     * Create a Date representing day <em>d</em>, month <em>m</em>, and year <em>y</em>.
     */
    public Date(final int d, final int m, final int y) {
        if (!isValidDate(d, m, y)) {
            throw new IllegalArgumentException("Date:Date("+d+", "+m+", "+y+"): not a legitimate date.");
        }
        else {
            day = d;
            month = m;
            year = y;
        }   
    }    
        
    /**
     * Create a Date that represents the same day, month and year as the other.
     */
    public Date(final Date other) {
        this.day = other.getDay();
        this.month = other.getMonth();
        this.year = other.getYear();
    }
    
    /**
     * Create a Date from a string of the form "[d]d/[m]m/yyyy".
     */
    public Date(final String string) {
        final String ERR_STR = "Date:Date("+string+"): ";
        if (!string.matches("\\d{1,2}/\\d{1,2}/\\d\\d\\d\\d")) {
            throw new IllegalArgumentException(ERR_STR+"expected date string in format [d]d/[m]m/yyyy.");
        }
        else {
            final Scanner scanner = new Scanner(string.trim()).useDelimiter("/");
            this.day = scanner.nextInt();
            this.month = scanner.nextInt();
            this.year = scanner.nextInt();
            if (!isValidDate(this.day, this.month, this.year)) {
                throw new IllegalArgumentException(ERR_STR+"not a legitimate date.");
            }
        }
    }
    
    /**
     * Obtain the day of the month.
     */
    public int getDay() { return day; }
    
    /**
     * Obtain the month of the year.
     */
    public int getMonth() { return month; }
    
    /**
     * Obtain the year.
     */
    public int getYear() { return year; }

    /**
     * Obtain the day of the week on which this date falls in the form of an integer where 1 is Monday and 7 is Sunday.
     */
    public int getWeekday() {
        return Date.getWeekdayISO(this.getDay(), this.getMonth(), this.getYear());
    }
        
    /**
     * Obtain the time from the other date to this date.
     */
    public Duration subtract(final Date other) {
        final int daysOther=Date.dayOfYear(other);
        int daysThis=0;
        for (int year=other.getYear(); year<this.getYear(); year++) {
            daysThis=daysThis+daysInYear(year);
        }
        daysThis=daysThis+Date.dayOfYear(this);
        return new Duration("day", daysThis-daysOther);
    }

    /**
     * Obtain the Date that occurred the given duration before this date.
     */
    public Date subtract(final Duration duration) {
        if (duration.isNegative()) {
            return this.add(duration.abs());
        }
        else {
            long days = duration.intValue("day");
            //
            Date temp = new Date(this.getDay(), this.getMonth(), this.getYear());
            while (days>=Date.dayOfYear(temp)) {
                days = days-Date.dayOfYear(temp);
                temp = new Date(31, 12, temp.getYear()-1);
            }
            while (days>temp.getDay()) {
                days = days-temp.getDay();
                temp = new Date(Date.daysInMonth(temp.getMonth()-1, temp.getYear()), temp.getMonth()-1, temp.getYear());
            }
            // Construction of new Date will throw exception if precedes 15th of October 1582 (the date that
            // the Gregorian calendar was first adopted (by some countries).
            try {
                temp = new Date((int)(temp.getDay()-days), temp.getMonth(), temp.getYear());
            }
            catch (IllegalArgumentException illArg) {
                throw new IllegalArgumentException("Date:subtract("+duration+"): result precedes Gregorian calendar adoption");
            }
            return temp;
        }
    }
    
    /**
     * Obtain the Date that occurs a duration period after this date.
     */
    public Date add(final Duration duration) {
        if (duration.isNegative()) {
            return this.subtract(duration.abs());
        }
        else {
            long days = duration.intValue("day");
            //
            Date temp = new Date(getDay(), getMonth(), getYear());
            while (days>Date.daysToEndOfYear(temp)) {
                days=days-(Date.daysToEndOfYear(temp)+1);
                temp = new Date(1, 1, temp.getYear()+1);
            }
            while (days>Date.daysToEndOfMonth(temp)) {
                days = days-(Date.daysToEndOfMonth(temp)+1);
                temp = new Date(1, temp.getMonth()+1, temp.getYear());
            }
            temp = new Date((int)(temp.getDay()+days), temp.getMonth(), temp.getYear());
            return temp;
        }
    }
    
    
    /** 
     * Obtain the number of months after this date that other occurs.
     */
    public double getMonthsTo(final Date other) {
        return (other.getYear()-this.getYear())*12-this.getMonth()+other.getMonth()
            -this.getDay()/(double)Date.daysInMonth(this.getMonth(), this.getYear())
            +other.getDay()/(double)Date.daysInMonth(other.getMonth(), other.getYear());
    }
    
    /**
     * Obtain the number of years after this date that other occurs.
     */
    public double getYearsTo(final Date other) {
        return other.getYear()-this.getYear()-Date.dayOfYear(this)/(double)daysInYear(this.getYear())
            +Date.dayOfYear(other)/(double)daysInYear(other.getYear());
    }
    
    /**
     * Obtain the Date that immediately follows this.
     */
    public Date next() {
        if (Date.daysToEndOfMonth(this)>0) {
            return new Date(this.getDay()+1, this.getMonth(), this.getYear());
        }
        else if (this.getMonth()<12) {
            return new Date(1, this.getMonth()+1, this.getYear());
        }       
        else {
            return new Date(1, 1, this.getYear());
        }
    }
    
    /**
     * Compare this Date to other date, returning a -ve number if this precedes other, a zero if they are coincicent, and a positive number if other precedes this.
     */
    public int compareTo(final Date other) {
        int test = this.getYear()-other.getYear();
        if (test==0) {
            test = this.getMonth()-other.getMonth();
        }
        if (test==0) {
            test = this.getDay()-other.getDay();
        }
        return test;
    }
    
    /**
     * Obtain a hashcode for this Date object.
     */
    public int hashCode() {
        return this.getYear()*365+this.getMonth()*30+this.getDay();
    }
    
    /**
     * Returns true if o is a Date object that represents the same date as this, and false otherwise.
     */
    public boolean equals(Object o) {
        if (!(o instanceof Date)) {
            return false;
        }
        else {
            final Date other = (Date)o;
            return this.getDay()==other.getDay()&&this.getMonth()==other.getMonth()&&this.getYear()==other.getYear();
        }
    }
    
    /**
     * Obtain a String representation of this date in the form [d]d/[m]m/yyyy.
     */
    public String toString() {
        return this.getDay()+"/"+this.getMonth()+"/"+this.getYear();
    }
    
    public static boolean validFormat(final String string) {
        return Pattern.matches("\\s*\\d{1,2}/\\d{1,2}/\\d{4}\\s*", string);
    }
    
    private static int dayOfYear(final Date date) {
        return Date.dayOfYear(date.getDay(), date.getMonth(), date.getYear());
    }

    private static int[] daysToMonth = { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365};

    private static int dayOfYear(final int day, final int month, final int year) {
        int result = Date.daysToMonth[month-1]+day;
        if (Date.isLeapYear(year)&&month>=3) {
            result = result+1;
        }
        return result;
    }
    
    private static int daysToEndOfYear(final Date date) {
        return Date.daysToEndOfYear(date.getDay(), date.getMonth(), date.getYear());
    }
    
    private static int daysToEndOfYear(final int day, final int month, final int year) {
        return Date.daysInYear(year)-Date.dayOfYear(day, month, year);
    }
    
    
    private static int daysToEndOfMonth(final Date date) {
        return Date.daysToEndOfMonth(date.getDay(), date.getMonth(), date.getYear());
    }
    
    private static int daysToEndOfMonth(final int day, final int month, final int year) {
        return Date.daysInMonth(month, year)-day;
    }
    
    private static int daysInMonth(final int month, final int year) {
        if (month==9 || month==4 || month==6 || month==11) { return 30; }
        else if (month==2 && Date.isLeapYear(year)) { return 29; }
        else if (month==2 && !Date.isLeapYear(year)) { return 28; }
        else { return 31; }
    }

    private static int daysInYear(final int year) {
        if (Date.isLeapYear(year)) {
            return 366;
        }
        else {
            return 365;
        }
    }
    
    private static boolean isLeapYear(final int year) {
        return (year%4==0 && year%100!=0 || year%400==0);
    }

    private static boolean isValidDate(final int day, final int month, final int year) {
        return year>0&&month>0&&month<13&&day>0&&day<=daysInMonth(month, year);
    }
    
    private static int getWeekdayISO(final int day, final int month, final int year) {
        // http://en.wikipedia.org/wiki/Zeller's_congruence
        final int q = day;
        final int m = month<3 ? month+12 : month;
        final int Y = month<3 ? year-1 : year;
        
        final int h = (q+((m+1)*26)/10+Y+Y/4+6*(Y/100)+(Y/400))%7;
        // Convert to ISO weekday number
        final int weekday = (5+h)%7+1;
        return weekday;        
    }
}
