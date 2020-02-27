import java.lang.Math.*;

public class PtLine extends VectorObject {

    private int xEnd, yEnd;
    private boolean steep;
    private int temp;
    private int ys;
    private double m;
    private int y0;
    private double error;

    public PtLine(int id, int x, int y, int xEnd, int yEnd){

        super(id, x, y);
        this.xEnd = xEnd;
        this.yEnd = yEnd;
        
        steep = Math.abs(this.yEnd-this.y)>Math.abs(this.xEnd-this.x);

        if (this.steep){
            this.temp = this.x;
            this.x = this.y;
            this.y = this.temp;
            this.temp = this.xEnd;
            this.xEnd = this.yEnd;
            this.yEnd = this.temp;
        }

        if(this.x>this.xEnd){
            this.temp = this.x;
            this.x = this.xEnd;
            this.xEnd = this.temp;
            this.temp = this.y;
            this.y = this.yEnd;
            this.yEnd = this.temp;
        }

        this.m = (float)(Math.abs(this.yEnd-this.y))/(float)(this.xEnd-this.x);
    }

    public void draw(char[][] matrix){
    
        this.y0 = this.y;
        this.error = 0;

        for (int i=this.x; i<=this.xEnd; i++) {

            if(this.y>this.yEnd){
               this.ys = -1;
            }
            else{
               this.ys = 1;
            }
            
            if(this.steep){
                matrix[i][this.y0] = '*';
            }
            else{
                matrix[this.y0][i] = '*';
            }

            this.error += this.m;

            if(this.error>0.5){
                this.y0 += this.ys;
                this.error -= 1;
            }
        }
    }
}