# 3D slicer Windows 10 Build Fail (only SimpleITK project)

**Topic ID**: 6727
**Date**: 2019-05-08
**URL**: https://discourse.slicer.org/t/3d-slicer-windows-10-build-fail-only-simpleitk-project/6727

---

## Post #1 by @hwanid (2019-05-08 03:41 UTC)

<p>Hello, I’m trying to build 3D slicer with 2019-4-30 files<br>
but, Every project is success except “SimpleITK” project</p>
<p>Is there any way to fix this?</p>
<p>Error LNK1112</p>
<p>‘x86’ [C:\Slicer-master-bin\SimpleITK-build\Lua-prefix\src\Lua-build\CMakeFiles\CMakeTmp\cmTC_62d6d.vcxproj] [C:\Slicer-master-bin\SimpleITK-build\Lua.vcxproj]</p>
<p>SimpleITK	<br>
C:\Slicer-master-bin\cmTC_62d6d.dir\Debug\testCCompiler.obj</p>
<p>More detail is below…</p>
<p>I’m on my work with</p>
<p>Windows 10<br>
CMake 3.14.3 with configure msvc 2017 &amp; x64 &amp; v140<br>
msvc2017 with v140<br>
Qt 5.9.5 + WebEngine + Script<br>
SlikSvn</p>
<p>Thank you</p>
<hr>
<p>for more detail, this is my CMake configure<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b06a18b07cb584b567cd10104af745c8d67f95f0.jpeg" data-download-href="/uploads/short-url/paDlpDFzBb7XK5I6S6gZGbDzRle.jpeg?dl=1" title="cmake%20configurelist" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b06a18b07cb584b567cd10104af745c8d67f95f0_2_301x500.jpeg" alt="cmake%20configurelist" data-base62-sha1="paDlpDFzBb7XK5I6S6gZGbDzRle" width="301" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b06a18b07cb584b567cd10104af745c8d67f95f0_2_301x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b06a18b07cb584b567cd10104af745c8d67f95f0_2_451x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b06a18b07cb584b567cd10104af745c8d67f95f0_2_602x1000.jpeg 2x" data-dominant-color="F17173"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cmake%20configurelist</span><span class="informations">971×1611 375 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<hr>
<p>this is full error message</p>
<p>1&gt;------ 모두 다시 빌드 시작: 프로젝트: SimpleITK, 구성: Debug x64 ------<br>
1&gt;Creating directories for ‘SimpleITK’<br>
1&gt;Building Custom Rule C:/Slicer-master/CMakeLists.txt<br>
1&gt;CMake does not need to re-run because C:/Slicer-master-bin/CMakeFiles/generate.stamp is up-to-date.<br>
1&gt;No download step for ‘SimpleITK’<br>
1&gt;No update step for ‘SimpleITK’<br>
1&gt;No patch step for ‘SimpleITK’<br>
1&gt;Performing configure step for ‘SimpleITK’<br>
1&gt;loading initial cache file C:/Slicer-master-bin/SimpleITK-prefix/tmp/SimpleITK-cache-Debug.cmake<br>
1&gt;-- Passing variable “BUILD_DOXYGEN=OFF” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_4D_IMAGES=ON” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_BUILD_DISTRIBUTE=ON” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_GIT_PROTOCOL=https” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_INSTALL_ARCHIVE_DIR=./lib/Slicer-4.11” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_INSTALL_LIBRARY_DIR=./lib/Slicer-4.11” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_INT64_PIXELIDS=OFF” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_LUA_EXECUTABLE=C:/Slicer-master-bin/SimpleITK-build/Lua/bin/lua” to SimpleITK external project.<br>
1&gt;-- Passing variable “SimpleITK_PYTHON_THREADS=ON” to SimpleITK external project.<br>
1&gt;-- Configuring done<br>
1&gt;-- Generating done<br>
1&gt;-- Build files have been written to: C:/Slicer-master-bin/SimpleITK-build<br>
1&gt;Performing build step for ‘SimpleITK’<br>
1&gt;.NET Framework용 Microsoft (R) Build Engine 버전 15.7.177.53362<br>
1&gt;Copyright (C) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;  Generating C:/Slicer-master-bin/SimpleITK-build/ExternalData/.ExternalSource/lua-5.1.5.tar.gz<br>
1&gt;  – Found object: “C:/Slicer-master-bin/ExternalData/Objects/MD5/2e115fe26e435e33b0d5c022e4490567”<br>
1&gt;  Generating C:/Slicer-master-bin/SimpleITK-build/ExternalData/.ExternalSource/virtualenv-15.1.0.tar.gz<br>
1&gt;  – Found object: “C:/Slicer-master-bin/ExternalData/Objects/MD5/44e19f4134906fe2d75124427dc9b716”<br>
1&gt;  Creating directories for ‘Lua’<br>
1&gt;  Building Custom Rule C:/Slicer-master-bin/SimpleITK/SuperBuild/CMakeLists.txt<br>
1&gt;  CMake does not need to re-run because C:/Slicer-master-bin/SimpleITK-build/CMakeFiles/generate.stamp is up-to-date.<br>
1&gt;  Performing download step (verify and extract) for ‘Lua’<br>
1&gt;  – verifying file…<br>
1&gt;       file=‘C:/Slicer-master-bin/SimpleITK-build/ExternalData/.ExternalSource/lua-5.1.5.tar.gz’<br>
1&gt;  – verifying file… done<br>
1&gt;  – extracting…<br>
1&gt;       src=‘C:/Slicer-master-bin/SimpleITK-build/ExternalData/.ExternalSource/lua-5.1.5.tar.gz’<br>
1&gt;       dst=‘C:/Slicer-master-bin/SimpleITK-build/Lua-prefix/src/Lua’<br>
1&gt;  – extracting… [tar xfz]<br>
1&gt;  – extracting… [analysis]<br>
1&gt;  – extracting… [rename]<br>
1&gt;  – extracting… [clean up]<br>
1&gt;  – extracting… done<br>
1&gt;  No update step for ‘Lua’<br>
1&gt;  Performing patch step for ‘Lua’<br>
1&gt;  Performing configure step for ‘Lua’<br>
1&gt;  Not searching for unused variables given on the command line.<br>
1&gt;  loading initial cache file C:/Slicer-master-bin/SimpleITK-build/Lua-prefix/src/Lua-build/CMakeCacheInit.txt<br>
1&gt;  – The C compiler identification is MSVC 19.14.26428.1<br>
1&gt;  – Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe<br>
1&gt;  – Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe – broken<br>
1&gt;  CMake Error at C:/Support/cmake-3.14.3-win64-x64/share/cmake-3.14/Modules/CMakeTestCCompiler.cmake:60 (message):<br>
1&gt;    The C compiler<br>
1&gt;<br>
1&gt;      “C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe”<br>
1&gt;<br>
1&gt;    is not able to compile a simple test program.<br>
1&gt;<br>
1&gt;    It fails with the following output:<br>
1&gt;<br>
1&gt;      Change Dir: C:/Slicer-master-bin/SimpleITK-build/Lua-prefix/src/Lua-build/CMakeFiles/CMakeTmp<br>
1&gt;<br>
1&gt;      Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/MSBuild/15.0/Bin/MSBuild.exe cmTC_62d6d.vcxproj /p:Configuration=Debug /p:Platform=Win32 /p:VisualStudioVersion=15.0 /v:m<br>
1&gt;      .NET Framework??Microsoft (R) Build Engine 踰꾩쟾 15.7.177.53362<br>
1&gt;      Copyright (C) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;        x86??Microsoft (R) C/C++ 理쒖쟻??而댄뙆?쇰윭 踰꾩쟾 19.14.26428.1<br>
1&gt;        Copyright (c) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;        cl /c /Zi /W2 /WX- /diagnostics:classic /Od /Ob0 /Oy- /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR="Debug"” /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_62d6d.dir\Debug\" /Fd"cmTC_62d6d.dir\Debug\vc141.pdb" /Gd /TC /analyze- /errorReport:queue “C:\Slicer-master-bin\SimpleITK-build\Lua-prefix\src\Lua-build\CMakeFiles\CMakeTmp\testCCompiler.c”<br>
1&gt;        testCCompiler.c<br>
1&gt;<br>
1&gt;cmTC_62d6d.dir\Debug\testCCompiler.obj : fatal error LNK1112: ‘x86’ [C:\Slicer-master-bin\SimpleITK-build\Lua-prefix\src\Lua-build\CMakeFiles\CMakeTmp\cmTC_62d6d.vcxproj] [C:\Slicer-master-bin\SimpleITK-build\Lua.vcxproj]<br>
1&gt;<br>
1&gt;<br>
1&gt;<br>
1&gt;<br>
1&gt;    CMake will not be able to correctly generate this project.<br>
1&gt;  Call Stack (most recent call first):<br>
1&gt;    CMakeLists.txt:3 (project)<br>
1&gt;<br>
1&gt;<br>
1&gt;  – Configuring incomplete, errors occurred!<br>
1&gt;  See also “C:/Slicer-master-bin/SimpleITK-build/Lua-prefix/src/Lua-build/CMakeFiles/CMakeOutput.log”.<br>
1&gt;  See also “C:/Slicer-master-bin/SimpleITK-build/Lua-prefix/src/Lua-build/CMakeFiles/CMakeError.log”.<br>
1&gt;“SimpleITK.vcxproj” 프로젝트를 빌드했습니다. - 실패(failure)<br>
========== 모두 다시 빌드: 성공 0, 실패 1, 생략 0 ==========</p>
<hr>

