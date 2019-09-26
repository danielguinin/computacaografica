from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math  
    

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

r = 2

def Esfera():

    angulo = 20

    for i in range(0, angulo):

        glBegin(GL_QUAD_STRIP)

        for j in range(0, angulo + 1):

            a = (((i*math.pi)/angulo)-(math.pi/2))
            b = ((j*math.pi)/(angulo/2))
            x = r*math.cos(a)*math.cos(b)
            y = r*math.sin(a)
            z = r*math.cos(a)*math.sin(b)

            glColor3f(1,0,0)
            glVertex3f(x,y,z)
            
            a = ((((i+1)*math.pi)/angulo)-(math.pi/2))
            x = r*math.cos(a)*math.cos(b)
            y = r*math.sin(a)
            z = r*math.cos(a)*math.sin(b)
            
            glColor3f(0,1,0)
            glVertex3f(x,y,z)

        glEnd()

        # glBegin(GL_POLYGON)
        # glBegin(GL_POINTS)
        # glBegin(GL_LINES)
        # glBegin(GL_LINE_STRIP)
        # glBegin(GL_LINE_LOOP)
        # glBegin(GL_TRIANGLES)
        # glBegin(GL_TRIANGLE_STRIP)
        # glBegin(GL_TRIANGLE_FAN)
        # glBegin(GL_QUADS)
        # glBegin(GL_QUAD_STRIP)
        # glBegin(GL_TRIANGLES)

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0)
    Esfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(40,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
