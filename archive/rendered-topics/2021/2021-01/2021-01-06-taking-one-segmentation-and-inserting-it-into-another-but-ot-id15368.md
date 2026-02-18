# Taking one segmentation and inserting it into another but other one has very small volume

**Topic ID**: 15368
**Date**: 2021-01-06
**URL**: https://discourse.slicer.org/t/taking-one-segmentation-and-inserting-it-into-another-but-other-one-has-very-small-volume/15368

---

## Post #1 by @NoobForSlicer (2021-01-06 04:01 UTC)

<p>So when I didn’t have much ram, I was cropping volume and then working with small volume segmenting only what needed there.</p>
<p>Then I cropped another part of that big main volume and segmented another thing.</p>
<p>Then I pulled the segment from one segmentation and inserted into another one.</p>
<p>This created a problem: When exporting the other segment is not visible.</p>
<p>From my understanding: cropped volume under the segmentation was small and the other segment is simply not even inside of it.</p>
<p>What to do?</p>

---

## Post #2 by @NoobForSlicer (2021-01-06 04:22 UTC)

<p>okay so for anyone reading this… if you messed up and used many small cropped volumes to paint and then ended up with bunch of cropped volumes and try to fuse them together…</p>
<p>Best way to put all segments back into 1 segmentation is:</p>
<p>have a volume that is as big and covers all the segmentations.<br>
Create one new segmentation for that volume.<br>
Put segments from all those dumb little segmentations you made on cropped volumes in that segmentation that has been created for the big mother volume <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I just managed to make it work, now copying and showing files works like charm <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #3 by @muratmaga (2021-01-06 04:25 UTC)

<p>I tried this and it works fine for me:</p>
<ol>
<li>Take MRHead and create two none overlapping cropped volumes.</li>
<li>Segment something from each of them separately.</li>
<li>Use the Segmentations Copy/Move segments operation to move one segment to the other</li>
<li>See that they now they both visible within the same segmentation (whichever one you copied to).</li>
</ol>
<p>You should of course adjust the background volume to be the full volume, not of the cropped ones. If you are only looking at the cropped volumes, one segmentation would be outside of the field of view (since Slicer automatically adjusts the FOV).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e22cb636888ef1d1bb103841d8a1a5ade7652c35.png" data-download-href="/uploads/short-url/wgPHzJTTWuFIuoyVlEfrYEkNPhj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e22cb636888ef1d1bb103841d8a1a5ade7652c35.png" alt="image" data-base62-sha1="wgPHzJTTWuFIuoyVlEfrYEkNPhj" width="588" height="499" data-dominant-color="4A4847"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">986×838 98.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @NoobForSlicer (2021-01-06 04:28 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="15368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>You should of course adjust the background volume to be the full volume, not of the cropped ones.</p>
</blockquote>
</aside>
<p>Absolutely! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Exactly <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> thank you so much for replying</p>

---
