---
topic_id: 8766
title: "Cannot Import Pydicom"
date: 2019-10-13
url: https://discourse.slicer.org/t/8766
---

# Cannot import pydicom

**Topic ID**: 8766
**Date**: 2019-10-13
**URL**: https://discourse.slicer.org/t/cannot-import-pydicom/8766

---

## Post #1 by @fedorov (2019-10-13 14:31 UTC)

<p>In the current nightly binary, neither <code>import dicom</code> nor <code>import pydicom</code> work. Is there a new way to import pydicom?</p>

---

## Post #2 by @fedorov (2019-10-13 14:58 UTC)

<p>Same runtime issue for DICOMPatcher, so at least it’s not just me…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f44350c95b015be310fa19fe4b6aba20bec110e2.png" data-download-href="/uploads/short-url/yQQIZJM4kBoM0230z9cGu48Dd5M.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f44350c95b015be310fa19fe4b6aba20bec110e2_2_690x110.png" alt="image" data-base62-sha1="yQQIZJM4kBoM0230z9cGu48Dd5M" width="690" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f44350c95b015be310fa19fe4b6aba20bec110e2_2_690x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f44350c95b015be310fa19fe4b6aba20bec110e2_2_1035x165.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f44350c95b015be310fa19fe4b6aba20bec110e2_2_1380x220.png 2x" data-dominant-color="FAE9E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1806×288 63.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2019-10-13 15:33 UTC)

<p>Thanks for reporting.  There have been several commits lately moving to standardized upstream python sources (e.g. see <a href="https://github.com/Slicer/Slicer/commit/f348d6f5bf977204e726146ec5b3f46143ff9109">this</a> and <a href="https://github.com/Slicer/Slicer/commit/fa6c90c5bf3dc9def76a144d8bb0e734e1bdbfea">this</a>).  I suspect it may take a few days for the packaging to settle out.</p>

---

## Post #4 by @lassoan (2019-10-13 20:47 UTC)

<p>The DICOM packages are missing even from the build tree.</p>

---

## Post #5 by @jamesobutler (2019-10-13 23:26 UTC)

<p>I’ll take a look. Thanks for the report!</p>

---

## Post #6 by @fedorov (2019-10-16 15:24 UTC)

<p>This issue was resolved by <a class="mention" href="/u/jamesobutler">@jamesobutler</a> in this PR, and confirmed working in today’s nightly.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1231" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/1231" target="_blank" rel="nofollow noopener">COMP: Fix python-dicom-requirements not installing</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:fix-pydicom</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-10-15" data-time="02:26:53" data-timezone="UTC">02:26AM - 15 Oct 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="nofollow noopener">
          <img alt="jamesobutler" src="https://avatars1.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 22 additions and 57 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/1231/files" target="_blank" rel="nofollow noopener">
          <span class="added">+22</span>
          <span class="removed">-57</span>
        </a>
      </div>
    </div>

  </div>
</div>
  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thank you James for the quick fix! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #7 by @jamesobutler (2019-11-02 14:38 UTC)

<p>It has broken again. I’m taking a look at the project dependencies again…</p>

---

## Post #8 by @lassoan (2019-11-03 02:05 UTC)

<p>OK. To fix the issue, I’ve reverted the latest python package related commit (<a href="https://github.com/Slicer/Slicer/commit/47a8e5b90fe7ca2ce2e3834a8f2b1019413907e5">https://github.com/Slicer/Slicer/commit/47a8e5b90fe7ca2ce2e3834a8f2b1019413907e5</a><br>
).</p>

---

## Post #9 by @jamesobutler (2019-11-03 17:21 UTC)

<p>Can anyone provide any sort of support for what I asked about in <a href="https://github.com/Slicer/Slicer/pull/1231#issue-328045247" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1231#issue-328045247</a>?</p>

---

## Post #10 by @jamesobutler (2019-11-03 21:49 UTC)

<p>PR is up to fix the issue <a href="https://github.com/Slicer/Slicer/pull/1246" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1246</a></p>

---

## Post #11 by @lassoan (2019-11-04 02:15 UTC)

<p>1246 is merged.</p>
<p>Do you still need help with <a href="https://github.com/Slicer/Slicer/pull/1231#issue-328045247">https://github.com/Slicer/Slicer/pull/1231#issue-328045247</a>?</p>

---

## Post #12 by @jamesobutler (2019-11-04 03:05 UTC)

<p>The python dependencies still don’t seem to be handled as I would expect. Most fixes have been trial and error so far.</p>

---
