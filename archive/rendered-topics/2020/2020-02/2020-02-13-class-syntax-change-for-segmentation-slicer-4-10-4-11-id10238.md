---
topic_id: 10238
title: "Class Syntax Change For Segmentation Slicer 4 10 4 11"
date: 2020-02-13
url: https://discourse.slicer.org/t/10238
---

# Class/syntax change for segmentation (slicer 4.10- 4.11)

**Topic ID**: 10238
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/class-syntax-change-for-segmentation-slicer-4-10-4-11/10238

---

## Post #1 by @prorai (2020-02-13 11:22 UTC)

<p>what are the changes in class and its parameters?</p>
<p>ExportAllSegmentsToModelHierarchy() is now ExportAllSegmentsToModels() , i believe its right.<br>
But what is vtkIdType 	folderItemId ? what should i pass here?</p>

---

## Post #2 by @lassoan (2020-02-13 13:39 UTC)

<p>The API is changed in Slicer-4.11 - see more information and link to code example in the migration guide: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Export_segments_to_models">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Export_segments_to_models</a></p>

---

## Post #3 by @prorai (2020-02-13 14:30 UTC)

<p>is there any changes in camera and actor setting my snap image is getting black not the color i’m passing as a parameter ?</p>

---

## Post #4 by @lassoan (2020-02-13 14:42 UTC)

<p>I don’t know what is a “snap image” and what color you pass as a parameter and where.</p>

---

## Post #5 by @prorai (2020-02-13 14:45 UTC)

<blockquote>
<pre><code>            modelNode = slicer.util.getNode(segment)
            pdMap = vtk.vtkPolyDataMapper()
            pdMap.SetInputData(modelNode.GetPolyData())
            modelActor = vtk.vtkLODActor()
            modelActor.SetMapper(pdMap)
            modelActor.GetProperty().SetColor(colors[segment])
            ren.AddActor(modelActor)
    pngName = 'Segment'
    ren.AddActor(camActor)

 
    # take a snap of new RenderWindow

    wti = vtk.vtkWindowToImageFilter()
    wti.SetInputBufferTypeToRGBA()
    wti.SetInput(renWin)
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(self.opPath) + '/' + pngName + '.png')
    writer.SetInputConnection(wti.GetOutputPort())
    writer.Write()
</code></pre>
</blockquote>
<p>Sorry for the less info, BTW this is my code , which works perfectly with slicer4.10 , but now with 4.11 the color ob the actor/object is black only</p>

---

## Post #6 by @lassoan (2020-02-13 15:01 UTC)

<p>To capture screenshots, check out these examples in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture</a></p>

---

## Post #7 by @prorai (2020-02-13 15:19 UTC)

<p>cant see any changes in code , but the object color in PNG is not the color i’m setting</p>
<blockquote>
<p>modelActor.GetProperty().SetColor(…)</p>
</blockquote>
<p>here</p>

---

## Post #8 by @lassoan (2020-02-13 19:42 UTC)

<p>Do you have any problem with models that Slicer puts in the scene or only those that you manually add? Why do you use LOD actor?</p>

---

## Post #9 by @prorai (2020-02-14 07:52 UTC)

<p>So the script is running in No window mode , that’s why i’m creating this setup to get a image of the model slicer generated.<br>
so i believe i’m using LODActor to get the model in the scene. is there any other way to get this done.?</p>

---

## Post #10 by @prorai (2020-02-17 14:34 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> i tried many ways even added light in that render window still 3D model didn’t coming in color.</p>

---

## Post #11 by @lassoan (2020-02-17 16:00 UTC)

<p>LOD (level-od-detail) actor renders at low resolution first and at increasingly high resolution to make rendering of complex scenes more interactive. You don’t need this but instead simple rendering using vtkActor.</p>
<p>I don’t understand yet what the problem is (what you mean by “3D model didn’t coming in color”), but if you want to do off-screen rendering (render without creating a visible render window) then it can be very tricky. It is an advanced topic and the solution depends on many factors (operating system, driver, what OpenGL implementation Slicer was built with, etc.).</p>

---

