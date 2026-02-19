---
topic_id: 14725
title: "Multiple 3D Viewers"
date: 2020-11-21
url: https://discourse.slicer.org/t/14725
---

# Multiple 3D viewers

**Topic ID**: 14725
**Date**: 2020-11-21
**URL**: https://discourse.slicer.org/t/multiple-3d-viewers/14725

---

## Post #1 by @Kalman (2020-11-21 18:26 UTC)

<p>Dear All,</p>
<p>I have a question regarding an “automatic visualization” workflow.<br>
The basic is that I have a large number of DICOM files from multiple specimen, and I would like to create a kind of thumbnail/preview image of each file using 3D rendering.</p>
<p>If I use the “Triple 3D” option and the three main keys (Home/End/Page Down) in the different windows, this is the result I get:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95b739fb4b9f7382232bed2840946523c9ed6f11.jpeg" data-download-href="/uploads/short-url/lmrHEl6PVB78WkpaNFlzr8iUGnT.jpeg?dl=1" title="skull_basic_3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95b739fb4b9f7382232bed2840946523c9ed6f11_2_690x465.jpeg" alt="skull_basic_3D" data-base62-sha1="lmrHEl6PVB78WkpaNFlzr8iUGnT" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95b739fb4b9f7382232bed2840946523c9ed6f11_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95b739fb4b9f7382232bed2840946523c9ed6f11_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95b739fb4b9f7382232bed2840946523c9ed6f11.jpeg 2x" data-dominant-color="9797C6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">skull_basic_3D</span><span class="informations">1368×923 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The <strong>question</strong> is that:</p>
<ul>
<li>how could I split the window to contain six 3D viewers?</li>
<li>and is it possible to predefine the desired views in each 3D viewer?<br>
(I show an example below what I’ve created in an image editor)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/685dfe6964fcbf24607426e9a688f29dafeaff9f.jpeg" data-download-href="/uploads/short-url/eTh2kWcUh6969pNT2krbisByx9J.jpeg?dl=1" title="skull_basic_3D_plan" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685dfe6964fcbf24607426e9a688f29dafeaff9f_2_690x326.jpeg" alt="skull_basic_3D_plan" data-base62-sha1="eTh2kWcUh6969pNT2krbisByx9J" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685dfe6964fcbf24607426e9a688f29dafeaff9f_2_690x326.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685dfe6964fcbf24607426e9a688f29dafeaff9f_2_1035x489.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685dfe6964fcbf24607426e9a688f29dafeaff9f_2_1380x652.jpeg 2x" data-dominant-color="9E99C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">skull_basic_3D_plan</span><span class="informations">1933×916 411 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It means that the:</p>
<ul>
<li>1st viewer shows the image from the right (Shift+Page Down) and also rotates it with 90° clockwise (in order to have a horizontal arrangement);</li>
<li>2nd viewer shows the image from the left (Page Down) and also rotates it with 90° counterclockwise;</li>
<li>3rd viewer shows the image from the front (Home);</li>
<li>4st viewer shows the image from the top (Shift+End) and also rotates it with 90° clockwise;</li>
<li>5st viewer shows the image from the bottom (End) and also rotates it with 90° counterclockwise;</li>
<li>6st viewer shows the image from the back (Shift+Home) and also rotates it with 180°;</li>
</ul>
<p>By doing so, it would be preferred if the images would have the same magnification (if I link the 3D viewers currently all of the images will show the same aspect, but I want to keep the different sides while zooming in and out).</p>
<p>What is your opinion, could it be done somehow?<br>
(I should add that I’m not an expert with the Python, so I cannot create a script in my own).</p>
<p>Thanks for the help in advance!</p>

---

## Post #2 by @timeanddoctor (2020-11-23 14:21 UTC)

<p>Do you just went show the different views of the 3d model?<br>
Maybe you can take it by vtk/blender.</p>

---

## Post #3 by @pieper (2020-11-23 14:53 UTC)

<p>This is all very doable, by defining custom layouts and scripting the cameras.  But yes, it requires python so maybe you can find a collaborator to help you.</p>

