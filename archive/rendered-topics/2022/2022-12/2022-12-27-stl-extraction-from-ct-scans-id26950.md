# STL Extraction from CT scans

**Topic ID**: 26950
**Date**: 2022-12-27
**URL**: https://discourse.slicer.org/t/stl-extraction-from-ct-scans/26950

---

## Post #1 by @detroitkiddo (2022-12-27 23:22 UTC)

<p>Hello all,</p>
<p>I am new to the forums and I am reaching out to ask a question regarding segmentation and 3D STL extractions from CT scans compared to MRIs. So far I am had no issues trying to extract the ventricular system (lateral and third) using MRI DICOM scans. However when I try to do the same with CT scans instead the quality is extremely bad and results in very poor 3D renders of the ventricular system. I am able to get great 3D renders of the skull using CT scans but extremely bad renders for the ventricles.</p>
<p>I wanted to ask if using CT scans for the ventricular system is just not possible and I am better off with MRIs or if perhaps I am using the wrong settings for CT scans. Currently for MRIs I use the segmentation tools with the right threshold to get my lateral and third ventricles and I am able to make perfect 3D models. When I apply the same technique with CTs it is extremely bad even with varied threshold settings.</p>
<p>Thank you all for the feedback!</p>

---

## Post #2 by @pieper (2022-12-27 23:51 UTC)

<p>Yes, CT provides less soft tissue contrast than MR.  I would suggest trying <a href="https://github.com/BBillot/SynthSeg">SynthSeg</a> on your CT.  It’s not available directly in Slicer but you can run it outside and easily load the results.</p>

---
