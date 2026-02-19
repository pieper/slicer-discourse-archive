---
topic_id: 31256
title: "How To Export Segments As One Object With Colors"
date: 2023-08-21
url: https://discourse.slicer.org/t/31256
---

# How to export segments as one object with colors

**Topic ID**: 31256
**Date**: 2023-08-21
**URL**: https://discourse.slicer.org/t/how-to-export-segments-as-one-object-with-colors/31256

---

## Post #1 by @Mehdi_Khamesi (2023-08-21 11:01 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.2.2<br>
Expected behavior: Creating volumetric mesh<br>
Actual behavior: exporting few segment as one object with their colors</p>
<p>Hello everyone,</p>
<p>I want to import part of brain into COMSOL. There are four segments and I have tried it by exporting them into a STL file. But due to some defects in the interface of segments it seems impossible. So now, I want to have them all in one object in the STL file plus their colors. In fact, when I merge them, there wouldn’t be any fault with geometry. On the other hand, only by using their colors I can define their domains in COMSOL.</p>
<p>With this description, Do you have any suggestion?</p>
<p>Best wishes,<br>
Mehdi</p>

---

## Post #2 by @pieper (2023-08-21 12:37 UTC)

<p>STL format is very limited.  You might be able to use vtk format, and use the Segment Mesher extension to create a mesh more suited to simulation.</p>

---

## Post #3 by @Mehdi_Khamesi (2023-08-21 12:42 UTC)

<p>Thanks for your response.<br>
I have test it. COMSOL doesn’t support vtk format. Then I used meshio but it also doesn’t support msh or mesh files.</p>

---

## Post #4 by @pieper (2023-08-21 17:41 UTC)

<p>There is probably a path to convert using some off the shelf tools, but if you know what you need for COMSOL it’s probably easy to write a python script to generate the right format.  I don’t use COMSOL, but if you are a customer of theirs they should be able to help you with this.</p>

---

## Post #5 by @Mehdi_Khamesi (2023-08-22 07:33 UTC)

<p>Again thank you for your attention.</p>
<p>In fact, I have talked to COMSOL supporter but it is a problem from the input data. It easy can import a wide range of data such as STL, STEP, OBJ, and so on. But as you can see in the following picture there are some self intersecting faces (red points) around the model.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4154806db63a7fe00181e76e9d5e893aeb80811e.png" data-download-href="/uploads/short-url/9jW4VUmmCCf2WfCOLhDtpTDtiii.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4154806db63a7fe00181e76e9d5e893aeb80811e_2_690x363.png" alt="Untitled" data-base62-sha1="9jW4VUmmCCf2WfCOLhDtpTDtiii" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4154806db63a7fe00181e76e9d5e893aeb80811e_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4154806db63a7fe00181e76e9d5e893aeb80811e_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4154806db63a7fe00181e76e9d5e893aeb80811e_2_1380x726.png 2x" data-dominant-color="5D5D83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1513×797 75.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure but maybe Volume clipping has caused this problem in the final step.</p>
<p>So again want you or <a class="mention" href="/u/lassoan">@lassoan</a> to help me to get an output (preferable OBJ or STL) which can build these segments as one object while containing different colors as the representative of segments. Even a clue can be so beneficial for me.</p>
<p>I really appreciate your consideration.</p>
<p>Best wishes,<br>
Mehdi</p>

---

## Post #6 by @pieper (2023-08-22 15:33 UTC)

<p>The SegmentMesher has many options so you should really try that. <a href="https://github.com/lassoan/SlicerSegmentMesher" class="inline-onebox">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a></p>
<p>You may also want to try using the cleaver or tetgen tools directly.</p>

---
