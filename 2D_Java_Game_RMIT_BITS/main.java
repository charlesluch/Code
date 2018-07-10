import DrawDeltaField;

import java.lang.String;
import java.util.Random;

class Solenya{
        public static final class Constants {
                public static final String[] COLORS = {"#000000", "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF"};
                public static final int[][]UNCHANGED_FIELD = new int[][]{
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1}
                };
                public static final String BACKGROUND_COLOR = "#DCDCDC";
                public static final String HIGHLIGHT_COLOR = "#AFFFAF";
                public static final String SCORE_COLOR = "#FFDF00";
                public static final int INITIAL_BALLS = 5;
        }

        public class Field{
            public int[][] cell;
        }

        public class GameEvents{
                public Field GenerateStartField (int balls){
                        Field field = new Field();
                        for (int i = 0, i < 10, i++){
                                for (int j = 0, i < 10, j++){
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
                                if(field.cell[posX][posY] != 0){
                                        field.cell[posX][posY] = random.nextInt(5) + 1;
                                        spawnedBalls++;
                                }
                        }
                        return field;
                }
        }

        public static void main(String[] args) {
                GameEvents gameEvents = new GameEvents();
                DrawDeltaField drawDeltaField = new DrawDeltaField();
                drawDeltaField(gameEvents.GenerateStartField(Constants.INITIAL_BALLS))
        }
}
