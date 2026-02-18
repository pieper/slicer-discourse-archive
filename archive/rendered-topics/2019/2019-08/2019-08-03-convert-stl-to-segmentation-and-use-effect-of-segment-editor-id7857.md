# Convert stl to segmentation and use effect of Segment Editor

**Topic ID**: 7857
**Date**: 2019-08-03
**URL**: https://discourse.slicer.org/t/convert-stl-to-segmentation-and-use-effect-of-segment-editor/7857

---

## Post #1 by @Jmarcs (2019-08-03 05:18 UTC)

<p>I would like to convert stl (that i have imported in 3dslicer) to segmentation and use effect of SEGMENT EDITOR<br>
I want the same accurancy and quality that my stl file<br>
Is it possible Please show me the way to do it<br>
best regards<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/104013eddf6fe93496743fb10358ef80552771fe.png" data-download-href="/uploads/short-url/2jKVoktafkX2FWBeI7O7cd9YtVI.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/104013eddf6fe93496743fb10358ef80552771fe_2_690x330.png" alt="Capture" data-base62-sha1="2jKVoktafkX2FWBeI7O7cd9YtVI" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/104013eddf6fe93496743fb10358ef80552771fe_2_690x330.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/104013eddf6fe93496743fb10358ef80552771fe_2_1035x495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/104013eddf6fe93496743fb10358ef80552771fe_2_1380x660.png 2x" data-dominant-color="747E75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1907×913 306 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-08-03 12:33 UTC)

<p>Segment Editor uses labelmap representation for the segments during editing, so the mesh will be converted to that. You can choose the resolution of the labelmap to preserve all details you are interested in. Increasing resolution makes the image larger, so there is a practical upper limit, depending on how powerful your computer is.</p>
<p>What would you like to do with the mesh? If you have a volumetric image to guide the mesh editing or plan to use other visualization, analysis, registration, surgical planning or navigation features of Slicer then it makes sense to edit the mesh in Slicer. If all you need is just some freehand sculpting then you may choose to use mesh modeling software instead, such as Blender.</p>

---
