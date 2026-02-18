# Support --designer launcher argument for Qt5 build

**Topic ID**: 1917
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/support-designer-launcher-argument-for-qt5-build/1917

---

## Post #1 by @cpinter (2018-01-23 17:39 UTC)

<p>The --designer launcher switch doesn’t work with Qt5 builds. It seems that it’s because the variable checked at this line is empty:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/CMake/SlicerMacroBuildApplication.cmake#L543" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/CMake/SlicerMacroBuildApplication.cmake#L543" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/CMake/SlicerMacroBuildApplication.cmake#L543</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="533" style="counter-reset: li-counter 532 ;">
<li># Configure Launcher</li>
<li># --------------------------------------------------------------------------</li>
<li>if(SLICERAPP_CONFIGURE_LAUNCHER)</li>
<li>  if(Slicer_USE_CTKAPPLAUNCHER)</li>
<li>
</li>
<li>    find_package(CTKAppLauncher REQUIRED)</li>
<li>
</li>
<li>    # Define list of extra 'application to launch' to associate with the launcher</li>
<li>    # within the build tree</li>
<li>    set(extraApplicationToLaunchListForBuildTree)</li>
<li class="selected">
</li>
<li>    if(${Slicer_REQUIRED_QT_VERSION} VERSION_GREATER_EQUAL 5 AND NOT QT_DESIGNER_EXECUTABLE)</li>
<li>      # Since Qt only provides a CMake module to find the designer library, we work</li>
<li>      # around this limitation by finding the designer executable.</li>
<li>      find_program(QT_DESIGNER_EXECUTABLE designer Designer "${QT_BINARY_DIR}")</li>
<li>    endif()</li>
<li>
</li>
<li>    if(EXISTS ${QT_DESIGNER_EXECUTABLE})</li>
<li>      ctkAppLauncherAppendExtraAppToLaunchToList(</li>
<li>        LONG_ARG designer</li>
<li>        HELP "Start Qt designer using Slicer plugins"</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>It would be great if this variable was set for Qt5 automatically. Any ideas how to make that happen?</p>

---

## Post #2 by @jcfr (2018-01-24 00:03 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="29" data-topic="952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"><a href="https://discourse.slicer.org/t/qt5-build-a-few-hiccups/952/29">Qt5 build : a few hiccups</a></div>
<blockquote>
<p>Any ideas how to make that happen?</p>
</blockquote>
</aside>
<p>Thanks to a PR of <a class="mention" href="/u/adamrankin">@adamrankin</a> and inputs from <a class="mention" href="/u/msmolens">@msmolens</a> and <a class="mention" href="/u/ihnorton">@ihnorton</a> , this is now fixed by <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26856">26856</a> and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26859">26859</a></p>

---

## Post #3 by @jcfr (2018-12-06 05:57 UTC)

<p>Commit <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27608" rel="nofollow noopener">r27608</a> fixes the lookup of the designer executable ensuring the one associated with the Qt5 version being is used is found.</p>

---
