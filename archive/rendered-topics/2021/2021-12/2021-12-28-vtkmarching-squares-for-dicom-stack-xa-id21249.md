---
topic_id: 21249
title: "Vtkmarching Squares For Dicom Stack Xa"
date: 2021-12-28
url: https://discourse.slicer.org/t/21249
---

# vtkMarching squares for dicom stack [XA]

**Topic ID**: 21249
**Date**: 2021-12-28
**URL**: https://discourse.slicer.org/t/vtkmarching-squares-for-dicom-stack-xa/21249

---

## Post #1 by @cfd_payne (2021-12-28 12:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> relative to our discussion on vtkForum around reconstructing set of 2d+t dicom files with modality=XA.</p><aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/vtkmarchingsquares-for-dicom-dcm-png-bmp-stack/7510">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/vtkmarchingsquares-for-dicom-dcm-png-bmp-stack/7510" target="_blank" rel="noopener nofollow ugc" title="02:59PM - 27 December 2021">VTK – 27 Dec 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/179;"><img src="https://discourse.vtk.org/uploads/default/optimized/2X/c/c45ce6f5fa443966a317ceb6c2b4405805ae4e1b_2_1024x266.png" class="thumbnail" width="690" height="179"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/vtkmarchingsquares-for-dicom-dcm-png-bmp-stack/7510" target="_blank" rel="noopener nofollow ugc">vtkMarchingSquares for DICOM *.dcm/png/bmp stack</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Support</span>
        </span>
      </span>
  </div>
</div>

  <p>@lassoan @dgobbi  Continuing the discussion from Stack of PNG files to be rendered as 3D:  I have a similar situation where the data seems 2D+t [typically coronary angiograms], i’m trying to understand “qualitative” flow pattern before and after...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I followed your tutorial on CTA-cardio, however the dicom i have is not trivial [for me atleast],</p>
<ol>
<li>
<p>when i load the dicom directory and examine , following are the warning i get<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f3def78f828403fbe2fb8d1696e382a019c6c0f.jpeg" data-download-href="/uploads/short-url/fS5H6Gp9UUsBK3umx666ZuLUEft.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f3def78f828403fbe2fb8d1696e382a019c6c0f_2_690x474.jpeg" alt="image" data-base62-sha1="fS5H6Gp9UUsBK3umx666ZuLUEft" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f3def78f828403fbe2fb8d1696e382a019c6c0f_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f3def78f828403fbe2fb8d1696e382a019c6c0f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f3def78f828403fbe2fb8d1696e382a019c6c0f.jpeg 2x" data-dominant-color="EFF2F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1021×702 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>when trying to carry out the segmentation, the 3D reconstruction is indefinite long squeeze<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc34223612a4c110cc5139a3302e392377818888.jpeg" data-download-href="/uploads/short-url/qQVsxbWlmurK5dKtaONBs7luiKs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc34223612a4c110cc5139a3302e392377818888_2_690x360.jpeg" alt="image" data-base62-sha1="qQVsxbWlmurK5dKtaONBs7luiKs" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc34223612a4c110cc5139a3302e392377818888_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc34223612a4c110cc5139a3302e392377818888_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc34223612a4c110cc5139a3302e392377818888_2_1380x720.jpeg 2x" data-dominant-color="AAAAB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1675×876 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>how do i progress from here, how to get the time transient information while reconstructing the geometry</p>

---

## Post #2 by @lassoan (2021-12-28 12:37 UTC)

<p>Probably the best is to use the items provided by the “Image sequence” reader. Select those items (and unselect the MultiVolume reader’s items) and load them. Instead of manually uncheck the MultiVolume item and check the Image sequence items, it may be easier to disable the MultiVolume plugin in the settings in the module panel on the left.</p>
<p>There is a warning about image spacing because XA images are acquired with perspective projection therefore there is no spacing (mm/pixel) value ethat would be valid for all visible structures. You can compute the spacing a specific plane by measuring the size of an object of known physical size and multiply the spacing value in Volumes module’s Information section.</p>
<p>What would you like to segment on the images and why? What is your overall goal? What metrics would you like to compute? Is there a journal paper that describes the kind of analysis that you are trying to reproduce?</p>

---

## Post #3 by @cfd_payne (2021-12-28 13:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21249">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably the best is to use the items provided by the “Image sequence” reader. Select those items (and unselect the MultiVolume reader’s items) and load them. Instead of manually uncheck the MultiVolume item and check the Image sequence items, it may be easier to disable the MultiVolume plugin in the settings in the module panel on the left.</p>
</blockquote>
</aside>
<p>Tried this but in vain.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21249">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What would you like to segment on the images and why? What is your overall goal? What metrics would you like to compute? Is there a journal paper that describes the kind of analysis that you are trying to reproduce?</p>
</blockquote>
</aside>
<p>Motivation1: enablers like <a href="https://kitware.github.io/vtk-examples/site/Cxx/Modelling/ContourTriangulator/" rel="noopener nofollow ugc">ContourTriangulator</a>, <a href="https://kitware.github.io/vtk-examples/site/Cxx/Modelling/MarchingSquares/" rel="noopener nofollow ugc">MarchingSquares</a> for image processing whose inputs start from PNG, <a href="https://kitware.github.io/vtk-examples/site/Cxx/VisualizationAlgorithms/ImageGradient/" rel="noopener nofollow ugc">ImageGradient</a> , [EnhanceEdges] from mhd<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6ae5f8321ca5807a6f14ed9933a6675c1f4fa9b.jpeg" data-download-href="/uploads/short-url/slC8az9UPjNAjZXrar49IZFQpTl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6ae5f8321ca5807a6f14ed9933a6675c1f4fa9b_2_250x250.jpeg" alt="image" data-base62-sha1="slC8az9UPjNAjZXrar49IZFQpTl" width="250" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6ae5f8321ca5807a6f14ed9933a6675c1f4fa9b_2_250x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6ae5f8321ca5807a6f14ed9933a6675c1f4fa9b_2_375x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6ae5f8321ca5807a6f14ed9933a6675c1f4fa9b_2_500x500.jpeg 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">512×512 98.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Motivation2:-  to reproduce “qualitative” flow behavior from dicom instead of vtk as described in the below example &amp; or visualize around arteries before/after stent placement<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d89ea6ee274b68852df96539176a00071c0b9a1.png" alt="image" data-base62-sha1="fD1wHoZ6DDU1tYm2aUc5KXZNo9H" width="320" height="240"></p>
<p>Haven’t put any thoughts beyond the above reads.</p>

---
