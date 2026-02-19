---
topic_id: 30050
title: "Create 3D Landmarks On The Model Surface Using Rgb Landmarks"
date: 2023-06-15
url: https://discourse.slicer.org/t/30050
---

# Create 3d landmarks on the model surface using RGB landmarks

**Topic ID**: 30050
**Date**: 2023-06-15
**URL**: https://discourse.slicer.org/t/create-3d-landmarks-on-the-model-surface-using-rgb-landmarks/30050

---

## Post #1 by @Muhammed_Fatih_Talu (2023-06-15 10:16 UTC)

<p>I save the front view of the model as RGB and find the landmarks of the face. But I need to create these landmarks on the 3d model. I need a link between the RGB pixel and the model voxel. Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ec1142b8df9c4301cc4ede9412966a5a1e95acb.jpeg" data-download-href="/uploads/short-url/8X9gTKhnePfaOH1cvT3gjjgcJJN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ec1142b8df9c4301cc4ede9412966a5a1e95acb_2_351x500.jpeg" alt="image" data-base62-sha1="8X9gTKhnePfaOH1cvT3gjjgcJJN" width="351" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ec1142b8df9c4301cc4ede9412966a5a1e95acb_2_351x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ec1142b8df9c4301cc4ede9412966a5a1e95acb_2_526x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ec1142b8df9c4301cc4ede9412966a5a1e95acb_2_702x1000.jpeg 2x" data-dominant-color="868787"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">727×1034 99.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-06-16 14:11 UTC)

<p>Do you want to mark points on a surface mesh? Why don’t you do that directly in Slicer?</p>

---

## Post #3 by @Muhammed_Fatih_Talu (2023-06-16 14:42 UTC)

<p>My goal is to find the face landmarks in the 3d head model in Slicer.<br>
I don’t know how to do this in Slicer. Maybe curvature can be used.</p>
<p>But the Google Mediapipe code captures the face landmarks in RGB image very well.<br>
Because of this, I obtained an RGB image from the model in Slicer and found landmarks by Mediapipe.</p>
<p>Now I want to find out which point on the 3d model surface this landmark information in 2d corresponds to.</p>
<p>The figure has a face landmark (F3). I want to find the point where this point corresponds on the surface. I think I can use trimesh’s rail function for this. I’m trying to find the intersection point on the surface by starting F3.</p>
<p>I need the mesh information of the model. I can get the nodes.</p>
<pre><code class="lang-auto">ModelNode = slicer.mrmlScene.GetFirstNodeByName('Model')
Vertices = numpy_support.vtk_to_numpy(ModelNode.GetPolyData().GetPoints().GetData())
</code></pre>
<p>But I can’t get the faces information.<br>
<code>Faces = ModelNode.GetMesh().GetCellData().GetArray()</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11ee07640ea90fd7fd1db7d02f92434f7f231fbf.jpeg" data-download-href="/uploads/short-url/2yC5FJbdwa23Cahe2vyA0rCFEyH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ee07640ea90fd7fd1db7d02f92434f7f231fbf_2_321x500.jpeg" alt="image" data-base62-sha1="2yC5FJbdwa23Cahe2vyA0rCFEyH" width="321" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ee07640ea90fd7fd1db7d02f92434f7f231fbf_2_321x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ee07640ea90fd7fd1db7d02f92434f7f231fbf_2_481x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ee07640ea90fd7fd1db7d02f92434f7f231fbf_2_642x1000.jpeg 2x" data-dominant-color="A4A471"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×1029 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2023-06-16 19:41 UTC)

<aside class="quote no-group" data-username="Muhammed_Fatih_Talu" data-post="3" data-topic="30050">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muhammed_fatih_talu/48/14646_2.png" class="avatar"> Muhammed_Fatih_Talu:</div>
<blockquote>
<p>I obtained an RGB image from the model in Slicer and found landmarks by Mediapipe</p>
</blockquote>
</aside>
<p>That’s good, you can then convert the 2D display coordinates to 3D coordinates using point picking as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-3d-coordinates-from-2d-display-coordinates">this code snippet</a>.</p>

---

## Post #5 by @Muhammed_Fatih_Talu (2023-06-17 06:33 UTC)