## Post #12 by @prorai (2020-02-18 07:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , Thank you for your response. i’ve change LOD Actor to vtkActor. and also added a spot light.</p>
<p>Please have a look what actually happening here or what exactly my problem is-</p>
<p>i’ve removed the --no-main-window to check the model in editor and my model looks like this,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28bce76c1088bb026607026fdccfbb40e43c4a7f.png" alt="image" data-base62-sha1="5OnP4w3gABQUPqCFwGpGNPqvNdd" width="196" height="200"></p>
<p>output model in windows 3D viewer<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439f6d0b77bf0951f76204c7287d9ee659fb6ba4.png" alt="image" data-base62-sha1="9EdyF0HBIfyUAfEF9seDXL7x33m" width="196" height="200"></p>
<p>And the renderwindow output After upgrading the slicer version to 4.11.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec57ee523c1f07634484d438668748df41a1c10f.png" alt="image" data-base62-sha1="xIN4Beb5GpwqKFjalcNR2UnYPMj" width="196" height="200"></p>

---

## Post #13 by @lassoan (2020-02-18 14:16 UTC)

<p>Does the rendering show up correctly on the screen?</p>
<p>Did you use the scripts at <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture</a> to capture the content of the view?</p>

---

## Post #14 by @prorai (2020-02-18 14:27 UTC)

<p>Yes i’m using same code to write PNG,<br>
i tried to sleep/pause the render window to check and in render window model result is like last image(the black one)</p>
<p>My updated code:</p>
<blockquote>
<pre><code>             ren = vtk.vtkRenderer()
             renWin = vtk.vtkRenderWindow()
             self.modelNode = slicer.util.getNode(segment)
             pdMap = vtk.vtkPolyDataMapper()
             pdMap.SetInputData(self.modelNode.GetPolyData())
             modelActor = vtk.vtkActor()
             modelActor.SetMapper(pdMap)
             modelActor.GetProperty().SetColor(self.colors[ModelColor])
             ren.AddActor(modelActor)

            # light added
            light = vtk.vtkLight()
            light.SetConeAngle(10)
            light.SetFocalPoint(modelActor.GetPosition())
            light.SetPosition(-4.0, 4.0, 1.0)
            light.SetColor(1.0,1.0,1.0)
            # lightActor = vtk.vtkLightActor()
            # lightActor.SetLight(light)
            ren.AddLight(light)
            ren.SetBackground(1.0, 1.0, 1.0)
            # renderwindow
            renWin.AddRenderer(ren)
            renWin.SetSize(640, 480)
            iren = vtk.vtkRenderWindowInteractor()
            iren.SetRenderWindow(renWin)
            cam1 = (ren.GetActiveCamera())
            ren.ResetCamera()
            cam1.Azimuth(180)
            cam1.Elevation(90)
            ## cam1.Dolly(1.5)
            ren.ResetCameraClippingRange()

            # intialize new Render Window
            renWin.Render()
            renWin.SetWindowName("Model PNG Image")

            iren.Initialize()
            pngName = 'Segment'
            # take a snap of new RenderWindow
            wti = vtk.vtkWindowToImageFilter()
            wti.SetInputBufferTypeToRGBA()
            wti.SetInput(renWin)
            writer = vtk.vtkPNGWriter()
            writer.SetFileName(str(self.opPath) + '/' + pngName + '.png')
            writer.SetInputConnection(wti.GetOutputPort())
            writer.Write()
</code></pre>
</blockquote>

---

## Post #15 by @lassoan (2020-02-18 14:34 UTC)

<p>If you use such low-level classes as mappers, actors, and lights then we cannot help. Slicer cannot ensure that you do things right. Why don’t you rely on Slicer’s MRML classes to render your segment?</p>

---

## Post #16 by @prorai (2020-02-18 14:39 UTC)

<p>Which MRML class i can use for mapper, actors or light?<br>
can you please give me few suggestions.</p>
<p>I really thankful for your help and response on this thread</p>

---

## Post #17 by @lassoan (2020-02-18 15:21 UTC)

<blockquote>
<p>Which MRML class i can use for mapper, actors or light?</p>
</blockquote>
<p>I would suggest to let Slicer take care of the rendering. Create a view as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_3D_view_outside_the_view_layout">here</a> then capture a screenshot like this:</p>
<pre data-code-wrap="python"><code class="lang-python">import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
cap.captureImageFromView(viewWidget.threeDView(),'c:/tmp/test.png')
</code></pre>

---
