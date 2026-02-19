---
topic_id: 25517
title: "Control Point Labels Show Through 3D Volume In Volume Render"
date: 2022-10-03
url: https://discourse.slicer.org/t/25517
---

# Control point labels show through 3D volume in volume rendering

**Topic ID**: 25517
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/control-point-labels-show-through-3d-volume-in-volume-rendering/25517

---

## Post #1 by @Pheasant (2022-10-03 04:58 UTC)

<p>Hi,</p>
<p>It would seem that the markup labels show through the 3D volume when using volume rendering. Is it possible to turn this off or is it a bug?</p>
<p>It gets very crowded with text and it is difficult to pinpoint the correct labels when they all can be constantly seen. I would like for the labels still to be there so they can be seen in the proper 2D slices and in the mark up module</p>

---

## Post #2 by @muratmaga (2022-10-03 05:17 UTC)

<aside class="quote no-group" data-username="Pheasant" data-post="1" data-topic="25517">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pheasant/48/15560_2.png" class="avatar"> Pheasant:</div>
<blockquote>
<p>3D volume when using volum</p>
</blockquote>
</aside>
<p>I don’t think this is possible with the UI controls. If you are not actively collecting landmarks, one solution would be to clone the pointList and then use one copy for 2D display (where you can turn off the 3D visibility), and you set to the second copy to set to be visible only in 3D but bring down the text scaling to % (so the labels are not visible, only the glyphs).</p>

---

## Post #3 by @Pheasant (2022-10-03 06:05 UTC)

<p>In the previous versions the volume covered the labels. Is ti possible to get that feature back?</p>
<p>The solution doesn’t seem to be too useful for our purposes.</p>

---

## Post #4 by @muratmaga (2022-10-03 15:18 UTC)

<aside class="quote no-group" data-username="Pheasant" data-post="3" data-topic="25517">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pheasant/48/15560_2.png" class="avatar"> Pheasant:</div>
<blockquote>
<p>In the previous versions the volume covered the labels. Is ti possible to get that feature back?</p>
</blockquote>
</aside>
<p>I don’t know, that’s up to the developers and how strongly this is needed by user base. I occasionally needed to do same need, but so far solution worked for me. I also find it a bit strange that the glyph can be occluded by the volume but not the accompanying label.</p>

---

## Post #5 by @rbumm (2022-10-03 16:00 UTC)

<p>Thank you for the report. The markup labels should definitely be occluded by the volume in the 3D view and I can reproduce they are not in Slicer 5.0.3 and 5.1. This looks like an issue and probably should be reported unless we oversee something here.</p>

---

## Post #6 by @muratmaga (2022-10-03 17:51 UTC)

<p>I recall vaguely a discussion with <a class="mention" href="/u/lassoan">@lassoan</a> and was under the impression that choice was by design (keeping the labels on all times).</p>

---

## Post #7 by @Pheasant (2022-10-04 05:56 UTC)

<p>That would be a weird design choice but hopefully the choice can be implemented. Thanks for the possible work around though, it can work in an emergency.</p>

---

## Post #8 by @rbumm (2022-10-04 15:56 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="25517">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>The markup labels should definitely be occluded by the volume</p>
</blockquote>
</aside>
<p>Sorry, I need to correct my post: The markup labels are occluded by <em>segmentations</em> in 3D Slicer and not by volume renderings.</p>

---

## Post #9 by @Pheasant (2022-11-01 07:43 UTC)

<p>So will it be fixed then? In previous versions the labels were occluded by volume renderings and I am not sure why this change occured if it is intentional.</p>

---

## Post #10 by @cpinter (2022-11-04 11:56 UTC)

<aside class="quote no-group" data-username="Pheasant" data-post="3" data-topic="25517">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pheasant/48/15560_2.png" class="avatar"> Pheasant:</div>
<blockquote>
<p>In the previous versions the volume covered the labels</p>
</blockquote>
</aside>
<p>Can you please tell us in which version you refer to? (The latest in that the volume covered the labels)</p>
<p>I imagine it was a long time ago, when 3D text actors were used to show labels, however, they had serious issues and then 2D text actors were introduced instead that are not occluded by 3D objects like volume rendering.</p>

---

## Post #11 by @Pheasant (2022-11-04 12:05 UTC)

<p>The latest I can find where it works is 4.10 it would seem.</p>
<p>What sort of issues were there regarding them? What would be the difference between the text and the points as those are properly occluded?</p>
<p>Would it be possible to link a hidden markup point to the text and hide the text if it the point is occluded or are the two objects completely different things?</p>

---
