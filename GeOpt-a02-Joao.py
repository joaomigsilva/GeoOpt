"""Provides a scripting component.
    Inputs:
        m: a mesh
        s: sun vector
    Output:
        a: List of Vectors
        b: List of Points
        c: list of angles
        d: exploded mesh
        """
        
import Rhino.Geometry as rg

#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a

m.FaceNormals.ComputeFaceNormals()
a = m.FaceNormals


# #2.
# #get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
# #store the centers into a list called centers 
# #output that list to b

faces= m.Faces
centers=[]
for i in range (len(faces)):
    point= m.Faces.GetFaceCenter(i)
    centers.append(point)
    
b=centers


# #3.
# #calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
# #store the angles in a list called angleList and output it to c

angleList=[]

for normal in a:
    ang=rg.Vector3d.VectorAngle(s,normal)
    angleList.append(ang)

c = angleList


# #4. explode the mesh - convert each face of the mesh into a mesh
# #for this, you have to first copy the mesh using rg.Mesh.Duplicate()
# #then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
# #and store the result into a list called exploded in output d

exploded = []
m2 = m.Duplicate()
faces2 = m2.Faces
for mesh in range (len(faces2)):
    exp = faces2.ExtractFaces([0])
    exploded.append(exp)
d = exploded


# #after here, your task is to apply a transformation to each face of the mesh
# #the transformation should correspond to the angle value that corresponds that face to it... 
# #the result should be a mesh that responds to the sun position... its up to you!


panels= []
for i in d:
    panels.append(i.DuplicateMesh())

# print(type(a))
# print(a[3])

for i in range(len(panels)):
    angle = c[i]*15
    panels[i].Rotate(angle,a[i],b[i])
    panels[i].Transform
h= panels
