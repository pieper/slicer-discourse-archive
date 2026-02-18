# Pyradiomics in 3D Slicer - install via Extension Manager?

**Topic ID**: 21394
**Date**: 2022-01-10
**URL**: https://discourse.slicer.org/t/pyradiomics-in-3d-slicer-install-via-extension-manager/21394

---

## Post #1 by @Gordon_Cowell (2022-01-10 21:16 UTC)

<p>Hi, I’m needing to switch from using Slicer 3D on my MacBook to a newer Windows version to help workflow on a project.  However, the Radiomics extension doesn’t now work when you try to install in via the Slicer 3D extension manager - does anyone know when/if the packaging issues will be resolved?</p>
<p>I have looked at building SlicerRadiomics from source, but not having a programming background I didn’t have much success… Any suggestions appreciated, thank you!</p>

---

## Post #2 by @pieper (2022-01-10 21:31 UTC)

<p>The radiomics extesnion is working on the current release on windows.  What version isn’t working for you?</p>

---

## Post #3 by @jamesobutler (2022-01-11 01:07 UTC)

<p>This <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2549740" rel="noopener nofollow ugc">failed SlicerRadiomics test</a> on the factory-south-macos build machine for current Slicer Stable (4.11.20210226) may indicate an error impacting all platforms.</p>
<pre><code class="lang-auto">Cloning into 'python-pyradiomics'...
fatal: remote error: 
  The unauthenticated git protocol on port 9418 is no longer supported.
Please see https://github.blog/2021-09-01-improving-git-protocol-security-github/ for more information.
</code></pre>
<p>This protocol may be getting used in the location shown below when packaging the python module into the Slicer extension. Due to rejections the https protocol was switched to instead of git as was done in this <a href="https://github.com/Slicer/ExtensionsIndex/commit/1b041ce56807dadee778b8088cea08652f319021" rel="noopener nofollow ugc">commit</a>.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SuperBuild/External_python-pyradiomics.cmake#L22-L30">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SuperBuild/External_python-pyradiomics.cmake#L22-L30" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SuperBuild/External_python-pyradiomics.cmake#L22-L30" target="_blank" rel="noopener nofollow ugc">AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SuperBuild/External_python-pyradiomics.cmake#L22-L30</a></h4>



  <pre class="onebox">    <code class="lang-cmake">
      <ol class="start lines" start="22" style="counter-reset: li-counter 21 ;">
          <li>if(NOT DEFINED git_protocol)</li>
          <li>  set(git_protocol "git")</li>
          <li>endif()</li>
          <li>
          </li>
<li>ExternalProject_SetIfNotDefined(</li>
          <li>  ${CMAKE_PROJECT_NAME}_${proj}_GIT_REPOSITORY</li>
          <li>  "${git_protocol}://github.com/Radiomics/pyradiomics"</li>
          <li>  QUIET</li>
          <li>  )</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Using latest Slicer Preview, it has a <a href="https://slicer.cdash.org/test/20927506" rel="noopener nofollow ugc">failed test</a> on Windows where the results likely indicate it is broken.</p>
<pre><code class="lang-auto">======================================================================
ERROR: test_SlicerRadiomics1 (SlicerRadiomics.SlicerRadiomicsTest)
Ideally you should have several levels of tests.  At the lowest level
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:/D/P/S-0-E-b/SlicerRadiomics-build/inner-build/lib/Slicer-4.13/qt-scripted-modules/SlicerRadiomics.py", line 896, in test_SlicerRadiomics1
    logic.runCLI(grayscaleNode, maskNode, tableNode, featureClasses, settings, enabledImageTypes)
  File "D:/D/P/S-0-E-b/SlicerRadiomics-build/inner-build/lib/Slicer-4.13/qt-scripted-modules/SlicerRadiomics.py", line 767, in runCLI
    self.runCLIWithParameterFile(imageNode, maskNode, tableNode, parameterFile, callback)
  File "D:/D/P/S-0-E-b/SlicerRadiomics-build/inner-build/lib/Slicer-4.13/qt-scripted-modules/SlicerRadiomics.py", line 806, in runCLIWithParameterFile
    self._startCLI(firstRun=True)
  File "D:/D/P/S-0-E-b/SlicerRadiomics-build/inner-build/lib/Slicer-4.13/qt-scripted-modules/SlicerRadiomics.py", line 575, in _startCLI
    RadiomicsCLI = slicer.modules.slicerradiomicscli
AttributeError: module 'modules' has no attribute 'slicerradiomicscli'
</code></pre>

---
