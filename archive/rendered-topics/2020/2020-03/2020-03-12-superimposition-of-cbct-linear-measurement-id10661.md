# Superimposition of CBCT + linear measurement

**Topic ID**: 10661
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/superimposition-of-cbct-linear-measurement/10661

---

## Post #1 by @mariaelh (2020-03-12 16:12 UTC)

<p>Hello,</p>
<p>I am currently developing a research protocol which requires the superimposition of 2 CBCT scans of the maxilla or the mandible. I then need to measure the dimensional changes in the alveolar bone of a specific section/slice. The measurements should be linear. Is this possible with the 3D Slicer?<br>
Thanks,</p>
<p>Maria</p>

---

## Post #2 by @lassoan (2020-03-12 22:28 UTC)

<p>You can align register images automatically, using “General registration (Elastix)” module (provided by SlicerElastix extension) or semi-automatically using Fiducial Registration Wizard module (provided by SlicerIGT extension).</p>
<p>You can make distance measurements using Markups module (line tool) in recent Slicer Preview Releases (or using annotation rulers in Slicer-4.10).</p>
<p>If you need more information then search this forum or try Google and if you get stuck then let us know.</p>

---
