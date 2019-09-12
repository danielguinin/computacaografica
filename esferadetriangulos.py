from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math  
    

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )


r = 2

# def makeVertice():
    
#     pontos = []

#     # a = 2*math.pi/n
#     # -((math.pi)/2) ((math.pi)/2) 2*math.pi

#     angulo = 40

#     for i in range(0, angulo):

#         pontos = []

#         for j in range(0, angulo):
#             a = (((i*math.pi)/angulo)-(math.pi/2))
#             b = ((j*math.pi)/(angulo/2))
#             x = r*math.cos(a)*math.cos(b)
#             y = r*math.sin(a)
#             z = r*math.cos(a)*math.sin(b)
#             pontos += [[x,y,z]]

#         glBegin(GL_POLYGON)
#         for i in range(0, len(pontos)):
#             glColor3fv(cores[i%len(cores)])
#             glVertex3fv(pontos[i])
#         glEnd()

#     return pontos

# vertices = makeVertice()


def Cubo():
    

    pontos = []

    # a = 2*math.pi/n
    # -((math.pi)/2) ((math.pi)/2) 2*math.pi

    angulo = 40

    for i in range(0, angulo):

        pontos = []

        for j in range(0, angulo):
            a = (((i*math.pi)/angulo)-(math.pi/2))
            b = ((j*math.pi)/(angulo/2))
            x = r*math.cos(a)*math.cos(b)
            y = r*math.sin(a)
            z = r*math.cos(a)*math.sin(b)
            pontos += [[x,y,z]]

        # glBegin(GL_POLYGON)
        # glBegin(GL_POINTS)
        # glBegin(GL_LINES)
        # glBegin(GL_LINE_STRIP)
        # glBegin(GL_LINE_LOOP)
        glBegin(GL_TRIANGLES)
        # glBegin(GL_TRIANGLE_STRIP)
        # glBegin(GL_TRIANGLE_FAN)
        # glBegin(GL_QUADS)
        # glBegin(GL_QUAD_STRIP)
        # glBegin(GL_TRIANGLES)
        for k in range(0, len(pontos)):
            glColor3fv(cores[j%len(cores)])
            glVertex3fv(pontos[k])
        glEnd()




    # i = 0
    # # facesTri = makeFacesTri(n)
    # for face in facesTri:
    #     glColor3fv(cores[i%len(cores)])
    #     for vertex in face:
    #         #glColor3fv(cores[vertex])
    #         glVertex3fv(vertices[vertex])
    #     i = i+1
    # glEnd()

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

