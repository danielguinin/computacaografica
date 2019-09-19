from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math  
    

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )


def f(x, y):
    # return (x**2 + y**2)**(1/2)
    # return 1-abs(x+y)-abs(y-x)
    # return math.log(x**2+y**2)
    return 1-abs(y)
    # return (math.sin(5*x))*((math.cos(5*y))/5)
    # return math.sin(10*(x**2+y**2))/10


def Figura():

    n = 20

    yInicial = -1.5
    yFinal = 1.5
    xInicial = -1.5
    xFinal = 1.5

    deltaY = (yFinal - yInicial)/n
    deltaX = (xFinal - xInicial)/n

    y = yInicial

    while y < yFinal:
        x = xInicial
        # glBegin(GL_QUAD_STRIP)
        # glBegin(GL_POLYGON)
        # glBegin(GL_POINTS)
        # glBegin(GL_LINES)
        # glBegin(GL_LINE_STRIP)
        # glBegin(GL_LINE_LOOP)
        # glBegin(GL_TRIANGLES)
        # glBegin(GL_TRIANGLE_STRIP)
        # glBegin(GL_TRIANGLE_FAN)
        # glBegin(GL_QUADS)
        glBegin(GL_QUAD_STRIP)
        # glBegin(GL_TRIANGLES)

        pontos = []

        while x < xFinal:
            pontos += [[x, y, f(x,y)]]
            pontos += [[x, y + deltaY, f(x, y + deltaY)]]
            x += deltaX

        for k in range(0, len(pontos)):
            glColor3f(0,abs(2.0*x)/(xFinal-xInicial),abs(2.0*y)/(yFinal-yInicial))
            glVertex3fv(pontos[k])

        glEnd()

        y += deltaY


def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0)
    Figura()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("FIGURA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(40,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()

