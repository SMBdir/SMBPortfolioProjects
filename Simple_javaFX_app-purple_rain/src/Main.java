import javafx.scene.Group;
import javafx.scene.Scene;

import java.util.ArrayList;

import PurpleRain.problemDomain.Droplet;
import javafx.animation.PathTransition;
import javafx.application.Application;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.util.Duration;
import javafx.scene.shape.Line;


public class Main extends Application {
    @Override
    public void start(Stage stage) {

        Group root = new Group();

        ArrayList<Droplet> droplets = new ArrayList<>();
        
        for(int i=0; i<500; i++){
            Droplet newDroplet = new Droplet();
            newDroplet.Initialize();
            newDroplet.DrawDroplet();
            Line newLine = newDroplet.getLine();
            droplets.add(newDroplet);
            
            root.getChildren().add(newLine);

            Line path = new Line(newDroplet.getX(), newDroplet.getY(),newDroplet.getX(), newDroplet.getY()+1000 );
            PathTransition newTransition = new PathTransition();
            newTransition.setNode(newLine);
            newTransition.setDuration(Duration.seconds(newDroplet.getSpeed()));
            newTransition.setPath(path);
            newTransition.setCycleCount(PathTransition.INDEFINITE);
            newTransition.play();
        }

  
        Scene scene = new Scene(root,Color.rgb(230, 230, 250));
    
        stage.setTitle("Purple Rain");
        stage.setWidth(800);
        stage.setHeight(600);
        stage.setResizable(false);


        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

    public void Update(){

    }
}
