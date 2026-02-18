# Problem changing the individual segment opacity in slice views

**Topic ID**: 24810
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/problem-changing-the-individual-segment-opacity-in-slice-views/24810

---

## Post #1 by @jamesobutler (2022-08-17 14:18 UTC)

<p>I’m having trouble changing an individual segment’s opacity and was wondering if this was a bug or expected behavior.</p>
<p>I set the segmentation wide slice fill opacity to 1.0, and then set the individual segment opacity to 0.5.  I observe that the segment in the 3D window changes appropriately to 50% opacity, but the opacity is not also changed in the slice views. Should the opacity value defined for the individual segment here in the Segmentations module apply to both the “3D” and “Slice fill” opacity? The [documentation] indicates that segment opacity and segmentation opacity should be multiplied. In this case 1 * 0.5 = 0.5 opacity for Slice fill for “Segment_1”.</p>
<p>I have observed this behavior in Slicer 5.0.3 (latest stable), Slicer 5.1.0-2022-08-16 (latest preview) and also Slicer 4.11.20210226 (former stable).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d07d6733feda20ea632ec9f8b2971ed4fe715a94.png" data-download-href="/uploads/short-url/tKnZj5daMWo7v6OjKQ36cWt3rrC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07d6733feda20ea632ec9f8b2971ed4fe715a94_2_690x370.png" alt="image" data-base62-sha1="tKnZj5daMWo7v6OjKQ36cWt3rrC" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07d6733feda20ea632ec9f8b2971ed4fe715a94_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07d6733feda20ea632ec9f8b2971ed4fe715a94_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07d6733feda20ea632ec9f8b2971ed4fe715a94_2_1380x740.png 2x" data-dominant-color="97989C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2022-08-17 14:33 UTC)

<p>I see now that the hovertip for the “Opacity” table header says it is the segment opacity specifically for the 3D views. Is there a reason why this column is ultimately just calling <code>SetSegmentOpacity3D</code> rather than <code>SetSegmentOpacity</code> which would set the value for 2D Fill and 3D to be the same? The general term for the column header of “Opacity” seems like it should manipulate both, while the header should be “3D Opacity” if it really is only supposed to manipulate the 3D views and indicated by the tooltip.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/164f51c39d8c88ac432fb0baa9583e3db3d4b835.png" alt="image" data-base62-sha1="3bmrBY84c1WVBdpKlHamRvjYpcV" width="232" height="65"></p>

---

## Post #3 by @jamesobutler (2022-08-17 15:02 UTC)

<p>I’ve issued the following PR which changes the opacity widget in the segments table to update not only Segment Opacity 3D, but also 2D Fill and 2D Outline.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6506">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6506" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6506" target="_blank" rel="noopener nofollow ugc">ENH: Segment table opacity changes all segment opacity</a>
    </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:segment-table-opacity-fill</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-08-17" data-time="15:01:28" data-timezone="UTC">03:01PM - 17 Aug 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 15 additions and 3 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6506/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+15</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://discourse.slicer.org/t/problem-changing-the-individual-segment-opaci<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6506" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ty-in-slice-views/24810

Previously the opacity widget in the segments table would only change the 3D segment opacity.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
