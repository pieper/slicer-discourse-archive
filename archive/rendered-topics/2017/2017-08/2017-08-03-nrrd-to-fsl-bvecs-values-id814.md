---
topic_id: 814
title: "Nrrd To Fsl Bvecs Values"
date: 2017-08-03
url: https://discourse.slicer.org/t/814
---

# NRRd to FSL bvecs values

**Topic ID**: 814
**Date**: 2017-08-03
**URL**: https://discourse.slicer.org/t/nrrd-to-fsl-bvecs-values/814

---

## Post #1 by @jfhartzell (2017-08-03 15:34 UTC)

<pre><code class="lang-auto">Operating system  : Mac OS Sierra 10.12.6
Slicer version    : 4.6.2 r25516
Expected behavior : correct bvecs output 
Actual behavior   : values of x and z vectors flipped from negative to positive or vice versa
</code></pre>
<p>Hi</p>
<p>After Slicer NIFTI to NRRD converson, then DTIPrep QC, and then Slicer NRRD to FSL (nii.gz) conversion, the output bvecs have the signs flipped in the x and z directions (the y direction is correct), i.e. formerly negative values are positive, and vice versa.</p>
<p>Is there a flag in Slicer DWIConvert to correct his automatically (and thereby avoid having to manually correct the bvecs)?</p>
<p>Cheers<br>
James</p>

---

## Post #2 by @hjmjohnson (2017-08-03 18:21 UTC)

<p>James,</p>
<p>We fixed this problem recently in DWIConvert, but we have not yet had a chance to integrate it into Slicer.  We will attempt to push the changes to Slicer in the next few weeks.</p>
<p>Hans</p>

---

## Post #3 by @jfhartzell (2017-08-04 12:14 UTC)

<p>Hans</p>
<p>Thanks for the update.  I ran DWIConvert from the command line, but it is<br>
the one currently integrated into the latest Slicer Download</p>
<p>4.6.2 r25516</p>
<p>Cheers</p>
<p>James</p>

---

## Post #4 by @ljod (2017-08-04 16:24 UTC)

<p>Thank you Hans we look forward to this update!</p>

---

## Post #5 by @Dani_Berge (2018-01-09 22:20 UTC)

<p>I still have the same problem both using DWIConvert within Slicer or standalone v1.2.4. In my case, the only flipped vector from nrrd to FSL is “y”. Also,  It seems that v1.2.8 for linux does not have DWIConvert when unpacked so I could not try with this latest update.<br>
Any news or way to fix it would be very appreciated.</p>
<p>Thanks.<br>
Otherwise: Anyone knows how to automatically flip this vector before or after converting to FSL?</p>

---
