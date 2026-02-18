# Qt creator can't see execution files after building from source

**Topic ID**: 14688
**Date**: 2020-11-19
**URL**: https://discourse.slicer.org/t/qt-creator-cant-see-execution-files-after-building-from-source/14688

---

## Post #1 by @keri (2020-11-19 13:41 UTC)

<p>Hi,</p>
<p>I built Slicer from source in debug mode. Now I’m trying to work with Slicer as with usual project but Qt creator can’t see any execution file and moreover header files are inactive like in the picture below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/723fa1c91f2ed0ea5c6c5d372cc4896429fedcfa.png" data-download-href="/uploads/short-url/giGLh5hlU2q2siCXacgLZbMkTGO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/723fa1c91f2ed0ea5c6c5d372cc4896429fedcfa.png" alt="image" data-base62-sha1="giGLh5hlU2q2siCXacgLZbMkTGO" width="228" height="500" data-dominant-color="F7F7F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">311×682 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I suspect that because those execution files are not added in CMakLists.txt<br>
How usually people debug SLicer?</p>
<p>Windows 10, MSVC 2017, Qt 5.14.2, ninja, Master Slicer branch<br>
Slicer source dir: C:\S\Slicer<br>
Build dir: C:\S\d</p>

---

## Post #2 by @keri (2020-11-20 12:34 UTC)

<p>I built SLicer using <strong>.bat</strong>:</p>
<pre><code>set SLICER_SOURCE_DIR="C:/S/Slicer"
set SLICER_BIN_DIR="C:/S/d"
set SLICER_QMAKE_EXE="C:/Qt/5.14.2/msvc2017_64/bin/qmake.exe"
set CMAKE_EXE="C:/Qt/Tools/CMake_64/bin/cmake.exe"
set CTEST_EXE="C:/Qt/Tools/CMake_64/bin/ctest.exe"

mkdir %SLICER_BIN_DIR%
cd /d %SLICER_BIN_DIR%

%CMAKE_EXE% %SLICER_SOURCE_DIR% -G Ninja -DQT_QMAKE_EXECUTABLE:PATH=%SLICER_QMAKE_EXE% -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=ON ^
-DSlicer_USE_SimpleITK:BOOL=OFF ^
-DQt5_DIR="C:/Qt/5.14.2/msvc2017_64/lib/cmake/Qt5" ^
-DCMAKE_BUILD_TYPE=Debug ^
-DCMAKE_INSTALL_PREFIX=C:/S/i
</code></pre>
<p>Next, <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtCreator" rel="noopener nofollow ugc">according to the documentation</a> I should be able to launch QtCreator with:</p>
<pre><code>cd C:\S\d\Slicer-build
.\Slicer.exe --launch C:\Qt\Tools\qtcreator-4.11.0\bin\qtcreator.exe
</code></pre>
<p>But I get error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd7f769184dc89a07d3407ed4a9c00af037e2a3d.png" alt="image" data-base62-sha1="AaxT5Hv8CqNDyXbDMAbYclRPc85" width="412" height="198"></p>
<p>Still struggling…</p>

---

## Post #3 by @jamesobutler (2020-11-20 13:36 UTC)

<p>Have you tried building using my configuration as described in <a href="https://github.com/Slicer/Slicer/issues/5300#issuecomment-728351584" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/5300#issuecomment-728351584</a>?</p>
<p>Slicer 4.11.20200930 git tag, VS 2019, Qt 5.15.1 (MSVC 2019, 64-bit) and a recent CMake version (I use CMake 3.18.4 successfully).</p>

---

## Post #4 by @keri (2020-11-20 13:54 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Hi,</p>
<p>I tried to use stable release with <code>git checkout v4.11.20200930</code> but the problem occurs when building <code>LibArchive</code>. It is discussed here <a href="https://discourse.slicer.org/t/libarchive-build-errors/13310" class="inline-onebox">LibArchive build errors</a></p>
<p>Thus I’m working with master branch.</p>
<p>I have not tried VS 2019 and Qt 5.15.1 as my other project uses VS2017 and Qt 5.14.2</p>
<p>I can try to rebuild Slicer with VS 2019, Qt 5.15.1 (or even Qt 5.15.2) but what to do with <code>LibArchive</code>? Should I still use master branch or 4.11.20200930 git tag? Or maybe I will not encounter such problem with VS 2019</p>
<p>I will rebuilt it and report the result</p>

