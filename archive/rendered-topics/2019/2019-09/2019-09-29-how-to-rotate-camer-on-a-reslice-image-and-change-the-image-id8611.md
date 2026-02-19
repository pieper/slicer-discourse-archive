---
topic_id: 8611
title: "How To Rotate Camer On A Reslice Image And Change The Image"
date: 2019-09-29
url: https://discourse.slicer.org/t/8611
---

# how to rotate camer on a reslice image and change the image display?

**Topic ID**: 8611
**Date**: 2019-09-29
**URL**: https://discourse.slicer.org/t/how-to-rotate-camer-on-a-reslice-image-and-change-the-image-display/8611

---

## Post #1 by @pingdan (2019-09-29 07:45 UTC)

<p>I display a image in renderer, and rotate some degree of camera, but the image of displaying don’t have difference. after rotation, I got the parameter of image, it has changed.</p>
<p>vtkSmartPointer reader = vtkSmartPointer::New();<br>
reader-&gt;SetDirectoryName(“D:\test”);<br>
reader-&gt;Update();<br>
vtkSmartPointer m_Renderer = vtkSmartPointer::New();<br>
vtkSmartPointer RenderWindowInteractor = vtkSmartPointer::New();</p>
<p>vtkSmartPointer m_RenderWindow = vtkSmartPointer::New();<br>
m_RenderWindow-&gt;AddRenderer(m_Renderer);<br>
m_RenderWindow-&gt;SetSize(640, 480);<br>
m_RenderWindow-&gt;SetWindowName(“ImageViewerTest”);</p>
<p>RenderWindowInteractor-&gt;SetRenderWindow(m_RenderWindow);<br>
RenderWindowInteractor-&gt;Initialize();</p>
<p>vtkSmartPointer&lt; vtkImagePlaneWidget &gt; m_ImagePlaneWidget = vtkSmartPointer&lt; vtkImagePlaneWidget &gt;::New();<br>
vtkSmartPointer&lt; vtkResliceCursorThickLineRepresentation &gt; m_ResliceCursorRep = vtkSmartPointer&lt; vtkResliceCursorThickLineRepresentation &gt;::New();<br>
vtkSmartPointer&lt; vtkResliceCursor &gt;  m_ResliceCursor = vtkSmartPointer&lt; vtkResliceCursor &gt;::New();<br>
vtkSmartPointer&lt; vtkResliceCursorWidget&gt; m_ResliceCursorWidget = vtkSmartPointer&lt; vtkResliceCursorWidget&gt;::New();</p>
<p>m_ResliceCursorRep-&gt;GetResliceCursorActor()-&gt;<br>
GetCursorAlgorithm()-&gt;SetResliceCursor(m_ResliceCursor);<br>
m_ResliceCursorRep-&gt;GetResliceCursorActor()-&gt;<br>
GetCursorAlgorithm()-&gt;SetReslicePlaneNormal(1);<br>
m_ResliceCursorWidget-&gt;SetInteractor(m_RenderWindow-&gt;GetInteractor());<br>
m_ImagePlaneWidget-&gt;SetInteractor(m_RenderWindow-&gt;GetInteractor());<br>
m_ImagePlaneWidget-&gt;SetDefaultRenderer(m_Renderer);<br>
m_ResliceCursorWidget-&gt;SetDefaultRenderer(m_Renderer);<br>
m_ResliceCursorWidget-&gt;SetRepresentation(m_ResliceCursorRep);</p>
<p>m_ResliceCursorWidget-&gt;SetEnabled(1);</p>
<p>m_ImagePlaneWidget-&gt;SetInputData(reader-&gt;GetOutput());<br>
m_ImagePlaneWidget-&gt;SetPlaneOrientation(1);<br>
m_ImagePlaneWidget-&gt;SetSliceIndex(256); //<br>
double pos[3];<br>
reader-&gt;GetOutput()-&gt;GetCenter(pos);<br>
m_ResliceCursor-&gt;SetImage(reader-&gt;GetOutput());<br>
m_ResliceCursor-&gt;SetCenter(pos);</p>
<p>m_ImagePlaneWidget-&gt;On();<br>
m_ImagePlaneWidget-&gt;InteractionOn();</p>
<p>//////////////////////////////////////////////////////////////////////////<br>
double range[2];<br>
reader-&gt;GetOutput()-&gt;GetScalarRange(range);<br>
m_ResliceCursorWidget-&gt;GetResliceCursorRepresentation()-&gt;<br>
SetWindowLevel(range[1] - range[0], (range[0] + range[1]) / 2.0);<br>
m_ImagePlaneWidget-&gt;SetWindowLevel(range[1] - range[0], (range[0] + range[1]) / 2.0);</p>
<p>m_Renderer-&gt;ResetCamera();<br>
m_Renderer-&gt;SetBackground(1, 1, 1);</p>
<p>double *focus = m_Renderer-&gt;GetActiveCamera()-&gt;GetFocalPoint();<br>
double *range1 = m_Renderer-&gt;GetActiveCamera()-&gt;GetClippingRange();<br>
vtkSmartPointeraCamera = vtkSmartPointer::New();<br>
aCamera = m_Renderer-&gt;GetActiveCamera();<br>
//Azimuth Ele no result, roll can result yaw disappear<br>
double *ori = aCamera-&gt;GetOrientation();<br>
double *viewup = aCamera-&gt;GetViewPlaneNormal();<br>
m_Renderer-&gt;GetActiveCamera()-&gt;Yaw(60);<br>
double *pos1 = aCamera-&gt;GetPosition();<br>
aCamera-&gt;Azimuth(60);<br>
aCamera-&gt;ComputeViewPlaneNormal();<br>
double *viewup1 = aCamera-&gt;GetViewPlaneNormal();<br>
m_Renderer-&gt;SetActiveCamera(aCamera);<br>
m_RenderWindow-&gt;Render();<br>
RenderWindowInteractor-&gt;Start();</p>

---

## Post #2 by @lassoan (2019-10-02 02:23 UTC)

<p>Could you describe what would you like to achieve? What you would like to visualize and how?</p>

---

## Post #3 by @pingdan (2019-10-09 05:10 UTC)

<p>I want to see the back of image.<br>
for example, when I reslice a image and display the front of image, now I want to rotate camera to the back of image and see the back of image. but I found I can’t see the back whatever I rotate the camera as if the camera didn’t move any more. I want to know, why the camera’s rotate setting why not effect? thanks</p>

---

## Post #4 by @FloCo (2022-06-30 07:41 UTC)

<p>Hello everyone,</p>
<p>I am having the same problem using similar code in version vtk 8.1.<br>
The only action that does something on the camera is the roll parameter but it does not rotate the image in the right way.<br>
Like <a class="mention" href="/u/pingdan">@pingdan</a> I’d like to see the image from its back and not from its top. I’ve tried every camera parameter (Orientation, Yaw, Roll, Elevation, Azimuth,Pitch, ViewUp, Position,…) but the only thing I can do is rotating the image along its perpendicular axis.<br>
I could flip the entire vtkImage to have the good result but then it would generate other problems. It looks like the printed image is a 2D slice but I can’t rotate it to see from behind.<br>
If someone found a solution to this problem.</p>
<p>Thank you !</p>

---
