import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;
/**
 * A Duration object represents a length of time (with millisecond accuracy). 
 * 
 * 
 * 
 * @author Stephan Jamieson
 * @version 16/08/2019
 */
public class Duration implements Comparable<Duration> {
    
    public final static Duration ZERO = new Duration(0);
    
    private final long milliseconds;
        
    /**
     * Create a Duration object that represents the given quantity of milliseconds.
     */
    public Duration(long quantity) {
        this.milliseconds = quantity;
    }
    
    /** 
     * Create a Duration object that represents the given quantity of the given time unit.
     * 
     * For example, the expression <em>new Duration("minutes", 4)</em> creates a Duration object
     * that represents 4 minutes.
     * 
     * Permissible time units are: "millisecond", "second", "minute", "hour", "day".
     * 
     */
    public Duration(String timeUnit, long quantity) {
        this(TimeUnit.parse(timeUnit), quantity);    
    }

    /** 
     * Create a Duration object that represents the given quantity of the given time unit.
     */
    public Duration(TimeUnit timeUnit, long quantity) {
        this.milliseconds = timeUnit.multiplyBy(quantity).intValue();    
    }

    /**
     * Create a Duration object that represents the same length of time as that given.
     */
    public Duration(Duration duration) {
        this.milliseconds = duration.intValue();
    }

        
    /**
     * Obtain an integer value for this duration in milliseconds.
     */
    public long intValue() {
        return this.milliseconds;
    }
    
    /** 
     * Obtain an integer value that represents that part of this Duration which may be expressed 
     * as a multiple of the given time unit.
     * 
     * For example, given a duration object d that represents 4 minutes and 30 seconds, 
     * d.intValue("minute") produces the value 4. 
     * 
     * Permissible time units are: "millisecond", "second", "minute", "hour", "day".
     */
    public long intValue(String timeUnit) {
        return this.intValue(TimeUnit.parse(timeUnit));
    }
    
    /** 
     * Obtain an integer value that represents that part of this Duration which may be expressed 
     * as a multiple of the given time unit.
     */
    public long intValue(TimeUnit timeUnit) {
        return this.divideBy(timeUnit);
    }
    
    /**
     * Obtain a double value for this duration in milliseconds;
     */
    public double doubleValue() {
        return this.milliseconds;
    }
    
    /**
     * Obtain a double value that represents this Duration expressed as a multiple of the given
     * time unit.
     * 
     * For example, given a duration object d that represents 4 minutes and 30 seconds,
     * d.doubleValue("minute") produces the value 4.5.
     * 
     */
    public double doubleValue(String timeUnit) {
        return this.doubleValue(TimeUnit.parse(timeUnit));
    }
        
    /**
     * Obtain a double value that represents this Duration expressed as a multiple of the given
     * time unit.
     */ 
    public double doubleValue(TimeUnit timeUnit) {
        return this.divideBy(timeUnit)+this.remainder(timeUnit).doubleValue()/timeUnit.doubleValue();
    }

    /**
     * Obtain the sum of this Duration and the given Duration.
     */
    public Duration add(Duration other) {
        return new Duration(this.intValue()+other.intValue());
    }
    
    /**
     * Obtain the result of subtracting the given Duration from this Duration. 
     */
    public Duration subtract(Duration other) {
        return new Duration(this.intValue()-other.intValue());
    }
        
    /**
     * Obtain the result of multiplying this Duration by the given value.
     */
    public Duration multiplyBy(long value) {
        return new Duration(this.intValue()*value);
    }
        
    /**
     * Obtain the result of multiplying this Duration by the given value.
     * The result is rounded to the nearest millisecond.
     */
    public Duration multiplyBy(double value) {
        return new Duration(Math.round(this.intValue()*value));
    }
    
    /**
     * Obtain the result of dividing this Duration by the given value.
     * The result is rounded to the nearest millisecond.
     */
    public Duration divideBy(long value) {
        long result = this.intValue()/value;
        long remainder = this.intValue()%value;
        if (remainder*2>=value) {
            result = result+1;
        }
        return new Duration(result);
    }
        
    /**
     * Obtain the result of dividing this duration by the given value.
     * The result is rounded to the nearest millisecond.
     * 
     */
    public Duration divideBy(double value) {
        return new Duration(Math.round(this.intValue()/value));
    }
    
    /**
     * Perform an integer division of this Duration by the given Duration.
     */
    public long divideBy(Duration other) {
        return this.intValue()/other.intValue();
    }    

    /**
     * Obtain the remainder of an integer division of this Duration by the given Duration.  
     */
    public Duration remainder(Duration modulus) {
        return new Duration(this.intValue()%modulus.intValue());
    }
    
    /**
     * Obtain an absolute (unsigned) instance of this Duration. 
     */
    public Duration abs() {
        return new Duration(Math.abs(this.intValue()));
    }
        
    /**
     * Returns true if this Duration has a negative value, false otherwise.
     */
    public boolean isNegative() {
        return this.intValue()<0;
    }
        
    /**
     * Return a negative, zero, or positive value, depending on whether this duration is smaller, 
     * equal to, or greater than the given duration.
     */
    public int compareTo(Duration other) {
        return (int)(this.intValue()-other.intValue());
    }
    
    /**
     * Obtain a hash code value for this object.
     */
    public int hashCode() {
        return (int)this.intValue();
    }
    
    /**
     * Determine whether object o is equivalent to this object.
     * 
     * Object o is equivalent if it is a Duration of the same value as this Duration.
     * 
     */
    public boolean equals(Object o) {
        if (!(o instanceof Duration)) {
            return false;
        }
        else {
            Duration other = (Duration)o;
            return this.intValue()==other.intValue();
        }
    }             
        
