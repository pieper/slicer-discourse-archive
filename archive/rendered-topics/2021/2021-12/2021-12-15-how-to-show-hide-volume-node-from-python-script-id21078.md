---
topic_id: 21078
title: "How To Show Hide Volume Node From Python Script"
date: 2021-12-15
url: https://discourse.slicer.org/t/21078
---

# How to show/hide volume node from python script

**Topic ID**: 21078
**Date**: 2021-12-15
**URL**: https://discourse.slicer.org/t/how-to-show-hide-volume-node-from-python-script/21078

---

## Post #1 by @ziri (2021-12-15 17:10 UTC)

<p>Hi,<br>
I’m trying to create a node from numpy array as shown below:</p>
<blockquote>
<p>nodeName = “NewVolumeNode”<br>
voxelType=vtk.VTK_UNSIGNED_CHAR<br>
imageOrigin = [0.0, 0.0, 0.0]<br>
imageSpacing = [1.0, 1.0, 1.0]<br>
imageDirections = [[1,0,0], [0,1,0], [0,0,1]]</p>
<p>data_vtk = vtk.util.numpy_support.numpy_to_vtk(num_array = imgdata.ravel(), deep = True, array_type = vtk.VTK_FLOAT)<br>
imageData = vtk.vtkImageData()<br>
imageData.SetDimensions(imgdata.shape[::-1])<br>
imageData.GetPointData().SetScalars(data_vtk)</p>
<p>volumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, nodeName)<br>
volumeNode.SetOrigin(imageOrigin)<br>
volumeNode.SetSpacing(imageSpacing)<br>
volumeNode.SetIJKToRASDirections(imageDirections)<br>
volumeNode.SetAndObserveImageData(imageData)<br>
volumeNode.CreateDefaultDisplayNodes()<br>
volumeNode.CreateDefaultStorageNode()</p>
</blockquote>
<p>However, I didn’t find a way on the wiki or other posts to toggle the volume node show/hidden button under Data/Subject Hierachy/Node. I tried:</p>
<blockquote>
<p>volumeNode.GetDisplayNode().SetVisibility(True)</p>
</blockquote>
<p>But it didn’t work, and I have to toggle the show/hidden manually in slicer UI under Data/Subject Hierachy/Node. Is there any python command to do this? Thanks!</p>

---

## Post #2 by @Juicy (2021-12-16 04:12 UTC)

<p>The following code will make the ‘volumeNode’ volume appear in the slice windows:</p>
<pre><code class="lang-auto">slicer.util.setSliceViewerLayers(background = volumeNode)
</code></pre>
<p>and this code will reset the slice windows to be centred on the new volume:</p>
<pre><code class="lang-auto">slicer.util.resetSliceViews()
</code></pre>
<p>This should effectively do the same thing as toggling the show hide button on the volume in the data module.</p>

---

## Post #3 by @ziri (2021-12-16 14:47 UTC)

<p>This works great, thanks!</p>

---

## Post #4 by @ziri (2021-12-16 16:07 UTC)

