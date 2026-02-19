---
topic_id: 8026
title: "Dcm Contour Propagation"
date: 2019-08-14
url: https://discourse.slicer.org/t/8026
---

# dcm contour propagation

**Topic ID**: 8026
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/dcm-contour-propagation/8026

---

## Post #1 by @vietlebao (2019-08-14 12:21 UTC)

<p>Hi there, I am a newbie here and it is also the first time asking.</p>
<p>I have a CT image with a manual contour (CT1), and another CT (CT2) image with no contour. I would want to register CT2 to CT1 (I have done this, and now I have a registed_image (CT3)). Now I want to propagate the manual contour from CT1 to CT3.</p>
<p>How can I do that and which package will help.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @cpinter (2019-08-14 12:43 UTC)

<p>I don’t think there is a one-step solution yet, but you can do it following these steps:</p>
<ul>
<li>Download SlicerElastix extension for easy registration of your CT data</li>
<li>Make sure your “contour” is a segmentation in Slicer (if you use Segment Editor or load it from DICOM then it is, otherwise please ask)</li>
<li>Go to Data module. Clone the segmentation (right-click -&gt; Clone). Double click the empty cell in the transforms column, and select the transform to apply it</li>
</ul>

---

## Post #3 by @vietlebao (2019-08-15 01:17 UTC)

<p>Thanks Cpinter. I did not success with final step. transforms column is “transforms hierarchy”? and “select the transform to apply” means I have go to transform module? can you capture on steps?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/231b337f65af481417528a8c22051afa112101f1.png" data-download-href="/uploads/short-url/50yZmmm4t8pRof8SHbjcVkXMuqZ.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/231b337f65af481417528a8c22051afa112101f1.png" alt="Untitled" data-base62-sha1="50yZmmm4t8pRof8SHbjcVkXMuqZ" width="530" height="500" data-dominant-color="EDF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">567×534 32.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-08-15 03:05 UTC)

<p>You can apply transforms at various places, whichever you find the most convenient for your workflow:</p>
<ul>
<li>in Data module’s “Subject hierarchy” tab as <a class="mention" href="/u/cpinter">@cpinter</a> described above (double-click in transform column).</li>
<li>in Data module’s “Transform hierarchy” by drag-and-drop</li>
<li>in Transforms module’s “Apply transform” section, by selecting nodes in the “Transformable” node tree and clicking the green arrow buttons</li>
</ul>

---

## Post #5 by @vietlebao (2019-08-15 06:45 UTC)

<p>Thanks Lassoan and Cpinter. I did it.</p>

---
