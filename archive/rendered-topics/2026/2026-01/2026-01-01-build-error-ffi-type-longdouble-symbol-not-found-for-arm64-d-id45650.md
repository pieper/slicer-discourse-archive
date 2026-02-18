# Build Error: _ffi_type_longdouble symbol not found for arm64 during Python build

**Topic ID**: 45650
**Date**: 2026-01-01
**URL**: https://discourse.slicer.org/t/build-error-ffi-type-longdouble-symbol-not-found-for-arm64-during-python-build/45650

---

## Post #1 by @salim (2026-01-01 10:40 UTC)

<p><strong>Hello Slicer Community,</strong></p>
<blockquote>
<p>I am encountering a linker error while building 3D Slicer from source on <strong>Apple Silicon</strong>. The build fails at approximately 51% during the <code>_freeze_importlib</code> step of the Python internal build.</p>
<p>51%] Linking C executable _freeze_importlib<br>
Undefined symbols for architecture arm64:<br>
“_ffi_type_longdouble”, referenced from:<br>
__ctypes_init_fielddesc in cfield.c.o<br>
ld: symbol(s) not found for architecture arm64<br>
clang: error: linker command failed with exit code 1 (use -v to see invocation)<br>
<strong>System &amp; Toolchain Information:</strong></p>
<ul>
<li>
<p><strong>Machine:</strong> Mac Studio (M1/M2/M3 Apple Silicon)</p>
</li>
<li>
<p><strong>OS:</strong> macOS 14.x or 15.x (Sequoia/Sonoma)</p>
</li>
<li>
<p><strong>Architecture:</strong> arm64</p>
</li>
<li>
<p><strong>Python Version:</strong> 3.12.10 (as bundled in the Slicer SuperBuild)</p>
</li>
<li>
<p><strong>CMake Version:</strong> 4.2.1</p>
</li>
<li>
<p><strong>Build Generator:</strong> Unix Makefiles (attempting to switch to Xcode)</p>
</li>
<li>
<p><strong>LibFFI:</strong> Homebrew version 3.5.2 is installed, but the build fails even with <code>Slicer_USE_SYSTEM_LibFFI:BOOL=OFF</code>.</p>
</li>
</ul>
<p><strong>Context:</strong> I have attempted to clear the <code>CMakeCache.txt</code> and rebuild with <code>Slicer_USE_SYSTEM_LibFFI</code> set to <code>OFF</code> to force an internal build of LibFFI. However, the linker still seems to be struggling to find the <code>_ffi_type_longdouble</code> symbol required by <code>_ctypes</code>. It appears that the linker might be picking up a system library or a Homebrew version that does not correctly export this symbol for the arm64 architecture.</p>
<p><strong>Question:</strong> Has anyone successfully resolved this architectural mismatch on Apple Silicon? Are there specific CMake flags or environment variables I should set to ensure Python links against a compatible version of LibFFI that supports <code>longdouble</code> on ARM64?</p>
<p>Thank you for your help!</p>
</blockquote>

---

## Post #2 by @jamesobutler (2026-01-01 13:40 UTC)

<p>Currently macOS arm64 builds are not supported. There are still some remaining items to fix as you discovered. You can however build on an Apple Silicon Mac by building the application as x86_64 and running it using Rosetta 2.</p>
<p>See the following issue and other discourse thread about current state of things:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6811">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6811" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6811" target="_blank" rel="noopener nofollow ugc">Support for building/testing/packaging Slicer on Apple arm64</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-02-02" data-time="00:01:58" data-timezone="UTC">12:01AM - 02 Feb 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is meta issues aiming to organize the sub-tasks associated with arm64 suppo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rt. See Sub-issues listed below.


Related issues and pull requests:
* https://github.com/Slicer/Slicer/issues/5944
* https://github.com/Slicer/Slicer/issues/6705
* https://github.com/Slicer/Slicer/issues/6490
* https://github.com/Slicer/Slicer/pull/8097

