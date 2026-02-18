# VMTK extension build error

**Topic ID**: 42765
**Date**: 2025-05-01
**URL**: https://discourse.slicer.org/t/vmtk-extension-build-error/42765

---

## Post #1 by @muratmaga (2025-05-01 20:24 UTC)

<p>Looks like VTMK is not building for the latest preview.</p>

---

## Post #2 by @jamesobutler (2025-05-01 20:29 UTC)

<p>See the following thread where <a class="mention" href="/u/chir.set">@chir.set</a> needs to finalize compatibility with VTK 9.4.</p>
<aside class="quote" data-post="1" data-topic="42605">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicervmtk-not-building-for-slicerpreview-on-cdash/42605">SlicerVMTK not building for SlicerPreview on cdash</a> <a class="badge-category__wrapper " href="/c/community/vmtk/28"><span data-category-id="28" style="--category-badge-color: #E45735; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This is the new home of the VMTK community (moved from VMTK Google Groups)"><span class="badge-category__name">VMTK</span></span></a>
  </div>
  <blockquote>
    SlicerVMTK is not building on cdash for SlicerPreview while it does build for SlicerStable. The error messages relate to the VMTK library itself. 
FYI, hoping for an investigation.
  </blockquote>
</aside>


---

## Post #3 by @muratmaga (2025-05-01 20:29 UTC)

<p>In windows stable (5.8.1) extension is present but fails to launch after the install with this error:</p>
<pre><code class="lang-auto">Error(s):
    CLI executable: C:/Users/maria/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerVMTK/lib/Slicer-5.8/qt-loadable-modules/vtkvmtk.py
    The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.
Fail to instantiate module  "vtkvmtk"
The following modules failed to be instantiated:
</code></pre>
<p>On Mac 5.8.1 it installs and works fine.</p>

---

## Post #4 by @jamesobutler (2025-05-01 20:30 UTC)

<p>This error message can be safely ignored. See the following:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/22">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22" target="_blank" rel="noopener nofollow ugc">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22" target="_blank" rel="noopener nofollow ugc">Fail to instantiate module “vtkvmtk” error reported at startup</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-09-25" data-time="15:37:26" data-timezone="UTC">03:37PM - 25 Sep 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This error is reported at Slicer startup if SlicerVMTK extension is installed:
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
```
CLI executable: C:/Users/E/AppData/Roaming/NA-MIC/Extensions-29387/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.
Fail to instantiate module “vtkvmtk”
The following modules failed to be instantiated:
vtkvmtk
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @chir.set (2025-05-01 20:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="42765" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Looks like VTMK is not building for the latest preview.</p>
</blockquote>
</aside>
<p>Not even for SlicerStable on cdash since a commit I made 2 weeks ago.</p>
<p>I am merging a patch and will see tomorrow.</p>

---

## Post #6 by @chir.set (2025-05-01 20:41 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="42765">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>needs to finalize compatibility with VTK 9.4</p>
</blockquote>
</aside>
<p>Please see <a href="https://discourse.slicer.org/t/slicervmtk-not-building-for-slicerpreview-on-cdash/42605/7">this comment</a>.</p>

---

## Post #7 by @chir.set (2025-05-02 15:44 UTC)

<p>SlicerVMTK built for Mac but not for Windows on cdash with the <a href="https://discourse.slicer.org/t/vmtk-extension-build-error/42765/5">last patch</a> I pushed.</p>
<p>I am reverting the offending commit and will monitor cdash to check how it builds on the 3 platforms.</p>

---

## Post #8 by @lassoan (2025-05-03 14:29 UTC)

<p>VTK-9.2/9.4 compatibility: I would recommend to keep the same source code for the stable and preview releases for now. To get VMTK compatibility with both VTK versions, update to the latest VMTK.</p>
<p>CMake updates: I would not try to make any CMake file changes in VMTK extension now (and revert any changes that cause trouble), but wait for Slicer and all its dependencies to support CMake4 first.</p>

---

## Post #9 by @chir.set (2025-05-03 18:22 UTC)

<p>SlicerVMTK now builds for Mac and Windows, for SlicerStable. The Linux build does not seem to be triggered, for another extension also.</p>

---

## Post #10 by @chir.set (2025-05-03 18:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="42765">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>update to the latest VMTK</p>
</blockquote>
</aside>
<p>For a successful build of VMTK itself at the <a href="https://github.com/vmtk/vmtk/commit/6c189dd6ee644a466498bd382b0c19229f20daa5" rel="noopener nofollow ugc">latest commit</a>, this patch must be applied, for VTK 9.4.</p>
<pre><code class="lang-auto">
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 0d46a7c..4043110 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -1,4 +1,4 @@
-cmake_minimum_required(VERSION 3.12...3.29.1)
+cmake_minimum_required(VERSION 3.3)
 
 project(VMTK)
 
@@ -27,7 +27,7 @@ if(VMTK_WITH_LIBRARY_VERSION)
      )
 endif()
 
-find_package( Python3 COMPONENTS Interpreter )
+find_package( PythonInterp )
 if (NOT VMTK_PYTHON_VERSION)
   set(VMTK_PYTHON_VERSION "python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}" CACHE STRING "" FORCE)
 endif ()
@@ -309,17 +309,11 @@ if(VMTK_SCRIPTS_ENABLED)
     ${VMTK_BINARY_DIR}/VMTKConfig.cmake
   @ONLY IMMEDIATE
   )
-  install(FILES ${VMTK_BINARY_DIR}/VMTKConfig.cmake
-    TYPE LIB
-  )
 
   configure_file(
     ${VMTK_SOURCE_DIR}/CMake/VMTKUse.cmake.in
     ${VMTK_BINARY_DIR}/VMTKUse.cmake
   @ONLY IMMEDIATE
   )
-  install(FILES ${VMTK_BINARY_DIR}/VMTKUse.cmake
-    TYPE LIB
-  )
 
 endif()
</code></pre>
<p>It’s just a reverse of that commit for the<code> CMakeLists.txt</code> only.</p>

---
