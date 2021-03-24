/**
 * <p>An object of this class represents a Currency such as US Dollars or British Pound Stirling.</p>
 * 
 * <p>A currency has a description/name, an ISO 4217 currency code and a symbol denoting the currency's major unit. 
 * Many currencies have a minor (or fractional) unit such as the cent in the case of US dollars. 
 * For those that have, commonly there are 100 minor per major, in some cases there are less, in others more.</p>
 * 
 * <p>A currency object, besides recording the details of a particular currency, also provides facilities 
 * for formatting/parsing monetary amounts i.e. for creating strings and for interpreting strings that represent amounts of the
 * currency. A number of simplifications are made in this regard:</p>
 * <ul>
 *  <li>It is assumed that the currency symbol always appears in front of an amount.</li> 
 *  
 *  <li>Negative quantities are represented by a minus sign, '-', that precedes the currency symbol, "-R35.50" for example 
 *      (as opposed to say "R-35.50").</li>   
 *
 *  <li>The decimal point is always represented using a full stop (as opposed to a comma for example), and no attempt is made 
 *      to group the digits of large quantities, so for example, one million Rand is assumed to be represented as "R1000000" 
 *      (as opposed to "R1,000,000").</li> 
 * </ul>
 * @author Stephan Jamieson
 * @version 15/11/2007
 */
public class Currency 
{
    private String symbol;
    private String code;
    private int minorPerMajor;
   
    private final static char DECIMAL_POINT = '.';
    private final static char MINUS_SIGN = '-';
    
    /**
     * Create a Currency object that represents the currency with 
     * the given unit symbol (e.g. "$" for US Dollars), ISO 4217 code
     * and number of minor units per major units (e.g. 100 in the case of pennies per British Pound).
     * 
     * 
     * @param symbol of the currency unit e.g. "$".
     * @param code ISO 4217 currency code e.g. GBP for British Pound Sterling.
     * @param minorPerMajor number of minor units per major unit (A power of 10 is expected).
     */
    public Currency(String symbol, String code, int minorPerMajor) {
        final String ERR_STR = "Currency("+symbol+", "+code+", "+minorPerMajor+"):";
        
        // Check that none of the String parameters are null.
        if (symbol==null||code==null) {
            throw new IllegalArgumentException(ERR_STR+" null String argument.");
        } 
        else {
            this.symbol=symbol;
            this.code = code;
        }
        // Check that minorPerMajor is a power of 10.
        if (minorPerMajor<0||minorPerMajor>0&&(Math.round(Math.log10(minorPerMajor))!=Math.log10(minorPerMajor))) {
            throw new IllegalArgumentException(ERR_STR+" a positive integer power of 10 is expected for the number of minor units per major unit");
        }
        else {
            this.minorPerMajor = minorPerMajor;
        }
    }
       
    /**
     * Obtain the symbol or sign for this currency.
     */
    public String symbol() { return symbol; }
    
    /**
     * Obtain the ISO 4217 code for this currency
     */
    public String code() { return code; }
    
    /**
     * Obtain the number of minor units per major unit e.g. there are 100 cents to the Euro.
     */
    public int minorPerMajor() { return minorPerMajor; }
   

    /**
     * Obtain the default number of fraction digits used for amounts of this currency. 
     * 
     * The number derives from the number of minor units per major unit. For example, there are 100 cents
     * to the Euro, thus there are 2 fraction digits.
     */
    public int fractionDigits() {
        return (""+this.minorPerMajor()).length()-1;
    }
    
