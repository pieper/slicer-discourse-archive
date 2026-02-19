---
topic_id: 42348
title: "Any Way To Reduce Image Stacks Size"
date: 2025-03-28
url: https://discourse.slicer.org/t/42348
---

# Any way to reduce image stacks size?

**Topic ID**: 42348
**Date**: 2025-03-28
**URL**: https://discourse.slicer.org/t/any-way-to-reduce-image-stacks-size/42348

---

## Post #1 by @JaredAmudeo (2025-03-28 18:37 UTC)

<p><strong>Hello!</strong> Recently, our research team has gained access to a benchtop micro-CT scanner, but the resulting files are very large, averaging over 10 GB. The output files are stacks of PNG and TIFF images.</p>
<p>I am aware of the <strong>Crop Volume</strong> module in <strong>3D Slicer</strong>, but I am looking for a method that can further reduce the file size.</p>
<p>Is there a way within <strong>3D Slicer</strong> or other software like <strong>Photoshop</strong> to reduce the size of these images? For example, by cropping out unwanted areas?</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @jamesobutler (2025-03-28 18:51 UTC)

<p>Try SlicerMorph’s tutorial about its ImageStacks Slicer module.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener nofollow ugc">Tutorials/ImageStacks at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener nofollow ugc">SlicerMorph/Docs/ImageStacks at master · SlicerMorph/SlicerMorph</a></h3>


  <p><span class="label1">Extension to import microCT data and conduct 3D morphometrics in Slicer - SlicerMorph/SlicerMorph</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @JaredAmudeo (2025-03-28 19:01 UTC)

<p>I know about that extension, in fact I used it and I understand that it allows you to choose a full resolution and medium resolution quality, but the idea is precisely not to lower the resolution of the tomographies.</p>

---

## Post #4 by @muratmaga (2025-03-28 19:10 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="3" data-topic="42348">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>but the idea is precisely not to lower the resolution of the tomographies.</p>
</blockquote>
</aside>
<p>So are you looking to compress them? if so, I think the only way you can reduce their file size is using an highly efficient compression, which probably give you another couple percent reduction.</p>
<p>In Memory consumption of the data has nothing to do with the file size. If you do not reduce the resolution of the images, the data will consume same amount of memory when loaded (regardless of the file size, which is dependent on the compression method used).</p>

---

## Post #5 by @JaredAmudeo (2025-03-28 21:40 UTC)

<p>I found a solution. Use ImageJ and Shrink the 2x2x2 in Transformation → bin</p>

---

## Post #6 by @jamesobutler (2025-03-28 22:19 UTC)

<p>That ImageJ solution is downsampling your volume to reduce the number of voxels and therefore memory usage. This would be like the SlicerMorph ImageStacks module’s option of “Quality” being set to “Half resolution”.</p>

---

## Post #7 by @JaredAmudeo (2025-03-28 22:38 UTC)

<p>Ohh, I get it now. I thought they were different things</p>

---
