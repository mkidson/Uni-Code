import java.util.*;
import java.io.*;

/**
 * Assignment 5 Q3 VectorGraphics 2011 version
 *
 * @version 1.1
 */
class VectorGraphics {
    private static final String RENDER = "W";
    private static final String EXIT = "X";
    private static final String ADD = "A";
    private static final String MOVE = "M";
    private static final String RECTANGLE = "RECTANGLE";
    private static final String HLINE = "HLINE";
    private static final String VLINE = "VLINE";
    private static final String PTLINE = "PTLINE";
    private static final String DELETE = "D";

    private int xSize, ySize;
    private VectorObject[] objects;
    private int numberOfObjects;

    VectorGraphics(int x, int y, int objSize) {
        this.xSize = x;
        this.ySize = y;
        this.objects = new VectorObject[objSize];
        this.numberOfObjects = 0;
    }

    void run(String filename) {
        Scanner inputStream = null;

        try {
            inputStream = new Scanner(new FileInputStream(filename));
        } catch (Exception e) {
            System.exit(0);
        }

        while (inputStream.hasNextLine()) {
            String action = inputStream.next().toUpperCase();
            if (action.equals(EXIT)) {
                return;
            } else if (action.equals(RENDER)) {
                render();
            } else if (action.equals(ADD)) {
                int id = inputStream.nextInt();
                int x = inputStream.nextInt();
                int y = inputStream.nextInt();
                String obj = inputStream.next().toUpperCase();
                if (obj.equals(RECTANGLE)) {
                    int xLen = inputStream.nextInt();
                    int yLen = inputStream.nextInt();
                    add(new Rectangle(id, x, y, xLen, yLen));
                } else if (obj.equals(HLINE)) {
                    int len = inputStream.nextInt();
                    add(new HLine(id, x, y, len));
                } else if (obj.equals(VLINE)) {
                    int len = inputStream.nextInt();
                    add(new VLine(id, x, y, len));
                } else if (obj.equals(PTLINE)) {
                    int bx = inputStream.nextInt();
                    int by = inputStream.nextInt();
                    add(new PtLine(id, x, y, bx, by));
                }
            } else if (action.equals(DELETE)) {
                int id = inputStream.nextInt();
                delete(id);
            } else if (action.equals(MOVE)) {
                int id = inputStream.nextInt();
                int x = inputStream.nextInt();
                int y = inputStream.nextInt();
                move(id, x, y);
            }
        }

        inputStream.close();
    }

    private void add(VectorObject anObject) {
        objects[numberOfObjects++] = anObject;
    }

    private boolean delete(int aNumber) {
        for (int i = 0; i < numberOfObjects; i++)
            if (aNumber == objects[i].getId()) {
                for (int j = i; j < numberOfObjects - 1; j++)
                    objects[j] = objects[j + 1];
                numberOfObjects--;
                return true;
            }
        return false;
    }

    private void move(int aNumber, int x, int y) {
        for (int i = 0; i < numberOfObjects; i++)
            if (aNumber == objects[i].getId()) {
                objects[i].setNewCoords(x, y);
                return;
            }
    }

    private void render() {
        char[][] matrix = new char[ySize][xSize];
        for (int y = 0; y < ySize; y++) {
            for (int x = 0; x < xSize; x++) {
                matrix[y][x] = ' ';
            }
        }
        for (int i = 0; i < numberOfObjects; i++) {
            objects[i].draw(matrix);
        }
        System.out.print('+');
        for (int x = 0; x < xSize; x++) {
            System.out.print('-');
        }
        System.out.println('+');
        for (int y = 0; y < ySize; y++) {
            System.out.print('+');
            for (int x = 0; x < xSize; x++) {
                System.out.print(matrix[y][x]);
            }
            System.out.println('+');
        }
        System.out.print('+');
        for (int x = 0; x < xSize; x++) {
            System.out.print('-');
        }
        System.out.println('+');
    }
}
