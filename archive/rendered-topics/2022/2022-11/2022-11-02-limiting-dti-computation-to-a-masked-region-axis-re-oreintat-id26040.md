# Limiting DTI computation to a masked region, axis re-oreintaton

**Topic ID**: 26040
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/limiting-dti-computation-to-a-masked-region-axis-re-oreintaton/26040

---

## Post #1 by @Ron (2022-11-02 16:47 UTC)

<p>To all,</p>
<ol>
<li>I am trying to limit the computation of the DTI data to a masked region (created using the segment editor) within the volume (in this case a human disc). For reference, I am trying to remove the green regions around the disc.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb169f0e83b32e1ac94e0000aeec740a409797de.jpeg" data-download-href="/uploads/short-url/zPejhAsgGkzXUi5EkwkIiOv0wBU.jpeg?dl=1" title="Master Scene View" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb169f0e83b32e1ac94e0000aeec740a409797de_2_620x500.jpeg" alt="Master Scene View" data-base62-sha1="zPejhAsgGkzXUi5EkwkIiOv0wBU" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb169f0e83b32e1ac94e0000aeec740a409797de_2_620x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb169f0e83b32e1ac94e0000aeec740a409797de_2_930x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb169f0e83b32e1ac94e0000aeec740a409797de_2_1240x1000.jpeg 2x" data-dominant-color="60595B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Master Scene View</span><span class="informations">1296×1045 673 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>How would re-Oriente the imaging planes ( green and yellow) windows to better match the disc anatomical axes<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb21d27d3f6779ac6e5b339a8a519a7131e1214d.jpeg" data-download-href="/uploads/short-url/xy4FuVnvXVopl3mI6wpTh21T6GN.jpeg?dl=1" title="Imaging axes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb21d27d3f6779ac6e5b339a8a519a7131e1214d_2_579x500.jpeg" alt="Imaging axes" data-base62-sha1="xy4FuVnvXVopl3mI6wpTh21T6GN" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb21d27d3f6779ac6e5b339a8a519a7131e1214d_2_579x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb21d27d3f6779ac6e5b339a8a519a7131e1214d_2_868x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb21d27d3f6779ac6e5b339a8a519a7131e1214d_2_1158x1000.jpeg 2x" data-dominant-color="907E72"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Imaging axes</span><span class="informations">1770×1528 650 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
Thank you, Ron</li>
</ol>

---

## Post #2 by @Ron (2022-11-03 17:36 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Andras hi, could  ask for your help with the first issue?  I hope to present next week, and it would be very helpful to be able to segment out all the data outside the disc segmentation.  I think there used to be an option to use the segment label to restrict the region of DTI reconstruction. However, I cannot find a way to do so (only option is brain label?).  Happy to share the slicer file.  R</p>

---

## Post #3 by @lassoan (2022-11-03 17:42 UTC)

