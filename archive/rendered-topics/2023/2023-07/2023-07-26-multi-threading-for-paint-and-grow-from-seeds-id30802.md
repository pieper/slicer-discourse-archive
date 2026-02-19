---
topic_id: 30802
title: "Multi Threading For Paint And Grow From Seeds"
date: 2023-07-26
url: https://discourse.slicer.org/t/30802
---

# Multi-threading for paint and grow from seeds

**Topic ID**: 30802
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/multi-threading-for-paint-and-grow-from-seeds/30802

---

## Post #1 by @coco (2023-07-26 16:01 UTC)

<p>Dear all,<br>
We run slicer on a linux calculation server because our 3D datasets are large (~50 GB per image).<br>
I’ve seen a couple of posts and detailed answers about multi-threading but can i ask you if “paint” and “grow from seeds” can be multithreaded as these tools take a lot of time for me and it would appear that I am using only one core even though I specify several cores.<br>
I’m currently using the CPU with the fastest clock rate available in our institute and just enough RAM (~190GB) to manage my dataset.<br>
Perhaps, more generally, it would be useful to know which computations are multithreaded and which are not ?</p>
<p>Kind regards</p>

---

## Post #2 by @coco (2023-07-27 08:50 UTC)

<p>Dear all. I realised my latest images were 16 bits which is more than required at the segmentation stage (but needed for preprocessing). So after conversion, I should have my problem solved as we manage to segment 10 GB images without too much issues.<br>
But still, I would like to know if there are some tweaks to do to improve paint/grow from seeds, espeically multithreading as it seems to work on single thread right now.<br>
Best</p>

---

## Post #3 by @pieper (2023-07-27 13:32 UTC)

<p>The current Grow from seeds uses an optimized GrowCut that may not be easy to parallelize.  You can find pointers to the implementations <a href="https://github.com/Slicer/Slicer/issues/6936">here</a></p>
<p>Here’s an example of <a href="https://github.com/pieper/SlicerCL/tree/master/GrowCutCL">a brute-force parallel implementation</a> that may be faster depending on the data.  It hasn’t been touched in many years but it might be possible to use if you are able to put in some effort.</p>

---

## Post #4 by @coco (2023-07-27 14:50 UTC)

<p>Thanks,<br>
Most likely something out of my reach but thanks pieper for the suggestion.</p>

---
