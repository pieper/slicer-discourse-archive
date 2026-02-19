---
topic_id: 4030
title: "Improve The Resolution Of Segment For Import A Model"
date: 2018-09-09
url: https://discourse.slicer.org/t/4030
---

# Improve the resolution of segment for "import a model"

**Topic ID**: 4030
**Date**: 2018-09-09
**URL**: https://discourse.slicer.org/t/improve-the-resolution-of-segment-for-import-a-model/4030

---

## Post #1 by @timeanddoctor (2018-09-09 00:25 UTC)

<p>What I am doing is to have a boolean opertation between two cylinder created by MakerupToModel.<br>
But the segment resolution seems not very well even after “crop volume wih 0.01 spacing scale” just as suggestion: <a href="https://discourse.slicer.org/t/segmentation-resolution/1394/10">Segmentation resolution</a>.</p>

---

## Post #2 by @lassoan (2018-09-09 11:59 UTC)

<p>The orange contour seems to be sufficiently high resolution. If you do not wish to see the underlying labelmap representation (that is always made up of rectangular voxels) then you can choose to view the closed surface representation (Segmentations module / Display / Advanced / Representation in 2D views: Closed surface). If that is still not smooth enough then you can reduce the spacing even further.</p>
<p>Note that in recent nightly builds, you can adjust voxel size in an existing segmentation (in Segment editor, click on the icon on the right side of Master volume selector). You still need to re-import the model but you don’t need to create a new segmentation each time you change the resolution.</p>

---

## Post #3 by @timeanddoctor (2018-09-09 23:11 UTC)

<p>Thank you Professor Lassoan.<br>
The segment become rough after a boolean operation just like the Ring structure showed in the pictures.<br>
The ring stucture created from a empty volume with little spacing and the other were copied from other segmentation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52910c2e68d705831952dd598e2d1ed0a6bdc269.jpeg" alt="360%E6%88%AA%E5%9B%BE-100573046" data-base62-sha1="bMpULwQVRfxI8nnuZtYTNWQGGhP" width="460" height="368"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9891c6b9921b95045f6d85a507c676d501d4d3a.jpeg" data-download-href="/uploads/short-url/obMrZAbYgpwHN31I5YmC3acfIjE.jpeg?dl=1" title="360%E6%88%AA%E5%9B%BE-100781578" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9891c6b9921b95045f6d85a507c676d501d4d3a_2_690x416.jpeg" alt="360%E6%88%AA%E5%9B%BE-100781578" data-base62-sha1="obMrZAbYgpwHN31I5YmC3acfIjE" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9891c6b9921b95045f6d85a507c676d501d4d3a_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9891c6b9921b95045f6d85a507c676d501d4d3a_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9891c6b9921b95045f6d85a507c676d501d4d3a.jpeg 2x" data-dominant-color="A5A6A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">360%E6%88%AA%E5%9B%BE-100781578</span><span class="informations">1211×731 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @timeanddoctor (2018-09-09 23:15 UTC)

<p>Can I have a boolean operation between segments by python script?<br>
And who can help me complete the code.<br>
Thanks!</p>

---

## Post #5 by @lassoan (2018-09-12 04:16 UTC)

<p>The resolution change that you described is a bug. Logical operator effect assumes all segments have the same resolution, but resolution of imported segments are not changed until the segments are modified. You can enforce resampling by clicking on the box icon on the right side of Master volume selector in Segment editor, then clicking on OK.</p>
<aside class="quote no-group" data-username="timeanddoctor" data-post="4" data-topic="4030">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>Can I have a boolean operation between segments by python script?</p>
</blockquote>
</aside>
<p>See how to run an effect from script <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">here</a>. You can find Logical operator effect parameters in <a href="https://github.com/Slicer/Slicer/blob/ad474e559bd6db6b54f037f79f445c6d4cd70d6f/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py#L88-L91">implementation of the effect</a>.</p>

---

## Post #6 by @timeanddoctor (2018-09-15 09:43 UTC)

<p>Can I open the “overwrite other segments” as Visible segments with code?</p>
<p><code>    effect.actor.VisibilityOff(1)</code>?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/110a4271efcb8bf9d404ffb558f24029533fc177.png" alt="image" data-base62-sha1="2qK64EpJdmeVbvjvznGwNclEvll" width="534" height="88"></p>

---

## Post #7 by @lassoan (2018-09-15 12:39 UTC)

<p>You can set overwrite mode in the segment editor widget node’s <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html#a99d0b1484b13c76df303e62b17ba5942">SetOverwriteMode()</a> method.</p>

---
