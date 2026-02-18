# Load DICOM Surface Segmentation Objects

**Topic ID**: 1125
**Date**: 2017-09-26
**URL**: https://discourse.slicer.org/t/load-dicom-surface-segmentation-objects/1125

---

## Post #1 by @juliaH (2017-09-26 14:59 UTC)

<p>Slicer version: 4.6.2</p>
<p>Hi,<br>
I just wondered, if there is any possibility to load DICOM Surface Segmentation Objects, as described in the DICOM Supplement 132 with the 3D Slicer.</p>
<p>Thank you in advance! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Best regards<br>
Julia</p>

---

## Post #2 by @pieper (2017-09-26 18:12 UTC)

<p>Hi Julia -</p>
<p>I wrote a first version that worked well on a sample dataset:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py" target="_blank" rel="nofollow noopener">pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py</a></h4>
<pre><code class="lang-py">import glob, os, json
from datetime import datetime
import string
import vtk, qt, ctk, slicer
from DICOMLib import DICOMPlugin
from DICOMLib import DICOMLoadable
import logging

#
# This is the plugin to handle translation of DICOM Surface SEG objects
#

class DICOMSurfaceSegmentationPluginClass(DICOMPlugin):

  def __init__(self,epsilon=0.01):
    super(DICOMSurfaceSegmentationPluginClass,self).__init__()
    self.loadType = "DICOMSurfaceSegmentation"

    self.surfaceSegmentationSOPClassUID = "1.2.840.10008.5.1.4.1.1.66.5"

</code></pre>

  This file has been truncated. <a href="https://github.com/pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>it should work to add this as loadable module.</p>
<p>I didn’t have any sharable sample data at the time so I didn’t add this to the core.  But I’d like to finish this sometime so if you have any example data to share testing/debugging that would be great.</p>

---

## Post #3 by @Sebastian_Hilbert (2018-06-30 14:02 UTC)

<p>I did not yet get the plugin working in slicer but managed to produce working code with the massive help of the author of the aliza dicom viewer.</p>
<p>It imports a <a href="https://dicom.innolitics.com/ciods/surface-segmentation" rel="nofollow noopener">dicom surface segmentation</a> and writes it to a vtk and stl file. The key part was to subtract 1 for the indices</p>
<p>polys.InsertCellPoint(index-1)</p>
<p>The dicom file to test this was created on a Siemens syngo workstation. I hope this helps. Would love to see this working in Slicer.</p>
<pre><code>import glob, os, json
from datetime import datetime
import string
import vtk
import logging


def load(loadable):
    import dicom
    dataset = dicom.read_file(loadable)
    loadSurfaceSegmentationDataset(dataset)

def loadSurfaceSegmentationDataset(dataset):
    for surface in dataset.SurfaceSequence:
      coordinates = surface.SurfacePointsSequence[0].PointCoordinatesData

      # generate points
      points = vtk.vtkPoints()
      polyData = vtk.vtkPolyData()
      polyData.SetPoints(points)

      for pointIndex in xrange(len(coordinates)/3):
        pointStart = pointIndex*3
        point = coordinates[pointStart:pointStart+3]
        point[0] *= -1
        point[1] *= -1
        points.InsertNextPoint(*point)

      polys = vtk.vtkCellArray()
      polyData.SetPolys(polys)

      # generate triangles
      extremes = [100,1]
      triIndices = surface.SurfaceMeshPrimitivesSequence[0].TrianglePointIndexList
      triangles = len(triIndices)/6
      for triangle in range(triangles):
        polys.InsertNextCell(3)
        for vertex in range(3):
          vertexIndex = 6*triangle + 2*vertex;
          low = ord(triIndices[vertexIndex])
          high = ord(triIndices[vertexIndex+1])
          index = (high &lt;&lt; 8) + low
          polys.InsertCellPoint(index-1)

          if index &lt; extremes[0]:
            extremes[0] = index
          if index &gt; extremes[1]:
            extremes[1] = index

    # visualization
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polyData)

    print polyData

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(255,255,255)

    ren=vtk.vtkRenderer()
    renWin=vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren=vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    ren.AddActor(actor)
    ren.SetBackground(0.1, 0.2, 0.4)
    renWin.SetSize(200, 200)

    iren.Initialize()

    ren.ResetCamera()
    ren.ResetCameraClippingRange()

    renWin.SetSize(800,600)
    renWin.Render()

    iren.Start()

    # build vtk file
    writer = vtk.vtkPolyDataWriter()
    writer.SetInputData(polyData)
    output_path = "test"
    writer.SetFileName(output_path + '.vtk')
    writer.Write()

    # build stl file
    surface_filter = vtk.vtkDataSetSurfaceFilter()
    surface_filter.SetInputData(polyData)

    triangle_filter = vtk.vtkTriangleFilter()
    triangle_filter.SetInputConnection(surface_filter.GetOutputPort())

    writer = vtk.vtkSTLWriter()
    writer.SetFileName(output_path + '.stl')
    writer.SetInputConnection(triangle_filter.GetOutputPort())
    writer.SetFileTypeToBinary()
    writer.Write()

