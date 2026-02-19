---
topic_id: 24396
title: "Incomplete Python Wrapping Of Vtksegmentation"
date: 2022-07-19
url: https://discourse.slicer.org/t/24396
---

# Incomplete Python Wrapping of vtkSegmentation

**Topic ID**: 24396
**Date**: 2022-07-19
**URL**: https://discourse.slicer.org/t/incomplete-python-wrapping-of-vtksegmentation/24396

---

## Post #1 by @edwardwang1 (2022-07-19 17:48 UTC)

<p>Hi there,</p>
<p>As per my other <a href="https://discourse.slicer.org/t/converting-segmentationnode-to-labelmap-takes-a-long-time-through-python/23696/8">thread</a>, I have been trying to access some C++ functions through Python. Specifically, I am trying to access the <a href="https://apidocs.slicer.org/master/classvtkSegmentation.html#a30d20a695d3e12469f4a176afe61f4e6" rel="noopener nofollow ugc">GetPossibleConversions</a> function of vtkSegmentation. The function was not available through Release Slicer(4.11 and 5.1). I have just built Slicer5.1 (and SlicerRT) from source on Windows 10, and the function is still not available.</p>
<p>Could someone point me to some documentation on how to wrapping VTK objects for Python? My understanding is that the process should be automatic, but I can’t figure out why some functions are wrapped and not others.</p>
<p>Thanks,<br>
Edward</p>

---

## Post #2 by @lassoan (2022-07-19 23:50 UTC)

<p>This method returns a very complex structure (vector of C++ object vectors and associated values), that cannot be automatically Python-wrapped. In the next two weeks I’ll add Python-wrappable, vtkObject based classes for storing segmentation conversion paths and parameters. These will make conversion methods available in Python.</p>

---

## Post #3 by @edwardwang1 (2022-07-20 00:21 UTC)

<p>Hey Andras,</p>
<p>Thanks for doing this for me. If there’s any way that I can help (i.e. testing), please let me know. I’m unfamiliar with C++ but willing to learn!</p>

---

## Post #4 by @lassoan (2022-08-21 07:58 UTC)

<p>The pull request that allows custom segment conversions via Python interface is under review and it’ll be most likely integrated in a few days:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6507">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6507" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6507" target="_blank" rel="noopener">ENH: Expose segment conversion paths in Python</a>
    </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:python-compatible-segment-conversion-api</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-08-20" data-time="18:09:55" data-timezone="UTC">06:09PM - 20 Aug 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 20 files with 1061 additions and 318 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6507/files" target="_blank" rel="noopener">
          <span class="added">+1061</span>
          <span class="removed">-318</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Previously, complex STL containers were used that were not Python-wrappable. Now<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6507" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> conversion paths and parameters are all VTK objects.
This allows converting segmentations using a custom path, when there are multiple conversion paths are available.
For example, multiple conversion paths are available after installing SlicerRT extension, which provides additional segment representations and conversion rules.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
