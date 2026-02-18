# Errors Importing CT files made with GE LightSpeed QXI 4

**Topic ID**: 10769
**Date**: 2020-03-21
**URL**: https://discourse.slicer.org/t/errors-importing-ct-files-made-with-ge-lightspeed-qxi-4/10769

---

## Post #1 by @FaceMaker (2020-03-21 03:23 UTC)

<p>Hello, I have been trying to import dicom files from ct-scan made with GE LightSpeed QXI 4.  I have researched the tutorials and information and researched the GE LightSpeed QXI 4.  The errors that occur are errors in spacing, geometry.  I get images that either look like aliens or like flattened heads.  None of the solutions I found work for me.  I downloaded the recommended extensions and it didn’t work, looked at the information in the Volumes module, etc.</p>
<p>This is an old ct-scan machine so I’m hoping someone already knows what to do to get a 3d object without distortions.</p>
<p>Is there a way to manually insert a space size for each slice?</p>
<p>I also found this formula for GE’s Lightspeed 64:<br>
64 x 0.625 mm (total z-axis length of 40 mm).</p>
<p>Would it be 4 x 0.625mm for GE LightSpeed QXI 4?</p>

---

## Post #2 by @lassoan (2020-03-21 13:53 UTC)

<p>See troubleshooting instructions in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">DICOM FAQ</a>. Let us know how they worked or send us anonymized/animal/phantom data set that we can inspect.</p>

---

## Post #3 by @pieper (2020-03-21 14:20 UTC)

<p>Also if you use a recent slicer you can enable acquisition geometry correction (to handle variable slice spacing).  It’s in Edit -&gt; Application Settings -&gt; DICOM tab.</p>

---

## Post #4 by @FaceMaker (2020-03-21 16:45 UTC)

<p>I did try this, it still looked distorted.  Will go through all the tutorials again.  Thank you for your help.</p>

---
