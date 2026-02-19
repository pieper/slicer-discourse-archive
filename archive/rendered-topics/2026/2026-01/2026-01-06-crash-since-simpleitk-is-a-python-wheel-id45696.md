---
topic_id: 45696
title: "Crash Since Simpleitk Is A Python Wheel"
date: 2026-01-06
url: https://discourse.slicer.org/t/45696
---

# Crash since SimpleITK is a python wheel

**Topic ID**: 45696
**Date**: 2026-01-06
**URL**: https://discourse.slicer.org/t/crash-since-simpleitk-is-a-python-wheel/45696

---

## Post #1 by @chir.set (2026-01-06 19:45 UTC)

<p>This line simply crashes Slicer since SimpleITK is no longer built:</p>
<p><code>import SimpleITK as sitk</code></p>
<p>Selecting the <code>Filters/Simple filters</code> menu item also crashes Slicer.</p>
<p>How can these troubles be solved?</p>
<p>Using <code>5.11.0-2026-01-04 r34365 / fa5d139</code> on Linux.</p>
<p>Thanks.</p>

---

## Post #2 by @jamesobutler (2026-01-06 22:04 UTC)

<p>Issue currently tracked and being discussed at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8947">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8947" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8947" target="_blank" rel="noopener nofollow ugc">Segmentation fault when importing SimpleITK in PythonSlicer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-01-06" data-time="16:57:26" data-timezone="UTC">04:57PM - 06 Jan 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/vboussot" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/17681131?v=4" class="onebox-avatar-inline" width="20" height="20">
          vboussot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Importing SimpleITK in Slicer’s bundled Python (PythonSlicer) causes<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> an immediate segmentation fault on Linux.

This issue affects all Slicer extensions that rely on SimpleITK, since any attempt to import SimpleITK in the Slicer Python environment crashes the interpreter, making such extensions unusable.

## Steps to reproduce

The issue is reproducible both in a Linux source build and in the Slicer Preview Release 5.11.0 (revision 34365, built 2026-01-06) using Python 3.12.10.

1) Launch Slicer or use the bundled Python interpreter (`PythonSlicer`).
2) In the Python interpreter, run: import SimpleITK
3) Actual behavior: Slicer (or `PythonSlicer`) crashes immediately with a segmentation fault.

## Environment
- Slicer version: Slicer-5.11.0 revision 34365 built 2026-01-06 
- Operating system: Linux</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @chir.set (2026-01-07 10:19 UTC)

<p>It is being resolved in that thread indeed, thank you.</p>

---
