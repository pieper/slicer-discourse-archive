# Centerline projection after registration

**Topic ID**: 39740
**Date**: 2024-10-17
**URL**: https://discourse.slicer.org/t/centerline-projection-after-registration/39740

---

## Post #1 by @fqzhice (2024-10-17 05:18 UTC)

<p>I extract vessel centerline by vmtk with type vtkMRMLModelNode.</p>
<p>Then i want get ijk coord for centerline projection after rigistration.</p>
<pre><code class="lang-auto">line = []  #line projection
centerlineNode = slicer.util.getNode('Centerlinemodel')  
mesh = centerlineNode.GetMesh()  
points = mesh.GetPoints()  
for id in range(points.GetNumberOfPoints()):  
point_Ras = points.GetPoint(id)  
point_ijk = self.ras2ijk(point_Ras, vessel_src_Node)  
point_kji = [point_ijk[2],point_ijk[1],point_ijk[0]]  
print('index:',point_kji)  # image coordinate position
...

    def ras2ijk(self, point_Ras, volumeNode):
        transformRasToVolumeRas = vtk.vtkGeneralTransform(
        slicer.vtkMRMLTransformNode.GetTransformBetweenNodes( volumeNode.GetParentTransformNode(),None,
                                                             transformRasToVolumeRas)
        point_VolumeRas = transformRasToVolumeRas.TransformPoint(point_Ras)
        volumeRasToIjk = vtk.vtkMatrix4x4()
        volumeNode.GetRASToIJKMatrix(volumeRasToIjk)
        point_ijk = [0, 0, 0, 1]
        volumeRasToIjk.MultiplyPoint(np.append(point_VolumeRas, 1.0), point_ijk)
        point_ijk = [int(round(c)) for c in point_ijk[0:3]]
       return point_ijk
</code></pre>
<p>Is that conversion right? point_kji get some invalid value such as minus value or value out of range.</p>

---
