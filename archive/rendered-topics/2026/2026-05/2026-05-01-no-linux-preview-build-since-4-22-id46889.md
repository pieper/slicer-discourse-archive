---
topic_id: 46889
title: "No Linux Preview Build Since 4 22"
date: 2026-05-01
url: https://discourse.slicer.org/t/46889
---

# No linux preview build since 4/22

**Topic ID**: 46889
**Date**: 2026-05-01
**URL**: https://discourse.slicer.org/t/no-linux-preview-build-since-4-22/46889

---

## Post #1 by @muratmaga (2026-05-01 15:59 UTC)

<p>I just downloaded the latest preview for Linux and it is dated 4/22.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/ebrahim">@ebrahim</a></p>

---

## Post #2 by @ebrahim (2026-05-01 16:45 UTC)

<p>Yes I think there are recent some issues being worked on (not by me)</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9134#issuecomment-4353140095">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9134#issuecomment-4353140095" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/9222709?u=99c30473ca68e6d8f7ce1c6517fdec63ef2a91ee&amp;v=4" class="onebox-avatar-inline" width="20" height="20">
          Sunderlandkyl
        </a> - <a href="https://github.com/Slicer/Slicer/pull/9134#issuecomment-4353140095" target="_blank" rel="noopener">BUG: Guard null SegmentationNode in qMRMLSegmentEditorWidget</a>
      </h4>



    <div class="branches">
      <code>main</code> ← <code>Sunderlandkyl:seg_edit_no_segmentation_effect_crash</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Seems there is a failure on the nightly Linux build that is causing the CI to fa<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9134" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">il:

```
CMake Error at /usr/src/Slicer-build/Slicer-build/CMake/LastConfigureStep/cmake_install.cmake:1117 (file):
  file INSTALL cannot find
  "/usr/src/Slicer-build/CTK-build/CMakeExternals/Install/lib/libQtTesting.so":
  No such file or directory.
Call Stack (most recent call first):
  /usr/src/Slicer-build/Slicer-build/cmake_install.cmake:162 (include)


/opt/rh/gcc-toolset-14/root/usr/bin/strip: '/usr/src/Slicer-build/Slicer-build/_CPack_Packages/linux-amd64/TGZ/Slicer-5.11.0-2026-04-30-linux-amd64/./lib/Slicer-5.11/libQtTesting.so': No such file
CPack Error: Error when generating package: Slicer
```

Linux nightly CDash failure:
https://slicer.cdash.org/builds/4205217/build</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9137">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9137" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9137" target="_blank" rel="noopener">BUG: Resolve QtTesting install library name from imported target (#9137)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>hjmjohnson:fix-qttesting-install-name</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-04-30" data-time="17:56:00" data-timezone="UTC">05:56PM - 30 Apr 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/hjmjohnson" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/313970?v=4" class="onebox-avatar-inline" width="20" height="20">
            hjmjohnson
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 67 additions and 5 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9137/files" target="_blank" rel="noopener">
            <span class="added">+67</span>
            <span class="removed">-5</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes #9135. The CTK QtTesting tag bump (`cf5fa41…`, "ctk-2026-03-27 Qt5+Qt6 sup<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9137" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">port") renamed the shared library output from `QtTesting` to `qttesting`, causing nightly Linux packaging to fail. This change queries the actual library file name from the imported `qttesting` CMake target instead of hard-coding it, so future renames don't silently break packaging.

&lt;details&gt;
&lt;summary&gt;Root cause&lt;/summary&gt;

`CMake/SlicerBlockInstallQtTesting.cmake` hard-coded `libQtTesting.so` / `libQtTesting.dylib` / `QtTesting.dll`. After the CTK tag bump, CTK installs `libqttesting.so` (lowercase), so the install step errors:

```
file INSTALL cannot find
  /usr/src/Slicer-build/CTK-build/CMakeExternals/Install/lib/libQtTesting.so
```

&lt;/details&gt;

&lt;details&gt;
&lt;summary&gt;Fix details&lt;/summary&gt;

- `find_package(QtTesting CONFIG REQUIRED)` to load the imported target.
- Probe target names (`qttesting`, `QtTesting`, `QtTesting::qttesting`, `CTK::QtTesting`) so a future namespaced rename fails loudly instead of silently.
- Resolve the library basename from `IMPORTED_LOCATION_&lt;CONFIG&gt;` (with fallbacks across known config types and `IMPORTED_LOCATION`).
- Use that basename for both `install(FILES …)` and `slicerStripInstalledLibrary(…)`.
- Documents a known limitation: assumes a single unversioned shared library file (no `libqttesting.so.1` SONAME chain). If upstream introduces SONAME versioning later, the block needs to install the symlink chain too — a comment in the file flags this.

Verified locally: the generated `cmake_install.cmake` now references `libqttesting.so` from the actual CTK install tree.

&lt;/details&gt;

## Test plan
- [ ] Linux nightly package build (CDash) succeeds: previously failing `cmake_install.cmake:1117` step now installs `libqttesting.so`.
- [ ] macOS package contains `libqttesting.dylib`.
- [ ] Windows package contains `qttesting.dll`.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
