# Import segmentation from model is too coarse

**Topic ID**: 2914
**Date**: 2018-05-23
**URL**: https://discourse.slicer.org/t/import-segmentation-from-model-is-too-coarse/2914

---

## Post #1 by @kayarre (2018-05-23 19:04 UTC)

<p>When I open a closed surface model and attempt to import it into the segmentation the resulting segmentation is very coarse and doesn’t match the voxel resolution of the background image volume and I don’t see a way to edit the resolution.</p>
<p>how can I get the reslution to match the background image?<br>
see the image the blue is the segmentation based on the background image and the yellow is the segmentation from the imported model.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3422ce30b36d93827ccf66e9799ff780fb66c96b.jpeg" alt="scan0001" data-base62-sha1="7rdoIOmX0pobOKyiJX7SiKEH1uX" width="559" height="383"></p>

---

## Post #2 by @cpinter (2018-05-23 19:28 UTC)

<p>Reference geometry is not defined for a new segmentation, only if you edit a segment in Segment Editor with a master volume specified. In that case the resolution will be 1x1x1mm^3.</p>
<p>In the current version the only way to specify the geometry in such a case is like this:</p>
<ul>
<li>Make the closed surface the master representation. You can do that in the Representations section in the Segmentations module</li>
<li>Long-click the Create button in the row of Binary labelmap</li>
<li>Click the only path in the top half of the popup window</li>
<li>Click the “Set geometry from volume” button in the bottom half, in the row of Reference image geometry</li>
<li>Set the volume you want the geometry to come from</li>
</ul>
<p>We should really rework the reference geometry part of the user interface, but it has never reached the top of the priority list up to this point. At the least probably we should allow selecting a reference volume in the Advanced section of the Export/import panel when we import models. Currently it’s only enabled when exporting labelmaps. <a class="mention" href="/u/kayarre">@kayarre</a> and <a class="mention" href="/u/lassoan">@lassoan</a> what do you think?</p>

---

## Post #3 by @lassoan (2018-07-17 21:50 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-import-export-segmentation-as-nrrd-file/3509">How to import/export segmentation as nrrd file?</a></p>

---
