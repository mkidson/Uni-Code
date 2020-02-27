import javax.swing.JFrame;
//
public class GUICreatorA {

    private GUICreatorA() {}
    
    public static void main(final String[] args) {
        final JFrame window;
    
        window = new JFrame("GUICreator A");
        window.setSize(300, 200);
        window.setLocation(50, 100);
    
        window.setVisible(true);
    }    
}
