import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
//
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
/**
 * 
 * WordList
 * A WordList is a list ADT that contains Words. 
 * Searches may be performed on a WordList using simple wildcard expressions.
 * 
 * @author Stephan Jamieson
 * @version 5th February 2007
 */
public class WordList implements Iterable<Word> {

    private List<String> copyright;
    private List<Word> words;

    /**
     * Create an empty WordList.
     */
    public WordList() {
        this.words = new ArrayList<Word>();
        this.copyright = new ArrayList<String>();
    }

    /**
     * If the word is not in the list then it is added and the method 
     * returns true. Otherwise it returns false.
     */
    public boolean add(Word word) {
        int index = Collections.binarySearch(words, word);
        if (index<0) { // The word is not in the list so we'll add it
            index = index+1;
            index = index - 2*index;
            words.add(index, word);
            return true;
        }
        else {
            return false;
        }
    }
        

    /**
     * If word is in the list then it is removed and the value true is
     * returned, otherwise false.
     */
    public boolean remove(Word word) {
        int index =Collections.binarySearch(words, word);

        if (index<0) { // The word is not in the list
            return false;
        }
        else {
            words.remove(index);
            return true;
        }
    }
    
    /**
     * Returns true if the given word is in the list, otherwise false.
     */
    public boolean contains(Word word) {
        return Collections.binarySearch(this.words, word)>=0;
    }

    /**
     * Returns an Iterator object that may be used to iterate
     * over this list of words.
     */
    public Iterator<Word> iterator() {
        return this.words.iterator();
    }

    /**
     * Returns a list of those words that match the given pattern.
     */
    public WordList match(Pattern pattern) {
        WordList result = new WordList();
        Iterator iterator = this.iterator();
    
        while (iterator.hasNext()) {
            Word word = (Word)iterator.next();
            if ( pattern.matches(word) ) {
            result.add(word);
            }
        }    
        return result;
    }

    /**
     * Returns the number of words in the list.
     */
    public int size() { return words.size(); }

    /**
     * Returns a String representation of the list of the form {word, ..., word}.
     */
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append("{");
   
        Iterator iterator = this.iterator(); 
        if (iterator.hasNext()) {
            result.append(iterator.next());
            while (iterator.hasNext()) {
                result.append(", "+iterator.next());
            }
        }
        result.append("}");
        return result.toString();
    }


    // Class methods

    private final static String START_LABEL = "START";

    private static void skipToStart(String startLabel, BufferedReader buffer, WordList list) throws IOException {
        String line = buffer.readLine();
    
        while (! line.equals(startLabel) ) {    
            list.copyright.add(line);
            line = buffer.readLine();
        }
    }

    /**
     * Constructs a word list from the named file. The file should be
     * organized such that there is a single word per line.
     * 
     * The file may contain a preamble such as a copyright notice. If
     * so, the beginning of the data should be marked by a line containing
     * the single word "START".
     * 
     * @throws FileNotFoundException if unable to open the named file.
     * @throws IOException if some error occurs during reading of the file (uncommon).
     * @throws IllegalArgumentException if one of the lines in the file does
     * not satisfy the requirements for a word (letters, hyphens, apostrophes, full-stops only).
     */
    public static WordList readFromFile(String filename) throws IOException, FileNotFoundException, IllegalArgumentException {
        WordList result = new WordList();    
        BufferedReader buffer = new BufferedReader(new FileReader(filename));
        skipToStart(START_LABEL, buffer, result);
    
        String line = buffer.readLine();
        while (line !=null) {    
            result.words.add(new Word( line.trim() ) );
            line = buffer.readLine();
        }
        buffer.close();
        return result;
    }

    private static void spoolData(Iterator data, BufferedWriter output) throws IOException {
        while (data.hasNext() ) {
            output.write(data.next().toString());
            output.newLine();
        }
    }

    /**
     * Writes the list to the specified file.
     * @throws IOException if an error occurs during file writing (uncommon).
     */
    public static void save(String filename, WordList list) throws IOException { 
        BufferedWriter output = new BufferedWriter(new FileWriter(filename));
        spoolData(list.copyright.iterator(), output);
        output.write(START_LABEL);
        output.newLine();
        spoolData(list.iterator(), output);    
        output.close();
    }


    // Test script
    public static void main(String[] args) {
        System.out.println("WordList test script");
    
        try {
            WordList wordList;
            Pattern pattern;
            wordList = WordList.readFromFile(args[0]);
            pattern = new Pattern(args[1]);
            System.out.println("Searching the word list with pattern \""+pattern+"\" produces "+wordList.match(pattern));
    
        }
        catch (FileNotFoundException fileNotFound) {
            System.out.println("Could not open file \""+args[0]+"\"");
            System.exit(-1);
        }
        catch (IOException ioException) {
            System.out.println("IOError trying to create word list from file \""+args[0]+"\"");
            System.exit(-1);
        }
        catch (ArrayIndexOutOfBoundsException indexOutOfBounds) {
            System.out.println("java WordList <filename> <pattern>");
            System.exit(-1);
        }
    } 
}
