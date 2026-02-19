---
topic_id: 35358
title: "The Volume Rendering Feature In My Slicer Is Not Working"
date: 2024-04-08
url: https://discourse.slicer.org/t/35358
---

# The volume rendering feature in my slicer is not working

**Topic ID**: 35358
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/the-volume-rendering-feature-in-my-slicer-is-not-working/35358

---

## Post #1 by @zeeshan (2024-04-08 16:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96ef104d0c47015b73daef9e9beba703fa0f8b59.png" data-download-href="/uploads/short-url/lxdOlPnvKV9pgSBRiMMMoOd2nep.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96ef104d0c47015b73daef9e9beba703fa0f8b59_2_690x331.png" alt="3" data-base62-sha1="lxdOlPnvKV9pgSBRiMMMoOd2nep" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96ef104d0c47015b73daef9e9beba703fa0f8b59_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96ef104d0c47015b73daef9e9beba703fa0f8b59_2_1035x496.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96ef104d0c47015b73daef9e9beba703fa0f8b59.png 2x" data-dominant-color="AEACAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1306×627 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
My volume rendering option is not working. I am unable to see a 3D model after volume rendering. Kindly check this issue.</p>

---

## Post #2 by @lassoan (2024-04-08 16:16 UTC)

<p>It looks like the CT image was acquired with a tilted gantry, which results in a warping transformation. To volume-render a warped volume, the warping transform must be hardened on the volume (see <a href="https://github.com/Slicer/Slicer/issues/6648">related issue</a>). You can do that in Data module: in the volume’s row, right-click on the transforms column and click <code>Harden transform</code>.</p>

---
