---
topic_id: 12859
title: "Pip Install Packages That Need Compilation"
date: 2020-08-04
url: https://discourse.slicer.org/t/12859
---

# Pip install packages that need compilation

**Topic ID**: 12859
**Date**: 2020-08-04
**URL**: https://discourse.slicer.org/t/pip-install-packages-that-need-compilation/12859

---

## Post #1 by @ezgimercan (2020-08-04 22:32 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/14">Slicer-Python Packages Use and Install</a>:</p>
<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="984" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/14">Slicer-Python Packages Use and Install</a></div>
<blockquote>
<p>Slicer’s pip does not yet support packages that need compilation. To get access to all Python packages, you have to build Slicer with your Python distribution. See some information here: <a href="https://www.slicer.org/wiki/Documentation/Labs/SlicerCondaIntegration" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Labs/SlicerCondaIntegration </a></p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Just checking to see if this is still the case. I am trying to integrate an old C++ code into a scripted module, I converted all to Python and it is using dlib library (<a href="https://pypi.org/project/dlib/" class="inline-onebox" rel="noopener nofollow ugc">dlib · PyPI</a>). I am getting CMake errors from Python Interactor, which I assume related to the above post.</p>
<pre><code>RuntimeError:
*******************************************************************
 CMake must be installed to build the following extensions: dlib
*******************************************************************
</code></pre>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2020-08-04 23:20 UTC)

<p>Yes, for ones that need to be compiled I would suggest to do the method described in this post so that it is compiled and packaged at time of building the extension. The build machine of the extension would then be the one that would need the build requirements.</p>
<aside class="quote quote-modified" data-post="8" data-topic="10110">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/install-python-library-with-extension/10110/8">Install python library with extension</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Ciao <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a>, if your extension is in the extension manager, you can actually do it directly in the cmake (so they will be packed at compilation time on the kitware factory machines): 


add  python requirements in the superbuild: 
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild.cmake#L28" rel="noopener nofollow ugc">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild.cmake#L28</a> 
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/slicerastro-requirements.txt" rel="noopener nofollow ugc">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/slicerastro-requirements.txt</a> 
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/External_python-slicerastro-requirements.cmake" rel="noopener nofollow ugc">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/External_python-slicerastro-requirements.…</a>
  </blockquote>
</aside>


---

## Post #3 by @jamesobutler (2020-08-04 23:30 UTC)

<p>If you’re curious about if dlib would make prebuilt binaries, you can see the developer’s response at <a href="https://github.com/davisking/dlib/issues/2121#issuecomment-653662699" rel="nofollow noopener">https://github.com/davisking/dlib/issues/2121#issuecomment-653662699</a>.</p>
<p>Of course finding a different python package that can do what you want and has wheels could be another option to avoid a superbuild project.</p>

---

## Post #4 by @ezgimercan (2020-08-04 23:32 UTC)

<p>Thanks, this helps a lot! I think I can find similar functions in opencv.</p>

---
