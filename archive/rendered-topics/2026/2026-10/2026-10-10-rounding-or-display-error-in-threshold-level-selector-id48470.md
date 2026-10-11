---
topic_id: 48470
title: "Rounding or display error in threshold level selector"
date: 2026-10-10
url: https://discourse.slicer.org/t/48470
last_bumped: 2026-10-10T16:52:09.698Z
---

# Rounding or display error in threshold level selector

**Topic ID**: 48470
**Date**: 2026-10-10
**URL**: https://discourse.slicer.org/t/rounding-or-display-error-in-threshold-level-selector/48470

---

## Post #1 by @muratmaga (2026-10-10 15:31 UTC)

<p>This is with the latest stable, but I have seen this issue with the float volumes before I don’t think it is new. The gist it cannot capture the true max and it leaves some of the voxels unselected.</p>
<p>Unselected region values are around 33.317… and should be included in the selection (since the max is set to 33.32). I cannot manually change the value either. So I think the internal selection logic is not using the same level of precision as the widget displaying selected threshold range</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8d46a34394d840846f9c0b497cb609a0a7fe920.jpeg" data-download-href="/uploads/short-url/uWaehtSNdPXs2vOCxeLvkhJO3XG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8d46a34394d840846f9c0b497cb609a0a7fe920_2_655x500.jpeg" alt="image" data-base62-sha1="uWaehtSNdPXs2vOCxeLvkhJO3XG" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8d46a34394d840846f9c0b497cb609a0a7fe920_2_655x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8d46a34394d840846f9c0b497cb609a0a7fe920_2_982x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8d46a34394d840846f9c0b497cb609a0a7fe920_2_1310x1000.jpeg 2x" data-dominant-color="A5AEA6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1401×1069 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Tried increasion the digits and enter the exact max value that’s being excluded and had no effect.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/109852728c8e32d62fc0b6585fbe0810216ef43d.jpeg" data-download-href="/uploads/short-url/2mNZg0KuFfFnSPvjSFhry37hnGJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/109852728c8e32d62fc0b6585fbe0810216ef43d_2_690x425.jpeg" alt="image" data-base62-sha1="2mNZg0KuFfFnSPvjSFhry37hnGJ" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/109852728c8e32d62fc0b6585fbe0810216ef43d_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/109852728c8e32d62fc0b6585fbe0810216ef43d_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/109852728c8e32d62fc0b6585fbe0810216ef43d_2_1380x850.jpeg 2x" data-dominant-color="B9BFB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1387×856 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-10-10 16:52 UTC)

<p>I opened a PR with help of claude:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9457">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9457" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9457" target="_blank" rel="noopener nofollow ugc">BUG: Fix loss of precision of floating-point segment editor effect parameters (#9457)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>muratmaga:fix-effect-double-parameter-precision</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-10-10" data-time="16:48:11" data-timezone="UTC">04:48PM - 10 Oct 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
            muratmaga
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 21 additions and 2 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9457/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+21</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Segment editor effects store `double` parameters via `QString::number(value)`, w<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9457" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">hich uses 6 significant
digits. `doubleParameter()` therefore returns a different value than what was set.

Most visible in the Threshold effect on floating-point volumes: setting the maximum threshold to the
volume maximum (e.g. 33.31780242919922) stores "33.3178", so voxels at the maximum are excluded in both
the preview and Apply, regardless of the slider's displayed decimals.
Reported in https://discourse.slicer.org/t/rounding-or-display-error-in-threshold-level-selector/48470

Fix: use `QLocale::FloatingPointShortest`, the shortest string that converts back to the exact same
double, in `setParameter(QString, double)` and `setCommonParameter(QString, double)`. Integer-valued and
short decimal values are stored the same as before (e.g. "0.1", "848").

Added `TestSection_DoubleParameterPrecision` to `SegmentationsModuleTest2`; it fails on Slicer 5.12.4
(33.31780242919922 -&gt; 33.3178, 123456.7 -&gt; 123457).

🤖 Generated with [Claude Code](https://claude.com/claude-code)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---