---

## Post #2 by @lassoan (2019-05-08 04:53 UTC)

<aside class="quote no-group" data-username="hwanid" data-post="1" data-topic="6727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/a6a055/48.png" class="avatar"> hwanid:</div>
<blockquote>
<p>1&gt; “C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.14.26428/bin/Hostx86/x86/cl.exe”<br>
1&gt;<br>
1&gt; is not able to compile a simple test program.</p>
</blockquote>
</aside>
<p>This indicates that you somehow not use the VS2015 (v140) toolset.<br>
Maybe disable SimpleITK for now and see if build completes successfully then.</p>

---

## Post #3 by @hwanid (2019-05-08 06:27 UTC)

<p>Thank you! I’ll do that.<br>
By the way, the slicer is successfully build although SimpleITK is failed<br>
Is it ok if I use this slicer?<br>
it looks working<br>
SimpleITK is only for increase speed?</p>

---

## Post #4 by @pieper (2019-05-08 12:09 UTC)

<p>SimpleITK is only used in some modules, like the SimpleFilters, so it’s a soft dependency.  For most uses you probably don’t need SimpleITK.</p>

---

## Post #5 by @jamesobutler (2019-05-08 22:23 UTC)

<p>I have faced this issue as well when building Slicer 4.10.1 tag in debug mode.  Slicer_USE_SimpleITK is selected as well as Slicer_SimpleITK_SHARED in the cmake configuration.  I also have definitely specified to build with the v140 toolset and can confirm the projects are listed with (Visual Studio 2015) listed next to them in Visual Studio.</p>
<p>I remember back in the day an issue with building SimpleITK in debug mode and I think that was solved in <a href="https://github.com/Slicer/Slicer/commit/f77b8075d436dfe9d3ff21874422132ab7dcb4c1" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/f77b8075d436dfe9d3ff21874422132ab7dcb4c1</a>, but maybe this was broken again?</p>

---

## Post #6 by @lassoan (2019-05-09 02:40 UTC)

<p>I build Slicer with SimpleITK on Windows on several computers without problems, both in debug and release mode, in stable (4.10) and master branch.</p>

---

## Post #7 by @jamesobutler (2019-05-09 12:44 UTC)

<p>I deleted the SimpleITK directories from my C:/S4.10D directory and tried building again, but the SimpleITK project failed again.</p>
<p>I noticed this line in the build output:</p>
<pre><code class="lang-auto">45&gt;luaexec.dir\Debug\lua.obj : fatal error LNK1112: module machine type 'x86' conflicts with target machine type 'x64' [C:\S4.10D\SimpleITK-build\Lua-prefix\src\Lua-build\luaexec.vcxproj] [C:\S4.10D\SimpleITK-build\Lua.vcxproj]
</code></pre>
<p>Could this be because I was using CMake 3.14.3, where I specifed the generator “Visual Studio 15 2017” and then specified the optional platform generator “x64” in the new line below. It otherwise says “if empty, generator uses: Win32”.  Then I also specified the optional toolset “v140”</p>
<p>My CMake configuration included the following entries:<br>
CMAKE_INSTALL_PREFIX = C:/Program Files (x86)/Slicer<br>
CMAKE_LINKER = C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/link.exe<br>
CMAKE_EXE_LINKER_FLAGS = /machine:x64<br>
CMAKE_MODULE_LINKER_FLAGS = /machine:x64<br>
CMAKE_SHARED_LINKER_FLAGS = /machine:x64<br>
CMAKE_STATIC_LINKER_FLAGS = /machine:x64</p>

---

## Post #8 by @lassoan (2019-05-09 16:56 UTC)

<p>It all sounds correct.</p>
<p>I’ve checked my debug-mode build and I have a Lua build there. I don’t think it is needed. We don’t use Lua. Maybe you can try to disable it (WRAP_LUA=&gt;OFF).</p>

---

## Post #9 by @jamesobutler (2019-05-09 18:00 UTC)

<p>I used CMake GUI to review the cmake configuration that the Slicer build project did for the SimpleITK project</p>
<p>Source: C:/S4.10D/SimpleITK<br>
Binaries: C:/S4.10D/SimpleITK-build</p>
<p>SimpleITK_USE_SYSTEM_LUA = OFF<br>
WRAP_LUA = OFF</p>

---

## Post #10 by @lassoan (2019-05-09 18:58 UTC)

<p>I’ve just checked and I have WRAP_LUA turned off, too. It seems that even if you turn off Lua wrapping, Lua is still built. Maybe you can ask why is this on the ITK forum (or maybe <a class="mention" href="/u/blowekamp">@blowekamp</a> can respond directly here).</p>
<p>The <code>lua.obj</code> file (that you get the error message for, because it is 32-bit on your system) on my system is 64-bit. At least, when I dump its content using <code>c:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64&gt;dumpbin.exe c:\D\S4D\SimpleITK-build\Lua-prefix\src\Lua-build\luaexec.dir\Debug\lua.obj /headers</code> I get this:</p>
<pre><code class="lang-auto">...
FILE HEADER VALUES
            8664 machine (x64)
...
</code></pre>
<p>I’ve started to use a new computer, and building Slicer right now with VS2019 IDE with VS2015 toolset, with latest CMake. We’ll see if I run into the same issue.</p>

---

## Post #11 by @blowekamp (2019-05-09 19:28 UTC)

<p>Hello,</p>
<p>The little “Lua” executable is needed for code generation for Simple ITK.</p>
<p>It looks like you might have specified the new “CMAKE_GENERATOR_PLATFORM” option instead of using the traditional platform in the generator. Support for this in SimpleITK was added here:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/SimpleITK/SimpleITK/commit/c1efa68601da3c44b89041db36a1fdf2a323d474#diff-1016ed022fec540a9fe0dbeb04c8b3af">
  <header class="source">

      <a href="https://github.com/SimpleITK/SimpleITK/commit/c1efa68601da3c44b89041db36a1fdf2a323d474#diff-1016ed022fec540a9fe0dbeb04c8b3af" target="_blank" rel="noopener nofollow ugc">github.com/SimpleITK/SimpleITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SimpleITK/SimpleITK/commit/c1efa68601da3c44b89041db36a1fdf2a323d474" target="_blank" rel="noopener nofollow ugc">Support additional CMake generator variables in Superbuild</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-03-06" data-time="21:15:43" data-timezone="UTC">09:15PM - 06 Mar 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/blowekamp" target="_blank" rel="noopener nofollow ugc">
          <img alt="blowekamp" src="https://avatars.githubusercontent.com/u/321061?v=4" class="onebox-avatar-inline" width="20" height="20">
          blowekamp
        </a>
      </div>

      <div class="lines" title="changed 1 files with 3 additions and 0 deletions">
        <a href="https://github.com/SimpleITK/SimpleITK/commit/c1efa68601da3c44b89041db36a1fdf2a323d474" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+3</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Ensure propagation of generator variables such as the architecture to
the superb<span class="show-more-container"><a href="https://github.com/SimpleITK/SimpleITK/commit/c1efa68601da3c44b89041db36a1fdf2a323d474" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">uild subprojects.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>A work around it to use the traditional way to specify the platform with the generator string: <a href="https://cmake.org/cmake/help/v3.10/generator/Visual%20Studio%2015%202017.html" class="inline-onebox" rel="noopener nofollow ugc">Visual Studio 15 2017 — CMake 3.10.3 Documentation</a></p>
<p>This SimpleITK patch does not appear to be in the slicer fork, it should be updated along the SimpleITK <code>release</code> branch.</p>

---

## Post #12 by @jamesobutler (2019-05-09 21:38 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> It appears that the Slicer/SimpleITK repo will need to have an updated branch created with this patch. Also, unclear what to do about building Slicer 4.10.1 stable.<br>
Either update the SimpleITK branch specified when building the Slicer-4.10 branch or update the build instructions for 4.10 to not use CMake &gt;3.14 or update to specify to use the old way with the platform with the generator string?</p>

---

## Post #13 by @lassoan (2019-05-09 22:41 UTC)

<p>If we create a new patch release (Slicer-4.10.2) then we may add CMake-3.14&gt; compatibility there, but 4.10.1 will require older CMake. Updating build instructions should be enough.</p>
<p>CMake usually handles API changes very nicely. If indeed new CMake cannot build older projects then CMake must be fixed. If the old style is deprecated now, it should be still supported for at least a year, to allow software libraries to transition smoothly.</p>

