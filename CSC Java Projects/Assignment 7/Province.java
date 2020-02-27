
/**
 * The Province enum provides values representing South African provinces from the point of 
 * view of vehicle registration identifiers (as appear on vehicle registration plates).
 * 
 * It offers a class (static) method for identifying and obtaining the Province value for a 
 * particular registration identifier.
 *
 * @author Stephan Jamieson
 * @version 11th September 2018
 */
import java.util.regex.Pattern;
//
public enum Province {

    WESTERN_CAPE("Western Cape"), 
    KWAZULU_NATAL("KwaZulu-Natal"), 
    MPUMALANGA("Mpumalanga"), 
    EASTERN_CAPE("Eastern Cape"), 
    LIMPOPO("Limpopo"), 
    GAUTENG("Gauteng"), 
    NORTHERN_CAPE("Northern Cape"), 
    FREE_STATE("Free State"), 
    NORTH_WEST("North West");

    private String name;
    private Pattern standard;    
    private Pattern personal;

    private Province(final String name) { this.name = name; }

    public String toString() { return this.name; }
    
    private final static String GENERAL_REGEX = "[A-Z]{3}[0-9]{3}";
    private final static String PERSONAL_REGEX = "[A-Z0-9][A-Z0-9]{0,6}";
    
    static {
        WESTERN_CAPE.standard = Pattern.compile("C[A-Z]{1,2}\\d{1,6}");
        KWAZULU_NATAL.standard = Pattern.compile("[A-Z]{1,2}\\d{1,6}");
        MPUMALANGA.standard = Pattern.compile(GENERAL_REGEX+"MP");
        EASTERN_CAPE.standard = Pattern.compile(GENERAL_REGEX+"EC");
        LIMPOPO.standard = Pattern.compile(GENERAL_REGEX+"L");
        GAUTENG.standard = Pattern.compile("("+GENERAL_REGEX+"GP)|([A-Z]{2}[0-9]{2}[A-Z]{2}GP)");
        NORTHERN_CAPE.standard = Pattern.compile(GENERAL_REGEX+"NC");
        FREE_STATE.standard = Pattern.compile(GENERAL_REGEX+"FS");
        NORTH_WEST.standard = Pattern.compile(GENERAL_REGEX+"NW");

        WESTERN_CAPE.personal = Pattern.compile(PERSONAL_REGEX+"WP");
        KWAZULU_NATAL.personal = Pattern.compile(PERSONAL_REGEX+"ZN");
        MPUMALANGA.personal = Pattern.compile(PERSONAL_REGEX+"MP");
        EASTERN_CAPE.personal = Pattern.compile(PERSONAL_REGEX+"EC");
        LIMPOPO.personal = Pattern.compile(PERSONAL_REGEX+"L");
        GAUTENG.personal = Pattern.compile(PERSONAL_REGEX+"GP");
        NORTHERN_CAPE.personal = Pattern.compile(PERSONAL_REGEX+"NC");
        FREE_STATE.personal = Pattern.compile(PERSONAL_REGEX+"FS");
        NORTH_WEST.personal = Pattern.compile(PERSONAL_REGEX+"NW");
    }

    
    /**
     * Given a String representing a registration identifier, the method returns the relevant Province.
     * @return Province
     * @throws IllegalArgumentException if the String does not form a valid licence identifier.
     */
    public static Province identifyProvince(String regIdentifier) throws IllegalArgumentException {
        final Province[] values = Province.values();
        for (Province province: values) {
            regIdentifier = regIdentifier.replaceAll("\\s|-", "");
            if (province.standard.matcher(regIdentifier).matches() || province.personal.matcher(regIdentifier).matches()) {
                return province;
            }
                
        }
        throw new IllegalArgumentException(String.format("Province:identify(%s): invalid string.", regIdentifier));
    }
    
    public static void main(final String[] args) {
        final String[] plates = { "CA 123-456", "CA JN 912-WP", "NN 21514", "GENIS 1-ZN", 
            "BBC123 MP", "CDS 791 MP", "BBC 123 EC", "FMJ 541 EC", "BBC 123 L", "CHZ 231 L", "BBC 123 GP", "BC 12 DF GP",
            "RDW112 GP", "BBC 123 NC", "BJW 595 NC", "BBC 123 FS", "BBC 123 NW", "DSM 032 NW"};
        for(String plate: plates) {
            System.out.printf("%s : %s\n", plate, Province.identifyProvince(plate));
        }
    }
}
        
        
