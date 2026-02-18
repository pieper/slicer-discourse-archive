# Poor segmentation and intersection performance

**Topic ID**: 31344
**Date**: 2023-08-24
**URL**: https://discourse.slicer.org/t/poor-segmentation-and-intersection-performance/31344

---

## Post #1 by @d0rnkernsky (2023-08-24 20:25 UTC)

<p>Hello everyone!</p>
<p>I have troubles with slicer’s performance while working with segmentation and segments. My goal is to build a heart segmentation that consists of 360 small segments. My workflow has two parts:</p>
<p>Part A: load a myocardium segmentation (a single object in seg.nrrd format) and add 360 wedges around it (like a cylinder)<br>
Context: Slicer loads it as a binary label map representation, I have to convert it to closed surface otherwise the wedging takes several hours vs. 3 minutes now. I use the AddSegmentFromClosedSurfaceRepresentation function to add the wedges.</p>
<p>Part B: take the intersection between the initial myocardium segmentation and each wedge.<br>
Context: When Part A completes, a window pops up saying that in order to edit the representation I have to convert it to a binary label map, which I do. The conversion takes 20 seconds. Then taking the intersections takes 50 minutes at best to complete.</p>
<p>I have several questions:</p>
<ol>
<li>Is intersection only available for binary label maps?</li>
<li>Is there a way to make taking the intersections faster? For example, doing it in a CLI module without visualizing it.</li>
</ol>
<p>Please let me know if I am not being clear. I will greatly appreciate your help.</p>

---
