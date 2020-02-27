
/**
 * A Pattern is used to identify Words with some specific
 * characteristics. Its intended use is in conjunction with Word and
 * WordList objects. WordList supports searching based on pattern
 * matching.
 *<br>
 * Characteristics of words include their length, character content
 * and character order. A Pattern is a description of those that are
 * required. A Pattern may range from a precise description that
 * matches a single Word to a very general description that may match
 * many words.
 *<br>
 * Patterns are sequences of letters, full stops, hyphens, apostrophes
 * and wildcard characters.  Hyphens, full stops and apostrophes are
 * all regarded as legitimate components of a Word.  When a letter or
 * one of these punctuation characters appears in a pattern it indicates
 * that the very same character must appear in the same position in
 * matching words. When a wildcard appears in a pattern it indicates
 * that a number of different characters or sequences of characters
 * are acceptable at that position.
 *<br>
 * The wildcard characters are query, '?', and asterisk, '*'. An
 * occurrance of a query indicates that any character may appear at that
 * position in a matching word. An occurrance of an asterisk
 * indicates that zero or more characters may appear at that
 * position in a matching word.
 *
 * @author Stephan Jamieson
 * @version %I%, %G%
 */
public class Pattern {


    private String pattern;

    /**
     * Creates a Pattern that's an exact match for the given Word.
     *
     * @param word a <code>Word</code> value
     * @exception NullPointerException <code>word</code>.
     */
    public Pattern(Word word) {

	if (word == null) {
	    throw new NullPointerException("Pattern(null) : null Word as argument.");
	}
	else {
	    this.pattern = word.toString();
	}
    }


    /**
     * Creates a Pattern based on the given String.
     *
     * @exception NullPointerException <code>pattern</code>.
     * @exception IllegalArgumentException If <code>! Pattern.legalPattern(pattern)</code>.
     */
    public Pattern(String pattern) throws IllegalArgumentException {

	if (pattern == null) {
	    throw new NullPointerException("Pattern(null) : null string as argument.");
	}
	else if (! legalPattern(pattern) ) {
	    throw new IllegalArgumentException("Pattern(\""+pattern+"\") : invalid string");
	}
	else {
	    this.pattern = pattern;
	}
    }

    public static final char QUERY = '?';
    public static final char ASTERISK = '*';

    /**
     * Returns the character at <code>index</code>.
     *
     * @exception IndexOutOfBoundsException If <code>index &gt this.length()-1</code>.
     */
    public char charAt(int index) {
	
	if (index >= this.length() ) {
	    throw new IndexOutOfBoundsException("Pattern: length "+this.length()+" : charAt("+index+") : out of bounds");
	}
	else {
	    return pattern.charAt(index);
	}
    }


    public Pattern toUpperCase() { return new Pattern(pattern.toUpperCase()); }
    public Pattern toLowerCase() { return new Pattern(pattern.toLowerCase()); }


    /**
     * Returns <code>true</code> if <code>this</code> Pattern matches <code>word</code> else <code>false</code>.
     *
     * @exception NullPointerException <code>word</code>.
    */
    public boolean matches(Word word) {
	
	if (word==null) {
	    throw new NullPointerException("Pattern: matches(null) : null Word");
	}
	else {
	    return match(pattern, word.toString());
	}
    }
  
    private static char firstCharOf(String string) { return string.charAt(0); }
    private static String restOf(String string) { return string.substring(1); }

    private static boolean match(String pattern, String word) {

	if ( word.length() == 0) {

	    if (pattern.length() == 0 ) {   
		return true;
	    }
	    else {
		if (firstCharOf(pattern) == ASTERISK ) {

		    return match(restOf(pattern), word);
		}
		else {
		    
		    return false;
		}
	    }
	}
	else { // word.length() > 0

	    char firstCharOfWord = firstCharOf(word);
	    String restOfWord = restOf(word);

	    if    (pattern.length() == 0 ) {

		return false;
	    } 
	    else {
		char firstCharOfPattern = firstCharOf(pattern);
		String restOfPattern = restOf(pattern);

		if (firstCharOfPattern == ASTERISK ) {
		
		    return match( restOfPattern , word) || match(pattern, restOfWord);
		}
		else if (firstCharOfPattern == firstCharOfWord ) {
		    
		    return match(restOfPattern, restOfWord ); 
		}
		else if (firstCharOfPattern == QUERY) {

		    return match(restOfPattern, restOfWord );
		}
		else {     
		    return false;
		}
	    }
	}
    }


