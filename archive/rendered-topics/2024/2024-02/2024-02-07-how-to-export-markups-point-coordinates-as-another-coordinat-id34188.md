# How to export Markups point coordinates as another coordinate system

**Topic ID**: 34188
**Date**: 2024-02-07
**URL**: https://discourse.slicer.org/t/how-to-export-markups-point-coordinates-as-another-coordinate-system/34188

---

## Post #1 by @quddngud0598 (2024-02-07 15:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8028975b5ecfe3895a6cbe6fe221de121943bfb1.png" data-download-href="/uploads/short-url/ihK57itvKMzAoI7A9peOUtolpcJ.png?dl=1" title="Q" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8028975b5ecfe3895a6cbe6fe221de121943bfb1_2_690x261.png" alt="Q" data-base62-sha1="ihK57itvKMzAoI7A9peOUtolpcJ" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8028975b5ecfe3895a6cbe6fe221de121943bfb1_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8028975b5ecfe3895a6cbe6fe221de121943bfb1_2_1035x391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8028975b5ecfe3895a6cbe6fe221de121943bfb1_2_1380x522.png 2x" data-dominant-color="73716D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Q</span><span class="informations">1422×538 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I use the Markup function in the Slicer to label a point and export the coordinates as json, the red box and coordinate value are saved.</p>
<p>I found that the coordinates are in the LPS coordinate system. <strong>However, I need the coordinates of the yellow box. Can anyone tell me how to export those coordinates or how I can convert the LPS coordinates to yellow box coordinates?</strong></p>

---

## Post #2 by @pieper (2024-02-07 16:03 UTC)

<p>This should help:  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates</a></p>

---
