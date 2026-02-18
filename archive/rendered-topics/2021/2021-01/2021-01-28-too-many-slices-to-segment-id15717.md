# Too many slices to segment

**Topic ID**: 15717
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/too-many-slices-to-segment/15717

---

## Post #1 by @vidyakar555 (2021-01-28 16:26 UTC)

<p>Hi, I am new to the community.</p>
<p>I am facing an issue with a discrepancy in the number of slices while segmentation. The MRI sequence has 23 slices as per volume information (and also if I open it any other software like ITK-SNAP or RADIANT viewer) but there are numerous (nearly several hundreds) while scrolling through to segment.<br>
Also the slices don’t seem discrete, there seems to be overlap between them when I scroll down to the next slice.</p>
<p>Anyone faced a similar challenge?<br>
Would appreciate your help!</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-01-28 16:43 UTC)

<p>Probably your image axes are not aligned with patient anatomical axes, so you are browsing an MPR view. Click <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">Rotate to volume plane</a> button to align the image viewer to the volume axes.</p>
<p>In contrast to RadiANT and ITK-Snap, which primarily operate in a single volume’s image space, in 3D Slicer all the tools operate in 3D physical space, regardless of how many volumes, models, or other objects you have loaded. We understand that this is not expected by users coming from more limited platforms and we will change the default behavior accordingly to be more friendly to newcomers. We already have a ticket for this specific issue (align slice views to the first loaded volume or maybe each time you drag-and-drop a volume from the data tree into a view - see <a href="https://github.com/Slicer/Slicer/issues/5379" class="inline-onebox">Make slice views aligned with image axes by default · Issue #5379 · Slicer/Slicer · GitHub</a>).</p>
<p>We would be happy to answer any additional questions you may have or suggestions that would make Slicer more intuitive for you.</p>

---

## Post #3 by @vidyakar555 (2021-02-07 18:49 UTC)

<p>Thanks a lot! Was point on</p>

---

## Post #4 by @lassoan (2021-02-07 18:59 UTC)

<p>Thanks for the update. In the meantime, we’ve implemented a <a href="https://github.com/Slicer/Slicer/issues/5379"><code>#5379</code></a>: in latest Slicer Preview Releases we align slice views to volume axes by default.</p>

---
