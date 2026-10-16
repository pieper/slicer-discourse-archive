---
topic_id: 48443
title: "AI driven upper airway analysis"
date: 2026-10-08
url: https://discourse.slicer.org/t/48443
last_bumped: 2026-10-15T15:55:12.064Z
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

## Post #4 by @mikebind (2026-10-15 15:55 UTC)

<p>The image in your post above looks sort of like they just took a centerline value and used it to color the airway surface points (there doesn’t seem to be any circumferential variation in color).  I don’t know of any existing automated way to transfer the centerline-associated associated values to model surface points, but it seems conceptually fairly straightforward, and you could probably have an LLM successfully guide you through it.  Here is how I would probably approach it:</p>
<ol>
<li>Export your airway segment to a surface model node.</li>
<li>For each point on your surface model’s polydata:
<ol>
<li>Find the closest point on your centerline curve</li>
<li>Get the associated stored maximum inscribed radius or diameter associated with that centerline point from the vmtk analysis</li>
<li>Store that value as a scalar associated with the model point</li>
</ol>
</li>
<li>In the surface model node’s display settings (Models module =&gt; Display =&gt; Scalars):
<ol>
<li>Check the “Visibility” box to turn on scalar display</li>
<li>Choose the name of the scalar where you stored the radius or diameter value as the “Active Scalar”</li>
<li>Choose a color map and data range to control how the colors map to the stored values</li>
</ol>
</li>
</ol>
<p>I think this should work well, and is hopefully not too difficult to implement. Good luck!</p>

---
