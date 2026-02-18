# VMTK Centerline Tree Model Implementation Problem

**Topic ID**: 41760
**Date**: 2025-02-18
**URL**: https://discourse.slicer.org/t/vmtk-centerline-tree-model-implementation-problem/41760

---

## Post #1 by @yoonjh119 (2025-02-18 16:39 UTC)

<p>Hello, I am implementing the centerline function of VMTK so that it can be executed with Python code. Recently, I have completed the implementation of the network model and am implementing the tree model. After loading the nifty file, I am creating polydata and obtaining the endpoint coordinates from the 3D slicer and then trying to get the centerline tree model that is the same as the slicer by inputting it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13ba3e780188da1fedbfb09977a1d0c545e795ba.png" data-download-href="/uploads/short-url/2Ow64mgmt17spzIZr7nqzf31baq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ba3e780188da1fedbfb09977a1d0c545e795ba_2_690x316.png" alt="image" data-base62-sha1="2Ow64mgmt17spzIZr7nqzf31baq" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ba3e780188da1fedbfb09977a1d0c545e795ba_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ba3e780188da1fedbfb09977a1d0c545e795ba_2_1035x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ba3e780188da1fedbfb09977a1d0c545e795ba_2_1380x632.png 2x" data-dominant-color="B9BBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2539×1164 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The code used is as follows.</p>
<pre><code class="lang-auto">import nibabel as nib
import numpy as np
import vtk
from vmtk import vtkvmtk
import vmtk.vtkvmtkMiscPython as vtkvmtkMisc
from vmtk import vmtkscripts
from vtk.util import numpy_support
import matplotlib.pyplot as plt
import pandas as pd
from vtk.util.numpy_support import vtk_to_numpy
from vtk.numpy_interface import dataset_adapter as dsa
import json
import logging
import vmtk.vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry

class endPointsMarkupsNode:
    def __init__(self):
        self.controlPoints = []
        self.selectedControlPoints = []

    def GetNumberOfControlPoints(self):
        return len(self.controlPoints)

    def AddControlPoint(self, position):
        self.controlPoints.append(position)
        self.selectedControlPoints.append(False)  # Not selected by default

    def GetNthControlPointPosition(self, index, pos):
        if index &lt; 0 or index &gt;= len(self.controlPoints):
            raise IndexError("Control point index out of range")
        pos[:] = self.controlPoints[index]

    def GetNthControlPointSelected(self, index):
        if index &lt; 0 or index &gt;= len(self.controlPoints):
            raise IndexError("Control point index out of range")
        return self.selectedControlPoints[index]

    def SetNthControlPointSelected(self, index, selected):
        if index &lt; 0 or index &gt;= len(self.controlPoints):
            raise IndexError("Control point index out of range")
        self.selectedControlPoints[index] = selected

    def RemoveNthControlPoint(self, index):
        if index &lt; 0 or index &gt;= len(self.controlPoints):
            raise IndexError("Control point index out of range")
        del self.controlPoints[index]
        del self.selectedControlPoints[index]

def extractCenterline(surfacePolyData, endPointsMarkupsNode, curveSamplingDistance=1.0):
    """Compute centerline.
    This is more robust and accurate but takes longer than the network extraction.
    :param surfacePolyData:
    :param endPointsMarkupsNode:
    :return:
    """
    capDisplacement = 0.0
    surfaceCapper = vtkvmtkComputationalGeometry.vtkvmtkCapPolyData()
    surfaceCapper.SetInputData(surfacePolyData)
    surfaceCapper.SetDisplacement(capDisplacement)
    surfaceCapper.SetInPlaneDisplacement(capDisplacement)
    surfaceCapper.Update()

    if not endPointsMarkupsNode or endPointsMarkupsNode.GetNumberOfControlPoints() &lt; 2:
        raise ValueError("At least two endpoints are needed for centerline extraction")

    tubePolyData = surfaceCapper.GetOutput()
    pos = [0.0, 0.0, 0.0]

    numberOfControlPoints = endPointsMarkupsNode.GetNumberOfControlPoints()
    foundStartPoint = False
    for controlPointIndex in range(numberOfControlPoints):
        if not endPointsMarkupsNode.GetNthControlPointSelected(controlPointIndex):
            foundStartPoint = True
            break

    sourceIdList = vtk.vtkIdList()
    targetIdList = vtk.vtkIdList()

    pointLocator = vtk.vtkPointLocator()
    pointLocator.SetDataSet(tubePolyData)
    pointLocator.BuildLocator()

    for controlPointIndex in range(numberOfControlPoints):
        isTarget = endPointsMarkupsNode.GetNthControlPointSelected(controlPointIndex)
        if not foundStartPoint and controlPointIndex == 0:
            isTarget = False
        endPointsMarkupsNode.GetNthControlPointPosition(controlPointIndex, pos)
        pointId = pointLocator.FindClosestPoint(pos)
        if isTarget:
            targetIdList.InsertNextId(pointId)
        else:
            sourceIdList.InsertNextId(pointId)

    centerlineFilter = vtkvmtkComputationalGeometry.vtkvmtkPolyDataCenterlines()
    centerlineFilter.SetInputData(tubePolyData)
    centerlineFilter.SetSourceSeedIds(sourceIdList)
    centerlineFilter.SetTargetSeedIds(targetIdList)
    centerlineFilter.SetRadiusArrayName("Radius")
    centerlineFilter.SetCostFunction('1/R')  # this makes path search prefer go through points with large radius
    centerlineFilter.SetFlipNormals(False)
    centerlineFilter.SetAppendEndPointsToCenterlines(0)
    centerlineFilter.SetSimplifyVoronoi(False)
    centerlineFilter.SetCenterlineResampling(False)
    centerlineFilter.SetResamplingStepLength(curveSamplingDistance)
    centerlineFilter.Update()

    if not centerlineFilter.GetOutput():
        raise ValueError("Failed to compute centerline (no output was generated)")
    centerlinePolyData = vtk.vtkPolyData()
    centerlinePolyData.DeepCopy(centerlineFilter.GetOutput())

    if not centerlineFilter.GetVoronoiDiagram():
        raise ValueError("Failed to compute centerline (no Voronoi diagram was generated)")
    voronoiDiagramPolyData = vtk.vtkPolyData()
    voronoiDiagramPolyData.DeepCopy(centerlineFilter.GetVoronoiDiagram())

    return centerlinePolyData, voronoiDiagramPolyData

