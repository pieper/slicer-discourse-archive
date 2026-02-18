# Resolution of the "Draw" effect

**Topic ID**: 34513
**Date**: 2024-02-24
**URL**: https://discourse.slicer.org/t/resolution-of-the-draw-effect/34513

---

## Post #1 by @yaraabdelazim (2024-02-24 02:02 UTC)

<p>Hello,</p>
<p>I am new at 3D slicer but I am trying to improve the resolution of the line drawn with the Draw effect in the SegmentEditor module by interpolating between two consecutive points so that the line or the shape drawn can appear to have a higher resolution and less pixelated. However, when I do that, I don’t get any errors relating to the code but I don’t notice any difference in the line drawn and the pixelation appears to be the same. Is there a better way to improve pixelation that I am perhaps unaware of? Should I be accessing the cells from the polyData attribute and changing its size ?</p>
<p>Here is my interpolation method:<br>
def interpolatePoints(self, point1, point2, numPoints=10):</p>
<pre><code>    """
    Interpolate numPoints equally spaced points between point1 and point2
    """
    pts = []
    for i in range(numPoints):
        t = i / (numPoints - 1) # t va de 0 à 1
        point = np.array(point1)*(1-t) + np.array(point2)*t  # interpolation linéaire
        pts.append(point.tolist())

    return pts
</code></pre>
<p>I call it in the apply method like so:</p>
<pre><code>def apply(self):
    lines = self.polyData.GetLines()
    lineExists = lines.GetNumberOfCells() &gt; 0
    if lineExists:
        # Close the polyline back to the first point
        idList = vtk.vtkIdList()
        idList.InsertNextId(self.polyData.GetNumberOfPoints() - 1)
        idList.InsertNextId(0)
        self.polyData.InsertNextCell(vtk.VTK_LINE, idList)

        # Get modifier labelmap qui représente la segmentation actuelle
        modifierLabelmap = self.scriptedEffect.defaultModifierLabelmap() 

        # Apply poly data on modifier labelmap
        segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()

        # Interpolation before applying mask
        for i in range(1, self.rasPoints.GetNumberOfPoints()):   
            lastPoint = self.rasPoints.GetPoint(i)
            firstPoint = self.rasPoints.GetPoint(i - 1)
            interpolatedPoints = self.interpolatePoints(firstPoint, lastPoint)
            for point in interpolatedPoints:
                self.rasPoints.InsertNextPoint(point)

        # Appliquer le polydata sur le modifierLabelmap en utilisant la méthode appendPolyMask qui permet d'ajouter le tracé à la segmentation
        num_cells = self.polyData.GetNumberOfCells()
        print(f"Number of cells in polyData: {num_cells}")

        
        # Access the cells in the polydata
        cellArray = self.polyData.GetLines()
   
        # Iterate through cells and get their size
        for cellId in range(cellArray.GetNumberOfCells()):
            cellSize = cellArray.GetCellSize(cellId)
            print(f"Size of cell {cellId}: {cellSize}")

        self.scriptedEffect.appendPolyMask(modifierLabelmap, self.polyData, self.sliceWidget, segmentationNode)

    self.resetPolyData()
    if lineExists:
        self.scriptedEffect.saveStateForUndo()
        self.scriptedEffect.modifySelectedSegmentByLabelmap(modifierLabelmap, slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeAdd)
</code></pre>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2024-02-24 02:09 UTC)

<p>Appearance of the line looks pixelated because no antialiasing is used in the slice views. It is not easy to get antialiasing work in current VTK version - see <a href="https://discourse.vtk.org/t/vtk-9-broken-lines/13288" class="inline-onebox">VTK 9 broken lines - Support - VTK</a></p>
<p>Blocky appearance of the segmentation (after the drawn line disappears) is due to the finite resolution of thr segmentation. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">this documentation</a> section for more details.</p>

---

## Post #3 by @yaraabdelazim (2024-02-26 08:57 UTC)

<p>Thank you for your response. I was wondering if it was possible to change the spacing in the code then so that I don’t have to do it everytime when I’m using the “Draw” effect. However, when I attempt to do that, the volume appears stretched out or compressed. Here’s how I do it:</p>
<p>class DrawPipeline:<br>
“”“Visualization objects and pipeline for each slice view for drawing”“”</p>
<pre><code>def __init__(self, scriptedEffect, sliceWidget):
    self.scriptedEffect = scriptedEffect
    self.sliceWidget = sliceWidget
    self.activeSliceOffset = None
    self.lastInsertSliceNodeMTime = None
    self.actionState = None

    self.xyPoints = vtk.vtkPoints()
    self.rasPoints = vtk.vtkPoints()
    self.polyData = self.createPolyData()

    self.mapper = vtk.vtkPolyDataMapper2D()
    # self.mapper.TransformCoordinateUseDoubleOn()
    self.actor = vtk.vtkTexturedActor2D()
    self.mapper.SetInputData(self.polyData)
    self.actor.SetMapper(self.mapper)
    actorProperty = self.actor.GetProperty()
    actorProperty.SetColor(1, 1, 0)
    actorProperty.SetLineWidth(0.1)

    self.createStippleTexture(0xAAAA, 8)
      
    volumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
    # Définir la taille des pixels
    volumeNode.SetSpacing(1.0, 1.0, 1.5)
</code></pre>

---

## Post #4 by @lassoan (2024-02-26 21:37 UTC)

<p>You can use this <a href="https://slicer.readthedocs.io/en/5.6/developer_guide/script_repository.html#resample-segmentation-to-higher-resolution">code snippet in the script repository</a> to resample a segmentation to higher resolution. This should not be done in a segment editor effect, but anytime after you created the segmentation node.</p>
<p>An alternative is to crop and resample the input volume before starting segmentation. This makes things a bit simpler, as the segmentation resolution will match the volume resolution. Cropping the image to the relevant region at the same time when you are resampling can help keeping memory usage at a level that your computer can still handle. For example, oversampling a volume by a factor of 2 will increase memory usage by 8x; oversampling by 4x will increase memory usage by 64x. So, if you don’t crop the input image to the minimum necessary size then the image that your computer could handle with 16GB RAM, after 4x oversampling may need 1TB RAM.</p>

---

## Post #5 by @yaraabdelazim (2024-02-27 08:54 UTC)

<p>Thank you, that was very helpful !</p>

---
