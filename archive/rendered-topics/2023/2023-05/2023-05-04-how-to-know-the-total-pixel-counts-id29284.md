---
topic_id: 29284
title: "How To Know The Total Pixel Counts"
date: 2023-05-04
url: https://discourse.slicer.org/t/29284
---

# How to know the total pixel counts?

**Topic ID**: 29284
**Date**: 2023-05-04
**URL**: https://discourse.slicer.org/t/how-to-know-the-total-pixel-counts/29284

---

## Post #1 by @akmal871026 (2023-05-04 09:21 UTC)

<p>Dear Sir,</p>
<p>I did the VOI (Volume of interest) on my image. But the total counts of pixel in the VOI do not appear in the table after I did the quantification as picture attached<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/970cb58b4cca29a981259f2f5d13b61ef067e31a.jpeg" data-download-href="/uploads/short-url/lyfki497ut16AYGM8ZhiyB22tfk.jpeg?dl=1" title="VOI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970cb58b4cca29a981259f2f5d13b61ef067e31a_2_617x499.jpeg" alt="VOI" data-base62-sha1="lyfki497ut16AYGM8ZhiyB22tfk" width="617" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970cb58b4cca29a981259f2f5d13b61ef067e31a_2_617x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970cb58b4cca29a981259f2f5d13b61ef067e31a_2_925x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970cb58b4cca29a981259f2f5d13b61ef067e31a_2_1234x998.jpeg 2x" data-dominant-color="E8E8E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VOI</span><span class="informations">2864×2320 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
.</p>
<p>Anyone can help me. the data set is attached <a href="https://drive.google.com/file/d/1vHGkqyk6V1-2-8StsyJs8mec96plxYpl/view?usp=share_link" class="inline-onebox" rel="noopener nofollow ugc">000000.dcm - Google Drive</a> .</p>

---

## Post #2 by @rbumm (2023-05-04 12:23 UTC)

<p>Enable “Labelmap statistics”, Go “Options”, check “Voxel count”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f1240674e25a39468f132547c628a89426e2405.png" data-download-href="/uploads/short-url/kpFnGMcF9kuCbmMLr4hs0S4hibr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f1240674e25a39468f132547c628a89426e2405_2_690x378.png" alt="image" data-base62-sha1="kpFnGMcF9kuCbmMLr4hs0S4hibr" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f1240674e25a39468f132547c628a89426e2405_2_690x378.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f1240674e25a39468f132547c628a89426e2405_2_1035x567.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f1240674e25a39468f132547c628a89426e2405.png 2x" data-dominant-color="B6B4B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1243×681 98.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @akmal871026 (2023-05-04 13:46 UTC)

<p>I was. But still not appear in table</p>

---

## Post #4 by @rbumm (2023-05-04 13:55 UTC)

<p>Did you select the scalar volume?</p>
<p>All voxel count is working here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5740edaf388da4b9ff3dbfbeff9eb6a5367336eb.png" data-download-href="/uploads/short-url/crSEcQdDvKRZWUICfkKXp4YRAZZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5740edaf388da4b9ff3dbfbeff9eb6a5367336eb_2_690x359.png" alt="image" data-base62-sha1="crSEcQdDvKRZWUICfkKXp4YRAZZ" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5740edaf388da4b9ff3dbfbeff9eb6a5367336eb_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5740edaf388da4b9ff3dbfbeff9eb6a5367336eb_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5740edaf388da4b9ff3dbfbeff9eb6a5367336eb.png 2x" data-dominant-color="908F8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1239×646 80.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @akmal871026 (2023-05-04 14:02 UTC)

<p>then where are your total counts in voi?</p>

---

## Post #6 by @rbumm (2023-05-04 15:31 UTC)

<p>The count is given as 7760, referring to Segment 1.</p>

---

## Post #7 by @akmal871026 (2023-05-04 15:39 UTC)

<p>that one is a number of voxels. <strong>not total counts of voxel</strong></p>

---

## Post #8 by @jamesobutler (2023-05-04 15:46 UTC)

<p>You are wanting to sum the Hounsfield values of all the voxels of the scalar volume within the segmentation? How do you plan to use that statistic? SegmentStatistics already provides mean, median, min, max type values. Mean * number of voxels should give you your total sum of the corresponding Hounsfield values.</p>

---

## Post #9 by @akmal871026 (2023-05-04 16:00 UTC)

<p>I see…then total pixel counts is mean*total voxel</p>

---

## Post #10 by @muratmaga (2023-05-04 17:23 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="9" data-topic="29284">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>pixel counts</p>
</blockquote>
</aside>
<p>in 3D there is no pixel (picture elements), the correct term is voxel (volume element).</p>

---
