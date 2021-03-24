

public class HLine extends VectorObject {

    private int xLength;

    public HLine(int id, int x, int y, int xLength){

        super(id, x, y);
        this.xLength = xLength;
    }

    public void draw(char[][] matrix){

        for (int i=this.x; i<this.x+this.xLength; i++) {
            
            matrix[this.y][i] = '*';
        }
    }
}