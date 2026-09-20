#include <GL/glut.h>
#include <math.h>
#include <iostream>
using namespace std;

void DCirkel()
{
    glBegin(GL_POINTS);

    float r = 100;
    float x = 0, y = r;

    while (x <= r)
    {
        glColor3f(0, 1, 1);

        glVertex2f(x, y);
        glVertex2f(x, -y);
        glVertex2f(-x, -y);
        glVertex2f(-x, y);

        x += 0.5;
        y = sqrt(r * r - x * x);
    }

    glEnd();
}

void display()
{

    glClearColor(1.0, 1.0, 1.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(320, -320, 240, -240);

    DCirkel();

    glFlush();
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);

    glutInitWindowSize(620, 400);
    glutInitWindowPosition(100, 100);

    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

    glutCreateWindow("Circle Drawing Algorithms");

    glutDisplayFunc(display);

    glutMainLoop();

    return 0;
}
