---
topic_id: 1748
title: "Comparing The Differences Between Two Slices Quantitatively"
date: 2017-12-30
url: https://discourse.slicer.org/t/1748
---

# Comparing the differences between two slices quantitatively 

**Topic ID**: 1748
**Date**: 2017-12-30
**URL**: https://discourse.slicer.org/t/comparing-the-differences-between-two-slices-quantitatively/1748

---

## Post #1 by @Ishan_Perera (2017-12-30 22:57 UTC)

<p>Operating system: MacOS High Sierra 10.13.1<br>
Slicer version: 4.7.0-2017-09-21 r26391 (I can upgrade/downgrade if need be)<br>
Expected behavior: Quantitative comparison of slices<br>
Actual behavior: N/A</p>
<p>I have been tasked with creating images that show the least amount of difference between two images (if possible around a specific area of the images). I am unsure of which module/filter to use in order to easily get quantitative data about the differences!</p>
<p>Please Help!</p>
<p>Thank you,<br>
Ishan</p>

---

## Post #2 by @lassoan (2017-12-31 02:10 UTC)

<p>What kind of images you need to compare? Would you like to subtract the images from each other or just visually compare them side-by-side?</p>
<p>For visual comparison, it is probably enough to just set the same window/level values for both volumes in Volumes module.</p>
<p>If you need to subtract the images then probably spatially alignment would improve image quality a lot. You can register images using <code>General registration (BRAINS)</code> or <code>General registration (Elastix)</code> modules (for the latter you need to install SlicerElastix extension).</p>

---

## Post #3 by @Ishan_Perera (2017-12-31 19:12 UTC)

<p>I am comparing MRI scans, I have conducted visual comparisons by overlapping them and allowing them to show 50/50, but I think the subtraction method would be more of what I am looking for. I will try the methods you have introduced and see if they work!</p>
<p>Thank you and Happy New Years!</p>

---

## Post #4 by @pieper (2018-01-01 00:26 UTC)

<p>Also you can just subtract the two volumes and look at the resulting volume:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/SubtractScalarVolumes" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/SubtractScalarVolumes</a></p>
<p>HTH,<br>
Steve</p>

---

## Post #5 by @kalaiselvi (2018-01-01 02:28 UTC)

<p>Dice coefficient  is an efficient similarity comparison measure among<br>
images.</p>

---
