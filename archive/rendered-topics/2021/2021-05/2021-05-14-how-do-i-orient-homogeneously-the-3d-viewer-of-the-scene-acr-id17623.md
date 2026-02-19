---
topic_id: 17623
title: "How Do I Orient Homogeneously The 3D Viewer Of The Scene Acr"
date: 2021-05-14
url: https://discourse.slicer.org/t/17623
---

# How do I orient homogeneously the 3d viewer of the scene across different scenes?

**Topic ID**: 17623
**Date**: 2021-05-14
**URL**: https://discourse.slicer.org/t/how-do-i-orient-homogeneously-the-3d-viewer-of-the-scene-across-different-scenes/17623

---

## Post #1 by @Gaborri (2021-05-14 17:04 UTC)

<p>Hi,<br>
I am doing some volume analysis of a tomography with time resolution.<br>
This means that I have several set of data that, if reconstructed, lead to different scenes (which I have saved indipendently).<br>
I would like to make some video of the 3d time resolved reconstruction, but since I have not enough power in my laptop, I need to do it in an old fashion way (exporting the images of the 3d and then put them together).</p>
<p>The problem is that somhow I have changed the orientation of segmentation in the 3d viewer of the scene and to have a constant orientation, I need to set back the original orientation of the 3d viewer.<br>
How can I do it?<br>
I am attaching two screenshot that show the situation<br>
These are two different scenes, and the only thing that changes is the orientation in the 3d viewer… I could I make it homogeneous (so then I can do a video). I would like a precise method to do it, and I would avoid to do it manually by scrolling.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b990786d513fe616dbe813449bf6a9259677105.jpeg" data-download-href="/uploads/short-url/8ve29wDw6Qk5XwRQLM7rDwwoMMB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b990786d513fe616dbe813449bf6a9259677105_2_690x388.jpeg" alt="image" data-base62-sha1="8ve29wDw6Qk5XwRQLM7rDwwoMMB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b990786d513fe616dbe813449bf6a9259677105_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b990786d513fe616dbe813449bf6a9259677105_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b990786d513fe616dbe813449bf6a9259677105.jpeg 2x" data-dominant-color="5D5E5D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b4bb2ed324958a0d0197fc9257d6ca530bf4ccc.jpeg" data-download-href="/uploads/short-url/m9ObUyGI7nEmxgwo0UPNfsbBZve.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b4bb2ed324958a0d0197fc9257d6ca530bf4ccc_2_690x388.jpeg" alt="image" data-base62-sha1="m9ObUyGI7nEmxgwo0UPNfsbBZve" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b4bb2ed324958a0d0197fc9257d6ca530bf4ccc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b4bb2ed324958a0d0197fc9257d6ca530bf4ccc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b4bb2ed324958a0d0197fc9257d6ca530bf4ccc.jpeg 2x" data-dominant-color="5B5C5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you very much for your time, any help would be appreciated.</p>

---

## Post #2 by @mikebind (2021-05-14 18:35 UTC)

<p>You can get the camera node settings from the view you want, and apply those in another scene.</p>
<pre><code>cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(slicer.app.layoutManager().threeDWidget(0).mrmlViewNode())
camPosition = [0,0,0] # just pre-allocating position variable
cameraNode.GetPosition(camPosition) # filling in the position variable
camFocalPoint = [0,0,0] # pre-allocating focal point (direction the camera is pointing from the position)
cameraNode.GetFocalPoint(camFocalPoint) # filling in focal point
camViewUp = [0,0,0] # pre-allocating view up direction (vector pointing up, perpendicular to vector from position to focal point)
cameraNode.GetViewUp(camViewUp) 
</code></pre>
<p>You can just record the values you find for these camera parameters, and then do the following to apply them to another scene:</p>
<pre><code>cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(slicer.app.layoutManager().threeDWidget(0).mrmlViewNode())
cameraNode.SetPosition(camPosition) # setting camera location
cameraNode.SetPosition(camFocalPoint) # setting direction camera is looking
cameraNode.SetViewUp(camViewUp) # setting up direction (i.e. the rotation around the position-focal point axis)</code></pre>

---

## Post #3 by @lassoan (2021-05-15 01:20 UTC)

<p>You can also play time sequences of any nodes (volumes, models, markups, transforms, …) using Sequences module.</p>
<p>Load all your volumes into the scene, go to Sequences module, go to Edit tab, select each volume node from the right box, and add it to the sequence (left box) by clicking the green button. You can replay sequences by switching to Browse tab, select your newly created sequence node, and click the green <code>+</code> button.</p>
<p>You can create videos of your sequence using Screen Capture module.</p>

---

## Post #4 by @Gaborri (2021-05-17 12:27 UTC)

<p>Hi,</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> , I guess I should open the python interface and paste your code right (sorry I am not good at programming)?</p>
<p>And then I just close the scene and open the one I want to paste again the second part of the code?</p>
<p>For <a class="mention" href="/u/lassoan">@lassoan</a> , the problem is my laptop RAM. I have a 16 gb Ram + graphic one (4GB), but it is not enough to digest 31 volumes (11 MB each) and create the sequence (RAM error occurs if I try so, even with only 7 volumes). If you have an idea how to skip this would be great!</p>

---

## Post #5 by @lassoan (2021-05-17 12:56 UTC)

<p>To deal with limited amount of physical RAM you can:</p>
<ul>
<li>load, crop/resample (using Crop volume module), and save each volume. Just by a downsampling by a spacing scale of 2x, you reduce the memory usage by 8x</li>
<li>increase virtual memory size in your system settings (this make make your computer slow when you load a lot of data, but the application will still keep running)</li>
<li>afyer you added a few volumes to the sequence, delete those volumes from the scene (they are stored in the sequence already)</li>
</ul>

---

## Post #6 by @mikebind (2021-05-17 15:38 UTC)

<p>Yes, you can open the python interactor (Ctrl+3 or the python button in the toolbar) and paste.  The variables you create (<code>camFocalPoint</code>, etc.) will persist after you close the scene and open a new one, but will not persist after you close and reopen Slicer. (To deal with that you could save them to a file, or even just print them and write them down (e.g. <code>print camFocalPoint</code> in the interactor)).  If you can get <a class="mention" href="/u/lassoan">@lassoan</a>’s solution working, that’s a much more elegant approach, but if not, maybe this hack can get you through what you want to accomplish.</p>

---
