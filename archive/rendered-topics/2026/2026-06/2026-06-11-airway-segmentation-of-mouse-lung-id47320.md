---
topic_id: 47320
title: "Airway segmentation of mouse lung"
date: 2026-06-11
url: https://discourse.slicer.org/t/47320
last_bumped: 2026-06-13T16:40:18.700Z
---

# Airway segmentation of mouse lung

**Topic ID**: 47320
**Date**: 2026-06-11
**URL**: https://discourse.slicer.org/t/airway-segmentation-of-mouse-lung/47320

---

## Post #1 by @ljuno (2026-06-11 20:54 UTC)

<p>Hello,</p>
<p>I am working with 3D slicer in hopes to segment the airway of this mouse lung, acquired from lightsheet microscopy. I would like to segment the main airways, but not the alveoli (at least not yet - I am hoping to do this in the future though) to measure the diameter of the airways and how they change in diameter as they get further away from the main bronchial tree. I have tried to use the threshold tool since it is dark in the airways, but I am still picking up the alveoli. I have also tried the grow from seeds module but it seems like it would require a lot of manual effort to get my segments how I would like them. That is fine and I can do the manual painting to fix it, but I was just wondering if there would be a more effective way to do this? I have not been able to use any of the lung/airway modules/extensions since my data is of a single (left) lung of a mouse from lightsheet microscopy and the ones I have seen are for both human lungs from CT. Thank you very much in advance for any advice you have!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9.jpeg" data-download-href="/uploads/short-url/dmt4PydSASLHW7O6cPf0mXxxY7v.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_690x353.jpeg" alt="image" data-base62-sha1="dmt4PydSASLHW7O6cPf0mXxxY7v" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_1380x706.jpeg 2x" data-dominant-color="3C3530"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×984 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7.jpeg" data-download-href="/uploads/short-url/mYniXAn95EbZtDoxTqJ1LDS8hdd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_690x355.jpeg" alt="image" data-base62-sha1="mYniXAn95EbZtDoxTqJ1LDS8hdd" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_1380x710.jpeg 2x" data-dominant-color="4B4747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×988 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ebrahim (2026-06-12 12:43 UTC)

<p>Some extensions that could be helpful are <a href="https://github.com/coendevente/SlicerNNInteractive">NNInteractive</a> and <a href="https://github.com/mazurowski-lab/slicersegmentwithsam">SegmentWithSAM</a>, both available in the extension manager.</p>
<p>You could try both and see if it at least gives you an easier starting point to work with</p>
<p>For SegmentWithSAM make sure to normalize image values to a 0-255 range. The work would then be layer by layer, but then it gives you a way to propagate your segmentation across slices. I had success solving a similar problem to yours with it. It still takes some fiddling to get the right workflow.</p>
<p>The alveoli are connected and are not isolated islands, right? If they were isolated islands you could use the islands tool in the segment editor and filter out connected components smaller than a certain size. If you have an easy way to <em>make</em> them become disconnected then this also becomes an option</p>

---

## Post #3 by @ljuno (2026-06-12 16:29 UTC)

<p>Hi Ebrahim,</p>
<p>Thank you very much for your insight! I will surely give those two extensions I try. Correct, they are connected (at least generally for the most part). I agree that being able to just keep the largest island would probably be the easiest for only getting the big airways and not the tiny ones. I did not realize there was a size exclusion, I will look into that as well. We have previously done most of our image analysis in Imaris which has size tools that help make surfaces for things like this where you only want the bigger parts of the airways. Perhaps that size filter in islands could work well. In the past for a different project I did do something similar where I basically made my 3D model, then used the scissor tool to chop away and disconnect all the bits I didn’t want and used the island tool to keep the largest one. That may also work here.</p>
<p>Thank you very much, I greatly appreciate it!</p>
<p>-Liberty</p>

---

## Post #4 by @ebrahim (2026-06-12 16:36 UTC)

<aside class="quote no-group" data-username="ljuno" data-post="3" data-topic="47320">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/59ef9b/48.png" class="avatar"> ljuno:</div>
<blockquote>
<p>In the past for a different project I did do something similar where I basically made my 3D model, then used the scissor tool to chop away and disconnect all the bits I didn’t want and used the island tool to keep the largest one. That may also work here</p>
</blockquote>
</aside>
<p>That’s a good idea</p>
<p>If the airway becomes very thin leading up the alveoli and then bubbles out into the alveoli then you could do something like the following with the margin tool:</p>
<ul>
<li>shrink segmentation until alveoli become severed from the main ariway</li>
<li>use islands tool to filter them out by size</li>
<li>grow segmentation back to what it was</li>
</ul>

---

## Post #5 by @vokavoka351 (2026-06-13 16:40 UTC)

<p>Actually, the fastest and most straightforward workflow to start with is using the <strong>Threshold</strong> effect in the Segment Editor. Since you are working with distinct structural densities, it gives you immediate, accurate initial results across all slices simultaneously.</p>
<p>To make the process much easier, try lowering the <strong>Opacity</strong> of your segmentation layer (you can adjust this in the segment list or advanced display settings). This allows you to see through the colorful mask, visually verifying all underlying anatomical structures and boundaries in real-time while you fine-tune the threshold range.</p>

---
