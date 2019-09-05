from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math  
    

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

n = 6
r = 2
h = 2

def makeVertice(n):

	pontos = []

	a = 2*math.pi/n
	
	for i in range(0,n):
		x = r*math.cos(i*a)
		y = 0
		z = r*math.sin(i*a)
		pontos += [[x,y,z]]

	for j in range(0,n):
		x = r*math.cos(j*a)
		y = h
		z = r*math.sin(j*a)
		pontos += [[x,y,z]]

	return pontos

vertices = makeVertice(n)
		
def makeLinhas(n):

	pontos = []
	
	for i in range (0,n-1):
		pontos += [[i,i+1]]
	pontos += [[0, n-1]]
	
	for i in range (0,n):
		pontos += [[i,n]]
	
	return pontos


def makeFacesTri(n):

	pontos = []
	
	for i in range (0, n-1):
		pontos += [[i,i+1, i + n + 1, i + n]]
	pontos += [[n-1, 0, n, (n*2)-1]]
	
	return pontos

facesTri = makeFacesTri(n)

def Cubo():
    # vertices = makeVertice(n)
    glBegin(GL_POLYGON)

    for i in range(0, n):
        glVertex3fv(vertices[i])
    glEnd()

    
    glBegin(GL_POLYGON)
    i = 0
    # facesTri = makeFacesTri(n)
    for face in facesTri:
        glColor3fv(cores[i%len(cores)])
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    # glColor3fv((0,0.5,0))
    # glBegin(GL_LINES)
    # linhas = makeLinhas(n)
    # for linha in linhas:
    #     for vertice in linha:
    #         glVertex3fv(vertices[vertice])
    # glEnd()

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