    /** 
     * Returns <code>true</code> if <code>c</code> is a legal pattern character else <code>false</code>.
     * Specifically, <code>c</code> is legal if <code>Word.legalCharacter(c)</code> or is a <code>QUERY</code>
     * or an <code>ASTERISK</code>.
     */
    public static boolean legalCharacter(char c) {
	return Word.legalCharacter(c) || c==QUERY || c==ASTERISK;
    }
    
    /**
     * Returns true if <code>pattern</code> represents a legal pattern else <code>false</code>.
     * Specifically, <code>pattern</code> is legal if for all characters <code>c</code> in
     * <code>pattern</code>, <code>legalCharacter(c)</code>.
     */
    public static boolean legalPattern(String pattern) {

	if (pattern.length() == 0) {
	    return true;
	}
	else if (legalCharacter(firstCharOf(pattern)) ) {
	    return legalPattern(restOf(pattern));
	}
	else {
	    return false;
	}
    }


    /**
     * Returns the string equivalent to this pattern.
     */
    public String toString() {
	
	return this.pattern;
    }
    
    /**
     * Returns the index of the first occurrence of <code>c</code> in
     * this pattern. If <code>c</code> is not found then returns -1.
     */
    public int indexOf(char c) { return this.indexOf(c, 0); }

    /**
     * Returns the index of the first occurrence of <code>c</code> in
     * this pattern, starting from index <code>fromIndex</code>. If
     * <code>c</code> is not found then returns -1.
     */
    public int indexOf(char c, int fromIndex) { return pattern.indexOf(c, fromIndex); }

    /**
     * Returns the index of the first occurrence of <code>pattern</code> in
     * this pattern. If <code>pattern</code> is not found then returns -1.
     *
     * @exception NullPointerException <code>pattern</code>.
     */
    public int indexOf(Pattern pattern) {
	if (pattern==null) {
	    throw new NullPointerException("Pattern: indexOf(null).");
	}
	else {
	    return this.indexOf(pattern, 0);
	}
    }

    /**
     * Returns the index of the first occurrence of <code>pattern</code> in
     * this pattern, starting from index <code>fromIndex</code>. If
     * <code>pattern</code> is not found then returns -1.
     *
     * @exception NullPointerException <code>pattern</pattern>.
     */
    public int indexOf(Pattern pattern, int fromIndex) {

	if (pattern==null) {
	    throw new NullPointerException("Pattern: indexOf(null, "+fromIndex+"): null parameter.");
	}
	else {
	    return this.pattern.indexOf(pattern.toString(), fromIndex);
	}
    }

    /**
     * Returns the index of the last occurrence of <code>c</code> in
     * this pattern. If <code>c</code> is not found then returns -1.
     */
    public int lastIndexOf(char c) { return this.lastIndexOf(c, this.length()-1); }


    /** 
     * Returns the index of the last occurrence of <code>c</code> in
     * this pattern, searching backwards from index
     * <code>fromIndex</code>. If <code>pattern</code> is not found
     * then returns -1.
     */ 
    public int lastIndexOf(char c, int fromIndex) { return pattern.lastIndexOf(c, fromIndex); }

    /**
     * Returns the index of the last occurrence of <code>pattern</code> in
     * this pattern. If <code>pattern</code> is not found then returns -1.
     *
     * @exception NullPointerException <code>pattern</code>.
     */
    public int lastIndexOf(Pattern pattern) { 

	if (pattern==null) { 
	    throw new NullPointerException("Pattern: lastIndexOf(null).");
	}
	else {
	    return this.pattern.lastIndexOf(pattern.toString(), this.length()-1);
	}
    }
    
