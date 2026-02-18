# How to get the boundary/edges of organs instead of the filled with color?

**Topic ID**: 26836
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/how-to-get-the-boundary-edges-of-organs-instead-of-the-filled-with-color/26836

---

## Post #1 by @Js165 (2022-12-20 00:16 UTC)

<p>How to get the boundary/edges of organs instead of the filled with color?</p>

---

## Post #2 by @lassoan (2022-12-20 05:39 UTC)

<p>You can adjust segmentation visualization options in <code>Segmentations</code> module’s <code>Display</code> section. uncheck <code>Slice fill</code> to only see the boundary of segments without any filling.</p>

---

## Post #3 by @Js165 (2022-12-20 13:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks a lot! It solved my issue. By the way, how can I increase the line width? Currently, <code>Slice Outline</code> is showing as 1.00.</p>

---

## Post #4 by @lassoan (2022-12-20 19:14 UTC)

<p>The 1.0 value (next to the visibility checkbox) refers to the opacity. The line thickness can be set in <code>Display</code> / <code>Advanced</code> section → <code>Slice intersection thickness</code>.</p>

---

## Post #5 by @Js165 (2022-12-20 19:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Solved, thanks!</p>

---

## Post #6 by @Windy (2024-05-01 02:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Is there a way to export this as it is? I tried exporting this as a labelmap and a nrrd, but it get filled during the exporting.</p>
<p>Also as a side question; is there a way to separate inner and outer border (surface, as it is a 3D segment) of a particular segment?</p>

---

## Post #7 by @lassoan (2024-05-01 03:15 UTC)

<p>If you want to get a surface mesh from a segmentation then you can directly export the segmentstion to obj or stl file in Segmentations module; or export to model node and then save the model as obj, stl, ply, vtk, vtp, … file.</p>

---

## Post #8 by @Windy (2024-05-01 04:06 UTC)

<p>Issue in that is I am loosing my unit measure information by that (Am I wrong?). I want to measure thickness of the segment at a later point. By thickness I meant the shortest distance from outer surface to inner surface. For example, refer the below image which shows what I did using STLs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6810dfd90035da2aefd0f90f256c96a34d076fa.png" data-download-href="/uploads/short-url/sk32k0f5Tthf0QgrXSzIRLEKSzU.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6810dfd90035da2aefd0f90f256c96a34d076fa_2_690x419.png" alt="screenshot" data-base62-sha1="sk32k0f5Tthf0QgrXSzIRLEKSzU" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6810dfd90035da2aefd0f90f256c96a34d076fa_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6810dfd90035da2aefd0f90f256c96a34d076fa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6810dfd90035da2aefd0f90f256c96a34d076fa.png 2x" data-dominant-color="CFDDDA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">987×600 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To get to this results what I did was;</p>
<ol>
<li>Create segmentation</li>
<li>Export it as a STL</li>
<li>Separated the inner and outer surface by manually removing the faces that connects the inner and outer surface, i.e. 3 ring like faces in each branch end.</li>
<li>Use trimesh.proximity.thickness to compute the distance between inner and outer surfaces.</li>
</ol>
<p>I have two issues with my approach.</p>
<ol>
<li>Exporting STL make the spatial data to be lost. I don’t know the unit of measurement in the above thickness. Should I just multiply the values I received with my pixel resolution of the original dataset to get the actual thickness value? Or is this my thickness value in micro meters?</li>
<li>I have to manually separate the inner and outer surfaces.</li>
</ol>

---
