void setup(){
  size(1000,650);
  ellipseMode(CENTER);
}

float anguloTerra = PI;
float annguloLua = PI;

void draw (){
  background(0,0,0);
  translate(width/2,height/2);

  //Cria Sol
  fill(255, 255, 51);
  ellipse(0, 0, 200, 200);
  
  //Cria Terra
  float xT= 250*sin(anguloTerra);
  float yT= 250*cos(anguloTerra);
  
  fill(153, 51, 255);
  ellipse(xT, yT, 70, 70);
  
  anguloTerra += PI/1000;
  
  //Cria Lua
  float xL = xT+70 * sin(annguloLua);
  float yL = yT+70 * cos(annguloLua);
  
  fill(160, 160, 160);
  ellipse(xL, yL, 30, 30);
  
  annguloLua += PI/100;
}
