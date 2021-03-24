
/**
 * <p>An object of this class represents an amount of money in a particular currency. Amounts can be added, subtracted, multiplied and subdivided.</p>
 * 
 * 
 * <p>The "assertSameCurrencyAs" methods is derived from Martin Fowler's Money class in "Patterns Of Enterprise Application Architecture", 2003.</p>
 * 
 * @author Stephan Jamieson 
 * @version 15/11/2007
 */
public class Money implements Comparable<Money> {

    private Currency currency;
    private long amount;
    
  
    /**
     * <p>Create a Money object that represents the given amount of the given currency.</p>
     * 
     * <p>The String given as the amount parameter is assumed to have the following format:</p>
     * <pre>
     * [-]&lt;symbol&gt;&lt;quantity of units&gt;[.&lt;quantity of subunits&gt;]
     * </pre>
     * 
     * @param amount a String representation of an amount in the given currency.
     * @param currency the currency of the amount represented.
     */
    public Money(String amount, Currency currency) {
        this(currency.parse(amount), currency);
    }

        /**
     * <p>Create a Money object that represents the given quantity (of the minor unit) of the given currency.</p>
     * 
     * <p>The amount is assumed to be in the currency's minor unit e.g. in pennies in the case 
     * that the currency is the British pound.</p>
     */
    public Money(long minorUnitAmount, Currency currency) {
        this.currency=currency;
        this.amount=minorUnitAmount;
    }

    /**
     * <p>Obtain a long integer that represents this Money object's value as a quantity of the minor 
     * unit of the currency.</p>
     * 
     * <p>For example, if the Money object represents R1.10 then this method 
     * will produce the long integer 110.</p> 
     */
    public long longAmount() {
        return this.amount;
    }
            
    /**
     * Obtain the Currency of this Money.
     */
    public Currency currency() {
        return currency;
    }
    
    
    /**
     * <p>Add the other amount of money to this amount.</p>
     * 
     * <p>The objects must be of the same currency.</p>
     * 
     * @param other the amount of money to add.
     * @return a Money object that represents the sum of this Money object and the other Money object.
     */
    public Money add(Money other) {
        assertSameCurrencyAs(other);
        return new Money(this.longAmount()+other.longAmount(), this.currency());
    }
    
    /**
     * <p>Subtract the other amount of money from this amount.</p>
     * 
     * <p>The Money objects must be of the same currency.</p>
     * 
     * @param other the amount of money to be subtracted.
     * @return a Money object that represents the amount that results when the other 
     * amount is subtracted from this amount.
     */
    public Money subtract(Money other) {
        assertSameCurrencyAs(other);
        return new Money(this.longAmount()-other.longAmount(), this.currency());
    }
        
    
    /**
     * <p>Compare this Money object to the other Money object, returning a negative, zero, 
     * or positive value depending on whether this Money object is smaller, equal to, or larger than 
     * the other Money object.</p>
     * 
     * <p>The Money objects that are compared must be of the same currency.</p>
     */
    public int compareTo(Money other) {
        assertSameCurrencyAs(other);
        return (int)(this.longAmount()-other.longAmount());
    }
    
    
    /**
     * <p>Determine whether this object is equivalent to the given object.</p>
     * 
     * @return true if o is an instance of Money and has the same amount of the same currency 
     * as this object, otherwise false.
     */
    public boolean equals(Object o) {
        if (!(o instanceof Money)) {
            return false;
        }
        else {
            Money other = (Money)o;
            return this.longAmount()==other.longAmount()&&this.currency().equals(other.currency());
        }
    }
    
    
    /**
     * Obtain a hash value for this Money object.
     */
    public int hashcode() {
        return (int)(this.longAmount()^(this.longAmount() >>> 32));
    }
    
    
    /**
     * Obtain a string representation of the monentary value represented 
     * by this object e.g. "$1.67" for a Money object that represents the amount 1.67
     * US dollars.
     */
    public String toString() {
        return currency.format(amount);
    }
    
    private void assertSameCurrencyAs(Money other) {
        if (this.currency()!=other.currency()) { throw new IllegalArgumentException("Money: mismatched currencies"); }
    }
    
    
}
