---
topic_id: 21602
title: "Markups Jump Slices Functionality Is Broken On Preview"
date: 2022-01-24
url: https://discourse.slicer.org/t/21602
---

# Markups Jump Slices functionality is broken on preview

**Topic ID**: 21602
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/markups-jump-slices-functionality-is-broken-on-preview/21602

---

## Post #1 by @muratmaga (2022-01-24 20:05 UTC)

<p>Tested with latest preview on Linux. Clicking on the control points do not jump the slice view to those coordinates.<br>
There is no error message that I can see.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @jamesobutler (2022-01-24 20:30 UTC)

<p>For me clicking on rows in the control points table does not respect the “Jump Slices” option in the Markups module. However, clicking on the control points in the slice view does work except that it always does the “Jump slices - centered” option.</p>
<p>It is a bit unclear to me what the difference might be between the jump slices option in the “Crosshair Selection” toolbar and the jump slices option in the markups module. Does the toolbar method change what happens when you click on the point in the slice views? If so, it doesn’t appear to respect that option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a1b08cf774d5886fa9a3a5d2aa881eee6aabd2.png" data-download-href="/uploads/short-url/iMsXXz0sgRQ9RkNCUjUJXv8Wk1Q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a1b08cf774d5886fa9a3a5d2aa881eee6aabd2_2_690x373.png" alt="image" data-base62-sha1="iMsXXz0sgRQ9RkNCUjUJXv8Wk1Q" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a1b08cf774d5886fa9a3a5d2aa881eee6aabd2_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a1b08cf774d5886fa9a3a5d2aa881eee6aabd2_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a1b08cf774d5886fa9a3a5d2aa881eee6aabd2_2_1380x746.png 2x" data-dominant-color="8C8C8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1522×824 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2022-01-24 21:25 UTC)

<p>Indeed, “Jump slices” in Markups module is indeed broken in the latest Slicer Preview Release. It would be great if <a class="mention" href="/u/smrolfe">@smrolfe</a> could fix this before Slicer5 is released (as always, within 1-2 weeks).</p>
<p>Other things seem to work as intended:</p>
<ul>
<li>Jump slices option in the Crosshair toolbar button controls how the slices are moved if the crosshair is moved (using Shift+MouseMove). By default, “offset” mode is used so that Shift+MouseMove can be used for slice browsing.</li>
<li>Clicking on a control point in a slice view always uses “centered” mode, as typically you want to see that point and “offset” mode does not guarantee this (even if the point is visible, it may be very hard to find if not centered and there are other points in the same plane).</li>
</ul>

---

## Post #4 by @smrolfe (2022-01-24 21:36 UTC)

<p>Thanks, I am looking into this (and the ROI color issue) now!</p>

---

## Post #5 by @smrolfe (2022-01-28 02:09 UTC)

<p>I submitted a fix for the broken “jump slices” function and a <a href="https://discourse.slicer.org/t/syncing-markups-edit-state-with-control-point-lock/21606/2">related bug </a> in the pull request:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6142">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6142" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6142" target="_blank" rel="noopener nofollow ugc">BUG: Adds varying colors to ROIs added as a single node</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>smrolfe:ROIColor</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-01-28" data-time="02:01:23" data-timezone="UTC">02:01AM - 28 Jan 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/smrolfe" target="_blank" rel="noopener nofollow ugc">
          <img alt="smrolfe" src="https://avatars.githubusercontent.com/u/43060230?v=4" class="onebox-avatar-inline" width="20" height="20">
          smrolfe
        </a>
      </div>

      <div class="lines" title="1 commits changed 6 files with 47 additions and 48 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6142/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+47</span>
          <span class="removed">-48</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit addresses issue: https://github.com/Slicer/Slicer/issues/5912

The<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6142" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> color assigned to a ROI created using the single node placement buttons in the Markups module and Markups Toolbar are varied to be consistent with the varying color of nodes created using continuous placement mode.

The colormap used for the ROIs is changed from the vtkMRMLColorTableNodeRandom to MediumChartColors, which are more distinguishable.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
