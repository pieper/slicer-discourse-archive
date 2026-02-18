# Problems applying texture to model in 4.11 version

**Topic ID**: 12180
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/problems-applying-texture-to-model-in-4-11-version/12180

---

## Post #1 by @lauraflores98 (2020-06-23 17:22 UTC)

<p>Operating system: macOS catalina 10.15.3<br>
Slicer version: 4.11.0<br>
Expected behavior:</p>
<p>I’m programming an extension.<br>
On it, I load a back scan (both the volume as a .obj  and the texture as .jpg) and later on apply the texture to the model.<br>
I do this with the following code:</p>
<p><strong>The button I use:</strong></p>
<pre><code>  def onLoad3DModel(self):
    logic = ScoliosisAnalysisLogic()
    self.modelNode, self.textureImageNode, valid = logic.Load3DModel(self.ui.dir3Dmodel.currentPath)
    if not self.modelNode or not self.textureImageNode:
        # keep disabled apply texture
        self.ui.ApplyTexture.enabled = valid
</code></pre>
<p><strong>where I load the files</strong></p>
<pre><code>   def Load3DModel(self, dir):
    # finds in the directory files with the extension .obj and .jpg
    valid = True
    for file in os.listdir(dir):
        if file.endswith(".obj"):
            path_obj = os.path.join(dir, file)
        if file.endswith(".jpg"):
            path_jpg = os.path.join(dir, file)
    try:
        [success, modelNode] = slicer.util.loadModel(path_obj, returnNode=True)
    except:
        modelNode = None
        valid = False
    try:
        [success, textureImageNode] = slicer.util.loadVolume(path_jpg, returnNode=True)
    except:
        textureImageNode = None
        valid = False
    return modelNode, textureImageNode, valid
</code></pre>
<p><strong>where I apply the texture</strong></p>
<pre><code>def onApplyTexture(self):
    logic.ShowTextureOnModel(self.modelNode, self.textureImageNode)
    logic.ConvertTextureToPointAttribute(self.modelNode, self.textureImageNode)

