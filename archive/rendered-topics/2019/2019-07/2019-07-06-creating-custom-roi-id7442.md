---
topic_id: 7442
title: "Creating Custom Roi"
date: 2019-07-06
url: https://discourse.slicer.org/t/7442
---

# Creating custom ROI

**Topic ID**: 7442
**Date**: 2019-07-06
**URL**: https://discourse.slicer.org/t/creating-custom-roi/7442

---

## Post #1 by @Jainey (2019-07-06 02:49 UTC)

<p>Hi All</p>
<p>Is there a way that I create a custom shaped ROI, instead of the box. A spherical one.</p>
<p>Thanks</p>
<p>Tom</p>

---

## Post #2 by @lassoan (2019-07-06 03:58 UTC)

<p>You can create arbitrarily shaped masks and segments in Segment Editor. You can construct various shapes using VTK sources using a few lines of Python code - see example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer" rel="nofollow noopener">here</a>. In recent Preview releases you can also create arbitrarily sized spherical markers using Markups module.</p>

---

## Post #3 by @Jainey (2019-07-08 17:30 UTC)

<p>Thanks Prof. <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>I am trying to crop an arbitrary shape. Do you think there is a module that I can combine with crop volume module so that  instead of the box ROI I can create a sphere which can be cropped .</p>
<p>I would like to keep it in the same format without segmenting/ stl or obj.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2019-07-09 03:37 UTC)

<aside class="quote no-group" data-username="Jainey" data-post="3" data-topic="7442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>I am trying to crop an arbitrary shape.</p>
</blockquote>
</aside>
<p>Images are always stored in a rectilinear grid. If you mean you want to blank out part of an image then you can do that in Segment Editor module: define a region using a segment (Paint effect with sphere brush; Scissors effect with sphere shape; etc.) then use Mask volume effect. To get Mask volume effect, install SegmentEditorExtraEffects extension.</p>

---

## Post #5 by @Jainey (2019-07-15 14:24 UTC)

<p>Thanks Prof. <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>I did install extra effects and it works fine. But say I want to cut out a sphere from the middle, I mask the surrounding image with this. Then can I still keep my middle sphere as a volume rather than a model/stl.</p>
<p>Thanks a lot</p>

---

## Post #6 by @lassoan (2019-07-15 14:39 UTC)

<aside class="quote no-group" data-username="Jainey" data-post="5" data-topic="7442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>can I still keep my middle sphere as a volume</p>
</blockquote>
</aside>
<p>Yes. This is what Mask volume is for. It blanks out regions in the volume that is inside or outside the selected segment.</p>

---

## Post #7 by @Jainey (2019-07-16 16:49 UTC)

<p>Thanks Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