---

## Post #4 by @Kalman (2020-11-23 18:28 UTC)

<p>It is only a volume rendered image without any segmentation and further 3D-modelling, what I would like to automatically export from a larger series, so unfortunately I can’t use the Blender (but indeed it is a good idea).</p>

---

## Post #5 by @Kalman (2020-11-23 18:38 UTC)

<p>Thanks! I will then look for a possible cooperator who can help me with this topic by creating that script.</p>

---

## Post #6 by @lassoan (2020-11-24 05:50 UTC)

<p>I’ve copy-pasted a script from code snippets in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repsository</a> that does something like that you need:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80568ae8b98f1600700e791a20691fda2fe6cc68.jpeg" data-download-href="/uploads/short-url/ijkx2vQvKffQyYNGoVcvPLe57pC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/80568ae8b98f1600700e791a20691fda2fe6cc68_2_690x385.jpeg" alt="image" data-base62-sha1="ijkx2vQvKffQyYNGoVcvPLe57pC" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/80568ae8b98f1600700e791a20691fda2fe6cc68_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/80568ae8b98f1600700e791a20691fda2fe6cc68_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/80568ae8b98f1600700e791a20691fda2fe6cc68_2_1380x770.jpeg 2x" data-dominant-color="201710"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2045×1142 443 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-python"># Set inputs

# Load a volume (just for this demo, we load a sample data set)
import SampleData
volumeNode = SampleData.SampleDataLogic().downloadCTChest()

# Set output folder and filename
outputScreenshotsFilenamePattern = slicer.app.temporaryPath+"/screenshots/screenshot_%d.png"
outputGalleryFilename = slicer.app.temporaryPath+"/screenshots/gallery.png"

# Set up volume rendering
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
displayNode.SetVisibility(True)
displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName('CT-Chest-Contrast-Enhanced'))

# Set up visualization for screenshots
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
threeDWidget = slicer.app.layoutManager().threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetCamera()
originalZoomFactor = threeDView.zoomFactor
threeDView.zoomFactor = 0.25
threeDView.zoomIn()
threeDView.setZoomFactor(originalZoomFactor)
threeDViewNode = threeDWidget.mrmlViewNode()
threeDViewNode.SetBackgroundColor(0,0,0)
threeDViewNode.SetBackgroundColor2(0,0,0)
threeDViewNode.SetAxisLabelsVisible(False)
threeDViewNode.SetBoxVisible(False)
threeDViewNode.SetOrientationMarkerType(threeDViewNode.OrientationMarkerTypeAxes)

# Create output folders
import os
filedir = os.path.dirname(outputScreenshotsFilenamePattern)
if not os.path.exists(filedir):
    os.makedirs(filedir)

# Capture screenshots
numberOfScreenshots = 6
axisIndex = [0, 2, 4, 1, 3, 5]  # order of views in the gallery image
import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
for screenshotIndex in range(numberOfScreenshots):
    threeDView.rotateToViewAxis(axisIndex[screenshotIndex])
    slicer.util.forceRenderAllViews()
    outputFilename = outputScreenshotsFilenamePattern % screenshotIndex
    cap.captureImageFromView(threeDView, outputFilename)

# Create gallery view of all images
cap.createLightboxImage(3,  # number of columns
    os.path.dirname(outputScreenshotsFilenamePattern),
    os.path.basename(outputScreenshotsFilenamePattern),
    numberOfScreenshots,
    outputGalleryFilename)
</code></pre>

---

## Post #7 by @Kalman (2020-11-24 11:07 UTC)

<p>Dear Andras, thank you very much for your help!<br>
I will try this script, and if I have anything more to ask, I’ll let you know.<br>
Thanks again!</p>

---

## Post #8 by @muratmaga (2020-11-24 22:38 UTC)

<p>FYI, I needed to add<br>
<code>import os</code><br>
at the top.</p>

---

## Post #9 by @Kalman (2020-11-25 09:35 UTC)

<p>Thank you for the remark!</p>

---
