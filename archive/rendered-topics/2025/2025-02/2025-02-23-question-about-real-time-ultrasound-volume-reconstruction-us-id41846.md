---
topic_id: 41846
title: "Question About Real Time Ultrasound Volume Reconstruction Us"
date: 2025-02-23
url: https://discourse.slicer.org/t/41846
---

# Question about Real-time Ultrasound Volume Reconstruction using SteamVR Tracker

**Topic ID**: 41846
**Date**: 2025-02-23
**URL**: https://discourse.slicer.org/t/question-about-real-time-ultrasound-volume-reconstruction-using-steamvr-tracker/41846

---

## Post #1 by @MasatoshiOBA (2025-02-23 10:42 UTC)

<h3><a name="p-122815-question-1" class="anchor" href="#p-122815-question-1" aria-label="Heading link"></a><strong>Question:</strong></h3>
<h4><a name="p-122815-overview-2" class="anchor" href="#p-122815-overview-2" aria-label="Heading link"></a><strong>Overview:</strong></h4>
<p>I am planning to perform <strong>ultrasound volume reconstruction</strong> using a SteamVR-compatible tracker.<br>
Currently, I have successfully used <code>pyigtl</code> to send tracking data to Slicer, and Slicer receives it as a <code>Transform node</code>.</p>
<hr>
<h3><a name="p-122815-problems-i-want-to-solve-3" class="anchor" href="#p-122815-problems-i-want-to-solve-3" aria-label="Heading link"></a><strong>Problems I want to solve:</strong></h3>
<h4><a name="p-122815-h-1-issue-with-volume-reslice-driver-settings-4" class="anchor" href="#p-122815-h-1-issue-with-volume-reslice-driver-settings-4" aria-label="Heading link"></a><strong>(1) Issue with Volume Reslice Driver Settings</strong></h4>
<ul>
<li>I set the <code>Red slice driver</code> of the <code>Volume Reslice Driver</code> to the transform node from the tracker (<code>Tracker_reference</code>) and set the mode to <code>"Transverse"</code>. However, only a single line appears on the screen.</li>
<li>On the other hand, if I apply the <code>Tracker_reference</code> <strong>directly to the Image</strong>, the image is displayed (see the attached screenshot).</li>
<li>In various <strong>real-time ultrasound reconstruction tutorials</strong>, I did not find any mention of needing to apply the transform to the <code>Image</code> itself.</li>
<li><strong>Is this procedure correct?</strong><br>
If it is incorrect, could you please advise on the correct way to configure it?</li>
</ul>
<h4><a name="p-122815-h-2-changing-the-reference-point-of-the-transform-5" class="anchor" href="#p-122815-h-2-changing-the-reference-point-of-the-transform-5" aria-label="Heading link"></a><strong>(2) Changing the Reference Point of the Transform</strong></h4>
<ul>
<li>As shown in the attached image, when I apply the tracker-derived <code>Transform node (Tracker_reference)</code>, the <strong>origin (0,0,0) of the transform node is aligned with Slicer’s global origin</strong>.</li>
<li>However, I would like the <strong>center of the transform to be the center of the ultrasound probe</strong> (the second tracker center position in the image).</li>
<li><strong>Is it possible to shift the reference point of the transform?</strong><br>
If so, how can I achieve this?</li>
</ul>
<hr>
<h3><a name="p-122815-things-i-have-tried-6" class="anchor" href="#p-122815-things-i-have-tried-6" aria-label="Heading link"></a><strong>Things I have tried:</strong></h3>
<p>I attempted to nest the transform nodes in the following structure:</p>
<p>pgsql</p>
<p>コピーする編集する</p>
<pre><code class="lang-auto">Tracker_reference
|
|_ Transform_0 (A transform to move Tracker_reference to the upper center of the Image, which is intended to represent the center of the probe)
   |
   |_ Image (The volume I want to manipulate)
</code></pre>
<p>However, even with this setup, when I activate the <code>Volume Reslice Driver</code>, <strong>Tracker_reference still behaves as if its reference point is at the lower left center of the screen</strong>, which is not the intended behavior.</p>
<hr>
<h3><a name="p-122815-environment-information-7" class="anchor" href="#p-122815-environment-information-7" aria-label="Heading link"></a><strong>Environment Information:</strong></h3>
<ul>
<li><strong>Slicer Version:</strong> 5.8.0</li>
<li><strong>Extensions Used:</strong> OpenIGTLink, SlicerIGT, etc.</li>
<li><strong>OpenIGTLink / pyigtl Version:</strong> (if applicable, please specify)</li>
<li><strong>Tutorials or References Used:</strong> (if applicable, please provide links)</li>
<li><strong>Other Settings or Attempts:</strong> As described above</li>
</ul>
<p>I truly appreciate your time in reading my post and any insights or advice you can provide.<br>
Your expertise and support mean a lot, and I am grateful for this amazing community that makes learning and problem-solving so much easier.</p>
<p>Thank you in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acf895548fa2a06b42b9a5533f94455a18408421.jpeg" data-download-href="/uploads/short-url/oGaI9NJezM1BZvt8ZixtZL6Rk9b.jpeg?dl=1" title="transform" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acf895548fa2a06b42b9a5533f94455a18408421_2_690x365.jpeg" alt="transform" data-base62-sha1="oGaI9NJezM1BZvt8ZixtZL6Rk9b" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acf895548fa2a06b42b9a5533f94455a18408421_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acf895548fa2a06b42b9a5533f94455a18408421_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acf895548fa2a06b42b9a5533f94455a18408421_2_1380x730.jpeg 2x" data-dominant-color="717075"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">transform</span><span class="informations">1885×999 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
