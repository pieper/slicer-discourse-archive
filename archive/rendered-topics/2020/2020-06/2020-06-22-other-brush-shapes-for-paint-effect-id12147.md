---
topic_id: 12147
title: "Other Brush Shapes For Paint Effect"
date: 2020-06-22
url: https://discourse.slicer.org/t/12147
---

# Other brush shapes for paint effect

**Topic ID**: 12147
**Date**: 2020-06-22
**URL**: https://discourse.slicer.org/t/other-brush-shapes-for-paint-effect/12147

---

## Post #1 by @muratmaga (2020-06-22 04:54 UTC)

<p>I am trying to measure trabecular bone properties from different regions of mouse proximal and distal femur epiphyses. Paint brush, with sphere brush enabled, works really well to draw a region of specific diameter. Then on, I can potnetially use the bone texture extension to calculate what we need.</p>
<p>For various reasons, we also need to do this as cubes. Would it be possible to implement other brush effects (particularly square and cube in 3D), that works like the current round brush? Right now I am using <code>CreateModel</code> from SlicerIGT to generate a cube of arbitrary dimensions, and then put it under transform to move it to specific region of the volume that I want to measure, and then convert to a segmentation. It gets a bit tedious.</p>

---

## Post #2 by @pieper (2020-06-22 15:41 UTC)

<p>It wouldn’t be too hard to add a cube brush option to the code, but I’m not sure how generally useful it would be and whether it’s worth exposing it in the interface.  If this is a one-off use case it might be easier to do a little script that paints a cube based on a hot key?</p>

---

## Post #3 by @muratmaga (2020-06-22 16:02 UTC)

<p>That will be fine, but the cube edges needs to be of variable size too…</p>

---

## Post #4 by @lassoan (2020-06-22 16:14 UTC)

<p>You could add a “Fill ROI” effect, which could fill or clear the an area in a segment specified by an ROI node.</p>

---

## Post #5 by @pieper (2020-06-22 16:31 UTC)

<p>Yes, that’s what I was thinking too - <a class="mention" href="/u/muratmaga">@muratmaga</a> would that be easier than what you are doing now?</p>
<p>What about something where a hot key fills in an ROI?</p>

---

## Post #6 by @muratmaga (2020-06-22 16:39 UTC)

<p>If we are talking about the regular annotation ROI boxes, that wouldn’t work for me very well, as it is not trivial to specify where to create them (or set a fix dimension).<br>
CreateModels work nice, expect it just randomly places the cube somewhere in the scene (as far as I can tell).</p>

---

## Post #7 by @lassoan (2020-06-22 16:56 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="12147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If we are talking about the regular annotation ROI boxes, that wouldn’t work for me very well, as it is not trivial to specify where to create them (or set a fix dimension).</p>
</blockquote>
</aside>
<p>You would add all controls that you need to the effect’s GUI (position, size, etc.).</p>
<p>Annotation ROI will be replaced by Markups ROI, so it might make sense to wait a few months for this to happen (or work on Markups ROI implementation to make it happen sooner).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="12147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>CreateModels work nice, expect it just randomly places the cube somewhere in the scene</p>
</blockquote>
</aside>
<p>CreateModels puts models in the RAS coordinate system origin, so that you can set their position and orientation using a transform.</p>

---

## Post #8 by @muratmaga (2020-06-22 17:01 UTC)

<p>It think fillROI with the new markupsROI would be good to have. I will continue using the CreateModels, till then.</p>

---

## Post #9 by @pieper (2020-06-22 17:51 UTC)

<p><code>CreateModels</code> probably just puts it at the origin, but it could be trivial to make it show up where your mouse is.</p>

---

## Post #10 by @Raj_Kumar_Ranabhat (2021-05-11 17:42 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> : Hi, how you were implementing cube model instead of sphere brush ? Can you please share the python scripts if available ?  Did you make a change in code of paint effect.py ?</p>
<p>Please feel free to write.</p>
<p>Thanks</p>

---

## Post #11 by @muratmaga (2021-05-11 19:02 UTC)

<p>I didn’t implement anything. Ended up using cube primitive from CreateModels of converting them to segmentation. but if someone implements the FillROI as a segment editor effect, I think it would be useful in general.</p>

---
