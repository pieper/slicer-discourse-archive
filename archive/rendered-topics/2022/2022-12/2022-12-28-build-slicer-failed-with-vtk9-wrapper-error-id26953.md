---
topic_id: 26953
title: "Build Slicer Failed With Vtk9 Wrapper Error"
date: 2022-12-28
url: https://discourse.slicer.org/t/26953
---

# Build  Slicer  Failed with   VTK9  Wrapper Error

**Topic ID**: 26953
**Date**: 2022-12-28
**URL**: https://discourse.slicer.org/t/build-slicer-failed-with-vtk9-wrapper-error/26953

---

## Post #1 by @Hanzhang_DAI (2022-12-28 05:25 UTC)

<p>Build  Command  :</p>
<pre><code class="lang-auto">cmake.exe ^
  -G "Visual Studio 17 2022" ^
  -A x64 ^
  -DQt5_DIR:PATH=C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5  ^
  -DBUILD_TESTING=OFF    ^
  -DSlicer_USE_QtTesting=OFF   ^
  -DSlicer_BUILD_DOCUMENTATION=OFF ^
C:\SD
</code></pre>
<p>and  then</p>
<pre><code class="lang-auto">cmake.exe  --build  .  --conifg Debug
</code></pre>
<pre><code class="lang-auto"> WrappingTools.vcxproj -&gt; C:\SDR\VTK-build\bin\Debug\vtkWrappingTools-9.1d.dll
    WrapHierarchy.vcxproj -&gt; C:\SDR\VTK-build\bin\Debug\vtkWrapHierarchy-9.1d.exe
    Generating the wrap hierarchy for VTK::CommonCore
    vtkWrapHierarchy-9.1d.exe: In C:/SDR/VTK/Common/Core/vtkArrayIteratorIncludes.h:44: syntax error.
C:\Program Files\Microsoft Visual Studio\2022\Enterprise\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(247,5):
error MSB8066: “C:\SDR\VTK-build\CMakeFiles\1cfbdef9874d7fdc273814d48bd74a5b\vtkCommonCore-hierarchy.txt.rule;C:\SDR\VT
K-build\CMakeFiles\df4d66c3f6286a66ff3e7e6450b91535\vtkCommonCore-hierarchy.rule”的自定义生成已退出，代码为 1。 [C:\SDR\VTK-build\Com
mon\Core\vtkCommonCore-hierarchy.vcxproj] [C:\SDR\VTK.vcxproj]
    Interaction.vcxproj -&gt; C:\SDR\VTK-build\bin\Debug\vtkInteraction-9.1d.dll
    ViewsCore-objects.vcxproj -&gt; C:\SDR\VTK-build\Views\Core\ViewsCore-objects.dir\Debug\ViewsCore-objects.lib
    ViewsContext2D-objects.vcxproj -&gt; C:\SDR\VTK-build\Views\Context2D\ViewsContext2D-objects.dir\Debug\ViewsContext2D-
  objects.lib
    sqlitebin.vcxproj -&gt; C:\SDR\VTK-build\bin\Debug\sqlitebin-9.1d.exe
C:\Program Files\Microsoft Visual Studio\2022\Enterprise\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(247,5):
error MSB8066: “C:\SDR\CMakeFiles\0ca0d5233e679e5f621ec3684d706eb7\VTK-update.rule;C:\SDR\CMakeFiles\0ca0d5233e679e5f62
1ec3684d706eb7\VTK-patch.rule;C:\SDR\CMakeFiles\0ca0d5233e679e5f621ec3684d706eb7\VTK-configure.rule;C:\SDR\CMakeFiles\0
ca0d5233e679e5f621ec3684d706eb7\VTK-build.rule;C:\SDR\CMakeFiles\0ca0d5233e679e5f621ec3684d706eb7\VTK-create_egg_info.r
ule;C:\SDR\CMakeFiles\0ca0d5233e679e5f621ec3684d706eb7\VTK-install.rule;C:\SDR\CMakeFiles\9da03540a85529a975aa26e942872
eb0\VTK-complete.rule;C:\SDR\CMakeFiles\a93f313db68a08233b06795067f443c0\VTK.rule”的自定义生成已退出，代码为 1。 [C:\SDR\VTK.vcxproj]
</code></pre>

---

## Post #2 by @jcfr (2022-12-28 05:41 UTC)

<p>To help understand the command and associated errors, I edited your text to use both backquotes <sup class="footnote-ref"><a href="#footnote-88156-1" id="footnote-ref-88156-1">[1]</a></sup> and  <code>^</code> to split windows command.</p>
<p>Could you indicate which version of Slicer you are attempt to build ?</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-88156-1" class="footnote-item">
<p><a href="https://meta.discourse.org/t/select-the-programming-language-used-in-code-blocks/19247" class="inline-onebox">Select the programming language used in code blocks - users - Discourse Meta</a> <a href="#footnote-ref-88156-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #3 by @Hanzhang_DAI (2022-12-28 10:05 UTC)

<p>Thank U .   Slice Version is v5.2.1  .     a builted  vtk9.1 without python-wrapper  in  system environment variable path.   is conflict with    ?</p>

---

## Post #4 by @Hanzhang_DAI (2022-12-28 10:06 UTC)

<p>I  run command with  admin privileges.</p>

---

## Post #5 by @lassoan (2022-12-28 13:46 UTC)

<aside class="quote no-group" data-username="Hanzhang_DAI" data-post="3" data-topic="26953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hanzhang_dai/48/17842_2.png" class="avatar"> Hanzhang_DAI:</div>
<blockquote>
<p>Slice Version is v5.2.1 . a builted vtk9.1 without python-wrapper in system environment variable path. is conflict with</p>
</blockquote>
</aside>
<p>If you have shared libraries in a folder that is in your system PATH environment variable then anything can happen, including build and/or runtime failure of any application. Therefore, the system PATH environment variable should be kept clean - there are several alternative ways to make utilities conveniently available, for example using <a href="https://learn.microsoft.com/en-gb/windows/win32/shell/app-registration">App Paths registry key</a>.</p>
<p>Confusing entries in the system PATH might have corrupted your build. So after removing all non-system paths from your PATH I would recommend to delete the entire Slicer build folder and restart the build from scratch. I would also recommend putting your build commands into a .bat file to allow (re)building Slicer anytime by a single click.</p>

---
