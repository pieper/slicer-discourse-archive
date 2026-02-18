# HounsField Units for CT scans

**Topic ID**: 33668
**Date**: 2024-01-08
**URL**: https://discourse.slicer.org/t/hounsfield-units-for-ct-scans/33668

---

## Post #1 by @Varsha (2024-01-08 12:24 UTC)

<p>Hi. I am trying to select a range of HU to work with my CT images (primarily because I want to visualise trabecular changes of the bone). Is selecting a threshold under “Segment Editor” the same as setting an HU range? Or is there a separate way to set this range. For example., I require an HU range of -150 to +1000. How should I go about doing this? Any help would be appreciated.</p>

---

## Post #2 by @hherhold (2024-01-08 12:37 UTC)

<p>The range of values in Segment Editor (and throughout Slicer) is whatever the absorbance values are in your volume - for a micro-CT volume, for example, a 16-bit scan would be 0-65535. For a medical CT scanner, those values would be in Hounsfeld units, so those are the values you would use when setting a threshold.</p>

---

## Post #3 by @Varsha (2024-01-08 13:13 UTC)

<p>Hi. Thank you so much for this. So it is my understanding that if I select a Threshold of -150 to +1000 under “Segment Editor” this is the same as setting an HU range of _150 to +1000?</p>

---

## Post #4 by @hherhold (2024-01-08 16:37 UTC)

<p>Yes, that is correct.</p>

---

## Post #5 by @Varsha (2024-01-09 08:56 UTC)

<p>Thank you so much! This has been very helpful.</p>

---

## Post #6 by @Danilo_Borja (2024-08-08 13:34 UTC)

<p>hello Varsha im looking to do same, in mandibular condyle pre post surgery can you please share the way yo do ti ?</p>

---
