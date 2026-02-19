---
topic_id: 6842
title: "Changing Image Display Between 4 10 X And 4 8 X Using The Sa"
date: 2019-05-18
url: https://discourse.slicer.org/t/6842
---

# Changing image display between 4.10.x and 4.8.x using the same Window level and lookup table ?

**Topic ID**: 6842
**Date**: 2019-05-18
**URL**: https://discourse.slicer.org/t/changing-image-display-between-4-10-x-and-4-8-x-using-the-same-window-level-and-lookup-table/6842

---

## Post #1 by @runze (2019-05-18 13:54 UTC)

<p>I used 4.8.1 and started to use 4.10.1 recently. I found that they showed the same image in different gray levels.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16e37577276d4d369971597e7b2cdb2a0798f817.png" data-download-href="/uploads/short-url/3gtPCQFuvo4o8WyEhhE977FApAH.png?dl=1" title="10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16e37577276d4d369971597e7b2cdb2a0798f817_2_481x500.png" alt="10" data-base62-sha1="3gtPCQFuvo4o8WyEhhE977FApAH" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16e37577276d4d369971597e7b2cdb2a0798f817_2_481x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16e37577276d4d369971597e7b2cdb2a0798f817_2_721x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16e37577276d4d369971597e7b2cdb2a0798f817_2_962x1000.png 2x" data-dominant-color="EFEBE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">10</span><span class="informations">963×1001 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have the same window level and lookup table settings. The data was loaded through PETDICOMextension. It seems that the value of the pixels is the same.</p>
<p>Just wondering what is different between 4.8.1 and 4.10.1 in displaying the image?</p>

---

## Post #2 by @lassoan (2019-05-18 14:10 UTC)

<p>I don’t see any difference between the two images above.</p>

---

## Post #3 by @runze (2019-05-26 01:27 UTC)

<p>For example, there are some black dots under the skin, maybe muscle. The bottom one (4.10.1) looks like less darker than the top one (4.8.1). Because the gray-scale represent the value of the pixels, it gives an impression that those pixels have different value, even though they are identical.</p>

---

## Post #4 by @pieper (2019-05-26 17:55 UTC)

<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a> that the effect is pretty subtle.  <a class="mention" href="/u/runze">@runze</a> do you think these differences have clinical significance?  Also do you have any way of knowing which one is more correct? (for example in comparison to a clinical system).</p>

---
