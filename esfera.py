from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math  
    

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

r = 2

def makeVertice():
    
    pontos = []

    # a = 2*math.pi/n
    # -((math.pi)/2) ((math.pi)/2) 2*math.pi

    angulo = 40

    for i in range(0, angulo):
        for j in range(0, angulo):
            a = (((i*math.pi)/angulo)-(math.pi/2))
            b = ((j*math.pi)/(angulo/2))
            x = r*math.cos(a)*math.cos(b)
            y = r*math.sin(a)
            z = r*math.cos(a)*math.sin(b)
            pontos += [[x,y,z]]

    return pontos

vertices = makeVertice()


def Cubo():
    # glBegin(GL_POINTS)
    # glBegin(GL_LINES)
    # glBegin(GL_LINE_STRIP)
    # glBegin(GL_LINE_LOOP)
    # glBegin(GL_TRIANGLES)
    # glBegin(GL_TRIANGLE_STRIP)
    # glBegin(GL_TRIANGLE_FAN)
    # glBegin(GL_QUADS)
    # glBegin(GL_QUAD_STRIP)
    glBegin(GL_POLYGON)

    for i in range(0, len(vertices)):
        glColor3fv(cores[i%len(cores)])
        glVertex3fv(vertices[i])

    glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0)
    Cubo()
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