###########################################################################################
if __name__ == "__main__":

    load('LASegSample.dcm')</code></pre>

---

## Post #4 by @Sebastian_Hilbert (2018-06-30 16:23 UTC)

<p>Just one more thing. There is a surfaces.dcm out in the wild that serves as as test file. It is referenced in this thread.</p>
<p><a href="https://groups.google.com/forum/#!topic/comp.protocols.dicom/3mhBWlLZSuM" class="onebox" target="_blank" rel="nofollow noopener">https://groups.google.com/forum/#!topic/comp.protocols.dicom/3mhBWlLZSuM</a></p>
<p>Be careful with this file. Indices seem to be off. To avoid confusion always work with files directly exported from software such as Syngo (Siemens).</p>

---

## Post #5 by @Mihail_Isakov (2018-06-30 17:29 UTC)

<p>Hi.<br>
Confirm. Indices must start with 1, not with 0 like in ‘surfaces.dcm’ i found somewhere and first used as reference too, Problem is too few example files. Many thanks to Sebastian Hilbert for sharing a real sample from Siemens Workstation.</p>
<p>DICOM PS3.3 C.27.2.1.1 Point Coordinates Data<br>
“When referencing individual points the index of the first point shall be 1.”<br>
<a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.27.2.html#sect_C.27.2.1.1" class="onebox" target="_blank" rel="nofollow noopener">http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.27.2.html#sect_C.27.2.1.1</a></p>
<p>And ‘surfaces.dcm’ hat 32 bit int in Triangle Point Index List OW VR too. Both.</p>
<p>BTW. Attribute Triangle Point Index List is retired.<br>
PS3.3 C.27.4.1 Surface Mesh Primitives Macro Attribute Descriptions<br>
“In a previous edition, other Attributes were used that had an OW VR and a limitation to no more than 65535 points per surface. These have been retired and replaced with new Attributes. See PS 3.3 2014a.”<br>
New attribute for triangle index list is “Long Triangle Point Index List” (0066,0041). But is not so critical.</p>
<p>Best Regards,<br>
M</p>

---

## Post #6 by @Mihail_Isakov (2018-07-01 05:48 UTC)

<p>Siemens SEG <a href="https://drive.google.com/file/d/1cGMkOZVf7x3orOKYEBB8lMjfsYTwRPVj/view?usp=sharing" rel="nofollow noopener">LASegSample.dcm</a></p>

---

## Post #7 by @issakomi (2025-03-06 09:30 UTC)

<p>Updated the link in the post above.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1SmkP93YHf0Sq1pYBNjFJyewmAhdP1Omk/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1SmkP93YHf0Sq1pYBNjFJyewmAhdP1Omk/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1SmkP93YHf0Sq1pYBNjFJyewmAhdP1Omk/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1SmkP93YHf0Sq1pYBNjFJyewmAhdP1Omk/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">LASegSample.dcm</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
