---
topic_id: 25881
title: "Ctk Vtkimagedatatoqimage Generates Weird Results"
date: 2022-10-25
url: https://discourse.slicer.org/t/25881
---

# ctk::vtkImageDataToQImage generates weird results

**Topic ID**: 25881
**Date**: 2022-10-25
**URL**: https://discourse.slicer.org/t/ctk-vtkimagedatatoqimage-generates-weird-results/25881

---

## Post #1 by @nnzzll (2022-10-25 03:08 UTC)

<p>I’m trying to convert vtkImageData to a QImage and display it.</p>
<p>Image below is the original image data displayed in sliceWidget.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2caf4892a1d629298875031914a0c0754739b9c1.jpeg" data-download-href="/uploads/short-url/6niydgPbUAq5eJenkz5GilxPvZD.jpeg?dl=1" title="Screenshot from 2022-10-25 11-01-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2caf4892a1d629298875031914a0c0754739b9c1_2_501x500.jpeg" alt="Screenshot from 2022-10-25 11-01-14" data-base62-sha1="6niydgPbUAq5eJenkz5GilxPvZD" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2caf4892a1d629298875031914a0c0754739b9c1_2_501x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2caf4892a1d629298875031914a0c0754739b9c1_2_751x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2caf4892a1d629298875031914a0c0754739b9c1.jpeg 2x" data-dominant-color="8B8B8B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-10-25 11-01-14</span><span class="informations">975×972 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this is what I got by using <code>ctk::vtkImageDataToQImage</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdcfb1731986c223e681a995bf873d7e9f36c7a4.png" data-download-href="/uploads/short-url/r59dN9ftniaKO8yxB9ScimnfDhO.png?dl=1" title="Screenshot from 2022-10-25 11-03-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdcfb1731986c223e681a995bf873d7e9f36c7a4.png" alt="Screenshot from 2022-10-25 11-03-23" data-base62-sha1="r59dN9ftniaKO8yxB9ScimnfDhO" width="507" height="500" data-dominant-color="848484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-10-25 11-03-23</span><span class="informations">1037×1022 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It confused me since in most cases, <code>ctk::vtkImageDataToQImage</code> generates the right result, I don’t know why this kind of case happened</p>

---

## Post #2 by @nnzzll (2022-10-25 07:42 UTC)

<p>The problem is due to <code>QImage()</code> constructor.<br>
In most cases, <code>QImage(int width, int height,QImage::QFormat format)</code> works fine, however, sometimes  the <code>bytesPerLine</code> need to be specified, otherwise this kind of tilted issue happens.<br>
This issue can be solved by the code below:</p>
<pre><code class="lang-auto">QImage VTKImageDataToQImage(vtkImageData* imageData)
{
  if (!imageData || !imageData-&gt;GetPointData() || !imageData-&gt;GetPointData()-&gt;GetScalars() ||
      imageData-&gt;GetScalarType() != VTK_UNSIGNED_CHAR)
  {
    return QImage();
  }

  int width = imageData-&gt;GetDimensions()[0];
  int height = imageData-&gt;GetDimensions()[1];
  vtkIdType numberOfScalarComponents = imageData-&gt;GetNumberOfScalarComponents();
  QImage image;
  QImage::Format format;
  if (numberOfScalarComponents == 3)
  {
    format = QImage::Format_RGB888;
  }
  else if (numberOfScalarComponents == 4)
  {
    format = QImage::Format_RGBA8888;
  }
#if QT_VERSION &gt;= QT_VERSION_CHECK(5, 5, 0)
  else if (numberOfScalarComponents == 1)
  {
    format = QImage::Format_Grayscale8;
  }
#endif
  else
  {
    // unsupported pixel format
    return QImage();
  }
  image = QImage(static_cast&lt;uint8_t*&gt;(imageData-&gt;GetScalarPointer(0, 0, 0)), width, height,
                 width * numberOfScalarComponents, format);
  return image.mirrored();
}
</code></pre>

---

## Post #3 by @lassoan (2023-01-07 00:41 UTC)

<p>Thank you, your fix was integrated into CTK at</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/dec834fccffebdc3b0896c157d39e3c0031c4a0a">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/dec834fccffebdc3b0896c157d39e3c0031c4a0a" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/dec834fccffebdc3b0896c157d39e3c0031c4a0a" target="_blank" rel="noopener">BUG: Fix ctk::vtkImageDataToQImage function</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-01-04" data-time="19:32:42" data-timezone="UTC">07:32PM - 04 Jan 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 21 additions and 17 deletions">
        <a href="https://github.com/commontk/CTK/commit/dec834fccffebdc3b0896c157d39e3c0031c4a0a" target="_blank" rel="noopener">
          <span class="added">+21</span>
          <span class="removed">-17</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Bytes per line must be specified to make sure the image is always converted corr<span class="show-more-container"><a href="https://github.com/commontk/CTK/commit/dec834fccffebdc3b0896c157d39e3c0031c4a0a" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ectly.

The problem was reported and solution was proposed here:
https://discourse.slicer.org/t/ctk-vtkimagedatatoqimage-generates-weird-results/25881/2</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