    /** 
     * Returns the index of the last occurrence of
     * <code>pattern</code> in this pattern, searching backwards from
     * index <code>fromIndex</code>. If <code>pattern</code> is not
     * found then returns -1.
     *
     * @exception NullPointerException <code>pattern</code>.
     */ 
    public int lastIndexOf(Pattern pattern, int fromIndex) {
	
	if (pattern==null) {
	    throw new NullPointerException("Pattern: lastIndexOf(null, "+fromIndex+"): null parameter.");
	}
	else {
	    return this.pattern.lastIndexOf(pattern.toString(), fromIndex);
	}
    }

    /**
     * Returns the length of this pattern.
     */
    public int length() { return pattern.length(); }

  
    /**
     * Inserts character <code>c</code> at index <code>atIndex</code>.
     *
     * @exception IllegalArugmentException If <code>c</code> is not a legal pattern character.
     * @exception IndexOutOfBoundsException If <code>atIndex</code> &gt <code>this.length()</code> or <code>atIndex</code> &lt 0.
     */
    public Pattern insert(char c, int atIndex) {
	if (!  legalCharacter(c)) {
	    throw new IllegalArgumentException("Pattern: insert("+c+", "+atIndex+") : illegal character");
	}
	else if (atIndex>this.length()-1 || atIndex<0) {
	    throw new IndexOutOfBoundsException("Pattern: length "+this.length()+" : insert("+c+", "+atIndex+") : index out of bounds.");
	}
	else {
	    String stringRep = this.toString();
	    return this.subpattern(0, atIndex).concat(c).concat(this.subpattern(atIndex));
	}
    }

    /**
     * Inserts  <code>pattern</code> at index <code>atIndex</code>.
     *
     * @exception NullPointerException <code>pattern</code>.
     * @exception IndexOutOfBoundsException If <code>atIndex &gt this.length() or atIndex &lt 0</code>.
     */
    public Pattern insert(Pattern pattern, int atIndex) { 
	if (pattern==null) {
	    throw new NullPointerException("Pattern: insert(null, "+atIndex+") : null pointer.");
	}
	else if (atIndex>this.length()-1 || atIndex<0) {
	    throw new IndexOutOfBoundsException("Pattern: length "+this.length()+" : insert(null, "+atIndex+"): index out of bounds.");
	}
	else {

	    return this.subpattern(0, atIndex).concat(pattern).concat(this.subpattern(atIndex));
	}
    }

    /**
     * Returns the subpattern beginning at index <code>atIndex</code>.
     *
     * @exception IndexOutOfBoundsException If <code>atIndex</code> &lt 0 or <code>atIndex</code> &gt <code>this.length()</code>.
     */ 
    public Pattern subpattern(int atIndex) {
	if (atIndex<0 || atIndex>this.length()) {
	    throw new IndexOutOfBoundsException("Pattern: length "+this.length()+" : subpattern("+atIndex+"): index out of bounds.");
	}
	else {
	    return this.subpattern(atIndex, this.length());
	}
    }

    /**
     * Returns the subpattern beginning at index <code>atIndex</code> and ending at <code>endIndex-1</code> inclusive.
     *
     * @exception IndexOutOfBoundsException If <code>atIndex</code> &lt 0 or <code>endIndex</code> &gt <code>this.length()</code> or <code>atIndex</code> &gt <code>endIndex</code>.
     */ 
    public Pattern subpattern(int atIndex, int endIndex) {
	if (atIndex<0 || endIndex>this.length() || atIndex>endIndex) {
	    throw new IndexOutOfBoundsException("Pattern: length "+this.length()+" : subpattern("+atIndex+", "+endIndex+"): index out of bounds");
	}
	else {
	    return new Pattern(this.toString().substring(atIndex, endIndex));
	}
    }

    /**
     * Appends <code>pattern</code> to the end of this pattern.
     *
     * @exception NullPointerException If <code>pattern</code> is <code>null</code>.
     */
    public Pattern concat(Pattern pattern) {
	if (pattern==null) {
	    throw new NullPointerException("Pattern: append(null) : null pointer.");
	}
	else {
	    return new Pattern(this.toString()+pattern.toString()); 
	}
    }

    /**
     * Appends <code>c</code> to the end of this pattern.
     *
     * @exception IllegalArgumentException If <code>c</code> is not a legal pattern character.
     */
    public Pattern concat(char c) {
	if (!  legalCharacter(c)) {
	    throw new IllegalArgumentException("Pattern: append("+c+") : illegal character");
	}
	else {
	    return new Pattern(this.toString()+c); 
	}
    }


