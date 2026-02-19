---
topic_id: 18645
title: "Segmentation Of Teeth"
date: 2021-07-12
url: https://discourse.slicer.org/t/18645
---

# Segmentation of teeth

**Topic ID**: 18645
**Date**: 2021-07-12
**URL**: https://discourse.slicer.org/t/segmentation-of-teeth/18645

---

## Post #1 by @Lucky_Girish (2021-07-12 17:05 UTC)

<p>Hi, I want to extract teeth from  a cbct, as different layers inside the teeth along with the nerves like here :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35f327621e97beed75ad51186f65da2fed2274bb.jpeg" data-download-href="/uploads/short-url/7Hgg9SI1F1E6NyRR31Xt46MkJN9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35f327621e97beed75ad51186f65da2fed2274bb_2_456x500.jpeg" alt="image" data-base62-sha1="7Hgg9SI1F1E6NyRR31Xt46MkJN9" width="456" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35f327621e97beed75ad51186f65da2fed2274bb_2_456x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35f327621e97beed75ad51186f65da2fed2274bb_2_684x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35f327621e97beed75ad51186f65da2fed2274bb_2_912x1000.jpeg 2x" data-dominant-color="EFE2D7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1460×1600 403 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Enamel,Dentin, Pulp, Nerves, Gum as diferent layers such that to carry out the stress analysis</p>
<p>If yes , pls provide me with some tutorial or any relevant documentation. I am new to slicer and this is for my study project.</p>
<p>Pls Help.</p>
<p>Thank you</p>

---

## Post #2 by @mohammed_alshakhas (2021-07-12 17:47 UTC)

<p>I don’t think cbct will help , unless you get high resolution small field images .<br>
I personally hate working with cbct . Medical CT with thin slices is way if you don’t have metal restorations  .</p>
<p>What I suggest if you do have high quality images is that you alter contrast from the top tool bar to increase contrast between layers then use threshold to segment .</p>

---
