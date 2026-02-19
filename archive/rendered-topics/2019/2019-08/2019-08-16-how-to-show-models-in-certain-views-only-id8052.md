---
topic_id: 8052
title: "How To Show Models In Certain Views Only"
date: 2019-08-16
url: https://discourse.slicer.org/t/8052
---

# How to show models in certain views only

**Topic ID**: 8052
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/how-to-show-models-in-certain-views-only/8052

---

## Post #1 by @SebastianE93 (2019-08-16 02:52 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.10.2</p>
<p>At Models Module, in the section of Visibility,<br>
how can I change the View to only Red, Yellow and Green for a ModelNode (with the python console)?<br>
As shown in the picture below.</p>
<p>Thank you in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ac1fea45d841111edd5221211d5c15db2a989c7.png" data-download-href="/uploads/short-url/66fGuYonu1NSAzpfIKi55ElFZJB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ac1fea45d841111edd5221211d5c15db2a989c7_2_459x500.png" alt="image" data-base62-sha1="66fGuYonu1NSAzpfIKi55ElFZJB" width="459" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ac1fea45d841111edd5221211d5c15db2a989c7_2_459x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ac1fea45d841111edd5221211d5c15db2a989c7_2_688x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ac1fea45d841111edd5221211d5c15db2a989c7.png 2x" data-dominant-color="CED1D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">725×789 34.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-08-16 05:09 UTC)

<p>You can specify list of view IDs to show your node in using the display node’s SetViewNodeIDs method. See complete example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_markup_fiducial_display_properties" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @SebastianE93 (2019-08-16 14:46 UTC)

<p>Thank you! It works perfectly.</p>

---
