# Script to compute Voronoi diagrams/largest aorta diameter using VMTK

**Topic ID**: 17549
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/script-to-compute-voronoi-diagrams-largest-aorta-diameter-using-vmtk/17549

---

## Post #1 by @banderies (2021-05-10 19:04 UTC)

<p>I have a large number of aorta segmentations (nifti masks), and I would like to figure out how to load each one and compute the largest diameter (aneurysm). It looks as if computing a Voronoi diagram using VMTK is an ideal solution, but I would like to write an extension to automatically load the segmentations from a folder, run the appropriate computations, and save the output. I would really appreciate it if someone could point me to any examples that I might start to learn from/adapt for this purpose.</p>
<p>From using the VMTK extension manually, I think the steps I would need to script are:</p>
<ol>
<li>Load the nifti mask as a volume (seemingly can’t be loaded as a segmentation without loading a corresponding volume as well)</li>
<li>Apply a simple threshold to get a segmentation (mask will be 0 or 1)</li>
<li>Simplify mesh/create model appropriate for VMTK processing</li>
<li>Compute Voronoi diagram and centerlines</li>
<li>Extract data as table(?) and/or save the largest diameter</li>
</ol>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-05-11 03:37 UTC)

<p>To use VTK from a script in Slicer’s Python environment:</p>
<aside class="quote no-group" data-username="banderies" data-post="1" data-topic="17549">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/cdc98d/48.png" class="avatar"> banderies:</div>
<blockquote>
<ol>
<li>Load the nifti mask as a volume (seemingly can’t be loaded as a segmentation without loading a corresponding volume as well)</li>
<li>Apply a simple threshold to get a segmentation (mask will be 0 or 1)</li>
</ol>
</blockquote>
</aside>
<p>Instead of these steps, you can load the nifti mask directly as a segmentation node. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-a-3d-image-or-model-file-as-segmentation">example</a>.</p>
<p>If you want to run some additional Segment Editor effects, you can load the mask as a scalar volume and use it as master volume and then follow <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-segment-editor-effects-from-script-qmrmlsegmenteditorwidget">these examples</a>.</p>
<aside class="quote no-group" data-username="banderies" data-post="1" data-topic="17549">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/cdc98d/48.png" class="avatar"> banderies:</div>
<blockquote>
<ul>
<li>Simplify mesh/create model appropriate for VMTK processing</li>
<li>Compute Voronoi diagram and centerlines</li>
<li>Extract data as table(?) and/or save the largest diameter</li>
</ul>
</blockquote>
</aside>
<p>You can use <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py">Extract Centerline</a> module logic class from your own scripts or copy paste any parts of the modules into your scripts.</p>
<p>If the aneurysms are not just slightly dilated vessels but ballooning out then instead of centerline analysis you may consider segmenting the aneurysm sack and get shape properties using Segment Statistics module (there are <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">many optional shape metrics</a> that you can enable).</p>

---
