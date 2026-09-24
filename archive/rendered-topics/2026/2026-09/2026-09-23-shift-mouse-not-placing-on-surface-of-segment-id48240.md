---
topic_id: 48240
title: "Shift-mouse not placing on surface of segment"
date: 2026-09-23
url: https://discourse.slicer.org/t/48240
last_bumped: 2026-09-23T16:56:54.796Z
---

# Shift-mouse not placing on surface of segment

**Topic ID**: 48240
**Date**: 2026-09-23
**URL**: https://discourse.slicer.org/t/shift-mouse-not-placing-on-surface-of-segment/48240

---

## Post #1 by @hherhold (2026-09-23 12:42 UTC)

<p>This is on main, built yesterday on MacBook Pro M5. When I hold down shift in the 3D view to place a crosshair, the crosshair is placed slightly above the segment (see attached image). This does not happen on my Windows machine running 5.12.1. Any ideas? This makes placing markups on 3D models inconsistent across platforms. Do I have some incorrect setting in the latest build? Many thanks!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72c4cc6d0e3d5bc0d67351c6ed55e1656dee59de.jpeg" data-download-href="/uploads/short-url/gni4ndBbO8pRm7XEGoO87KlRurQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72c4cc6d0e3d5bc0d67351c6ed55e1656dee59de_2_690x427.jpeg" alt="image" data-base62-sha1="gni4ndBbO8pRm7XEGoO87KlRurQ" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72c4cc6d0e3d5bc0d67351c6ed55e1656dee59de_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72c4cc6d0e3d5bc0d67351c6ed55e1656dee59de_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72c4cc6d0e3d5bc0d67351c6ed55e1656dee59de_2_1380x854.jpeg 2x" data-dominant-color="84615C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1189 440 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @hherhold (2026-09-23 12:49 UTC)

<p>This also occurs on 5.12.4 amd64 (running under rosetta).</p>

---

## Post #3 by @hherhold (2026-09-23 13:33 UTC)

<p>And also on Windows running 5.12.4.</p>
<p>I actually have a fix for this, with Claude’s help: it looks like it’s associated with “BUG: Keep 3D picking fast when a large surface is shown” (commit 20a81474c0, Aug 2).</p>
<p>Salient points from Claude:</p>
<ol>
<li><strong>The cause:</strong> the 5.12.4 change adds a lookup structure (a cell locator) to large surfaces. With it, VTK’s picker takes the first triangle that comes within the pick tolerance of the ray, not the one the ray actually hits.</li>
<li><strong>The fix:</strong> it doesn’t touch the locator. It first searches for a triangle the ray actually hits, then falls back to the normal tolerance search.</li>
<li><strong>Performance:</strong> a pick still takes microseconds, versus milliseconds before 5.12.4. Rays that miss the surface can take a second search, but even the slowest pick in the benchmark was under 0.1 ms.</li>
</ol>
<p>I’m happy to submit a PR, let me know.</p>

---

## Post #4 by @hherhold (2026-09-23 14:36 UTC)

<p>The thread associated with this change can be found here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9329">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9329" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9329" target="_blank" rel="noopener nofollow ugc">BUG: Keep 3D picking fast when a large surface is shown (#9329)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>pieper:markups-fast-surface-pick</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-08-02" data-time="16:53:49" data-timezone="UTC">04:53PM - 02 Aug 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 11 files with 406 additions and 9 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9329/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+406</span>
            <span class="removed">-9</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">### Symptom
Picking in a 3D view is janky whenever a large surface is shown — mo<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9329" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">st commonly
a segmentation closed surface. Markup control-point dragging (default snap mode
"to visible surface") and hover read-out both pick on every mouse move; hiding
the surface makes interaction smooth again. A plain `forceRender()` of the same
scene is fast (~12 ms), so the cost is in picking, not rendering.

### Cause
`vtkCellPicker` tests **every cell of every pickable surface** unless a spatial
locator is registered for that surface's data. Over a segmentation closed
surface with millions of cells each pick costs tens to hundreds of milliseconds
(measured ~184 ms over a 2.4 M-cell surface; a warmed pick is as slow as the
first, confirming it is brute force, not a one-time build).

### Fix
Add **`vtkMRMLAccuratePicker`** (a `vtkCellPicker` subclass) that registers and
caches a `vtkStaticCellLocator` for each large, pickable surface in the renderer
before every pick — rebuilding a locator only when its surface changes and
dropping it when the surface is hidden. Picks become indexed queries; tolerance,
picked position, and returned normal are unchanged.

Following review feedback, this is **shared per view rather than per widget**:
`vtkMRMLThreeDViewInteractorStyle` now creates a `vtkMRMLAccuratePicker` as the
picker it already hands to `vtkMRMLInteractionEventData`, so every widget — and
anything that needs quick localization in world coordinates — reuses one picker
and one set of locators. This also accelerates the interaction-context / hover
pick (`ComputeAccurateWorldPosition`), not just markups. The markups widget
passes the shared picker to its representation for each interaction event, so
control-point dragging uses it too.

