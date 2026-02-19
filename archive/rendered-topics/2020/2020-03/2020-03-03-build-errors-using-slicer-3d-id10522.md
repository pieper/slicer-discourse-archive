---
topic_id: 10522
title: "Build Errors Using Slicer 3D"
date: 2020-03-03
url: https://discourse.slicer.org/t/10522
---

# Build errors using slicer 3D

**Topic ID**: 10522
**Date**: 2020-03-03
**URL**: https://discourse.slicer.org/t/build-errors-using-slicer-3d/10522

---

## Post #1 by @loubna (2020-03-03 15:10 UTC)

<p>Hi,</p>
<p>I try the re-implement the VTKMPUReconstruction method using slicer3D. The slicer3D is compiled without errors. I create a new extension , add a module and I tried implement a non -optimezd marching cubes and some other examples when I get a good results.</p>
<p>But with this method I get Following errors: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/257ee27846f310c333cc6886a75dea55bc8e654d.png" data-download-href="/uploads/short-url/5lHvXCDR9EMmHBu0SqACJu9V245.png?dl=1" title="capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/257ee27846f310c333cc6886a75dea55bc8e654d_2_690x272.png" alt="capture" data-base62-sha1="5lHvXCDR9EMmHBu0SqACJu9V245" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/257ee27846f310c333cc6886a75dea55bc8e654d_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/257ee27846f310c333cc6886a75dea55bc8e654d_2_1035x408.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/257ee27846f310c333cc6886a75dea55bc8e654d_2_1380x544.png 2x" data-dominant-color="EFEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture</span><span class="informations">1841×726 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are there any lib directory or include that i must add in the project because generally The error of "unresolved external symbol " usually cause by complier can not find the lib files?</p>
<p>Thank’s in advance for your help</p>

---

## Post #2 by @pieper (2020-03-03 15:57 UTC)

<p>For reference, it appears this issue is cross-posted at the VTK discourse linked below.  (It’s not technically wrong to post both places, but it’s probably most efficient to wait for an answer on one site before posting to the second and also to link back to the other so that anyone trying to help you can have the full context).</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="16" height="16">
      <a href="https://discourse.vtk.org/t/building-errors/2746" target="_blank" title="02:35PM - 03 March 2020">VTK – 3 Mar 20</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:107/57;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="107" height="57"></div>

<h3><a href="https://discourse.vtk.org/t/building-errors/2746" target="_blank">Building errors</a></h3>

<p>Hi,  I tried to  re-implement the vtkMPUReconstruction using the slicer3D.   The 3D Slicer is compiled without errors. but when I compile the method I get  errors like this:  LNK2001	unresolved external symbol “public: virtual void...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
