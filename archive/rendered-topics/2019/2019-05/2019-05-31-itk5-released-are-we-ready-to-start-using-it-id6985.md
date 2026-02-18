# ITK5 released, are we ready to start using it?

**Topic ID**: 6985
**Date**: 2019-05-31
**URL**: https://discourse.slicer.org/t/itk5-released-are-we-ready-to-start-using-it/6985

---

## Post #1 by @pieper (2019-05-31 19:31 UTC)

<p>Now that ITK5 is officially out, are there any roadblocks to updating slicer?</p>
<p>(and congrats to the ITK team! <img src="https://emoji.discourse-cdn.com/twitter/trumpet.png?v=12" title=":trumpet:" class="emoji" alt=":trumpet:" loading="lazy" width="20" height="20"> )</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.itk.org/t/itk-5-0-0-has-been-released/1931">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/itk-5-0-0-has-been-released/1931" target="_blank" rel="noopener" title="07:19PM - 31 May 2019">ITK – 31 May 19</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/211;"><img src="https://discourse.itk.org/uploads/default/optimized/1X/12d1f73f47d43ae60c9c48d9ba6fff49558bd291_2_1024x314.jpeg" class="thumbnail" width="690" height="211"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.itk.org/t/itk-5-0-0-has-been-released/1931" target="_blank" rel="noopener">ITK 5.0.0 has been released!</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #ED207B;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Announcements</span>
        </span>
      </span>
  </div>
</div>

  <p>We are happy to announce the Insight Toolkit (ITK) 5.0.0! 🎉 ITK is an open-source, cross-platform toolkit for N-dimensional scientific image processing, segmentation, and registration.  ITK 5.0.0 is a major release that features an incredible...</p>

  <p>
    <span class="label1">Reading time: 6 mins 🕑</span>
      <span class="label2">Likes: 24 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @jcfr (2019-05-31 19:34 UTC)

<p>The good news is that ITK community has been very proactive and helped us transition to ITK5, we are already using 5.0.rc01.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/87105dfbfa055518bf724a880969d423a273b2c1/SuperBuild/External_ITK.cmake#L34-L36" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/87105dfbfa055518bf724a880969d423a273b2c1/SuperBuild/External_ITK.cmake#L34-L36" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/87105dfbfa055518bf724a880969d423a273b2c1/SuperBuild/External_ITK.cmake#L34-L36</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="34" style="counter-reset: li-counter 33 ;">
<li>ExternalProject_SetIfNotDefined(</li>
<li>  Slicer_${proj}_GIT_TAG</li>
<li>  "e8acd1230a9313a39f3ed18374acc62a92463dfa" # 5.0.rc01 (2019-01-30) + backports: DCMTK + ITKDeprecated</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Updating to use the ITKv5 final version should require less work.</p>

---

## Post #3 by @pieper (2019-05-31 20:34 UTC)

<p>That’s great <a class="mention" href="/u/jcfr">@jcfr</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p><a class="mention" href="/u/siaeleni">@siaeleni</a> and I have an extension we’d like to submit but there was one small build error so we we’ve been holding back until Slicer moves to the new version.  There’s no particular rush, but it’s good to know there aren’t any other showstoppers.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SNRLab/LineMarkerRegistration/pull/3">
  <header class="source">

      <a href="https://github.com/SNRLab/LineMarkerRegistration/pull/3" target="_blank" rel="noopener">github.com/SNRLab/LineMarkerRegistration</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SNRLab/LineMarkerRegistration/pull/3" target="_blank" rel="noopener">ENH: create extension and port to ITKv5</a>
      </h4>

    <div class="branches">
      <code>SNRLab:master</code> ← <code>pieper:master</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2019-05-07" data-time="20:29:53" data-timezone="UTC">08:29PM - 07 May 19 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="2 commits changed 9 files with 88 additions and 30 deletions">
          <a href="https://github.com/SNRLab/LineMarkerRegistration/pull/3/files" target="_blank" rel="noopener">
            <span class="added">+88</span>
            <span class="removed">-30</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit moves the LineMarkerRegistration module
into a subdirectory and als<span class="show-more-container"><a href="https://github.com/SNRLab/LineMarkerRegistration/pull/3" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">o modernizes the code
with a few C++ 11 and ITK v5 updates.

Note that to avoid a build error related to std::vector
of bool on mac, ITK should include the following patch:
https://github.com/InsightSoftwareConsortium/ITK/pull/486/files</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
