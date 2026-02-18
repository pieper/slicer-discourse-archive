# Segmenting the root canal space of the tooth

**Topic ID**: 33737
**Date**: 2024-01-11
**URL**: https://discourse.slicer.org/t/segmenting-the-root-canal-space-of-the-tooth/33737

---

## Post #1 by @Meso_Mazen (2024-01-11 17:07 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.6.1<br>
Expected behavior: segmenting and displaying the root canal space.<br>
Actual behavior: Segmenting the outline of the tooth as a whole.</p>

---

## Post #2 by @Meso_Mazen (2024-01-11 17:23 UTC)

<p>Dear colleagues,</p>
<p>I extend my gratitude for the consistent support provided on this platform.</p>
<p>I appreciate the assistance in handling the ISQ format, enabling me to visualize micro CT scans using 3D Slicer.</p>
<p>Upon importing an ISQ file from a single-tooth scan via the Scanco micro CT machine, I successfully segmented the tooth by choosing an appropriate threshold (refer to the attached 1st picture). However, for my research, I specifically require the outline of the root canal space (as depicted in the 2nd image). The goal is to export the file as an STL file for comparison with another STL file through superimposition. Is there a method to include both the outline of the root canal space and the outer tooth anatomy in a single STL file?</p>
<p>Thank you for your assistance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af5167e72aadb4e51c348fbdb6365b3ed011289b.jpeg" data-download-href="/uploads/short-url/p0VY3jd99GMZ2mBwPfSyABG0U79.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af5167e72aadb4e51c348fbdb6365b3ed011289b_2_690x363.jpeg" alt="image" data-base62-sha1="p0VY3jd99GMZ2mBwPfSyABG0U79" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af5167e72aadb4e51c348fbdb6365b3ed011289b_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af5167e72aadb4e51c348fbdb6365b3ed011289b_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af5167e72aadb4e51c348fbdb6365b3ed011289b_2_1380x726.jpeg 2x" data-dominant-color="98999A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1012 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29bfd8847296ac1f0b007026338013fc332dec37.jpeg" alt="image" data-base62-sha1="5XkBrBTje4ZwHDJmXUSgY0FCPFt" width="659" height="456"></p>

---

## Post #3 by @muratmaga (2024-01-11 20:34 UTC)

<p>I don;t think that’s possible with STL format. OBJ should be fine though.</p>

---

## Post #4 by @lassoan (2024-01-15 05:48 UTC)

<aside class="quote no-group" data-username="Meso_Mazen" data-post="2" data-topic="33737">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e9bcb4/48.png" class="avatar"> Meso_Mazen:</div>
<blockquote>
<p>The goal is to export the file as an STL file for comparison with another STL file through superimposition</p>
</blockquote>
</aside>
<p>Do you mean you want to visually compare meshes?<br>
Slicer offers lots of quantification, alignement, and comparison tools. If you describe what you want to achieve then we may be able to tell how to do it within Slicer.</p>

---

## Post #5 by @Meso_Mazen (2024-01-21 19:42 UTC)

<p>Thank you for the prompt reply. I’m interested in aligning two STL files. This involves preparing a space within the root canal to specific dimensions. One STL file is obtained through micro-CT scanning (used as a reference), while the other is obtained through direct digital scanning of the same tooth. My goal is to calculate the differences in distances between the two STL files (two meshes) and determine the root mean square. Additionally, I aim to compare the differences in distances at specific points throughout the entire space created inside the tooth.</p>
<p>CloudCompare software can perform these computations, however i can’t do so because when I import the segmented data from 3rd slicer into CloudCompare, the prepared space is not demarcated inside the tooth.</p>
<p>It would be highly beneficial if 3D Slicer had a feature that could exclusively segment the prepared space. This capability would enable a focused comparison with the other STL file.</p>

---

## Post #6 by @muratmaga (2024-01-21 21:57 UTC)

<p>This done through registration. There are number of different ways you can do this. The easiest might be the FastAlignModel within SlicerMorph extension.</p>
<p>after you load the both STLs, follow the tutorial example; <a href="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign" class="inline-onebox">Tutorials/FastModelAlign at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>You need to skip the scaling step, and do only a rigid alignment.</p>
<p>Or you can use a few anatomical landmarks, and do it through the Fiducial Registration Wizard in SlicerIGT extension.</p>

---