<p>Thanks Lassoan. This code worked for me. Only one problem remained. How can I find the maximum values of horizontal and vertical variables in the command below? So how can I get the image size?</p>
<pre><code class="lang-auto">modelDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName("vtkMRMLModelDisplayableManager")
modelDisplayableManager.Pick( horizontal, vertical )
</code></pre>

---

## Post #6 by @lassoan (2023-06-18 12:44 UTC)

<p>If you have the image you know its size, too.</p>

---

## Post #7 by @Muhammed_Fatih_Talu (2023-06-18 14:19 UTC)

<p>I get the RGB image by Screen Capture the model image in threeDView. When I make Screen Capture, the original data size and the size I captured are different. I want to eliminate this difference.</p>
<p>In other words, I want to save an RGB image from the anterior view of the 3d model, find the landmark of the face, and create the landmark I found on the model.</p>

---

## Post #8 by @Muhammed_Fatih_Talu (2023-06-17 17:07 UTC)

<p>I know the RGB image dimensions and the corresponding point position. But I don’t know how to find its place in the model with this information?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0129063b10c5be9d60c4874d5be727a120c6dfc3.jpeg" data-download-href="/uploads/short-url/agn2R760qCg89qu7W5pKYHhSdt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0129063b10c5be9d60c4874d5be727a120c6dfc3_2_690x354.jpeg" alt="image" data-base62-sha1="agn2R760qCg89qu7W5pKYHhSdt" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0129063b10c5be9d60c4874d5be727a120c6dfc3_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0129063b10c5be9d60c4874d5be727a120c6dfc3_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0129063b10c5be9d60c4874d5be727a120c6dfc3_2_1380x708.jpeg 2x" data-dominant-color="807D5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1520×780 98.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Using the code below, I can put a landmark at the [i,j] point of the model. However, I cannot connect [x,y] in the picture to [i,j] in the model. Thank you for your help</p>
<pre><code class="lang-auto">if modelDisplayableManager.Pick(i,j) and modelDisplayableManager.GetPickedNodeID():
       rasPosition = modelDisplayableManager.GetPickedRAS()
       slicer.modules.markups.logic().AddControlPoint(rasPosition[0],rasPosition[1],rasPosition[2]);
</code></pre>

---

## Post #9 by @lassoan (2023-06-18 14:32 UTC)

<p>You can capture the rendered image from the 3D view as shown in Python examples in the script repository.</p>

---

## Post #10 by @Muhammed_Fatih_Talu (2023-06-18 14:51 UTC)

<p>I can capture anterior image of the 3d model. However, when I put a landmark in the x,y coordinate of this image, does it put the 3d model in the right place?</p>
<p>Capture image sizes vary depending on whether the program is full screen or not. this leads to inconsistency.</p>

---

## Post #11 by @Muhammed_Fatih_Talu (2023-06-18 16:55 UTC)

<p>Problem solved. It turns out that the RGB dimensions I saved and the dimensions of the 3d model were exactly the same. Dear Andrew, thank you for your valuable guidance.</p>
<p>The code below got the job done.</p>
<pre><code class="lang-auto">threeDView = slicer.app.layoutManager().threeDWidget(0).threeDView()
modelDisplayableManager = threeDView.displayableManagerByClassName("vtkMRMLModelDisplayableManager")
#threeDView.resetFocalPoint()  # reset the 3D view cube size and center it
#threeDView.resetCamera()  # reset camera zoom
threeDView.rotateToViewAxis(3) # look from anterior direction
renderWindow = threeDView.renderWindow()
renderWindow.SetAlphaBitPlanes(1)
wti = vtk.vtkWindowToImageFilter()
wti.SetInputBufferTypeToRGBA()
wti.SetInput(renderWindow)
writer = vtk.vtkPNGWriter()
writer.SetFileName("C:/Users/Administrator/Desktop/Slicer/face.png")
writer.SetInputConnection(wti.GetOutputPort())
writer.Write()

FaceXY = [[957,659]]  # for example
for i in range(len(FaceXY)):
    if modelDisplayableManager.Pick(FaceXY[i][0], FaceXY[i][1]) and modelDisplayableManager.GetPickedNodeID():
        rasPosition = modelDisplayableManager.GetPickedRAS()
        slicer.modules.markups.logic().AddControlPoint(rasPosition[0],rasPosition[1],rasPosition[2]);
</code></pre>

---
