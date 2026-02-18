# Irregular volume geometry detected when exporting DCM

**Topic ID**: 34947
**Date**: 2024-03-18
**URL**: https://discourse.slicer.org/t/irregular-volume-geometry-detected-when-exporting-dcm/34947

---

## Post #1 by @kkkkkkk123 (2024-03-18 09:59 UTC)

<p>Hello, I applied the Gaussian Blur Image Filter to a PET series and exported the result to DICOM. However, when I import the new series in the DICOM browser and load them into the Scene, an acquisition transform is generated with the following message:</p>
<pre><code class="lang-auto">[Python] Irregular volume geometry detected (maximum error of 635 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.
</code></pre>
<p>I think something in the geometry changed with the export?<br>
Does anyone knows why this happens and how to fix it?</p>

---

## Post #2 by @pieper (2024-03-18 15:05 UTC)

<p>Best would be to see if you can replicate this issue using public data.  Often that approach will help you narrow down what’s different about your use case, usually some aspect of the data that hasn’t been taken into account.</p>

---

## Post #3 by @kkkkkkk123 (2024-03-20 08:15 UTC)

<p>It seems like the issue remains, but not if I use CT, only when using PET</p>

---
