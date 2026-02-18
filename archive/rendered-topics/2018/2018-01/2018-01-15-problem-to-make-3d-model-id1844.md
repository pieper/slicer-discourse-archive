# Problem to make 3D model

**Topic ID**: 1844
**Date**: 2018-01-15
**URL**: https://discourse.slicer.org/t/problem-to-make-3d-model/1844

---

## Post #1 by @Kamil (2018-01-15 14:05 UTC)

<p>Hi,</p>
<p>As usual I wanted to create a 3D model using Editor. I set up the threshold and press Model Maker. However this time I have below error.</p>
<hr>
<p>ERROR: no model scene defined! Using slicer:00000272B4204780#vtkMRMLLabelMapVolumeNode1.mrml<br>
WARNING: If you started Model Maker from the Slicer3 GUI, the models will NOT be loaded automatically.<br>
You must use File-&gt;Import Scene slicer:00000272B4204780#vtkMRMLLabelMapVolumeNode1.mrml to see your models (don’t use Load or it will close your current scene).</p>
<hr>
<p>Model scene file doesn’t exist yet: slicer:00000272B4204780#vtkMRMLLabelMapVolumeNode1.mrml<br>
Error: no model hierarchy node at ID “”, creating one<br>
Error reading colour file C:/Users/LMECAL~1/AppData/Local/Temp/Slicer/FGEA_vtkMRMLColorTableNodeFileGenericAnatomyColors.txt.ctbl</p>
<p>I used the CT data that worked in pass but it does not work as well. Somebody know what it can be a problem? I have already reinstalled Slicer. My version is 4.8.1.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2018-01-15 14:41 UTC)

<aside class="quote no-group" data-username="Kamil" data-post="1" data-topic="1844">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/94ad74/48.png" class="avatar"> Kamil:</div>
<blockquote>
<p>As usual I wanted to create a 3D model using Editor</p>
</blockquote>
</aside>
<p>The legacy Editor module is only kept there for backward compatibility. Please use Segment Editor module instead, which has many more and better features that can help you to create much higher quality segmentations in a fraction of the time. You can display segmentation in 3D by a single click (it is kept in sync with the slice views automatically). You can export the 3D representation of the segmentation to a model node using 3 clicks. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">here</a>.</p>
<p>To answer your specific question, in the “Models” field, you need to specify a model hierarchy, for example by clicking on the node selector then choosing “Create new ModelHierarchy”.</p>

---

## Post #3 by @pieper (2018-01-15 15:16 UTC)

<p><a class="mention" href="/u/kamil">@Kamil</a> is this behavior new and reproducible with 4.8.1 but doesn’t happen with 4.8?  Or did something else change on your computer?</p>

---

## Post #4 by @lassoan (2018-01-16 12:37 UTC)

<p>3 posts were split to a new topic: <a href="/t/how-to-get-same-voxel-values-in-matlab-as-in-slicer/1854">How to get same voxel values in Matlab as in Slicer</a></p>

---
