---
topic_id: 26104
title: "Model Registration As Measurement Of Displacement"
date: 2022-11-07
url: https://discourse.slicer.org/t/26104
---

# Model registration as measurement of displacement

**Topic ID**: 26104
**Date**: 2022-11-07
**URL**: https://discourse.slicer.org/t/model-registration-as-measurement-of-displacement/26104

---

## Post #1 by @jegberink (2022-11-07 09:28 UTC)

<p>Hey Everyone,</p>
<p>I’m using ALPACA from Slicermorph to measure the rotation and translation from a preoperative, postoperative and planning of the femoral head after an osteotomy.</p>
<p>Explanation of my methods:</p>
<p>I have a preoperative CT and a postoperative CT of a patient. I also have a 3d model of a planning.<br>
I segment the femur for both preoperative and postoperative.</p>
<p>I alligned all of the femoral shafts (with ALPACA) and created a coordinate system so i can measure all patients from a similar point. as shown here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cf05665f9423c8c8ed4f11d3712e69938666545.png" data-download-href="/uploads/short-url/hPg7Slm9QvZIEKqiVcObOFDPbGR.png?dl=1" title="front view femur alligned" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cf05665f9423c8c8ed4f11d3712e69938666545_2_398x500.png" alt="front view femur alligned" data-base62-sha1="hPg7Slm9QvZIEKqiVcObOFDPbGR" width="398" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cf05665f9423c8c8ed4f11d3712e69938666545_2_398x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cf05665f9423c8c8ed4f11d3712e69938666545.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cf05665f9423c8c8ed4f11d3712e69938666545.png 2x" data-dominant-color="9287C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">front view femur alligned</span><span class="informations">499×626 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now i overlap the proximal femur above the saw cut with ALPACA, to see how it has changed in terms of rotations and translations like this (yellow= PreOp, Blue= PostOp, Red=planning):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02863b1fdc00816e3abcf7497e2eecf914e8707d.png" data-download-href="/uploads/short-url/mkxGXS0TGJL4ITy24SaTGEPlEh.png?dl=1" title="front view femur alligned overlap proximal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02863b1fdc00816e3abcf7497e2eecf914e8707d_2_636x500.png" alt="front view femur alligned overlap proximal" data-base62-sha1="mkxGXS0TGJL4ITy24SaTGEPlEh" width="636" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02863b1fdc00816e3abcf7497e2eecf914e8707d_2_636x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02863b1fdc00816e3abcf7497e2eecf914e8707d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02863b1fdc00816e3abcf7497e2eecf914e8707d.png 2x" data-dominant-color="907EB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">front view femur alligned overlap proximal</span><span class="informations">823×646 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I thought it would be possible to subtract the difference in each plane to get the difference between postoperative and planning. However, this does not seem to coincide.<br>
when i use ALPACA to overlap postoperative to the planning like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1609d4d1d3a600d428c9e6cfc1f5b021bf1714bf.png" data-download-href="/uploads/short-url/38XzcTmNA7vV4hHcFU8X2nWvA1F.png?dl=1" title="post to planning" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1609d4d1d3a600d428c9e6cfc1f5b021bf1714bf_2_355x500.png" alt="post to planning" data-base62-sha1="38XzcTmNA7vV4hHcFU8X2nWvA1F" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1609d4d1d3a600d428c9e6cfc1f5b021bf1714bf_2_355x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1609d4d1d3a600d428c9e6cfc1f5b021bf1714bf.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1609d4d1d3a600d428c9e6cfc1f5b021bf1714bf.png 2x" data-dominant-color="958BBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">post to planning</span><span class="informations">412×579 77.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I get the following rotations and translations:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f17e1b7974b464f4ade45e2435fb9983208042c.png" data-download-href="/uploads/short-url/4r3Y0De9rCOP3njCjmIt04sH6Mc.png?dl=1" title="output slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f17e1b7974b464f4ade45e2435fb9983208042c_2_689x258.png" alt="output slicer" data-base62-sha1="4r3Y0De9rCOP3njCjmIt04sH6Mc" width="689" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f17e1b7974b464f4ade45e2435fb9983208042c_2_689x258.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f17e1b7974b464f4ade45e2435fb9983208042c_2_1033x387.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f17e1b7974b464f4ade45e2435fb9983208042c.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">output slicer</span><span class="informations">1299×487 25.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My understanding of this is clearly flawed, if there is anyone who could explain to me where i’m going wrong in my thinking i would greatly appreciate it.</p>

---

## Post #2 by @lassoan (2022-12-01 07:54 UTC)

<p>Comparing pose differences is a very complex topic and there are many potential approaches. Based on the clinical requirements, you need to specify exactly what differences you want to quantify, such as rotation around a specific axis, surface-to-surface distance in a specific region, absolute orientation difference, orientation difference of vectors projected on a specific plane,…</p>

---
