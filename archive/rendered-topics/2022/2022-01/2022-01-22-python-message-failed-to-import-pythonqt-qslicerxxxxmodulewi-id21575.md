# Python message: "Failed to import PythonQt.qSlicerxxxxModuleWidgets"

**Topic ID**: 21575
**Date**: 2022-01-22
**URL**: https://discourse.slicer.org/t/python-message-failed-to-import-pythonqt-qslicerxxxxmodulewidgets/21575

---

## Post #1 by @AndreaVitali86 (2022-01-22 15:54 UTC)

<p>Dear All,</p>
<p>I’m Andrea Vitali from University of Bergamo (Italy) and our students faced a specific problem during the development of a C++ module based on the template “loadablecustommarkups”.</p>
<p>In particular, we have problems with creating the loadable-custom-markups module in 3Dslicer version 4.13.0 for Windows 10 with Visual Studio 2019, Qt5 version 5.0.2 and Cmake version 3.15.4. We followed the instructions in the 3D-slicer documentation:</p>
<ul>
<li>Setting up the source and debug-mode build folder respectively named "S4_13" and "S4_13D",</li>
<li>Creating an extension and adding a "custom loadable markup" module from “Extension Wizard”,</li>
<li>Compiling files using c-make by entering the path to source and debug-mode build folder, where it’s necessary the .git file in our module,</li>
<li>Opening the project in Visual Studio and compiling "All-build" project,</li>
</ul>
<p>Despite this, when we try to open the Slicer.exe file, we get errors with the message “Failed to import PythonQt.qSlicercustomMarkupModuleWidgets”.<br>
While if we create a standard loadable module with the same procedure, no error appears.</p>
<p>I also found this post “<a href="https://discourse.slicer.org/t/build-error-caused-by-qslicersubjecthierarchyplotsplugin/2060" class="inline-onebox">Build error caused by qSlicerSubjectHierarchyPlotsPlugin</a>” in which the same error was relative to the maximum lenght of the file name. Coudl it be the same issue?</p>
<p>Thanks in advance,</p>
<p>Regards,<br>
Andrea Vitali</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0429be2e38678ca539510218141b4b8de7e24af8.png" data-download-href="/uploads/short-url/APliRzugyKm6AtAtGzd3MQ1OYM.png?dl=1" title="Error3Dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0429be2e38678ca539510218141b4b8de7e24af8_2_690x415.png" alt="Error3Dslicer" data-base62-sha1="APliRzugyKm6AtAtGzd3MQ1OYM" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0429be2e38678ca539510218141b4b8de7e24af8_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0429be2e38678ca539510218141b4b8de7e24af8_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0429be2e38678ca539510218141b4b8de7e24af8_2_1380x830.png 2x" data-dominant-color="474756"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error3Dslicer</span><span class="informations">1680×1011 73.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/559a3b1815464f9e924b3c732de05023c59830be.png" data-download-href="/uploads/short-url/cdh1qwTe46MLSkDr9M1qadBQnV4.png?dl=1" title="ErrorInEXE" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/559a3b1815464f9e924b3c732de05023c59830be.png" alt="ErrorInEXE" data-base62-sha1="cdh1qwTe46MLSkDr9M1qadBQnV4" width="690" height="361" data-dominant-color="0E0E0E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ErrorInEXE</span><span class="informations">976×512 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-01-22 16:30 UTC)

<p>Yes, it could be the path.  Be sure to use something very short.  I use <code>c:/s</code> for debug and <code>c:/sr</code> for release builds in windows.</p>

---

## Post #3 by @AndreaVitali86 (2022-01-24 10:24 UTC)

<p>Hi Steve,</p>
<p>thank you for your replay. However, the error still remain. We have tried with the generation of a standard loadable module and everything works fine.</p>
<p>I think that it should be better to move the discussion in the section “Development”.</p>
<p>Regards,</p>

---

## Post #4 by @jpdefrutos (2022-01-25 13:10 UTC)

<p>Hi,</p>
<p>We are experiencing the same situation on Windows 10, with a library compiled with our extension. The compiled .lib lives in the solution directory, close to C:\ to avoid any path-length related issues. Yet, the python script to build the UI fails to find the library and halts the execution, leaving the UI partly built. 3DSlicer v4.13.0, VS 2019 v16, Qt 5.15.02 and CMake 3.22.1.</p>
<p>The library is exported using the directive Q_SLICER_MODULE_${MODULE_NAME_UPPER}_WIDGETS_EXPORT and built using the flag WRAP_PYTHONQT (SlicerMacroBuildModuleWidget)</p>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>

---

## Post #5 by @AndreaVitali86 (2022-01-25 16:45 UTC)

<p>Hi Javier,</p>
<p>I have also tried:</p>
<ol>
<li>Generate the markups module library directly inside C:</li>
<li>Name the module with a single letter (“m”)</li>
</ol>
<p>The error still occur. I hope in the developers’ help.</p>

---

