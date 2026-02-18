# Can anyone help me with extraction of arteries from CT angiography of brain?

**Topic ID**: 7974
**Date**: 2019-08-10
**URL**: https://discourse.slicer.org/t/can-anyone-help-me-with-extraction-of-arteries-from-ct-angiography-of-brain/7974

---

## Post #1 by @Ritu_Karela (2019-08-10 12:49 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>

---

## Post #2 by @lassoan (2019-08-10 17:50 UTC)

<p>I’ve added some more information to your other related posting:</p>
<aside class="quote quote-modified" data-post="35" data-topic="1263">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vmtk-vessel-filtering-not-working/1263/35">VMTK vessel filtering not working</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can start with simple thresholding, choosing threshold value so low that all vessels that you are interested are included. Then use that for masking and use Grow from seeds. This should allow very clear separation of bone from vessels. 
However, if image is noisy and/or low-resolution, contrast filling is uneven, etc. then it may be hard to choose a threshold value that includes small vessels and you may need to do more manual work, e.g., with Paint effect or Draw tubes effect, with threshol…
  </blockquote>
</aside>


---
