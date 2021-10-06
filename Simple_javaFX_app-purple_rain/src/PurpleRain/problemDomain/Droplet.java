package PurpleRain.problemDomain;

import java.time.YearMonth;
import java.util.Map;
import java.util.Random;

import javafx.scene.paint.Color;
import javafx.scene.shape.Line;

public class Droplet{

    private float x;
    private float y;
    private float z;
    private float speed;
    private float lineLength;
    private float thickness;
    private Line line;
   
    

    
    private final float WIDTH_OF_RAIN = 1;
    private final int MAX_SPEED = 4;

    private final float STARTY = 0;
    private final int MAX_WIDTH = 800;

    public Droplet() {
    }
    public float getSpeed() {
        return speed;
    }
    public void setSpeed(float speed) {
        this.speed = speed;
    }
    public float getX() {
        return x;
    }
    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }
    public void setY(float y) {
        this.y = y;
    }
    public Droplet(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public void Initialize(){
        Random rand = new Random();
        Random randSpeed = new Random();
        int xStartPosition = rand.nextInt(MAX_WIDTH);
        float speed_of_droplet = randSpeed.nextInt(400);
        speed_of_droplet = speed_of_droplet/100;
        speed = speed_of_droplet;

        x = xStartPosition;
        int low = -400;
        int high = -100;
        int result = rand.nextInt(high-low) + low;
        y = result;

        int zMax = 20;
        int zMin = 0;
        z = rand.nextInt(zMax - zMin) + zMin;

        lineLength = map(z,0,20,10,20);
        speed = map(z,0,20,4,0);
        thickness = map(z,0,20,1,2);
    }

    private float map(float chosenNumber, int i, int j, int k, int l) {
        float diff1 = j-i;
        float diff2 = l-k;
        float fraction = diff2/diff1;
        float answer = k+(chosenNumber*fraction);
        return answer;
    }


    public void DrawDroplet(){
        line = new Line(x, y, x, y+lineLength);
        line.setStrokeWidth(thickness);
        String rgb = "138, 43, 226";
        line.setStyle("-fx-stroke: rgba(" + rgb + ", 1.0);");
    }
    public Line getLine(){
        return line;
    }

    public float DropletFalls(float y){
        float updateY = y+1;
        return updateY;
    }



}