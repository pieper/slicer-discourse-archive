---
topic_id: 16694
title: "Convert Nrrd To Nii Gz"
date: 2021-03-22
url: https://discourse.slicer.org/t/16694
---

# Convert nrrd to nii.gz

**Topic ID**: 16694
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/convert-nrrd-to-nii-gz/16694

---

## Post #1 by @Hball99 (2021-03-22 15:02 UTC)

<p>Hello there!</p>
<p>For a special use case, I need all my data in nii.gz format. Right now, I have 200+ CT-Volumes plus segmentations both stores in .nrrd data format. I could open each of those volumes/segmentations in 3D slicer manually and store them as nii.gz, but I am looking for a way to script that problem, so I don’t have to do it 200 times.</p>
<p>Since I am a newbie to that topic, I do not know where to start and I was wondering if you have any good ideas/known libraries/ways to script that problem within 3D slicer or outside 3D slicer.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2021-03-22 16:07 UTC)

<p>These scripts were written for diffusion images but should work for other volumes.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/3407942?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">pnlbwh/conversion</a></h3>


  <p><span class="label1">Various mri conversion/modification scripts. Contribute to pnlbwh/conversion development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>dcm2niix should also work.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/rordenlab/dcm2niix" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/22748159?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/rordenlab/dcm2niix" target="_blank" rel="noopener">rordenlab/dcm2niix</a></h3>


  <p><span class="label1">dcm2nii DICOM to NIfTI converter: compiled versions available from NITRC</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @dave3d (2021-03-22 20:32 UTC)

<p>Really easy to do in Python with SimpleITK.</p>
<pre><code>import SimpleITK as sitk

img = sitk.ReadImage("your_image.nrrd")
sitk.WriteImage(img, "your_image.nii.gz")
</code></pre>
<p>fin</p>

---
