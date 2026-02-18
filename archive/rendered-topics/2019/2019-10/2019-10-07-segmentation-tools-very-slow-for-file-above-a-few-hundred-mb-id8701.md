# Segmentation tools very slow for file above a few hundred Mb

**Topic ID**: 8701
**Date**: 2019-10-07
**URL**: https://discourse.slicer.org/t/segmentation-tools-very-slow-for-file-above-a-few-hundred-mb/8701

---

## Post #1 by @pgueriau (2019-10-07 23:23 UTC)

<p>Operating system: tried on different systems, all of them better than the recommended hardware configuration<br>
Slicer version: 4.10.1<br>
Expected behavior: color / record the selected pixels using Draw of Level tracing should take no more than a second<br>
Actual behavior: it takes 10 seconds.</p>
<p>Sorry if this post overlaps with a previous one, I couldn’t find anything related while going through the forum.</p>
<p>I am wondering how is the segmentation recording/saving coded, as segmentation of my current dataset (276 images for a total of ~450 Mo, i.e. not a big file) using simple tools like Draw or Level tracing takes some 10 seconds to display / record the segmented area after a “click”… My idea being to segment several structures every 5-10 slices to then “fill between slices”, it’s not doable.</p>
<p>I have to confess that I am new with Slicer, as I had access to (expensive) proprietary software until recently. With the latter such basic/simple segmentation operations were quasi-instantaneous (even working on much larger datasets), hence my surprise here.</p>
<p>So, I have tried 3 different operating systems so far (MacBook Pro, PC, gamer PC), all with higher spec than the recommended hardware configuration, and the result is identical (which is somehow reinsuring I suppose).</p>
<p>Now, if I only open 30 images (out of the 276), then Draw or Level tracing takes “only” 2-3 seconds to display / record the segmented area.<br>
And around 1 second if I crop half of these images.</p>
<p>So, it seems to me that while applying the segmentation to a single tomographic slice, the code runs through the whole stack of images, making processing ?unnecessary long. Couldn’t it be a way to just “color” the pixels corresponding to the selected area, and only do the save /assignation of the segmented pixels within the whole volume in a later stage?</p>
<p>Thank you very much for your help. I really enjoy Slicer, in particular this Level tracing tool that, besides being unfortunately so slow for me, works extremely well and is incredibly useful for my applications.</p>
<p>Pierre</p>

---

## Post #2 by @lassoan (2019-10-07 23:38 UTC)

<p>First of all, we are constantly making fixes and improvements, so please try with the latest stable version of Slicer (currently 4.10.2) and a recent preview version.</p>
<p>If you have at least 10x more physical RAM in your computer than the size of the data set then most interactive segmentation operations should be instantaneous. If the input file is compressed then most likely the uncompressed file is about 1GB so you would need 10GB RAM if you want to make sure that swapping memory to disk does not slow you down (and of course close all other memory-hogging applications, such as web browsers).</p>
<p>If you enabled “Show 3D” then make sure to disable surface smoothing while you are interactively editing the segmentation.</p>

---

## Post #3 by @pieper (2019-10-08 20:40 UTC)

<p>Also, if you watch a few of the videos on the tutorial pages you’ll see how slicer works for us, and you can also try some of our SampleData.  If you find scenarios or data that don’t perform well can you share a short screen video to illustrate what you did?</p>

---
