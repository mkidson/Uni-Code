
/**
 * A Duration object represents a length of time (with millisecond accuracy). 
 * 
 * 
 * 
 * @author Stephan Jamieson
 * @version 28/05/2010
 */
public class Duration implements Comparable<Duration> {
    
    public final static Duration ZERO = new Duration(0);
    public final static Duration ONE_MILLISECOND = new Duration(1);
    public final static Duration ONE_SECOND = new Duration(1000);
    public final static Duration ONE_MINUTE = new Duration(60000);
    public final static Duration ONE_HOUR = new Duration(3600000);
    public final static Duration ONE_DAY = new Duration(86400000);
    public final static Duration ONE_WEEK = new Duration(604800000);
    
    private long milliseconds;
        
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
        this.milliseconds = durationOf(timeUnit).multiplyBy(quantity).intValue();    
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
        return this.divideBy(durationOf(timeUnit));
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
        Duration unit = durationOf(timeUnit);
        return this.divideBy(unit)+this.remainder(unit).doubleValue()/unit.doubleValue();
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
    
    private static Duration durationOf(String timeUnit) {
        timeUnit = timeUnit.toLowerCase().trim();
        if (timeUnit.charAt(timeUnit.length()-1)=='s') {
            timeUnit = timeUnit.substring(0, timeUnit.length()-1);
        }
        if (timeUnit.equals("millisecond")) {
            return ONE_MILLISECOND;
        }
        else if (timeUnit.equals("second")) {
            return ONE_SECOND;
        }
        else if (timeUnit.equals("minute")) {
            return ONE_MINUTE;
        }
        else if (timeUnit.equals("hour")) {
            return ONE_HOUR;
        }
        else if (timeUnit.equals("day")) {
            return ONE_DAY;
        }
        else if (timeUnit.equals("week")) {
            return ONE_WEEK;
        }
        else {
            throw new IllegalArgumentException("Duration: Time unit '"+timeUnit+"' not recognised");
        }
    }
  
}
