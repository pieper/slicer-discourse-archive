---
topic_id: 26671
title: "Seeking Help On Fish Bone Density Measurement"
date: 2022-12-10
url: https://discourse.slicer.org/t/26671
---

# Seeking help on fish bone density measurement

**Topic ID**: 26671
**Date**: 2022-12-10
**URL**: https://discourse.slicer.org/t/seeking-help-on-fish-bone-density-measurement/26671

---

## Post #1 by @tinacai (2022-12-10 02:38 UTC)

<p>Hello 3D Slicer Community,</p>
<p>I am a new user of 3D Slicer and am trying to measure bone density of fish across species, I am wondering if any one has any suggestion of resources that I could look into as a starting point to learn about how to do the measurement and using the software in general?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2022-12-10 07:18 UTC)

<p>You should have everything you would need to calculate bone density in Slicer. However, be warned that proper bone density calculation requires scans in which intensity values are calibrated using known phantoms.</p>
<p>If your scan and image reconstruction protocol are identical across your samples, you might be able to calculate relative bone density (aka bone volume fraction), which is basically the ratio number of voxels designated as bone (e.g., after thresholding) to the total number of voxels in the region. The higher the number, the denser the bone is (ratio of 1 indicating no porosity).</p>
<p>The rest is having a protocol that allows you to define your regions/volume of interest consistently across your samples. This might be harder than you think in multi-species samples.</p>

---

## Post #3 by @tinacai (2022-12-10 07:22 UTC)

<p>Thank you so much for this advice! Is there possibly any resource that I could use to learn the appropriate protocols?</p>

---

## Post #4 by @muratmaga (2022-12-10 07:25 UTC)

<p>I do not know of a resource, but there was a related discussion in this thread. <a href="https://discourse.slicer.org/t/bone-mineral-density-bmd-measurement-method/11010/3" class="inline-onebox">Bone Mineral Density (BMD) measurement method - #3 by manjula</a></p>
<p>you may want to ask <a class="mention" href="/u/manjula">@manjula</a> if he has a protocol that he can share?</p>

---

## Post #5 by @manjula (2022-12-14 14:56 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="26671">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>do</p>
</blockquote>
</aside>
<p>Sorry for the delayed reply.<br>
Basically we used this manual and article to do the BMD calculation. We can replicate the workflow here in 3D Slicer.</p>
<aside class="onebox pdf" data-onebox-src="https://medicine.temple.edu/sites/medicine/files/files/ct_analyzer.pdf">
  <header class="source">

      <a href="https://medicine.temple.edu/sites/medicine/files/files/ct_analyzer.pdf" target="_blank" rel="noopener nofollow ugc">medicine.temple.edu</a>
  </header>

  <article class="onebox-body">
    <a href="https://medicine.temple.edu/sites/medicine/files/files/ct_analyzer.pdf" target="_blank" rel="noopener nofollow ugc"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://medicine.temple.edu/sites/medicine/files/files/ct_analyzer.pdf" target="_blank" rel="noopener nofollow ugc">ct_analyzer.pdf</a></h3>

  <p class="filesize">1806.15 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><a href="https://drive.google.com/file/d/137C5JtcJFodOsrCLkQRugvhuIGvNLXDW/view?usp=share_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/137C5JtcJFodOsrCLkQRugvhuIGvNLXDW/view?usp=share_link</a></p>
<p>We did calculated the BMD using microCT(calibrated)  (U-CT, MILabs)</p>
<ol>
<li>Do the MicroCT scan of the standard phantoms (calibration rods )</li>
<li>Do your sample scans</li>
<li>calculated the HU values using the segment stattistics module after segmenting the ROI</li>
<li>Using the HU values of the phantoms did the linear regressiion</li>
</ol>
<p>Afterwards using the linear regression formula you can obtain the BMD of the samples/ROI</p>
<p>Thank you.</p>

---

## Post #6 by @Joseph_L (2023-10-27 00:40 UTC)

<p>Manjula, are you able to resend the google drive link? It has expired or is broken</p>

---