---

## Post #5 by @keri (2020-11-21 13:44 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> hi,</p>
<p>I just compiled SLicer 4.11.20200930 git tag with MSVC 2019 and Qt 5.14.2</p>
<p>I still got the error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a6fdb7461ec454bc2ae46825d7400393c654b0a.png" alt="image" data-base62-sha1="3LS4aB26bjWiS3l3rr8A4pOpcf0" width="412" height="276"><br>
But I can skip it and continue to normally launch Slicer.</p>
<p>The main question is still undclear, how to open Slicer project and debug Slicer in Qt?<br>
I follow this documentation <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtCreator" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Tutorials/QtCreator - Slicer Wiki</a><br>
I typed:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92bfcda928b2dbe0f9548a8ac5c5295100635d36.png" alt="image" data-base62-sha1="kWcE8Y1rAtSmnXMbLkfZZy4E8Ye" width="690" height="133"><br>
and with MSVC 2019 Qt 5.15.2 it doesn’t give platform plugin error anymore. That is good. After I press <code>ENTER</code> nothing happens. THose two lines in CMD are shown.</p>
<p>and this is how my project is look like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba61270565388902f4045128c4e3a8dd74cd3233.png" data-download-href="/uploads/short-url/qAMXn4O3LhppLVbiCtIeT3l6o9B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba61270565388902f4045128c4e3a8dd74cd3233_2_690x370.png" alt="image" data-base62-sha1="qAMXn4O3LhppLVbiCtIeT3l6o9B" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba61270565388902f4045128c4e3a8dd74cd3233_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba61270565388902f4045128c4e3a8dd74cd3233_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba61270565388902f4045128c4e3a8dd74cd3233_2_1380x740.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×860 72.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jamesobutler (2020-11-21 15:28 UTC)

<p>I’ve never used the Qt Creator IDE so I can’t provide much help on how to proceed there.</p>
<p>You can also view info at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html?highlight=Debugging#debug-slicer" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html?highlight=Debugging#debug-slicer</a> which has some information about various Slicer debugging using Visual Studio whether C++ or Python based debugging.</p>

---

## Post #7 by @keri (2020-11-22 13:58 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> hi,</p>
<p>Thank you a lot! Finally when I 99 % followed the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html?highlight=Debugging#debug-slicer" rel="noopener nofollow ugc">instructions from here</a> (previously I used to build it with Ninja and now I’ve built it with VS 2019 x64 build system) I could launch Slicer from VS 2019 and stop it at a break point in debug mode.</p>
<p>As I don’t really like writing code in VS I’m going to download and try to use VS code. If there is something that I should know about this idea, please notify me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>By the way now there is no any errors when I launch Slicer as it used to be earlier.</p>

---

## Post #8 by @lassoan (2020-12-04 05:21 UTC)

<p>3 posts were split to a new topic: <a href="/t/use-hdf5-library-in-a-slicer-module/14877">Use HDF5 library in a Slicer module</a></p>

---

## Post #9 by @SteveLiu (2022-06-28 04:54 UTC)

<p>Hello I am stuck by the same step in qtcreator Ubuntu OS<br>
Would you like to share some detailed steps to configure the project</p>

---

## Post #10 by @keri (2022-06-28 06:15 UTC)

<p><a class="mention" href="/u/steveliu">@SteveLiu</a> QtCreator doesn’t support intellisense and other staff for cmake superbuild projects (I as I know).</p>
<p><strong>How I use QtCreator with Slicer:</strong><br>
Slicer may build extensions along. (or you can find any and build it externally by yourself).<br>
Extension is a complete cmake project that you can open with QtCreator.<br>
Extension needs to <code>find_package(Slicer)</code> and usually it uses some headers from Slicer <code>#include &lt;qSlicer...&gt;</code>.</p>
<p>If you open an extension in QtCreator then you will see that intellisense work fine there (probably if the extension doesn’t use Superbuild).</p>
<p>Also if you then open Slicer source files while the extension is an active project in QtCreator than you will find that intellisense also work for Slicer (probably not as good as for regular project but it is pretty enough).</p>
<p>To make a little easier I prefer switching the mode of a tree view in left upper corner: from <code>Projects</code> to <code>Files system</code> so that there is no greyer-out header and source files</p>

---
