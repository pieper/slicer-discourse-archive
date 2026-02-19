---
topic_id: 42902
title: "Build Error In Custom 3D Slicer App Qmrmlwidget Is Not A Cla"
date: 2025-05-13
url: https://discourse.slicer.org/t/42902
---

# Build Error in Custom 3D Slicer App: 'qMRMLWidget': is not a class or namespace name and pixmapFromIcon not found

**Topic ID**: 42902
**Date**: 2025-05-13
**URL**: https://discourse.slicer.org/t/build-error-in-custom-3d-slicer-app-qmrmlwidget-is-not-a-class-or-namespace-name-and-pixmapfromicon-not-found/42902

---

## Post #1 by @software (2025-05-13 07:04 UTC)

<p>Hi all,<br>
I’m encountering an issue while building a custom 3D Slicer-based application using the Kitware custom app template. I’ve previously created another custom app (around 2 months ago) with the <strong>same versions</strong> of CMake and Qt, and that build completed successfully.</p>
<p>Now, after a long 5.5-hour build process, the current app fails with the following errors:<br>
*<strong>‘qMRMLWidget’: is not a class or namespace name [E:\New\build\Slicer-build\Applications\NewSlicerApp\qNewSlicerApp.vcxproj]<br>
‘pixmapFromIcon’: identifier not found [E:\New\build\Slicer-build\Applications\NewSlicerApp\qNewSlicerApp.vcxproj]</strong><br>
<strong>The final message is</strong>:<br>
<strong>Custom build for ‘…Slicer-configure.rule; … Slicer-build.rule; … Slicer-install.rule’ exited with code 1.</strong><br>
<strong>What I’ve tried:</strong></p>
<ul>
<li>I double-checked that the Qt and CMake versions match my previous working setup.</li>
<li>I haven’t made any changes to Slicer core or its dependencies.</li>
<li>The custom app is based on the same Kitware template I used before.</li>
</ul>
<p>Any idea why this might be happening now, especially with <code>qMRMLWidget</code> not being recognized? Could something have changed in the Slicer nightly/master branch, or do I need to add additional includes or dependencies in the new app?</p>
<p>Appreciate any suggestions or guidance to fix this and complete the build.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2025-05-13 07:34 UTC)

<p>What commit of Slicer does your custom app specify to build? Is your repo publicly available to see?</p>
<p>Are you using Visual Studio 2022? What version of CMake are you using? What version of Qt?</p>

---

## Post #3 by @software (2025-05-13 07:42 UTC)

<p>cmake version 3.31.5<br>
Visual Studio 2022 already installed<br>
[1/12] project_name (SlicerCustomAppTemplate): New<br>
[2/12] github_organization (Kitware): NewOrg<br>
[3/12] github_project (New): NewSlicer<br>
[4/12] org_domain (<a href="http://kitware.com" rel="noopener nofollow ugc">kitware.com</a>): <a href="http://neworg.com" rel="noopener nofollow ugc">neworg.com</a><br>
[5/12] org_name (Kitware, Inc.): New Organization<br>
[6/12] app_name (New): NewSlicer<br>
[7/12] bundle_identifier (com.neworg.new): com.neworg.newslicerapp<br>
[8/12] app_version_major (0): 0<br>
[9/12] app_version_minor (1): 1<br>
[10/12] app_version_patch (0): 0<br>
[11/12] app_description_summary (Customized version of Slicer): Customized medical imaging platform for New Organization<br>
[12/12] cdash_drop_site (<a href="http://open.cdash.org" rel="noopener nofollow ugc">open.cdash.org</a>): <a href="http://open.cdash.org" rel="noopener nofollow ugc">open.cdash.org</a><br>
**and this is the cmake.txt created **</p>
<h1><a name="p-125049-slicer-sources-1" class="anchor" href="#p-125049-slicer-sources-1" aria-label="Heading link"></a>Slicer sources</h1>
<p>include(FetchContent)<br>
if(NOT DEFINED slicersources_SOURCE_DIR)</p>
<h1><a name="p-125049-download-slicer-sources-and-set-variables-slicersources_source_dir-and-slicersources_binary_dir-2" class="anchor" href="#p-125049-download-slicer-sources-and-set-variables-slicersources_source_dir-and-slicersources_binary_dir-2" aria-label="Heading link"></a>Download Slicer sources and set variables slicersources_SOURCE_DIR and slicersources_BINARY_DIR</h1>
<p>FetchContent_Populate(slicersources<br>
GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/Slicer/Slicer<br>
GIT_TAG        763a244c8518599b5c4d41123011c4a05cbb0557<br>
GIT_PROGRESS   1<br>
)</p>

---

## Post #4 by @nyk3151 (2025-05-14 22:44 UTC)

<p>Hello,software.</p>
<p>Actually, I faced same error when trying to build slicer custom app like you.<br>
I hypothesize that latest version of slicer is still unstable.</p>
<p>Therefore, I changed GIT_TAG in CMakeLists as follows .</p>
<p>Before</p>
<pre><code class="lang-auto">FetchContent_Populate(slicersources
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/Slicer/Slicer
  GIT_TAG        763a244c8518599b5c4d41123011c4a05cbb0557
  GIT_PROGRESS   1
  )
</code></pre>
<p>After</p>
<pre><code class="lang-auto">FetchContent_Populate(slicersources
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/Slicer/Slicer
  GIT_TAG        v5.8.1
  GIT_PROGRESS   1
  )
</code></pre>
<p>This modification made the build successful.</p>

---
