# Segmentation masks disappears from 2d views after histogram thresholding (but not 3d)

**Topic ID**: 34199
**Date**: 2024-02-07
**URL**: https://discourse.slicer.org/t/segmentation-masks-disappears-from-2d-views-after-histogram-thresholding-but-not-3d/34199

---

## Post #1 by @bbkonk (2024-02-07 23:15 UTC)

<p>Not sure if this is a Slicer issue or a MONAI issue, but I’ve only hit the issue so far using the MONAILabel and MONAILabel Reviewer plugins. When I use threshold an image and see, for example Editable area = Inside segment_1), after “Apply” the segmentation mask for that label disappears from all 2d views. Any paint etc. drawing done after that point similarly does not appear in the 2d views. I do however see the label in the 3d view (including post-threshold values and any modifications I make with paint etc.).</p>

---

## Post #2 by @bbkonk (2024-02-08 13:35 UTC)

<p>I’ve tried a few versions including the stable 5.6.1 and the 5.7.0 release.</p>

---

## Post #3 by @lassoan (2024-02-11 11:50 UTC)

<p>The issue is fixed now in the Slicer Preview Release.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7577">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7577" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7577" target="_blank" rel="noopener">BUG: Fix segment disappearing when sharing segment editor node between widgets</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-segment-disappear</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-02-09" data-time="13:22:18" data-timezone="UTC">01:22PM - 09 Feb 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 88 additions and 57 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7577/files" target="_blank" rel="noopener">
            <span class="added">+88</span>
            <span class="removed">-57</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When a single vtkMRMLSegmentEditorNode was used by multiple qSlicerSegmentEditor<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7577" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">Widget instances then after using Threshold effect, the current segment disappeared from slice views.

The reason was that Threshold effects in every segment editor widgets get activated (via sharing the segment editor node) and they all started preview, saved original segment opacity, and then on "Apply" restored the original segment opacity. However, the segment opacity that was restored by second, third, etc. effects were not the original anymore, but it was already the opacity that was set to 0 (it has to be set to 0 to prevent the current segment occluding the preview).

The solution could have been to store the original opacity in a shared location (e.g., in the segment editor node), but that would not have solved the slight rendering issue (preview glow was darker) and performance degradation caused by several effects showing the preview glow at the same time.

Fixed it by storing the object ID of the threshold effect that manipulates the segmentation display node in the node's "SegmentEditor.PreviewingEffect" attribute. All other Threshold effects check this attribute and if they find that another effect already provide preview then they don't display the preview.

This commit also fixes disappearing segment when selecting another segmentation node while the Threshold effect is active.

fixes #6874</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
