import java.util.regex.Pattern;
import java.util.NoSuchElementException;
import java.util.Scanner;
/**
 * The Week class represents ISO weeks. 
 * https://en.wikipedia.org/wiki/ISO_week_date
 * 
 * A Week comprises a number and year i.e. the number of the week in that year. 
 * 
 * Weeks start on a Monday. The first Week of a year is the one in which the first Thursday of the year falls. 
 * 
 * @author Stephan Jamieson
 * @version 27/3/2011
 */
public class Week implements Comparable<Week> {

    private final int number;
    private final int year;
    
    /**
     * Create a Week object representing the <em>n</em>th week in year <em>y</em>. 
     */
    public Week(final int n, final int y) {
        this.number = n;
        this.year = y;
    }
    
    /**
     * Create a Week object from a string of the form "&lt;number&gt;/&lt;year&gt;" where "&gt;number&lt;"
     * is a number of up to two digits, and "&gt;year&lt;" is a 4-digit number.
     */
    public Week(final String string) {
        final Scanner scanner = new Scanner(string.trim()).useDelimiter("/");
        try {
            this.number = scanner.nextInt();
            this.year = scanner.nextInt();
            if (this.number<0 || this.number>Week.weeksInYearISO(this.year)) {
                throw new IllegalArgumentException("Week: week number out of range.");
            }
        }
        catch (NoSuchElementException noSucElExcep) {
            throw new IllegalArgumentException("Week format: \"[d]d/dddd\"");
        }
    }
    
    /**
     * Obtain the Week number.
     */
    public int number() { return number; }
    
    /**
     * Obtain the year.
     */
    public int year() { return year; }
    
    /** 
     * Obtain the date for Monday of this week.
     */
    public Date begin() {
        return Week.startOfWeekISO(this.number(), this.year());
    }
    
    /**
     * Obtain the date for Sunday of this week.
     */
    public Date end() {
        return begin().add(new Duration("day", 6));
    }
    
    /**
     * Determine whether the given date falls within this week.
     */
    public boolean includes(final Date date) {
        return begin().compareTo(date)<=0&&date.compareTo(end())<=0;
    }
    
    /**
     * Returns true if <em>o</em> is a Week object that represents the same ISO week as this object.
     */
    public boolean equals(final Object o) {
        if (!(o instanceof Week)) {
            return false;
        }
        else {
            final Week other = (Week)o;
            return this.number()==other.number()&&this.year()==other.year();
        }
    }
    
    /**
     * Compare this week to other week. Returns a -ve value if this Week precedes the other Week, zero if they represent the same 
     * week, and a +ve value if the other Week precedes this.
     */
    public int compareTo(final Week other) {
        int result = this.year()-other.year();
        if (result==0) {
            result= this.number()-other.number();
        }
        return result;
    }
        
    /**
     * Obtain a hash code for this object.
     */
    public int hashCode() {
        int result = 17;
        result = 37*result+number();
        result = 37*result+year();
        return result;
    }
       
    /**
     * Obtain a String representation of this Week of the form "&lt;number&gt;/&lt;year&gt;".
     */
    public String toString() {
        return number+"/"+year;
    }

    
    /**
     * Obtain the date for the Monday of the first week of the given year.
     */
    public static Date dayOneISO(final int year) {
        final Date firstJan = new Date(1, 1, year);
        final int dayOfWeek = firstJan.getWeekday();
        if (dayOfWeek==1) {
            return firstJan;
        }
        else if (dayOfWeek>1&&dayOfWeek<5) {
            return new Date(31-dayOfWeek+2, 12, year-1);
        }
        else {
            assert dayOfWeek>4&&dayOfWeek<8;
            return new Date(9-dayOfWeek, 1, year);
        }
    }
    
    private static int dayOfYearISO(final Date date) {
        final Date dayOne = dayOneISO(date.getYear());
        return (int)date.subtract(dayOne).intValue("day");
    }
    
    /**
     * Obtain the number of days in this year according to the ISO week date system i.e. weeksInYearISO(year)*7.
     */
    public static int daysInYearISO(final int year) {
        return (int)dayOneISO(year+1).subtract(dayOneISO(year)).intValue("day");
    }
    
    /**
     * Obtain the number of weeks in this year according to the ISO week date system.
     */
    public static int weeksInYearISO(final int year) {
        return daysInYearISO(year)/7;    
    }
    
    /**
     * Obtain the date for Monday of the ISO week with the given number and year.
     */
    public static Date startOfWeekISO(final int weekNumber, final int year) {
        return dayOneISO(year).add(new Duration("week", weekNumber-1));
    }
    
    /**
     * Obtain the Week in which the given date falls.
     */
    public static Week weekOf(final Date date) {
        return new Week(dayOfYearISO(date)/7+1, date.getYear());
    }
    
    /**
     * Determine whether the given string is a valid representation of an ISO Week.
     */
    public static boolean validFormat(final String string) {
        return Pattern.matches("\\s*\\d{1,2}/\\d{4}\\s*", string);
    }
}
