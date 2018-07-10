/* Tasks to complete:
 * display balls on that grid (hard)
 * display grid (medium)
 * convert remaining color constants from String to Color type (easy)
 */

// 0 - research into custom graphics https://www.ntu.edu.sg/home/ehchua/programming/java/J4b_CustomGraphics.html#zz-2

import java.awt.Graphics;
/* device independent tools for drawing on the screen */

// Drawing (or printing) texts on the graphics screen:
drawString(String str, int xBaselineLeft, int yBaselineLeft);

// Drawing lines:
drawLine(int x1, int y1, int x2, int y2);
drawPolyline(int[] xPoints, int[] yPoints, int numPoint);

// Drawing primitive shapes:
drawRect(int xTopLeft, int yTopLeft, int width, int height);
drawOval(int xTopLeft, int yTopLeft, int width, int height);
drawArc(int xTopLeft, int yTopLeft, int width, int height, int startAngle, int arcAngle);
draw3DRect(int xTopLeft, int, yTopLeft, int width, int height, boolean raised);
drawRoundRect(int xTopLeft, int yTopLeft, int width, int height, int arcWidth, int arcHeight)
drawPolygon(int[] xPoints, int[] yPoints, int numPoint);

// Filling primitive shapes:
fillRect(int xTopLeft, int yTopLeft, int width, int height);
fillOval(int xTopLeft, int yTopLeft, int width, int height);
fillArc(int xTopLeft, int yTopLeft, int width, int height, int startAngle, int arcAngle);
fill3DRect(int xTopLeft, int, yTopLeft, int width, int height, boolean raised);
fillRoundRect(int xTopLeft, int yTopLeft, int width, int height, int arcWidth, int arcHeight)
fillPolygon(int[] xPoints, int[] yPoints, int numPoint);

// Drawing (or Displaying) images:
drawImage(Image img, int xTopLeft, int yTopLeft, ImageObserver obs);  // draw image with its size
drawImage(Image img, int xTopLeft, int yTopLeft, int width, int height, ImageObserver o);  // resize image on screen

---

// Graphics context's current color.
void setColor(Color c)
Color getColor()

// Graphics context's current font.
void setFont(Font f)
Font getFont()

// Set/Get the current clip area. Clip area shall be rectangular and no rendering is performed outside the clip area.
void setClip(int xTopLeft, int yTopLeft, int width, int height)
void setClip(Shape rect)
public abstract void clipRect(int x, int y, int width, int height) // intersects the current clip with the given rectangle
Rectangle getClipBounds()  // returns an Rectangle
Shape getClip()            // returns an object (typically Rectangle) implements Shape

---

void clearRect(int x, int y, int width, int height)
   // Clear the rectangular area to background
void copyArea(int x, int y, int width, int height, int dx, int dy)
   // Copy the rectangular area to offset (dx, dy).
void translate(int x, int y)
   // Translate the origin of the graphics context to (x, y). Subsequent drawing uses the new origin.
FontMetrics getFontMetrics()
FontMetrics getFontMetrics(Font f)
   // Get the FontMetrics of the current font / the specified font

import java.awt.Color;
/* provides 13 standard colors WE WILL NOT BE USING! */

RED       : java.awt.Color[r=255, g=0,   b=0]
GREEN     : java.awt.Color[r=0,   g=255, b=0]
BLUE      : java.awt.Color[r=0,   g=0,   b=255]
YELLOW    : java.awt.Color[r=255, g=255, b=0]
MAGENTA   : java.awt.Color[r=255, g=0,   b=255]
CYAN      : java.awt.Color[r=0,   g=255, b=255]
WHITE     : java.awt.Color[r=255, g=255, b=255]
BLACK     : java.awt.Color[r=0,   g=0,   b=0]
GRAY      : java.awt.Color[r=128, g=128, b=128]
LIGHT_GRAY: java.awt.Color[r=192, g=192, b=192]
DARK_GRAY : java.awt.Color[r=64,  g=64,  b=64]
PINK      : java.awt.Color[r=255, g=175, b=175]
ORANGE    : java.awt.Color[r=255, g=200, b=0]

