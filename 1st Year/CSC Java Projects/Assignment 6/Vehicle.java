

public class Vehicle {

    private int numPassengers;
    private String colour;

    public Vehicle (int passengers, String colour) {
    
        this.numPassengers = passengers;
        this.colour = colour;
    }

    public String toString() {
    
        return colour + " " + numPassengers + " passengers";
    }
}