    /**
     * Replaces the character at index <code>atIndex</code> with <code>c</code>.
     *
     * @exception IllegalArgumentException If <code>c</code> is not a legal pattern character.
     * @exception IndexOutOfBoundsException If <code>atIndex &lt 0 or atIndex &gt this.length()-1</code>.
     */
    public Pattern replace(char c, int atIndex) {

	if (!  legalCharacter(c)) {
	    throw new IllegalArgumentException("Pattern: replace("+c+", "+atIndex+") : illegal character");
	}
	else if (atIndex<0 || atIndex>this.length()-1) {
	    throw new IndexOutOfBoundsException("Pattern: length "+this.length()+" : replace("+c+", "+atIndex+") : index out of bounds");
	}
	else {
	    return this.subpattern(0, atIndex).concat(c).concat(this.subpattern(atIndex+1));
	}
    }

    /**
     * Replaces the subpattern beginning at index <code>atIndex</code> and of the same length as <code>pattern</code> with <code>pattern</code>.
     *
     * @exception NullPointerException If <code>pattern</code> is <code>null</code>.
     * @exception IndexOutOfBoundsException If <code>atIndex &lt 0 or atIndex+pattern.length() &gt this.length()</code>.
     */
    public Pattern replace(Pattern pattern, int atIndex) {

	if (pattern==null) {
	    throw new NullPointerException("Pattern: (null, "+atIndex+") : null pointer.");
	}
	else if (atIndex<0 || atIndex+pattern.length()>this.length()) {
	    throw new IndexOutOfBoundsException("Pattern: length "+this.length()+" : replace(\""+pattern.toString()+"\", "+atIndex+"): pattern too big to fit");
	}
	else {
	   return this.subpattern(0, atIndex).concat(pattern).concat(this.subpattern(atIndex+pattern.length()));
      
	}
    }


    // ************************* Test Scripts *****************************

    private static void testIndexOf(Pattern pattern, char c) {
   
	System.out.println("** Testing indexOf. **");	    

	int index = pattern.indexOf(c);
	System.out.println("indexOf(\'"+c+"\') is "+index);
	while (index !=-1) {

	    System.out.print("indexOf(\'"+c+"\', "+(index+1)+") is ");
	    index = pattern.indexOf(c, index+1);
	    System.out.println(index);	      
	}
    }

    private static void testIndexOf(Pattern pattern, Pattern subPattern) {
   
	System.out.println(" ** Testing indexOf **");

	int index = pattern.indexOf(subPattern);
	System.out.println("indexOf(\""+subPattern+"\") is "+index);
	while (index !=-1) {

	    System.out.print("indexOf(\""+subPattern+"\", "+(index+1)+") is ");
	    index = pattern.indexOf(subPattern, index+1);
	    System.out.println(index);	      
	}
    
    }

    private static void testLastIndexOf(Pattern pattern, char c) {

	System.out.println("** Testing lastIndexOf **");
        
	int index = pattern.lastIndexOf(c);
	System.out.println("lastIndexOf(\'"+c+"\') is "+index);
	while (index !=-1) {

	    System.out.print("lastIndexOf(\'"+c+"\', "+(index-1)+") is ");
	    index = pattern.lastIndexOf(c, index-1);
	    System.out.println(index);	      
	}
    }

    private static void testLastIndexOf(Pattern pattern, Pattern subPattern) {

	System.out.println("** Testing lastIndexOf **");

	int index = pattern.lastIndexOf(subPattern);
	System.out.println("lastIndexOf(\""+subPattern+"\") is "+index);
	while (index !=-1) {
	    
	    System.out.print("lastIndexOf(\""+subPattern+"\", "+(index-1)+") is ");
	    index = pattern.lastIndexOf(subPattern, index-1);
		System.out.println(index);	      
	    }
    }


    private static void testConcat(Pattern pattern, char c) {

	System.out.println("Test concat(\'"+c+"\') on "+pattern+" is "+pattern.concat(c));
    }

    private static void testConcat(Pattern pattern, Pattern subPattern) {

	System.out.println("Test concat(\""+subPattern+"\") on "+pattern+" is "+pattern.concat(subPattern));
    }


