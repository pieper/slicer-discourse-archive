---
topic_id: 40270
title: "Select Specific Control Points From Qslicersimplemarkupswidg"
date: 2024-11-19
url: https://discourse.slicer.org/t/40270
---

# Select specific control points from qSlicerSimpleMarkupsWidget

**Topic ID**: 40270
**Date**: 2024-11-19
**URL**: https://discourse.slicer.org/t/select-specific-control-points-from-qslicersimplemarkupswidget/40270

---

## Post #1 by @justomont (2024-11-19 17:30 UTC)

<p>Hey there!</p>
<p>I’m developing a scripted module and I want the user to be able to select and unselect specific markup control points from the module’s GUI, similarly to what can be done from the Markups module. For example, the user here selected control points A2, A4 and A5:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/680c3a8eea2dd1dc34b254a44c3d4479655e5647.png" data-download-href="/uploads/short-url/eQrR7SrMfzumltweJyvtiJUpAzB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680c3a8eea2dd1dc34b254a44c3d4479655e5647_2_517x172.png" alt="image" data-base62-sha1="eQrR7SrMfzumltweJyvtiJUpAzB" width="517" height="172" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680c3a8eea2dd1dc34b254a44c3d4479655e5647_2_517x172.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680c3a8eea2dd1dc34b254a44c3d4479655e5647_2_775x258.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680c3a8eea2dd1dc34b254a44c3d4479655e5647_2_1034x344.png 2x" data-dominant-color="313131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1050×350 38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For the GUI I’m using the ‘qSlicerSimpleMarkupsWidget’ but I cannot work around including the option to select/unselect specific control points. As of right now, it looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fbc7d2149c570d0d6682a6fb5b084d271c11996.png" data-download-href="/uploads/short-url/kvy72QcW0dEhsNG6FHC66EyjFEW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fbc7d2149c570d0d6682a6fb5b084d271c11996.png" alt="image" data-base62-sha1="kvy72QcW0dEhsNG6FHC66EyjFEW" width="391" height="256"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">522×342 13.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How could I accomplish this? I know that I can access if the user selected/unselected in the Markups Module, but I want the user to be able to do it all from the same Module I’m developing.</p>
<p>Thanks in advance!</p>

---
