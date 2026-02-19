---
topic_id: 36806
title: "Automated Pyradiomics Feature Work With Dicom Input Image Vo"
date: 2024-06-15
url: https://discourse.slicer.org/t/36806
---

# Automated PyRadiomics Feature work with DICOM(input image volume) and DICOM RT structure (input regions)

**Topic ID**: 36806
**Date**: 2024-06-15
**URL**: https://discourse.slicer.org/t/automated-pyradiomics-feature-work-with-dicom-input-image-volume-and-dicom-rt-structure-input-regions/36806

---

## Post #1 by @youngchanseo (2024-06-15 14:13 UTC)

<p>Hello.</p>
<p>I have already installed pyradiomics and Slicer RT via extension manager.</p>
<p>In the DICOM RT structure file, there are contour data for regions of interest (ROIs) [1]) of the tumor shape.<br>
In the DICOM file, I have an MRI of the patient.<br>
I searched for Radiomics in the 3d slicer’s module and ran it. I put the DICOM RT file in the “input regions” and the MR image in the “Input Image Volume”.<br>
As shown in the image below, I was able to successfully extract the Radiomics Features from the MR image of the ROI (Tumor).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287.jpeg" data-download-href="/uploads/short-url/xdJaCbALZcW307ZZZENt5cjS62P.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_483x500.jpeg" alt="image" data-base62-sha1="xdJaCbALZcW307ZZZENt5cjS62P" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_483x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_724x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_966x1000.jpeg 2x" data-dominant-color="3C3B58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×1207 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here I have two questions</p>
<ol>
<li>
<p>the features and calculated values are displayed in a table, but is it possible to export them to an excel file?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4119646bebdb610ab4d9f6037e01f91a7520cd2b.png" data-download-href="/uploads/short-url/9hTraI8h1BRif5NDG8hj7WNFZH5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4119646bebdb610ab4d9f6037e01f91a7520cd2b_2_690x297.png" alt="image" data-base62-sha1="9hTraI8h1BRif5NDG8hj7WNFZH5" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4119646bebdb610ab4d9f6037e01f91a7520cd2b_2_690x297.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4119646bebdb610ab4d9f6037e01f91a7520cd2b_2_1035x445.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4119646bebdb610ab4d9f6037e01f91a7520cd2b_2_1380x594.png 2x" data-dominant-color="C1C2C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1533×661 40 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>i need to do these operations multiple times. So I want to do these labor intensive things automatically.<br>
Is it possible to automate this with python code?<br>
For example, I have 100 RT structure (outlined tumor regions) DICOM files and 100 DICOM (MR brain) images, can I use code to automatically extract features in pyRadiomics &amp; 3d slicer to do the work at once?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419.png" data-download-href="/uploads/short-url/3B3UGvw9q0PfN2II0BuV6m8sZWV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419_2_690x337.png" alt="image" data-base62-sha1="3B3UGvw9q0PfN2II0BuV6m8sZWV" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419.png 2x" data-dominant-color="C9C6CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">995×486 75.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>[1] <a href="https://kr.mathworks.com/help/images/create-and-display-3-d-mask-of-dicom-rt-contour-data.html" class="inline-onebox" rel="noopener nofollow ugc">Create and Display 3-D Mask of DICOM-RT Contour Data - MATLAB &amp; Simulink - MathWorks 한국</a></p>

---

## Post #2 by @cpinter (2024-06-17 08:42 UTC)

<ol>
<li>Click on the save button, only select the table node, then choose either csv or tsv, and save. You can open it in Excel</li>
<li>Yes. I suggest starting from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> and look at the code of Slicer and the extension itself when in doubt. The forum contains a lot of topics about python automation of certain workflows as well.</li>
</ol>

---
