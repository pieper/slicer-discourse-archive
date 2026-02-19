---
topic_id: 38173
title: "Custom Application Build Fails Due To Missing Description Fi"
date: 2024-09-03
url: https://discourse.slicer.org/t/38173
---

# Custom application build fails due to missing DESCRIPTION_FILE after upgrade to 5.6.2

**Topic ID**: 38173
**Date**: 2024-09-03
**URL**: https://discourse.slicer.org/t/custom-application-build-fails-due-to-missing-description-file-after-upgrade-to-5-6-2/38173

---

## Post #1 by @darabi (2024-09-03 08:36 UTC)

<p>Hello,<br>
I have a custom application which built and ran fine on 5.4.x. After upgrading the dependencies to 5.6.2 and the latest versions of the plugins which I use, the build fails with</p>
<pre><code class="lang-auto">CMake Error at CMake/SlicerMacroBuildApplication.cmake:66 (message):
  error: Variable DESCRIPTION_FILE set to
  /home/darabi/wrk/medical/3d/myapp/build/slicersources-src/README.txt
  corresponds to an nonexistent file.
Call Stack (most recent call first):
  /home/darabi/wrk/medical/3d/myapp/MyApp/Applications/MyAppApp/CMakeLists.txt:57 (slicerMacroBuildAppLibrary)


-- Configuring incomplete, errors occurred!
See also "/home/darabi/wrk/medical/3d/myapp/cpbuild/Slicer-build/CMakeFiles/CMakeOutput.log".
See also "/home/darabi/wrk/medical/3d/myapp/cpbuild/Slicer-build/CMakeFiles/CMakeError.log".
make[2]: *** [slicersources-build/CMakeFiles/Slicer.dir/build.make:123: slicersources-build/Slicer-prefix/src/Slicer-stamp/Slicer-configure] Error 1
make[1]: *** [CMakeFiles/Makefile2:1346: slicersources-build/CMakeFiles/Slicer.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

</code></pre>
<p>I probably need to configure something in addition?</p>
<p>Thank you for your help</p>
<p>Kambiz</p>

---

## Post #2 by @darabi (2024-09-03 08:44 UTC)

<p>Sorry for the noise, I was grepping with a typo!</p>
<p>Found the variable in <code>slicer-application-properties.cmake</code>.</p>

---

## Post #3 by @jamesobutler (2024-09-03 13:58 UTC)

<p>Below is the corresponding commit change to the Slicer CustomAppTemplate. You can generally review the latest commits in that repo to update your custom app to the latest versions of configurations (as though you created a brand new custom app using latest template). There are some recent additions such as applying the ruff linter using GitHub Actions to keep your custom app in line with Slicer linting.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/commit/b0a4fc2597c7928c285e973e03d937e920c1498f">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/commit/b0a4fc2597c7928c285e973e03d937e920c1498f" target="_blank" rel="noopener nofollow ugc">github.com/KitwareMedical/SlicerCustomAppTemplate</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/commit/b0a4fc2597c7928c285e973e03d937e920c1498f" target="_blank" rel="noopener nofollow ugc">Update slicer-application-properties.cmake (#55)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-02-19" data-time="13:59:14" data-timezone="UTC">01:59PM - 19 Feb 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/brandus1" target="_blank" rel="noopener nofollow ugc">
          <img alt="brandus1" src="https://avatars.githubusercontent.com/u/62740047?v=4" class="onebox-avatar-inline" width="20" height="20">
          brandus1
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/commit/b0a4fc2597c7928c285e973e03d937e920c1498f" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fix configuration applying a fix similar to Slicer/Slicer@50beca56c (COMP: Fix
<span class="show-more-container"><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/commit/b0a4fc2597c7928c285e973e03d937e920c1498f" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">configuration referencing README.md). It follows up on changes originally introduced
in Slicer/Slicer@2fe5bde (DOC: Convert README to markdown for adding of badges)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @darabi (2024-09-04 14:46 UTC)

<p>Thank you for the hint. In fact, that was the repo where I was trying to find DESCRIPTION_FILE, but if you misspell it, you’ll never find anything <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---
