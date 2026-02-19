---
topic_id: 21873
title: "Why Are Dimensions Transposed In Arrayfromvolume"
date: 2022-02-09
url: https://discourse.slicer.org/t/21873
---

# Why are dimensions transposed in `arrayFromVolume`?

**Topic ID**: 21873
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/why-are-dimensions-transposed-in-arrayfromvolume/21873

---

## Post #1 by @ebrahim (2022-02-09 17:31 UTC)

<p>In the function <code>slicer.util.arrayFromVolume</code>, it looks like the IJK directions get permuted, <a href="https://github.com/Slicer/Slicer/blob/fab4ec043672efc3434ae29fea498979b9ae7b17/Base/Python/slicer/util.py#L1469" rel="noopener nofollow ugc">see the <code>reversed</code> here</a>. Can anyone explain the reason for this?</p>
<p>If I understand correctly, this permutes <code>I,J,K</code> to <code>K,J,I</code>, so for example the 0th dimension of the array returned by <code>arrayFromVolume</code> ends up corresponding to the <code>K</code> direction. That seems weird, so maybe I am missing something here…</p>

---

## Post #2 by @jamesobutler (2022-02-09 18:50 UTC)

<p>Take a look at this comment</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/very-confused-about-imdata-matrix-index-order/6608/2?u=lassoan">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/very-confused-about-imdata-matrix-index-order/6608/2?u=lassoan" target="_blank" rel="noopener nofollow ugc" title="03:42PM - 11 September 2021">VTK – 11 Sep 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<h3><a href="https://discourse.vtk.org/t/very-confused-about-imdata-matrix-index-order/6608/2?u=lassoan" target="_blank" rel="noopener nofollow ugc">Very confused about imdata matrix index order</a></h3>

  <p>For an array (or matrix), the indexing is [row, col] for two dimensions, or [slice, row, col] for three dimensions.  Consider the following code, where a[1,0] means row=1, col=0:  &gt;&gt;&gt; import numpy as np &gt;&gt;&gt; np.array([[1,2],[3,4]])...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>linked from this ITK thread</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.itk.org/t/image-index-ordering-in-python-api/4496">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/image-index-ordering-in-python-api/4496" target="_blank" rel="noopener nofollow ugc" title="08:47PM - 13 October 2021">ITK – 13 Oct 21</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.itk.org/uploads/default/original/1X/8a8379ed42cbc60fb262a064faca192c7d7111e7.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://discourse.itk.org/t/image-index-ordering-in-python-api/4496" target="_blank" rel="noopener nofollow ugc">Image index ordering in Python API</a></h3>

  <p>I know this topic has been discussed before, and maybe all decisions have been made and too much legacy exists anyway already…  Still, I find it strange to have this numpy array like view of an ITK image with inverted index ordering:   coming from...</p>

  <p>
    <span class="label1">Reading time: 2 mins 🕑</span>
      <span class="label2">Likes: 7 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ebrahim (2022-02-09 18:59 UTC)

<p>Thank you, I suppose this explains the reasoning. <code>K,J,I</code> order is trying to be like (slice, row, column).</p>

---
