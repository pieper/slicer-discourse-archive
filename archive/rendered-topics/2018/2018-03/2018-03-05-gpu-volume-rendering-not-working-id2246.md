---
topic_id: 2246
title: "Gpu Volume Rendering Not Working"
date: 2018-03-05
url: https://discourse.slicer.org/t/2246
---

# GPU Volume rendering not working

**Topic ID**: 2246
**Date**: 2018-03-05
**URL**: https://discourse.slicer.org/t/gpu-volume-rendering-not-working/2246

---

## Post #1 by @MHB (2018-03-05 23:00 UTC)

<p>Operating system: win64<br>
Slicer version: 4.8.1</p>
<p>Having trouble volume rendering using the GPU raycasting option? (Dell XPS, intel i7, GTX 1050 GPU). When GPU volume rendering is enabled, it does not display anything, but CPU rendering, works fine. I’ve mandated GPU use through Nvidia’s control panel, but still nothing. Note that I’m loading a stack of images that aren’t DICOM formatted, so it could just be that I’ve made a simple mistake.</p>

---

## Post #2 by @pieper (2018-03-05 23:19 UTC)

<p>Are you able to use GPU volume rendering with data from the SampleData module?  This would help determine if it’s your data or your system at issue (from what you’ve said I suspect maybe it’s the data).  If it is the data, then it could help for you to provide a publicly shareable dataset that could be used to see if the issue can be replicated on other systems.</p>

---

## Post #3 by @MHB (2018-03-06 00:42 UTC)

<p>Steve:<br>
Thanks for your feedback, it appears to work with the SampleData, so it’s likely the data format on my end. This particular dataset isn’t shareable, but I will try to find one to get some additional help.</p>

---

## Post #4 by @MHB (2018-03-06 00:55 UTC)

<p>Steve:<br>
Actually, belay my earlier comment. GPU based ray casting is not working even with SampleData. I had initially thought it was (it was rendering black patches) but when compared to results from CPU rendering, it is obvious that GPU is not performing properly.</p>

---

## Post #5 by @pieper (2018-03-06 01:20 UTC)

<p>Interesting - okay, so maybe there’s something with your driver?  Windows with an nvidia 1050 should be a pretty mainstream system so I don’t know why it’s not working normally for you.  Maybe if you past in a screenshot of the rendering you see for one of the sample datasets someone will have suggestions.</p>

---

## Post #6 by @lassoan (2018-03-06 01:34 UTC)

<p>You have to enable GPU volume rendering for SlicerApp-real.exe.</p>
<p>It would be also interesting to try latest nightly build of 3D Slicer, as in recent 4.9.x versions volume rendering works with many more GPUs than in 4.8.1 version.</p>

---

## Post #7 by @MHB (2018-03-06 01:38 UTC)

<p>Andras:<br>
That was it. Apparently I’d enabled GPU on wrong slicer.exe file. Apologies for the new guy mistakes!</p>

---