---

## Post #14 by @jcfr (2019-05-09 23:56 UTC)

<p>Outstanding detective work <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>Either update the SimpleITK branch specified when building the Slicer-4.10 branch or update the build instructions for 4.10 to not use CMake &gt;3.14 or update to specify to use the old way with the platform with the generator string?</p>
</blockquote>
<p>It will be easy enough to backport that fixes in 4.10.2. We will also apply the fix right away in Slicer.</p>
<p>Note that using CMake &gt; 3.14 is still possible, you just need to specify the Win64 string.</p>
<blockquote>
<p>If indeed new CMake cannot build older projects then CMake must be fixed. If the old style is deprecated now, it should be still supported for at least a year, to allow software libraries to transition smoothly.</p>
</blockquote>
<p>To clarify, specifying <code>Win64</code> after the generator name for VS 2015 and older is still supported even with the latest CMake. It is not available only when using VS 2019.</p>
<p>See <a href="https://cmake.org/cmake/help/v3.14/generator/Visual%20Studio%2015%202017.html#platform-selection" class="inline-onebox">Visual Studio 15 2017 — CMake 3.14.7 Documentation</a></p>
<p>The <code>-A</code> argument and associated option <code>CMAKE_GENERATOR_PLATFORM</code> have been introduced a while back. See <a href="https://cmake.org/cmake/help/latest/release/3.1.html#variables" class="inline-onebox">CMake 3.1 Release Notes — CMake 3.28.1 Documentation</a></p>
<p>See</p>

---

## Post #15 by @lassoan (2019-05-10 00:12 UTC)

<p>For me, release-mode build completed without errors, using VS2019 IDE, VS2015 toolset, x64, with SimpleITK enabled. I’m not sure what <a class="mention" href="/u/jamesobutler">@jamesobutler</a> did differently. I’ve started a debug-mode build now.</p>

---

## Post #16 by @jamesobutler (2019-05-10 00:49 UTC)

<p>I didn’t try a release build so hard to say if it would’ve messed up for me then. <a class="mention" href="/u/lassoan">@lassoan</a> Let me know how the debug build goes for you.</p>
<p>I did use Visual Studio 2017 and it’s generator and not Visual Studio 2019. With CMake 3.14.3 specifying X64 and v140 toolset. I think the only cmake settings I changed from default were setting it to a “stable” release type, setting the forced revision to 27931, and setting the MP flags to 4 to speed up the build process.</p>

---

## Post #17 by @jcfr (2019-05-10 06:50 UTC)

<p>To follow up:</p>
<ul>
<li>fixed in master and committed in <code>trunk</code> as <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28220" rel="nofollow noopener">r28220</a>
</li>
<li>backported in master-410 branch and committed in <code>branches/Slicer-4-10/</code> as <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28221" rel="nofollow noopener">r28221</a>
</li>
</ul>

---

## Post #18 by @lassoan (2019-05-10 12:40 UTC)

<p>Debug-mode build completed without errors, too (even without <a class="mention" href="/u/jcfr">@jcfr</a>’s fixes), using VS2019 IDE, VS2015 toolset, x64, with SimpleITK enabled.</p>

---

## Post #19 by @jamesobutler (2019-05-10 14:08 UTC)

<p>Here was my original CMakeCache.txt for completeness:</p>
<pre><code class="lang-auto"># This is the CMakeCache file.

# For build in directory: c:/S4.10D

# It was generated by CMake: C:/Program Files/CMake/bin/cmake.exe

# You can edit this file to change values found and used by cmake.

# If you do not want to change any of the values, simply exit the editor.

# If you do want to change a value, simply edit, save, and exit the editor.

# The syntax for the file is as follows:

# KEY:TYPE=VALUE

# KEY is the name of a variable in the cache.

# TYPE is a hint to GUIs for the type of VALUE, DO NOT EDIT TYPE!.

# VALUE is the current value for the KEY.

########################

# EXTERNAL cache entries

########################

//Additional CXX Flags

ADDITIONAL_CXX_FLAGS:STRING=

//Additional C Flags

ADDITIONAL_C_FLAGS:STRING=

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_CLI_ARCHIVE_OUTPUT_DIRECTORY:PATH=C:/S4.10D/Slicer-build/lib/Slicer-4.10/cli-modules

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_CLI_INSTALL_ARCHIVE_DESTINATION:PATH=./lib/Slicer-4.10/cli-modules

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_CLI_INSTALL_LIBRARY_DESTINATION:PATH=./lib/Slicer-4.10/cli-modules

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_CLI_INSTALL_RUNTIME_DESTINATION:PATH=./lib/Slicer-4.10/cli-modules

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_CLI_LIBRARY_OUTPUT_DIRECTORY:PATH=C:/S4.10D/Slicer-build/lib/Slicer-4.10/cli-modules

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_CLI_RUNTIME_OUTPUT_DIRECTORY:PATH=C:/S4.10D/Slicer-build/lib/Slicer-4.10/cli-modules

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_DISABLE_TESTING:BOOL=ON

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_ExternalData_DATA_MANAGEMENT_TARGET:STRING=SlicerData

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINSTools_SUPERBUILD:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

BRAINS_DEBUG_IMAGE_WRITE:BOOL=OFF

//Build the testing tree.

BUILD_TESTING:BOOL=OFF

//Semicolon separated list of supported configuration types, only

// supports Debug, Release, MinSizeRel, and RelWithDebInfo, anything

// else will be ignored.

CMAKE_CONFIGURATION_TYPES:STRING=Debug;Release;MinSizeRel;RelWithDebInfo

//CMake CXX Flags

CMAKE_CXX_FLAGS:STRING=/DWIN32 /D_WINDOWS /W2 /GR /EHsc

//Flags used by the CXX compiler during DEBUG builds.

CMAKE_CXX_FLAGS_DEBUG:STRING=/MDd /Zi /Ob0 /Od /RTC1

//Flags used by the CXX compiler during MINSIZEREL builds.

CMAKE_CXX_FLAGS_MINSIZEREL:STRING=/MD /O1 /Ob1 /DNDEBUG

//Flags used by the CXX compiler during RELEASE builds.

CMAKE_CXX_FLAGS_RELEASE:STRING=/MD /O2 /Ob2 /DNDEBUG

//Flags used by the CXX compiler during RELWITHDEBINFO builds.

CMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING=/MD /Zi /O2 /Ob1 /DNDEBUG

//Build with /MP flag enabled

CMAKE_CXX_MP_FLAG:BOOL=OFF

//The maximum number of processes for the /MP flag

CMAKE_CXX_MP_NUM_PROCESSORS:STRING=

//Libraries linked by default with all C++ applications.

CMAKE_CXX_STANDARD_LIBRARIES:STRING=kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib

//CMake C Flags

CMAKE_C_FLAGS:STRING=/DWIN32 /D_WINDOWS /W2

//Flags used by the C compiler during DEBUG builds.

CMAKE_C_FLAGS_DEBUG:STRING=/MDd /Zi /Ob0 /Od /RTC1

//Flags used by the C compiler during MINSIZEREL builds.

CMAKE_C_FLAGS_MINSIZEREL:STRING=/MD /O1 /Ob1 /DNDEBUG

//Flags used by the C compiler during RELEASE builds.

CMAKE_C_FLAGS_RELEASE:STRING=/MD /O2 /Ob2 /DNDEBUG

//Flags used by the C compiler during RELWITHDEBINFO builds.

CMAKE_C_FLAGS_RELWITHDEBINFO:STRING=/MD /Zi /O2 /Ob1 /DNDEBUG

//Libraries linked by default with all C applications.

CMAKE_C_STANDARD_LIBRARIES:STRING=kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib

//Flags used by the linker during all build types.

CMAKE_EXE_LINKER_FLAGS:STRING=/machine:x64

//Flags used by the linker during DEBUG builds.

CMAKE_EXE_LINKER_FLAGS_DEBUG:STRING=/debug /INCREMENTAL

//Flags used by the linker during MINSIZEREL builds.

CMAKE_EXE_LINKER_FLAGS_MINSIZEREL:STRING=/INCREMENTAL:NO

//Flags used by the linker during RELEASE builds.

CMAKE_EXE_LINKER_FLAGS_RELEASE:STRING=/INCREMENTAL:NO

//Flags used by the linker during RELWITHDEBINFO builds.

CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO:STRING=/debug /INCREMENTAL

//Install path prefix, prepended onto install directories.

CMAKE_INSTALL_PREFIX:PATH=C:/Program Files (x86)/Slicer

//Path to a program.

CMAKE_LINKER:FILEPATH=C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/link.exe

//Flags used by the linker during the creation of modules during

// all build types.

CMAKE_MODULE_LINKER_FLAGS:STRING=/machine:x64

//Flags used by the linker during the creation of modules during