def ShowTextureOnModel(self, modelNode, textureImageNode):
    modelDisplayNode = modelNode.GetDisplayNode()
    modelDisplayNode.SetBackfaceCulling(0)
    textureImageFlipVert = vtk.vtkImageFlip()
    textureImageFlipVert.SetFilteredAxis(1)
    textureImageFlipVert.SetInputConnection(textureImageNode.GetImageDataConnection())
    modelDisplayNode.SetTextureImageDataConnection(textureImageFlipVert.GetOutputPort())

 def ConvertTextureToPointAttribute(self, modelNode, textureImageNode):
    polyData = modelNode.GetPolyData()
    textureImageFlipVert = vtk.vtkImageFlip()
    textureImageFlipVert.SetFilteredAxis(1)
    textureImageFlipVert.SetInputConnection(textureImageNode.GetImageDataConnection())
    textureImageFlipVert.Update()
    textureImageData = textureImageFlipVert.GetOutput()
    pointData = polyData.GetPointData()
    tcoords = pointData.GetTCoords()
    # THIS IS WHERE I GET MY ERROR
    numOfPoints = pointData.GetNumberOfTuples()
    assert numOfPoints == tcoords.GetNumberOfTuples(), "Number of texture coordinates does not equal number of points"
    textureSamplingPointsUv = vtk.vtkPoints()
    textureSamplingPointsUv.SetNumberOfPoints(numOfPoints)
    for pointIndex in range(numOfPoints):
        uv = tcoords.GetTuple2(pointIndex)
        textureSamplingPointsUv.SetPoint(pointIndex, uv[0], uv[1], 0)
    textureSamplingPointDataUv = vtk.vtkPolyData()
    uvToXyz = vtk.vtkTransform()
    textureImageDataSpacingSpacing = textureImageData.GetSpacing()
    textureImageDataSpacingOrigin = textureImageData.GetOrigin()
    textureImageDataSpacingDimensions = textureImageData.GetDimensions()
    uvToXyz.Scale(textureImageDataSpacingDimensions[0] / textureImageDataSpacingSpacing[0],
                  textureImageDataSpacingDimensions[1] / textureImageDataSpacingSpacing[1], 1)
    uvToXyz.Translate(textureImageDataSpacingOrigin)
    textureSamplingPointDataUv.SetPoints(textureSamplingPointsUv)
    transformPolyDataToXyz = vtk.vtkTransformPolyDataFilter()
    transformPolyDataToXyz.SetInputData(textureSamplingPointDataUv)
    transformPolyDataToXyz.SetTransform(uvToXyz)
    probeFilter = vtk.vtkProbeFilter()
    probeFilter.SetInputConnection(transformPolyDataToXyz.GetOutputPort())
    probeFilter.SetSourceData(textureImageData)
    probeFilter.Update()
    rgbPoints = probeFilter.GetOutput().GetPointData().GetArray('ImageScalars')
    colorArrayRed = vtk.vtkDoubleArray()
    colorArrayRed.SetName('ColorRed')
    colorArrayRed.SetNumberOfTuples(numOfPoints)
    colorArrayGreen = vtk.vtkDoubleArray()
    colorArrayGreen.SetName('ColorGreen')
    colorArrayGreen.SetNumberOfTuples(numOfPoints)
    colorArrayBlue = vtk.vtkDoubleArray()
    colorArrayBlue.SetName('ColorBlue')
    colorArrayBlue.SetNumberOfTuples(numOfPoints)
    for pointIndex in range(numOfPoints):
        rgb = rgbPoints.GetTuple3(pointIndex)
        colorArrayRed.SetValue(pointIndex, rgb[0])
        colorArrayGreen.SetValue(pointIndex, rgb[1])
        colorArrayBlue.SetValue(pointIndex, rgb[2])
    colorArrayRed.Modified()
    colorArrayGreen.Modified()
    colorArrayBlue.Modified()
    pointData.AddArray(colorArrayRed)
    pointData.AddArray(colorArrayGreen)
    pointData.AddArray(colorArrayBlue)
    pointData.Modified()
    polyData.Modified()
</code></pre>
<p>The thing is: if I use version 4.11 I get this error and the texture is not applied correctly;</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b261d7bbab8d0206761b3b6880efb2c4eeec7dbf.png" data-download-href="/uploads/short-url/ps2CeSr7IvmHCFqonMXdxRhzJcb.png?dl=1" title="Captura de pantalla 2020-06-23 a las 18.00.32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b261d7bbab8d0206761b3b6880efb2c4eeec7dbf.png" alt="Captura de pantalla 2020-06-23 a las 18.00.32" data-base62-sha1="ps2CeSr7IvmHCFqonMXdxRhzJcb" width="690" height="54" data-dominant-color="FFDADA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2020-06-23 a las 18.00.32</span><span class="informations">1085×85 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but If I use version 4.10.2, the texture is applied correctly and everything is perfect (so I suppose the code is not wrong)</p>
<p>I suspect the error is related with the version I’m using (4.11). But I need to fix it. I have to use 4.11 to do the extension because I have another issue that can only be fixed by updating the version<br>
(this one: <a href="https://discourse.slicer.org/t/import-data-automatically-to-a-volume-node-from-a-folder-using-command-line/10753/8" class="inline-onebox">Import data automatically to a volume node from a folder using command line - #8 by lassoan</a> )</p>
<p>I can’t find anything related with this (I’m only a student)<br>
how can I fix it?</p>
<p>Thank you!!</p>

---

## Post #2 by @lassoan (2020-06-23 17:48 UTC)

<p>I was able to reproduce the problem. It seems that LPS-&gt;RAS conversion removed texture coordinates. I’ll try fix it today.</p>

---

## Post #3 by @lassoan (2020-06-23 18:55 UTC)

<p>The <a href="https://github.com/Slicer/Slicer/commit/962d9a62e07723669b5de2fd2e7458951955dd1c">fix</a> is ready and it will available in tomorrow’s Slicer Preview Release. Thanks for reporting the issue!</p>

---
