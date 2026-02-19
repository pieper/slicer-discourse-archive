---
topic_id: 4650
title: "Some Problems With 3Dslicer Shape Analysis Mancova"
date: 2018-11-06
url: https://discourse.slicer.org/t/4650
---

# Some problems with 3Dslicer shape analysis-MANCOVA

**Topic ID**: 4650
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/some-problems-with-3dslicer-shape-analysis-mancova/4650

---

## Post #1 by @HanZhuang (2018-11-06 02:51 UTC)

<p>Operating system:Linux 14.04 LTS<br>
Slicer version:Slicer-4.8.1-linux-amd64</p>
<p>Expected behavior:<br>
Recently, I am using 3D Slicer to do morphological analysis of brain structure.What I expected was that all the images put in can get the expected result after SPHARM- PDM.</p>
<p>Actual behavior:<br>
In the data processing, I encountered some problems. For example, a manually segmented image, where data number is 12 stuck in step 1: GenParaMesh. In the image data segmented by Freesurfer, such as NO.023, completed with errors will be shown, but the next task will continue.I didn’t find the problem.If it is convenient for you, could you help me? In the attachment, I attached some data and pictures.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4b24911bb359293ae94ed4a4c3e61745bbb4e90.png" data-download-href="/uploads/short-url/nuYhm0wbUbjlpKMnBMCyvau2Y9y.png?dl=1" title="02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b24911bb359293ae94ed4a4c3e61745bbb4e90_2_690x396.png" alt="02" data-base62-sha1="nuYhm0wbUbjlpKMnBMCyvau2Y9y" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b24911bb359293ae94ed4a4c3e61745bbb4e90_2_690x396.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b24911bb359293ae94ed4a4c3e61745bbb4e90_2_1035x594.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4b24911bb359293ae94ed4a4c3e61745bbb4e90_2_1380x792.png 2x" data-dominant-color="7E828C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02</span><span class="informations">1839×1056 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @bpaniagua (2018-11-07 14:34 UTC)

<p>Hi HanZhuang,</p>
<p>Thank you for your interest in SPHARM-PDM and SlicerSALT.</p>
<p>Can you please let us know what is the message in the error log?  You can access the error log through the menu View &gt;&gt; Error Log or by pressing Crtl+0.</p>
<p>Also, what does the segmentation that fails look like?<br>
You can inspect them via the DataImporter in SlicerSALT or using Model Maker in Slicer.</p>
<p>Thank you,<br>
Beatriz</p>

---

## Post #3 by @HanZhuang (2018-11-08 07:06 UTC)

<p>In the Freesurfer segmented Putamen data, NC019-freesurfer-Putamen_L and NC023-freesurfer-Putamen_L are “completed with errors”, the error log says “no input provided”, show in Fig1.<br>
In the manually segmented Putamen data, NC012-manual-Putamen_L was stuck in Step 1：GenParaMesh, show in Fig2.</p>
<p>There is data in the links provided, “NC001-manual-putamen_l” can be run correctly, and “NC012-manual-putamen_L” prompts “completed with errors”, “NC019-freesurfer -Putamen_L” and “NC023-freesurfer -Putamen_L” prompts “completed with errors”.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfd7b93ff9fe6174e214a2221c254e38e97a0fe0.png" data-download-href="/uploads/short-url/vWcF1qmExL2RyPSPNN2gE6LEYgw.png?dl=1" title="Fig1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfd7b93ff9fe6174e214a2221c254e38e97a0fe0_2_690x396.png" alt="Fig1" data-base62-sha1="vWcF1qmExL2RyPSPNN2gE6LEYgw" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfd7b93ff9fe6174e214a2221c254e38e97a0fe0_2_690x396.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfd7b93ff9fe6174e214a2221c254e38e97a0fe0_2_1035x594.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfd7b93ff9fe6174e214a2221c254e38e97a0fe0_2_1380x792.png 2x" data-dominant-color="F0F1F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig1</span><span class="informations">1839×1056 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
