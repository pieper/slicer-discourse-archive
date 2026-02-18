# Need help with volumetric analysis on dental CBCT's

**Topic ID**: 3284
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/need-help-with-volumetric-analysis-on-dental-cbcts/3284

---

## Post #1 by @JBouwer (2018-06-25 16:41 UTC)

<p>Hi there, I am totally new to slicer and would like to use it for a research study where volumetric changes of alveolar bone is measured before and after grafting.  I have gone through the tutorials and there is a quantitative imaging tutorial, however this is only helpful in measuring volumetric change in pathologic lesions with well circumscribed margins.  I basically need to align and superimpose two dicom images T1 and T2 and measure horizontal and vertical difference between the two over a defined area, an extraction socket.  I would greatly appreciate it if someone could point me in the right direction.</p>

---

## Post #2 by @cpinter (2018-06-25 17:13 UTC)

<p>Aligning two images is called registration. You can use the BRAINS General Registration module or the Slicer Elastix extension to register the images. Both work well, but Elastix needs less parameter tuning, so it’s somewhat more automatic.</p>
<p>Once you have the two images registered you can segment the two sockets using the Segment Editor module and then do measurements in Segment Statistics.</p>
<p>You can find many tutorials for both steps, but let us know if you’re stuck.</p>

---

## Post #3 by @JBouwer (2018-06-26 16:15 UTC)

<p>Hi there,</p>
<p>Thank you for your response.  Can you direct me with any online links as I have browsed the tutorial area for image registration but most are for Cranial MRI’s.  I am looking to register 2 small field of view dental CBCT’s and measure hard tissue changes.</p>
<p>Thank you</p>
<p>Jonathan</p>

---
