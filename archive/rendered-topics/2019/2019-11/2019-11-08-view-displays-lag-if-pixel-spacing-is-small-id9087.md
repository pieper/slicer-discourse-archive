---
topic_id: 9087
title: "View Displays Lag If Pixel Spacing Is Small"
date: 2019-11-08
url: https://discourse.slicer.org/t/9087
---

# View displays lag if pixel-spacing is small

**Topic ID**: 9087
**Date**: 2019-11-08
**URL**: https://discourse.slicer.org/t/view-displays-lag-if-pixel-spacing-is-small/9087

---

## Post #1 by @aiden.zhu (2019-11-08 16:22 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0-2019-06-23<br>
Expected behavior: display views normally<br>
Actual behavior: slice-views displays lag.</p>
<p>You see, now I have an image which has a pixel-spacing 15nm (that means, 1.5e-5mm). I load this image to Slicer and it seems fine. But the mouse-scroll to change slices along views does not work (slower than usual, the slice-bar on the top of each view work fine though). So I try to put a fake pixel-spacing value as 1.5mm or even 0.015mm, it works fine to middle-mouse-button-scroll to browse slices along views.</p>
<p>This issue may be reproduced by yourself , trying to use that famous MRHead image, if you set image pixel spacing as 0.001mm, it’s fine. but if you set image pixel spacing as 0.0001 mm, then you try mouse-scrolling where you may see my issue.</p>
<p>The famous MRHead could be load here as:</p>
<p>import SampleData<br>
volumeNode = SampleData.SampleDataLogic().downloadMRHead()</p>

---

## Post #2 by @lassoan (2019-11-08 17:58 UTC)

<p>Regardless of using Slicer for astronomy or microscopy, coordinate values should be in a reasonable range. You may run into various issues if you use coordinate values that are extremely large or extremely small.</p>
<p>Do not rescale your image if your problem is that the displayed unit is incorrect. Instead, change units in application settings / units section. Since units are rarely changed from the default, it may go unnoticed if usage of mm is hardcoded at some places. If you encounter such cases then let us know (if they are easy to fix then we may fix it, if not then we may ask for your help).</p>

---

## Post #3 by @aiden.zhu (2019-11-08 18:37 UTC)

<p>Thanks a lot, Andras.</p>
<p>I may try to set up units for some certain images, but it is really NOT that convenient while we have images with pixel-spacing values ranging from 10mm to 15nm.</p>
<p>From a view of a scientist, pixel-spacing values should NOT bring such issues since a value is a value, a float is a float. Anyway, if you guys may solve this issue, that will be a big help and this also helps more applicable in a widely expanded range of industries.</p>
<p>Best,<br>
Aiden</p>

---

## Post #4 by @muratmaga (2019-11-08 18:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, I tried and think the lag is no much due to change in the units, but simply the slider has only 0.001 mm increments, so slices do not get changed until the units incremented more than 0.001 mm (which will take 10 slices in this scenario). We will encounter small voxel data more and more through SlicerMorph. I wonder if it possible to tie the precision of the slice views (current seems only three significant digits), to image precision of the volume being displayed?</p>

---

## Post #5 by @pieper (2019-11-08 19:02 UTC)

<p>Definitely, there’s a lot of room for improving support for different units and spacings, and supporting more than 3 digits makes sense.</p>
<p>One thing to keep in mind is that it’s not just a notation thing, the stability and even accuracy of a lot of floating point computations depends a lot on the range of values, so it’s good to avoid extremely large or small values and rather change the units.</p>

---

## Post #6 by @lassoan (2019-11-08 19:14 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="9087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I tried and think the lag is no much due to change in the units, but simply the slider has only 0.001 mm increments, so slices do not get changed until the units incremented more than 0.001 mm</p>
</blockquote>
</aside>
<p>Precision of that slider can already be set in Application settings / Units.</p>
<p>Units may not be respected everywhere right now, but probably should be fixable without too much effort in many places.</p>
<p>There are a few cases where some design changes would be needed. For example: The ruler, uses multiple units (not just mm but cm, etc.) to keep numbers easy to read. We should also ensure that units received from external sources are respected/converted (e.g., if a DICOM volume is loaded and application length unit is micrometer then spacing values should be converted accordingly).</p>

---

## Post #7 by @muratmaga (2019-11-08 19:18 UTC)

<p>True. I set it to 8 digits for length and it does display the full precision.</p>
<p>But still slices only updated if the increments is multiple of 0.001 (i.e., it doesn’t matter how many significant digits it display for the functionality).</p>

---

## Post #8 by @lassoan (2019-11-08 19:23 UTC)

<p>This is one of the things that is probably fixable without any design changes (most likely cause by some unnecessary assumption in the slider widget).</p>

---

## Post #9 by @lassoan (2019-11-08 20:21 UTC)

<aside class="quote no-group" data-username="aiden.zhu" data-post="3" data-topic="9087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> aiden.zhu:</div>
<blockquote>
<p>From a view of a scientist, pixel-spacing values should NOT bring such issues since a value is a value, a float is a float.</p>
</blockquote>
</aside>
<p>If you use computers, it is important to understand the limitation of floating-point number representation. For example, regardless of what software do you use, if you have a small number, add a large number to it, subtract the same large number, then the result will be 0 (not the original small number). These kind of errors would happen all the time if you attempted to process images together that have vastly different scale.</p>
<p>You can have a look at this <a href="https://www.phys.uconn.edu/~rozman/Courses/P2200_15F/downloads/floating-point-guide-2015-10-15.pdf">document</a> describing some of the common issues.</p>
<p>Even if length scale difference between two data sets is “just” 6 magnitudes (mm/nm), it means that volume scale difference would be 18 magnitudes away. For example, if you compute the volume of a structure in the small image and volume of another structure in the large image then you can store the results in two separate floating-point variables (v1 and v2), but you cannot store the sum of these volumes (v1+v2) in one floating-point variable.</p>

---

## Post #10 by @aiden.zhu (2019-11-08 21:42 UTC)

<p>Thanks a lot for the considerate and detailed explanation, Andras. I understand your point there due to the scale difference.</p>
<p>I double-checked the instruction here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_up_custom_units_in_slice_view_ruler" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_up_custom_units_in_slice_view_ruler</a><br>
where there are two steps:  1. change the unit in Application settings / Units and 2. update ruler display settings using the script below (it can be copied to your Application startup script)</p>
<p>So my question is: is there a way to access “application settings/Units” via python? so that I may try to do python coding to change units based on my different-scaled images.<br>
Thanks!</p>
<p>Best,<br>
Aiden</p>

---

## Post #11 by @lassoan (2019-11-09 00:51 UTC)

<p>Yes, units can be customized in Python, as units information is stored in nodes in the scene.</p>

---