# Path to NIfTI file
input_nifti_01 = 'combined_mask_02.nii.gz'
msk_name_01 = 'output_mask_poly.vtk'

nifti_img = nib.load(input_nifti_01)
data = nifti_img.get_fdata()

reader = vtk.vtkNIFTIImageReader()
reader.SetFileName(input_nifti_01)
reader.Update()

affine = nifti_img.affine


# Create numpy arrays for start and end points (LPS coordinates)
startPoint = [-1.96, -153.29446411132812, 379.3500061035156]
endPoint = [-10.934102058410645, -171.96652221679688, 319.4288635253906]


# Read NIfTI file into VTK
reader = vtk.vtkNIFTIImageReader()
reader.SetFileName(input_nifti_01)
reader.Update()

cast = vtk.vtkImageCast()
cast.SetInputData(reader.GetOutput())
cast.SetOutputScalarTypeToFloat()
cast.Update()

mc = vtk.vtkMarchingCubes()
mc.SetInputData(cast.GetOutput())
mc.ComputeNormalsOn()
mc.SetValue(0, 0.5)
mc.Update()

transform = vtk.vtkTransform()
transform.Scale(-1.0, -1.0, 1.0)  # RAS to LPS
if reader.GetQFormMatrix():
    transform.Concatenate(reader.GetQFormMatrix())
elif reader.GetSFormMatrix():
    transform.Concatenate(reader.GetSFormMatrix())

tpd = vtk.vtkTransformPolyDataFilter()
tpd.SetInputData(mc.GetOutput())
tpd.SetTransform(transform)
tpd.Update()

# Clean and triangulate
cleaner = vtk.vtkCleanPolyData()
cleaner.SetInputData(tpd.GetOutput())

triangleFilter = vtk.vtkTriangleFilter()
triangleFilter.SetInputConnection(cleaner.GetOutputPort())
triangleFilter.Update()
simplifiedPolyData = triangleFilter.GetOutput()

writer = vtk.vtkPolyDataWriter()
writer.SetInputData(simplifiedPolyData)
writer.SetFileName(msk_name_01)
writer.Update()


# Add start and end points to the markup node
endPointsNode = endPointsMarkupsNode()
endPointsNode.AddControlPoint(startPoint)
endPointsNode.SetNthControlPointSelected(0, False)
endPointsNode.AddControlPoint(endPoint)
endPointsNode.SetNthControlPointSelected(1, True)

# Extract centerline
centerlinePolyData, voronoiDiagramPolyData = extractCenterline(simplifiedPolyData, endPointsNode)

# Save results (e.g., as VTK files)
writer = vtk.vtkPolyDataWriter()
writer.SetFileName("centerline.vtk")
writer.SetInputData(centerlinePolyData)
writer.Write()

writer.SetFileName("voronoi_diagram.vtk")
writer.SetInputData(voronoiDiagramPolyData)
writer.Write()

print("Centerline extraction completed and saved to 'centerline.vtk' and 'voronoi_diagram.vtk'")

</code></pre>
<p>However, the following error occurs and it does not proceed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b407213c7c87d544102d063f5cb6520b0f93ce11.jpeg" data-download-href="/uploads/short-url/pGBdEInfZUz3ZTVPvS4lDYRPYaZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b407213c7c87d544102d063f5cb6520b0f93ce11_2_640x500.jpeg" alt="image" data-base62-sha1="pGBdEInfZUz3ZTVPvS4lDYRPYaZ" width="640" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b407213c7c87d544102d063f5cb6520b0f93ce11_2_640x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b407213c7c87d544102d063f5cb6520b0f93ce11_2_960x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b407213c7c87d544102d063f5cb6520b0f93ce11_2_1280x1000.jpeg 2x" data-dominant-color="E4E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×1125 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there a solution to this? The same problem occurs not only in the extractCenterline function but also in the previous version, computecenterline. Thank you.</p>

---
