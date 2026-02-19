---
topic_id: 38068
title: "Build Slicer Using Qt6 On Win11"
date: 2024-08-28
url: https://discourse.slicer.org/t/38068
---

# Build Slicer using Qt6 on Win11

**Topic ID**: 38068
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/build-slicer-using-qt6-on-win11/38068

---

## Post #1 by @chz31 (2024-08-28 00:45 UTC)

<p>Hi all,</p>
<p>Does Slicer build on Windows support Qt6? I could not find Qt 5 install online. I tried to set Qt locations following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#:~:text=cd%20C%3A%5CD%0A%0A%22C%3A%5CProgram%20Files%5CCMake%5Cbin%5Ccmake.exe%22%20%5E%0A%20%20%2DG%20%22Visual%20Studio%2017%202022%22%20%2DA%20x64%20%5E%0A%20%20%2DDQt5_DIR%3APATH%3DC%3A/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5%20%5E%0A%20%20%2DS%20C%3A%5CD%5CS%20%2DB%20C%3A%5CD%5CSR%0A%0A%22C%3A%5CProgram%20Files%5CCMake%5Cbin%5Ccmake.exe%22%20%2D%2Dbuild%20C%3A%5CD%5CSR%20%2D%2Dconfig%20Release" rel="noopener nofollow ugc">instruction</a>. I simply updated Qt 5 to Qt6_DIR. It reported a Qt5.15 not found error (paste below) in <code>CMake/SlicerBlockFindQtAndCheckVersion.cmake</code> I manually updated all <code>Qt5</code> in <code>slicer_source/CMake/SlicerBlockFindQtAndCheckVersion.cmake</code> to <code>Qt6</code>, but it appears that there are many cmake files that looked for Qt5.</p>
<p>Are there particular version of Slicer repository for Qt6 or are there easy way to update the cmake files to use Qt6? Somehow I could build Slicer on my personal laptop on WSL2 Ubuntu 22.04.</p>
<pre><code class="lang-auto">-- Could NOT find WrapVulkanHeaders (missing: Vulkan_INCLUDE_DIR)
-- Could NOT find WrapVulkanHeaders (missing: Vulkan_INCLUDE_DIR)
-- Could NOT find Qt6XmlPatterns (missing: Qt6XmlPatterns_DIR)
CMake Warning at CMake/SlicerBlockFindQtAndCheckVersion.cmake:22 (find_package):
  Found package configuration file:

    C:/Qt/6.7.2/msvc2019_64/lib/cmake/Qt6/Qt6Config.cmake

  but it set Qt6_FOUND to FALSE so package "Qt6" is considered to be NOT
  FOUND.  Reason given by package:

  Failed to find required Qt component "XmlPatterns".

  Expected Config file at
  "C:/Qt/6.7.2/msvc2019_64/lib/cmake/Qt6XmlPatterns/Qt6XmlPatternsConfig.cmake"
  does NOT exist



  Configuring with --debug-find-pkg=Qt6XmlPatterns might reveal details why
  the package was not found.

  Configuring with -DQT_DEBUG_FIND_PACKAGE=ON will print the values of some
  of the path variables that find_package uses to try and find the package.

Call Stack (most recent call first):
  CMake/SlicerBlockFindQtAndCheckVersion.cmake:67 (__SlicerBlockFindQtAndCheckVersion_find_qt)
  CMakeLists.txt:698 (include)


CMake Error at CMake/SlicerBlockFindQtAndCheckVersion.cmake:30 (message):
  error: Qt 5.15 was not found on your system.You probably need to set the
  Qt6_DIR variable.
Call Stack (most recent call first):
  CMake/SlicerBlockFindQtAndCheckVersion.cmake:67 (__SlicerBlockFindQtAndCheckVersion_find_qt)
  CMakeLists.txt:698 (include)
</code></pre>

---

## Post #2 by @jamesobutler (2024-08-28 01:32 UTC)

<p>As of right now there is not Qt6 support for Slicer with Qt 5.15 being the latest known working version. You can follow progress on the task at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6388">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6388" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6388" target="_blank" rel="noopener nofollow ugc">Update Slicer to use Qt6</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-19" data-time="20:35:46" data-timezone="UTC">08:35PM - 19 May 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Users are running into issues that are not going to be fixed on Qt5, therefore, <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">we need to switch to Qt6.

Issues reported by users that would be likely fixed by moving to Qt6:
- Proxy issues on mac (https://discourse.slicer.org/t/proxy-issue-in-extensions-manager/23467)

Unfortunately, Qt6 considerably raises minimum software and hardware requirements - see https://github.com/Slicer/Slicer/pull/6108</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @chz31 (2024-08-28 03:22 UTC)

<p>Thanks for the information Is there anyway I can download Qt5.15? It appears that the online installer only has qt &gt; 6.5 (it did have an option of qt5 compatibility though).</p>

---

## Post #4 by @cpinter (2024-08-28 08:19 UTC)

<p>I remember something like having to check “Archives” or something similar in the installer app for the 5.x versions to show. It is still there, please look around a bit more.</p>

---

## Post #5 by @chz31 (2024-08-28 16:59 UTC)

<p>Thanks! I’ll give it try.</p>

---