Related discourse posts:
* https://discourse.slicer.org/t/issues-running-slicer-on-macbook-m1-max/23974/3
* https://discourse.slicer.org/t/slicer-quit-unexpectedly-on-macbook-with-m1-chip/25989
* https://discourse.slicer.org/t/build-arm-32-openssl/31204
* https://discourse.slicer.org/t/developing-for-slicer-on-apple-silicon-build-targeting-x86-64/40686</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote" data-post="1" data-topic="35699">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/ba8739/48.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/build-3d-slicer-for-macos-arm64/35699">Build 3D Slicer for MacOS arm64?</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --style-square --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
    </div>
  </div>
  <blockquote>
    PyTorch has support for using the shaders in the M series chips, but to use it, one has to use the arm64 version of Python. Should a native (in this case, M3) build of Slicer3D be possible? If yes, where should I get the 5.15.2 Qt package (for MacOS arm64)? 
Thank you! 
Gene
  </blockquote>
</aside>


---

## Post #3 by @GeneRisi (2026-01-01 15:40 UTC)

<p>I looked up longdouble for both ARM64 and x86_64 architectures and what I found is that the actual implementation is hardware, compiler and OS specific. Longdouble can be 80 bits in the calculations padded to 128 bits in memory, or 128 bits, or 64 bits and treated the same as double. I don’t know if all of the scenarios are handled in the build process.</p>

---

## Post #4 by @jamesobutler (2026-01-01 16:57 UTC)

<p>Slicer’s version of libffi needs updating along with other things to support native arm64 builds. For now building on Apple Silicon is possible, but you must build the application as x86_64 instead of arm64.</p>

---

## Post #5 by @salim (2026-01-06 10:21 UTC)

<p>Thank you <a class="mention" href="/u/jamesobutler">@jamesobutler</a>  for the clarification regarding the current state of macOS arm64 support.<br>
Based on the guidance, I am building <strong>3D Slicer as x86_64 on Apple Silicon and running it under Rosetta 2</strong>.</p>
<p>I am working on a <strong>custom 3D Slicer application</strong>, and below are the <strong>exact commands and configuration</strong> I am using, followed by the <strong>errors I am encountering</strong>.</p>
<hr>
<h3><a name="p-131036-build-environment-1" class="anchor" href="#p-131036-build-environment-1" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/hammer_and_wrench.png?v=15" title=":hammer_and_wrench:" class="emoji" alt=":hammer_and_wrench:" loading="lazy" width="20" height="20"> Build environment</h3>
<ul>
<li>
<p><strong>macOS</strong>: 14.x (Apple Silicon, Mac Studio)</p>
</li>
<li>
<p><strong>Architecture</strong>: x86_64 (Rosetta 2)</p>
</li>
<li>
<p><strong>Xcode</strong>: Installed from <code>/Applications/Xcode.app</code></p>
</li>
<li>
<p><strong>Qt</strong>: 5.15.2 (clang_64)</p>
</li>
<li>
<p><strong>CMake</strong>: system-installed</p>
</li>
<li>
<p><strong>Custom Slicer build</strong></p>
</li>
</ul>
<hr>
<h3><a name="p-131036-cmake-configuration-used-2" class="anchor" href="#p-131036-cmake-configuration-used-2" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/receipt.png?v=15" title=":receipt:" class="emoji" alt=":receipt:" loading="lazy" width="20" height="20"> CMake configuration used</h3>
<pre><code class="lang-auto">cd ~/Slicer-Build

# Clean previous build
rm -rf Slicer-build

cmake \
  -DCMAKE_OSX_ARCHITECTURES:STRING=x86_64 \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=14.0 \
  -DCMAKE_OSX_SYSROOT:PATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DQt5_DIR:PATH=/opt/Qt/5.15.2/clang_64/lib/cmake/Qt5 \
  -DSlicer_USE_SYSTEM_QT:BOOL=ON \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DSlicer_USE_PYTHONQT:BOOL=OFF \
  -DSlicer_USE_PYTHON:BOOL=ON \
  -S ~/Slicer-Source \
  -B .

