# Help synchronising Bruker SkyScan with CT

**Topic ID**: 31121
**Date**: 2023-08-13
**URL**: https://discourse.slicer.org/t/help-synchronising-bruker-skyscan-with-ct/31121

---

## Post #1 by @atay5510 (2023-08-13 10:34 UTC)

<p>I’m doing a project in which I’ll be scanning a cadaveric temporal bone specimen implanted with a cochlear implant electrode in a MicroCT (SkyScan) and a commercial helical/spiral CT.</p>
<p>I’d then like to take measurements of the distance of the electrode contacts with various anatomical landmarks, on both the MicroCT scan and the helical CT scan</p>
<p>In order to ensure I am measuring between the same landmarks on each scan, I’d like to synchronise the two scans with respect to orientation and position.</p>
<p>Is there a way that 3D slicer can do this automatically? Or will I need to manually adjust the planes of the scan to match each other (to the best of my judgement).</p>
<p>Many thanks in advance.</p>

---

## Post #2 by @muratmaga (2023-08-14 17:13 UTC)

<p>What you describe is called co-registration. If you are going to rely on landmarks to co-register the helical and microCT scan of the same cochlea, then you can use the Fiducial Landmark Wizard tool in the SlicerIGT extension. Place your landmarks first in one scan, and then place them in the other scan in the same order, and choose to do a rigid alignment. See this tutorial.</p>
<p><a href="https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!24624&amp;ithint=file%2cpptx&amp;authkey=!AJlO_xg84-IhsVo" rel="noopener nofollow ugc">SlicerIGT-U12_LandmarkRegistration.pptx - Microsoft PowerPoint Online (live.com)</a></p>

---