// DEBUG builds.

CMAKE_MODULE_LINKER_FLAGS_DEBUG:STRING=/debug /INCREMENTAL

//Flags used by the linker during the creation of modules during

// MINSIZEREL builds.

CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL:STRING=/INCREMENTAL:NO

//Flags used by the linker during the creation of modules during

// RELEASE builds.

CMAKE_MODULE_LINKER_FLAGS_RELEASE:STRING=/INCREMENTAL:NO

//Flags used by the linker during the creation of modules during

// RELWITHDEBINFO builds.

CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO:STRING=/debug /INCREMENTAL

//Path to a program.

CMAKE_MT:FILEPATH=CMAKE_MT-NOTFOUND

//Value Computed by CMake

CMAKE_PROJECT_DESCRIPTION:STATIC=

//Value Computed by CMake

CMAKE_PROJECT_HOMEPAGE_URL:STATIC=

//Value Computed by CMake

CMAKE_PROJECT_NAME:STATIC=Slicer

//Value Computed by CMake

CMAKE_PROJECT_VERSION:STATIC=4.10.1

//Value Computed by CMake

CMAKE_PROJECT_VERSION_MAJOR:STATIC=4

//Value Computed by CMake

CMAKE_PROJECT_VERSION_MINOR:STATIC=10

//Value Computed by CMake

CMAKE_PROJECT_VERSION_PATCH:STATIC=1

//Value Computed by CMake

CMAKE_PROJECT_VERSION_TWEAK:STATIC=

//RC compiler

CMAKE_RC_COMPILER:FILEPATH=rc

//Flags for Windows Resource Compiler during all build types.

CMAKE_RC_FLAGS:STRING=/DWIN32

//Flags for Windows Resource Compiler during DEBUG builds.

CMAKE_RC_FLAGS_DEBUG:STRING=/D_DEBUG

//Flags for Windows Resource Compiler during MINSIZEREL builds.

CMAKE_RC_FLAGS_MINSIZEREL:STRING=

//Flags for Windows Resource Compiler during RELEASE builds.

CMAKE_RC_FLAGS_RELEASE:STRING=

//Flags for Windows Resource Compiler during RELWITHDEBINFO builds.

CMAKE_RC_FLAGS_RELWITHDEBINFO:STRING=

//Flags used by the linker during the creation of shared libraries

// during all build types.

CMAKE_SHARED_LINKER_FLAGS:STRING=/machine:x64

//Flags used by the linker during the creation of shared libraries

// during DEBUG builds.

CMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING=/debug /INCREMENTAL

//Flags used by the linker during the creation of shared libraries

// during MINSIZEREL builds.

CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL:STRING=/INCREMENTAL:NO

//Flags used by the linker during the creation of shared libraries

// during RELEASE builds.

CMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING=/INCREMENTAL:NO

//Flags used by the linker during the creation of shared libraries

// during RELWITHDEBINFO builds.

CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO:STRING=/debug /INCREMENTAL

//If set, runtime paths are not added when installing shared libraries,

// but are added when building.

CMAKE_SKIP_INSTALL_RPATH:BOOL=OFF

//If set, runtime paths are not added when using shared libraries.

CMAKE_SKIP_RPATH:BOOL=OFF

//Flags used by the linker during the creation of static libraries

// during all build types.

CMAKE_STATIC_LINKER_FLAGS:STRING=/machine:x64

//Flags used by the linker during the creation of static libraries

// during DEBUG builds.

CMAKE_STATIC_LINKER_FLAGS_DEBUG:STRING=

//Flags used by the linker during the creation of static libraries

// during MINSIZEREL builds.

CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL:STRING=

//Flags used by the linker during the creation of static libraries

// during RELEASE builds.

CMAKE_STATIC_LINKER_FLAGS_RELEASE:STRING=

//Flags used by the linker during the creation of static libraries

// during RELWITHDEBINFO builds.

CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO:STRING=

//If this value is on, makefiles will be generated without the

// .SILENT directive, and all commands will be echoed to the console

// during the make. This is useful for debugging only. With Visual

// Studio IDE projects all commands are done without /nologo.

CMAKE_VERBOSE_MAKEFILE:BOOL=OFF

//Dot tool for use with Doxygen

DOXYGEN_DOT_EXECUTABLE:FILEPATH=DOXYGEN_DOT_EXECUTABLE-NOTFOUND

//Doxygen documentation generation tool (http://www.doxygen.org)

DOXYGEN_EXECUTABLE:FILEPATH=DOXYGEN_EXECUTABLE-NOTFOUND

//git command line client

GIT_EXECUTABLE:FILEPATH=C:/Program Files/Git/cmd/git.exe

//Patch command line executable

Patch_EXECUTABLE:FILEPATH=C:/Program Files/Git/usr/bin/patch.exe

QT_QMAKE_EXECUTABLE:FILEPATH=NOTFOUND

//The directory containing a CMake configuration file for Qt5Core.

Qt5Core_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Core

//The directory containing a CMake configuration file for Qt5Gui.

Qt5Gui_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Gui

//The directory containing a CMake configuration file for Qt5Multimedia.

Qt5Multimedia_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Multimedia

//The directory containing a CMake configuration file for Qt5Network.

Qt5Network_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Network

//The directory containing a CMake configuration file for Qt5OpenGL.

Qt5OpenGL_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5OpenGL

//The directory containing a CMake configuration file for Qt5Positioning.

Qt5Positioning_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Positioning

//The directory containing a CMake configuration file for Qt5PrintSupport.

Qt5PrintSupport_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5PrintSupport

//The directory containing a CMake configuration file for Qt5Qml.

Qt5Qml_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Qml

//The directory containing a CMake configuration file for Qt5Quick.

Qt5Quick_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Quick

//The directory containing a CMake configuration file for Qt5Script.

Qt5Script_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Script

//The directory containing a CMake configuration file for Qt5Sql.

Qt5Sql_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Sql

//The directory containing a CMake configuration file for Qt5Svg.

Qt5Svg_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Svg

//The directory containing a CMake configuration file for Qt5UiTools.

Qt5UiTools_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5UiTools

//The directory containing a CMake configuration file for Qt5WebChannel.

Qt5WebChannel_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5WebChannel

//The directory containing a CMake configuration file for Qt5WebEngineCore.

Qt5WebEngineCore_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5WebEngineCore

//The directory containing a CMake configuration file for Qt5WebEngineWidgets.

Qt5WebEngineWidgets_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5WebEngineWidgets

//The directory containing a CMake configuration file for Qt5WebEngine.

Qt5WebEngine_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5WebEngine

//The directory containing a CMake configuration file for Qt5Widgets.

Qt5Widgets_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Widgets

//The directory containing a CMake configuration file for Qt5XmlPatterns.

Qt5XmlPatterns_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5XmlPatterns

//The directory containing a CMake configuration file for Qt5Xml.

Qt5Xml_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5Xml

//The directory containing a CMake configuration file for Qt5.

Qt5_DIR:PATH=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5

//Value Computed by CMake

Slicer_BINARY_DIR:STATIC=C:/S4.10D

//Download and integrate BRAINSTools sources.

Slicer_BUILD_BRAINSTOOLS:BOOL=ON

//Build Slicer CLI Plugins

Slicer_BUILD_CLI:BOOL=ON

//Build Slicer with CLI support

Slicer_BUILD_CLI_SUPPORT:BOOL=ON

//Download and integrate CompareVolumes sources.

Slicer_BUILD_CompareVolumes:BOOL=ON

//Build Slicer with DICOM support

Slicer_BUILD_DICOM_SUPPORT:BOOL=ON

//Build Slicer with diffusion (DWI, DTI) support

Slicer_BUILD_DIFFUSION_SUPPORT:BOOL=ON

//Build documentation (Doxygen, sphinx, ...)

Slicer_BUILD_DOCUMENTATION:BOOL=ON

//Download and integrate DataStore sources.

Slicer_BUILD_DataStore:BOOL=ON

//Build Slicer extension manager

Slicer_BUILD_EXTENSIONMANAGER_SUPPORT:BOOL=ON

//Build Slicer with Internationalization support

Slicer_BUILD_I18N_SUPPORT:BOOL=OFF

//Build Python wrapping for ITK

Slicer_BUILD_ITKPython:BOOL=OFF

//Build Slicer LEGACY_CLI Plugins

Slicer_BUILD_LEGACY_CLI:BOOL=ON

//Download and integrate LandmarkRegistration sources.

Slicer_BUILD_LandmarkRegistration:BOOL=ON

//Build MultiVolume support.

Slicer_BUILD_MULTIVOLUME_SUPPORT:BOOL=ON

//Download and integrate MultiVolumeExplorer sources.

Slicer_BUILD_MultiVolumeExplorer:BOOL=ON

//Download and integrate MultiVolumeImporter sources.

Slicer_BUILD_MultiVolumeImporter:BOOL=ON

//Build Slicer with parameter serializer support

Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT:BOOL=ON