| | before | after |
|---|---|---|
| pick over a 2.4 M-cell surface | ~184 ms | ~0.03 ms |
| scripted control-point drag over the surface | ~184 ms/move | ~0.4 ms/move |

The only residual cost is a one-time locator build (~50 ms for a multi-million
cell surface) on the first pick after such a surface appears — a single frame,
then sub-millisecond. Helps any large surface, not only segmentations.

### Test
`vtkMRMLAccuratePickerTest` picks repeatedly over a 1.6 M-cell surface and
asserts the picks stay fast (&lt; 30 ms/pick). It fails (~78 ms/pick) without the
locator and passes (~0.2 ms/pick) with it; the wide gap keeps it insensitive to
hardware speed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @pieper (2026-09-23 14:38 UTC)

<p>Thanks for catching this and sorry about the regression.</p>
<p>Yes, a PR ideally with a confirmed test to prevent a future regression would be great.</p>

---

## Post #6 by @hherhold (2026-09-23 15:02 UTC)

<p>Okie dokie, I usually do PRs by hand but I’m going to try Claude this time, apologies in advance if it goes wonky.</p>
<p>Edit - spelling error.</p>

---

## Post #7 by @hherhold (2026-09-23 15:27 UTC)

<p>OK, submitted.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9404">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9404" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9404" target="_blank" rel="noopener nofollow ugc">BUG: Keep 3D picked positions on the surface when using cell locators (#9404)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>hherhold:fix-accurate-picker-surface-offset</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-09-23" data-time="15:24:24" data-timezone="UTC">03:24PM - 23 Sep 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/hherhold" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/2367009?v=4" class="onebox-avatar-inline" width="20" height="20">
            hherhold
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 185 additions and 11 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9404/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+185</span>
            <span class="removed">-11</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Since #9329, positions picked in 3D views on large surfaces can land in front of<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9404" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> the surface instead of on it. This is easy to see with the crosshair: Shift + mouse-move over a segmentation closed surface puts the crosshair slightly above the surface. Slicer 5.12.1 puts it on the surface; 5.12.4 does not, on both macOS and Windows.

## Cause

#9329 makes `vtkMRMLAccuratePicker` register a `vtkStaticCellLocator` for each surface with 10,000 or more cells. With a locator, `vtkCellPicker::IntersectDataSetWithLine()` takes the first cell along the ray that intersects the ray within the pick tolerance. `vtkTriangle::IntersectWithLine()` accepts a ray that crosses the plane of the triangle within the tolerance of the triangle, and returns that crossing point. Over a curved surface, that is often a neighboring triangle in front of the one that the ray hits, so the picked position is in front of the surface. Without a locator, `vtkCellPicker` prefers the cell with the smallest parametric distance, which is the cell that the ray passes through.

## Fix

`vtkMRMLAccuratePicker` overrides `IntersectDataSetWithLine()`. For a surface indexed with a locator, it first searches for a cell that the ray hits, and uses the pick tolerance only if the ray does not hit the surface (for example, just outside its silhouette). The first search uses 1e-6 times the pick tolerance rather than zero: with zero tolerance, a ray that passes exactly through a shared edge can miss both triangles due to rounding. Picking stays locator-accelerated.

## Testing

- `vtkMRMLAccuratePickerTest` now also picks a 15 × 15 grid of positions on a bumpy surface (80,000 triangles, about 1 unit wide) and checks that they are on the surface. Without the fix, 197 of 225 positions are off the surface, by up to 9e-4. With the fix, none are (largest distance 2e-16). The existing speed check still passes.
- MRMLDisplayableManager and Markups tests pass.
- Checked interactively on macOS with a segmentation closed surface: the crosshair is on the surface.

Pick times with the VTK of Slicer 5.12.4 (Apple M5 Max), for a grid of picks over a whole 2000 × 550 view:

| Surface | Without locator (up to 5.12.3) | With locator (5.12.4) | This PR |
|---|---|---|---|
| 124k triangles | 1.7 ms | 8 µs (16 µs on the surface) | 14 µs (15 µs on the surface) |
| 588k triangles | 7.6 ms | 9 µs (26 µs on the surface) | 15 µs (19 µs on the surface) |

Rays that miss the surface can take a second locator search. These times were measured in Python by running a second pick for those rays, which overstates their cost; the slowest pick was under 0.1 ms.

## Backport

Please add the `backport:5.x` label (I can't set labels): #9329 was backported to 5.12, so 5.12.4 has this issue.

🤖 Generated with [Claude Code](https://claude.com/claude-code)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @hherhold (2026-09-23 16:56 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  I have to say, the speedup in placing markups is a game changer for me.</p>

---
