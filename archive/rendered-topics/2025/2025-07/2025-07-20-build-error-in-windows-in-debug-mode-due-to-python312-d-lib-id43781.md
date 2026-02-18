# Build error in Windows in debug mode due to python312_d.lib

**Topic ID**: 43781
**Date**: 2025-07-20
**URL**: https://discourse.slicer.org/t/build-error-in-windows-in-debug-mode-due-to-python312-d-lib/43781

---

## Post #1 by @lassoan (2025-07-20 12:42 UTC)

<p>I’ve been building Slicer for a long while using the same scripts. I’ve updated to the latest Slicer main version (from a version maybe a few weeks ago), started a clean build from scratch (removed all build folders) and this latest version does not build due to python312_d.lib is not found when linking qSlicerBaseQTCore.</p>
<pre data-code-wrap="txt"><code class="lang-txt">165&gt;------ Build started: Project: qSlicerBaseQTCore, Configuration: Debug x64 ------
165&gt;LINK : fatal error LNK1104: cannot open file 'python312_d.lib'
</code></pre>
<p>Has anyone encountered this error?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---

## Post #2 by @lassoan (2025-07-20 12:54 UTC)

<p>The only mentions of python312_d.lib in any files in all build folders:</p>
<p>In <code>Python-3.12.10/PC/pyconfig.h</code>, <code>python-build/bin/Release/PC/pyconfig.h</code>, and <code>python-install\include\pyconfig.h</code>:</p>
<pre><code class="lang-auto">...
/* For an MSVC DLL, we can nominate the .lib files used by extensions */
#ifdef MS_COREDLL
#       if !defined(Py_BUILD_CORE) &amp;&amp; !defined(Py_BUILD_CORE_BUILTIN)
                /* not building the core - must be an ext */
#               if defined(_MSC_VER)
                        /* So MSVC users need not specify the .lib
                        file in their Makefile (other compilers are
                        generally taken care of by distutils.) */
#                       if defined(_DEBUG)
#                               pragma comment(lib,"python312_d.lib")
#                       elif defined(Py_LIMITED_API)
#                               pragma comment(lib,"python3.lib")
#                       else
#                               pragma comment(lib,"python312.lib")
#                       endif /* _DEBUG */
#               endif /* _MSC_VER */
#       endif /* Py_BUILD_CORE */
#endif /* MS_COREDLL */
...
</code></pre>
<p>In Slicer-build\Base\QTCore\qSlicerBaseQTCore.dir\Debug\qSlicerCoreApplication.obj:</p>
<pre><code class="lang-auto">/DEFAULTLIB:"python312_d.lib"
</code></pre>
<p>Modifying the pyconfig.h files from:</p>
<pre><code>#                               pragma comment(lib,"python312_d.lib")
</code></pre>
<p>to</p>
<pre><code>#                               pragma comment(lib,"python312.lib")
</code></pre>
<p>resolves the build problem, so something may have changed in how pyconfig.h is included or in <code>MS_COREDLL</code>, <code>Py_BUILD_CORE</code>, <code>Py_BUILD_CORE_BUILTIN</code>, <code>_MSC_VER</code>, or <code>_DEBUG</code> defines.</p>

---

## Post #3 by @cpinter (2025-07-30 11:48 UTC)

<p>For the record I have the very same problem with the latest version. We cannot really debug Slicer until this is solved, so unless everyone is on vacation, please try to chime in <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Thanks a lot!</p>

---

## Post #4 by @Benjamin_Bennett (2025-08-03 21:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="43781">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code> pragma comment(lib,"python312_d.lib")</code></p>
</blockquote>
</aside>
<p>do you want to just patch the source? there is already a pythonapplypatches.cmake.</p>
<p>Is there still a reason to just use the release library still on windows? it is change from 2013 i guess the cmake python build is that still case? ef28720</p>

---

## Post #5 by @lassoan (2025-08-03 21:30 UTC)

<p>Yes, just change the source (single line of change) and everything works. It is a very quick and easy workaround but of course it should be fixed properly.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> please have a look at this when you have time.</p>
<blockquote>
<p>Is there still a reason to just use the release library still on windows?</p>
</blockquote>
<p>The motivation for this is the same as before. When we build the application in Debug mode, we almost always do that to debug the Slicer application or extensions; and not to debug implementation of low-level libraries such as CPython. Building Python in Release mode allows us to have much better Python runtime performance.</p>

---

## Post #6 by @jcfr (2025-08-03 23:01 UTC)

<p>Corresponding patch should be added to <a href="https://github.com/python-cmake-buildsystem/cpython?tab=readme-ov-file#available-branches">https://github.com/python-cmake-buildsystem/cpython?tab=readme-ov-file#available-branches</a> and then integrated to <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/tree/master/patches/3.12">https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/tree/master/patches/3.12</a></p>

---

## Post #7 by @jcfr (2025-08-03 23:07 UTC)

<p>Alternatively, the <code>undef</code> of <code>_DEBUG</code> is already taking care of here:</p>
<ul>
<li><a href="https://github.com/commontk/PythonQt/blob/7f7105ba9ec59d719ded80090e049fa85ad76e79/src/PythonQtPythonInclude.h#L95">PythonQtPythonInclude.h</a></li>
<li><a href="https://github.com/Slicer/VTK/blob/slicer-v9.5.0-2025-06-19-e70c856bd/Utilities/Python/vtkPython.h#L40">vtkPython.h</a></li>
</ul>
<p>The right solution would then to either add a MRML or Slicer specific header or include Python using the PythonQt or VTK one.</p>

---

## Post #8 by @Benjamin_Bennett (2025-08-04 01:05 UTC)

<p>I just added it to the pythonapplypatches .  i have a local crude multi-machine build that I use git to sync my builds.</p>
<p>What way is preferred way? I did the patch applying because that is what I found first .</p>

---

## Post #9 by @lassoan (2025-08-18 01:05 UTC)

<p>I’ve created a pull request with a simple fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8651">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8651" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8651" target="_blank" rel="noopener">COMP: Fix Windows build error in debug mode due to python312_d.lib</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:fix-python312_d-error</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-08-18" data-time="00:52:48" data-timezone="UTC">12:52AM - 18 Aug 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 0 additions and 3 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8651/files" target="_blank" rel="noopener">
            <span class="added">+0</span>
            <span class="removed">-3</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes the build error described in https://discourse.slicer.org/t/build-error-in<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8651" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">-windows-in-debug-mode-due-to-python312-d-lib/43781/8

Python.h cannot be directly included in an application on Windows, because the linked library is specified in the Python.h header file, but the application's build mode (Debug, Release, etc.) is not always the same as Python's build mode (always Release in Slicer). This is a well-known issue and workarounds are implemented in PythonQt and VTK: https://github.com/commontk/PythonQt/blob/7f7105ba9ec59d719ded80090e049fa85ad76e79/src/PythonQtPythonInclude.h#L95 https://github.com/Slicer/VTK/blob/slicer-v9.5.0-2025-06-19-e70c856bd/Utilities/Python/vtkPython.h#L40

Since including "PythonQt.h" automatically includes "Python.h" with the appropriate workarounds, the best solution to the build error is simply not including "Python.h" directly.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In <a href="https://github.com/python/cpython/blob/bc2872445b2aee4bb4e001d4171489d7123b1daf/PC/pyconfig.h#L332C36-L332C44">latest Python version</a> a separate <code>Py_DEBUG</code> option is used, so the Python build mode can be specified separately from the application’s build mode.</p>

---

## Post #10 by @cpinter (2025-08-18 09:41 UTC)

<p>Thank you very much Andras! What a nice simple fix!</p>

---
