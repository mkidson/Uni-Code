// KDSMIL001
// 28 July 2019


/**
 * Creates an object containing information about a seller
 */
public class Seller {


    public String ID;
    public String name;
    public String location;
    public String product;
    public Money unit_price = new Money("R0", new Currency("R", "ZAR", 100));
    public int number_of_units;

}