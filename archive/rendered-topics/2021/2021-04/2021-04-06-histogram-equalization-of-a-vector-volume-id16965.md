---
topic_id: 16965
title: "Histogram Equalization Of A Vector Volume"
date: 2021-04-06
url: https://discourse.slicer.org/t/16965
---

# Histogram equalization of a vector volume

**Topic ID**: 16965
**Date**: 2021-04-06
**URL**: https://discourse.slicer.org/t/histogram-equalization-of-a-vector-volume/16965

---

## Post #1 by @giovform (2021-04-06 15:11 UTC)

<p>Hi, is there a way to apply a histogram equalization on vector volumes just for display purposes? I wrote a code that performs it, but by altering the data array directly, and saving the original result when the user decides to “turn off” the equalization.</p>
<p>As an example of histogram equalization of a color image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fc32b0502926cd90a342e01b73eed8ce26db311.png" data-download-href="/uploads/short-url/fWH8YICl2mLHjwEew7c83mdOI4F.png?dl=1" title="UCYQs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc32b0502926cd90a342e01b73eed8ce26db311_2_517x168.png" alt="UCYQs" data-base62-sha1="fWH8YICl2mLHjwEew7c83mdOI4F" width="517" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc32b0502926cd90a342e01b73eed8ce26db311_2_517x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc32b0502926cd90a342e01b73eed8ce26db311_2_775x252.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fc32b0502926cd90a342e01b73eed8ce26db311.png 2x" data-dominant-color="898884"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">UCYQs</span><span class="informations">873×285 438 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any ideas would be appreciated.</p>

---

## Post #2 by @pieper (2021-04-06 21:36 UTC)

<p>Probably the easiest is just to clone the data and modify/display the clone and delete it when you are done.  Like is done in the Surface Toolbox.</p>

---

## Post #3 by @giovform (2021-04-06 21:42 UTC)

<p>Alright, I was researching the Simple Filters module, and thought it would be a way, but indeed, this solution you mentioned is something in the lines of what I am already doing and is working fine. Thanks Pieper.</p>

---
