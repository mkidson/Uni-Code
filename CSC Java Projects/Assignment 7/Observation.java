import java.lang.Comparable;


/**
 * Observation
 */
public class Observation implements Comparable<Observation> {

    private Registration registration;
    private Time time;

    public Observation(final Registration registration, final Time time) {

        this.registration = registration;
        this.time = time;
    }

    public Time getTime(){

        return this.time;
    }

    public Registration getIdentifier(){

        return this.registration;
    }

    public boolean isFor(final Registration identifier){

        boolean isFor = false;
        if (identifier.equals(this.registration)) {
            
            isFor = true;
        }

        return isFor;
    }

    public boolean inPeriod(final Time s, final Time e){

        boolean inPeriod = false;
        if (s.compareTo(e)<=0) {
            if (s.compareTo(this.time)<=0 && e.compareTo(this.time)>=0) {
                inPeriod = true;
            }
        }

        return inPeriod;
    }

    public boolean equals(Object o){

        if(o==this) return true;
        if(o==null || o.getClass() != this.getClass()) return false;

        Observation obs = (Observation) o;
        return (obs.getTime().equals(this.time) && obs.getIdentifier().equals(this.registration));
    }

    public int compareTo(Observation other){

        return this.time.compareTo(other.getTime());
    }

    public String toString(){

        return "[" + this.time.toString() +", "+ this.registration.toString() +"]";
    }
}