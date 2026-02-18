# DICOM gray level normalization , 3 sigma normalization

**Topic ID**: 18518
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/dicom-gray-level-normalization-3-sigma-normalization/18518

---

## Post #1 by @hamdullaherk (2021-07-05 14:09 UTC)

<p>Hi, I am a radiologist who is interests in texture analysis and radomics.<br>
I am a beginner at 3Dslicer. Firstly I want to ask, how can I use 3sigma normalization technique in DICOM images. I don’t know how can ı do it? can you help me?<br>
Thanks.</p>

---

## Post #2 by @pieper (2021-07-13 20:11 UTC)

<p>Some normalization can be done in pyradiomics as part of that analysis:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/pull/209">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/pull/209" target="_blank" rel="noopener">github.com/AIM-Harvard/pyradiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AIM-Harvard/pyradiomics/pull/209" target="_blank" rel="noopener">Implement normalization function in imageoperations</a>
    </h4>

    <div class="branches">
      <code>AIM-Harvard:master</code> ← <code>JoostJM:add-normalize-function</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-02-22" data-time="08:42:29" data-timezone="UTC">08:42AM - 22 Feb 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/JoostJM" target="_blank" rel="noopener">
          <img alt="JoostJM" src="https://avatars.githubusercontent.com/u/18026947?v=4" class="onebox-avatar-inline" width="20" height="20">
          JoostJM
        </a>
      </div>

      <div class="lines" title="2 commits changed 3 files with 99 additions and 31 deletions">
        <a href="https://github.com/AIM-Harvard/pyradiomics/pull/209/files" target="_blank" rel="noopener">
          <span class="added">+99</span>
          <span class="removed">-31</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Optionally normalize gray value intensities before any resampling or filters are<span class="show-more-container"><a href="https://github.com/AIM-Harvard/pyradiomics/pull/209" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> applied. Image is normalized on all gray values (not just those in the ROI). Disabled by default. Controlled by 3 new params (`normalize`, `normalizeScale` and `removeOutliers`).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or you could use numpy operations on the pixel data to implement the statistics and normalization in a few lines.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume</a></p>

---