    private static void testMatches(Pattern pattern, Word word) {

	System.out.println("Test matches(\""+word+"\") on "+pattern+" is "+pattern.matches(word));
    }

    private static void testInsert(Pattern pattern, char c, int testIndex) {

	System.out.print("Test insert(\'"+c+"\', "+testIndex+") on "+pattern+" is ");
	try {
	    System.out.println(pattern.insert(c, testIndex)); 
	}
	catch (Exception e) {
	    System.out.println(e);
	}
    }

    private static void testInsert(Pattern pattern, Pattern subPattern, int testIndex) {

	System.out.print("Test insert(\""+subPattern+"\", "+testIndex+") on "+pattern+" is ");
	try {
	    System.out.println(pattern.insert(subPattern, testIndex)); 
	}
	catch (Exception e) {
	    System.out.println(e);
	}
    }


    private static void testReplace(Pattern pattern, char c, int testIndex) {

	System.out.print("Test replace(\'"+c+"\', "+testIndex+") on "+pattern+" is ");
	try {
	    System.out.println(pattern.replace(c, testIndex)); 
	}
	catch (Exception e) {
	    System.out.println(e);
	}
    }

    private static void testReplace(Pattern pattern, Pattern subPattern, int testIndex) {

	System.out.print("Test replace(\""+subPattern+"\", "+testIndex+") on "+pattern+" is ");
	try {
	    System.out.println(pattern.replace(subPattern, testIndex)); 
	}
	catch (Exception e) {
	    System.out.println(e);
	}
    }

    private static void testSubPattern(Pattern pattern, int indexOne, int indexTwo) {

	System.out.print("Test subpattern("+indexOne+") on "+pattern+" is ");
	try {
	    System.out.println(pattern.subpattern(indexOne)); 
	}
	catch (Exception e) {
	    System.out.println(e);
	}
	System.out.print("Test subpattern("+indexOne+", "+indexTwo+") on "+pattern+" is ");
	try {
	    System.out.println(pattern.subpattern(indexOne, indexTwo)); 
	}
	catch (Exception e) {
	    System.out.println(e);
	}

    }

    public static void main(String args[]) {

	Pattern pattern=null;
	Pattern subPattern=null;
	char testChar=0;
	int testIndexOne = 0;
	int testIndexTwo = 0;
	Word word=null;
	
	try {
	    pattern = new Pattern(args[0]);
	    subPattern = new Pattern(args[1]);
	    testChar = args[2].charAt(0);
	    testIndexOne = Integer.parseInt(args[3]);
	    testIndexTwo = Integer.parseInt(args[4]);
	    word = new Word(args[5]);
	}
	catch (Exception e) {
	    System.out.println("java Pattern <pattern> <subpattern> <char> <int> <int> <word>");
	    System.exit(-1);
	}

	System.out.println("Pattern test script");
	System.out.print("Performing method tests using \""+pattern+"\", \""+subPattern+"\", \'"+testChar+"\', ");
	System.out.println(testIndexOne+", "+testIndexTwo+", \""+word+"\".");
	
	System.out.println("Its length is "+pattern.length());
	int i=0;
	try {
	    while (i <= pattern.length()) {
		System.out.println("charAt("+i+") is "+pattern.charAt(i));
		i++;
	    }
	}
	catch (IndexOutOfBoundsException indexOut) {
	    System.out.println("charAt("+i+") is "+indexOut);
	}
	testIndexOf(pattern, testChar);
	testIndexOf(pattern, subPattern);
	testLastIndexOf(pattern, testChar);
	testLastIndexOf(pattern, subPattern);
	pattern = pattern.toUpperCase();
	System.out.println("toUpperCase() is " + pattern);
	pattern = pattern.toLowerCase();
	System.out.println("toLowerCase() is " + pattern);
	testConcat(pattern, testChar);
	testConcat(pattern, subPattern);
	testMatches(pattern, word);
	testInsert(pattern, testChar, testIndexOne);
	testInsert(pattern, subPattern, testIndexOne);
	testReplace(pattern, testChar, testIndexOne);
	testReplace(pattern, subPattern, testIndexOne);
	testSubPattern(pattern, testIndexOne, testIndexTwo); 
    }
}