<p>Sorry I have one follow-up question… I found it is not quite the same thing as toggling the show/hide button. For example, I was trying to load a 2D ultrasound image (volume size=[1,480,640]) and apply transformation on the image. After initial loading, I did</p>
<blockquote>
<p>usImgTransformNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTransformNode”, “TrackedUSImagePose”)<br>
usImgNode.SetAndObserveTransformNodeID(usImgTransformNode.GetID())<br>
and do <code>slicer.util.resetSliceViews()</code> I got:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/044a41963209e445e17172cc91688053e8f1c84b.png" data-download-href="/uploads/short-url/BX0bJt95dLxiXwqi5l0VL3W0PN.png?dl=1" title="Image 003" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/044a41963209e445e17172cc91688053e8f1c84b_2_690x366.png" alt="Image 003" data-base62-sha1="BX0bJt95dLxiXwqi5l0VL3W0PN" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/044a41963209e445e17172cc91688053e8f1c84b_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/044a41963209e445e17172cc91688053e8f1c84b_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/044a41963209e445e17172cc91688053e8f1c84b_2_1380x732.png 2x" data-dominant-color="5F5F67"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 003</span><span class="informations">1920×1019 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then I fill in the transformation node with actual matrix by <code>usImgTransformNode.SetMatrixTransformToParent(transformMatrix)</code> and do <code>slicer.util.resetSliceViews()</code>, I got:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fb6d5ed3d3160146278bce6b9d50c796f67a493.png" data-download-href="/uploads/short-url/dEJ5a5hVZfQ264C3RCCTSPOxN8D.png?dl=1" title="Image 005" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fb6d5ed3d3160146278bce6b9d50c796f67a493_2_690x366.png" alt="Image 005" data-base62-sha1="dEJ5a5hVZfQ264C3RCCTSPOxN8D" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fb6d5ed3d3160146278bce6b9d50c796f67a493_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fb6d5ed3d3160146278bce6b9d50c796f67a493_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fb6d5ed3d3160146278bce6b9d50c796f67a493_2_1380x732.png 2x" data-dominant-color="5D5D66"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 005</span><span class="informations">1920×1019 54.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
which is not showing the correct reformatted slice aligned with the volume. However, if I first hide the  by clicking the hide button in Data widget<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6883abd9a570e511b716e453169f8dad3d9b44da.png" data-download-href="/uploads/short-url/eUzLcGlXEpgvoGh1AqO30fX0LAm.png?dl=1" title="Image 006" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6883abd9a570e511b716e453169f8dad3d9b44da_2_690x365.png" alt="Image 006" data-base62-sha1="eUzLcGlXEpgvoGh1AqO30fX0LAm" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6883abd9a570e511b716e453169f8dad3d9b44da_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6883abd9a570e511b716e453169f8dad3d9b44da_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6883abd9a570e511b716e453169f8dad3d9b44da_2_1380x730.png 2x" data-dominant-color="5C5C64"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 006</span><span class="informations">1920×1018 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
and re-click the show button, I have:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1f10503d0f60a83e6057c5ec4ce2b94a9a5d752.png" data-download-href="/uploads/short-url/n6BfNzpV03cjEyOIBhcG424Fodk.png?dl=1" title="Image 007" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f10503d0f60a83e6057c5ec4ce2b94a9a5d752_2_690x365.png" alt="Image 007" data-base62-sha1="n6BfNzpV03cjEyOIBhcG424Fodk" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f10503d0f60a83e6057c5ec4ce2b94a9a5d752_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f10503d0f60a83e6057c5ec4ce2b94a9a5d752_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f10503d0f60a83e6057c5ec4ce2b94a9a5d752_2_1380x730.png 2x" data-dominant-color="5D5E66"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 007</span><span class="informations">1920×1016 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
which is the display I’d like to have. I wonder is there a mechanism behind the show/hide button that I can do with script to enable this kind of behavior? I essentially would like to change the transformation matrice multiple times and show the US image moving in 3D as well as showing the image in one of the slice view.<br>
Thanks!</p>
</blockquote>

---

## Post #5 by @Juicy (2021-12-16 21:09 UTC)

<p>I am not really sure what is going on there as my slicer program does not have that same behaviour although I am using an older version (4.11.20200930)</p>
<p>Usually the red, yellow and green slice views just look along the primary axes, e.g. the red slice always looks normal to the Sup/Inf axis. It looks like when you pressed the show hide button that the yellow view has become reformatted to look at the rotated volume. As I said my slicer does not reformat the slice views by toggling the show hide button so I am not sure why yours does this?</p>
<p>Anyway if you want some code which is equivalent to pressing the " Rotate to volume plane" button which reformats the slice views to look at the rotated volume try this:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
sliceWidget = layoutManager.sliceWidget('Red')
controller = sliceWidget.sliceController()
controller.rotateSliceToBackground()
slicer.util.resetSliceViews()
</code></pre>
<p>This just rotates the red slice to the volume. Just replace the ‘Red’ with ‘Yellow’ or ‘Green’ if you want to rotate the other slices. If you want to rotate all 3 then you will need to loop through them:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
for sliceViewName in layoutManager.sliceViewNames():
    sliceWidget = layoutManager.sliceWidget(sliceViewName)
    controller = sliceWidget.sliceController()
    controller.rotateSliceToBackground()


slicer.util.resetSliceViews()
</code></pre>

---

## Post #6 by @ziri (2021-12-19 21:33 UTC)

<p>Thanks! I am using the latest stable version (4.11.20210226, revision 29738, built 2021-03-01), and I found that currently there is an attribute error when doing</p>
<blockquote>
<p>controller.rotateSliceToBackground()<br>
AttributeError: qMRMLSliceControllerWidget has no attribute named ‘rotateSliceToBackground’</p>
</blockquote>
<p>I think now it has been updated to <code>controller.rotateSliceToLowestVolumeAxes()</code> which works great.</p>

---
