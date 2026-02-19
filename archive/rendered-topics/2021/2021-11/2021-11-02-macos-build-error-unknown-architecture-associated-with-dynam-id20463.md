---
topic_id: 20463
title: "Macos Build Error Unknown Architecture Associated With Dynam"
date: 2021-11-02
url: https://discourse.slicer.org/t/20463
---

# macOS build #error "Unknown architecture !" associated with DynamicModeler/Logic/FastMarching

**Topic ID**: 20463
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/macos-build-error-unknown-architecture-associated-with-dynamicmodeler-logic-fastmarching/20463

---

## Post #1 by @hherhold (2021-11-02 16:07 UTC)

<p>I get as far as:</p>
<pre><code>In file included from /opt/SB/debug/SurfaceToolbox/DynamicModeler/Logic/FastMarching/gw_core/../gw_maths/GW_Maths.h:13:
/opt/SB/debug/SurfaceToolbox/DynamicModeler/Logic/FastMarching/gw_core/../gw_maths/GW_MathsConfig.h:139:3: error: "Unknown architecture !"
    #error "Unknown architecture !"
</code></pre>
<p>Now, I <em>am</em> building on MacOS 11.6, with my CMAKE_OSX_DEPLOYMENT_TARGET set to 10.15, but I have done this before (though a while ago) and had no issues. Perhaps I should build with an up to date deployment target version.</p>

---

## Post #2 by @jcfr (2021-11-02 16:09 UTC)

<blockquote>
<p><code>#error "Unknown architecture !" </code></p>
</blockquote>
<p>This particular issue is being address in <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/48" class="inline-onebox">Fix macOS build error, simplify setting of position independent flag and fix warnings by jcfr · Pull Request #48 · Slicer/SlicerSurfaceToolbox · GitHub</a> and should be addressed in the next hour.</p>

---

## Post #3 by @hherhold (2021-11-02 16:09 UTC)

<p>Got it, thanks <a class="mention" href="/u/jcfr">@jcfr</a>!</p>

---

## Post #4 by @jcfr (2021-11-02 17:29 UTC)

<p>This has been fixed in</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5982">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5982" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5982" target="_blank" rel="noopener">COMP: Fix macOS build error updating SlicerSurfaceToolbox</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:update-surfacetoolbox-fix-macos-build-error</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-02" data-time="17:21:54" data-timezone="UTC">05:21PM - 02 Nov 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5982/files" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit fixes a regression introduced in a15cbacbb9 (ENH: Add "Select
by po<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5982" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ints" tool to Dynamic Modeler module)

List of SlicerSurfaceToolbox changes:

```
$ git shortlog 8dd9ce053..df684ae --no-merges
Jean-Christophe Fillion-Robin (20):
      COMP: Simplify setting of position independent flag for MeshGeodesics target
      COMP: Fix -Wunknown-pragmas in DynamicModeler/Logic/FastMarching
      COMP: Fix -Wunused-parameter in DynamicModeler/Logic/FastMarching
      COMP: Fix -Wreorder in DynamicModeler/Logic/FastMarching
      BUG: Fix GW_Face::GetEdgeNumber to return -1 if edge is not found
      COMP: Fix -Wunused-variable in GW_Mesh::BuildCurvatureData
      COMP: Fix -Wsign-compare in GW_VectorStatic.h
      COMP: Fix -Woverloaded-virtual in DynamicModeler/Logic/FastMarching
      COMP: Fix -Wdelete-non-virtual-dtor in GW_GeodesicFace.inl
      COMP: Fix -Wunused-variable in GW_GeodesicPath
      COMP: Fix -Wunused-local-typedefs in vtkFastMarchingGeodesicDistance
      COMP: Fix -Wunused-variable in GW_TriangularInterpolation_(Cubic|Quadratic)
      COMP: Fix -Wformat-security in GW_OutputStream
      COMP: Fix DynamicModeler/Logic/FastMarching build error on macOS
      COMP: Fix -Winconsistent-missing-override in DynamicModeler/Logic/FastMarching
      BUG: Fix -Woverloaded-virtual in DynamicModeler/Logic/FastMarching/gw_geodesic/GW_GeodesicMesh.h
      BUG: Fix -Wparentheses in GW_GeodesicPath::AddNewPoint()
      COMP: Fix -Wsign-compare in vtkFastMarchingGeodesicDistance::SetupCallbacks()
      Revert "BUG: Fix GW_Face::GetEdgeNumber to return -1 if edge is not found"
      ENH: Re-add GW_GeodesicMesh::GetRandomVertex(GW_Bool bForceFar) for debugging
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @hherhold (2021-11-02 18:48 UTC)

<p>OK, I can build and run on MacOS. Thanks!</p>

---
