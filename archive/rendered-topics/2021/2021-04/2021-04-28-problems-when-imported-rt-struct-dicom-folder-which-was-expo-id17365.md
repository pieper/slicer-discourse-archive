---
topic_id: 17365
title: "Problems When Imported Rt Struct Dicom Folder Which Was Expo"
date: 2021-04-28
url: https://discourse.slicer.org/t/17365
---

# Problems when imported RT-Struct dicom folder which was exported by Slicer 3D into Varian Eclipse

**Topic ID**: 17365
**Date**: 2021-04-28
**URL**: https://discourse.slicer.org/t/problems-when-imported-rt-struct-dicom-folder-which-was-exported-by-slicer-3d-into-varian-eclipse/17365

---

## Post #1 by @Namng1210 (2021-04-28 08:19 UTC)

<p>Dear authors,<br>
I have recently asked you guys about how to export to a segmentation nifti files into RT-Struct by python script and i was able to do it thanks to your instructions. But now, i’m facing new problems.<br>
<strong>When i took the folder which was output by 3D Slicer to Varian Eclipse, i got a tons of error which was showed as below</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://user-images.githubusercontent.com/69883752/116051395-c0884180-a6a2-11eb-88fa-657da488ccb6.png" title="image" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/69883752/116051395-c0884180-a6a2-11eb-88fa-657da488ccb6.png" alt="image" width="690" height="347"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1547×780</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg>
</div></a></div>.<br>
<strong>And here is also the result when imported Auto_SS ( Segmentation rt-struct file which was created by 3D Slicer)</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://user-images.githubusercontent.com/69883752/116052410-c9c5de00-a6a3-11eb-9700-a166f811dd37.png" title="image" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/69883752/116052410-c9c5de00-a6a3-11eb-9700-a166f811dd37.png" alt="image" width="690" height="241"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1497×524</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg>
</div></a></div><br>
Can you show me how to deal with these problems ?<br>
Hope you reply me soon.</p>

---

## Post #2 by @Namng1210 (2021-05-04 08:08 UTC)

<p>Dear authors,<br>
I have recently asked you guys about how to export to a segmentation nifti files into RT-Struct by python script and i was able to do it thanks to your instructions. But now, i’m facing new problems.<br>
<strong>When i took the folder which was output by 3D Slicer to Varian Eclipse, i got a tons of error which was showed as below</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://user-images.githubusercontent.com/69883752/116051395-c0884180-a6a2-11eb-88fa-657da488ccb6.png" title="image" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/69883752/116051395-c0884180-a6a2-11eb-88fa-657da488ccb6.png" alt="image" width="690" height="347"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1547×780</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg>
</div></a></div>.<br>
<strong>And here is also the result when imported Auto_SS ( Segmentation rt-struct file which was created by 3D Slicer)</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://user-images.githubusercontent.com/69883752/116052410-c9c5de00-a6a3-11eb-9700-a166f811dd37.png" title="image" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/69883752/116052410-c9c5de00-a6a3-11eb-9700-a166f811dd37.png" alt="image" width="690" height="241"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1497×524</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg>
</div></a></div><br>
Can you show me how to deal with these problems ?<br>
Hope you reply me soon.</p>

---

## Post #3 by @cpinter (2021-05-04 09:27 UTC)

<p>Please do not repeat questions. If you want to bump it add a comment.</p>
<p>Does the same issue happen if you export the RTSS from the GUI?<br>
Does the same issue happen if you try to import these dataset to Varian?</p><aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerRt/SlicerRtData/tree/master/plastimatch_tiny-rt-study" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/e36fd9c22f6eef75301c04b4bb004ca2e1530fb65b02110480bed08c313d26e8/SlicerRt/SlicerRtData" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/SlicerRt/SlicerRtData/tree/master/plastimatch_tiny-rt-study" target="_blank" rel="noopener">SlicerRt/SlicerRtData</a></h3>

<p><a href="https://github.com/SlicerRt/SlicerRtData/tree/master/plastimatch_tiny-rt-study" target="_blank" rel="noopener">master/plastimatch_tiny-rt-study</a></p>

  <p><span class="label1">Sample DICOM-RT datasets for demonstration and testing purposes</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerRt/SlicerRtData/tree/master/plastimatch-phantom-randomnoise" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/e36fd9c22f6eef75301c04b4bb004ca2e1530fb65b02110480bed08c313d26e8/SlicerRt/SlicerRtData" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/SlicerRt/SlicerRtData/tree/master/plastimatch-phantom-randomnoise" target="_blank" rel="noopener">SlicerRt/SlicerRtData</a></h3>

<p><a href="https://github.com/SlicerRt/SlicerRtData/tree/master/plastimatch-phantom-randomnoise" target="_blank" rel="noopener">master/plastimatch-phantom-randomnoise</a></p>

  <p><span class="label1">Sample DICOM-RT datasets for demonstration and testing purposes</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I unfortunately cannot be of real help to you as I don’t have personal experience nor access to Varian systems. If somebody who has sees your post that person will surely answer.</p>

---
