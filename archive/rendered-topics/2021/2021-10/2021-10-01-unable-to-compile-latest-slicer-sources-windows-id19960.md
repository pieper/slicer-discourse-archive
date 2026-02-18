# Unable to compile latest Slicer sources (Windows)

**Topic ID**: 19960
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/unable-to-compile-latest-slicer-sources-windows/19960

---

## Post #1 by @rbumm (2021-10-01 20:58 UTC)

<p>I was asked today to do a test with the very latest latest preview sources.<br>
Thought this would be a good exercise because I thought had it all set up, simply not used for several weeks.</p>
<p>What I did:</p>
<ul>
<li>Within Github I fetched the latest Slicer changes to my personal Slicer fork.</li>
<li>Made sure that I use the master branch.</li>
<li>Pulled from the master fork to my development system.</li>
<li>Performed a full cmake</li>
</ul>
<pre><code class="lang-auto">mkdir D:\D\S4R
cd /d D:\D\S4R
"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 16 2019" -A x64 -DQt5_DIR:PATH=D:\Qt\5.15.1\msvc2019_64\lib\cmake\Qt5 D:\D\S4
"C:\Program Files\CMake\bin\cmake.exe" --build . --config Release
echo %time%
pause

</code></pre>
<ul>
<li>Opend Visual Studio and loaded slicer.sln from d:\D\S4R</li>
<li>Build “ALL_BUILD” with Visualstudio 2019 (worked beforew)</li>
</ul>
<p>and received two errors:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Severity</th>
<th>Code</th>
<th>Description</th>
<th>Project</th>
<th>File</th>
<th>Line</th>
<th>Suppression State</th>
</tr>
</thead>
<tbody>
<tr>
<td>Error</td>
<td>C2666</td>
<td>‘operator ==’: 5 overloads have similar conversions</td>
<td>vtkSlicerMarkupsModuleLogic</td>
<td>D:\D\S4\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.cxx</td>
<td>264</td>
<td></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th>Severity</th>
<th>Code</th>
<th>Description</th>
<th>Project</th>
<th>File</th>
<th>Line</th>
<th>Suppression State</th>
</tr>
</thead>
<tbody>
<tr>
<td>Error (active)</td>
<td>E0350</td>
<td>more than one operator == matches these operands:</td>
<td>vtkSlicerMarkupsModuleLogic</td>
<td>D:\D\S4\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.cxx</td>
<td>264</td>
<td></td>
</tr>
</tbody>
</table>
</div><p>What have I done wrong ?<br>
In general: Is cmake necessary after every pull from the Slicer fork ?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-10-02 15:56 UTC)

<p>You can see on the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">dashboard</a> if there are any build errors using the official build configuration.</p>
<p>If there are no build errors there but Slicer fails to build on your computer then it is most likely due to using slightly different build tools or options. You can find the exact compiler version, Qt version, etc. on the dashboard (see <a href="https://slicer.cdash.org/build/2420650/notes">build notes</a> and in the beginning of the build logs).</p>
<p>The “more than one operator == matches these operands” usually means that you need to make a comparison more explicit by casting one or both operands to a more specific type (for example, use <code>ActiveMarkupsNode-&gt;GetPointer()</code> instead of just <code>ActiveMarkupsNode</code>). We had a similar build error a couple of weeks ago and a the same <a href="https://github.com/Slicer/Slicer/commit/149d8876af1246caa7b884b66a45b9ce683ede9d">fix</a> (adding <code>GetPointer()</code>) should work for you. We don’t understand yet why this syntax is needed for certain compilers in certain parts of the code (most places this is not necessary). but the change is harmless enough so if it works for you then please submit a pull request to apply it to the Slicer core, too.</p>
<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="19960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>In general: Is cmake necessary after every pull from the Slicer fork ?</p>
</blockquote>
</aside>
<p>A full build is only needed if one of the dependencies (VTK, CTK, ITK, …) are updated, which is quite rare. You can usually just build <code>&lt;Slicer-top-level-build-folder&gt;/Slicer-build/Slicer.sln</code> in Visual Studio (see details <a href="https://github.com/Slicer/Slicer/blob/master/Docs/developer_guide/debugging/windowscpp.md#debugging-using-visual-studio">here</a>).</p>

