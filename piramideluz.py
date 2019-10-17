from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math
import sys
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

n = 70
r = 3

def makeVertice(n):

	pontos = []

	a = 2*math.pi/n
	
	for i in range(0,n):
		x = r*math.cos(i*a)
		y = 0
		z = r*math.sin(i*a)
		pontos += [[x,y,z]]
	
	pontos += [[0,3,0]]		
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
		pontos += [[i,i+1, n]]
	pontos += [[n-1, 0, n]]
	
	return pontos

facesTri = makeFacesTri(n)
 
def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)
 
def Cubo():
    glBegin(GL_QUADS)
    for face in faces:
        glNormal3fv(calculaNormalFace(face))
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    
def Cubo():
    # vertices = makeVertice(n)
    glBegin(GL_POLYGON)

    for i in range(0, n):
        glVertex3fv(vertices[i])

    glEnd()

    
    glBegin(GL_TRIANGLES)
    i = 0
    # facesTri = makeFacesTri(n)
    for face in facesTri:
        # glColor3fv(cores[i%len(cores)])
        glNormal3fv(calculaNormalFace(face))
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()
 
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Cubo()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,10,0,0,0,0,1,0)
 
def init():
#    mat_ambient = (0.0, 0.0, 0.5, 1.0)
    mat_ambient = (0.8, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    mat_shininess = (100,)
    light_position = (0, 8, 0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
 
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Cubo")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()
 
main()
