import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Exam extends JFrame implements ActionListener {
 private JTextField txt = new JTextField();
 public Exam() {
 setSize(400,400);
 setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE);
 setLayout( new GridLayout(2,2) );
 add(txt);
 JLabel lab = new JLabel(" "); add(lab);
 JButton pea = new JButton("PEAS"); add(pea);
 JButton nut = new JButton("NUTS"); add(nut);
 pea.addActionListener(this);
 nut.addActionListener(this);
 }
 public void actionPerformed( ActionEvent e) {
 String veg = e.getActionCommand();
 if (veg.equals("PEAS")) txt.setText("R4.00");
 if (veg.equals("NUTS")) txt.setText("R9.00");
 }
 public static void main(String[] args) {
 Exam w = new Exam();
 w.setVisible(true);
 }
}