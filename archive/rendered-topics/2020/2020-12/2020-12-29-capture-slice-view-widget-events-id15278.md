# Capture slice view widget events

**Topic ID**: 15278
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/capture-slice-view-widget-events/15278

---

## Post #1 by @talmazov (2020-12-29 17:50 UTC)

<p>Hey all,<br>
I would like to know if it is possible to attach a function callback on event associated with the view slice’s change in position. Basically callback on the slider i have circled in the attached screenshot.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98b67153d8b4c9b05540c5d004a158ca81d1b7f3.png" alt="image" data-base62-sha1="lMXsljULnAYh8rnh8A9ywXuwg95" width="509" height="215"></p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-12-29 19:04 UTC)

<p>You probably don’t want to observe GUI widget events, but changes in the slice node position. You can find an example of observing slice node changes here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_slice_planes">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_slice_planes</a></p>

---
