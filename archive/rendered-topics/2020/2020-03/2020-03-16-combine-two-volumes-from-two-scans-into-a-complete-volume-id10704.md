# Combine Two Volumes From Two Scans Into A Complete Volume

**Topic ID**: 10704
**Date**: 2020-03-16
**URL**: https://discourse.slicer.org/t/combine-two-volumes-from-two-scans-into-a-complete-volume/10704

---

## Post #1 by @Aryan_Ghazipour (2020-03-16 13:05 UTC)

<p>Hello,</p>
<p>I have a volume that was CT scanned two times. There are two DICOM series’, one for each half of the volume. I would like to display the complete volume, both halves, in Slicer. The goal is to align the two volumes and merge them together so that I can extract a particular slice from the complete volume.</p>
<p>Thanks in advance,<br>
Aryan</p>

---

## Post #2 by @pieper (2020-03-16 16:53 UTC)

<p>That should be doable.  Basic steps would be to align them first with a transform, if they overlap then you should be able to do this automatically but first manually.  Then you would use crop volume to add a margin to one half big enough for the whole thing and also to crop out overlap.  Then you can use the add scalar volumes module to put them together.</p>

---
