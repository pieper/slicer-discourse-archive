---
topic_id: 28052
title: "How To Normalize The Intensity"
date: 2023-02-26
url: https://discourse.slicer.org/t/28052
---

# How to normalize the intensity?

**Topic ID**: 28052
**Date**: 2023-02-26
**URL**: https://discourse.slicer.org/t/how-to-normalize-the-intensity/28052

---

## Post #1 by @Floren (2023-02-26 10:05 UTC)

<p>Hello, everyone!</p>
<p>I am working with prostate adc maps and trying to measure adc value for prostate tumors in order to demonstrate that there is a correlation between adc value and Gleason score.</p>
<p>I understood that i must first normalize the intensity of the images. The problem is that i don’t really know how to do that.</p>
<p>I appreciate any information you may have.</p>

---

## Post #2 by @Young_Wang (2023-02-27 19:05 UTC)

<p><a class="mention" href="/u/floren">@Floren</a> The way I typically do it, not sure if it’s the best way</p>
<ol>
<li>module finder</li>
<li>simple filter</li>
<li>rescaleIntensityImageFilter<br>
I suggest you make a clone of your volume first, and then output into a different volume so you still have a copy of the original.</li>
</ol>

---
