---
topic_id: 28289
title: "Dicom To Rectilinear Grid Vtk"
date: 2023-03-10
url: https://discourse.slicer.org/t/28289
---

# Dicom to rectilinear grid vtk

**Topic ID**: 28289
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/dicom-to-rectilinear-grid-vtk/28289

---

## Post #1 by @fil (2023-03-10 20:18 UTC)

<p>How can I create rectilinear grid .vtk file from DICOM flies, please? I used to be able to do this using slicer. Any help will be much appreciated. Thank you.</p>

---

## Post #2 by @lassoan (2023-03-11 07:02 UTC)

<p>You can load the DICOM image and then when you save it choose the .vtk file format. You will see a warning because .vtk file format cannot store image axis directions, but the file is still saved.</p>

---

## Post #3 by @fil (2023-03-11 12:18 UTC)

<p>Thank you for your answer. I have tried this and is giving me structured grid vtk file not a rectilinear grid. What I need is rectilinear grid vtk file. Thank you</p>

---

## Post #4 by @lassoan (2023-03-11 16:18 UTC)

<p>VTK files are confusing because they may store many types of data. What would you actually like to save: a labelmap image, a surface mesh, or a volumetric mesh?</p>

---

## Post #5 by @fil (2023-03-11 16:32 UTC)

<p>They are DICOM files.</p>

---

## Post #6 by @lassoan (2023-03-11 16:39 UTC)

<p>You import DICOM files into Slicer. What would you like to then save - a grayscale image, a label image, a surface mesh, or a volumetric mesh? What software will use that file and how?</p>

---

## Post #7 by @fil (2023-03-11 17:59 UTC)

<p>I need a VTK rectilinear grid to use it in bonemat software. I suppose is a gray scale image as I need the gray scale.<br>
Thank you</p>

---

## Post #8 by @lassoan (2023-03-12 20:22 UTC)

<p>Bonemat can load the image that you saved in .vtk format.</p>
<p>Saving in Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0021014163775d1985d8a9609b87ae60476a1cf3.png" data-download-href="/uploads/short-url/18IbxLqMJCTZTOtW1eWNqPKXdx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0021014163775d1985d8a9609b87ae60476a1cf3_2_690x351.png" alt="image" data-base62-sha1="18IbxLqMJCTZTOtW1eWNqPKXdx" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0021014163775d1985d8a9609b87ae60476a1cf3_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0021014163775d1985d8a9609b87ae60476a1cf3_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0021014163775d1985d8a9609b87ae60476a1cf3.png 2x" data-dominant-color="383838"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1263×643 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Saved .vtk file loaded into bonemat and displayed in OrthoSlice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da628d47b59bb5dd7c7f63b6ca2742b0e22145c2.jpeg" data-download-href="/uploads/short-url/v9VezfEJr58RSQjk5K08n4N9LkC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da628d47b59bb5dd7c7f63b6ca2742b0e22145c2_2_665x500.jpeg" alt="image" data-base62-sha1="v9VezfEJr58RSQjk5K08n4N9LkC" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da628d47b59bb5dd7c7f63b6ca2742b0e22145c2_2_665x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da628d47b59bb5dd7c7f63b6ca2742b0e22145c2_2_997x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da628d47b59bb5dd7c7f63b6ca2742b0e22145c2_2_1330x1000.jpeg 2x" data-dominant-color="888B8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1558×1170 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2023-03-12 20:33 UTC)

<p>By the way, it seems that <a href="http://www.bonemat.org/downloads/Bonemat_manual.pdf">all that bonemat can do</a> you can already do in Slicer. For the parameter mapping from CT densities to mechanical properties you can use a few lines of Python code (or using <a href="https://pypi.org/project/py_bonemat_abaqus/">py_bonemat_abaqus</a>). The license of bonemat is quite restrictive and you can do so much more in Slicer that I would recommend to consider using just Slicer for your workflow.</p>

---

## Post #10 by @fil (2023-03-13 10:11 UTC)

<p>I was unaware that Slicer could map material properties from CT scan data as I am unfamiliar with this software. For example, I used Slicer to create a rectilinear grid vtk file, but now it only makes a structured grid vtk file. Please direct me on how Slicer can do this. Also, is the resulting file with mapped materials compatible with Abaqus software? Also, I am not that familiar with Python code.<br>
In Bonemat, I can see this file, but it is not mapping anything on my mesh. The error I get is “scalar visibility: false”. I have looked to see how to fix this error, but I need help finding something.<br>
On the other hand, I used pybonemat for Abaqus, which looks like a better variant than Bonemat. However, I have tried with both vtk and DICOM files, and I got the following errors:<br>
“AttributeError: Dataset does not have attribute ‘ImagePositionPatient’.”<br>
“ValueError: Error reading VTK header, unrecognised format” the vtk file was created with Slicer.<br>
Thank you very much for your help.</p>

---
