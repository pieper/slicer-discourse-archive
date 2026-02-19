---
topic_id: 9722
title: "Shrink Wrap To Create Mask"
date: 2020-01-06
url: https://discourse.slicer.org/t/9722
---

# Shrink wrap to create mask

**Topic ID**: 9722
**Date**: 2020-01-06
**URL**: https://discourse.slicer.org/t/shrink-wrap-to-create-mask/9722

---

## Post #1 by @hherhold (2020-01-06 22:01 UTC)

<p>I asked a question similar to this a couple of years ago, but the requirements are now a bit different. We have a number of CT scanned specimens (insects, mammals, etc) and we’re interested in segmenting out the internal air spaces. This is slightly different than human tracheal systems as there are sometimes multiple entry points (insects, for example) and odd morphologies (nasal turbinates, for example).</p>
<p>Thresholding works fairly well, as air is differentiated from tissue. The issue is that separating the air outside the specimen from inside the specimen can be very tedious, especially for specimens with many openings to the outside.</p>
<p>What would be ideal (I think) is to create a “specimen mask” by shrink-wrapping around the outside of the specimen. Then this mask would be used as the “Editable area” in Segment Editor and simple thresholding inside that mask could be used to isolate air spaces.</p>
<p>I’ve tried making a mask like this by thresholding the entire specimen, then growing using the margin effect to close up small air spaces, then shrinking back down to the original size. This works well for all but larger air spaces, where I can’t grow large enough with out starting to distort to the point where shrinking back down results in just a blob.</p>
<p>Is there a way to make a “shrink wrap” style mask like this? Or do you guys have any other ideas on how to accomplish this kind of operation?</p>
<p>Many thanks in advance!!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-01-06 22:18 UTC)

<p>Shrink-wrap solidification method is now available as a Segment editor effect (provided by SurfaceWrapSolidify extension).</p>

---

## Post #3 by @hherhold (2020-01-06 23:03 UTC)

<p>DOH! I <em>knew</em> I’d seen something about this.</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---
