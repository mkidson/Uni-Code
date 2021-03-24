import java.awt.event.*;
import java.util.ArrayList;
import java.awt.*;
import javax.swing.*;
import javax.swing.text.html.HTML;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import java.awt.Color;

/**
 * Hangman
 */
public class Hangman extends JFrame implements ActionListener{

    private static final long serialVersionUID = 1L;
    private int difficulty = 0;
    private JPanel topPanel;
    private JPanel buttonPanel;
    private JPanel mainPanel;
    private JLabel imageLabel;
    private ImageIcon mainImage;
    private JPanel bottomPanel;
    private JLabel displayText;
    private JPanel textInput;
    private JTextField inputText;
    private String word;
    private String wordGuess;
    private WordHandler words = new WordHandler("dictionary.txt");
    private char[] guesses = new char[26];
    private String guessesWord = "";
    private int count = 1;

    public Hangman() {
        
        super("Hangman");
        setSize(400, 450);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        topPanel = new JPanel();
        topPanel.setLayout(new GridLayout(2, 1));
        buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());

        JButton easy = new JButton("Easy");
        easy.addActionListener(this);
        JButton medium = new JButton("Medium");
        medium.addActionListener(this);
        JButton hard = new JButton("Tuffy bag tuff");
        hard.addActionListener(this);
        buttonPanel.add(easy);
        buttonPanel.add(medium);
        buttonPanel.add(hard);

        JLabel choose = new JLabel("Choose your difficulty", SwingConstants.CENTER);

        topPanel.add(choose);
        topPanel.add(buttonPanel);

        mainPanel = new JPanel();
        mainPanel.setLayout(new FlowLayout());
        mainImage = new ImageIcon("hangman.gif");
        imageLabel = new JLabel(mainImage);
        mainPanel.add(imageLabel);
        
        bottomPanel = new JPanel();
        bottomPanel.setLayout(new GridLayout(1, 2));

        displayText = new JLabel("<html>Pick your difficulty and the game will begin. </html>", SwingConstants.CENTER);
        bottomPanel.add(displayText);
        
        textInput = new JPanel();
        textInput.setLayout(new GridLayout(2, 1));
        inputText = new JTextField(1);
        inputText.addActionListener(this);
        inputText.addMouseListener(new MouseAdapter(){
            public void mouseClicked(MouseEvent e){
                inputText.setText("");
                inputText.setForeground(Color.black);

            }
        });

        textInput.add(inputText);
        JButton go = new JButton("Go!");
        go.addActionListener(this);
        textInput.add(go);

        bottomPanel.add(textInput);

        add(bottomPanel, BorderLayout.SOUTH);
        add(mainPanel, BorderLayout.CENTER);
        add(topPanel, BorderLayout.NORTH);

    }
    
    public class EndingListener implements ActionListener{
        
        public void actionPerformed(ActionEvent e){
            
            System.exit(0);
        }
    }

    public void actionPerformed(ActionEvent e) {
          
        String text = e.getActionCommand();

        switch (text) {
            case "Easy":

                guesses = new char[12];
                guessesWord = "";
                count = 1;
                words.setCount(0);
                inputText.setEditable(true);
                inputText.setForeground(Color.gray);
                inputText.setText("Type your guesses here");
                
                mainImage = new ImageIcon("state1.gif");
                this.imageLabel.setIcon(mainImage);
                this.difficulty = 1;

                this.word = this.words.chooseWord();
                this.wordGuess = this.words.createWordGuess(this.word);

                displayText.setText("<html>The word is " + word.length() + " letters long<br>" + this.wordGuess + "<br>Your guesses have been: <br>" + guessesWord);
                break;
        
            case "Medium":

                guesses = new char[12];
                guessesWord = "";
                count = 1;
                words.setCount(0);
                inputText.setEditable(true);
                inputText.setForeground(Color.gray);
                inputText.setText("Type your guesses here");

                mainImage = new ImageIcon("state1.gif");
                this.imageLabel.setIcon(mainImage);
                this.difficulty = 2;

                this.word = this.words.chooseWord();
                this.wordGuess = this.words.createWordGuess(this.word);

                displayText.setText("<html>The word is " + word.length() + " letters long<br>" + this.wordGuess + "<br>Your guesses have been: <br>" + guessesWord);

                break;

            case "Tuffy bag tuff":

                guesses = new char[12];
                guessesWord = "";
                count = 1;
                words.setCount(0);
                inputText.setEditable(true);
                inputText.setForeground(Color.gray);
                inputText.setText("Type your guesses here");
                
                mainImage = new ImageIcon("state1.gif");
                this.imageLabel.setIcon(mainImage);
                this.difficulty = 3;

                this.word = this.words.chooseWord();
                this.wordGuess = this.words.createWordGuess(this.word);

                displayText.setText("<html>The word is " + word.length() + " letters long<br>" + this.wordGuess + "<br>Your guesses have been: <br>" + guessesWord);

                break;
            
            case "Go!":

                String inputString = inputText.getText();
                
                if (inputString == null) {
                    break;
                    
                } else {
                    
                    char guess = inputString.charAt(0);
                    ArrayList<Integer> indices = words.checkWord(guess, word);
                    
                    if (indices.size() == 0){
                        
                        if(!words.contains(guess, guesses)){

                            count += this.difficulty;

                            guesses = words.addChar(guess, guesses);
                            guessesWord = words.charArrayToString(guesses);
    
                            displayText.setText("<html>The word is " + word.length() + " letters long<br>" + this.wordGuess + "<br>Your guesses have been: <br>" + guessesWord);
    
                            mainImage = new ImageIcon("state"+count+".gif");
                            this.imageLabel.setIcon(mainImage);

                        } else {
                            break;
                        }

                    } else {
                        
                        this.wordGuess = words.updateWordGuess(guess, indices, wordGuess);
                        displayText.setText("<html>The word is " + word.length() + " letters long<br>" + this.wordGuess + "<br>Your guesses have been: <br>" + guessesWord);
                        
                    }

                    if(word.equals(wordGuess)){

                        displayText.setText("<html>CONGRATULATIONS<br>You won! Pick a difficulty to play again!");
                        mainImage = new ImageIcon("winner.gif");
                        this.imageLabel.setIcon(mainImage);
                        inputText.setEditable(false);
                    }

                    else if(count >= 11){

                        displayText.setText("<html>GAME OVER<br>Pick a difficulty to try again<br>The word was: " + word);
                        mainImage = new ImageIcon("gameover.gif");
                        this.imageLabel.setIcon(mainImage);
                        inputText.setEditable(false);
                    }
                }
                inputText.setText("");
                
                break;
        }
    }

    public static void main(String[] args) {
            
        Hangman newTest = new Hangman();
        newTest.setVisible(true);
    }
}