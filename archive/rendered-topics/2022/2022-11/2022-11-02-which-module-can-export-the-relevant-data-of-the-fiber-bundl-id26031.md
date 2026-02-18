# Which module can export the relevant data of the fiber bundle，which created using UKF tractography

**Topic ID**: 26031
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/which-module-can-export-the-relevant-data-of-the-fiber-bundle-which-created-using-ukf-tractography/26031

---

## Post #1 by @Joshuazzzs (2022-11-02 11:53 UTC)

<p>Hi!<br>
We use the UKF tractography module to creat the neural fibers. Which module can export the relevant data of the fiber bundle, as in the following image, generate a table directly…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1fa535324410dd332cb48bc3771ebeaa93965f8.jpeg" data-download-href="/uploads/short-url/tXy6TtLyg0xjIP95E4VkHdmxPzW.jpeg?dl=1" title="922e2f6638eb83fae5237475b6ac5bf" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1fa535324410dd332cb48bc3771ebeaa93965f8_2_690x368.jpeg" alt="922e2f6638eb83fae5237475b6ac5bf" data-base62-sha1="tXy6TtLyg0xjIP95E4VkHdmxPzW" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1fa535324410dd332cb48bc3771ebeaa93965f8_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1fa535324410dd332cb48bc3771ebeaa93965f8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1fa535324410dd332cb48bc3771ebeaa93965f8.jpeg 2x" data-dominant-color="DDDADA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">922e2f6638eb83fae5237475b6ac5bf</span><span class="informations">1024×547 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-11-02 23:57 UTC)

<p>It looks like you need these instructions:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md" target="_blank" rel="noopener">SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md</a></h4>


      <pre><code class="lang-md"># Tutorial

This tutorial explains how to perform whole-brain tractography parcellation using the [whitematteranalysis (WMA)](https://github.com/SlicerDMRI/whitematteranalysis) software and the anatomically curated [O'Donnell Research Group (ORG)](http://dmri.slicer.org/atlases/) white matter atlas.

On this page, we provide step-by-step instructions to guide a user to run the entire tractography parcellation pipeline for **_an individual subject_**.

   &gt; We also provide a master shell script ```wm_apply_ORG_atlas_to_subject.sh``` (see documentation [here](https://github.com/SlicerDMRI/whitematteranalysis/blob/73a7948751f49d9fda8ec84fb5caeecaeeb92621/bin/wm_apply_ORG_atlas_to_subject.sh#L1-L40)) that enables running the whole pipeline in one command. However, we recommend the users to run through the following step-by-step tutorial first to get familiar with the whole fiber clustering pipeline.
   
   &gt; Note: ```wm_apply_ORG_atlas_to_subject.sh``` provides options to remove intermediate files to save disk space.

## 1. Software prerequisites
   - Install [3D Slicer](https://download.slicer.org/)
      &gt; 3D Slicer is an open source software platform for medical image informatics, image processing, and three-dimensional visualization.
   - Install [SlicerDMRI](http://dmri.slicer.org/download/)
      &gt; SlicerDMRI is an open-source project to improve and extend diffusion magnetic resonance imaging software in 3D Slicer.
   - Install [whitematteranalysis (WMA)](https://github.com/SlicerDMRI/whitematteranalysis#wma-installation)
      &gt; WMA is an open source software package for data-driven fiber clustering white matter parcellation.
    
## 2. Download tutorial data
   - Download the tutorial data package ([WMA_tutorial_data.zip](https://www.dropbox.com/s/beju3c0g9jqw5uj/WMA_tutorial_data.zip?dl=0), ~2.5GB)
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