    /**
     * <p>Given a real number that represents an amount of this currency, obtain an integer value that represents
     * the same amount expressed as a quantity in the currency's minor unit.</p>
     * 
     * <p>So for example, assuming</p>
     * <pre>
     * Currency USD = new Currency("$", "USD", 100);
     * </pre>
     * 
     * <p>The expression</p>
     * <pre>
     * USD.convert(10.05)
     * </pre>
     * 
     * <p>will produce the integer <span class="code">1005</span>.</p>
     * 
     * <p>Amounts are rounded to the nearest minor unit. So for example, the expression</p>
     * <pre>
     * USD.convert(1.005) 
     * </pre>
     * <p>will produce the integer <span class="code">1001</span>.</p>
     */
    public long convert(double amount) {
        return Math.round(amount*this.minorPerMajor());
    }
    
    
    /**
     * Obtain a string representation for the amount given. The amount is assumed to be in the currency's minor unit 
     * e.g. pennies for Sterling, cents for the Euro.
     * 
     * So for example, assuming
     * <pre>
     * Currency USD = new Currency("$", "USD", 100);
     * </pre>
     * 
     * The expression 
     * <pre>
     * USD.format(3500)
     * </pre>
     * 
     * will produce the String <span class="code">"$35.00"</span>.
     * 
     * @param amount a quantity of the minor unit of the currency.
     */
    public String format(long amount) {
        StringBuffer result = new StringBuffer();
        // Building String from left to right.
        // Insert minus sign if necessary.
        if (amount<0) {
            result.append(MINUS_SIGN);
            amount = Math.abs(amount);
        }
        // Append currency symbol
        result.append(this.symbol());
        // Append units.
        result.append(Long.toString(amount/this.minorPerMajor()));
        // Stick in decimal point
        result.append(DECIMAL_POINT);
        
        {   // Format fractional part, padding with leading zeroes if necessary.
            final String fraction = Long.toString(amount%this.minorPerMajor());
            // Pad with leading zeroes if necessary
            final int leadingZeroes = this.fractionDigits()-fraction.length();
            if (leadingZeroes>0) {
                result.append(padding(leadingZeroes));
            }
            result.append(fraction);
        }
        return result.toString();
    }

    /**
     * Obtain a numerical value for the quantity represented by the given string.
     * The result is given as a quantity of the currency's minor unit. 
     * 
     * The String given as a parameter is assumed to have the following format:
     * <pre>
     * [-]&lt;symbol&gt;&lt;quantity of units&gt;[.&lt;quantity of subunits&gt;]
     * </pre>
     * 
     * Optionally, the String begins with a minus sign. Next comes the currency symbol, followed by the quantity of
     * major units, followed by an optional fractional part, i.e. a decimal point, '.', followed by a quantity of 
     * minor units. So for example, assuming that we're dealing with quantities of South African Rand,
     * the Strings "-R1", "R1.09", "-R0.10", "R25.00" are all valid, and will produce the values -100, 109, -10, 2500 respectively. 
     * 
     * @param amount a String representing an amount of this currency.
     */
    public long parse(final String amount) {        
        final boolean isNegative;
        String temp = amount.trim();
            
        if (temp.charAt(0)==MINUS_SIGN) {
            isNegative = true;
            temp = temp.substring(1).trim();
        }
        else {
            isNegative = false;
        }
        
        // Check symbol
        if (!temp.startsWith(this.symbol())) {
            throw new IllegalArgumentException("Currency:parseString("+amount+"): wrong currency symbol or currency symbol missing/misplaced?");
        }
        temp = temp.substring(this.symbol().length()).trim();
  
        // Look for fractional portion.
        final int pointPos = temp.indexOf(DECIMAL_POINT);        
        if (pointPos<0) {
            // No fractional portion.
            // Pad out string with suitable number of zeroes
            temp = temp+Currency.padding(this.fractionDigits());
        }
        else {
            // We have a fractional portion.
            // Check fractional portion has correct number of digits.
            if (temp.length()-(pointPos+1)!=this.fractionDigits()) {
                throw new IllegalArgumentException("Currency:parseString("+amount+"): wrong number of fraction digits or are whitespace or other characters present?");
            }
      
            // Correct number of digits, remove decimal point from string.
            temp = temp.substring(temp.indexOf(this.symbol())+this.symbol().length(), pointPos).trim()+temp.substring(pointPos+1).trim();   
        }
        
        // Finished processing the string. Convert the result to an integer value.
        final long value = Long.parseLong(temp);
        if (isNegative) {
            return -value;
        }
        else {
            return value;
        }
    }
    
    
    /**
     * Determine whether this currency object represents the same currency as the
     * other currency object.
     * @param other the other currency object.
     */
    public boolean equals(Currency other) {
        return this.code().equals(other.code());
    }
    
    public int hashCode() {
        return this.code().hashCode();
    }

    private final static String[] padding = { "", "0", "00", "000"};    
    private static String padding(int quantity) {
        return padding[quantity];
    }
        
    
}