---

## Post #3 by @rbumm (2021-10-03 08:43 UTC)

<p>I tried  a complete rebuild from scratch deleting all local files and cloned into “S4” from my personal Slicer fork (master) (fetched all recent changes from <a href="https://github.com/Slicer/Slicer" class="inline-onebox">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a> before)<br>
Then again cmake config release.<br>
After several hours, it finished without error and  I saw that the location of slicer.sln had been changed to the root of “S4R”<br>
I opened that with visual studio 19 and “BUILD ALL”.<br>
After another several hours, Slicer got built better, but at least two errors occurred -  “SimpleITK” still refuses to build today.</p>
<p>At least I can now confirm that Lung CT Segmenter works with correct slice switches in the recent preview 4.13.</p>
<p>Are build errors normal and to be expected in the preview ?</p>

---

## Post #4 by @rbumm (2021-10-03 14:40 UTC)

<p>In the end it turned out, that a complete build of 4.13.0-2021-10-01 r30278 free of errors required a local Python install including setting the Python “Path” variable on Windows 10.</p>
<p>SimpleITK would not build without that install in VS2019 and fail with an error message pointing in that direction.</p>
<p>My Slicer build prerequisites are<br>
(Windows 10)</p>
<p>CMake &gt;= 3.15.1<br>
Git &gt;= 1.7.10<br>
NSIS (optional)<br>
Qt5<br>
Visual Studio<br>
Python &gt;= 3.9</p>

---

## Post #5 by @lassoan (2021-10-03 18:33 UTC)

<p>You did not mention that you switched to the correct build mode in Visual Studio. Your first failures might have been due to building in Visual Studio in default Debug mode, while using CMake to built in Release mode.</p>
<p>There are two Slicer.sln files in your build tree. One in the top-level build, one in n the inner build. The former builds all dependencies, the latter only builds Slicer application.</p>
<p>You do not need any other Python other than what Slicer builds for itself and any additional local Python installs known to interfere with the build process (SimpleITK and other SuperBuild-type extensions fail the build). The simplest workaround is to temporarily rename other Python installations. See more information here: <a href="https://github.com/Slicer/Slicer/issues/5498" class="inline-onebox">Slicer build error with VTK9 in debug mode due to SimpleITK Python configuration problem · Issue #5498 · Slicer/Slicer · GitHub</a></p>

---

## Post #6 by @rbumm (2021-10-03 19:47 UTC)

<p>So I uninstalled Python 3.9 and tried to build SimpleITK again in VS2019 either in Debug and Release mode.<br>
Both failed, the latter (Release) with:</p>
<p>18&gt;  Could NOT find Python3 (missing: Python3_EXECUTABLE Python3_LIBRARIES<br>
18&gt;  Python3_INCLUDE_DIRS Interpreter Development.Module) (Required is at least<br>
18&gt;  version “3.6”)</p>
<p>I used the Slicer.sln present at c:/D/S4R.</p>

---

## Post #7 by @lassoan (2021-10-03 20:39 UTC)

<p>What CMake version do you use? With CMake 3.19.6 I don’t have any SimpleITK build issues, unless some other Python versions are installed on my computer that CMake finds. I’ll start a clean build with latest CMake (3.21.3) and see if I can reproduce the build issue.</p>
<p>In the meantime, can you upload your full build log somewhere (dropbox, onedrive, …) and post the link here so that I can check if there is any sign of some Python installation interferes with the build?</p>
<aside class="quote no-group" data-username="rbumm" data-post="4" data-topic="19960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Python &gt;= 3.9</p>
</blockquote>
</aside>
<p>Have we listed Python as a dependency somewhere? If yes, could you please send us the link?</p>

---

## Post #8 by @rbumm (2021-10-04 11:02 UTC)

<p>Saw this too late, I will have to do the full build later and overnight and probably have the log tomorrow.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="19960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have we listed Python as a dependency somewhere</p>
</blockquote>
</aside>
<p>No, this is not officially listed, it was just my own memo.</p>

---

## Post #9 by @rbumm (2021-10-05 12:08 UTC)

