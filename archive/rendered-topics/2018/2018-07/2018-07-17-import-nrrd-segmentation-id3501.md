# import nrrd segmentation

**Topic ID**: 3501
**Date**: 2018-07-17
**URL**: https://discourse.slicer.org/t/import-nrrd-segmentation/3501

---

## Post #1 by @margherita (2018-07-17 13:36 UTC)

<p>Hallo i’m new user and i have a problem in importing volume segmentation of lung lesions<br>
Exactly i’ve segmented and saved the leasions (the 4 files ) but i cannot reload them into slicer for editing them<br>
how can i do it<br>
thanks</p>

---

## Post #2 by @cpinter (2018-07-17 13:59 UTC)

<p>Based on the new description it is not obvious to me what the problem is exactly.</p>
<ul>
<li>What Slicer version do you use?</li>
<li>How did you segment the lesion? Using Segment Editor?</li>
<li>How did you save it?</li>
<li>How are you trying to load it?</li>
</ul>
<p>For reference, my answer in <a href="https://discourse.slicer.org/t/import-segmentation-from-model-is-too-coarse/2914/2">the thread</a> this question originally appeared:</p>
<blockquote>
<p>Import: drag&amp;drop nrrd on Slicer, and in the popup window, choose Segmentation in the Description column.</p>
<p>Export: if you want to export the segmentation as a single nrrd file (all segments in the same file, which means overlapping segments are not permitted), then you can export the segmentation into a labelmap in the Segmentations module or in the Data module by right-clicking the segmentation, then click the Save button and save the labelmap as an nrrd.</p>
<p>As a side note, next time please create a new topic instead of commenting a new question to an only tangentially related topic. Thanks!</p>
</blockquote>

---

## Post #3 by @lassoan (2019-03-01 13:56 UTC)

<p>3 posts were split to a new topic: <a href="/t/dicom-import-fails/5986">DICOM import fails</a></p>

---