<aside class="quote no-group" data-username="Ron" data-post="1" data-topic="26040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>I am trying to limit the computation of the DTI data to a masked region</p>
</blockquote>
</aside>
<p>You can use “Mask volume” effect in Segment Editor to blank out voxels of a volume outside the current segment. Would that be sufficient for you?</p>
<aside class="quote no-group" data-username="Ron" data-post="1" data-topic="26040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>How would re-Oriente the imaging planes ( green and yellow) windows to better match the disc anatomical axes</p>
</blockquote>
</aside>
<p>You can use Crop volume module for this. You can enable rotation for the region of interest (by right-clicking on any of its control point and in check “Interaction options” → “Rotate”.</p>

---

## Post #4 by @Ron (2022-11-03 17:43 UTC)

<p>I hope so, I will try this now.   Steve is also looking into this.</p>

---

## Post #5 by @pieper (2022-11-03 17:59 UTC)

<p>Trying to mask a DTI volume with the segment editor led to a crash (maybe not a surprise but still not good).</p>
<p>This method works after exporting the segmentation to a label:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; d = array("Output DTI*e")
&gt;&gt;&gt; m = array("11-9001-pre_load-Segmentation-label")
&gt;&gt;&gt; d[numpy.where(m != 1)] = numpy.zeros([3,3])
</code></pre>
<p>I’ll make new nrrd dti files for you Ron.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/426e655f1e7b2c37ff703611a286c76c0823fcd1.jpeg" alt="image" data-base62-sha1="9tG2bThHRsqjjFZnO1EdfQbm8Vz" width="548" height="456"></p>

---

## Post #6 by @Ron (2022-11-03 18:02 UTC)

<p>Steve  Thanks!!!</p>
<p>Ron Noah Alkalay is inviting you to a scheduled Zoom meeting.</p>
<p>Topic: My Meeting<br>
Time: Nov 3, 2022 02:00 PM Eastern Time (US and Canada)</p>
<p>Join Zoom meeting</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://harvard.zoom.us/j/91785507313?pwd=ZThhc0hoSWpFYkc1WjBraE04OHlLQT09">
  <header class="source">
      <img src="https://harvard.zoom.us/zoom.ico" class="site-icon" width="32" height="32">

      <a href="https://harvard.zoom.us/j/91785507313?pwd=ZThhc0hoSWpFYkc1WjBraE04OHlLQT09" target="_blank" rel="noopener nofollow ugc">Zoom Video</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://harvard.zoom.us/j/91785507313?pwd=ZThhc0hoSWpFYkc1WjBraE04OHlLQT09" target="_blank" rel="noopener nofollow ugc">Join our Cloud HD Video Meeting</a></h3>

  <p>Zoom is the leader in modern enterprise video communications, with an easy, reliable cloud platform for video and audio conferencing, chat, and webinars across mobile, desktop, and room systems. Zoom Rooms is the original software-based conference...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Password: 898459</p>
<p>Join by telephone (use any number to dial in)<br>
+1 312 626 6799<br>
+1 646 931 3860<br>
+1 929 436 2866<br>
+1 301 715 8592<br>
+1 309 205 3325<br>
+1 669 900 6833<br>
+1 689 278 1000<br>
+1 719 359 4580<br>
+1 253 215 8782<br>
+1 346 248 7799<br>
+1 360 209 5623<br>
+1 386 347 5053<br>
+1 507 473 4847<br>
+1 564 217 2000<br>
+1 669 444 9171</p>
<p>International numbers available: <a href="https://harvard.zoom.us/u/adf8DddVEX" class="inline-onebox" rel="noopener nofollow ugc">Zoom International Dial-in Numbers - Zoom</a></p>
<p>One tap mobile: +13126266799,91785507313# US (Chicago)</p>
<p>Join by SIP conference room system<br>
Meeting ID: 917 8550 7313<br>
<a href="mailto:91785507313.898459@zoomcrc.com">91785507313.898459@zoomcrc.com</a></p>
<p>Ron N Alkalay<br>
Associate Professor,<br>
Dept of Orthopedic Surgery, Harvard Medical School<br>
Center for Advanced<br>
Orthopedic Studies<br>
Beth Israel<br>
Deaconess Medical Center<br>
1 Overland Street<br>
Boston, MA, 02215<br>
Tel. 617-667-5185<br>
Fax. 617-667-7175<br>
email:<br>
rn_alkalay@bidmc.harvard.edu</p>

---

## Post #7 by @pieper (2022-11-03 18:38 UTC)

<p>Thanks for your help with this <a class="mention" href="/u/lassoan">@lassoan</a>.  I showed <a class="mention" href="/u/ron">@Ron</a> how to do the numpy approach so he’s set now.</p>

---

## Post #8 by @Ron (2022-11-03 19:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57ef0c39043f20087191876c8ab50c0c1d6a6c87.jpeg" data-download-href="/uploads/short-url/cxTHeEzVEg4ynU08L54rUlI21Rt.jpeg?dl=1" title="Full spine hi-res-oreintation map" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ef0c39043f20087191876c8ab50c0c1d6a6c87_2_690x438.jpeg" alt="Full spine hi-res-oreintation map" data-base62-sha1="cxTHeEzVEg4ynU08L54rUlI21Rt" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ef0c39043f20087191876c8ab50c0c1d6a6c87_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ef0c39043f20087191876c8ab50c0c1d6a6c87_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ef0c39043f20087191876c8ab50c0c1d6a6c87_2_1380x876.jpeg 2x" data-dominant-color="7E8073"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Full spine hi-res-oreintation map</span><span class="informations">1920×1219 433 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
:)!</p>

---
