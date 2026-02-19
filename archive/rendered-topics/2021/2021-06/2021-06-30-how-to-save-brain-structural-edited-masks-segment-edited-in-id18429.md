---
topic_id: 18429
title: "How To Save Brain Structural Edited Masks Segment Edited In"
date: 2021-06-30
url: https://discourse.slicer.org/t/18429
---

# How to save brain structural edited masks (segment edited) in nifti for freesurfer use?

**Topic ID**: 18429
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/how-to-save-brain-structural-edited-masks-segment-edited-in-nifti-for-freesurfer-use/18429

---

## Post #1 by @Tamires_Zanao (2021-06-30 13:17 UTC)

<p>Hi! I automatically generated structural brain masks with the purpose of using FreeSurfer. The masks need some editing, and I used Slicer Segment Editor for it (opened mask as label &gt; imported labelmap as segmentation &gt; add T1 as master volume &gt; edited masks). However, I couldn’t save it as a nifti, so I saved as nrrd and later converted it to nifti. It didn’t work. How can I save my edited mask (in nifti) in order to use them for freesurfer? Do I have to convert the labelmap in something else?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-07-02 04:04 UTC)

<p>You can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">Export to file</a> feature in Segment Editor module. NIFTI export is available in the current Slicer Stable Release.</p>

---
