# How to show only selected control point, and hide non selected in mark ups

**Topic ID**: 29261
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/how-to-show-only-selected-control-point-and-hide-non-selected-in-mark-ups/29261

---

## Post #1 by @Kae1 (2023-05-02 23:25 UTC)

<p>Is it possible to show only a selected control point on coronal, sagittal and axial slices, and hide the none selected control points?</p>
<p>I have a range of implanted stereo EEG electrode contacts in my mark up file and am using the ‘jump slice’ function in Markups/Control Points to view selected electrode/contacts in the three axis. However when I ‘jump slice’ to view any given electrode/contact, the axial/coronal/sagittal slices are still crowded with the many other electrodes/contacts in the brain, which are proximal to the electrode of interest.</p>
<p>I want to be able to ‘jump slice’ to view a given electrode/contact point of interest in a way that hides all the other contact points, so that the electrode/contact of interest is more easily and clearly seen.</p>
<p>Does Slicer mark up have this functionality?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-05-03 00:23 UTC)

<p>If I remember correctly, when you click on a markup to jump slices, only the views in the same “view group” jump. You can modify the view group of the red, green, yellow slices from the default 0 to different ones (0, 1, 2) in View Controllers module.</p>

---
