# What is the default co-ordinate system in nrrd files saved from Slicer?   

**Topic ID**: 2719
**Date**: 2018-04-27
**URL**: https://discourse.slicer.org/t/what-is-the-default-co-ordinate-system-in-nrrd-files-saved-from-slicer/2719

---

## Post #1 by @Krishna_Nanda (2018-04-27 14:43 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,</p>
<p>I have a quick question about the nrrd files saved from Slicer. Is the default nrrd co-ordinate system LPS? When and how could it be RAS?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2018-04-27 15:33 UTC)

<p>You can look at the ‘space’ field in the nrrd header.  Slicer uses ITK, which writes LPS.</p>
<p>The <a href="http://teem.sf.net/">sourceforge site</a> appears to be down right now, but the unu command should be able to change the space.</p>

---
