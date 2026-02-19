---
topic_id: 24653
title: "Calculate External Contour For Segment In Segmentation"
date: 2022-08-05
url: https://discourse.slicer.org/t/24653
---

# Calculate external contour for segment in segmentation

**Topic ID**: 24653
**Date**: 2022-08-05
**URL**: https://discourse.slicer.org/t/calculate-external-contour-for-segment-in-segmentation/24653

---

## Post #1 by @Mik (2022-08-05 14:30 UTC)

<p>I’m trying to calculate external contour and then transform it into markups curve node.Here is a <a href="https://kitware.github.io/vtk-examples/site/Cxx/PolyData/ExternalContour/" rel="noopener nofollow ugc">VTK example</a> with such case. Position and orientation of camera are known. Segment polydata is white, background is black.</p>
<p>Can the same VTK filter be used in 3D Slicer, or the program has builtin methods for that?</p>
<p>Code below gives an empty polydata:</p>
<pre><code class="lang-auto">    view = slicer.app.layoutManager().threeDWidget(0).threeDView()
    renderWindow = view.renderWindow()
    renderers = renderWindow.GetRenderers()
    renderer = renderers.GetItemAsObject(0)

    winToImageFilter = vtk.vtkWindowToImageFilter()
    winToImageFilter.SetInput(renderWindow)
    winToImageFilter.SetScale(2) #image quality
    winToImageFilter.Update()

    contFilter = vtk.vtkContourFilter()
    contFilter.SetInputConnection(winToImageFilter.GetOutputPort())
    contFilter.SetValue(0, 255)
    contFilter.Update()

    # Make the contour coincide with the data.
    contour = contFilter.GetOutput()
</code></pre>
<p>Data example<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a42196f3a3a77da36a0a987958292a07a42a593e.png" data-download-href="/uploads/short-url/npYgMplNoLl7QVssWTYkLaK1K90.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a42196f3a3a77da36a0a987958292a07a42a593e.png" alt="image" data-base62-sha1="npYgMplNoLl7QVssWTYkLaK1K90" width="502" height="500" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">684×680 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2022-08-08 08:38 UTC)

<p>I’m not aware of any function ready-made in Slicer for this. I think your approach is reasonable. On thought is that maybe you want to switch to orthogonal projection instead of the default perspective for this. Or maybe not, if you want the contour that is visible from a point in space.</p>

---

## Post #3 by @mau_igna_06 (2022-08-08 09:02 UTC)

<p>I think you could apply a projection transform to your model using your camera. And you may need to use vtkFeatureEdges after that in some combination of options</p>
<p>This may be related:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/bounding-volume-of-cylinder-path/8498/11">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/bounding-volume-of-cylinder-path/8498/11" target="_blank" rel="noopener" title="07:54PM - 27 May 2022">VTK – 27 May 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<h3><a href="https://discourse.vtk.org/t/bounding-volume-of-cylinder-path/8498/11" target="_blank" rel="noopener">Bounding volume of cylinder path</a></h3>

  <p>Thanks Will. I see the impact of Flying edges. But VoxelModeller is the time killer, especially when I bump the dimensions.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---

## Post #4 by @Mik (2022-08-08 09:34 UTC)

<p>Thank both of you!<br>
I will try several approaches and let you know. I’ve found some mistakes in my script and now trying to fix them.</p>
<p>The VTK example works but orientation and scale of the contour model must be modified.</p>

---
