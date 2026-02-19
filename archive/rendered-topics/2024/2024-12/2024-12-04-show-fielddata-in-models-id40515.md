---
topic_id: 40515
title: "Show Fielddata In Models"
date: 2024-12-04
url: https://discourse.slicer.org/t/40515
---

# Show FieldData in Models

**Topic ID**: 40515
**Date**: 2024-12-04
**URL**: https://discourse.slicer.org/t/show-fielddata-in-models/40515

---

## Post #1 by @phcerdan (2024-12-04 21:27 UTC)

<p>The only way to pass metadata along a pipeline in VTK is with FieldData.</p><aside class="onebox discoursetopic" data-onebox-src="https://discourse.paraview.org/t/solved-adding-metadata-to-a-vtkinformation-or-a-grid-object-flowing-through-the-pipeline/318">
  <header class="source">
      <img src="https://discourse.paraview.org/uploads/default/optimized/2X/8/8ca8a3bd08e322918d9c0958f548dec7d0e7cd8d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.paraview.org/t/solved-adding-metadata-to-a-vtkinformation-or-a-grid-object-flowing-through-the-pipeline/318" target="_blank" rel="noopener nofollow ugc" title="12:37PM - 16 July 2018">ParaView – 16 Jul 18</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.paraview.org/uploads/default/original/2X/8/8ca8a3bd08e322918d9c0958f548dec7d0e7cd8d.png" class="thumbnail onebox-avatar" width="500" height="500">

<div class="title-wrapper">
  <h3><a href="https://discourse.paraview.org/t/solved-adding-metadata-to-a-vtkinformation-or-a-grid-object-flowing-through-the-pipeline/318" target="_blank" rel="noopener nofollow ugc">[Solved] Adding metadata to a vtkInformation or a grid object flowing through...</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #0E76BD;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Development</span>
        </span>
      </span>
  </div>
</div>

  <p>Hello,  I need to retrieve some metadata (user information e.g. distances in meters) related to a data object (e.g. vtkImageData) in my Paraview’s filters plugins.  I noticed that a filter’s output is shallow copied in the filter next to it,...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 2 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
FieldData is not associated to vertices or edges on the Mesh.</p>
<p>Slicer has no way, up to my knowledge to show the FieldData of a vtk file. Paraview shows it in the Information tab. I wonder if we could add that to the information tab in Models as well:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfeeb295cab30fdee26372b67cbed18a58c50197.png" data-download-href="/uploads/short-url/vWZSKQHt7pce8qaDFuMHtcA25W7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfeeb295cab30fdee26372b67cbed18a58c50197.png" alt="image" data-base62-sha1="vWZSKQHt7pce8qaDFuMHtcA25W7" width="527" height="260"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">527×260 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
