---
topic_id: 44525
title: "Where Is Relax Polygons In The Latest Slicer Version Any Alt"
date: 2025-09-18
url: https://discourse.slicer.org/t/44525
---

# ​Where is “Relax Polygons” in the latest Slicer version? Any alternatives?

**Topic ID**: 44525
**Date**: 2025-09-18
**URL**: https://discourse.slicer.org/t/where-is-relax-polygons-in-the-latest-slicer-version-any-alternatives/44525

---

## Post #1 by @DDD (2025-09-18 17:50 UTC)

<p>​Hi everyone,</p>
<p>I’m using the latest version of 3D Slicer (version 5.6.2), and I can’t seem to find the “Relax Polygons” option in the “Surface Toolbox” module anymore.</p>
<p>In previous versions, I used “Relax Polygons” regularly to smooth mesh surfaces (such as STL models) before computing curvature using `vtkCurvatures`. This helped reduce curvature calculation errors caused by rough or noisy geometry.</p>
<p>However, in the latest version, Surface Toolbox is still available, but the “Relax Polygons” feature seems to be missing.</p>
<p>Questions:</p>
<p>1.Was “Relax Polygons” removed or renamed in recent versions?</p>
<p>2. Is there another module that includes this functionality?</p>
<p>3. If it’s no longer available in the Graphical User Interface, is there an equivalent method—such as a Python script or another module—to perform the same Laplacian smoothing?</p>
<p>Any advice or workarounds would be greatly appreciated. I rely on this feature for preparing surface models for curvature and morphometric analysis.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @mau_igna_06 (2025-09-18 20:19 UTC)

<blockquote>
<p>1.Was “Relax Polygons” removed or renamed in recent versions?</p>
</blockquote>
<p>Hi, yes. Here is the code:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/1525a5b5ef0c20566b5888f1b2f8c953c8adc524/relaxPolygons/relaxPolygons.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/1525a5b5ef0c20566b5888f1b2f8c953c8adc524/relaxPolygons/relaxPolygons.cxx" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerSurfaceToolbox</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/1525a5b5ef0c20566b5888f1b2f8c953c8adc524/relaxPolygons/relaxPolygons.cxx" target="_blank" rel="noopener nofollow ugc">relaxPolygons/relaxPolygons.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/1525a5b5ef0c20566b5888f1b2f8c953c8adc524/relaxPolygons/relaxPolygons.cxx" rel="noopener nofollow ugc"><code>1525a5b5e</code></a>
</div>


      <pre><code class="lang-cxx">#include "relaxPolygonsCLP.h"

//VTK Includes
#include "vtkFillHolesFilter.h"
#include "vtkPolyDataNormals.h"
#include "vtkXMLPolyDataWriter.h"
#include "vtkXMLPolyDataReader.h"
#include "vtkSmartPointer.h"
#include "vtkPolyData.h"
#include "vtkNew.h"
#include "vtkCleanPolyData.h"
#include "vtkWindowedSincPolyDataFilter.h"

// Similar Features to Smoothing in surface toolbox, but this is more definite.


int main (int argc, char * argv[])
 {
 PARSE_ARGS;

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/1525a5b5ef0c20566b5888f1b2f8c953c8adc524/relaxPolygons/relaxPolygons.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jamesobutler (2025-09-18 20:42 UTC)

<aside class="quote no-group" data-username="DDD" data-post="1" data-topic="44525">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/9fc348/48.png" class="avatar"> DDD:</div>
<blockquote>
<p>1.Was “Relax Polygons” removed or renamed in recent versions?</p>
</blockquote>
</aside>
<p>It appears to have been removed through the following PR by <a class="mention" href="/u/lassoan">@lassoan</a> , where he mentions:</p>
<blockquote>
<p>removed relax option (it was the same as smoothing).</p>
</blockquote>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/pull/41">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/41" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerSurfaceToolbox</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/41" target="_blank" rel="noopener nofollow ugc">ENH: Remove CLI modules that perform trivial tasks</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>remove-trivial-clis</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-18" data-time="18:54:43" data-timezone="UTC">06:54PM - 18 Jun 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 136 files with 1949 additions and 4499 deletions">
          <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/41/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1949</span>
            <span class="removed">-4499</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit replaces 130 files with about 50 lines of code.

VTK is easily ava<span class="show-more-container"><a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/41" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ilable in Python and it is simpler, more flexible, and more portable to run a Python script instead of compiling a C++ CLI module.

Also fixed extraction of feature edges; and removed relax option (it was the same as smoothing).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @DDD (2025-09-19 15:07 UTC)

<p>Thanks for sharing the code! I tried to use it but I’m not sure how to make it work in Slicer. Could you please provide some guidance?</p>

---

## Post #5 by @DDD (2025-09-19 15:12 UTC)

<p>Thanks for sharing the code! I see this is a C++ implementation. Could you guide me on how to implement this in Slicer? Should I compile it as a standalone module, or is there a way to achieve the same smoothing effect using Python and VTK within Slicer’s environment?</p>

---

## Post #6 by @pieper (2025-09-19 15:45 UTC)

<p>The C++ code looks like just some parameter settings on <code>vtkWindowedSincPolyDataFilter</code> so it should be basically trivial to make a python version.  If it does something better than what you can do with the smoothing option, you can look at what parameters matter and maybe just expose them in the smoothing option UI.</p>

---
