---
topic_id: 48443
title: "AI driven upper airway analysis"
date: 2026-10-08
url: https://discourse.slicer.org/t/48443
last_bumped: 2026-10-09T14:25:36.144Z
---

# AI driven upper airway analysis

**Topic ID**: 48443
**Date**: 2026-10-08
**URL**: https://discourse.slicer.org/t/ai-driven-upper-airway-analysis/48443

---

## Post #1 by @Algiz (2026-10-08 15:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87adb61abdb75ea3bc1ea519379798e8ed684442.jpeg" data-download-href="/uploads/short-url/jmgDgBvH1BKRhRjQfiod028mDvk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87adb61abdb75ea3bc1ea519379798e8ed684442_2_690x496.jpeg" alt="image" data-base62-sha1="jmgDgBvH1BKRhRjQfiod028mDvk" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87adb61abdb75ea3bc1ea519379798e8ed684442_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87adb61abdb75ea3bc1ea519379798e8ed684442_2_1035x744.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87adb61abdb75ea3bc1ea519379798e8ed684442.jpeg 2x" data-dominant-color="CBC6B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1317×948 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello! I am trying to analyze my own cbct scan using 3d slicer and it is a very interesting program. some extensions have already helped me segment the airway and do a rudimentary airway analysis to determine the narrowest points but this only followe a line set between points within the model and the data spreads and graphs are confusing and questionable.</p>
<p>I did use blueskyplan which allowed me to easily segment my whole skull but it sadly seems to not have a dedicated option like this.</p>
<p>Could anyone who is better at this maybe make a function that automatically does an analysis like in the image on a segmented airway? Would be cool if you could also do it for the nasal cavity or both the nose and throat together.</p>
<p>Sadly all these programs that can do these features are locked behind a paywall or you being a medical provider.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @mau_igna_06 (2026-10-08 22:55 UTC)

<p>For the airway you should be able to use vmtk, check out its Slicer extension. I think the analysis you want to do is similar to what is done using vmtk for aorta</p>

---

## Post #3 by @Algiz (2026-10-09 14:25 UTC)

<p>I did use vmtk, although I had a lot of trouble shooting before I got it to work. I found that I didn’t get a clean representation since it’s only a line that I can color code between the marked points of the analysis.</p>

---
