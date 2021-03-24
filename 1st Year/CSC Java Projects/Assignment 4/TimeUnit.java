/**
 * A TimeUnit is a named Duration constant. 
 * 
 * 
 * 
 * @author Stephan Jamieson
 * @version 16/08/2019
 */
 public final class TimeUnit extends Duration {
    private String name;
    private TimeUnit(final String name, final long milliseconds) {
        super(milliseconds);
        this.name = name;
    }
    public String getName() { return name; }
    
    public final static TimeUnit MILLISECOND = new TimeUnit("millisecond", 1);
    public final static TimeUnit SECOND = new TimeUnit("second", 1000);
    public final static TimeUnit MINUTE = new TimeUnit("minute", SECOND.intValue()*60);
    public final static TimeUnit HOUR = new TimeUnit("hour", MINUTE.intValue()*60);
    public final static TimeUnit DAY = new TimeUnit("day", HOUR.intValue()*24);
    public final static TimeUnit WEEK = new TimeUnit("week", DAY.intValue()*7);
    private final static TimeUnit[] VALUES = {WEEK, DAY, HOUR, MINUTE, SECOND, MILLISECOND};
 
    public static TimeUnit[] values() { return VALUES; }
    
    public static TimeUnit parse(String timeUnitName) {
        timeUnitName = timeUnitName.trim().toLowerCase();
        if (timeUnitName.charAt(timeUnitName.length()-1)=='s') {
            // Depluraise
            timeUnitName = timeUnitName.substring(0, timeUnitName.length()-1);
        }
        for(TimeUnit timeUnit : values()) {
            if (timeUnit.name.equals(timeUnitName)) {
                return timeUnit;
            }
        }
        return null;
    }
}