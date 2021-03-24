import java.util.Scanner;
/**
 * A Time object represents a twenty four hour clock reading composed of hours, minutes and seconds.
 * 
 * 
 * @author Stephan Jamieson
 * @version 16/8/19
 */
public class Time implements Comparable<Time> {


    public final static Time MIDNIGHT = new Time(0, 0);
    public final static Time MIDDAY = new Time(12,0);
    
    private Duration time;

    
    /**
     * Create a Time object from the given duration. 
     * 
     * The given value is mapped onto the twenty four hour clock. So for example, a duration of 
     * 7 hours, 5 minutes produces a Time object representing the value 07:05.
     * 
     * If the given value exceeds a twenty four hour period then it is "wrapped around". 
     * So for example, a duration of 25.5 hours produces a Time object representing the value 01:30.
     * 
     * @param duration the value representing the desired time.
     */
    public Time(Duration duration) {
        duration = duration.remainder(TimeUnit.DAY);
        if (duration.isNegative()) {
            duration = duration.add(TimeUnit.DAY);
        }
        this.time = duration;
    }
    
    /**
     * Create a Time object representing the given time in hours and minutes.
     */
    public Time(int hours, int minutes) {
        this(hours, minutes, 0);
    }
    
    /**
     * Create a Time object representing the given time in hours, minutes and seconds.
     */
    public Time(int hours, int minutes, int seconds) {
        time = (new Duration("hour", hours)).add(new Duration("minute", minutes))
                .add(new Duration("second", seconds));
    }
    
    public Time(String string) {
        Scanner scanner = new Scanner(string.trim()).useDelimiter(":");
        int hours = scanner.nextInt();
        int minutes = scanner.nextInt();
        int seconds = 0;
        if (scanner.hasNextInt()) { seconds = scanner.nextInt(); }
        time = new Duration("hour", hours).add(new Duration("minute", minutes))
                .add(new Duration("second", seconds));
    }
    
    /**
     * Obtain the hours component of the time value represented.
     */
    public int getHours() {
        return (int)(this.asDuration().divideBy(TimeUnit.HOUR));
    }
    
    /**
     * Obtain the minutes component of the time value represented.
     */
    public int getMinutes() {
        Duration result = this.asDuration();
        return (int)(result.remainder(TimeUnit.HOUR).divideBy(TimeUnit.MINUTE));
    }
    
    /**
     * Obtain the seconds component of the time value represented.
     */
    public int getSeconds() {
        Duration result = this.asDuration();
        return (int)(result.remainder(TimeUnit.MINUTE).divideBy(TimeUnit.SECOND));
    }
    
    /**
     * Translate this Time object into the equivalent Duration.
     */
    public Duration asDuration() {
        return new Duration(this.time);
    }
    
    /**
     * Obtain the Time that results from adding the given period to this Time.
     */
    public Time add(Duration duration) {
        return new Time(this.asDuration().add(duration));
    }
    
    /**
     * Obtain the Time that results from subtracting the given period from this Time.
     */
    public Time subtract(Duration duration) {
        return new Time(this.asDuration().subtract(duration));
    }
    
    /**
     * Obtain the period between this time and the given time by subtracting the latter 
     * from the former.
     */
    public Duration subtract(Time other) {
        return subtract(other.asDuration()).asDuration();
    }
        
    /**
     * Returns true if the given object is a Time object and represents the same time value as this Time 
     * object, otherwise returns false.
     */
    public boolean equals(Object o) {
        if (!(o instanceof Time)) {
            return false;
        }
        else {
            Time other = (Time)o;
            return this.asDuration().equals(other.asDuration());
        }
    }
    
    /**
     * Obtain a hashcode value for this object.
     */
    public int hashCode() {
        return this.asDuration().hashCode();
    }
    
    /**
     * Compare this Time object with the other Time object, returning -1, 0 or 1, depending on whether this 
     * Time precedes, is equal to, or exceeds the other time value.
     * 
     */
    public int compareTo(Time other) {
        return this.asDuration().compareTo(other.asDuration());
    }
   
    private String format(int value) {
        if (value<10) {
            return "0"+value;
        }
        else {
            return ""+value;
        }
    }

    /**
     * Obtain a String representation of this Time.
     */
    public String toString() {
        return format(this.getHours())+":"+format(this.getMinutes())+":"+format(this.getSeconds());       
    }
    
    public static boolean isValid(String string) {
        return string.matches("\\d:[0-5]\\d")||string.matches("[01]\\d:[0-5]\\d")||string.matches("2[0-3]:[0-5]\\d");
    }
}