<p>I did the full release build last night, there was a SimpleITK issue, here is the log file:</p>
<p><a href="https://drive.google.com/drive/folders/1PGXiCAJMTx--4gV3sK9fvLF5cM_HDL09?usp=sharing" class="onebox" target="_blank" rel="noopener">https://drive.google.com/drive/folders/1PGXiCAJMTx--4gV3sK9fvLF5cM_HDL09?usp=sharing</a></p>
<p>My CMake version is 3.20.5.</p>

---

## Post #10 by @lassoan (2021-10-05 21:01 UTC)

<p>I’ve noticed this warning:</p>
<blockquote>
<p>47&gt;D:\D\S4R\SlicerExecutionModel\CMake\WindowsApplicationUseUtf8.manifest : manifest authoring warning 81010002: Unrecognized Element “activeCodePage” in namespace “<a href="http://schemas.microsoft.com/SMI/2019/WindowsSettings">http://schemas.microsoft.com/SMI/2019/WindowsSettings</a>”. [D:\D\S4R\SlicerExecutionModel-build\GenerateCLP\GenerateCLPLauncher.vcxproj]</p>
</blockquote>
<p>This indicates that you are building using a very old Windows SDK. <a href="https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/">Installing a more recent version</a> should fix the warning, but by default you should have an SDK that supports activeCodePage setting.</p>
<p>What Windows version do you use?<br>
Have you installed Visual Studio 2019 from scratch or you upgraded from some older versions that were previously installed?</p>
<p>In the meantime, I’m trying to reproduce the error that you have, so far without success.</p>

---

## Post #11 by @lassoan (2021-10-05 21:30 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Probably Python detection is broken in CMake-3.20. Could you try upgrading to latest CMake (3.21.3) and restart the build from scratch?</p>

---

## Post #12 by @rbumm (2021-10-07 18:15 UTC)

<p>I updated CMake but unfortunately also tried to install the latest Windows SDK at the same time.<br>
This fails continuously over the last day and, in addition, Visual Studio 2019 no longer builds Slicer or any of my other projects. So I can not test anything right now, sry.</p>

---

## Post #13 by @lassoan (2021-10-07 20:04 UTC)

<p>What computer do you use is it Windows 10?</p>
<p>You can fix everything by removing all versions of Visual Studio, Windows SDK, and CMake from your computer and install the current Visual Studio version and CMake. Probably latest Visual Studio automatically installs a good Windows SDK if you are using a current Windows 10 version.</p>

---

## Post #14 by @rbumm (2021-10-09 15:19 UTC)

<p>Reinstalling everything was my plan anyway so this fixed the Visual Studio Community 2019 installation on my development PC, ran the build again, latest CMake, no Python installed, this failed again.</p>
<p>Today I tried to reproduce that on on another Windows system: a gaming laptop. Updated CMake.<br>
Fetched, merged and pulled from my Slicer fork,  started a full release build with no S4R present<br>
Python 3.9 installed.</p>
<pre><code class="lang-auto">set startTime=%time%
mkdir C:\D\S4R
cd /d C:\D\S4R
"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 16 2019" -A x64 -DQt5_DIR:PATH=D:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5 C:\D\S4
"C:\Program Files\CMake\bin\cmake.exe" --build . --config Release
echo Start Time: %startTime%
echo Finish Time: %time%
pause   
</code></pre>
<p>worked well (3 hrs build time, 10 GB S4R directory output size, Slicer starting up correctly, version of yesterday).<br>
Then deleted S4R, uninstalled Python and build again with the same script:<br>
 → same failure as on the other Windows PC.</p>
<p>Hope this is helpful somehow,  I could live with having Python installed to make the build, but probably this is not the solution you are going for.  Time note: This was certainly not present three months ago, when I did my first full slicer builds.</p>

---

## Post #15 by @lassoan (2021-10-10 12:47 UTC)

<p>Very useful information, thank you.</p>
<p>Maybe there is something special in your configurations (e.g., German Windows version or locale) that changes how Slicer’s Python is built or detected. Or maybe there is something different in old Visual Studio installations (such as presence of a built-in Python interpreter?).</p>
<p>Can you share the full build log of either the successful or the failed build (preferably both)? That would help us find out where Python is needed and why Slicer Python is not found there.</p>

