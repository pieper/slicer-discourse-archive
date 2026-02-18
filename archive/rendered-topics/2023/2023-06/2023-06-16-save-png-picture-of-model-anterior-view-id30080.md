# Save PNG picture of model anterior view

**Topic ID**: 30080
**Date**: 2023-06-16
**URL**: https://discourse.slicer.org/t/save-png-picture-of-model-anterior-view/30080

---

## Post #1 by @Muhammed_Fatih_Talu (2023-06-16 18:32 UTC)

<p>I have drawn the blue box by hand to understand the problem.<br>
I want to save the blue box content as PNG file.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24fa7533b06c111e0e726038143c6d373ba1e683.png" alt="image" data-base62-sha1="5h7N7KXFDqTVRVTeGXYr1mP1Cw3" width="326" height="395"></p>
<p>I can find the coordinates of the boundary points of the blue box.</p>
<pre><code class="lang-auto">ModelNode = slicer.mrmlScene.GetFirstNodeByName('Model')
Vertices = numpy_support.vtk_to_numpy(ModelNode.GetPolyData().GetPoints().GetData())
blueboxMin=[Vertices[:,0].min(), Vertices[:,1].min(), Vertices[:,2].min()]
blueboxMax=[Vertices[:,0].max(), Vertices[:,1].max(), Vertices[:,2].max()]
</code></pre>
<p>But I don’t know how to save this region inside as PNG.</p>

---

## Post #2 by @jamesobutler (2023-06-16 20:03 UTC)

<p>If you want a quick image of the 3D View, you can right-click in the view and select “Copy image” which will copy it to your clipboard and then you can paste it to your application of choice for saving as a png, or paste it directly into a power point file.</p>
<p>You can also use the “Screen Capture” module to save images of the various slice views.</p>

---

## Post #3 by @Muhammed_Fatih_Talu (2023-06-16 20:40 UTC)

<p>Thanks Jame,<br>
I found the solution to the problem:</p>
<pre><code class="lang-auto"># Set background to black (required for transparent background)
view = slicer.app.layoutManager().threeDWidget(0).threeDView()
view.rotateToViewAxis(3)  # look from anterior direction
#view.resetFocalPoint()  # reset the 3D view cube size and center it
#view.resetCamera()  # reset camera zoom
</code></pre>
<p>after that</p>
<pre><code class="lang-auto"># Capture RGBA image
renderWindow = view.renderWindow()
renderWindow.SetAlphaBitPlanes(1)
wti = vtk.vtkWindowToImageFilter()
wti.SetInputBufferTypeToRGBA()
wti.SetInput(renderWindow)
writer = vtk.vtkPNGWriter()
writer.SetFileName("C:/Users/Administrator/Desktop/Slicer/face.png")
writer.SetInputConnection(wti.GetOutputPort())
writer.Write()
</code></pre>
<p>and cropping RGB</p>
<pre><code class="lang-auto">image = Image.open("C:/Users/Administrator/Desktop/Slicer/face.png")
image = image.convert("RGBA") 
width, height = image.size

left = width
top = height
right = 0
bottom = 0
for x in range(width):
    for y in range(height):
        pixel = image.getpixel((x, y))
        if pixel[3] != 0:
            left = min(left, x)
            top = min(top, y)
            right = max(right, x)
            bottom = max(bottom, y)

cropped_image = image.crop((left, top, right + 1, bottom + 1))
cropped_image.save("cropped_face.png")
</code></pre>

---
