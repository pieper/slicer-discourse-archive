---
topic_id: 42698
title: "DTI Alps results are low, below 1"
date: 2025-04-26
url: https://discourse.slicer.org/t/42698
last_bumped: 2026-05-17T21:09:44.918Z
---

# DTI Alps results are low, below 1

**Topic ID**: 42698
**Date**: 2025-04-26
**URL**: https://discourse.slicer.org/t/dti-alps-results-are-low-below-1/42698

---

## Post #1 by @ecgt (2025-04-26 14:43 UTC)

<p>I am having low values for the index<br>
I did 40 controls and i have = 0.855±0.045<br>
I did the procedure explained in the web<br>
What am I doing wrong?</p>

---

## Post #2 by @Zhilang_Qiu (2025-06-02 23:46 UTC)

<p>Hi Eduardo, I have the same question – DTI-ALPS index calculated by Slicer are below 1. Have you found the answer yet? Thanks in advance!</p>

---

## Post #3 by @ecgt (2025-06-03 09:53 UTC)

<p>Dear Zhilang Qiu<br>
I emailed Mr Senra Filho and this is his answer<br>
I send him one of my cases but I did not receive an answer</p>
<p>Dear Dr. Gonzalez-Toledo,</p>
<p>Thank you very much for your kind message and for watching my presentation. I am truly honored by your interest in my work, and it is a great pleasure to hear from someone with such a distinguished career in neuroradiology.</p>
<p>Regarding the DTI-ALPS measurements you’ve obtained, I’m happy to assist as best I can. While I’m not fully sure yet what specific kind of help may be most useful, I’d be glad to look into the details with you and perhaps review the processing steps together. Please feel free to share more information on your workflow in 3D Slicer (e.g., preprocessing steps, ROI placement, study design and hypothesis), so I can better understand what may be influencing the values.</p>
<p>For further reading and comparison, I recommend reviewing the original studies that introduced and validated the ALPS index:</p>
<ul>
<li>
<p>Taoka et al. (2017). <em>Evaluation of glymphatic system activity with the diffusion MR technique: diffusion tensor image analysis along the perivascular space (DTI-ALPS) in Alzheimer’s disease cases.</em> <strong>Japanese Journal of Radiology</strong>. DOI: 10.1007/s11604-017-0617-z</p>
</li>
<li>
<p>Taoka et al. (2022). <em>Differentiation of idiopathic normal pressure hydrocephalus from Alzheimer’s disease using the DTI-ALPS index.</em> <strong>Frontiers in Neurology</strong>. DOI: 10.3389/fneur.2022.1010381</p>
</li>
</ul>
<p>These references might help to contextualize your findings and verify whether your values are within expected ranges for healthy controls.</p>
<p>Please let me know how I can be of help, and I’ll do my best to support your work.</p>
<p>With warm regards,<br>
<strong>Acsenra Senra Filho, PhD</strong><br>
Assistant Professor, State University of Campinas, Sao Paulo, Brazil</p>
<p>Let me know if you have some news</p>
<p>Eduardo</p>

---

## Post #5 by @Zhilang_Qiu (2025-06-03 16:35 UTC)

<p>Thank you, Dr. Gonzalez-Toledo! Happy to hear your reply. I’ll post it here if I find the answer.</p>
<p>Best,<br>
Zhilang</p>

---

## Post #6 by @ecgt (2025-06-20 17:30 UTC)

<p>Dr Senra Filho checked my file and results and found out that the low results were OK.<br>
We need our normals. In my case  0.855±0.045  (40 controls)</p>

---

## Post #7 by @Zhilang_Qiu (2026-03-23 19:16 UTC)

<p>Hi Eduardo,</p>
<p>Sorry for the very late reply, I just realized I had forgotten to respond to this question.</p>
<p>I had figured out the issue: a low DTI-ALPS value (&lt; 1.0) is typically not normal. The problem was caused by that we actually had exported four segmentations rather the aimed one (e.g., Assoc_L). The solution is to just turn off the other “eye” icons when exporting the aimed one. Please see the attached figure for illustration of the steps.</p>
<p>Best,<br>
Zhilang</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5e4062d95d63e229d2981a1f1e287b86fcd8d04.jpeg" data-download-href="/uploads/short-url/seCBgKdEIVXJ1GNVPUYQpFNKtIE.jpeg?dl=1" title="AAA" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5e4062d95d63e229d2981a1f1e287b86fcd8d04_2_690x388.jpeg" alt="AAA" data-base62-sha1="seCBgKdEIVXJ1GNVPUYQpFNKtIE" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5e4062d95d63e229d2981a1f1e287b86fcd8d04_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5e4062d95d63e229d2981a1f1e287b86fcd8d04_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5e4062d95d63e229d2981a1f1e287b86fcd8d04.jpeg 2x" data-dominant-color="EFF2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AAA</span><span class="informations">1280×720 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @ecgt (2026-03-23 22:39 UTC)

<p>Hi Zhilang</p>
<p>Thank you for remember me<br>
This is a very important issue!!<br>
You solved it !!<br>
\Thanks again</p>
<p>Eduardo</p>

---

## Post #9 by @Kessmat_Mostafa (2026-05-17 21:09 UTC)

<p>Thank you so much</p>
<p>I was gonna change my research topic because I couldnt figure out why the numbers werent making sense</p>
<p>Truly appreciate your help</p>

---
