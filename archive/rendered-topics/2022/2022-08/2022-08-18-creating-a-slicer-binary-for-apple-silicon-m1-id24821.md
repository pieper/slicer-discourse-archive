---
topic_id: 24821
title: "Creating A Slicer Binary For Apple Silicon M1"
date: 2022-08-18
url: https://discourse.slicer.org/t/24821
---

# Creating a Slicer binary for Apple Silicon M1

**Topic ID**: 24821
**Date**: 2022-08-18
**URL**: https://discourse.slicer.org/t/creating-a-slicer-binary-for-apple-silicon-m1/24821

---

## Post #1 by @efu98 (2022-08-18 16:13 UTC)

<p>Hello!<br>
I am trying to create a binary of a custom application based on Slicer for Apple Silicon M1. I have managed built Qt5 (using this <a href="https://www.reddit.com/r/QtFramework/comments/ll58wg/how_to_build_qt_creator_for_macos_arm64_a_guide/" rel="noopener nofollow ugc">tutorial</a>) and installed the other prerequisites. However, when I try building Slicer, I get the following errors:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83d66c81d231c6b1ff005b3ba2edb11dd29d287e.png" data-download-href="/uploads/short-url/iOhWSlmDoztWDbyCiQ9i5pypBXE.png?dl=1" title="Screen Shot 2022-08-18 at 12.08.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d66c81d231c6b1ff005b3ba2edb11dd29d287e_2_690x178.png" alt="Screen Shot 2022-08-18 at 12.08.41 PM" data-base62-sha1="iOhWSlmDoztWDbyCiQ9i5pypBXE" width="690" height="178" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d66c81d231c6b1ff005b3ba2edb11dd29d287e_2_690x178.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d66c81d231c6b1ff005b3ba2edb11dd29d287e_2_1035x267.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d66c81d231c6b1ff005b3ba2edb11dd29d287e_2_1380x356.png 2x" data-dominant-color="363535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-18 at 12.08.41 PM</span><span class="informations">1522×394 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the cmake command I am using :</p>
<pre><code class="lang-auto">cmake \  
-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=12.1 \
-DSlicer_USE_SYSTEM_OpenSSL:BOOL=ON \
-DQt5_DIR:PATH=/Users/efu/qt5-5.15-macOS-release/qtbase/lib/cmake/Qt5 \
-DCMAKE_OSX_ARCHITECTURES="arm64" \
-DOPENSSL_ROOT_DIR:PATH=/opt/homebrew/opt/openssl/ \
/Users/efu/Slicer
</code></pre>
<p>Has anyone come across this problem? Is there a way to fix it?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2022-08-18 16:36 UTC)

<p>That’s a python build error so it should be fixable.  You may be able to use the system python, or get a (newer?) python and edit <a href="https://github.com/Slicer/Slicer/blob/main/SuperBuild/External_python.cmake">this file and related places</a>.</p>
<p>You will no doubt hit more issues when you get to CTK and the Slicer core codebase.  It would be great if you could start a draft pull request with any changes you need to make to the Slicer build system so other people can test / contribute.</p>

---

## Post #3 by @efu98 (2022-08-18 16:45 UTC)

<p>Thank you! Will using the system python prevent me from creating a functional binary? I am a bit confused about what can be installed directly using homebrew and what has to be built “by hand”.</p>

---

## Post #4 by @pieper (2022-08-18 16:50 UTC)

<aside class="quote no-group" data-username="efu98" data-post="3" data-topic="24821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/46a35a/48.png" class="avatar"> efu98:</div>
<blockquote>
<p>Will using the system python prevent me from creating a functional binary?</p>
</blockquote>
</aside>
<p>It might but probably it can be packaged like any python build.  Best would be to find a way to build from source using a version that works on the target architecture.</p>
<p>As you’ve seen the Slicer build system is big and it depends on several other large projects so it make take a while to port everything.</p>

---
