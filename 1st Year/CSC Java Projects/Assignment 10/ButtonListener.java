import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextField;
import java.util.Date;
//
public class ButtonListener implements ActionListener {
    
    private JTextField textField;
    
    public ButtonListener(final JTextField field) {
        this.textField = field;
    }

    public void actionPerformed(ActionEvent e) {
        final Date dateAndTime = new Date();
        final String text = dateAndTime.toString();
        textField.setText(text);
    }
}
