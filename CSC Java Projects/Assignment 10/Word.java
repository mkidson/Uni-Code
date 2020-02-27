import java.util.Locale;
import java.text.Collator;
import java.text.CollationKey;
//
/**
 * A Word is a sequence of letters and the punctuation characters full
 * stop, apostrophe and hyphen. Instances of Words can be
 * compared. The default order is that of ZA English.
 * 
 * @author Stephan Jamieson
*/
public class Word implements Comparable<Word> {

    private String wordPhrase;
    private CollationKey collationKey;

    /**
     * Creates a Word that consists of the same sequence of letters as
     * the String <code>wordPhrase</code>.  Throws an
     * IllegalArgumentException if <code>wordPhrase</code> does not
     * represent a legitimate word.
     *
     *  @exception IllegalArgumentException If <code>! legalWordPhrase(wordPhrase)</code>.
     */
    public Word(String wordPhrase) {
        wordPhrase = wordPhrase.trim();
        if (! legalWordPhrase(wordPhrase)) {
            throw new IllegalArgumentException("Word("+wordPhrase+") : not a legal word phrase");
        }
        else {
            this.wordPhrase = wordPhrase;
            this.collationKey = collator.getCollationKey(wordPhrase);
        } 
    }

    /**
     * Compares relative ordering of this Word with the given
     * Word. Returns a value that is -ve, 0, or +ve depending on
     * whether this word comes before, is equal to, or comes after the
     * given word.
     *
     * @exception ClassCastException If <code>o</code> is not a Word.
     */
    public int compareTo(Word o) {
        Word other = (Word)o;
        return this.collationKey.compareTo(other.collationKey);
    }


    /**
     * Returns <code>true</code> if <code>o</code> is a Word and
     * consists of the same character sequence as this Word.
     */
    public boolean equals(Object o) {
        if (! (o instanceof Word)) {
            return false;
        }
        else {
            Word other = (Word)o;
            return this.wordPhrase.equals(other.wordPhrase);
        }
    }

    /**
     * Returns the String equivalent for this word.
     */
    public String toString() { return wordPhrase; } 


    /**
     * Returns the result of concatenating the specified word onto the end of this word.
     */
    public Word concat(Word word) { 
        return new Word(this.toString()+word.toString());
    }

    /**
     * Returns the character at <code>index</code>.
     *
     * @exception IndexOutOfBoundsException If <code>index &gt this.length()-1</code>.
     */
    public char charAt(int index) {
        if (index >= this.length() ) {
            throw new IndexOutOfBoundsException("Word: length "+this.length()+" : charAt("+index+") : out of bounds");
        }
        else {
            return wordPhrase.charAt(index);
        }
    }


    public Word toUpperCase() { return new Word(wordPhrase.toUpperCase()); }
    public Word toLowerCase() { return new Word(wordPhrase.toLowerCase()); }

  /**
     * Returns the index of the first occurrence of <code>c</code> in
     * this pattern. If <code>c</code> is not found then returns -1.
     */
    public int indexOf(char c) { return this.indexOf(c, 0); }

    /**
     * Returns the index of the first occurrence of <code>c</code> in
     * this word, starting from index <code>fromIndex</code>. If
     * <code>c</code> is not found then returns -1.
     */
    public int indexOf(char c, int fromIndex) { return wordPhrase.indexOf(c, fromIndex); }

    /**
     * Returns the index of the first occurrence of <code>word</code> in
     * this word. If <code>word</code> is not found then returns -1.
     *
     * @exception NullPointerException <code>word</code>.
     */
    public int indexOf(Word word) {
        if (word==null) {
            throw new NullPointerException("Word: indexOf(null).");
        }
        else {
            return this.indexOf(word, 0);
        }
    }

    /**
     * Returns the index of the first occurrence of <code>word</code> in
     * this word, starting from index <code>fromIndex</code>. If
     * <code>word</code> is not found then returns -1.
     *
     * @exception NullPointerException <code>word</code>.
     */
    public int indexOf(Word word, int fromIndex) {
    
        if (word==null) {
            throw new NullPointerException("Word: indexOf(null, "+fromIndex+"): null parameter.");
        }
        else {
            return this.wordPhrase.indexOf(word.toString(), fromIndex);
        }
    }

    /**
     * Returns the index of the last occurrence of <code>c</code> in
     * this word. If <code>c</code> is not found then returns -1.
     */
    public int lastIndexOf(char c) { return this.lastIndexOf(c, this.length()-1); }


    /** 
     * Returns the index of the last occurrence of <code>c</code> in
     * this word, searching backwards from index
     * <code>fromIndex</code>. If <code>word</code> is not found
     * then returns -1.
     */ 
    public int lastIndexOf(char c, int fromIndex) { return wordPhrase.lastIndexOf(c, fromIndex); }

    /**
     * Returns the index of the last occurrence of <code>word</code> in
     * this word. If <code>word</code> is not found then returns -1.
     *
     * @exception NullPointerException <code>word</code>.
     */
    public int lastIndexOf(Word word) { 
        if (word==null) { 
            throw new NullPointerException("Word: lastIndexOf(null).");
        }
        else {
            return this.wordPhrase.lastIndexOf(word.toString(), this.length()-1);
        }
     }
    
