---
topic_id: 13900
title: "3D View Rotation Stops Working Other Odd Bugs If Repeated Co"
date: 2020-10-06
url: https://discourse.slicer.org/t/13900
---

# 3D View rotation stops working (+other odd bugs) if repeated control point location

**Topic ID**: 13900
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/3d-view-rotation-stops-working-other-odd-bugs-if-repeated-control-point-location/13900

---

## Post #1 by @mikebind (2020-10-06 18:33 UTC)

<p>Running 4.11.202000930 (but bug is not new to this version, was at least present in the 2020-09-02 release) on Windows.</p>
<p>As a minimal example, the following code makes the left-click/drag rotation in a 3D view stop working, even from a newly opened Slicer.</p>
<pre><code>cn = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode', 'testCurveNode')
cn.AddControlPointWorld(vtk.vtkVector3d([0,0,0]))
cn.AddControlPointWorld(vtk.vtkVector3d([0,0,0]))
</code></pre>
<p>No errors reported in the log messages.  Scroll to zoom still works.  Scroll wheel click and drag drags the MarkupsCurve (including changing its control point coordinates) instead of panning the view (the reference cube stays in place while the markups curve (points) move).  Choosing the Spin or Rock 3D view buttons lead to weird distortions in the reference cube which gradually work themselves out.  The problem occurs for any repeated coordinates, not just [0,0,0].</p>
<p>Adding a non-identical point to the curve node seems to restore normal view rotation behavior. If there are multiple curve nodes in the scene, having just one of them be of this aberrant form is enough to lock up the 3D view.</p>

---

## Post #2 by @lassoan (2020-10-06 18:54 UTC)

<p>Thanks for reporting - fixed.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/bd10ac9a1ee46b2b4ab87b7c3885d35a57e8d4f8" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/bd10ac9a1ee46b2b4ab87b7c3885d35a57e8d4f8" target="_blank" rel="noopener">BUG: Fix incorrect curve picking when all curve points are exactly at the same position</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-10-06" data-time="18:51:24" data-timezone="UTC">06:51PM - 06 Oct 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 3 additions and 2 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/bd10ac9a1ee46b2b4ab87b7c3885d35a57e8d4f8" target="_blank" rel="noopener">
          <span class="added">+3</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Cell locator's FindClosestPoint method returns dist2=-1 if no cell is found. This confused the tolerance check, which detected that the picked...</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
