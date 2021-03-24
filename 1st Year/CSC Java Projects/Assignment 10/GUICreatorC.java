import java.awt.BorderLayout;
import java.awt.Container;
//
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
//
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;
//
import java.util.Date;
//
import javax.swing.WindowConstants;
//
public class GUICreatorC {

    private GUICreatorC() {}
    
    public static void main(final String[] args) {
        
        final JFrame window;
        final JButton button;
        final JTextField textField;

        window = new JFrame("GUICreator C");
        window.setLocation(50, 100);

        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    
        textField = new JTextField(20);
        textField.setEditable(false);

        button = new JButton("Press Here");
        button.addActionListener(new ButtonListener(textField));
        
        final Container contentPane = window.getContentPane();
        contentPane.add(button, BorderLayout.SOUTH);
        contentPane.add(textField, BorderLayout.NORTH);
        window.pack();
        window.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        window.setVisible(true);
    }
}