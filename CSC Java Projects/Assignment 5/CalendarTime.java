import java.util.Scanner;
/**
 * An object of this class represents a calendar time i.e. a date and time.
 * 
 * @author Stephan Jamieson
 * @version 16/3/2011
 */
public class CalendarTime implements Comparable<CalendarTime> {

    private final Date date;
    private final Time time;
    
    /**
     * Create a CalendarTime object that represents the given date and time.
     */
    public CalendarTime(final Date date, final Time time) {
        this.date = date;
        this.time = time;
    }
        
    /**
     * Create a CalendarTime object from a String of the form "&lt;date&gt;%&lt;time&gt;". 
     * See the Date and Time classes for further details of format. 
     */
    public CalendarTime(final String string) {
        final Scanner scanner = new Scanner(string);
        scanner.useDelimiter("\\s*%\\s*");
        this.date = new Date(scanner.next());
        this.time = new Time(scanner.next());
    }
  
    /**
     * Obtain the date component of this calendar time.
     */
    public Date date() {
        return date;
    }
    
    /**
     * Obtain the time component of this calendar time.
     */
    public Time time() {
        return time;
    }
    
    /**
     * Subtract given CalendarTime from this CalendarTime.
     */
    public Duration subtract(final CalendarTime other) {
        Duration duration = this.time().subtract(other.time());
        duration = duration.add(this.date().subtract(other.date()));
        return duration;
    }

    /**
     * Add the given duration to this CalendarTime.
     */
    public CalendarTime add(final Duration duration) {
        if (duration.isNegative()) {
            return this.subtract(duration.abs());
        }
        else {
            final Duration temp = duration.add(this.time().asDuration());
            final Duration hoursMinutes = temp.remainder(TimeUnit.DAY);
            final Duration days = temp.subtract(hoursMinutes);
            final Date date = this.date().add(days);
            final Time time = new Time(hoursMinutes);
            return new CalendarTime(date, time);
        }
    }
    
    /**
     * Subtract the given duration from this CalendarTime.
     */
    public CalendarTime subtract(final Duration duration) {
        if (duration.isNegative()) {
            return this.add(duration.abs());
        }
        else {
            Duration temp = duration.subtract(this.time().asDuration());
            if (!temp.remainder(TimeUnit.DAY).equals(Duration.ZERO)) {
                temp = temp.add(TimeUnit.DAY);
            }
            final Duration hoursMinutes = temp.remainder(TimeUnit.DAY);            
            final Time time = new Time(TimeUnit.DAY.subtract(hoursMinutes));

            // Subtraction from date may produce an exception if the result predates
            // introduction of the Gregorian calendar.
            final Duration days = temp.subtract(hoursMinutes);
            final Date date = this.date().subtract(days);

            return new CalendarTime(date, time);
        }
    }
    
    /**
     * Obtain a hash code for this object.
     */
    public int hashCode() {
        return date.hashCode()+time.hashCode();    
    }
    
    /**
     * Returns true if <em>o</em> is a CalendarTime object representing the same date and time as this CalendarTime object.
     */
    public boolean equals(Object o) {
        if (!(o instanceof CalendarTime)) {
            return false;
        }
        else {
            CalendarTime other = (CalendarTime)o;
            return this.date().equals(other.date())&&this.time().equals(other.time());
        }
    }
    
    /**
     * Compare this CalendarTime object to the other CalendarTime object. Returns a -ve value if this CalendarTime 
     * precedes the other CalendarTime, zero if they are equivalent, and a +ve value if this CalendarTime follows the other CalendarTime. 
     */
    public int compareTo(CalendarTime other) {
        int result = this.date().compareTo(other.date());
        if (result==0) {
            result = this.time().compareTo(other.time());
        }
        return result;
    }
    
    /**
     * Obtain a string representation of this CalendarTime in the form "&lt;date&gt; &lt;time&gt;".
     */
    public String toString() {
        return date.toString()+"%"+time.toString();
    }
   
}
