---
topic_id: 47196
title: "Echo Volume Render depth coloring not working"
date: 2026-06-01
url: https://discourse.slicer.org/t/47196
last_bumped: 2026-08-13T22:33:40.768Z
---

# Echo Volume Render depth coloring not working

**Topic ID**: 47196
**Date**: 2026-06-01
**URL**: https://discourse.slicer.org/t/echo-volume-render-depth-coloring-not-working/47196

---

## Post #1 by @aabrown100-git (2026-06-01 21:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2.jpeg" data-download-href="/uploads/short-url/i16byBHVexlMGQkd2gnWoeJkopk.jpeg?dl=1" title="Screenshot 2026-06-01 at 2.47.03 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_690x393.jpeg" alt="Screenshot 2026-06-01 at 2.47.03 PM" data-base62-sha1="i16byBHVexlMGQkd2gnWoeJkopk" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_1380x786.jpeg 2x" data-dominant-color="A09EA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-06-01 at 2.47.03 PM</span><span class="informations">2672×1522 519 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My volume rendering of a 3D echo image does not show depth dependent coloring, like in this demo video: <a href="https://www.youtube.com/watch?v=hzxzUILNhnA&amp;list=PLIFpHI5hhxkszTWJTaWDM-eGTR8zBubSA&amp;index=14" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=hzxzUILNhnA&amp;list=PLIFpHI5hhxkszTWJTaWDM-eGTR8zBubSA&amp;index=14</a>. I tried adjusting the various sliders, but they seems to have no effect, except for “Depth coloring” which just changes the render color uniformly.</p>
<p>3D Slicer 5.10.0, 2026 Macbook Pro, M5 Pro chip.</p>

---

## Post #2 by @aabrown100-git (2026-08-03 19:25 UTC)

<p>Pinging this in hopes of getting some advice!</p>

---

## Post #3 by @mikebind (2026-08-05 05:55 UTC)

<p>Try narrowing the range on the depth coloring slider, it is currently stretching the depth colormap over 500 mm, and my guess is that the rendered echo region covers a small slice of that, so the color range you see is just a small slice of the colormap.  Slide the whole range until the rendered region is a medium depth color, then bring in the edges until you see the range of the colormap that you would like (presumably most of it).</p>

---

## Post #4 by @aabrown100-git (2026-08-05 18:52 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> Thanks for the advice. I tried increasing the “Depth range” to [-10000, 10000], and decreasing to [-10, 10]. For each, sliding the range as well as the min and max had no effect. I’ve attached screen recordings. Please let me know if I’m doing anything obviously wrong!</p>
<div class="youtube-onebox lazy-video-container" data-video-id="Y1rn2ysKFHg" data-video-title="Screen Recording 2026 08 05 at 11 25 37 AM" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Y1rn2ysKFHg" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://i.ytimg.com/vi/Y1rn2ysKFHg/hqdefault.jpg" title="Screen Recording 2026 08 05 at 11 25 37 AM" width="480" height="360">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="jbEk3bYk2ZU" data-video-title="Screen Recording 2026 08 05 at 11 28 23 AM" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=jbEk3bYk2ZU" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://i.ytimg.com/vi/jbEk3bYk2ZU/hqdefault.jpg" title="Screen Recording 2026 08 05 at 11 28 23 AM" width="480" height="360">
  </a>
</div>


---

## Post #5 by @mikebind (2026-08-05 20:27 UTC)

<p>Hm, that does seem odd. I just confirmed that I can get sensible depth renderings using this module.  I’m using Slicer 5.10.0, the same as you.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91e20786581ff97d5f850cf3545beaa88ddeabc9.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d0226be85b60a669120fa61647f817b1b98ccf3.jpeg" data-video-base62-sha1="kOxuVZA55zrIvOX8wGPyufkqqud.mp4">
  </div>I have observed in the past that Echo Volume Render does not play well with any manual adjustment of settings in the Volume Rendering module.  Any chance that you touched something there?  If so, I would try just reopening Slicer and starting from scratch in the Echo Volume Render module, which will reset any confused settings. Beyond that, I would try a different echo volume to see if the issue seems specific to this dataset.  Has this worked for you in the past?<p></p>

---

## Post #6 by @aabrown100-git (2026-08-13 22:33 UTC)

<p>Thanks Mike, I tried reopening Slicer and also using a different echo volume, but no dice. (This hasn’t worked for me in the past).</p>
<p>When you get a chance, could you try the following steps and let me know if it works.</p>
<ol>
<li>
<p>Open Slicer 5.12.3</p>
</li>
<li>
<p>Install SlicerHeart extension</p>
</li>
<li>
<p>Download the SlicerHeart “Mitral” dataset in the Sample Data module.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1.jpeg" data-download-href="/uploads/short-url/6t9FMEhFRgTl6F5blJVhKOcYsr7.jpeg?dl=1" title="Screenshot 2026-08-13 at 3.30.00 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_690x410.jpeg" alt="Screenshot 2026-08-13 at 3.30.00 PM" data-base62-sha1="6t9FMEhFRgTl6F5blJVhKOcYsr7" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_1380x820.jpeg 2x" data-dominant-color="B0ADAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-08-13 at 3.30.00 PM</span><span class="informations">2928×1744 550 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>Switch to the Echo Volume Render module and see if the volume render has depth color (it does not for me)</li>
</ol>

---