//Build Slicer QT Loadable Modules

Slicer_BUILD_QTLOADABLEMODULES:BOOL=ON

//Build Slicer Python QT Modules

Slicer_BUILD_QTSCRIPTEDMODULES:BOOL=ON

//Build Qt designer plugins

Slicer_BUILD_QT_DESIGNER_PLUGINS:BOOL=ON

//Download and integrate SimpleFilters sources.

Slicer_BUILD_SimpleFilters:BOOL=ON

//Build Slicer executable as a console app on windows (allows debug

// output)

Slicer_BUILD_WIN32_CONSOLE:BOOL=ON

//Name of the modules shown on the toolbar by default (comma-separated

// list)

Slicer_DEFAULT_FAVORITE_MODULES:STRING=Data, Volumes, Models, Transforms, Markups, SegmentEditor

//Name of the module that Slicer activates on start-up by default

Slicer_DEFAULT_HOME_MODULE:STRING=Welcome

//Text displayed at the first startup of Slicer in a popup window

Slicer_DISCLAIMER_AT_STARTUP:STRING=Thank you for using %1!&lt;br&gt;&lt;br&gt;This software is not intended for clinical use.

//Overwrite value of auto-discovered Slicer_WC_LAST_CHANGED_DATE

// (format: YYYY-MM-DD)

Slicer_FORCED_WC_LAST_CHANGED_DATE:STRING=

//Overwrite value of auto-discovered Slicer_WC_REVISION

Slicer_FORCED_WC_REVISION:STRING=27931

//Main project name

Slicer_MAIN_PROJECT:STRING=SlicerApp

//Organization domain

Slicer_ORGANIZATION_DOMAIN:STRING=www.na-mic.org

//Organization name

Slicer_ORGANIZATION_NAME:STRING=NA-MIC

//Type of Slicer release.

Slicer_RELEASE_TYPE:STRING=Stable

//Minimum required Qt version

Slicer_REQUIRED_QT_VERSION:STRING=5.10.0

//Value Computed by CMake

Slicer_SOURCE_DIR:STATIC=C:/Slicer

//Build Slicer and the projects it depends on.

Slicer_SUPERBUILD:BOOL=ON

//Configure ctkAppLauncher.

Slicer_USE_CTKAPPLAUNCHER:BOOL=ON

//Organize build targets into folders

Slicer_USE_FOLDERS:BOOL=ON

//If behind a firewall turn this off to use https instead.

Slicer_USE_GIT_PROTOCOL:BOOL=ON

//Build Slicer with NumPy

Slicer_USE_NUMPY:BOOL=ON

//Integrate a python-QT interpreter into Slicer.

Slicer_USE_PYTHONQT:BOOL=ON

//Enable PythonQt SSL support

Slicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=OFF

//Enable PythonQt Tcl adapter layer

Slicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF

//Integrate QtTesting framework into Slicer.

Slicer_USE_QtTesting:BOOL=ON

//Build Slicer with SimpleITK support

Slicer_USE_SimpleITK:BOOL=ON

//Build SimpleITK with shared libraries. Reduces linking time,

// increases run-time load time.

Slicer_USE_SimpleITK_SHARED:BOOL=ON

//Enable VTKs Debug Leaks functionality in both VTK and Slicer.

Slicer_USE_VTK_DEBUG_LEAKS:BOOL=ON

//Rendering backend.

Slicer_VTK_RENDERING_BACKEND:STRING=OpenGL2

//Which multi-threaded parallelism implementation to use in VTK.

// Options are Sequential or TBB.

Slicer_VTK_SMP_IMPLEMENTATION_TYPE:STRING=TBB

//The VTK major version (7 or 8).

Slicer_VTK_VERSION_MAJOR:STRING=8

//Build with library version information

Slicer_WITH_LIBRARY_VERSION:BOOL=OFF

//subversion command line client

Subversion_SVN_EXECUTABLE:FILEPATH=C:/Program Files/SlikSvn/bin/svn.exe

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_ANTS:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_AutoWorkup:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSABC:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSConstellationDetector:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSContinuousClass:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSCreateLabelMapFromProbabilityMaps:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSCut:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSDemonWarp:BOOL=ON

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSFit:BOOL=ON

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSInitializedControlPoints:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSLandmarkInitializer:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSMultiModeSegment:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSMultiSTAPLE:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSMush:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSPosteriorToContinuousClass:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSROIAuto:BOOL=ON

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSRefacer:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSResample:BOOL=ON

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSSnapShotWriter:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSSurfaceTools:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSTalairach:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_BRAINSTransformConvert:BOOL=ON

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_ConvertBetweenFileFormats:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_DWIConvert:BOOL=ON

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_DebugImageViewer:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_GTRACT:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_ICCDEF:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_ImageCalculator:BOOL=OFF

//Variable set by 'ExternalProject_Add_Source' based on VARS parameter.

USE_ReferenceAtlas:BOOL=OFF

//Enable/Disable coverage

WITH_COVERAGE:BOOL=OFF

########################

# INTERNAL cache entries

########################

//ADVANCED property for variable: ADDITIONAL_CXX_FLAGS

ADDITIONAL_CXX_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: ADDITIONAL_C_FLAGS

ADDITIONAL_C_FLAGS-ADVANCED:INTERNAL=1

//This is the directory where this CMakeCache.txt was created

CMAKE_CACHEFILE_DIR:INTERNAL=c:/S4.10D

//Major version of cmake used to create the current loaded cache

CMAKE_CACHE_MAJOR_VERSION:INTERNAL=3

//Minor version of cmake used to create the current loaded cache

CMAKE_CACHE_MINOR_VERSION:INTERNAL=14

//Patch version of cmake used to create the current loaded cache

CMAKE_CACHE_PATCH_VERSION:INTERNAL=3

//Path to CMake executable.

CMAKE_COMMAND:INTERNAL=C:/Program Files/CMake/bin/cmake.exe

//Path to cpack program executable.

CMAKE_CPACK_COMMAND:INTERNAL=C:/Program Files/CMake/bin/cpack.exe

//Path to ctest program executable.

CMAKE_CTEST_COMMAND:INTERNAL=C:/Program Files/CMake/bin/ctest.exe

//ADVANCED property for variable: CMAKE_CXX_FLAGS

CMAKE_CXX_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_CXX_FLAGS_DEBUG

CMAKE_CXX_FLAGS_DEBUG-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_CXX_FLAGS_MINSIZEREL

CMAKE_CXX_FLAGS_MINSIZEREL-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_CXX_FLAGS_RELEASE

CMAKE_CXX_FLAGS_RELEASE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_CXX_FLAGS_RELWITHDEBINFO

CMAKE_CXX_FLAGS_RELWITHDEBINFO-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_CXX_STANDARD_LIBRARIES

CMAKE_CXX_STANDARD_LIBRARIES-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_C_FLAGS

CMAKE_C_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_C_FLAGS_DEBUG

CMAKE_C_FLAGS_DEBUG-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_C_FLAGS_MINSIZEREL

CMAKE_C_FLAGS_MINSIZEREL-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_C_FLAGS_RELEASE

CMAKE_C_FLAGS_RELEASE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_C_FLAGS_RELWITHDEBINFO

CMAKE_C_FLAGS_RELWITHDEBINFO-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_C_STANDARD_LIBRARIES

CMAKE_C_STANDARD_LIBRARIES-ADVANCED:INTERNAL=1

//Executable file format

CMAKE_EXECUTABLE_FORMAT:INTERNAL=Unknown

//ADVANCED property for variable: CMAKE_EXE_LINKER_FLAGS

CMAKE_EXE_LINKER_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_EXE_LINKER_FLAGS_DEBUG

CMAKE_EXE_LINKER_FLAGS_DEBUG-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_EXE_LINKER_FLAGS_MINSIZEREL

CMAKE_EXE_LINKER_FLAGS_MINSIZEREL-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_EXE_LINKER_FLAGS_RELEASE

CMAKE_EXE_LINKER_FLAGS_RELEASE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO

CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO-ADVANCED:INTERNAL=1

//Name of external makefile project generator.

CMAKE_EXTRA_GENERATOR:INTERNAL=

//Name of generator.

CMAKE_GENERATOR:INTERNAL=Visual Studio 15 2017

//Generator instance identifier.

CMAKE_GENERATOR_INSTANCE:INTERNAL=C:/Program Files (x86)/Microsoft Visual Studio/2017/Community

//Name of generator platform.

CMAKE_GENERATOR_PLATFORM:INTERNAL=x64

//Name of generator toolset.

CMAKE_GENERATOR_TOOLSET:INTERNAL=v140

//Source directory with the top level CMakeLists.txt file for this

// project

CMAKE_HOME_DIRECTORY:INTERNAL=C:/Slicer

//ADVANCED property for variable: CMAKE_LINKER

CMAKE_LINKER-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_MODULE_LINKER_FLAGS

