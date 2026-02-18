# Python package installation

**Topic ID**: 19496
**Date**: 2021-09-03
**URL**: https://discourse.slicer.org/t/python-package-installation/19496

---

## Post #1 by @riep (2021-09-03 11:51 UTC)

<p>Hi everyone,<br>
Is there a way to install a python package in slicer’s python environment (using pip) but not during the runtime of Slicer. What would be the cleanest way to do it?<br>
Thanks for your advices,</p>
<p>Pierre</p>

---

## Post #2 by @jamesobutler (2021-09-03 14:05 UTC)

<p>In the Slicer binary folder there is PythonSlicer.exe which you can use like you would a system python install python packages into slicer’s python environment. <code>PythonSlicer.exe -m pip install X</code>.</p>
<p>Are you asking how to do this not during runtime of Slicer because you are changing the version of a python package that is in Slicer core? If so, this could lead to some incompatibilities as Slicer is tested primarily on the specific versions included.</p>
<p>If you’re looking to install a python package as required by a module, but you don’t want to do it during Slicer run-time you could package the python package at time of building the extension. See <a href="https://github.com/AIM-Harvard/SlicerRadiomics" rel="noopener nofollow ugc">SlicerRadiomics</a> of how they package <code>pyradiomics</code> with the extension.</p>

---

## Post #3 by @riep (2021-09-03 15:23 UTC)

<p>Hi James,<br>
Thank you for your input.<br>
The last paragraph, probably what we are looking for. For instance, how we can install scipy at building stage.</p>
<p>I will look at it !<br>
Cheers,</p>

---

## Post #4 by @jamesobutler (2021-09-03 16:56 UTC)

<p>Using pip install to install scipy indicates you are likely wanting the whl file as provided by PyPI. Slicer already by default contains Scipy as you shouldn’t need to install it again. Is there something wrong with this already included version?</p>

---

## Post #5 by @riep (2021-09-04 20:13 UTC)

<p>sorry, scipy was just for the example. I need to install weasypdf.</p>

---

## Post #6 by @lassoan (2021-09-05 00:24 UTC)

<aside class="quote no-group" data-username="riep" data-post="5" data-topic="19496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/riep/48/9933_2.png" class="avatar"> riep:</div>
<blockquote>
<p>I need to install weasypdf</p>
</blockquote>
</aside>
<p>There is no such package on PyPI. Are you sure this is the correct name?</p>

---

## Post #7 by @riep (2021-09-05 13:06 UTC)

<p>Maybe documentation is not up-to-date but there is <a href="https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#linux" class="inline-onebox" rel="noopener nofollow ugc">First Steps — WeasyPrint 53.2 documentation</a></p>

---

## Post #8 by @lassoan (2021-09-05 20:21 UTC)

<p>This (<code>weasyprint</code>) is a different package. You wrote you were trying to install the non-existing <code>weasypdf</code> package.</p>

---

## Post #9 by @riep (2021-09-06 06:13 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=10" title=":expressionless:" class="emoji" alt=":expressionless:"> sorry about that… I will post my solution here.</p>

---

## Post #10 by @riep (2021-09-06 10:51 UTC)

<p>Well, I am really struggling to understand Cmake and the way it could be done. Could you help me on that, please ?</p>

---

## Post #11 by @lassoan (2021-09-06 12:45 UTC)

<p>Would you like to bundle the Python package in an extension or in a custom Slicer application?</p>

---

## Post #12 by @riep (2021-09-06 14:56 UTC)

<p>In a custom slicer application</p>

---

## Post #13 by @jamesobutler (2021-09-06 15:54 UTC)

<p>For a Slicer custom app you can use SlicerSalt as an example. See the following below how some python packages are installed as part of the superbuild process.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/SlicerSALT/blob/345f48977013b4cfa8a3c3f9240cb27bfb0ea77a/SuperBuild/External_python-mfsda-requirements.cmake">
  <header class="source">

      <a href="https://github.com/Kitware/SlicerSALT/blob/345f48977013b4cfa8a3c3f9240cb27bfb0ea77a/SuperBuild/External_python-mfsda-requirements.cmake" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/SlicerSALT/blob/345f48977013b4cfa8a3c3f9240cb27bfb0ea77a/SuperBuild/External_python-mfsda-requirements.cmake" target="_blank" rel="noopener nofollow ugc">Kitware/SlicerSALT/blob/345f48977013b4cfa8a3c3f9240cb27bfb0ea77a/SuperBuild/External_python-mfsda-requirements.cmake</a></h4>


    <pre><code class="lang-cmake">set(proj python-mfsda-requirements)

# Set dependency list
set(${proj}_DEPENDENCIES python python-numpy python-scipy python-pip)

if(NOT DEFINED Slicer_USE_SYSTEM_${proj})
  set(Slicer_USE_SYSTEM_${proj} ${Slicer_USE_SYSTEM_python})
endif()

# Include dependent projects if any
ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDENCIES)

if(Slicer_USE_SYSTEM_${proj})
  foreach(module_name IN ITEMS pandas statsmodels)
    ExternalProject_FindPythonPackage(
      MODULE_NAME "${module_name}"
      REQUIRED
      )
  endforeach()
endif()
</code></pre>


  This file has been truncated. <a href="https://github.com/Kitware/SlicerSALT/blob/345f48977013b4cfa8a3c3f9240cb27bfb0ea77a/SuperBuild/External_python-mfsda-requirements.cmake" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
