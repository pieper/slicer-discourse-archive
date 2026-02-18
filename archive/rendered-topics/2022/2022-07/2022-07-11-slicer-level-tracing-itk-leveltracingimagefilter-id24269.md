# Slicer level tracing, itk::LevelTracingImageFilter

**Topic ID**: 24269
**Date**: 2022-07-11
**URL**: https://discourse.slicer.org/t/slicer-level-tracing-itk-leveltracingimagefilter/24269

---

## Post #1 by @Eleonora_Tiribilli (2022-07-11 10:28 UTC)

<p>Someone knows how the <em><strong>itk::LevelTracingImageFilter</strong></em> works?</p>
<p>I found only the header file, with no explanation <a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkITK/itkLevelTracingImageFilter.h" class="inline-onebox" rel="noopener nofollow ugc">Slicer/itkLevelTracingImageFilter.h at main · Slicer/Slicer · GitHub</a></p>

---

## Post #2 by @Andinet_Enquobahrie (2022-07-11 11:12 UTC)

<p>The header file comment provides an explanation</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/vtkITK/itkLevelTracingImageFilter.h#L12-L27">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkITK/itkLevelTracingImageFilter.h#L12-L27" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkITK/itkLevelTracingImageFilter.h#L12-L27" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Libs/vtkITK/itkLevelTracingImageFilter.h#L12-L27</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="12" style="counter-reset: li-counter 11 ;">
          <li>/** \class LevelTracingImageFilter</li>
          <li> * \brief Trace a level curve/surface given a seed point on the level curve/surface.</li>
          <li> *</li>
          <li> * LevelTracingImageFilter traces a level curve (or surface) from a</li>
          <li> * seed point.  The pixels on this level curve "boundary" are labeled</li>
          <li> * as 1. Does nothing if seed is in uniform area.</li>
          <li> *</li>
          <li> * LevelTracingImageFilter provides a quick method to select a point</li>
          <li> * on a boundary of an object in a grayscale image and retrieve the</li>
          <li> * entire boundary of the object.</li>
          <li> *</li>
          <li> * For 2D images, the algorithm follows the boundary using 8-connected</li>
          <li> * neighbors.  For ND images, the algorithm traces the boundary using</li>
          <li> * face connected neighbors.</li>
          <li> *</li>
          <li> */</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Andinet_Enquobahrie (2022-07-11 11:18 UTC)

<p>It is one of the editor effects in the Segment Editor</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0311ed517fbcfa9ad8eb6c6283b0caa9b6de6ea.jpeg" data-download-href="/uploads/short-url/vZibZzbLmxtTXZ6CyKSKJJ3uYNY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0311ed517fbcfa9ad8eb6c6283b0caa9b6de6ea_2_690x431.jpeg" alt="image" data-base62-sha1="vZibZzbLmxtTXZ6CyKSKJJ3uYNY" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0311ed517fbcfa9ad8eb6c6283b0caa9b6de6ea_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0311ed517fbcfa9ad8eb6c6283b0caa9b6de6ea_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0311ed517fbcfa9ad8eb6c6283b0caa9b6de6ea_2_1380x862.jpeg 2x" data-dominant-color="B1B2B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1202 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
