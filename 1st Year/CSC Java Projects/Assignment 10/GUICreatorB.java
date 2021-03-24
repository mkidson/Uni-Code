import java.awt.BorderLayout;
import java.awt.Container;
//
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;
//
public class GUICreatorB {

    private GUICreatorB() {}
    
    public static void main(final String[] args) {

        final JFrame window;
        final JButton button;
        final JTextField textField;
        
        
        window = new JFrame("GUICreator B");
        window.setLocation(50, 100);
        
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        button = new JButton("Press Here");
        textField = new JTextField(20);
            
        Container contentPane = window.getContentPane();
        contentPane.add(button, BorderLayout.SOUTH);
        contentPane.add(textField, BorderLayout.NORTH);
        window.pack();

        window.setVisible(true);
    }
}