CMAKE_MODULE_LINKER_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_MODULE_LINKER_FLAGS_DEBUG

CMAKE_MODULE_LINKER_FLAGS_DEBUG-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL

CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_MODULE_LINKER_FLAGS_RELEASE

CMAKE_MODULE_LINKER_FLAGS_RELEASE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO

CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_MT

CMAKE_MT-ADVANCED:INTERNAL=1

//number of local generators

CMAKE_NUMBER_OF_MAKEFILES:INTERNAL=1

//Platform information initialized

CMAKE_PLATFORM_INFO_INITIALIZED:INTERNAL=1

//ADVANCED property for variable: CMAKE_RC_COMPILER

CMAKE_RC_COMPILER-ADVANCED:INTERNAL=1

CMAKE_RC_COMPILER_WORKS:INTERNAL=1

//ADVANCED property for variable: CMAKE_RC_FLAGS

CMAKE_RC_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_RC_FLAGS_DEBUG

CMAKE_RC_FLAGS_DEBUG-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_RC_FLAGS_MINSIZEREL

CMAKE_RC_FLAGS_MINSIZEREL-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_RC_FLAGS_RELEASE

CMAKE_RC_FLAGS_RELEASE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_RC_FLAGS_RELWITHDEBINFO

CMAKE_RC_FLAGS_RELWITHDEBINFO-ADVANCED:INTERNAL=1

//Path to CMake installation.

CMAKE_ROOT:INTERNAL=C:/Program Files/CMake/share/cmake-3.14

//ADVANCED property for variable: CMAKE_SHARED_LINKER_FLAGS

CMAKE_SHARED_LINKER_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_SHARED_LINKER_FLAGS_DEBUG

CMAKE_SHARED_LINKER_FLAGS_DEBUG-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL

CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_SHARED_LINKER_FLAGS_RELEASE

CMAKE_SHARED_LINKER_FLAGS_RELEASE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO

CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO-ADVANCED:INTERNAL=1

//CHECK_TYPE_SIZE: sizeof(unsigned short)

CMAKE_SIZEOF_UNSIGNED_SHORT:INTERNAL=2

//ADVANCED property for variable: CMAKE_SKIP_INSTALL_RPATH

CMAKE_SKIP_INSTALL_RPATH-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_SKIP_RPATH

CMAKE_SKIP_RPATH-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_STATIC_LINKER_FLAGS

CMAKE_STATIC_LINKER_FLAGS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_STATIC_LINKER_FLAGS_DEBUG

CMAKE_STATIC_LINKER_FLAGS_DEBUG-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL

CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_STATIC_LINKER_FLAGS_RELEASE

CMAKE_STATIC_LINKER_FLAGS_RELEASE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO

CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO-ADVANCED:INTERNAL=1

//ADVANCED property for variable: CMAKE_VERBOSE_MAKEFILE

CMAKE_VERBOSE_MAKEFILE-ADVANCED:INTERNAL=1

//Result of TEST_BIG_ENDIAN

CMAKE_WORDS_BIGENDIAN:INTERNAL=0

//ADVANCED property for variable: DOXYGEN_DOT_EXECUTABLE

DOXYGEN_DOT_EXECUTABLE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: DOXYGEN_EXECUTABLE

DOXYGEN_EXECUTABLE-ADVANCED:INTERNAL=1

//Details about finding Git

FIND_PACKAGE_MESSAGE_DETAILS_Git:INTERNAL=[C:/Program Files/Git/cmd/git.exe][v()]

//Details about finding Patch

FIND_PACKAGE_MESSAGE_DETAILS_Patch:INTERNAL=[C:/Program Files/Git/usr/bin/patch.exe][v()]

//Details about finding Subversion

FIND_PACKAGE_MESSAGE_DETAILS_Subversion:INTERNAL=[C:/Program Files/SlikSvn/bin/svn.exe][v1.9.7()]

//ADVANCED property for variable: GIT_EXECUTABLE

GIT_EXECUTABLE-ADVANCED:INTERNAL=1

//Result of TRY_COMPILE

HAVE_CMAKE_SIZEOF_UNSIGNED_SHORT:INTERNAL=TRUE

//Result of TRY_COMPILE

HAVE_CMAKE_WORDS_BIGENDIAN:INTERNAL=TRUE

//Have include stddef.h

HAVE_STDDEF_H:INTERNAL=1

//Have include stdint.h

HAVE_STDINT_H:INTERNAL=1

//Have include sys/types.h

HAVE_SYS_TYPES_H:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_BRAINSTOOLS

Slicer_BUILD_BRAINSTOOLS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_CompareVolumes

Slicer_BUILD_CompareVolumes-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_DOCUMENTATION

Slicer_BUILD_DOCUMENTATION-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_DataStore

Slicer_BUILD_DataStore-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_LandmarkRegistration

Slicer_BUILD_LandmarkRegistration-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_MULTIVOLUME_SUPPORT

Slicer_BUILD_MULTIVOLUME_SUPPORT-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_MultiVolumeExplorer

Slicer_BUILD_MultiVolumeExplorer-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_MultiVolumeImporter

Slicer_BUILD_MultiVolumeImporter-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_QTLOADABLEMODULES

Slicer_BUILD_QTLOADABLEMODULES-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_QTSCRIPTEDMODULES

Slicer_BUILD_QTSCRIPTEDMODULES-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_BUILD_SimpleFilters

Slicer_BUILD_SimpleFilters-ADVANCED:INTERNAL=1

//CMake supports HTTPS protocol

Slicer_CMake_HTTPS_Supported:INTERNAL=TRUE

//ADVANCED property for variable: Slicer_DEFAULT_FAVORITE_MODULES

Slicer_DEFAULT_FAVORITE_MODULES-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_DEFAULT_HOME_MODULE

Slicer_DEFAULT_HOME_MODULE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_DISCLAIMER_AT_STARTUP

Slicer_DISCLAIMER_AT_STARTUP-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_FORCED_WC_LAST_CHANGED_DATE

Slicer_FORCED_WC_LAST_CHANGED_DATE-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_FORCED_WC_REVISION

Slicer_FORCED_WC_REVISION-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_ORGANIZATION_DOMAIN

Slicer_ORGANIZATION_DOMAIN-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_ORGANIZATION_NAME

Slicer_ORGANIZATION_NAME-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_RELEASE_TYPE

Slicer_RELEASE_TYPE-ADVANCED:INTERNAL=1

//STRINGS property for variable: Slicer_RELEASE_TYPE

Slicer_RELEASE_TYPE-STRINGS:INTERNAL=Experimental;Preview;Stable

//ADVANCED property for variable: Slicer_SUPERBUILD

Slicer_SUPERBUILD-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_USE_CTKAPPLAUNCHER

Slicer_USE_CTKAPPLAUNCHER-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_USE_FOLDERS

Slicer_USE_FOLDERS-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Slicer_USE_QtTesting

Slicer_USE_QtTesting-ADVANCED:INTERNAL=1

//STRINGS property for variable: Slicer_VTK_SMP_IMPLEMENTATION_TYPE

Slicer_VTK_SMP_IMPLEMENTATION_TYPE-STRINGS:INTERNAL=Sequential;TBB

//STRINGS property for variable: Slicer_VTK_VERSION_MAJOR

Slicer_VTK_VERSION_MAJOR-STRINGS:INTERNAL=7;8

//ADVANCED property for variable: Slicer_WITH_LIBRARY_VERSION

Slicer_WITH_LIBRARY_VERSION-ADVANCED:INTERNAL=1

//ADVANCED property for variable: Subversion_SVN_EXECUTABLE

Subversion_SVN_EXECUTABLE-ADVANCED:INTERNAL=1
</code></pre>

---

## Post #20 by @jamesobutler (2019-05-10 14:12 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I see the commit in the github master, but I don’t see the backported commit in the github master-410 branch. Maybe it was only done in the SVN master-410 branch?</p>

---

## Post #21 by @jcfr (2019-05-10 14:55 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="20" data-topic="6727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>but I don’t see the backported commit in the github master-410 branch. Maybe it was only done in the SVN master-410 branch?</p>
</blockquote>
</aside>
<p>Good catch. The sync of svn maintenance branch with GitHub is not automated. Should be good now.</p>

---

## Post #22 by @jcfr (2019-05-10 15:11 UTC)

<p>For reference, I also just updated the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Backport_commit_into_release_branch" rel="nofollow noopener">ReleaseProcess#Backport_commit_into_release_branch</a> guide</p>

---

## Post #23 by @jamesobutler (2019-05-10 18:09 UTC)

