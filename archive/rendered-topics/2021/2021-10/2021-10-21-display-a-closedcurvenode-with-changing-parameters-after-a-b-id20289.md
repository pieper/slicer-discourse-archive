# Display a ClosedCurveNode with changing parameters after a button press event

**Topic ID**: 20289
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/display-a-closedcurvenode-with-changing-parameters-after-a-button-press-event/20289

---

## Post #1 by @helenawill95 (2021-10-21 18:36 UTC)

<p>I am creating a module where i would like to display a closed curve after an event. The closed curve will change after each event (button / addition of fiducial point) dependent on the new coordinates defined.</p>
<p>How can I create the closed curve node and display it with a set of  changing coordinates in a module, I am able to do this manually via python interactor but struggling to import this into my module?</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2021-10-22 18:27 UTC)

<p>Do you use markups closed curve or you are observing a markups fiducial list and update the curve whenever the points are moved?</p>

---

## Post #3 by @helenawill95 (2021-10-26 13:04 UTC)

<p>I am using a markups closed curve, but have it working now thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I  just need to include observer events to ensure the curve is deleted when deleted manually on Slicer GUI.</p>

---
