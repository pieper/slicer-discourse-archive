---
topic_id: 41926
title: "Slicerspectrecon On Ubuntu"
date: 2025-03-01
url: https://discourse.slicer.org/t/41926
---

# SlicerSPECTRecon on Ubuntu

**Topic ID**: 41926
**Date**: 2025-03-01
**URL**: https://discourse.slicer.org/t/slicerspectrecon-on-ubuntu/41926

---

## Post #1 by @Michel_Atieh (2025-03-01 11:12 UTC)

<p>Hello,<br>
I recently discovered the extension SlicerSPECTRecon and have successfully been able to get it working on Windows with 3D Slicer version 5.6.2.<br>
However, I am encountering issues when trying to run it on Ubuntu. Do you have any idea why this might be happening?</p>
<p>Thank you for your support and for the great work!<br>
Kind regards,<br>
Michel<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dac1cbaf3661b00bd50685d8db00b40977f4514.png" data-download-href="/uploads/short-url/kdi4t4M3kRfrfOuTbo8Y9kegDT6.png?dl=1" title="Screenshot from 2025-02-28 12-31-06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dac1cbaf3661b00bd50685d8db00b40977f4514_2_690x374.png" alt="Screenshot from 2025-02-28 12-31-06" data-base62-sha1="kdi4t4M3kRfrfOuTbo8Y9kegDT6" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dac1cbaf3661b00bd50685d8db00b40977f4514_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dac1cbaf3661b00bd50685d8db00b40977f4514_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dac1cbaf3661b00bd50685d8db00b40977f4514_2_1380x748.png 2x" data-dominant-color="302D2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-28 12-31-06</span><span class="informations">1853×1005 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-03-01 13:39 UTC)

<p>I haven’t used that extension myself, but I can see in the screenshot that <code>torchvision</code> is not found.   You can try the <a href="https://github.com/fepegar/SlicerPyTorch/tree/e1c85cc0a62e92fa6c38223cd88c611906adb60e">SlicerPyTorch</a> extension.</p>

---
