# Conversion of DICOM to STL using 3D Slicer

**Topic ID**: 1810
**Date**: 2018-01-10
**URL**: https://discourse.slicer.org/t/conversion-of-dicom-to-stl-using-3d-slicer/1810

---

## Post #1 by @klintx211 (2018-01-10 20:17 UTC)

<p>I’ve seen tutorials on converting a set of DICOM files to a 3D STL model. Many recommend using 3D Slicer. 3D Slicer takes in DICOM files but returns an NRRD file instead of an STL. My question is what exactly did 3D Slicer do to my DICOMs and what exactly does an NRRD file contain? Is NRRD an 3D model or is it still 2D? And does the NRRD file contains segmented DICOMs or unsegmented DICOMs? Please help me out.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @cpinter (2018-01-10 20:40 UTC)

<p>NRRD is binary labelmap (a 3D image), and STL is a surface mesh. This tutorial shows you how to make an STL file from a segmentation of anatomical images:</p><aside class="quote quote-modified" data-post="1" data-topic="700">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-video-tutorial-for-segment-editor-lumbar-spine-segmentation-for-3d-printing/700">New video tutorial for Segment editor - lumbar spine segmentation for 3D printing</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is the first part of a video tutorial series that teaches how to use Segment editor. This tutorial explains how to create a 3D-printable lumbar spine segment that can be used for lumbar puncture training: 

The video tutorial was created by Hilary Lia (PerkLab, Queen’s University), with help from <a class="mention" href="/u/cpinter">@cpinter</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/ungi">@ungi</a>. 
Please post your comments here about how useful this tutorial format is, what did you like/what to improve, what topics/techniques/anatomical structures you would be int…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2018-01-11 04:42 UTC)

<p>There are also some more segmentation tutorials on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">Slicer training page</a>.</p>

---
