import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;


public class WordHandler {

    private String[] wordList = new String[77613];
    private int count = 0;

    public WordHandler(String filename) {
        try {
            File fileToRead = new File(filename);
            Scanner fileScanner = new Scanner(fileToRead);

            for (int i = 0; i < 77613; i++) {
                
                this.wordList[i] = fileScanner.nextLine().toLowerCase();
            }

            fileScanner.close();
        }

        catch(FileNotFoundException ex){
            System.out.println("Error");
        }
    }

    public void printList(){

        for (int i = 0; i < wordList.length; i++) {
            
            System.out.println(wordList[i]);
        }
    }

    public String chooseWord(){

        Random randNum = new Random();
        int wordNum = randNum.nextInt(77614);

        return this.wordList[wordNum];
    }

    public String createWordGuess(String word){

        char[] wordGuessChar = new char[word.length()];
        for (int i = 0; i < word.length(); i++) {
            wordGuessChar[i] = '-';
        }

        return new String(wordGuessChar);
    }

    //This method will check if a given char is in a given word and return the index values for the charArray of the given string
    public ArrayList<Integer> checkWord(char guess, String word){

        ArrayList<Integer> indices = new ArrayList<Integer>();
        char[] wordChar = word.toCharArray();
        for (int i = 0; i < wordChar.length; i++) {
            if (wordChar[i] == guess) {
                indices.add(i);
            }
        }
        return indices;
    }

    //This method will take an ArrayList<Integer> and replace the entries of the given string at the given indices with the given char
    public String updateWordGuess(char guess, ArrayList<Integer> indices, String wordGuess){

        char[] wordGuessChar = wordGuess.toCharArray();
        for (Integer index : indices) {
            wordGuessChar[index] = guess;
        }

        return new String(wordGuessChar);
    }

    public char[] addChar(char guess, char[] arr){

        arr[this.count] = guess;
        count++;
        return arr;
    }

    public String charArrayToString(char[] arr){

        String out = "";
        for (char i : arr) {
            out = out + i + ' ';
        }
        return out;
    }

    public boolean contains(char c, char[] arr){

        boolean out = false;
        for (char i : arr) {
            if(i == c){
                out = true;
            }
        }

        return out;
    }

    public void setCount(int i){

        this.count = i;
    }

    public static void main(String[] args) {
        
        WordHandler test = new WordHandler("dictionary.txt");
        System.out.println(test.chooseWord());
    }
}