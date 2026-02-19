---
topic_id: 45987
title: "Changing Precision"
date: 2026-01-29
url: https://discourse.slicer.org/t/45987
---

# Changing precision

**Topic ID**: 45987
**Date**: 2026-01-29
**URL**: https://discourse.slicer.org/t/changing-precision/45987

---

## Post #1 by @dpvaldes (2026-01-29 16:34 UTC)

<p>Is there any way I can change the precision of my voxel signal? Not just for displaying the values but actually changing precision.</p>
<p>I have voxels with very small values (10**(-7)) and I want them rounded to 3 decimals.</p>
<p>I know I can do it through Python code if I transform by whole dicom files but is there any way to do it through the Slicer interface on volumes I have already loaded?</p>

---

## Post #2 by @muratmaga (2026-01-29 17:48 UTC)

<aside class="quote no-group" data-username="dpvaldes" data-post="1" data-topic="45987">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dpvaldes/48/79438_2.png" class="avatar"> dpvaldes:</div>
<blockquote>
<p>I know I can do it through Python code if I transform by whole dicom files but is there any way to do it through the Slicer interface on volumes I have already loaded?</p>
</blockquote>
</aside>
<p>I presume you are talking about image spacing? If so, you can manually edit those values in the Volumes module, and save it (though you will have to resave them as NRRD).</p>
<p>The question is why do you want to do that? You can set the precision field of slicer to 3 significant digits and it will only display the 3 digits, without you having to do this manually. Check out the Units field in the Application Settings and see if does what you want to do.</p>

---

## Post #3 by @dpvaldes (2026-01-29 18:27 UTC)

<p>I’m not talking about spacing. I want to perform other operations were I cannot have 0.0000001 signals that are not physically relevant. Changing the displayed values is of no use for this.</p>
<p>I managed to do something like I this with the ThresholdImageFilter in Simple Filters. Not the same that I want but it works for the post-processing I want to do.</p>

---

## Post #4 by @muratmaga (2026-01-29 19:16 UTC)

<p>If you want to change your intensity values (filter, round, etc), I would use python. Something like this:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume" target="_blank" rel="noopener nofollow ugc">array - Script repository — 3D Slicer  documentation</a></h3>

  <p>Additional options may be specified in properties argument. For example, load an image stack by disabling singleFile option:</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @cpinter (2026-01-30 11:51 UTC)

<p>Not sure if the units settings would help with this (Edit / Application Settings / Units)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31ebba70f36bc4b80a407c7ac7b99b0f9335aae3.png" data-download-href="/uploads/short-url/77CrnpNWSJdJva4m3wNz3DIGyDp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31ebba70f36bc4b80a407c7ac7b99b0f9335aae3.png" alt="image" data-base62-sha1="77CrnpNWSJdJva4m3wNz3DIGyDp" width="690" height="377" data-dominant-color="F2F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×407 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @dpvaldes (2026-01-30 13:15 UTC)

<p>Thank you but that only changes the displayed values, not the actual values.</p>

---

## Post #7 by @cpinter (2026-01-30 13:21 UTC)

<p>OK I didn’t have the time to read the comments carefully. In this case I suggest either use numpy as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggest, or if you prefer not to bother with scripts, I’d use the <code>ShiftScaleImageFilter</code> in the Simple Filters module.</p>

---

## Post #8 by @dpvaldes (2026-01-30 13:29 UTC)

<p>I do a lot of scripting but for this particular case I wanted to see if there was a GUI option, I finally settled with the ThresholdImageFilter.</p>

---
