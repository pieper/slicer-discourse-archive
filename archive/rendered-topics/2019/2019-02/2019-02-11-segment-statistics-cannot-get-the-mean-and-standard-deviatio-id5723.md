---
topic_id: 5723
title: "Segment Statistics Cannot Get The Mean And Standard Deviatio"
date: 2019-02-11
url: https://discourse.slicer.org/t/5723
---

# Segment statistics-- cannot get the mean and standard deviation

**Topic ID**: 5723
**Date**: 2019-02-11
**URL**: https://discourse.slicer.org/t/segment-statistics-cannot-get-the-mean-and-standard-deviation/5723

---

## Post #1 by @TingtingYu (2019-02-11 07:56 UTC)

<p>Hi,</p>
<p>I used <strong>segment statistics</strong> to calculate the mean and standard deviation. However, I only get the <strong>Surface area and Volume</strong>, would you mind letting me what is going on? Why I cannot get other measurement values, such as mean, standard deviation, etc.</p>
<p>Best,<br>
Tingting<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcb74de76fad36c4b44842a0ce9d3a4576c8f983.png" data-download-href="/uploads/short-url/vuxLOpbAQ8he73cpt5UzSovEt9N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcb74de76fad36c4b44842a0ce9d3a4576c8f983_2_564x500.png" alt="image" data-base62-sha1="vuxLOpbAQ8he73cpt5UzSovEt9N" width="564" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcb74de76fad36c4b44842a0ce9d3a4576c8f983_2_564x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcb74de76fad36c4b44842a0ce9d3a4576c8f983_2_846x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcb74de76fad36c4b44842a0ce9d3a4576c8f983.png 2x" data-dominant-color="B8B8B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1063×942 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2019-02-11 15:10 UTC)

<p>Probably your segmentation does not have labelmap representation. Go to Segmentations module, and in the Representations panel click Create for Binary labelmap. Then try to run Segment Statistics again.</p>

---

## Post #3 by @TingtingYu (2019-02-12 03:05 UTC)

<p>Hi Csaba,</p>
<p>Thank you. you method is helpful, I can get the other measurement values now.</p>
<p>Best,<br>
Tingting</p>

---