</code></pre>
<hr>
<h3><a name="p-131036-build-command-3" class="anchor" href="#p-131036-build-command-3" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/building_construction.png?v=15" title=":building_construction:" class="emoji" alt=":building_construction:" loading="lazy" width="20" height="20"> Build command</h3>
<pre><code class="lang-auto">cmake --build . -j4 2&gt;&amp;1 | tee build.log

</code></pre>
<p>When attempting to build Python explicitly:</p>
<pre><code class="lang-auto">cmake --build . --target python -j4 2&gt;&amp;1 | tee python-build.log

</code></pre>
<hr>
<h3><a name="p-131036-build-errors-encountered-4" class="anchor" href="#p-131036-build-errors-encountered-4" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/cross_mark.png?v=15" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> Build errors encountered</h3>
<p>During the build, I encounter the following error related to Python headers:</p>
<pre><code class="lang-auto">/Users/archiwizstudio/Slicer-Source/Base/QTCore/qSlicerCoreApplication.cxx:1216:8:
error: unknown type name 'Py_ssize_t'; did you mean 'ssize_t'?

</code></pre>
<p>Additional output:</p>
<pre><code class="lang-auto">[ 47%] Built target qMRMLWidgets
make[3]: *** [all] Error 2
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2
make: *** [all] Error 2

