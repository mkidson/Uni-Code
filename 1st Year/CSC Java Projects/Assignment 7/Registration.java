import java.lang.Comparable;
/**
 * An object of the Registration class represents a South African vehicle registration. 
 *  
 * @author Alan Berman [Adapted from Stephan Jamieson]
 * @version 14/7/15
 */
// REMOVE implements
public class Registration implements Comparable<Registration> {

    private final Province province;
    private final String identifier;
    
    /**
     * Create a Registration object from a string of suitable format.
     * @param code a String representing a vehicle registration.
     * @throws IllegalArgument exception if code does not represent a valid registration.
     */
    public Registration(final String identifier) throws IllegalArgumentException {
        this.province = Province.identifyProvince(identifier);
        this.identifier = identifier;
    }
    
    public Province getProvince() { return this.province; }
    public String getIdentifier() { return this.identifier; }
    
	/**
	* Determine whether the given string is a valid registration identifier.
	*/
    public static boolean isValid(final String regIdentifier) { 
        try {
            Province province = Province.identifyProvince(regIdentifier);
            return true;
        }
        catch (IllegalArgumentException illExcep) {
            return false;   
        }
    }

    public int compareTo(Registration other){

        return this.identifier.compareTo(other.getIdentifier());
    }

    public boolean equals(Object other){

        if(other == this) return true;
        if(other == null || (other.getClass() != this.getClass())) return false;

        Registration r = (Registration) other;
        return identifier.equals(r.getIdentifier());
    }
    
    public String toString(){

        return this.identifier;
    }

}