---

## Post #16 by @jamesobutler (2021-10-10 13:51 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="6" data-topic="19960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>So I uninstalled Python 3.9 and tried to build SimpleITK again in VS2019 either in Debug and Release mode.<br>
Both failed, the latter (Release) with:</p>
<p>18&gt; Could NOT find Python3 (missing: Python3_EXECUTABLE Python3_LIBRARIES<br>
18&gt; Python3_INCLUDE_DIRS Interpreter Development.Module) (Required is at least<br>
18&gt; version “3.6”)</p>
</blockquote>
</aside>
<p>I observed the same type thing as above when building a fresh new debug build of Slicer. SimpleITK was the only project that failed. I used default configure options for the Slicer superbuild except turned off Build Testing and enabled the MP build flag. SimpleITK was to be built with shared libs. I was using a different Windows machine from what I typically use and also building a debug build which I typically don’t use as well. No system python was installed. Using CMake 3.21.3, with Visual Studio 16.11.4, and Windows 11 SDK 10.0.22000 (the latest <a href="https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/" rel="noopener nofollow ugc">Windows SDK</a> offered through Visual Studio Installer).</p>
<pre><code class="lang-auto">46&gt;CMake Error at C:/Program Files/CMake/share/cmake-3.21/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
46&gt;  Could NOT find Python3 (missing: Python3_EXECUTABLE Python3_LIBRARIES
46&gt;  Python3_INCLUDE_DIRS Interpreter Development.Module) (Required is at least
46&gt;  version "3.6")
46&gt;Call Stack (most recent call first):
</code></pre>
<p>I suppose the issue is similar to the old issue with SimpleITK with shared libs in a debug build. In my “C:/S5R/SimpleITK-build/CMakeCache.txt” it reports the following where it finds the Slicer python paths correctly, but does not define <code>PYTHON_DEBUG_LIBRARY</code> or <code>PYTHON_LIBRARY_DEBUG</code> which appears to be what the build error was alerting about?</p>
<pre><code class="lang-auto">//Path to a library.
PYTHON_DEBUG_LIBRARY:FILEPATH=PYTHON_DEBUG_LIBRARY-NOTFOUND

//Initial cache
PYTHON_EXECUTABLE:PATH=C:/S5R/python-install/bin/PythonSlicer.exe

//Initial cache
PYTHON_INCLUDE_DIR:PATH=C:/S5R/python-install/include

//Initial cache
PYTHON_LIBRARY:FILEPATH=C:/S5R/python-install/libs/python36.lib

//Path to a library.
PYTHON_LIBRARY_DEBUG:FILEPATH=PYTHON_LIBRARY_DEBUG-NOTFOUND
</code></pre>
<p>Also in the same file</p>
<pre><code class="lang-auto">//Path to a program.
_Python3_CONFIG:INTERNAL=_Python3_CONFIG-NOTFOUND
//Path to a program.
_Python3_EXECUTABLE:INTERNAL=_Python3_EXECUTABLE-NOTFOUND
//Path to a library.
_Python3_LIBRARY_RELEASE:INTERNAL=_Python3_LIBRARY_RELEASE-NOTFOUND
</code></pre>

---

## Post #17 by @rbumm (2021-10-10 16:41 UTC)

<p>Thanks for the feedback, this seems very familiar and SimpleITK has always been the problematic step in my release builds on Windows 10 without Python installed.<br>
I would prefer not to do these hour-long builds again if not needed, just instruct me when to do so and which files would be needed exactly. I would have planned to do a redirect of the full build make file output into a text file without having Python locally installed.</p>

---

## Post #18 by @lassoan (2021-10-12 00:04 UTC)

<p>Thanks for all your help, I’ve submitted a pull request that will fix this issue: <a href="https://github.com/Slicer/Slicer/pull/5942" class="inline-onebox">BUG: Fix Slicer build errors due to failing to configure SimpleITK by lassoan · Pull Request #5942 · Slicer/Slicer · GitHub</a></p>

---
