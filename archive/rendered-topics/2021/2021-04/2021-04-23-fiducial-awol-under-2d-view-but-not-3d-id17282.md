# Fiducial awol under 2D view but not 3D

**Topic ID**: 17282
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/fiducial-awol-under-2d-view-but-not-3d/17282

---

## Post #1 by @njeffery123 (2021-04-23 17:49 UTC)

<p>Dear All,</p>
<p>Just upgraded from 4.10 to latest stable version 4.11.20210226</p>
<p>My old 4.10 scenes open up ok but strangely I can not see my fiducial markers in the 2D views. They do appear ok in the 3D view, just missing altogether from the 2D slice views.</p>
<p>If I create a new set they do appear in 2D and 3D (identical settings). I have tried all the settings under “2D display”</p>
<p>Bit of a puzzle and would be a shame to revert back to an older version so I can continue working with my exisitng fiducials. Any ideas?</p>
<p>I should note one, possibly related observation: my data is in nrrd format. Under 4.10 the coronal and sagittal views were the wrong way round. Didn’t matter to me. Under 4.11 the views are correct. I wonder if this has scuppered the fiducials.</p>

---

## Post #2 by @lassoan (2021-04-23 17:52 UTC)

<p>This is due to a new feature that 2D visibility of markups are now taken into account (see details <a href="https://discourse.slicer.org/t/fiducial-markups-not-showing-in-4-11-0/6501/6">here</a>). You can either switch to a recent Slicer Preview Release or enable 2D visibility for the fiducials manually (by right-clicking on the eye icon of the markups node in Data module).</p>

---

## Post #3 by @njeffery123 (2021-04-23 18:17 UTC)

<p>Fab, thanks Andras. That worked - I can see them!</p>
<p>I did do a search for the problem but didn’t find your earlier post to Radek’s query - apologies for making you repeat!</p>
<p>Loving the additional markup functions<br>
cheers<br>
Nathan</p>

---