<p>I deleted the SimpleITK folders from my C:/S4D directory, fetched the latest from Slicer master-410 branch, configured the cmake project again in Cmake GUI and built again.  SimpleITK began building correctly and the project has now officially built successfully. <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=12" title=":tada:" class="emoji" alt=":tada:" loading="lazy" width="20" height="20"></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a href="https://github.com/Slicer/Slicer/commit/ebce522e0cb99a5e312800c6f01bc49e237942da" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/commit/ebce522e0cb99a5e312800c6f01bc49e237942da</a> Works well in the master-410 branch. I did notice that the comment for the tag line is incorrect.  Technically</p>
<pre><code class="lang-auto">"e52c9ab047b514ef9584fef475e0ed416ad8fa4a" # slicer-v1.2.0-2019-02-27-dc5c1a1 (based of v1.1.0 tag)
</code></pre>
<p>should be</p>
<pre><code class="lang-auto">"e52c9ab047b514ef9584fef475e0ed416ad8fa4a" # slicer-v1.1.0-2018-03-21-dbc8dfe (based of v1.1.0 tag)
</code></pre>
<p>but not a big deal.</p>

---

## Post #24 by @jcfr (2019-05-10 18:23 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="23" data-topic="6727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>SimpleITK began building correctly and the project has now officially built successfully</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="jamesobutler" data-post="23" data-topic="6727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>well in the master-410 branch. I did notice that the comment for the tag line is incorrect.</p>
</blockquote>
</aside>
<p>Thanks for reporting. This is now fixed.</p>

---

## Post #25 by @Saima (2019-07-19 04:38 UTC)

<p>Hi James,<br>
I am building slicer in release mode.</p>
<p>Specifications:<br>
Slicer 4.10 which I downloaded thorugh<br>
svn co <a href="http://svn.slicer.org/Slicer4/branches/Slicer-4-10" rel="noopener nofollow ugc">http://svn.slicer.org/Slicer4/branches/Slicer-4-10</a> Slicer-r28257 -r 28257<br>
cmake 3.14.6 msvc 2017<br>
VS 2017 community edition</p>
<p>cmake configuration:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdfc09f1c947a14ae1bf1d18b498228ae0f2cf99.png" data-download-href="/uploads/short-url/r6GeqjiaPrqCyKtOWPzbmiZQZId.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfc09f1c947a14ae1bf1d18b498228ae0f2cf99_2_517x368.png" alt="image" data-base62-sha1="r6GeqjiaPrqCyKtOWPzbmiZQZId" width="517" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfc09f1c947a14ae1bf1d18b498228ae0f2cf99_2_517x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfc09f1c947a14ae1bf1d18b498228ae0f2cf99_2_775x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdfc09f1c947a14ae1bf1d18b498228ae0f2cf99.png 2x" data-dominant-color="F7F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1002×714 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2abbb7818e39ab73aa6ee6609559abc37b570cf4.png" data-download-href="/uploads/short-url/662eA4SEDaCzAWoKyqchANrFZtO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2abbb7818e39ab73aa6ee6609559abc37b570cf4_2_345x194.png" alt="image" data-base62-sha1="662eA4SEDaCzAWoKyqchANrFZtO" width="345" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2abbb7818e39ab73aa6ee6609559abc37b570cf4_2_345x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2abbb7818e39ab73aa6ee6609559abc37b570cf4_2_517x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2abbb7818e39ab73aa6ee6609559abc37b570cf4_2_690x388.png 2x" data-dominant-color="EDEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">804×454 7.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Qt 5.11.0 with msvc 2017 x64 with qtwebengine and qt script</p>
<p>Then I run the slicer.sln in release mode with x64 selected in the active solution platform of vs 2017<br>
build failed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e6ce14381b7ced6d24a301337cb5c58575fda17.jpeg" data-download-href="/uploads/short-url/i2pqZVkNaYCCoE9mxVquwoRJzDN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e6ce14381b7ced6d24a301337cb5c58575fda17_2_345x187.jpeg" alt="image" data-base62-sha1="i2pqZVkNaYCCoE9mxVquwoRJzDN" width="345" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e6ce14381b7ced6d24a301337cb5c58575fda17_2_345x187.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e6ce14381b7ced6d24a301337cb5c58575fda17_2_517x280.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e6ce14381b7ced6d24a301337cb5c58575fda17_2_690x374.jpeg 2x" data-dominant-color="C3C9CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1044 493 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Error list<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c12e7f1fe114d161ed68fdc04a4c5f68009acaf.jpeg" data-download-href="/uploads/short-url/1IOeBNUy2dlTgdOMushqWYZ7ZSf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c12e7f1fe114d161ed68fdc04a4c5f68009acaf_2_345x187.jpeg" alt="image" data-base62-sha1="1IOeBNUy2dlTgdOMushqWYZ7ZSf" width="345" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c12e7f1fe114d161ed68fdc04a4c5f68009acaf_2_345x187.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c12e7f1fe114d161ed68fdc04a4c5f68009acaf_2_517x280.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c12e7f1fe114d161ed68fdc04a4c5f68009acaf_2_690x374.jpeg 2x" data-dominant-color="CBD3DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1044 482 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6348861dc06fc5669381276fe52453db346f054.jpeg" data-download-href="/uploads/short-url/shp5A5bGxzXcEvsvw6Op0uRiV80.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6348861dc06fc5669381276fe52453db346f054_2_345x187.jpeg" alt="image" data-base62-sha1="shp5A5bGxzXcEvsvw6Op0uRiV80" width="345" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6348861dc06fc5669381276fe52453db346f054_2_345x187.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6348861dc06fc5669381276fe52453db346f054_2_517x280.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6348861dc06fc5669381276fe52453db346f054_2_690x374.jpeg 2x" data-dominant-color="D0D5DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1044 484 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Need help to build the slicer what am I doing wrong. can t understand.<br>
cmake configurations<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d0df50cc67a31a08aac4e9afa1731d97e656d73.png" data-download-href="/uploads/short-url/hQhAowzoR8Kw3Ljoe0BiYpNHdM7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d0df50cc67a31a08aac4e9afa1731d97e656d73_2_517x278.png" alt="image" data-base62-sha1="hQhAowzoR8Kw3Ljoe0BiYpNHdM7" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d0df50cc67a31a08aac4e9afa1731d97e656d73_2_517x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d0df50cc67a31a08aac4e9afa1731d97e656d73_2_775x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d0df50cc67a31a08aac4e9afa1731d97e656d73_2_1034x556.png 2x" data-dominant-color="EBEBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 60 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb3f227c6420a5120e61e37c2c6eac11a546369.png" data-download-href="/uploads/short-url/AlcOd3xaePx11JbswAambbsl5fX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feb3f227c6420a5120e61e37c2c6eac11a546369_2_517x278.png" alt="image" data-base62-sha1="AlcOd3xaePx11JbswAambbsl5fX" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feb3f227c6420a5120e61e37c2c6eac11a546369_2_517x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feb3f227c6420a5120e61e37c2c6eac11a546369_2_775x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feb3f227c6420a5120e61e37c2c6eac11a546369_2_1034x556.png 2x" data-dominant-color="E8EAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 59.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7a0a999cd228c626e0b684d2f3eca7cf7c9b43f.png" data-download-href="/uploads/short-url/nUTXewgc07BW2g3cnSS7TcX3FCf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7a0a999cd228c626e0b684d2f3eca7cf7c9b43f_2_517x278.png" alt="image" data-base62-sha1="nUTXewgc07BW2g3cnSS7TcX3FCf" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7a0a999cd228c626e0b684d2f3eca7cf7c9b43f_2_517x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7a0a999cd228c626e0b684d2f3eca7cf7c9b43f_2_775x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7a0a999cd228c626e0b684d2f3eca7cf7c9b43f_2_1034x556.png 2x" data-dominant-color="E9EBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3f073d4c9fb2b6be05516b8effbdd9c1a96dfb3.png" data-download-href="/uploads/short-url/yNZbVoARyJ3g1TPBn1bS51jujBh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3f073d4c9fb2b6be05516b8effbdd9c1a96dfb3_2_517x278.png" alt="image" data-base62-sha1="yNZbVoARyJ3g1TPBn1bS51jujBh" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3f073d4c9fb2b6be05516b8effbdd9c1a96dfb3_2_517x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3f073d4c9fb2b6be05516b8effbdd9c1a96dfb3_2_775x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3f073d4c9fb2b6be05516b8effbdd9c1a96dfb3_2_1034x556.png 2x" data-dominant-color="F29698"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 57.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bca38fc5febfa142911ee9ae385fbb14bb22877e.png" data-download-href="/uploads/short-url/qUMc09uxkuEmnsKRQI3HcDCryZ8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca38fc5febfa142911ee9ae385fbb14bb22877e_2_517x278.png" alt="image" data-base62-sha1="qUMc09uxkuEmnsKRQI3HcDCryZ8" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca38fc5febfa142911ee9ae385fbb14bb22877e_2_517x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca38fc5febfa142911ee9ae385fbb14bb22877e_2_775x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca38fc5febfa142911ee9ae385fbb14bb22877e_2_1034x556.png 2x" data-dominant-color="F79595"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 54.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4042d4be740969ba40075899fb1feefcc42bca86.png" data-download-href="/uploads/short-url/9atK3PBXdml1uYRBKZL1bApJfuu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4042d4be740969ba40075899fb1feefcc42bca86_2_517x278.png" alt="image" data-base62-sha1="9atK3PBXdml1uYRBKZL1bApJfuu" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4042d4be740969ba40075899fb1feefcc42bca86_2_517x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4042d4be740969ba40075899fb1feefcc42bca86_2_775x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4042d4be740969ba40075899fb1feefcc42bca86_2_1034x556.png 2x" data-dominant-color="F79595"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 48.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6d74909f252acfd41def506ad7d89f8f4212440.png" data-download-href="/uploads/short-url/wW741hcQaLH7nBXZPEKy3OLZ172.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d74909f252acfd41def506ad7d89f8f4212440_2_517x278.png" alt="image" data-base62-sha1="wW741hcQaLH7nBXZPEKy3OLZ172" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d74909f252acfd41def506ad7d89f8f4212440_2_517x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d74909f252acfd41def506ad7d89f8f4212440_2_775x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d74909f252acfd41def506ad7d89f8f4212440_2_1034x556.png 2x" data-dominant-color="F79999"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 46.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #26 by @jamesobutler (2019-07-19 10:52 UTC)

