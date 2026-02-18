# Crop Volume Issue in 4.11

**Topic ID**: 21862
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/crop-volume-issue-in-4-11/21862

---

## Post #1 by @sni94 (2022-02-09 00:03 UTC)

<p>In version 4.11, I try to crop a volume but the resulting volume just looks like a single slice. When I change all my views to view that volume, the position readout in the top right corner of each view only shows -1, 0, and 1 mm, and when you move between each of those, the image doesn’t change at all. I’ve compared this to cropping a volume in 4.10.2 and made sure all the options in the UI are the same, and it’ll be successful in 4.10.2 but show what I described in 4.11. People on my team say they have used 4.11 successfully to crop a volume before but now they are seeing this issue. Any ideas on what might be causing this?</p>

---

## Post #2 by @mikebind (2022-02-09 00:33 UTC)

<p>Is your cropping ROI the same in each case? I think that older versions of Slicer automatically fit the ROI to the volume on initialization, whereas perhaps that works differently with the newer MarkupsROI? Perhaps you need to explicitly click the “Fit to Volume” button to get that same behavior?</p>

---
