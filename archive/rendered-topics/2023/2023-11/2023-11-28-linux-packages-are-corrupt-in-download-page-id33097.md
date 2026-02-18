# Linux packages are corrupt in download page

**Topic ID**: 33097
**Date**: 2023-11-28
**URL**: https://discourse.slicer.org/t/linux-packages-are-corrupt-in-download-page/33097

---

## Post #1 by @Alex_Vergara (2023-11-28 20:20 UTC)

<p>The Linux packages for Slicer 5.6 and 5.7 are corrupt in the download page. This also reflects in the AUR packages that builds upon these.</p>

---

## Post #2 by @lassoan (2023-11-30 04:51 UTC)

<p>What do you mean by corrupted? Cannot be unzipped?</p>

---

## Post #3 by @Alex_Vergara (2023-11-30 09:49 UTC)

<p>Apparently I was having a download issue and the packages were incompletely downloaded. This happened in several browsers and in the AUR script. Today I have tested again and everything seems to be working.</p>

---

## Post #4 by @lassoan (2023-11-30 11:45 UTC)

<p>Thanks for the update. In case of show/unstable network connection, downloads may fail due to http range requests not handled properly by the download server - maybe you have run into this yesterday.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/slicer_download/issues/28">
  <header class="source">

      <a href="https://github.com/Slicer/slicer_download/issues/28" target="_blank" rel="noopener">github.com/Slicer/slicer_download</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/slicer_download/issues/28" target="_blank" rel="noopener">Download backend: Disable or add support for HTTP range requests</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-06-06" data-time="15:30:45" data-timezone="UTC">03:30PM - 06 Jun 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">References:
* https://discourse.slicer.org/t/incomplete-slicer-package-download<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">-gzip-stdin-invalid-compressed-data-format-violated/29748/12
* https://github.com/girder/slicer_package_manager</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