<p><a class="mention" href="/u/saima">@Saima</a> Please read and follow the build instructions carefully (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Common_Prerequisites_2" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Common_Prerequisites_2</a>).</p>
<p>You have to use Qt 5.10.X or earlier, such as 5.9 series, when building Slicer on Windows. You mixed Qt Webengine for MSVC 2017 with MSVC 2015 which is what you specified when you set “v140” as the toolset. That refers to building as MSVC 2015 even though you might be using the Visual Studio 2017 IDE.</p>

---

## Post #27 by @Saima (2019-07-24 05:22 UTC)

<p>Hi Andras,<br>
Which slicer patch should be used for building I am using:</p>
<p>I downloaded the slicer using the following on git cmd:</p>
<p>svn co <a href="http://svn.slicer.org/Slicer4/branches/Slicer-4-10" rel="noopener nofollow ugc">http://svn.slicer.org/Slicer4/branches/Slicer-4-10</a> Slicer-r28257 -r 28257</p>
<p>cmake 3.15 with visual studio 15  2017 and v140 and x64</p>
<p>qt 5.10.0 with msvc 2015 x64</p>
<p>I am runing into lot of build errors.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01fc2e451133f06fb4f709b76d0cfd12fd439d48.png" data-download-href="/uploads/short-url/hyLSoWy9GMQJ14nagSooF7Bcgg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01fc2e451133f06fb4f709b76d0cfd12fd439d48_2_690x375.png" alt="image" data-base62-sha1="hyLSoWy9GMQJ14nagSooF7Bcgg" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01fc2e451133f06fb4f709b76d0cfd12fd439d48_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01fc2e451133f06fb4f709b76d0cfd12fd439d48_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01fc2e451133f06fb4f709b76d0cfd12fd439d48_2_1380x750.png 2x" data-dominant-color="CDD4DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1045 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18db28883a143fd8609cda3a9ab78eb29d93e189.png" data-download-href="/uploads/short-url/3xT0eMehaJqH6T3PLyue3LJNZe9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18db28883a143fd8609cda3a9ab78eb29d93e189_2_690x375.png" alt="image" data-base62-sha1="3xT0eMehaJqH6T3PLyue3LJNZe9" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18db28883a143fd8609cda3a9ab78eb29d93e189_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18db28883a143fd8609cda3a9ab78eb29d93e189_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18db28883a143fd8609cda3a9ab78eb29d93e189_2_1380x750.png 2x" data-dominant-color="B2C6D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1045 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What am I missing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/030c751f75e0f7b55fe819122719350ddc78a1e7.png" data-download-href="/uploads/short-url/qY7AUEW02l0cNGHgN279mBWh0z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/030c751f75e0f7b55fe819122719350ddc78a1e7.png" alt="image" data-base62-sha1="qY7AUEW02l0cNGHgN279mBWh0z" width="512" height="500" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1060×1034 53.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please help me in building the slicer. I am following all the things dont know what I am missing.</p>
<p>visual studio:<br>
Environment variable VTK_ROOT is set to:<br>
46&gt;<br>
46&gt;    C:\Users\22374464\Slicer 4.8.1\lib\Slicer-4.8\python2.7\site-packages\vtk<br>
46&gt;<br>
46&gt;  For compatibility, CMake is ignoring the variable.<br>
46&gt;This warning is for project developers.  Use -Wno-dev to suppress it.<br>
46&gt;<br>
46&gt;CMake Error at CMakeLists.txt:844 (find_package):<br>
46&gt;  Could not find a configuration file for package “VTK” that is compatible<br>
46&gt;  with requested version “8”.<br>
46&gt;<br>
46&gt;  The following configuration files were considered but not accepted:<br>
46&gt;<br>
46&gt;    C:/D/S4D/VTK-build/VTKConfig.cmake, version: 8.2.0 (32bit)<br>
46&gt;<br>
46&gt;<br>
46&gt;<br>
46&gt;-- Configuring incomplete, errors occurred!<br>
46&gt;See also “C:/D/S4D/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
46&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: “cmd.exe” exited with code 1.<br>
46&gt;Done building project “Slicer.vcxproj” – FAILED.<br>
47&gt;------ Build started: Project: ALL_BUILD, Configuration: Debug x64 ------<br>
47&gt;Building Custom Rule C:/D/S4/CMakeLists.txt<br>
========== Build: 28 succeeded, 19 failed, 0 up-to-date, 0 skipped ==========</p>

---

## Post #28 by @lassoan (2019-07-24 20:24 UTC)

<p>Please try to build the latest trunk version of Slicer in source folder C:\D\S4, binary folder C:\D\S4D by specifying all parameters via command-line arguments (as described in “Alternative option” section <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows_2" rel="nofollow noopener">here</a>).</p>

---

## Post #29 by @Saima (2019-07-25 05:39 UTC)

<p>how to get the latest trunk version of slicer. Please help.</p>

---

## Post #30 by @lassoan (2019-07-25 19:16 UTC)

<p>If you checkout the repository using either SVN or git, you will get the latest version of the main branch by default. You need this version. The main branch is called “trunk” according to SVN terminology and “master” according to git terminology.</p>

---

## Post #31 by @Saima (2019-07-28 11:16 UTC)

<p>Hi Andras,<br>
I used the latest trunk version of slicer. downloaded as:<br>
svn co <a href="http://svn.slicer.org/Slicer4/trunk" class="inline-onebox" rel="noopener nofollow ugc">GitHub - NA-MIC/svn.slicer.org-Slicer4: Archive of source code originally available at svn.slicer.org/Slicer4</a><br>
I am getting no errors this time but getting alot of warnings.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a5301144c2329932836855c6585f5776b7c8472.png" data-download-href="/uploads/short-url/jJFJ3blyAYohH9Ic8RDt9WafkD8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a5301144c2329932836855c6585f5776b7c8472_2_690x375.png" alt="image" data-base62-sha1="jJFJ3blyAYohH9Ic8RDt9WafkD8" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a5301144c2329932836855c6585f5776b7c8472_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a5301144c2329932836855c6585f5776b7c8472_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a5301144c2329932836855c6585f5776b7c8472_2_1380x750.png 2x" data-dominant-color="CFD4D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1045 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is this because I didnt run it using the command prompt.</p>

---

## Post #32 by @Saima (2019-07-29 02:54 UTC)

<p>Successfully build with release mode</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7e84d6b1776c310f9b1ff88629a0e91c24a2402.png" data-download-href="/uploads/short-url/uO0mqFlYt8h6QnenPCto5asLVV8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7e84d6b1776c310f9b1ff88629a0e91c24a2402_2_431x500.png" alt="image" data-base62-sha1="uO0mqFlYt8h6QnenPCto5asLVV8" width="431" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7e84d6b1776c310f9b1ff88629a0e91c24a2402_2_431x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7e84d6b1776c310f9b1ff88629a0e91c24a2402_2_646x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7e84d6b1776c310f9b1ff88629a0e91c24a2402.png 2x" data-dominant-color="1D1D1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">661×766 6.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but dont know what the warnings are about. Could you please tell me why I am getting warnings.</p>
<p>Thank you</p>

---

## Post #33 by @lassoan (2019-07-29 03:10 UTC)

<p>In a software application that is built from many libraries in several different build environments, it is usually not practically feasible to eliminate build warnings (especially when they are in external libraries). You can ignore the warnings.</p>

---

## Post #34 by @Saima (2019-07-29 03:15 UTC)

<p>how to build in debug mode. Should I just change the mode in the visual studio to debug and then do build_all</p>

---

## Post #35 by @lassoan (2019-07-29 03:19 UTC)

<p>You can use the same source code folder (C:\D\S4) but you need to create a completely separate build tree for debug-mode and release-mode builds.</p>

---