// Constructing your own colors

Color(int r, int g, int b);             // between 0 and 255
Color(float r, float g, float b);       // between 0.0f and 1.0f
Color(int r, int g, int b, int alpha);         // between 0 and 255
Color(float r, float g, float b, float alpha); // between 0.0f and 1.0f
   // alpha of 0 for totally transparent, 255 (or 1.0f) for totally opaque
   // The default alpha is 255 (or 1.0f) for totally opaque

   // To retrieve the individual components, you can use getRed(), getGreen(), getBlue(), getAlpha()

// To set the background and foreground (text) color of a component/container, you can invoke:

   JLabel label = new JLabel("Test");
   label.setBackground(Color.LIGHT_GRAY);
   label.setForeground(Color.RED);

// To set the color of the Graphics context g (for drawing lines, shapes, and texts), use g.setColor(color):

   g.setColor(Color.RED);
   g.drawLine(10, 20, 30, 40);   // in Color.RED
   Color myColor = new Color(123, 111, 222);
   g.setColor(myColor);
   g.drawRect(10, 10, 40, 50);   // in myColor


/* 0 - Trace code and come up with questions:
        * many constants defined in class Constants
        * public int[][] cell; is a reference to a cell on the game board...
        * Game Events and Draw initialised in main:
            * draw.DrawDeltaField(gameEvents.GenerateStartField(Constants.INITIAL_BALLS));
            * GameEvents:
                * begins with an UNCHANGED_FIELD ([-1][-1] for all cells)
                * CURRENTLY ends with a field of 5 balls (INITIAL_BALLS) of colors from 1-6 amongst a field of empty cells.
            * Draw:
                * CloseOperation, MouseListener, Size, Title, Background and Visibility defined


    QUESTIONS TO SORT OUT WITHIN MY OWN UNDERSTANDING:
        * MouseListener - is it mouse only? if so, can we be more general to keep options open for different forms of input?
        * how do we ammend Draw to display grid, balls and color?

    QUESTIONS FOR ALINA:
        * I read field.cell = Constants.UNCHANGED_FIELD; as assigning all cells to -1, am I correct?
        * Why then do we use an array after? what is the reason for the differing treatment of the field.cell instance of the field class?

        * This code in GameEvents:
        Field field = new Field();
        field.cell = Constants.UNCHANGED_FIELD;
        for (int i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){
                field.cell[i][j] = 0;
        * assigns all fields in our 2D array game board to -1 and then to 0, why do we use field.cell = Constants.UNCHANGED_FIELD; and then use 2 for loops?
        * Does JFrame.addMouseListener support touchscreen? if not, should we use a more general listener instead?
        * (more for @kailan, @charles and @geremy than for you):
            * what JFrame methods do you suggest for:
                a. the drawing of the grid?
                b. the drawing of the balls?
            * how might we approach displaying the game screen? Which JFrame methods should we be paying attention to to make that happen?


*/
// 1: GameEvents
import java.util.Random;

public class GameEvents extends Solenya{
    public Field GenerateStartField (int balls){
        Field field = new Field();
        field.cell = Constants.UNCHANGED_FIELD;
        for (int i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){
                field.cell[i][j] = 0;
            }
        }
        Random random = new Random();
        int spawnedBalls = 0;
        int posX = 0;
        int posY = 0;
        while (spawnedBalls < balls){
            posX = random.nextInt(10);
            posY = random.nextInt(10);
            if(field.cell[posX][posY] < 1){
                field.cell[posX][posY] = random.nextInt(5) + 1;
                spawnedBalls++;
            }
        }
        return field;
    }
// 2: Draw
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Draw extends Solenya {
    public void DrawDeltaField(Solenya.Field field)
    {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.addMouseListener(new MouseActions());

        frame.setSize(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT);
        frame.setTitle("Lines");
        frame.setBackground(Constants.BACKGROUND_COLOR);
        frame.setVisible(true);

    }
}

// 3: how DrawDeltaField is used



 // 1 - display grid (medium)

/* Uses JFrame
*/

 // 2 - display balls on the grid (hard)



 // 3 - convert remaining color constants from String to Color type (easy)
