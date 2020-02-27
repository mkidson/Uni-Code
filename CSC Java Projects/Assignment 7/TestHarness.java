import java.util.Collections;
/**
 * Write a description of class TestSuite here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
//
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
//
public class TestHarness {
    
    private TestHarness() {}

    private final static String DATA_FILE = "vehicledata.txt";

 
    private static List<String> readTestData(final String filename) throws FileNotFoundException {
        final List<String> results = new ArrayList<String>();
        final Scanner file = new Scanner(new File(filename));
        while (file.hasNextLine()) {
            results.add(file.nextLine());
        }
        file.close();
        return results;
    }
        
    // The registration of the first car observed.
    private final static String FIRST_OBSERVED_REG = "CA 485-984";
    // The registration of the second car observed.
    private final static String SECOND_OBSERVED_REG = "ALK582 GP";
    // The registrations of all vehicles observed.
    private final static String VEHICLES_USED = "[CA 485984, ALK582 GP,732907 L,NN 281972, 6JKML3 MP,99TYJV GP,D87293 EC,"
				+ "556MSI FS, M83 ZN, 897352 WP, FKH222 NC, 023682 GP, 6JKML3 MP, 8FKEW ZN, ALK582 GP, "
				+ "AAB928 L, OUF288 EC, ALK582 GP, 44HALI FS, NA 018283,CFG 018]";

    public static void main(String args[]) throws IOException {
        List<String> testData = null;
        try {
        // Get file test data.
            testData = readTestData(DATA_FILE);
        }
        catch (FileNotFoundException fileExcep) {
            System.out.println("Unable to open data file.");
            System.exit(-1);
        }
        
        // Create observations object
        final Observations observations = new Observations();
        // Iterate through the file converting each line to a Registration object and appending it 
        // to the recorded vehicle observations. 
       
        for (String plate: readTestData(DATA_FILE)) {
            observations.record(new Registration(plate));
        }
        /* At this point we have an Observations object
         */
                
        /*
         * Test One : check the Observations "getTotal" method works.
         */ 
        System.out.println("Testing to see if the total of the number of observations is accurate.");
        System.out.println("The result is "+observations.getTotal()+" (should be "+testData.size()+").");
        
        /*
         * Test Two : check the Observations "iterator" method works.
         * Tried to use this but didn't compile:
         *      for(Registration reg : observations) {
         *          System.out.println(reg);
         *      }
         * A puzzle.
         */
        System.out.println("Testing to see if we can iterate through all the observations.");
        System.out.println("The result is:");
        for (Registration reg : observations) {
            System.out.println(reg);
        }
        System.out.println("(Compare with the file "+DATA_FILE+" to verify correct).");
        
        /*
         * Test Three : check the Observations "observed" method works.
         */
        System.out.println("Testing to see if vehicle with registration "+FIRST_OBSERVED_REG+" was observed");
        Registration testReg = new Registration(FIRST_OBSERVED_REG);
        System.out.println("The result is "+observations.observed(testReg)+" (should be true).");
        
        /*
         * Test Four : check the Observations "numberOfObservations" method works.
         */
        System.out.print("Testing to see how many times the vehicle with registration "+SECOND_OBSERVED_REG);
        System.out.println(" has been observed");
        testReg = new Registration(SECOND_OBSERVED_REG);
        System.out.println("The result is "+observations.numberOfObservations(testReg)+" (should be 3).");

        /*
        * Test Five: check the Observations "getVehicles" method works.
        */
        System.out.println("Testing to see the registrations of all the vehicles that have been observed.");
        List<Registration> result = observations.getVehicles();
        // Print them in order so can easily check result.
        Collections.sort(result);
        System.out.println("The result is "+result);
        System.out.println("(should be "+VEHICLES_USED+")");  
    }
    
    
}
