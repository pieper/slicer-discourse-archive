---
topic_id: 4517
title: "Moving Slice Intersection Crosshair Over A Fiducial Point"
date: 2018-10-24
url: https://discourse.slicer.org/t/4517
---

# Moving slice intersection/crosshair over a fiducial point

**Topic ID**: 4517
**Date**: 2018-10-24
**URL**: https://discourse.slicer.org/t/moving-slice-intersection-crosshair-over-a-fiducial-point/4517

---

## Post #1 by @mag (2018-10-24 01:53 UTC)

<p>Hello,</p>
<p>this is just a very minor issue but I am using Slicer a lot lately and it started bothering me a bit.</p>
<p>When I display the slice intersection or the cross hair and use Shift-Key + mouse movements to scroll the slice viewers, if I have a fiducial point and I want to place the crosshair exactly on it, it won’t go because the mouse changes to the picking-hand mode. So I have to use the sliders on top of the viewers to move the intersection/crosshair exactly on top of the fiducial point.</p>
<p>As I said, not a big issue but it slows me down and if there is a way to change it so that when Shift is pressed the mouse never switches to the picking hand mode that would be great (hoping that doesn’t screw other mouse/keyboard shortcuts).</p>
<p>Thanks,</p>
<p>Marta</p>

---

## Post #2 by @jamesobutler (2018-10-24 03:01 UTC)

<p>Hi Marta,</p>
<p>I can replicate what you are experiencing. There is actually another way for you to quickly move all the slice intersections so that they are exactly over a fiducial point which I think is what you are primarily concerned with achieving.  If you switch to the Markups module you will see a table of fiducials. If you check the “Click to Jump Slices” checkbox then highlighting/selecting a new row in the table will automatically jump all the slice intersections to be over that fiducial. You can also right-click an individual row in the table and choose “Jump slices”.</p>
<p>Also, Slicer 4.10 has recently been released as a new stable build with various other improvements. I recognize that you are using an older version because in the current version of Slicer the mouse hand doesn’t actually change to the picking-hand mode anymore when hovering near/on a fiducial. However, I can confirm that it doesn’t solve the issue you have with using shift-key + mouse move to move slice viewers over a fiducial.</p>

---

## Post #3 by @cpinter (2018-10-24 12:25 UTC)

<p>Hi Marta,</p>
<p>Besides the “jump to slices” feature butt@jamesobutler described, you could also use the workaround to decrease glyph size. If you open Advanced in the Markups module, then decrease the Glyph Scale slider, then the “dead space” can be arbitrary small. This is only a workaround of course.</p>
<p>To me it seems reasonable to ignore the widgets when the shift key is pressed, as pressing shift clearly indicates the user’s intention of scrolling though slices, and there is limited possibility for further interactions in that mode.</p>

---
