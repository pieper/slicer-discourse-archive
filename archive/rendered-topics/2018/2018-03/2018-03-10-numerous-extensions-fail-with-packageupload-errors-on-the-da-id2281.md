# Numerous extensions fail with "packageupload" errors on the dashboard

**Topic ID**: 2281
**Date**: 2018-03-10
**URL**: https://discourse.slicer.org/t/numerous-extensions-fail-with-packageupload-errors-on-the-dashboard/2281

---

## Post #1 by @fedorov (2018-03-10 02:50 UTC)

<p>There are many extensions, including SlicerDMRI, SlicerOpenIGTLink, SlicerRadiomics, LASegmenter, TOMAAT, MatlabBridge, that are failing with the error below starting from March 8. I am unable to reproduce this error locally. Anyone has an idea what is happening?</p>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview" class="onebox" target="_blank" rel="noopener">http://slicer.cdash.org/index.php?project=SlicerPreview</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10ab6dc6eb1ceef1a180a7a1b7bd40e8c325eff6.png" data-download-href="/uploads/short-url/2nsVi8nUKHG9d8L5kRliVBYt8qi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ab6dc6eb1ceef1a180a7a1b7bd40e8c325eff6_2_690x167.png" alt="image" data-base62-sha1="2nsVi8nUKHG9d8L5kRliVBYt8qi" width="690" height="167" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ab6dc6eb1ceef1a180a7a1b7bd40e8c325eff6_2_690x167.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ab6dc6eb1ceef1a180a7a1b7bd40e8c325eff6_2_1035x250.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ab6dc6eb1ceef1a180a7a1b7bd40e8c325eff6_2_1380x334.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2114×514 48.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @fedorov (2018-03-10 02:52 UTC)

<p>Coincidentally, there was a change to a relevant cmake script in the Slicer tree 2 days ago…</p>
<p><a href="https://github.com/Slicer/Slicer/commit/0d1f48832335074a1a91b5c3b71d7f0fc7993637#diff-8a153a54f093a6f42e991fbeea8a455e" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/commit/0d1f48832335074a1a91b5c3b71d7f0fc7993637#diff-8a153a54f093a6f42e991fbeea8a455e</a></p>

---

## Post #3 by @fedorov (2018-03-10 02:53 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> any thoughts? Were those changes tested with a package upload process as done on the dashboard?</p>

---

## Post #4 by @jcfr (2018-03-10 03:22 UTC)

<p>We will have a look shortly. Thanks for your patience.</p>

---

## Post #5 by @jcfr (2018-03-10 03:32 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="2281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Were those changes tested with a package upload process as done on the dashboard?</p>
</blockquote>
</aside>
<p>Almost, each one of these tests setup a mock server to validate that expected packages and queries  are done.</p>
<pre><code class="lang-auto">$ ctest -R py_cmake_slicer_extensions_ 
Test project /home/jcfr/Projects/Slicer-Qt5-VTK9-Release/Slicer-build
    Start  7: py_cmake_slicer_extensions_index_build_without_upload
1/4 Test  #7: py_cmake_slicer_extensions_index_build_without_upload ...............   Passed   35.81 sec
    Start  8: py_cmake_slicer_extensions_index_build_with_upload
2/4 Test  #8: py_cmake_slicer_extensions_index_build_with_upload ..................   Passed   36.16 sec
    Start  9: py_cmake_slicer_extensions_index_build_with_upload_using_ctest
3/4 Test  #9: py_cmake_slicer_extensions_index_build_with_upload_using_ctest ......   Passed   35.86 sec
    Start 10: py_cmake_slicer_extensions_index_build_without_upload_using_ctest
4/4 Test #10: py_cmake_slicer_extensions_index_build_without_upload_using_ctest ...   Passed   35.65 sec

100% tests passed, 0 tests failed out of 4

Label Time Summary:
CMake    = 143.47 sec*proc (4 tests)

Total Test time (real) = 143.51 sec

</code></pre>
<blockquote>
<p>there was a change to a relevant cmake script in the Slicer tree 2 days ago…</p>
</blockquote>
<p>I think this is  unrelated, the variable that was involved in the removed code are not used anywhere.</p>

---

## Post #6 by @jcfr (2018-03-10 03:46 UTC)

<p>Problem has been addressed.</p>
<p>We locally modified code to disable the building of extension packages and forgot to revert the changes. This was motivated  to test the upload of extension without having to wait for packages to be re-generated.</p>
<p>I will implement a solution avoiding such problem from happening again in the future.</p>

---

## Post #7 by @jcfr (2018-03-10 12:17 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="2281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I will implement a solution avoiding such problem from happening again in the future.</p>
</blockquote>
</aside>
<p>This has also been implemented in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27037">r27037</a></p>
<p>Note: Today, since the scripts were manually triggered later than usual, Slicer extension and application <em>preview</em> (aka nightly) packages will be available for download later than expected.</p>

---

## Post #8 by @lassoan (2018-03-10 13:56 UTC)

<p>It would be great if we could switch to the new “Preview” term, but for that the update page would need to be updated. <a class="mention" href="/u/jcfr">@jcfr</a> Do you know what’s the status of that?</p>

---

## Post #9 by @jcfr (2018-03-10 18:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="2281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>that the update page would need to be updated.</p>
</blockquote>
</aside>
<p>If you talk about the download page, I think <a class="mention" href="/u/mhalle">@mhalle</a> will integrate the PR soon.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/mhalle/slicer4-download_deprecated/pull/13">
  <header class="source">

      <a href="https://github.com/mhalle/slicer4-download_deprecated/pull/13" target="_blank" rel="noopener">github.com/mhalle/slicer4-download_deprecated</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/mhalle/slicer4-download_deprecated/pull/13" target="_blank" rel="noopener">download page: Update quality dashboard links, and update "Nightly" to "Preview"</a>
      </h4>

    <div class="branches">
      <code>mhalle:master</code> ← <code>jcfr:update-quality-dashboard-links</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-02-16" data-time="20:30:52" data-timezone="UTC">08:30PM - 16 Feb 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="2 commits changed 1 files with 2 additions and 2 deletions">
          <a href="https://github.com/mhalle/slicer4-download_deprecated/pull/13/files" target="_blank" rel="noopener">
            <span class="added">+2</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://discourse.slicer.org/t/different-dashboard-for-master-and-stable-bui<span class="show-more-container"><a href="https://github.com/mhalle/slicer4-download_deprecated/pull/13" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">lds/2091</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
`</p>

---
