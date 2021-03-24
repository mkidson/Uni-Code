

public class Rectangle extends VectorObject {

    private int xLength, yLength;

    public Rectangle(int id, int x, int y, int xLength, int yLength){

        super(id, x, y);
        this.xLength = xLength;
        this.yLength = yLength;
    }

    public void draw(char[][] matrix){

        for (int i=this.x; i<this.x+this.xLength; i++){
            for (int c=this.y; c<this.y+this.yLength; c++) {
                
                matrix[c][i] = '*';
            }
        }
    }
}