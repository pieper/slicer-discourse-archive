---
topic_id: 23961
title: "Fyi Small Patch To Build Slicer On Arch Linux"
date: 2022-06-20
url: https://discourse.slicer.org/t/23961
---

# FYI : small patch to build Slicer on Arch Linux

**Topic ID**: 23961
**Date**: 2022-06-20
**URL**: https://discourse.slicer.org/t/fyi-small-patch-to-build-slicer-on-arch-linux/23961

---

## Post #1 by @chir.set (2022-06-20 11:50 UTC)

<p>Building Slicer at 5ecfcc37a51 failed on Arch Linux, with QSignalSpy not found message.</p>
<p>This patch is required for a successful build :</p>
<pre><code class="lang-auto">$ git diff
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 5158d8759..8aa04ccd8 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -608,6 +608,7 @@ endif()
   # This component is needed for building VTK
   if(UNIX AND NOT APPLE)
     list(APPEND Slicer_REQUIRED_QT_MODULES X11Extras)
+    list(APPEND Slicer_REQUIRED_QT_MODULES Test)
   endif()
 
   find_package(Qt5 COMPONENTS Core QUIET)
</code></pre>
<p>Just FYI, in case it would need a fix somewhere, if it’s not Arch specific.</p>

---

## Post #2 by @RafaelPalomar (2022-06-20 12:09 UTC)

<p>Thank you <a class="mention" href="/u/chir.set">@chir.set</a>. This looks to me related to the following PR</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6165">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6165" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6165" target="_blank" rel="noopener nofollow ugc">COMP: Add Concurrent and Test as Qt requirements</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>ALive-research:comp/qtconcurrent_qttest</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-08" data-time="08:14:22" data-timezone="UTC">08:14AM - 08 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/RafaelPalomar" target="_blank" rel="noopener nofollow ugc">
          <img alt="RafaelPalomar" src="https://avatars.githubusercontent.com/u/1978682?v=4" class="onebox-avatar-inline" width="20" height="20">
          RafaelPalomar
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6165/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Qt modules Concurrent and Test are explicit requirements for CTK. This
commit a<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6165" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">dds these as requirements for Slicer too.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The bottom line is that we need to conciliate the Slicer Qt requirements with those of CTK as <a class="mention" href="/u/jcfr">@jcfr</a> suggested in the PR. I’ll try to give more priority to solve this issue so these types of errors don’t occur in the future</p>

---

## Post #3 by @jamesobutler (2022-06-20 13:09 UTC)

<p>Here’s the corresponding issue report:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6437">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6437" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6437" target="_blank" rel="noopener nofollow ugc">fail to build master branch due to fatal error: QSignalSpy: No such file or directory</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-19" data-time="08:12:05" data-timezone="UTC">08:12AM - 19 Jun 22 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-06-19" data-time="14:09:26" data-timezone="UTC">02:09PM - 19 Jun 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/hubutui" target="_blank" rel="noopener nofollow ugc">
          <img alt="hubutui" src="https://avatars.githubusercontent.com/u/2948593?v=4" class="onebox-avatar-inline" width="20" height="20">
          hubutui
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

fail to build master branch:
```
/build/3dslicer-git/src/3dslice<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">r/Base/QTCore/qSlicerExtensionsManagerModel.cxx:31:10: fatal error: QSignalSpy: No such file or directory
   31 | #include &lt;QSignalSpy&gt;
      |          ^~~~~~~~~~~~
compilation terminated.
```
see also the complete build log [here](https://github.com/Slicer/Slicer/files/8934955/log.txt.tar.gz). You could jump to the line 72251 for the error messages.

Maybe we forget to add `testlib` according to Qt official [doc](https://doc.qt.io/qt-5/qsignalspy.html)?

## Steps to reproduce

I build 3dslicer with this [PKGBUILD](https://github.com/archlinuxcn/repo/blob/8c62f8b6aca24634780329e42c49286236610ebf/archlinuxcn/3dslicer-git/PKGBUILD) on ArchLinux with minor modification. I use
```
make -C "build" VERBOSE=1 
```
to print more information.

## Expected behavior



## Environment
- Slicer version: the master branch, date 20220619
- Operating system: ArchLinux</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @RafaelPalomar (2022-06-20 14:08 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a>, <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a href="https://github.com/Slicer/Slicer/pull/6165" rel="noopener nofollow ugc">Slicer/Slicer#6437</a> and <a href="https://github.com/Slicer/Slicer/issues/6437" rel="noopener nofollow ugc">Slicer/Slicer#6165</a> point to similar problems but are not exactly the same. One refers to a compilation error when building slicer and the other refers to a possible configuration error on CTK when building the superbuild. Sorry for the confusion.</p>

---
