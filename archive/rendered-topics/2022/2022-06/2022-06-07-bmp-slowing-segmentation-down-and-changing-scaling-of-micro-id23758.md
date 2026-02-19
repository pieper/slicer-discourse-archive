---
topic_id: 23758
title: "Bmp Slowing Segmentation Down And Changing Scaling Of Micro"
date: 2022-06-07
url: https://discourse.slicer.org/t/23758
---

# .bmp slowing segmentation down and changing scaling of micro-CT images?

**Topic ID**: 23758
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/bmp-slowing-segmentation-down-and-changing-scaling-of-micro-ct-images/23758

---

## Post #1 by @dbgraf20 (2022-06-07 20:02 UTC)

<p>We have a micro-CT scanner that will only spit out .bmp files for us. My entire 3d slicer career I have only used .dcm. Segmentation has been nearly instant with .dcm files. My question comes from the fact that slicer doesn’t seem to work well with .bmp files. Segmentation with .bmp files seems to take 10x as long as doing it with a .dcm file. Also, the mice we are working on, 3d slicer seems to think are 3 meters long. Does 3d slicer work better with .dcm files? Would it be worth the money to get a .bmp to .dcm converter to speed up segmentation?</p>

---

## Post #2 by @pieper (2022-06-07 20:13 UTC)

<p>You should try the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks</a> module in the SlicerMorph extension.  You can specify screen spacing and other options.  BMP should not be slower than dicom in general, but maybe the dimensions or other differences slow things down.</p>

---

## Post #3 by @muratmaga (2022-06-07 20:32 UTC)

<aside class="quote no-group" data-username="dbgraf20" data-post="1" data-topic="23758">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/41988e/48.png" class="avatar"> dbgraf20:</div>
<blockquote>
<p>Also, the mice we are working on, 3d slicer seems to think are 3 meters long.</p>
</blockquote>
</aside>
<p>That’s because BMP extension does not preserve the scale of the data correctly (dicom or NRRD does).<br>
Also, by default BMP/PNG/JPG are treated as multichannel RGB image in Slicer, hence that may contribute to your slowdown.<br>
Install SlicerMorph extension, and use ImageStacks. Here is the tutorial for it: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks#readme" class="inline-onebox">Tutorials/ImageStacks at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>Also, if your scanner is Bruker/Skyscan, you can try the SkyscanReconImport module, to which yousimply point out the *_rec.log file from your reconstruction. This is also available as part of SlicerMorph.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport#readme">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport#readme" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport#readme" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport#readme" target="_blank" rel="noopener">//github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
