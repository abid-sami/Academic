#include <GL/glut.h>
#include<math.h>
#include <algorithm>
using namespace std;

void dda(float xa, float ya, float xb, float yb){
    float xs = xa, ys = ya, xe = xb, ye = yb;
    float m = (ye - ys)/(xe - xs);

    if (m<1){
        if(xs>xe){
            swap(xs,xe);
            swap(ys,ye);
        }
        float x= xs, y = ys;
        glBegin(GL_POINTS);

        while(x <= xe){
           glColor3f(1,0,1);
           glVertex2i(x,y);
           x = x+1;
           y = y+m;
           y = round(y);
        }
        glEnd();
    }
    else if(m>1){
        if(ys>=ye){
            swap(xs,xe);
            swap(ys,ye);
        }
        float x= xs, y = ys;
        glBegin(GL_POINTS);
        while(y <= ye){
           glColor3f(1,0,1);
           glVertex2i(x,y);
           y = y+1;
           x = x+(1/m);
           x = round(x);
        }
        glEnd();
    }
}



void display(){
  glClear(GL_COLOR_BUFFER_BIT);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(0,640,0,640);
  glPointSize(2.0);
  dda(20,30,300,200);
  glFlush();
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitWindowSize(640,480);
    glutInitWindowPosition(10,10);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH);

    glutCreateWindow("GLUT Shapes");

    glutDisplayFunc(display);

    glutMainLoop();

    return EXIT_SUCCESS;
}