    /**
     * Returns a representation of this Duration as quantities of the given series of units.
     * Given a unit at units[i], units[i+1] must be a sub unit.
     * 
     * Example {em>(new Duration("second", 93873)).split("hour", "minute", "second")</em> returns an array containing
     *     the values 26, 4, 33 i.e. 26 hours with remainder of 44 minutes with remainder of 33 seconds. 
     */
    public static long[] split(Duration duration, final String... units) {
        final TimeUnit[] timeUnits = new TimeUnit[units.length];
        for(int i=0; i<units.length; i++) { 
            timeUnits[i] = TimeUnit.parse(units[i]);
        }
        return split(duration, timeUnits);
    }

    /**
     * Returns a representation of this Duration as quantities of the given series of units.
     * Given a unit at units[i], units[i+1] must be a sub unit.
     * 
     * Example <em>(new Duration(TimeUnit.SECOND, 93873)).split(TimeUnit.HOUR, TimeUnit.MINUTE, TimeUnit.SECOND)</em> returns an array containing
     *     the values 26, 4, 33 i.e. 26 hours with remainder of 44 minutes with remainder of 33 seconds. 
     */
    public static long[] split(Duration duration, final TimeUnit... timeUnits) {
        final long[] quantities = new long[timeUnits.length];
        
        for(int i=0; i<timeUnits.length; i++) {
            quantities[i] = duration.intValue(timeUnits[i]);
            duration = duration.remainder(timeUnits[i]);
        }
        return quantities;
    }
    
   
    private final static String format(final long value, final String timeUnit) {
        return format(value, TimeUnit.parse(timeUnit));
    }
    
    private final static String format(final long value, final TimeUnit unit) {
        final String result = value+" "+unit.getName();
        if (value==1) return result; else return result+"s";
    }
    
    /**
     * Obtain a formatted string that expresses the given duration as a series of non-zero time unit quantities from the largest applicable
     * to the given smallest.
     * 
     * Example: Given <em>Duration d=new Duration("second", 88893); )</em>, the expression <em>Duration(d, "second")</em> returns the
     * string "1 day 41 minutes 33 seconds", while <em>Duration(d, "minute")</em> returns the string "1 day 41 minutes". 
     * 
     */
    public static String format(final Duration duration, final String smallestUnit) {
        return Duration.format(duration, TimeUnit.parse(smallestUnit));
    }

    /**
     * Obtain a formatted string that expresses the given duration as a series of non-zero time unit quantities from the largest applicable
     * to the given smallest.
     * 
     * Example: Given <em>Duration d=new Duration(TimeUnit.SECOND, 88893); )</em>, the expression <em>Duration(d, TimeUnit.SECOND)</em> returns the
     * string "1 day 41 minutes 33 seconds", while <em>Duration(d, TimeUnit.MINUTE)</em> returns the string "1 day 41 minutes". 
     * 
     */
    public static String format(final Duration duration, final TimeUnit smallestUnit) {
        // Select subset of time units.
        TimeUnit[] timeUnits = TimeUnit.values();
        for(int i=0; i<timeUnits.length; i++) {
            if (timeUnits[i].equals(smallestUnit)) {
                timeUnits = Arrays.copyOfRange(timeUnits, 0, i+1);
            }
        }
        final String[] names = new String[timeUnits.length];
        for(int i=0; i<timeUnits.length; i++) {
            names[i]=timeUnits[i].getName();
        }
        return format(duration, names);
    }
    
    /**
     * Obtain a formatted string that expresses the given duration as a series of no-zero quantities of the given time units.
     * 
     * Example: Given <em>Duration d=new Duration("second", 88893); )</em>, the expression <em>Duration(d, "hour", "minute", "second")</em> returns the
     * string "24 hours 41 minutes 33 seconds", while <em>Duration(d, "hour", "second")</em> returns the string "24 hours 2493 seconds". 
     */
    public static String format(final Duration duration, final String... units) {
        final TimeUnit[] timeUnits = new TimeUnit[units.length];
        for(int i=0; i<units.length; i++) { 
            timeUnits[i] = TimeUnit.parse(units[i]);
        }
        return format(duration, timeUnits);
    }
    
    /**
     * Obtain a formatted string that expresses the given duration as a series of no-zero quantities of the given time units.
     * 
     * Example: Given <em>Duration d=new Duration(TimeUnit.SECOND, 88893); )</em>, the expression
     * <em>Duration(d, TimeUnit.HOUR, TimeUnit.MINUTE, TimeUnit.SECOND)</em> returns the string "24 hours 41 minutes 33 seconds", while 
     * <em>Duration(d, TimeUnit.HOUR, TimeUnit.SECOND)</em> returns the string "24 hours 2493 seconds". 
     */
    public static String format(final Duration duration, final TimeUnit... timeUnits) {
        final StringBuilder builder = new StringBuilder();
        
        final long[] quantities = Duration.split(duration, timeUnits);
        if (timeUnits.length>0) {
            // Locate first non-zero
            int index=0;
            while(index<timeUnits.length&&quantities[index]==0) { 
                index++;
            }
            if (index==timeUnits.length) {
                // Zero duration
                builder.append(format(quantities[index-1], timeUnits[index-1]));
            }
            else {
                // Locate last non-zero
                int last = timeUnits.length-1;
                while(last>0&&quantities[last]==0) {
                    last--;
                }
                builder.append(format(quantities[index], timeUnits[index]));
                index++;
                // Handle the rest bar last
                while(index<=last) {
                    if (quantities[index]!=0) {
                        builder.append(" "+format(quantities[index], timeUnits[index]));
                    }
                    index++;
                }
            }
        }
        return builder.toString();
    }
}

