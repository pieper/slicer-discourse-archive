---
topic_id: 41280
title: "How To Renumber Segment Labels After Deleting Regions In A L"
date: 2025-01-25
url: https://discourse.slicer.org/t/41280
---

# How to Renumber Segment Labels After Deleting Regions in a Label File?

**Topic ID**: 41280
**Date**: 2025-01-25
**URL**: https://discourse.slicer.org/t/how-to-renumber-segment-labels-after-deleting-regions-in-a-label-file/41280

---

## Post #1 by @ebhebh (2025-01-25 12:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29aae44ea1e61f1db4767734d0fccdc5232353ed.png" data-download-href="/uploads/short-url/5WBI2wBFMHgx2QxS522rHaQ3Qkt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29aae44ea1e61f1db4767734d0fccdc5232353ed_2_690x355.png" alt="image" data-base62-sha1="5WBI2wBFMHgx2QxS522rHaQ3Qkt" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29aae44ea1e61f1db4767734d0fccdc5232353ed_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29aae44ea1e61f1db4767734d0fccdc5232353ed_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29aae44ea1e61f1db4767734d0fccdc5232353ed_2_1380x710.png 2x" data-dominant-color="919093"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×976 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Dear 3D Slicer Community,</p>
<p>I need some assistance with modifying a label file. The file contains five segmented regions, labeled 1, 2, 3, 4, and 5. I would like to delete the segments corresponding to labels 1 and 2, leaving only the regions with labels 3, 4, and 5. However, I want to update the label numbers of the remaining segments, so that the new labels will be 1, 2, and 3, respectively (instead of 3, 4, and 5).</p>
<p>Could you please guide me on how to:</p>
<ol>
<li>Delete the segments labeled 1 and 2.</li>
<li>Reassign the labels of the remaining segments to 1, 2, and 3.</li>
</ol>
<p>I would appreciate any help or suggestions on how to perform these actions within 3D Slicer.</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2025-01-29 11:09 UTC)

<p>If you use a segmentation node instead of a labelmap volume node, I think you can just delete the segments and when you export to labelmap, the label numbers will start at 1. Segment names and IDs do not have an effect on the labelmap labels. Isn’t this so?</p>
<p>Actually I think it is counterproductive using integers as segment names, better use terminologies and automatically generated names from those entries.</p>

---

## Post #3 by @ebhebh (2025-02-08 08:23 UTC)

<p>Thanks! I’ll try it sometime and see if I can fix it.</p>

---
