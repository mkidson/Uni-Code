

abstract class VectorObject
{
   protected int id, x, y;
   
   VectorObject ( int anId, int ax, int ay )
   {
      id = anId;
      x = ax;
      y = ay;
   }
   
   int getId ()
   {
      return id;
   }
   
   void setNewCoords ( int newx, int newy )
   {
      x = newx;
      y = newy;
   }
   
   public abstract void draw ( char [][] matrix );
}
