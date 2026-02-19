---
topic_id: 32618
title: "Export Dcm As A Single File"
date: 2023-11-06
url: https://discourse.slicer.org/t/32618
---

# Export dcm as a single file

**Topic ID**: 32618
**Date**: 2023-11-06
**URL**: https://discourse.slicer.org/t/export-dcm-as-a-single-file/32618

---

## Post #1 by @mohammed_alshakhas (2023-11-06 07:41 UTC)

<p>is it possible to export dicom as a single file rather than a directory?<br>
thanks</p>

---

## Post #2 by @pieper (2023-11-06 15:54 UTC)

<p>The dicom multiframe image format is very uncommon so we don’t support writing it directly (only reading it).  If you really need a single dicom file you can use an external converter.</p>
<p>You’ll find it’s not a simple topic:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.itk.org/t/how-to-convert-dicom-sequence-images-into-a-multi-frame-dicom-file/3116">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/how-to-convert-dicom-sequence-images-into-a-multi-frame-dicom-file/3116" target="_blank" rel="noopener" title="10:04AM - 25 May 2020">ITK – 25 May 20</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.itk.org/uploads/default/original/1X/8a8379ed42cbc60fb262a064faca192c7d7111e7.png" class="thumbnail onebox-avatar" width="500" height="500">

<div class="title-wrapper">
  <h3><a href="https://discourse.itk.org/t/how-to-convert-dicom-sequence-images-into-a-multi-frame-dicom-file/3116" target="_blank" rel="noopener">How to convert DICOM sequence images into a multi frame DICOM file.</a></h3>
</div>

  <p>Now I have dicom files of one sequence? Totally 117 files. Now I want to write these files into on .dcm File？  How to do it? not use mimics and so on.</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 12 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://groups.google.com/g/comp.protocols.dicom/c/h-8rj9ObBMM?pli=1" class="onebox" target="_blank" rel="noopener">https://groups.google.com/g/comp.protocols.dicom/c/h-8rj9ObBMM?pli=1</a></p>

---
