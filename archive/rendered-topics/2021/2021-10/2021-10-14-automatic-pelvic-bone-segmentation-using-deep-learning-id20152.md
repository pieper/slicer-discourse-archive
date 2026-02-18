# Automatic Pelvic bone segmentation using deep learning

**Topic ID**: 20152
**Date**: 2021-10-14
**URL**: https://discourse.slicer.org/t/automatic-pelvic-bone-segmentation-using-deep-learning/20152

---

## Post #1 by @AMK (2021-10-14 14:50 UTC)

<p>Hi,</p>
<p>I am trying to segment pelvic region using deep learning. During my research for open-source data, I found a github link to this page.<br>
<a href="https://github.com/ICT-MIRACLE-lab/CTPelvic1K" rel="noopener nofollow ugc">ICT-MIRACLE-lab/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models”. (github.com)</a></p>
<p>This link provides everything required for my initial development. I now want to test my own CT data. But I am not sure how to do this model inference in Slicer. My data is in DICOM format.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-10-14 16:07 UTC)

<p>Probably the easiest for testing would be to load the dicom data in slicer and export it in whatever format the python code requires (probably nii or similar) and then run the code outside of slicer and load the results back for visualization.  You may need to work with the authors of that model to learn how to run it.  From a quick look that code looks good, but it was set up for the publication but not as a ready to use tool without more work.</p>

---
