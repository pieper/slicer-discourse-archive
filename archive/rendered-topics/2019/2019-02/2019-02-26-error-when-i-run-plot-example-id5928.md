# Error when i run plot example

**Topic ID**: 5928
**Date**: 2019-02-26
**URL**: https://discourse.slicer.org/t/error-when-i-run-plot-example/5928

---

## Post #1 by @dp1991 (2019-02-26 11:59 UTC)

<p>hi friends<br>
i run this example <a href="https://vtk.org/Wiki/VTK/Examples/Cxx/Plotting/ScatterPlot" rel="nofollow noopener">https://vtk.org/Wiki/VTK/Examples/Cxx/Plotting/ScatterPlot</a><br>
but i receive error<br>
i attach images that show program and error<br>
how can i resolve it ??</p>

---

## Post #2 by @dp1991 (2019-02-26 12:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c4e256be688fd52fc92148d9c3418a6f3aa92bc.png" data-download-href="/uploads/short-url/42oNo4LHzE1Py6yRsNTHnrmXfJO.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c4e256be688fd52fc92148d9c3418a6f3aa92bc_2_690x431.png" alt="Untitled" data-base62-sha1="42oNo4LHzE1Py6yRsNTHnrmXfJO" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c4e256be688fd52fc92148d9c3418a6f3aa92bc_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c4e256be688fd52fc92148d9c3418a6f3aa92bc_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c4e256be688fd52fc92148d9c3418a6f3aa92bc_2_1380x862.png 2x" data-dominant-color="282826"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1680×1050 88.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @dp1991 (2019-02-26 12:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa33f6c9041067a993493d3955bd2036587d321d.png" data-download-href="/uploads/short-url/zHoHoIATiLL4aquSYDxqAdl8bHn.png?dl=1" title="Untitled3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa33f6c9041067a993493d3955bd2036587d321d.png" alt="Untitled3" data-base62-sha1="zHoHoIATiLL4aquSYDxqAdl8bHn" width="690" height="488" data-dominant-color="EEEEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled3</span><span class="informations">885×627 4.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @dp1991 (2019-02-26 12:24 UTC)

<p>i resolve it by adding<br>
<span class="hashtag">#include</span> “vtkAutoInit.h”<br>
VTK_MODULE_INIT(vtkRenderingOpenGL2); // VTK was built withvtkRenderingOpenGL2<br>
VTK_MODULE_INIT(vtkInteractionStyle);<br>
VTK_MODULE_INIT(vtkRenderingVolumeOpenGL2);</p>
<p><span class="hashtag">#pragma</span> warning(disable : 4996)<br>
before main function<br>
but i have new error<br>
“vtkContextDevice2D”<br>
how to resolve new error ??</p>

---

## Post #5 by @pieper (2019-02-26 12:52 UTC)

<p>Hi <a class="mention" href="/u/dp1991">@dp1991</a> -</p>
<p>That topic would be better for the VTK discourse:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/" target="_blank" rel="noopener">VTK</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<h3><a href="https://discourse.vtk.org/" target="_blank" rel="noopener">VTK</a></h3>

  <p>A place to discuss VTK development</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2019-02-26 14:57 UTC)

<p>Note that you can display plots (line, bar, scatter) in Slicer from Table nodes using Plots module. You can also create a plot from Python as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Plotting" rel="nofollow noopener">this example</a>.</p>

---

## Post #7 by @dp1991 (2019-02-27 05:14 UTC)

<p>thanks<br>
i can solve it <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=6" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---