</code></pre>
<p>Attempting to build the Python target directly results in:</p>
<pre><code class="lang-auto">make: *** No rule to make target `python'.  Stop.

</code></pre>
<hr>
<h3><a name="p-131036-cmake-cache-confirmation-5" class="anchor" href="#p-131036-cmake-cache-confirmation-5" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/magnifying_glass_tilted_left.png?v=15" title=":magnifying_glass_tilted_left:" class="emoji" alt=":magnifying_glass_tilted_left:" loading="lazy" width="20" height="20"> CMake cache confirmation</h3>
<pre><code class="lang-auto">grep -i "Slicer_USE_PYTHON" CMakeCache.txt

</code></pre>
<p>Output:</p>
<pre><code class="lang-auto">Slicer_USE_PYTHON:BOOL=ON
Slicer_USE_PYTHONQT:BOOL=OFF

</code></pre>
<p>No Python include or library paths appear to be populated:</p>
<pre><code class="lang-auto">grep -i "PYTHON" CMakeCache.txt | grep -i "DIR\|INCLUDE\|LIBRARY"

</code></pre>
<hr>
<h3><a name="p-131036-questions-6" class="anchor" href="#p-131036-questions-6" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/red_question_mark.png?v=15" title=":red_question_mark:" class="emoji" alt=":red_question_mark:" loading="lazy" width="20" height="20"> Questions</h3>
<ol>
<li>
<p>Is this Python error (<code>Py_ssize_t</code> not found) expected when using <strong>system Python</strong> with <code>Slicer_USE_PYTHON=ON</code>?</p>
</li>
<li>
<p>Is it required to use <strong>Slicer SuperBuild–provided Python</strong> instead of system Python on macOS?</p>
</li>
<li>
<p>Are there <strong>recommended Python versions</strong> (e.g., 3.9 / 3.10) known to work reliably for x86_64 Rosetta builds?</p>
</li>
<li>
<p>Does this configuration depend on a <strong>specific Xcode version</strong> for successful Python integration?</p>
</li>
</ol>
<p>Any guidance or recommended build scripts for resolving Python-related build issues on Apple Silicon (x86_64 via Rosetta) would be greatly appreciated.<br>
this is the systmem information<br>
System</p>
<p>OS: macOS 26.2<br>
Build: 25C56<br>
Kernel: Darwin 25.2.0<br>
Machine Architecture: arm64<br>
Rosetta Translation: NO (sysctl.proc_translated = 0)</p>
<h2><a name="p-131036-xcode-7" class="anchor" href="#p-131036-xcode-7" aria-label="Heading link"></a>Xcode</h2>
<p>Xcode Version: 26.2<br>
Xcode Build: 17C52<br>
Xcode Path: /Applications/Xcode.app/Contents/Developer<br>
macOS SDK: MacOSX26.2.sdk<br>
SDK Version: 26.2</p>
<h2><a name="p-131036-compiler-8" class="anchor" href="#p-131036-compiler-8" aria-label="Heading link"></a>Compiler</h2>
<p>Compiler: Apple clang<br>
Version: 17.0.0 (clang-1700.6.3.2)<br>
Target: arm64-apple-darwin25.2.0<br>
clang Binary: Universal (x86_64 + arm64e)</p>
<h2><a name="p-131036-build-tools-9" class="anchor" href="#p-131036-build-tools-9" aria-label="Heading link"></a>Build Tools</h2>
<p>CMake Version: 4.2.1<br>
CMake Provider: Kitware<br>
Make Version: GNU Make 3.81<br>
Make Binary: Universal (x86_64 + arm64e)<br>
Ninja Version: 1.13.2<br>
Ninja Binary: arm64 (/opt/local/bin/ninja)</p>
<h2><a name="p-131036-qt-10" class="anchor" href="#p-131036-qt-10" aria-label="Heading link"></a>Qt</h2>
<p>Qt Version: 5.15.2<br>
QMake Version: 3.1<br>
Qt Path: /opt/Qt/5.15.2/clang_64<br>
Qt Architecture: x86_64<br>
Qt5Core: /opt/Qt/5.15.2/clang_64/lib/libQt5Core.dylib</p>
<h2><a name="p-131036-python-11" class="anchor" href="#p-131036-python-11" aria-label="Heading link"></a>Python</h2>
<p>python: not found<br>
python3 Version: 3.14.2<br>
python3 Path: /opt/homebrew/bin/python3<br>
Python Architecture: arm64</p>
<h2><a name="p-131036-git-12" class="anchor" href="#p-131036-git-12" aria-label="Heading link"></a>Git</h2>
<p>Git Version: (not reported)<br>
Repository: Slicer (custom build)</p>
<h2><a name="p-131036-slicer-configuration-relevant-flags-13" class="anchor" href="#p-131036-slicer-configuration-relevant-flags-13" aria-label="Heading link"></a>Slicer Configuration (relevant flags)</h2>
<p>Slicer_USE_PYTHON: ON<br>
Slicer_USE_PYTHONQT: OFF<br>
Slicer_USE_SYSTEM_QT: ON</p>
<p>Thank you for your help.</p>

---

## Post #6 by @jamesobutler (2026-01-06 12:18 UTC)

<p>As a first try you should let the Slicer super build build all the dependencies it wants including the python version which becomes an embedded python in the application. It will have to build an x86_64 python for use in this x86_64 application.</p>
<p>The following linked post was a good one that helped me build an x86_64 build on arm mac successfully.</p>
<aside class="quote" data-post="6" data-topic="40686">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/arhowe00/48/80367_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/developing-for-slicer-on-apple-silicon-build-targeting-x86-64/40686/6">Developing for Slicer on Apple Silicon (build targeting x86_64)</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    This is really helpful <a class="mention" href="/u/jamesobutler">@jamesobutler</a> , kudos!
  </blockquote>
</aside>

<p>The Slicer factory build machine builds successfully on macOS with the following environment:</p>
<aside class="quote" data-post="4" data-topic="44950">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/maintenance-of-macos-dashboard-in-progress-upgrading-from-ventura-to-sequoia/44950/4">Maintenance of macOS dashboard in progress - upgrading from Ventura to Sequoia</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    Updates: 


XCode has been updated to 26.1 and clang version is now 17.0.0. 


Issue related to the build of Qt 5.15.18 should now all be sorted our and the build is in progress <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=15" title="rocket" alt="rocket" class="emoji"> 
For more details: <a href="https://github.com/commontk/qt-easy-build/pull/80" class="inline-onebox" rel="noopener nofollow ugc">[5.15.18] Fix detection of OpenGL Qt backend and OpenSSL linkage on macOS by jcfr · Pull Request #80 · commontk/qt-easy-build · GitHub</a>
  </blockquote>
</aside>


---

## Post #7 by @pieper (2026-01-06 14:14 UTC)

<p>This is unlikely to work:</p>
<blockquote>
<p>-DSlicer_USE_PYTHONQT:BOOL=OFF \</p>
</blockquote>
<p>I doubt that path is ever tested since PythonQt is pretty central to most Slicer use cases.</p>

---

## Post #8 by @salim (2026-01-12 10:40 UTC)

<p>Hello <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I’m trying to build <strong>3D Slicer on macOS (x86_64)</strong> using <strong>Xcode 16.1</strong> and the <strong>macOS 15 SDK</strong>, and I’m currently facing linker errors related to Qt during the VTK build stage.</p>
<p>At the moment, I <strong>do not have Qt built from source</strong>, as I couldn’t find an easily available source/build setup for macOS. I am currently using <strong>Qt 5 from Homebrew (<code>brew install qt@5</code>)</strong>.</p>
<p>Since I am <strong>new to macOS development</strong>, I’m not sure whether using <strong>Homebrew’s Qt5</strong> is appropriate for building 3D Slicer, or if this could be the cause of the Qt symbol/linker issues I’m seeing.</p>
<h3><a name="p-131158-questions-1" class="anchor" href="#p-131158-questions-1" aria-label="Heading link"></a>Questions:</h3>
<ol>
<li>
<p>Is <strong>Homebrew Qt5 (<code>qt@5</code>)</strong> supported or recommended for building 3D Slicer on macOS?</p>
</li>
<li>
<p>If not, what is the <strong>recommended way to obtain Qt 5.15.2</strong> for macOS (prebuilt binaries or building from source)?</p>
</li>
<li>
<p>For those who have successfully built Slicer on macOS, could you please share:</p>
<ul>
<li>
<p>The <strong>Qt version used</strong></p>
</li>
<li>
<p>The <strong>Xcode version</strong></p>
</li>
<li>
<p>The <strong>exact CMake configuration / build command</strong> used by you or by Kitware?</p>
</li>
</ul>
</li>
<li>
<p>Are there any <strong>known compatibility issues</strong> between <strong>Qt 5.15.x</strong> and <strong>Xcode 16.x / macOS 15 SDK</strong>?</p>
</li>
</ol>
<p>Any guidance, commands, or references would be very helpful, especially from someone who has already completed a successful macOS build.</p>
<p>Thank you very much for your help.</p>
<p>Best regards,<br>
<strong>Salim Ullah</strong></p>

---

## Post #9 by @pieper (2026-01-12 15:17 UTC)

<p>I haven’t built from source on a mac recently, and when I tried to rebuild a previous build with the current Slicer source there were errors (I don’t recall the specifics).  So I suspect with the ongoing changes in the OS, xcode, cmake, python, homebrew, and Slicer source it’s possible that there is no currently working build formula for any particular machine.  I know that the script below did work, maybe a year ago with whatever OS and xcode were current at the time.</p>
<pre><code class="lang-auto">BUILD_TYPE=Debug
#BUILD_TYPE=Release

CMAKE=/Users/pieper/Downloads/cmake-3.31.7-macos10.10-universal/CMake.app/Contents/bin/cmake

${CMAKE} \
	-DSlicer_VTK_VERSION_MAJOR:STRING=9 \
	-DCMAKE_BUILD_TYPE:STRING=${BUILD_TYPE} \
	-DCMAKE_OSX_DEPLOYMENT_TARGET=13.0 \
	-DQt5_VERSION:STRING=5.15 \
	-DQt5_DIR:PATH=/usr/local/Cellar/qt@5/5.15.17/lib/cmake/Qt5 \
	/Users/pieper/slicer/latest/Slicer
</code></pre>
<p>Personally I’ve been waiting for things to settle down before trying to build again.  It would be great if you can work through and get a working combination.</p>

---
