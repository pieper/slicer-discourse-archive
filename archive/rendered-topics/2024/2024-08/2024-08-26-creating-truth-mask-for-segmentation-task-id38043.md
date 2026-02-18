# Creating Truth Mask for Segmentation Task

**Topic ID**: 38043
**Date**: 2024-08-26
**URL**: https://discourse.slicer.org/t/creating-truth-mask-for-segmentation-task/38043

---

## Post #1 by @Marcellofabrizio (2024-08-26 21:54 UTC)

<p><strong>Hello everyone!</strong></p>
<p>I’m a Computer Science student currently working on a research project focused on segmenting root canals using DICOM images. My approach involves using a U-Net combined with DenseNet-121. I have access to 81 scans, and I’m aiming to achieve something similar to this paper: <a href="https://www.nature.com/articles/s41598-024-62211-y" rel="noopener nofollow ugc">Link to Paper</a>.</p>
<p>At the moment, I’m extracting each slice from the DICOM files into PNG format and manually segmenting them with the assistance of a dentistry student. However, this process is extremely labor-intensive and seems less than ideal, especially since it results in a loss of the 3D context.</p>
<p>I’m considering using Slicer to perform the segmentation directly on the DICOM images and then exporting the segmentation masks for use with the model. However, I’m not entirely sure how to approach this and would greatly appreciate any advice on exporting these masks in a format to train the U-Net + DenseNet-121 model.</p>
<p>Any insights, tips, or resources would be incredibly helpful!</p>
<p><strong>Thank you so much!</strong></p>

---

## Post #2 by @lassoan (2024-08-26 21:59 UTC)

<p>Segmenting 2D slices one by one sounds very inefficient and could be potentially very inaccurate. Instead, you could start with 3D segmentation of all the teeth fully automatically, using an already trained model, such as <a href="https://github.com/gaudot/SlicerDentalSegmentator">DentalSegmentator</a>. You may then find the root canal within each tooth with classic manual or semi-automatic 3D segmentation tools.</p>

---

## Post #3 by @Marcellofabrizio (2024-08-26 23:35 UTC)

<p><strong>Thanks for the reply!</strong></p>
<p>I realize I wasn’t entirely clear in my initial post. While I mentioned wanting to segment “root canals,” I’m actually focusing on a specific one, known as the “Mesio-Buccal 2” canal. I’ve highlighted it here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13053f3473dc689ff1866721e0565fa76dbfa2d2.jpeg" data-download-href="/uploads/short-url/2IgjqxP6EAsxDHkPYjIdtdbnDJU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13053f3473dc689ff1866721e0565fa76dbfa2d2_2_690x327.jpeg" alt="image" data-base62-sha1="2IgjqxP6EAsxDHkPYjIdtdbnDJU" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13053f3473dc689ff1866721e0565fa76dbfa2d2_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13053f3473dc689ff1866721e0565fa76dbfa2d2_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13053f3473dc689ff1866721e0565fa76dbfa2d2_2_1380x654.jpeg 2x" data-dominant-color="B6B4B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×905 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The segmentation was exported as an NRRD file, which I believe contains the 3D information related to the segmentation. Is that correct?</p>
<p>This might be a bit more technical, but with this NRRD file, would it be possible to use it as the ground truth mask for the model I’ve developed?</p>

---
