#include <GL/glut.h>
#include<math.h>
#include<iostream>
using namespace std;

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);

  //Horizontal line drawing algorithm
    float xs=0.4;
    float xe=0.8;
    float y=0.6;

    if (xs > xe)
    {
    float temp = xs;
      xs = xe;
      xe = temp;
    }

    float x = xs;

    glBegin(GL_POINTS);

    while(x<=xe){
        glColor3f(0,1,1);
        glVertex2f(x,y);
        x+=0.001;
    }

    glEnd();
    glFlush();

};

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
};
