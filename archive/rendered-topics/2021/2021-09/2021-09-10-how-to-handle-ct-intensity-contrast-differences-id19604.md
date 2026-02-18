# How to handle CT intensity / contrast differences

**Topic ID**: 19604
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/how-to-handle-ct-intensity-contrast-differences/19604

---

## Post #1 by @rbumm (2021-09-10 09:35 UTC)

<p>In the COVID-19 open-source dataset of <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> some CTs have a large variation in terms of brightness, intensity, and contrast.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5695ab3efb6e249273e44f69e64425bd2efdbd6b.jpeg" data-download-href="/uploads/short-url/clXJ3hQJovNtbyLUNzDvysBTFUv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5695ab3efb6e249273e44f69e64425bd2efdbd6b_2_550x500.jpeg" alt="image" data-base62-sha1="clXJ3hQJovNtbyLUNzDvysBTFUv" width="550" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5695ab3efb6e249273e44f69e64425bd2efdbd6b_2_550x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5695ab3efb6e249273e44f69e64425bd2efdbd6b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5695ab3efb6e249273e44f69e64425bd2efdbd6b.jpeg 2x" data-dominant-color="86858C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">759×690 80.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Up: weak contrast<br>
Lower: better contrast</p>
<p>I need to do extensive window leveling work to achieve an acceptable display.<br>
How do you guys handle this kind of problem? Is there a trick, maybe script,  to get a good initial brightness and contrast (lung window)  in all CT?</p>

---

## Post #2 by @rbumm (2021-09-10 09:38 UTC)

<p>In astrophotography (fits images) I would “stretch” each image / channel to archieve a similar histogram.</p>

---

## Post #3 by @pieper (2021-09-10 11:32 UTC)

<p>Probably you just need to set the same window level.  Easiest is to use one of the presets in the Volumes module - right click on the volume in the Data module and pick Edit properties then click the lung preset.  For dicom we use the window/level from the header (usually set by the radiographer) but for non-dicom there’s a formula which depends on the values in the data, which can vary.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35d93170990bcc87f0345c7dfb007ea6b4494b87.png" alt="image" data-base62-sha1="7GmDGnpUwJMonddm1Rw3sZY3BuD" width="410" height="228"></p>

---

## Post #4 by @rbumm (2021-09-10 13:44 UTC)

<p>Excellent, that works.</p>

---

## Post #5 by @lassoan (2021-09-11 00:42 UTC)

<p>See some more information on how to adjust window/level:</p>
<aside class="quote quote-modified" data-post="1" data-topic="7284">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284">Recent improvements in window/level management</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is a quick summary of image window/level (brightness/contrast) adjustment changes introduced in recent Slicer Preview (formerly known as “Nightly”) releases. 

Improved automatic window/level algorithm

Images that do not contain preferred window/level information are displayed with automatically computed values. The complex automatic computation algorithm that had been used in Slicer worked marginally better for some images, but sometimes generated too bright images and overall the results…
  </blockquote>
</aside>

<p>I’ve fixed the DICOM import plugin now to <a href="https://github.com/Slicer/Slicer/issues/5140">use the middle slice’s window/level instead of the first file’s</a>. <a class="mention" href="/u/rbumm">@rbumm</a> It would be great if you could test the Slicer Preview Release tomorrow if the default window/level setting works better.</p>

---

## Post #6 by @rbumm (2021-09-11 10:38 UTC)

<p>Unfortunately, today’s preview Slicer 4.13.0-2021-09-10 does not start correctly on Windows (it shows just the initial splash screen, no further action).</p>

---

## Post #7 by @rbumm (2021-09-11 11:05 UTC)

<p>The only way I got 4.13.0-2021-09-10 starting was to redirect stderr or stdout in powershell command line.</p>
<pre><code class="lang-auto">./Slicer.exe &gt;&gt; err.txt
</code></pre>
<p>The default window level for the problematic CT (Pat 27 of the public COV dataset) was the same, too bright.<br>
When I switched to the “Volumes” module slicer crashed.</p>

---

## Post #8 by @lassoan (2021-09-11 19:30 UTC)

<p>Thanks for reporting the startup failure/crash, it’s probably due to my changes that I made yesterday in an attempt to improve console output on Windows. I’ll fix it today.</p>
<p>Can you check in the DICOM browser what window width &amp; center values are stored in the files? (right-click on the series and choose View metadata to see the DICOM fields)</p>

---

## Post #9 by @rbumm (2021-09-11 20:52 UTC)

<p>The open source COV CTs all come as nrrd datasets so they are not in the DICOM database and I can not easily extract the metadata. Pls tell me if you want me to check/do anything else.</p>

---

## Post #10 by @lassoan (2021-09-12 18:28 UTC)

<p>I see, there is nothing further to test then. I don’t think nrrd files can store the recommended window/level setting, so for those files the window/level setting is determined automatically (by using a range between the 0.1 and 99.9 percentiles of the intensity histogram).</p>

---

## Post #11 by @rbumm (2021-09-12 19:38 UTC)

<p>The features of “Volumes” enable a good selection of presets.<br>
BTW today´s version of the preview release starts up well and “Volumes” does not crash it.</p>

---
