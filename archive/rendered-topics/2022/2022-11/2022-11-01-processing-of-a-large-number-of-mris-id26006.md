# Processing of a large number of MRIs

**Topic ID**: 26006
**Date**: 2022-11-01
**URL**: https://discourse.slicer.org/t/processing-of-a-large-number-of-mris/26006

---

## Post #1 by @tsinesh (2022-11-01 17:09 UTC)

<p>How can I perform an analysis on a large data set with e.g. 800 MRIs? I imagine to process all images uniformly as far as possible automatically in a loop: e.g.</p>
<ul>
<li>N4 homogenization algorithm for MRI Bias Field Correction</li>
<li>LaplacianSharpeningImageFilter to enhance edges</li>
<li>Vesselness filter</li>
<li>manual step: local threshold to extract arteries</li>
<li>manual step: starting points for</li>
<li>centerline</li>
<li>saving of results</li>
</ul>
<p>With the Pipeline Case Iterator plugin, no filters or the N4 algorithm are available to me.</p>
<p>How can I implement such an analysis pipeline? Is it possible without Python programming knowledge? Is there sample code for something like this?</p>

---
