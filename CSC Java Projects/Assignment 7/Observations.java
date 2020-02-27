import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;
import java.lang.Iterable;
/**
 * An object of this class is used to record obervations of 
 * vehicles, say for the purposes of monitoring road use. 
 *
 * Essentially, an Observations object stores a sequence of vehicle registrations 
 * in the order in which the corresponding vehicles were observed e.g.     
 * Say an observation of vehicle CA976543WP is followed by an observation
 * of CDS791 MP,
 * followed by vehicle CHZ897 L, followed by another observation of vehicle
 * CA9765 WP
 * then the sequence stored would be <<CA9765 WP,CDS791 MP,CHZ897 L,CA9765 WP>>.
 *
 * A vehicle may be observed more than once.
 *
 * @author Alan Berman [Adapted from Stephan Jamieson]
 * @version 14/7/15
 */
public class Observations implements Iterable<Registration>{

    private List<Registration> observations;
    
    /**
     * Create a new Observations object.
     */
    public Observations()  {
        observations = new ArrayList<Registration>();
    }
    
    /**
     * Record a new observation, appending the given registration to the existing sequence.  
     * @param reg the registration of the vehicle observed.
     */
    public void record(Registration reg) {
        observations.add(reg);
    }
    
    /**
     * Determine whether a vehicle with the given registration has
     * been observed at some point i.e. whether it appears at least once
     * in the sequence.
     */
    public boolean observed(Registration reg) {
        return observations.contains(reg);
    }
    
    /**
     * Obtain the total number of observations.
     */
    public int getTotal() { return observations.size(); }
    
    /**
     * Obtain an iterator that can be used to view the observations one by one.
     */
    public Iterator<Registration> iterator() {
        return new ArrayList<Registration>(observations).iterator();
    }
        
    /**
     * Return the number of times the vehicle with the given registration has been observed.
     */
    public int numberOfObservations(Registration reg) {
        int count = 0;
        for(Registration observed : observations) {
            if (observed.equals(reg)) {
                count++;
            }
        }
        return count;
    }

    /**
     * Obtain a list of the vehicles which have been observed.
     */
    public List<Registration> getVehicles() {
        List<Registration> results = new ArrayList<Registration>();
        for(Registration observed : observations) {
            if (! results.contains(observed)) {
                results.add(observed);
            }
        }
        return results;
    }
}