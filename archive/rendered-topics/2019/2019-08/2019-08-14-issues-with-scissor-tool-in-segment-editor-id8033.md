# Issues With Scissor Tool in Segment Editor

**Topic ID**: 8033
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/issues-with-scissor-tool-in-segment-editor/8033

---

## Post #1 by @jake111 (2019-08-14 19:35 UTC)

<p>I’m trying to use the scissor tool to isolate a liver from a full abdomin CT scan.  I’ve loaded the image &gt; Segment Editor &gt; Add &gt; Scissor tool but when I drag to select the area with erase inside/outside/etc. nothing happens.</p>
<p>I found that if I paint then the scissor tool works to cut the painted area, but won’t work on the organs themselves, only what I’ve added.  This led me to thinking that my master volume had an issue since I couldn’t work directly on the organs.</p>
<p>Is there a way to use master volume to select the organs directly?   Or is there something else going wrong?</p>

---

## Post #2 by @Amine (2019-08-14 20:41 UTC)

<p>Hi, Scissor tool only allows you to work on existing segments, you cannot isolate an organ from your image directly, there are a lot of options avaible (fill inside, outside, etc) to use, note that scissor tool “fill inside” will fill everything behind the drawn area, it is mostly useful to cut unwanted parts from a threshold obtained segment<br>
If you aim to draw individual slices then use the draw tool instead and you can interpolate between multiple drawn slices using fill between slices. (Note: do not draw successive slices, always leave a space so fill between slices can work)</p>

---

## Post #3 by @lassoan (2019-08-14 23:46 UTC)

<aside class="quote no-group" data-username="jake111" data-post="1" data-topic="8033">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e47774/48.png" class="avatar"> jake111:</div>
<blockquote>
<p>won’t work on the organs themselves, only what I’ve added</p>
</blockquote>
</aside>
<p>Do you mean you would like to alter voxels in the master volume (blank out certain regions)? For segmenting an organ, you don’t need to do this, you just paint an overlay. Later, if you want, you can blank out regions inside or outside a segment using “Mask volume” effect (provided by SegmentEditorExtraEffects extension).</p>

---

## Post #4 by @jake111 (2019-08-20 23:14 UTC)

<p>I was just referring to altering the voxels within the master volume.  Thanks for the help, I got it figured out.</p>

---
