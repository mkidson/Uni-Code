

public class VLine extends VectorObject {

    private int yLength;

    public VLine(int id, int x, int y, int yLength){

        super(id, x, y);
        this.yLength = yLength;
    }

    public void draw(char[][] matrix){

        for (int i=this.y; i<this.y+this.yLength; i++) {
            
            matrix[i][this.x] = '*';
        }
    }
}