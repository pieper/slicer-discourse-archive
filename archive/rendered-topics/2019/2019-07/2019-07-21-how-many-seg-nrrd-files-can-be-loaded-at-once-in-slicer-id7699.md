# How many seg.nrrd files can be loaded at once in Slicer?

**Topic ID**: 7699
**Date**: 2019-07-21
**URL**: https://discourse.slicer.org/t/how-many-seg-nrrd-files-can-be-loaded-at-once-in-slicer/7699

---

## Post #1 by @NoobForSlicer (2019-07-21 02:01 UTC)

<p>How many seg.nrrd files can be loaded at once in Slicer?</p>
<p>Is there some kind of limit? Is it just a question of memory or maybe some other things?</p>
<p>I will have to load around 50 segmentations for one project, so far I made 3 segmentations <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> manually and 10 using some semi-automated built in tools. It’s kind of going slow I’ll get there hopefully <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Just interested if I’m doing something wrong and maybe around number of 49 something goes south and won’t load haha</p>
<p>I think I also read somewhere a topic that there are some better techniques and this wouldn’t be the smartest way?</p>
<p>sorry i’m a noob <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #2 by @lassoan (2019-07-21 03:07 UTC)

<aside class="quote no-group" data-username="NoobForSlicer" data-post="1" data-topic="7699">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar"> NoobForSlicer:</div>
<blockquote>
<p>How many seg.nrrd files can be loaded at once in Slicer?</p>
</blockquote>
</aside>
<p>The only limit is your memory space. If you don’t have enough physical memory then you can configure more virtual memory in your operating system but then of course things will be slow.</p>
<p>It may be a good idea to only keep those segmentations in the scene that you are actively using (displaying, processing, …). You can save the segmentation into file and remove from the scene to save memory and reload it later when you need it.</p>

---

## Post #3 by @NoobForSlicer (2019-07-21 09:42 UTC)

<p>Very clear and to the point as always Andras…<br>
Thank you very much.</p>
<p>Absolutely, saving segmentations and working with them was so easy to learn and use, load and unload. I was just thinking to myself too good to be true? <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>
<p>Thank you so much for helping me out and guiding me.</p>

---
