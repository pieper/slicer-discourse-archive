---
topic_id: 43123
title: "Slicerradiomics Extension Not Showing Up On Macos 15 5 Slice"
date: 2025-05-27
url: https://discourse.slicer.org/t/43123
---

# SlicerRadiomics Extension Not Showing Up on macOS 15.5 (Slicer 5.9.0 Preview)

**Topic ID**: 43123
**Date**: 2025-05-27
**URL**: https://discourse.slicer.org/t/slicerradiomics-extension-not-showing-up-on-macos-15-5-slicer-5-9-0-preview/43123

---

## Post #1 by @Raghad (2025-05-27 22:24 UTC)

<p>Hi,</p>
<p>I’m trying to install and use the <strong>SlicerRadiomics</strong> extension on my Mac, but I haven’t been able to get it to show up, despite following all the instructions.</p>
<p>System Info:</p>
<ul>
<li><strong>macOS version</strong>: 15.5 (Sequoia)</li>
<li><strong>Slicer version</strong>: 5.9.0-2025-05-25 r33658 (Preview build)</li>
<li><strong>Slicer install location</strong>: Application moved to <code>/Applications</code> as required</li>
</ul>
<p>What I Tried:</p>
<ol>
<li>Opened the Extension Manager and searched for <strong>“Radiomics”</strong> — nothing appeared.</li>
<li>Verified I’m using the <strong>Preview</strong>, not Stable.</li>
<li>Downloaded the zipped folders from GitHub: <code>SlicerRadiomics</code> and <code>SlicerRadiomicsCLI</code></li>
<li>Tried manually adding the module path under the <strong>Modules &gt; Add Modules</strong> option, but it still doesn’t show up.</li>
<li>Tried the link to download the compiled extension:<br>
<code>https://slicer-packages.kitware.com/catalog/All/33658/macosx</code> — but it’s not working.</li>
</ol>
<p>Questions:</p>
<ul>
<li>Is the SlicerRadiomics extension still unavailable for macOS?</li>
<li>Is there a manual installation method that works currently?</li>
<li>If not, what’s the best workaround? (e.g., using PyRadiomics in Python after segmentation in Slicer?)</li>
</ul>
<p>I’d really appreciate any help, especially if anyone has gotten this to work on a Mac recently.</p>
<p>Thanks so much!</p>

---

## Post #2 by @jamesobutler (2025-05-27 22:32 UTC)

<p>Similar to the following post:</p><aside class="quote quote-modified" data-post="1" data-topic="35637">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicerradiomics-extension-on-mac/35637">SlicerRadiomics extension on Mac</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello! 
I just downloaded Slicer 5.7.0. on my Macbook “Ventura 13.2.1”.  I wanted to use the SlicerRadiomics extension but I couldn’t find it. I’ve since caught up with the issue in this forum. 
I wanted to kindly ask if there have been any updates regarding this problem. 
I read that, for the time being, the best course of action was to download a previous Slicer version. However, I couldn’t access versions prior to Slicer 4 and I’ve found that these issues with SlicerRadiomics were present sin…
  </blockquote>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/issues/77">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/77" target="_blank" rel="noopener nofollow ugc">github.com/AIM-Harvard/SlicerRadiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/77" target="_blank" rel="noopener nofollow ugc">SlicerRadiomics unavailable for macOS since Slicer Preview 5.3.0 as of 2023-03-31</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-04-21" data-time="15:25:26" data-timezone="UTC">03:25PM - 21 Apr 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The SlicerRadiomics extension has had build errors since March 31st, 2023 that h<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">as made it unavailable on macOS 
https://slicer.cdash.org/viewBuildError.php?buildid=2985286

It is unable to build a macOS whl of [`pyradiomics`](https://github.com/AIM-Harvard/pyradiomics). Around the time when this extension started to fail,
- The Slicer factory macOS machine was updated from macOS 10.13 (High Sierra) to macOS 13.0 (Ventura). See https://discourse.slicer.org/t/transition-of-macos-preview-build-from-host-10-13-high-sierra-to-13-ventura/28668. 
- Also the minimum required macOS deployment was changed to macOS 11.0 in https://github.com/Slicer/Slicer/commit/592ee0b516cd8cb448ab897c312ee6e4458dbb11.

cc: @JoostJM @fedorov</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> I see you have recently <a href="https://github.com/AIM-Harvard/pyradiomics/commits/master/?author=hjmjohnson" rel="noopener nofollow ugc">pushed a lot</a> of maintenance related work to the <code>pyradiomics</code> project. Do you intend to also update the SlicerRadiomics extension to use the latest? Currently SlicerRadiomics specifies an old tag of <code>pyradiomics</code> (2024-01-03):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/blob/8426cdfe0fcb179e3f88a931b05cd40ed1ddaf94/SuperBuild/External_python-pyradiomics.cmake#L34">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/8426cdfe0fcb179e3f88a931b05cd40ed1ddaf94/SuperBuild/External_python-pyradiomics.cmake#L34" target="_blank" rel="noopener nofollow ugc">github.com/AIM-Harvard/SlicerRadiomics</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/8426cdfe0fcb179e3f88a931b05cd40ed1ddaf94/SuperBuild/External_python-pyradiomics.cmake#L34" target="_blank" rel="noopener nofollow ugc">SuperBuild/External_python-pyradiomics.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/8426cdfe0fcb179e3f88a931b05cd40ed1ddaf94/SuperBuild/External_python-pyradiomics.cmake#L34" rel="noopener nofollow ugc"><code>8426cdfe0</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="24" style="counter-reset: li-counter 23 ;">
          <li>endif()</li>
          <li></li>
          <li>ExternalProject_SetIfNotDefined(</li>
          <li>  ${CMAKE_PROJECT_NAME}_${proj}_GIT_REPOSITORY</li>
          <li>  "${git_protocol}://github.com/Radiomics/pyradiomics"</li>
          <li>  QUIET</li>
          <li>  )</li>
          <li></li>
          <li>ExternalProject_SetIfNotDefined(</li>
          <li>  ${CMAKE_PROJECT_NAME}_${proj}_GIT_TAG</li>
          <li class="selected">  "146e3bd0971336913f9c9f49ce535bc4663ca5c2"</li>
          <li>  QUIET</li>
          <li>  )</li>
          <li></li>
          <li>set(wrapper_script)</li>
          <li>if(MSVC)</li>
          <li>  find_package(Vcvars REQUIRED)</li>
          <li>  set(wrapper_script ${Vcvars_WRAPPER_BATCH_FILE})</li>
          <li>endif()</li>
          <li></li>
          <li># Alternative python prefix for installing extension python packages</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
