---
topic_id: 25389
title: "Variable Slicer Wc Last Changed Date Is Expected To Be Defin"
date: 2022-09-22
url: https://discourse.slicer.org/t/25389
---

# Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined

**Topic ID**: 25389
**Date**: 2022-09-22
**URL**: https://discourse.slicer.org/t/variable-slicer-wc-last-changed-date-is-expected-to-be-defined/25389

---

## Post #1 by @miniminic (2022-09-22 08:12 UTC)

<p>Cmake error: Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined.</p>
<pre><code class="lang-auto">1&gt;CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:87 (message):
1&gt;  Skipping repository info extraction: directory [E:/QY3D/Slicer] is not a
1&gt;  GIT checkout
1&gt;Call Stack (most recent call first):
1&gt;  CMake/SlicerPackageAndUploadTarget.cmake:105 (SlicerMacroExtractRepositoryInfo)
1&gt;  CMake/LastConfigureStep/CMakeLists.txt:41 (include)
1&gt;This warning is for project developers.  Use -Wno-dev to suppress it.
1&gt;
1&gt;CMake Error at CMake/SlicerPackageAndUploadTarget.cmake:118 (message):
1&gt;  Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined.
1&gt;Call Stack (most recent call first):
1&gt;  CMake/LastConfigureStep/CMakeLists.txt:41 (include)
1&gt;
1&gt;
1&gt;-- Configuring incomplete, errors occurred!
</code></pre>
<p>I found articles about it in the forums, but there doesn’t seem to be a solution</p>

---

## Post #2 by @lassoan (2022-09-22 13:59 UTC)

<p>Have you downloaded the Slicer source tree az a zip file or you checked out the git repository?</p>

---

## Post #3 by @miniminic (2022-09-22 14:01 UTC)

<p>Yes, I deleted the.git file in order to commit the source code to my own Git branch</p>

---

## Post #4 by @miniminic (2022-09-22 14:02 UTC)

<p>This is the second time I’ve encountered this problem. The previous time I re-downloaded the Slicer source code, compiled and merged my changes, but it was too time-consuming</p>

---

## Post #5 by @lassoan (2022-09-22 14:50 UTC)

<p>As a result of deleting the .git file/folder your git repository got corrupted and Slicer’s build system failed to retrieve the required version information. You need to have a valid git repository, or instead you might be able to set the Slicer_WC_LAST_CHANGED (and other CMake variables) manually.</p>
<p>Do you already use the <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer">Slicercustom application template</a>? That makes it straightforward to maintain your own customized version of Slicer.</p>

---

## Post #6 by @miniminic (2022-09-22 14:51 UTC)

<p>Yes I am using slicerCAT for development</p>

---

## Post #7 by @miniminic (2022-09-22 14:54 UTC)

<p>If I want to set the value of Slicer_WC_LAST_CHANGED, how much should I set it to, or what rules should I follow to set these variables</p>

---

## Post #8 by @lassoan (2022-09-22 18:13 UTC)

<aside class="quote no-group" data-username="miniminic" data-post="6" data-topic="25389" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miniminic/48/16647_2.png" class="avatar"> miniminic:</div>
<blockquote>
<p>Yes I am using slicerCAT for development</p>
</blockquote>
</aside>
<p>OK, then all you need to set the <code>GIT_REPOSITORY</code> and <code>GIT_TAG</code> to your Slicer fork repository and branch/tag here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L15-L16">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L15-L16" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L15-L16" target="_blank" rel="noopener">KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L15-L16</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="15" style="counter-reset: li-counter 14 ;">
          <li>GIT_REPOSITORY git://github.com/Slicer/Slicer</li>
          <li>GIT_TAG        39be4408f084b3e5d632b373a4985cd7fa6c661b</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The build scripts will automatically retrieve all necessary information from there.</p>

---

## Post #9 by @miniminic (2022-09-22 23:50 UTC)

<p>Thank you very much, you solved a lot of my problems</p>

---

## Post #10 by @ferhue (2025-01-29 10:40 UTC)

<p>The same just happened to me because I had move the git source repo with the sources from HOME to /opt/ and changed the ownership. (So even <code>git status</code> here was giving an error)</p>
<p>The error was solved after doing:</p>
<pre><code class="lang-auto">git config --global --add safe.directory /opt/Slicer_src
</code></pre>

---
