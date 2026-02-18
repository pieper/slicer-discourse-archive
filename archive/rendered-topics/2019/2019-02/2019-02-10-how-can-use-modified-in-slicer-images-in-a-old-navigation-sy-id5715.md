# How can use modified in Slicer images in a old navigation system?...

**Topic ID**: 5715
**Date**: 2019-02-10
**URL**: https://discourse.slicer.org/t/how-can-use-modified-in-slicer-images-in-a-old-navigation-system/5715

---

## Post #1 by @ratuat (2019-02-10 02:34 UTC)

<p>Hi everyone! I ran into such a problem.</p>
<ol>
<li>
<p>How to merge MRI T1W series and tractography?</p>
</li>
<li>
<p>How to export the processed (merged with tractography, pointed ROI’s) in 3DSlicer study back into DICOM format so that it can be used in the navigation station (the old medtronic stealth station of 2004 year release).</p>
</li>
</ol>
<p>Thank you for your help!</p>

---

## Post #2 by @pieper (2019-02-11 15:15 UTC)

<p>It would be kind of ugly, but you should be able to convert the tracts into a volume (label map) and export that to DICOM that would load in the old stealth station.</p>

---
