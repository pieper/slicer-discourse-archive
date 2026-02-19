---
topic_id: 8810
title: "Failed To Build Slicercustomapptemplate"
date: 2019-10-17
url: https://discourse.slicer.org/t/8810
---

# Failed to build SlicerCustomAppTemplate

**Topic ID**: 8810
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/failed-to-build-slicercustomapptemplate/8810

---

## Post #1 by @rleguay (2019-10-17 08:44 UTC)

<p>Hi everyone,</p>
<p>I tried to build a custom app using the great <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="nofollow noopener">SlicerCustomAppTemplate</a> on Windows 10 with Qt 5.12.4 and VS 2017 in 64 bits. I have Git and SVN installed (is SVN still required?).</p>
<p>If I checked the option <code>Slicer_WITH_LIBRARY_VERSION</code>, the compilation failed during the configuration of ModuleDescriptionParser due to <code>ModuleDescriptionParser_LIBRARY_PROPERTIES</code> variable and <code>set_target_properties(${lib_name} PROPERTIES ${ModuleDescriptionParser_LIBRARY_PROPERTIES})</code> (line 198 of SlicerExecutionModel/ModuleDescriptionParser/CMakeLists.txt)</p>
<p>I just uncheck this option and the compilation work like a charm.</p>
<p>So two questions:</p>
<ul>
<li>Does this option still used?</li>
<li>Does this option work on Windows?</li>
</ul>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-10-17 13:03 UTC)

<p>I don’t think the option is commonly used, but it should work. On Windows, too.</p>
<p>Can you copy here the complete error message?</p>

---

## Post #3 by @Sam_Horvath (2019-10-17 15:23 UTC)

<p>I would guess that this is somehow related to the wrong version info (Slicer vs custom app) leaking in through this option. <a class="mention" href="/u/jcfr">@jcfr</a> ??</p>
<p>Trying a build now to test.</p>

---

## Post #4 by @Sam_Horvath (2019-10-17 20:25 UTC)

<p>So, enabling this option breaks the standard Slicer build as well.</p>
<p>The target properties are set here:</p>
<pre><code>if(Slicer_WITH_LIBRARY_VERSION)
  set(Slicer_LIBRARY_PROPERTIES ${Slicer_LIBRARY_PROPERTIES}
    VERSION ${Slicer_VERSION_FULL}
    SOVERSION ${Slicer_VERSION}
  )
endif()
</code></pre>
<p>But the resulting string list is:</p>
<p><code>VERSION;SOVERSION;4.11.0</code></p>
<p>working on a fix for this</p>

---

## Post #5 by @Sam_Horvath (2019-10-17 20:55 UTC)

<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1233" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/1233" target="_blank" rel="nofollow noopener">COMP:  Re-order CMakeLists to allow for build with Library Version op…</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>sjh26:library-version-fix</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-10-17" data-time="20:55:02" data-timezone="UTC">08:55PM - 17 Oct 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="nofollow noopener">
          <img alt="sjh26" src="https://avatars2.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 10 additions and 9 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/1233/files" target="_blank" rel="nofollow noopener">
          <span class="added">+10</span>
          <span class="removed">-9</span>
        </a>
      </div>
    </div>

  </div>
</div>
  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @rleguay (2019-10-18 07:53 UTC)

<p>Sorry for the late answer: it took a lot of time to build Slicer (I activated the ITK Python build too).<br>
Even if there is a fix I put the error messages:</p>
<pre><code class="lang-auto">36&gt;CMake Error at Libs/ITKFactoryRegistration/CMakeLists.txt:101 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/vtkAddon/CMakeLists.txt:129 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/vtkTeem/CMakeLists.txt:108 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/vtkITK/CMakeLists.txt:159 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/vtkSegmentationCore/CMakeLists.txt:98 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/FreeSurfer/CMakeLists.txt:96 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/MRML/Core/CMakeLists.txt:282 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/MRML/CLI/CMakeLists.txt:95 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/RemoteIO/CMakeLists.txt:108 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/MRML/Logic/CMakeLists.txt:116 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/MRML/DisplayableManager/CMakeLists.txt:192 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/MRML/IDImageIO/CMakeLists.txt:92 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Libs/MRML/Widgets/CMakeLists.txt:511 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at Base/Logic/CMakeLists.txt:176 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
...
36&gt;CMake Error at CMake/SlicerMacroBuildBaseQtLibrary.cmake:212 (set_target_properties):
36&gt;  set_target_properties called with incorrect number of arguments.
36&gt;Call Stack (most recent call first):
36&gt;  Base/QTCore/CMakeLists.txt:251 (SlicerMacroBuildBaseQtLibrary)
...
</code></pre>

---

## Post #7 by @Sam_Horvath (2019-10-18 15:02 UTC)

<p>The fix for this has been merged into Slicer master:<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/96a3d7240587d1a957ac5df8c962e78ec0b9074c" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/96a3d7240587d1a957ac5df8c962e78ec0b9074c" target="_blank" rel="nofollow noopener">COMP:  Re-order CMakeLists to allow for build with Library Version option</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-10-18" data-time="14:53:09" data-timezone="UTC">02:53PM - 18 Oct 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="nofollow noopener">
          <img alt="sjh26" src="https://avatars2.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 10 additions and 9 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/96a3d7240587d1a957ac5df8c962e78ec0b9074c" target="_blank" rel="nofollow noopener">
          <span class="added">+10</span>
          <span class="removed">-9</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Slicer_WITH_LIBRARY_VERSION requires the full version info from Slicer
svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28561
git-svn-id: http://svn.slicer.org/Slicer4/trunk@28561 3bd1e089-480b-0410-8dfb-8563597acbee</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>You should update your custom app to use this git hash, and do a clean build with the option enabled.</p>

---
