# Extensions for macOS not being build after February 15

**Topic ID**: 22125
**Date**: 2022-02-23
**URL**: https://discourse.slicer.org/t/extensions-for-macos-not-being-build-after-february-15/22125

---

## Post #1 by @Alex_Vergara (2022-02-23 09:21 UTC)

<p>Since february 15 there are no builds for Slicer Elastix extension available, see <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Elastix" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>

---

## Post #2 by @Alex_Vergara (2022-02-23 09:26 UTC)

<p>Actually reviewing it, I don’t see any build of any extension for macOS after February 15, see <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2022-02-16&amp;end=2022-02-23&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=macos" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>

---

## Post #3 by @Sam_Horvath (2022-02-23 17:57 UTC)

<p>Looks like there is a macOS build error for the main slicer package, which would also kill the extension builds.  <a class="mention" href="/u/jcfr">@jcfr</a> looking into it now.  Appears to be related to libarchive?</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=2600868" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/viewBuildError.php?buildid=2600868</a></p>

---

## Post #4 by @jcfr (2022-02-24 06:19 UTC)

<p>The issue was caused by a regression introduced in <a href="https://github.com/Slicer/Slicer/commit/e5c5ad7801b81c99a0e37b44ce570e9acbfdb7f0">e5c5ad7</a> (<code>COMP: Update LibArchive from 3.4.3 to 3.5.2 to support GCC v11</code>) and has been documented in the following issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6219">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6219" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6219" target="_blank" rel="noopener">macOS build is failing with `install_name_tool: can't open file: /path/to/LibArchive-install/lib/libarchive.17.dylib`</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-24" data-time="05:22:17" data-timezone="UTC">05:22AM - 24 Feb 22 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-02-24" data-time="06:02:09" data-timezone="UTC">06:02AM - 24 Feb 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          priority:high
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Following https://github.com/Slicer/Slicer/commit/e5c5ad7801b81c99a0e37b44ce570e<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">9acbfdb7f0 associated with https://github.com/Slicer/Slicer/pull/6197, the following error is reported when attempting to build on macOS:

```
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: can't open file: /Volumes/D/P/S-0-build/LibArchive-install/lib/libarchive.17.dylib (No such file or directory)
```


## Steps to reproduce

```
cmake \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.13 \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DQt5_DIR:PATH=/path/to/Qt/lib/cmake/Qt5 \
  /path/to/source/code/of/Slicer

make LibArchive
```

## Expected behavior

No build error

## Environment
- Slicer version: https://github.com/Slicer/Slicer/commit/e5c5ad7801b81c99a0e37b44ce570e9acbfdb7f0
- Operating system: macOS</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It has been fixed in the following pull request now integrated into the main line:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6220">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6220" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6220" target="_blank" rel="noopener">COMP: Fix LibArchive external project install step on macOS</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:6219-fix-macOS-LibArchive-fix-rpath-step</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-24" data-time="06:00:29" data-timezone="UTC">06:00AM - 24 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6220/files" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit fixes a regression introduced in e5c5ad780 (COMP: Update
LibArchive<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6220" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> from 3.4.3 to 3.5.2 to support GCC v11), it addresses the
following error by updating the interface number hard-coded in the library
path used in the "fix_rpath" external project step specific to macOS.

Error:

```
  error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool:
  can't open file: /path/to/S-0-build/LibArchive-install/lib/libarchive.17.dylib (No such file or directory)
```

See #6219</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
