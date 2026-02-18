# Rigidly register a segment without CT to another segment with CT

**Topic ID**: 10993
**Date**: 2020-04-05
**URL**: https://discourse.slicer.org/t/rigidly-register-a-segment-without-ct-to-another-segment-with-ct/10993

---

## Post #1 by @mimi (2020-04-05 00:17 UTC)

<p>Hello! I have a segment of the left ventricle without a CT (visualizing electrophysiological data) which I would like to register to a segment of the left ventricle on a CT. The idea is to overlay the electrophysiological data with the anatomy. I tried segment registration but it moves the CT to the segment instead of moving the segment to the CT. I would be grateful for hint in the right direction. Thank you</p>

---

## Post #2 by @lassoan (2020-04-05 00:28 UTC)

<aside class="quote no-group" data-username="mimi" data-post="1" data-topic="10993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/9fc348/48.png" class="avatar"> mimi:</div>
<blockquote>
<p>I tried segment registration but it moves the CT to the segment instead of moving the segment to the CT</p>
</blockquote>
</aside>
<p>Switch input volumes+segmentations: set to fixed what was moving, set to moving what was fixed. Or you may keep your inputs as is, invert the computed transform in Transforms module (by clicking “Invert” button in Transforms module), and apply it to the fixed volume+segmentation.</p>

---

## Post #3 by @mimi (2020-04-05 00:30 UTC)

<p>Hi! Thanks for the quick reply. Did I use the right module? Where is this ‘Invert’ button? Really appreciate your help</p>

---

## Post #4 by @lassoan (2020-04-05 01:22 UTC)

<aside class="quote no-group" data-username="mimi" data-post="3" data-topic="10993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/9fc348/48.png" class="avatar"> mimi:</div>
<blockquote>
<p>Where is this ‘Invert’ button?</p>
</blockquote>
</aside>
<p>In Transforms module / Edit section.</p>

---

## Post #5 by @mimi (2020-04-05 01:23 UTC)

<p>Thank you. What do I select as a fixed image if the segment that I want to move does not have CT associated with it. So far, there is no option to not have a CT</p>

---

## Post #6 by @lassoan (2020-04-05 01:43 UTC)

<p>If selection is required then you can select any volume (for example, load the CT twice) and just don’t use the transformed image, only the computed transformation.</p>

---
