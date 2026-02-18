# Minimum setup for tracking and navigation

**Topic ID**: 6988
**Date**: 2019-06-01
**URL**: https://discourse.slicer.org/t/minimum-setup-for-tracking-and-navigation/6988

---

## Post #1 by @PaoloZaffino (2019-06-01 15:31 UTC)

<p>Hi all,<br>
I have a question about the integration of Slicer and a tracking/navigation system.<br>
What is the minimum setup (both hardware and software) for running a demo of surgical tools tracking and navigation?</p>
<p>Thanks a lot!<br>
Paolo</p>

---

## Post #2 by @lassoan (2019-06-01 15:56 UTC)

<p>To demonstrate the concept only, you can just use a webcam and print 2D barcodes. It won’t be accurate (can have up to centimeters of error), but you don’t need to buy hardware.</p>
<div class="lazyYT" data-youtube-id="MOqh6wgOOYs" data-youtube-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>For accurate tracking (about a millimeter of total system error), the cheapest device to buy is the <a href="https://www.optitrack.com/products/v120-duo/" rel="nofollow noopener">Optitrack Duo</a> for $2300.</p>
<p>There is an open-source electromagnetic tracker (<a href="https://anser.io/anserlong.html#/" rel="nofollow noopener">Anser</a>) that you have to assemble and calibrate yourself but probably the material cost is no more than a few hundred $ and probably the error is just a few millimeters.</p>
<p>You can also connect Slicer to existing clinical surgical navigation systems (BrainLab and Medtronic are supported right now).</p>

---

## Post #3 by @PaoloZaffino (2019-06-05 08:19 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>!<br>
It is exactly what I was looking for…amazing!</p>
<p>Paolo</p>

---