## Post #6 by @RafaelPalomar (2022-01-26 10:12 UTC)

<p><a class="mention" href="/u/andreavitali86">@AndreaVitali86</a>, <a class="mention" href="/u/jpdefrutos">@jpdefrutos</a>, the problem looks similar, but we cannot conclude it is the same problem yet.</p>
<p>What we have seen with <a class="mention" href="/u/jpdefrutos">@jpdefrutos</a> is that PythonD libraries generated are <code>.lib</code> files (I’m not a Windows user of Slicer, but I would expect a <code>.dll</code> to be generated in order to be loaded in run-time).</p>
<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a> does this make sense?</p>

---

## Post #7 by @pieper (2022-01-26 12:49 UTC)

<p>This is sounding like a cmake library issue either not generating, building, or copying the python wrapper files correctly.  It might also be that they aren’t being put in the path correctly for the launcher.  Maybe a good debug strategy would be to look at the files generated for loadable module code that works as expected in python and then see the corresponding pattern of wrapped code and libraries for any differences with the custom markup code.</p>

---

## Post #8 by @lassoan (2022-01-27 14:23 UTC)

<p>Can you post a link to your source code? Do you only see the errors if you try to use the qSlicerexePModuleWidgets from a Python scripted module?</p>

---

## Post #9 by @AndreaVitali86 (2022-01-28 19:27 UTC)

<p>Hi all,</p>
<p>I conferm the same issue mentioned by <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>: we have a<br>
<code>qSlicerCustomModuleWidgetsPythonQt.lib</code> instead of the <code>.dll</code> file</p>
<p>We have to check how the files are generated in Visual Studio as suggested by <a class="mention" href="/u/pieper">@pieper</a>. I will do it the next week.</p>
<p>About the questions of <a class="mention" href="/u/lassoan">@lassoan</a>:</p>
<ul>
<li>
<p>Can you post a link to your source code?<br>
I can post the code but we did not develop custom code inside the software modules automatically generated by the custom markups widget template.<br>
Anyway, this is the github repo: <code>https://github.com/AndreaVitali86/SlicerCustomMarkups</code></p>
</li>
<li>
<p>Do you only see the errors if you try to use the qSlicerexePModuleWidgets from a Python scripted module?<br>
The code is relative to a loadable module (<code>C++</code>) so, the builded files are imported during the initiliazation of 3D slicer: when the initialization phase of all the modules finishes the python console give us the reported error. In other words, we are not using a Python scripted module.</p>
</li>
</ul>
<p>Thank you very much for your efforts.</p>

---

## Post #10 by @lassoan (2022-01-28 21:28 UTC)

<p>I’ve submitted a pull request that fixes the module:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/AndreaVitali86/SlicerCustomMarkups/pull/1">
  <header class="source">

      <a href="https://github.com/AndreaVitali86/SlicerCustomMarkups/pull/1" target="_blank" rel="noopener">github.com/AndreaVitali86/SlicerCustomMarkups</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AndreaVitali86/SlicerCustomMarkups/pull/1" target="_blank" rel="noopener">Basic fixes</a>
    </h4>

    <div class="branches">
      <code>AndreaVitali86:main</code> ← <code>lassoan:basic-fixes</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-01-28" data-time="21:23:53" data-timezone="UTC">09:23PM - 28 Jan 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="5 commits changed 5 files with 11 additions and 59 deletions">
        <a href="https://github.com/AndreaVitali86/SlicerCustomMarkups/pull/1/files" target="_blank" rel="noopener">
          <span class="added">+11</span>
          <span class="removed">-59</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes the module that is discussed at
https://discourse.slicer.org/t/python-mes<span class="show-more-container"><a href="https://github.com/AndreaVitali86/SlicerCustomMarkups/pull/1" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">sage-failed-to-import-pythonqt-qslicerxxxxmodulewidgets/21575/9

The error message still persists and the markup option widget is not available in Python, but everything else works.
The https://github.com/SlicerHeart/SlicerSurfaceMarkup extension does not seem to have this issue, so it could be fixed by careful comparison.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The problem was that the code pieces that allow the template to be used as a test need to be removed.</p>
<p>I could not find the root cause of why Python-wrapping of the widgets does not work correctly (and thus the Python module cannot be imported and the <code>Failed to import PythonQt.qSlicerCustomMarkupsModuleWidgets</code> error is logged). But this extension does not seem to have this issue, so by making this extension more similar to it should fix the issue:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerHeart/SlicerSurfaceMarkup">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/33cc23d557463b95b4f4239b0807521f17223e3906e15054ad24e93b5c01891f/SlicerHeart/SlicerSurfaceMarkup" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" target="_blank" rel="noopener">GitHub - SlicerHeart/SlicerSurfaceMarkup: Extension to test the new grid...</a></h3>

  <p>Extension to test the new grid surface markup with - GitHub - SlicerHeart/SlicerSurfaceMarkup: Extension to test the new grid surface markup with</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
