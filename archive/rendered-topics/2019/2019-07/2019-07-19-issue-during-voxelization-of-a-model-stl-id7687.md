---
topic_id: 7687
title: "Issue During Voxelization Of A Model Stl"
date: 2019-07-19
url: https://discourse.slicer.org/t/7687
---

# Issue during voxelization of a model stl

**Topic ID**: 7687
**Date**: 2019-07-19
**URL**: https://discourse.slicer.org/t/issue-during-voxelization-of-a-model-stl/7687

---

## Post #1 by @Clara (2019-07-19 15:57 UTC)

<p>Hi all!</p>
<p>I have to convert a surface model stl into a voxelized mask, with 1s inside and 0s outside. It is important that the mask has the same dimensions and voxel size as another volume I want to register with. In Matlab the available functions don’t allow to specify voxel size and this is very important for me. Getting inspired by this post: <a href="https://discourse.slicer.org/t/voxelization-of-mesh/4942" class="inline-onebox">Voxelization of mesh</a>,  I follow these steps:</p>
<ol>
<li>Import stl and convert into segmentation node by right clicking on the model entry in the data module.</li>
<li>Import the other volume, and in the volume section specify the voxel size and center it.</li>
<li>Go to the transform model, and create a new transformation which moves the segmentation so that the crucial parts of it overlap the other volume. This step may not be needed.</li>
<li>Go to the Segmentation Module, and select export the segmentation as a labelmap, indicating as  reference volume the other one, so that the output voxelized mask has the same dimensions and voxel size.</li>
<li>Then, go to the volume section, select the just created volume, and convert to scalar volume.</li>
</ol>
<p>I’d like to know if these steps are well or if there is another way to do it better. The stl model sometimes appears to be bigger than the object in the other volume, when it shouldn’t be. And other  thing: should the stl model have some basis features (i.g. closed surface, filled inside etc.)?</p>

---

## Post #2 by @lassoan (2019-08-11 04:54 UTC)

<p>You can do it a bit simpler:</p>
<ul>
<li>Load the STL as segmentation: in “Add data” dialog, choose “Segmentation” in description column</li>
<li>Create master volume of at the desired resolution: Go to Segment Editor module, click on Specify geometry button (next to Master volume selector), select your input mesh as source geometry, specify voxel size (spacing values) and click OK</li>
<li>Create binary labelmap representation: go to Data module, right-click on the segmentation and choose Export visible segments to binary labelmap</li>
</ul>

---

## Post #3 by @UWIZEYE_Clarisse (2021-09-21 17:00 UTC)

<p>Hello,<br>
I am new to this forum, but I use 3DSlicer most of the time. I like the idea of creating the binary label map from the 3Dmodel. However, I don’t know what I did wrong; when I loaded the created binary “file.nrrd” to check if I could reconstruct the 3D from that estimation, they didn’t fit together. Do you know how to fix that?</p>

---

## Post #4 by @lassoan (2021-09-21 17:12 UTC)

<p>Could you attach a screenshot to illustrate what you mean by “didn’t fit together”?</p>
<p>How did you create the file.nrrd file? (using export to files? or by exporting to labelmap volume node and use save scene?)</p>

---

## Post #5 by @UWIZEYE_Clarisse (2021-09-21 17:24 UTC)

<p>A friend of mine used ilaskit to annotate regions of interest and she generated 3D models as obj files. When she tried to recover her work it was gone. Then I suggested to her to create the binary image from her obj file. I load the model and select segmentation then go to the segmentation editor and generate the label map as you suggested.</p>
<p>So to export I got to import/export nodes<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d527d179f8d553e495254fbde8366bfbeff032ec.png" alt="image.png" data-base62-sha1="upF0I0SsxiAn3PcwxtOoCUmCIDq" width="302" height="131"></p>
<p>and export then export to files.</p>
<p>Just by checking if the generated file was fitting to the model to double check before I confirm to her that things it is okay I found the merge not fitting at all; see the screenshot below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2332ac08fe59216f8a990c3b478cce818e43e1d.png" data-download-href="/uploads/short-url/wh3x3ieWZKrfTyo1OLm6w0ep6Nf.png?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2332ac08fe59216f8a990c3b478cce818e43e1d_2_241x221.png" alt="Capture.PNG" data-base62-sha1="wh3x3ieWZKrfTyo1OLm6w0ep6Nf" width="241" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2332ac08fe59216f8a990c3b478cce818e43e1d_2_241x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2332ac08fe59216f8a990c3b478cce818e43e1d_2_361x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2332ac08fe59216f8a990c3b478cce818e43e1d_2_482x442.png 2x" data-dominant-color="757F75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">828×761 8.02 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is a kind of rotation. I was thinking of using volume information to adjust the files but I think you have maybe a better way to go.<br>
Thank you for your help.</p>

---

## Post #6 by @lassoan (2021-09-21 17:42 UTC)

<p>OK, this looks good, the difference is just due to using a different coordinate system convention (RAS or LPS). You can choose which coordinate system convention to use when you import/export models or segmentations. You can also switch between RAS/LPS for a loaded node by mirroring along the first and second axis.</p>

---

## Post #7 by @UWIZEYE_Clarisse (2021-09-21 20:02 UTC)

<p>Excellent. Thank you very much.</p>

---
