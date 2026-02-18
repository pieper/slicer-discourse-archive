# Gel Dosimetry Slicelet - Calibration

**Topic ID**: 15739
**Date**: 2021-01-29
**URL**: https://discourse.slicer.org/t/gel-dosimetry-slicelet-calibration/15739

---

## Post #1 by @SmHoop (2021-01-29 16:15 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>Hi,</p>
<p>In the calibration step of the slicelet (from the Wiki) I see step 10:</p>
<ol start="10">
<li>Get mean optical densities from the central cylinder of the CALIBRATION volume</li>
</ol>
<p>Must a MeV irradiation be performed down the central axis of a jar to compare with databook/commissioning PDD values imported, or can a lateral irradiation be used? Can a MV irradiation be used, or does it require the entire range as an MeV would provide? I’m assuming it relies on the typical axial view being down the length of the jar to determine this?</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2021-01-29 16:22 UTC)

<p>The Gel Dosimetry application has a fixed workflow, so you must follow that. See details here</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/WC2015_Gel_slicelet_tutorial.pdf">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/WC2015_Gel_slicelet_tutorial.pdf" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/WC2015_Gel_slicelet_tutorial.pdf" target="_blank" rel="noopener">SlicerRt/SlicerRtDoc/blob/master/tutorials/WC2015_Gel_slicelet_tutorial.pdf</a></h4>


  This file is binary. <a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/WC2015_Gel_slicelet_tutorial.pdf" target="_blank" rel="noopener">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="SmHoop" data-post="1" data-topic="15739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f6c823/48.png" class="avatar"> SmHoop:</div>
<blockquote>
<p>Must a MeV irradiation be performed down the central axis of a jar to compare with databook/commissioning PDD values imported</p>
</blockquote>
</aside>
<p>Yes</p>
<aside class="quote no-group" data-username="SmHoop" data-post="1" data-topic="15739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f6c823/48.png" class="avatar"> SmHoop:</div>
<blockquote>
<p>Can a MV irradiation be used</p>
</blockquote>
</aside>
<p>You need to use the very same type of beam for calibration and treatment evaluation.</p>
<p><a class="mention" href="/u/kmalexander">@kmalexander</a> please confirm if you have a minute.</p>

---

## Post #3 by @kmalexander (2021-01-29 16:51 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/smhoop">@SmHoop</a> The reason we use an electron beam calibration is that it produces the greatest range of dose values within the length of our gel jar.  You can certainly try using a 6 MV photon beam for calibration.  What size jar are you using?  If you’re using the comparable 1L jars as we do (around 15 cm tall), your dose values for calibration will be limited from PDD100% to roughly PDD60%.  Do note:  The automatic scaling and shifting of the curves will likely not produce a very good match, since you’re in essence lining up two straight lines.  I’d encourage you to think about placing some sort of optical marker at a known depth so that you can see the spike in your PDD and can align that to the known depth.   Hope this helps a bit!</p>

---

## Post #4 by @SmHoop (2021-01-29 17:33 UTC)

<p>Yes thank you both, this is very helpful information. I think for this data set the best course is to find the manual calibration coefficients. Future experiments will have to be set-up much more carefully to be inline with the workflow. I did achieve a 94.76% gamma match at 3%3mm using a CAX MV irradiation as the calibration, used on a lateral MV irradiation (matched with Eclipse plan), but that hasn’t worked for anything else so far.</p>

---

## Post #5 by @SmHoop (2021-02-04 17:47 UTC)

<p><a class="mention" href="/u/kmalexander">@kmalexander</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>Quick follow-up if you have time!</p>
<p>I’ve manually determined a calibration fit in Matlab by taking a 1 cm (for noise) cylinder down the center of the MeV irradiation and determining the median value of each slice down the length. (This image shows the curve overlaid on the dose profile taken from the Eclipse plan, not showing the alignment tweaks to find the range of best fit)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60b851fba70ed8bdfc733cc984b9fcf5ed95fa23.png" data-download-href="/uploads/short-url/dNCJYcSyjqRjElse3nqDlAteJV1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b851fba70ed8bdfc733cc984b9fcf5ed95fa23_2_276x500.png" alt="image" data-base62-sha1="dNCJYcSyjqRjElse3nqDlAteJV1" width="276" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b851fba70ed8bdfc733cc984b9fcf5ed95fa23_2_276x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b851fba70ed8bdfc733cc984b9fcf5ed95fa23_2_414x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60b851fba70ed8bdfc733cc984b9fcf5ed95fa23.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">464×839 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I register the dosimeter in Slicer and apply these manual coefficients it blows up the dosimeter to values of basically the first coefficient, as seen in this picture below (Calibrated overlaid on Eclipse Dose, with value in Data probe on bottom left):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/351bc8db43b36cf9f46b4b13b77a64e6c3464cb6.png" data-download-href="/uploads/short-url/7zOPIuCWlsLReI1fyANayLVVit0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351bc8db43b36cf9f46b4b13b77a64e6c3464cb6_2_462x500.png" alt="image" data-base62-sha1="7zOPIuCWlsLReI1fyANayLVVit0" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351bc8db43b36cf9f46b4b13b77a64e6c3464cb6_2_462x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351bc8db43b36cf9f46b4b13b77a64e6c3464cb6_2_693x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/351bc8db43b36cf9f46b4b13b77a64e6c3464cb6.png 2x" data-dominant-color="CED2CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×888 46.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I use these values to scale the attenuation coefficients in Matlab I see a reasonable fit (unsurprisingly given the linear fit).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eccc6f67c91c7419741dc87ba91e40e2e9566e7.png" data-download-href="/uploads/short-url/6G0HcmEUrPCyKe9TMpED3iB8qTt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eccc6f67c91c7419741dc87ba91e40e2e9566e7.png" alt="image" data-base62-sha1="6G0HcmEUrPCyKe9TMpED3iB8qTt" width="553" height="500" data-dominant-color="F4F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">563×509 17.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any ideas on why Slicer is having a hard time with this? Thank you!</p>

---

## Post #6 by @SmHoop (2021-02-07 19:57 UTC)

<p>I just realized the manual dose calibration in Gel Dosimetry is y = b + mx, not y = mx+b, in the input order. That solved my issue.</p>

---
