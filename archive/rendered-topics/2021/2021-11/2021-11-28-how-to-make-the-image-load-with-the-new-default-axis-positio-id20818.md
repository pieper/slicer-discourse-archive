# How to make the image load with the new default axis position

**Topic ID**: 20818
**Date**: 2021-11-28
**URL**: https://discourse.slicer.org/t/how-to-make-the-image-load-with-the-new-default-axis-position/20818

---

## Post #1 by @slicer365 (2021-11-28 14:51 UTC)

<p>About craniocerebral images,</p>
<p>the patient’s head is tilted.</p>
<p>I use Slicer to adjust it. For example, after adjusting with ACPC, I export the data to nrrd format. When I re-import, the default formatted orientation is loaded. It’s not the axis, it is reformt.</p>

---

## Post #2 by @pieper (2021-11-28 15:00 UTC)

<p>Be sure to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the transform</a> before saving if you want it included in the nrrd file.</p>

---

## Post #3 by @slicer365 (2021-11-28 23:41 UTC)

<p>Thank you for your answer!</p>
<p>Yes,I harden it .</p>
<p>However ,when I re-import the nrrd file ,the Red view is Reformat，as is shown in this picture.</p>
<p>I need to manually adjust it back to the axis position</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/100a10586b7f57a92fccb0e0563aab2ecff0f89f.png" alt="捕获" data-base62-sha1="2hTctvsuKGNp8kU0cgoz8BEfEBx" width="346" height="326"></p>

---

## Post #4 by @pieper (2021-11-29 15:12 UTC)

<p>Perhaps this change from late January 2021 is at the root of the issue you are reporting:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/9c7cf1c219b2ee8987897ee1498b0ab9dff3f2f5">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/9c7cf1c219b2ee8987897ee1498b0ab9dff3f2f5" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/9c7cf1c219b2ee8987897ee1498b0ab9dff3f2f5" target="_blank" rel="noopener">ENH: Make slice views aligned with image axes by default (#5417)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-01-29" data-time="22:15:19" data-timezone="UTC">10:15PM - 29 Jan 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 9 files with 155 additions and 61 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/9c7cf1c219b2ee8987897ee1498b0ab9dff3f2f5" target="_blank" rel="noopener">
          <span class="added">+155</span>
          <span class="removed">-61</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Users were confused by showing reformatted images by default, therefore image di<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/9c7cf1c219b2ee8987897ee1498b0ab9dff3f2f5" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">splay actions are changed to facilitate axis-aligned display.
Slice views are rotated to be aligned with closest image axes if:
- Volume selection is propagated - for example when a volume is loaded or a CLI completes execution. Unless if a view is excluded by setting vtkMRMLSliceCompositeNode::DoPropagateVolumeSelection to false or "show" option is disable in Add data dialog.
- In Data module / Subject hierarchy tree -&gt; eye icon is clicked. Unless "Reset view orientation on show" checkbox (checked by default) is unchecked in context menu of the eye icon.
- Dragging a volume from Data module / Subject hierarchy tree to a view. Unless "Reset view orientation on show" checkbox (checked by default) is unchecked in context menu of the eye icon.

fixes #5379</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2021-11-29 15:21 UTC)

<p>The feature of allowing automatic alignment of slice views to image axes was added because most people came to Slicer from using 2D image viewers and they did not understand what was happening to their images. For users who understand the concept of reformatted views and prefer to work in anatomical orientations, the automatic alignment feature <a href="https://discourse.slicer.org/t/slice-view-orientation-of-oblique-rotated-volumes-aligned-to-volume-or-anatomical-axes/20092/2">can be disabled by right-clicking in the subject hierarchy tree</a>.</p>

---
