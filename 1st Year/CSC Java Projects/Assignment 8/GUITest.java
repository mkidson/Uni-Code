import java.awt.event.*;
import java.awt.*;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

import javafx.scene.paint.Color;

/**
 * GUITest
 */
public class GUITest extends JFrame {

    private static final long serialVersionUID = 1L;

    public GUITest() {
        
        super();
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JLabel hello = new JLabel("Hello World");
        add(hello);
    }
    
    public class EndingListener implements ActionListener{
        
        public void actionPerformed(ActionEvent e){
            
            System.exit(0);
        }
    }
    
        public static void main(String[] args) {
            
            GUITest newTest = new GUITest();
            newTest.setVisible(true);
        }
}