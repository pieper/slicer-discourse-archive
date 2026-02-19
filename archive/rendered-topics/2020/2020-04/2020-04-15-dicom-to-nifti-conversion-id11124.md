---
topic_id: 11124
title: "Dicom To Nifti Conversion"
date: 2020-04-15
url: https://discourse.slicer.org/t/11124
---

# DICOM to NIFTI conversion

**Topic ID**: 11124
**Date**: 2020-04-15
**URL**: https://discourse.slicer.org/t/dicom-to-nifti-conversion/11124

---

## Post #1 by @rickychen (2020-04-15 12:15 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hi guys,</p>
<p>I’m wondering if someone knows how Slicer deals with the DICOM to NIFTI conversion? More specifically, what packages or tools do they use to achieve this? Is there any source code online on Slicer repo?</p>
<p>I know in Slicer, the DICOM file can be loaded into the scene and saved as various formats like .nrrd or NIFTI.</p>
<p>Best regards,<br>
Ricky</p>

---

## Post #2 by @Sam_Horvath (2020-04-15 15:45 UTC)

<p>Slicer loads from DICOM into its internal representation (vtkImageData) using a number of libraries. mostly GDCM and DCMTK.  It then uses ITK file writers to create the NIFTI image.</p>

---

## Post #3 by @pieper (2020-04-15 15:47 UTC)

<aside class="quote no-group" data-username="rickychen" data-post="1" data-topic="11124">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/74df32/48.png" class="avatar"> rickychen:</div>
<blockquote>
<p>More specifically, what packages or tools do they use to achieve this? Is there any source code online on Slicer repo?</p>
</blockquote>
</aside>
<p>The code with DICOM in the name here is a place to start, but this code itself relies on multiple libraries:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" target="_blank" rel="noopener">//github.com/Slicer/Slicer/tree/main/Modules/Scripted</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also this thread may help you:</p>
<aside class="quote quote-modified" data-post="12" data-topic="540">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-convert-dicom-files-to-nrrd/540/12">How to convert dicom files to nrrd</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can also consider one of the many tools out there that are much easier to use than Slicer for batch volume reconstruction (faster, easier to use, possibly more robust). 
You can find a list of some of the most popular ones (incomplete, I am sure) here: <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/">https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/</a>. 
A number of them (including Slicer converters) are set up in this dockerfile: <a href="https://github.com/QIICR/dcmheat/blob/master/docker/Dockerfile">https://github.com/QIICR/dcmheat/blob/master/docker/Dockerfile</a> (just noti…
  </blockquote>
</aside>


---