    /** 
     * Returns the index of the last occurrence of
     * <code>word</code> in this word, searching backwards from
     * index <code>fromIndex</code>. If <code>word</code> is not
     * found then returns -1.
     *
     * @exception NullPointerException <code>word</code>.
     */ 
    public int lastIndexOf(Word word, int fromIndex) {  
        if (word==null) {
            throw new NullPointerException("Word: lastIndexOf(null, "+fromIndex+"): null parameter.");
        }
        else {
            return this.wordPhrase.lastIndexOf(word.toString(), fromIndex);
        }
    }

    /**
     * Returns the length of the word.
     */
    public int length() { return wordPhrase.length(); }



    // Helper components 

    // A Collator object knows the rules for ordering words.
    private static Collator collator = makeZAStrongCollator();

    private static Collator makeZAStrongCollator() {
        Collator collator = Collator.getInstance(new Locale.Builder().setLanguage("en").setRegion("ZA").build());
        collator.setStrength(Collator.IDENTICAL);
        return collator;
    }


    /**
     * Returns <code>true</code> if <code>c</code> is a legitimate
     * component of a Word, else <code>false</code>. i.e.  <code>c</code> is a
     * legitimate component if it is a letter, hyphen, full stop or
     * apostrophe.
     */
    public static boolean legalCharacter(char c) {
        return (Character.isLetter(c) || c=='\'' || c=='-' || c=='.' || c=='/');
    }

    /**
     * Returns <code>true</code> if <code>wordPhrase</code> is a
     * legitimate representation of a Word, else false. i.e. If for
     * all the characters <code>c</code> in <code>wordPhrase</code>,
     * <code>legalCharacter(c)</code>.
     */
    public static boolean legalWordPhrase(String wordPhrase) {
        if ( wordPhrase.length() == 0 ) {
            return false;
        }
        else if ( wordPhrase.length() == 1 && legalCharacter(wordPhrase.charAt(0)) ) {
            return true;
        }
        else if ( wordPhrase.length() > 1 && legalCharacter(wordPhrase.charAt(0)) ) {
            return legalWordPhrase(wordPhrase.substring(1));
        }
        else {
            return false;
        }
    }

    // ************************* Test Scripts *****************************

    private static void testIndexOf(Word word, char c) {   
        System.out.println("** Testing indexOf. **");       
    
        int index = word.indexOf(c);
        System.out.println("indexOf(\'"+c+"\') is "+index);
        while (index !=-1) {    
            System.out.print("indexOf(\'"+c+"\', "+(index+1)+") is ");
            index = word.indexOf(c, index+1);
            System.out.println(index);        
        }
    }

    private static void testIndexOf(Word word, Word subWord) {   
        System.out.println(" ** Testing indexOf **");
    
        int index = word.indexOf(subWord);
        System.out.println("indexOf(\""+subWord+"\") is "+index);
        while (index !=-1) {
    
            System.out.print("indexOf(\""+subWord+"\", "+(index+1)+") is ");
            index = word.indexOf(subWord, index+1);
            System.out.println(index);        
        }    
    }

    private static void testLastIndexOf(Word word, char c) {
        System.out.println("** Testing lastIndexOf **");
            
        int index = word.lastIndexOf(c);
        System.out.println("lastIndexOf(\'"+c+"\') is "+index);
        while (index !=-1) {
            System.out.print("lastIndexOf(\'"+c+"\', "+(index-1)+") is ");
            index = word.lastIndexOf(c, index-1);
            System.out.println(index);        
        }
    }

    private static void testLastIndexOf(Word word, Word subWord) {
        System.out.println("** Testing lastIndexOf **");
    
        int index = word.lastIndexOf(subWord);
        System.out.println("lastIndexOf(\""+subWord+"\") is "+index);
        while (index !=-1) {            
            System.out.print("lastIndexOf(\""+subWord+"\", "+(index-1)+") is ");
            index = word.lastIndexOf(subWord, index-1);
            System.out.println(index);        
        }
    }


    public static void main(String args[]) {
        Word word=null;
        Word subWord=null;
        char testChar=0;
    
        try {
            word = new Word(args[0]);
            subWord = new Word(args[1]);
            testChar = args[2].charAt(0);
        }
        catch (Exception e) {
            System.out.println("java Word <word> <subword> <char>");
            System.exit(-1);
        }
    
        System.out.println("Word test script");
        System.out.println("Performing method tests using \""+word+"\", \""+subWord+"\", \'"+testChar+"\'");
        
        System.out.println("Its length is "+word.length());
        int i=0;
        try {
            while (i <= word.length()) {
                System.out.println("charAt("+i+") is "+word.charAt(i));
                i++;
            }
        }
        catch (IndexOutOfBoundsException indexOut) {
            System.out.println("charAt("+i+") is "+indexOut);
        }
        testIndexOf(word, testChar);
        testIndexOf(word, subWord);
        testLastIndexOf(word, testChar);
        testLastIndexOf(word, subWord);
        word = word.toLowerCase();
        System.out.println("toLowerCase() is " + word);
        word = word.toUpperCase();
        System.out.println("toUpperCase() is " + word);
    }
}
