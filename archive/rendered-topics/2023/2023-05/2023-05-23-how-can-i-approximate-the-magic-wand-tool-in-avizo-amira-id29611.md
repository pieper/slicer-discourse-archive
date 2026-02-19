---
topic_id: 29611
title: "How Can I Approximate The Magic Wand Tool In Avizo Amira"
date: 2023-05-23
url: https://discourse.slicer.org/t/29611
---

# How can I approximate the magic wand tool in Avizo/Amira?

**Topic ID**: 29611
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/how-can-i-approximate-the-magic-wand-tool-in-avizo-amira/29611

---

## Post #1 by @Russell_Engelman (2023-05-23 19:27 UTC)

<p>I have a skull that I segmented using thresholding that I would like to segment into two layers, corresponding to the upper and lower jaws. I have previously done this in Amira/Avizo, where I select one of the two volumes using magic wand and transfer it to a new material layer.</p>
<p>However, Slicer does not appear to have a function exactly approximating the magic wand tool. I have tried using the Flood Fill extension in the SegmentEditorsExtraEffects package but when I select the volume in the initial material there is no indication an area is highlighted and the material is apparently not being selected by the tool (I cannot get it to move to the new layer). This occurs even when I turn the intensity tolerance to be very large or change the neighborhood size. I have not been able to find any tutorials that show what Flood Fill is supposed to look like when it works correctly.</p>
<p>I also tried using Grow From Seeds but this results in the entire image being segmented, rather than keeing the upper and lower jaws separate (as they are in the original data stack).</p>
<p>Does anyone know why Flood Fill is not working, or another possible alternative to Magic Wand?</p>

---

## Post #2 by @lassoan (2023-05-23 19:39 UTC)

<p>If the upper and lower jaws are not connected then you can simply split them by using the <code>Islands</code> effect’s <code>Split islands to segments</code> method.</p>
<p>If they are not separated then you can use Scissors effect to split the segment (what Amira calls a segment is called “segment” in Slicer) into two, using Scissors effect by setting <code>Operation</code> → <code>Fill inside</code> and <code>Editable area</code> → <code>Inside all segments</code>. See detailed step-by-step instructions <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">here</a>. If you can find a view where the jaws appear separate then you only need the second part of the recipe.</p>
<p>If you want to split segments with a very complex, fuzzy border, then you can use <code>Grow from seeds</code> effect. Make sure to select, <code>Editable area</code> → <code>Inside all segments</code> to prevent re-segmentation of the entire image.</p>
<p>In general, you can expect that you can do much more with Slicer than with Amira/Avizo, but since Slicer is a more complex and versatile tool, with much more functions, it is not always that easy to figure out how to achieve something. If instructions from bing-chat/chatgpt don’t work and you cannot find an answer by googling either then you can always ask here.</p>

---

## Post #3 by @Russell_Engelman (2023-05-23 19:55 UTC)

<p>The split islands to segments method is helpful. Is there a way to split all objects that are not truly connected? I tried using it but what ends up happening is the function ends up removing a large amount of my threshholded volume, retains only the teeth (very little of the thinner bone), and creates two new segments but does not separate the upper and lower jaw into new segments.</p>
<p>Before:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94546b8ffa5ab8b4a0e6dfd19586710464cd5a74.jpeg" data-download-href="/uploads/short-url/labxawPn6hpm9zPIIE2Hoa2EvAw.jpeg?dl=1" title="before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94546b8ffa5ab8b4a0e6dfd19586710464cd5a74_2_690x388.jpeg" alt="before" data-base62-sha1="labxawPn6hpm9zPIIE2Hoa2EvAw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94546b8ffa5ab8b4a0e6dfd19586710464cd5a74_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94546b8ffa5ab8b4a0e6dfd19586710464cd5a74_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94546b8ffa5ab8b4a0e6dfd19586710464cd5a74_2_1380x776.jpeg 2x" data-dominant-color="76787F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before</span><span class="informations">1920×1080 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71721c028a27538806263620a7691f47d4cf2cb0.jpeg" data-download-href="/uploads/short-url/gbAqOlsN9Q6SVMB9uT8oYgr930Y.jpeg?dl=1" title="after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71721c028a27538806263620a7691f47d4cf2cb0_2_690x388.jpeg" alt="after" data-base62-sha1="gbAqOlsN9Q6SVMB9uT8oYgr930Y" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71721c028a27538806263620a7691f47d4cf2cb0_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71721c028a27538806263620a7691f47d4cf2cb0_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71721c028a27538806263620a7691f47d4cf2cb0_2_1380x776.jpeg 2x" data-dominant-color="777880"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after</span><span class="informations">1920×1080 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2023-05-23 20:03 UTC)

<aside class="quote no-group" data-username="Russell_Engelman" data-post="3" data-topic="29611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/russell_engelman/48/18425_2.png" class="avatar"> Russell_Engelman:</div>
<blockquote>
<p>all objects that are not truly</p>
</blockquote>
</aside>
<p>A single voxel that touches both structures in a single slice would block split islands. A quick and simple way to deal with that is to shrink your segment by 1-2 voxels, run your split islands tool, and then dilate each new segment the same amount you shrank.</p>
<p>.</p>

---

## Post #5 by @lassoan (2023-05-23 22:04 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> this is én excellent suggestion.</p>
<p>Also note that you don’t need to restrict editing with masking settings if you use Islands effect / Split islands to segments (in fact, it may interfere with how you use the effect).</p>

---

## Post #6 by @pieper (2023-05-24 17:57 UTC)

<p>If the data has a well-defined threshold-based boundary like the CT you show, then you may want to do the shrink, then separate the islands, then grow by more than you shrank, and re-apply the threshold so that you don’t lose resolution from the shrink-grow operation.</p>

---
