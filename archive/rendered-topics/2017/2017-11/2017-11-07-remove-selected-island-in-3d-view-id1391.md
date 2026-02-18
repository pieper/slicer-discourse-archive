# Remove Selected Island in 3D view?

**Topic ID**: 1391
**Date**: 2017-11-07
**URL**: https://discourse.slicer.org/t/remove-selected-island-in-3d-view/1391

---

## Post #1 by @hherhold (2017-11-07 00:03 UTC)

<p>“Remove Selected Island” is one of my most often-used features - I rely on it heavily. Is there a reason it’s not implemented in the 3D view like some of the other tools (paint, scissors, eraser)?</p>
<p>I’d be curious to take a crack at implementing it as long as there’s no significant technical hurdle like “ITK/VTK doesn’t support it”.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-11-07 00:30 UTC)

<p>What I usually do now is that I enable crosshair on the toolbar, then move the crosshair by Shift+MouseMove in the 3D view, then I click on the island in one of the 2D views. This is not ideal, as it requires an extra click in the slice view, so it would be great if you could contribute the enhancement that would remove the need for the extra click.</p>
<p>The only non-trivial part of the implementation is how to get the segment id from a 3D position. The problem is that the cursor position is right at the segment boundary, so it might be slightly outside the segment. You cannot simply check if that exact position is inside a segment but you may need to add a slight offset along the camera projection line at that position to make sure you get an position inside a segment; or compute the closest distance to all segments, and choose the segment that is closest to the current position.</p>

---

## Post #3 by @hherhold (2017-11-07 00:43 UTC)

<p>Yep, the crosshair trick is what I do right now.</p>
<p>I’ll take a look at adding it. I will most probably be back with more questions - thanks for getting me started!</p>
<p>-Hollister</p>

---

## Post #4 by @TudorSlicer (2022-01-11 22:52 UTC)

<p>I am trying to use Islands to keep one of the bones in a wrist CT.   In Segment Editor I click on Islands and the select Keep Selected Island.  With the crosshair within the radius on all three windows I do not get the option to “apply” and discard everything else.<br>
What am I doing wrong?</p>

---

## Post #5 by @lassoan (2022-03-13 04:39 UTC)

<p>After you choose the “Keep selected island” option, you need to click in the slice view to select an island. If you used the crosshair to find a position in 3D view then you need to click near the crosshair in a slice view. I’ve now improved the <a href="https://github.com/Slicer/Slicer/blob/master/Docs/user_guide/modules/segmenteditor.md#-islands">documentation of the Islands effect</a> to make things more clear.</p>

---
