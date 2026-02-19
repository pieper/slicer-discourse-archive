---
topic_id: 8112
title: "Extracting Diffusion Tensor From Dti Images"
date: 2019-08-21
url: https://discourse.slicer.org/t/8112
---

# Extracting diffusion tensor from DTI images 

**Topic ID**: 8112
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/extracting-diffusion-tensor-from-dti-images/8112

---

## Post #1 by @mshah (2019-08-21 00:03 UTC)

<p>Hi everyone,</p>
<p>I’m having a lot of trouble with the software so far. I am trying to a) visualize the tensor field of dti images and b) extract the 3x3 tensor matrix from each voxel of the images (or directly the eigenvalues of the matrix). In the tutorials online, it seems that they focus on converting the DWI image to DTI, then working from there. I keep getting errors (b0 not detected) in the conversion and i do not have DWI images for all my patients. I would like to extract the information I need directly from loading the DTI images themselves onto the software. Is this possible? What is the protocol for this? Aditionally, I would need to convert the DTI images to nhdr, but would the DWI converter still work for this?</p>
<p>thanks!</p>

---

## Post #2 by @ljod (2019-08-21 00:28 UTC)

<p>Hi! You need to get the DWI images from the scanner to be able to do any sort of tensor or tractography analysis. What do you mean by DTI image? Do you actually mean your scanner computed tensors or is it a more typical FA or MD image?</p>

---

## Post #3 by @mshah (2019-08-21 05:10 UTC)

<p>Hi thank you for the response!</p>
<p>I mean that my data set consists of the Diffusion Tensor Images (DTI). I have taken these off of the TCGI data base, specifically the IvyGap data base. For the patients I am analyzing, I need all the diffusion tensors for each voxel at particular slices. If slicer focuses on taking the DWI image and estimating the DTI, why cant I directly use the DTI images? For reference I have attached the corresponding DWI and DTI images for a patient I’m interested in analyzing, patient W13 from the IvyGap data base. The problem is I only have DTI images for all the patients in my study, patient W13 is the only DWI set of images I have. Please let me know what I can do, its crucial to my study!</p>
<p><aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1RUM-YGp01-3h2YgCBsOEEjzZRL9wNGTp/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1RUM-YGp01-3h2YgCBsOEEjzZRL9wNGTp/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1RUM-YGp01-3h2YgCBsOEEjzZRL9wNGTp/view?usp=sharing" target="_blank" rel="nofollow noopener">5-AX EPI DTI-36289.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1oVaihj795rk-9Sqg7-gyuq9C5rOZTKgO/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1oVaihj795rk-9Sqg7-gyuq9C5rOZTKgO/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1oVaihj795rk-9Sqg7-gyuq9C5rOZTKgO/view?usp=sharing" target="_blank" rel="nofollow noopener">4-AX EPI DWI-45431.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Thank you so much</p>

---

## Post #4 by @ljod (2019-08-21 07:27 UTC)

<p>I see. This is an unusual use case because DTI is not generally provided. If you are able to convert the DTI to nrrd format DTI, Slicer can read that. If you open Slicer and  download sample data, there is an example tensor dataset for download. Alternatively to get an example, you can save a tensor dataset you’ve calculated in Slicer. The nrrd format is described here:</p>
<p><a href="http://teem.sourceforge.net/nrrd/format.html" class="onebox" target="_blank" rel="nofollow noopener">http://teem.sourceforge.net/nrrd/format.html</a></p>

---

## Post #5 by @mshah (2019-08-26 18:55 UTC)

<p>Hi, how would I do the conversion. Would I still need to use the DWIconverter to load as nrrd images even though they are not DWI images?</p>

---
