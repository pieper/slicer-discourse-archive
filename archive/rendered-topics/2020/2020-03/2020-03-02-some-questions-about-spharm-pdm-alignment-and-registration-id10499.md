---
topic_id: 10499
title: "Some Questions About Spharm Pdm Alignment And Registration"
date: 2020-03-02
url: https://discourse.slicer.org/t/10499
---

# Some questions about SPHARM-PDM, alignment, and registration

**Topic ID**: 10499
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/some-questions-about-spharm-pdm-alignment-and-registration/10499

---

## Post #1 by @keven (2020-03-02 16:15 UTC)

<p>Dear experts :</p>
<p>Recently，I  read a paper, Clinical application of SPHARM-PDM to quantify temporomandibular joint osteoarthritis, which was published in the Computerized Medical Imaging and Graphics in 2011. This is a brilliant paper. It gives me a lot of inspiration.<br>
I am very interested in the SPHARM-PDM. Now I want to study the bone remodeling of the affected joint due to TMJ osteoarthropathy before and after the treatment. I think the SPHARM-PDM can help me to accurately analyze the bone remodeling of the TMJ. But I still have some questions about the analysis process of SPHARM-PDM, I hope I can get your answers or guidance. These are my questions:</p>
<ol>
<li>
<p>When I was reading the paper mentioned above, I found that “Alignment of all surfaces was performed using rigid Procrustes alignment” was needed after the segmentation of anatomic structures and the establishment of correspondence across all surfaces. I want to ask if the alignment is necessary? What is the purpose of the alignment? What is the specific way to achieve the rigid Procrustes alignment?</p>
</li>
<li>
<p>I want to calculate the corresponding point distance between the two models in 3D-Slicer. Is it necessary for me to complete the registration of the models after the establishment of correspondence across all surfaces by calculation of the SPHARM-PDM, and then calculate the corresponding point distance between the models? If so, which registration should I choose?</p>
</li>
</ol>
<p>I look forward to your reply.</p>

---

## Post #2 by @bpaniagua (2020-03-02 16:38 UTC)

<p>Dear Kaiwen,</p>
<p>Thanks for your interest in SPHARM.</p>
<blockquote>
<p>When I was reading the paper mentioned above, I found that “Alignment of all surfaces was performed using rigid Procrustes alignment” was needed after the segmentation of anatomic structures and the establishment of correspondence across all surfaces. I want to ask if the alignment is necessary? What is the purpose of the alignment? What is the specific way to achieve the rigid Procrustes alignment?</p>
</blockquote>
<p>Procrustes alignment is used to align shapes based on their geometry, since it uses information obtained from the SPHARM modeling process. You can perform procrustes alignment after you have ran SPHARM modeling in SlicerSALT. If you have pre-aligned segmentations and want to keep that positioning you just have to use the spharm models without alignment.</p>
<blockquote>
<p>I want to calculate the corresponding point distance between the two models in 3D-Slicer. Is it necessary for me to complete the registration of the models after the establishment of correspondence across all surfaces by calculation of the SPHARM-PDM, and then calculate the corresponding point distance between the models? If so, which registration should I choose?</p>
</blockquote>
<p>You can calculate corresponding point to point distances using the <a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/ModelToModelDistance">Model to Model distance module.</a> AFTER you have computed and quality controlled SPHARM-PDM models. Same thing about registration I mentioned earlier applies here.</p>
<p>Additional great training resources can be found in the <a href="https://www.youtube.com/user/DCBIA">DCBIA youtube channel</a>, where Lucia Cevidanes and her team (<a href="https://discourse.slicer.org/c/community/slicercmf/13">associated project SlicerCMF</a>) teach how to use 3DSlicer modules for processing of CMF images.</p>
<p>I hope that helps!<br>
Bea</p>

---

## Post #3 by @keven (2020-03-02 16:55 UTC)

<p>Dear Beatriz Paniagua，<br>
Thanks for your reply. Your answers are very helpful.<br>
I would like to ask more：<br>
Does “alignment” and “registration” mean the same thing? Which module can be used in 3D-Slicer to achieve the alignment?<br>
I look forward to your reply.</p>

---

## Post #4 by @lili-yu22 (2021-07-03 05:26 UTC)

<p>l want to know the difference，too</p>

---

## Post #5 by @lili-yu22 (2021-07-08 06:59 UTC)

<p>Dear experts：<br>
when I ran SPHARM modeling ， I want to know the 6-DOF after rigid Procrustes alignment, but  which file contain the transform?</p>

---

## Post #6 by @lili-yu22 (2021-07-29 08:21 UTC)

<p>thank you expert.“You can perform procrustes alignment after you have ran SPHARM modeling in SlicerSALT”, the procrustes alignment is Rigid Alignment as the picture? can you give me detailed process?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0eff817e0bd74242d3b089c01dd28dd4a6c97ea.jpeg" data-download-href="/uploads/short-url/mXIwEK4I0wr0Mt8UkaMKDgfKSZc.jpeg?dl=1" title="IMG_20210729_160256_edit_61794221693695" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0eff817e0bd74242d3b089c01dd28dd4a6c97ea_2_690x303.jpeg" alt="IMG_20210729_160256_edit_61794221693695" data-base62-sha1="mXIwEK4I0wr0Mt8UkaMKDgfKSZc" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0eff817e0bd74242d3b089c01dd28dd4a6c97ea_2_690x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0eff817e0bd74242d3b089c01dd28dd4a6c97ea_2_1035x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0eff817e0bd74242d3b089c01dd28dd4a6c97ea_2_1380x606.jpeg 2x" data-dominant-color="7C80A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20210729_160256_edit_61794221693695</span><span class="informations">1920×845 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
