---
topic_id: 43723
title: "How To Measure The Perimeter Of Slices From A Full Body 3D M"
date: 2025-07-15
url: https://discourse.slicer.org/t/43723
---

# How to Measure the Perimeter of Slices from a Full-Body 3D Model

**Topic ID**: 43723
**Date**: 2025-07-15
**URL**: https://discourse.slicer.org/t/how-to-measure-the-perimeter-of-slices-from-a-full-body-3d-model/43723

---

## Post #1 by @yoshi (2025-07-15 04:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0b4bae06d61e4cdb90c5c20b21a52c52c378165.jpeg" data-download-href="/uploads/short-url/ruKSXQIwLnIPfTgq2wduNyMfGlv.jpeg?dl=1" title="2025-07-14 195342" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0b4bae06d61e4cdb90c5c20b21a52c52c378165_2_690x463.jpeg" alt="2025-07-14 195342" data-base62-sha1="ruKSXQIwLnIPfTgq2wduNyMfGlv" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0b4bae06d61e4cdb90c5c20b21a52c52c378165_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0b4bae06d61e4cdb90c5c20b21a52c52c378165_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0b4bae06d61e4cdb90c5c20b21a52c52c378165.jpeg 2x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-07-14 195342</span><span class="informations">1327×891 72.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi everyone,</p>
<p>I’m new to 3D Slicer. I have a full-body 3D STL model and would like to display slice images at arbitrary positions (see attached picture) and obtain both the perimeter and area of each slice.</p>
<p>I’ve found that if I manually draw a closed curve, Slicer will show the perimeter, but is there a way to have Slicer automatically extract the contour and measure the perimeter (and area) for me?</p>
<p>Thanks in advance for any guidance!</p>

---

## Post #2 by @lassoan (2025-07-15 04:32 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> Can any of your modules in VMTK extension compute perimeter of the cross-section (or could be easily added)?</p>

---

## Post #3 by @chir.set (2025-07-15 07:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="43723">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can any of your modules in VMTK extension compute perimeter of the cross-section (or could be easily added)?</p>
</blockquote>
</aside>
<p>No, the perimeter of a cross-section was not a goal.</p>
<p>However, it should be scriptable fairly easily using <a href="https://discourse.slicer.org/t/vmtk-cross-sectional-perimeter-calculation/37747/3">vtkvmtkPolyDataBoundaryExtractor</a>.</p>
<p>It would mean pulling in the VMTK libraries. StenosisMeasurement2D would be the elect module to add this functionality, as <a class="mention" href="/u/yoshi">@yoshi</a> can get both the area and the perimeter. But then, how to integrate this calculation in the module, since it does not fit in the <code>spirit</code> of the module?</p>
<p>An independent script still using VMTK is also an option.</p>
<p>The last option would be to consider the cell ids: investigate their neighbourhood relationship, so as not to require VMTK. I may start delving into that in the coming days.</p>
<p>What’s your opinion about these options?</p>

---

## Post #4 by @yoshi (2025-07-15 08:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you for your support.<br>
<a class="mention" href="/u/chir.set">@chir.set</a><br>
I saw your reply here: <a href="https://discourse.slicer.org/t/vmtk-cross-sectional-perimeter-calculation/37747/4" class="inline-onebox">VMTK - cross-sectional perimeter calculation - #4 by chir.set</a><br>
It seems to describe exactly what I’m looking for.</p>
<p>For example, if I want to get the area and perimeter of the slice shown in the Red window, and the slice intersects both legs, two cross-sections are displayed.<br>
Even if multiple cross-sections are present, I would like to obtain the area and perimeter for each one as separate closed curves.</p>
<p>I’m not sure what would be the best way to implement this, but if we could select the slice view (e.g., Red, Green, Yellow), run the calculation, and have the area and perimeter results appear in a table, it would be very useful for anatomical measurements.</p>
<p>Thank you again for your support.</p>

---

## Post #5 by @chir.set (2025-07-28 14:03 UTC)

<p><a class="mention" href="/u/yoshi">@yoshi</a></p>
<p>You may consider this <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/Perimeters/" rel="noopener nofollow ugc">module</a> that does what you wish.</p>
<p>I considered that it may be useful in clinical practice, for example, to measure/follow</p>
<ul>
<li>the abdominal perimeter in bariatric surgery</li>
<li>the leg perimeter in deep veinous thrombosis</li>
<li>…</li>
</ul>

---

## Post #6 by @yoshi (2025-07-31 10:26 UTC)

<p>Sorry for the late reply.<br>
Thank you very much for creating the module!<br>
I will try it out right away.<br>
As you mentioned, I believe it will be useful for analyzing obesity and similar cases.<br>
Just wanted to express my gratitude first.</p>

---

## Post #7 by @yoshi (2025-08-15 05:07 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a><br>
I have installed it and tried various things. It was able to measure just as I expected.<br>
Thank you very much for creating the module.<br>
<a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you for your support.</p>

---
