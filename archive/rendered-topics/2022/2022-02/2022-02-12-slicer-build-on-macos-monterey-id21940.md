# Slicer build on macOS Monterey

**Topic ID**: 21940
**Date**: 2022-02-12
**URL**: https://discourse.slicer.org/t/slicer-build-on-macos-monterey/21940

---

## Post #1 by @priya.vada4 (2022-02-12 18:41 UTC)

<p>Has anyone built Slicer and Qt 5.15.2 on macOS Monterey with Xcode 13.2. I seem to be running into a lot of issues with building Qt5.15.2 from source (including JCFR’s easy script). I also tried to build Slicer with the Qt binaries but after building the code, I get a lot of errors related to link libraries. One example of the error is shown below:</p>
<p>Error(s):<br>
Cannot load library /S4-new2/S-s/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDataModule.dylib: (dlopen(/S4-new2/S-s/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDataModule.dylib, 0x0085): Symbol not found: __ZN6vtksys18SystemToolsManagerC1Ev<br>
Referenced from: /S4-new2/S-s/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDataModule.dylib<br>
Expected in: /S4-new2/S-s/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/libvtkSlicerDataModuleLogic.dylib)</p>
<p>Any idea how this could be resolved?</p>
<p>Priya</p>

---

## Post #2 by @hherhold (2022-02-12 18:59 UTC)

<p>I’ve built on Monterey (12.1) with Qt 5.15.2 and Xcode 13.2.1, though not for a couple of weeks. Not sure what those link errors are, sorry, but that configuration should work.</p>

---

## Post #3 by @pieper (2022-02-12 19:04 UTC)

<p>I typically use Qt from homebrew on mac with no problem, but I haven’t built from scratch in a while.</p>

---

## Post #4 by @hherhold (2022-02-12 19:08 UTC)

<p>Same for me (Qt from homebrew).</p>

---

## Post #5 by @priya.vada4 (2022-02-12 19:19 UTC)

<p>Thanks Steve and Hollister. I am trying to create a Slicer package for a collaborator with a custom module, therefore trying to build Qt from source.</p>
<p>Priya</p>

---

## Post #6 by @hherhold (2022-02-12 20:27 UTC)

<p>I just configured with this <code>cmake</code> line:</p>
<pre><code>cmake -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.15 -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:PATH=/usr/local/Cellar/qt/5.15.2/lib/cmake/Qt5 ../Slicer
</code></pre>
<p>and it’s building now. Should work, I’ll let you know if it doesn’t.</p>
<p>Even if you’re making a custom module, why do you need to build Qt from source?</p>

---

## Post #7 by @hherhold (2022-02-12 21:25 UTC)

<p>So this is kinda odd. I now get:</p>
<pre><code class="lang-auto">[ 15%] Building CXX object Libs/vtkITK/CMakeFiles/vtkITKPython.dir/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx.o
In file included from /opt/SB/debug/Slicer-build/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx:10:
In file included from /opt/SB/Slicer/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilter.h:18:
In file included from /opt/SB/Slicer/Libs/vtkITK/vtkITKImageToImageFilterFF.h:21:
In file included from /opt/SB/debug/ITK/Modules/Bridge/VTK/include/itkVTKImageExport.h:143:
In file included from /opt/SB/debug/ITK/Modules/Bridge/VTK/include/itkVTKImageExport.hxx:27:
In file included from /opt/SB/debug/ITK/Modules/Core/Common/include/itkNumericTraitsDiffusionTensor3DPixel.h:22:
In file included from /opt/SB/debug/ITK/Modules/Core/Common/include/itkDiffusionTensor3D.h:26:
In file included from /opt/SB/debug/ITK/Modules/Core/Common/include/itkSymmetricSecondRankTensor.h:29:
/opt/SB/debug/ITK/Modules/Core/Common/include/itkSymmetricEigenAnalysis.h:156:1: warning: control may reach end of non-void function [-Wreturn-type]
}
^
In file included from /opt/SB/debug/Slicer-build/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx:10:
In file included from /opt/SB/Slicer/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilter.h:19:
In file included from /opt/SB/debug/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkGradientAnisotropicDiffusionImageFilter.h:21:
In file included from /opt/SB/debug/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkAnisotropicDiffusionImageFilter.h:21:
In file included from /opt/SB/debug/ITK/Modules/Core/FiniteDifference/include/itkDenseFiniteDifferenceImageFilter.h:21:
In file included from /opt/SB/debug/ITK/Modules/Core/FiniteDifference/include/itkFiniteDifferenceImageFilter.h:21:
In file included from /opt/SB/debug/ITK/Modules/Core/Common/include/itkInPlaceImageFilter.h:189:
/opt/SB/debug/ITK/Modules/Core/Common/include/itkInPlaceImageFilter.hxx:97:5: error: use of undeclared identifier '__ASSERT_FUNCTION'
    itkAssertOrThrowMacro(inputAsOutput.IsNotNull(), "Unable to convert input image to output image as expected!");
</code></pre>
<p>Looks like __ASSERT_FUNCTION is from assert.h? Am I misreading this?</p>

---

## Post #8 by @hherhold (2022-02-15 16:32 UTC)

<p>Hey <a class="mention" href="/u/pieper">@pieper</a> Steve, have you seen this ITK problem on a Mac? (or anybody else)?</p>

---

## Post #9 by @che85 (2022-02-16 20:18 UTC)

<p>I am experiencing the same issues when starting Slicer.</p>
<p>cmake configuration below:</p>
<pre><code class="lang-auto">
   cmake ../../sources/cpp/Slicer/ \
    -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=12.1 \
    -DQt5_DIR:PATH=/Users/herzc/Qt/5.15.2/clang_64/lib/cmake/Qt5 \
    -DCMAKE_OSX_ARCHITECTURES:STRING=x86_64 \
    -DSlicer_USE_SYSTEM_OpenSSL:BOOL=ON \
    -DSlicer_USE_SimpleITK:BOOL=OFF

</code></pre>
<p>Getting errors like this:</p>
<pre><code class="lang-auto">dlopen(/Users/herzc/D/S4D/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/qSlicerVolumeRenderingModuleWidgetsPythonQt.so, 0x0001): Symbol not found: __ZSt9terminatev
  Referenced from: /Users/herzc/D/S4D/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/qSlicerVolumeRenderingModuleWidgetsPythonQt.so
  Expected in: /Users/herzc/D/S4D/ITK-build/lib/libITKDiffusionTensorImage-5.2.1.dylib
dlopen(/Users/herzc/D/S4D/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/qSlicerDICOMLibModuleWidgetsPythonQt.so, 0x0001): Symbol not found: __ZSt9terminatev
  Referenced from: /Users/herzc/D/S4D/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/qSlicerDICOMLibModuleWidgetsPythonQt.so
  Expected in: /Users/herzc/D/S4D/ITK-build/lib/libitklbfgs-5.2.1.dylib
dlopen(/Users/herzc/D/S4D/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/qSlicerTablesModuleWidgetsPythonQt.so, 0x0001): Symbol not found: __ZSt9terminatev
  Referenced from: /Users/herzc/D/S4D/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/qSlicerTablesModuleWidgetsPythonQt.so
  Expected in: /Users/herzc/D/S4D/ITK-build/lib/libITKOptimizersv4-5.2.1.dylib

</code></pre>
<p>I am using Qt from the online installer but can also try again with the one installed from brew (but Qt designer doesn’t work with that one)</p>
<p>I will try again with the cmake configuration from here: <a href="https://discourse.slicer.org/t/slicer-build-on-macos-monterey/21940/6" class="inline-onebox">Slicer build on macOS Monterey - #6 by hherhold</a></p>

---

## Post #10 by @hherhold (2022-02-16 20:21 UTC)

<p>Something relatively recent changed; I can build a fork from late January but the latest master fails.</p>
<p>The build machine looks okay though, I wonder if it’s a Monterey thing with some recent update?</p>

---

## Post #11 by @che85 (2022-02-16 20:22 UTC)

<p>Building an early Jan version works, but I am still getting the same errors when starting Slicer.</p>
<p>I will try with your configuration.</p>

---

## Post #12 by @hherhold (2022-02-16 20:26 UTC)

<p>I looked through the 85 or so commits between the branch I have from late January (I said fork before, sorry, meant branch) and master from today, but nothing was obvious. I might try a binary search and see what broke things, I’ll let you know if I get to this.</p>

---

## Post #13 by @pieper (2022-02-16 20:39 UTC)

<p>Thanks - let us know what you find.  I haven’t had a chance to try building since my mac (and my brain) are tied up with some other projects.</p>

---

## Post #14 by @hherhold (2022-02-17 02:35 UTC)

<p>It looks like it was this one (below). The errors I get are the ones above, and included below for completeness.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/416a492f0a87c88e32c064afe877c759ff18681d">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/416a492f0a87c88e32c064afe877c759ff18681d" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/416a492f0a87c88e32c064afe877c759ff18681d" target="_blank" rel="noopener nofollow ugc">COMP: Update python-cmake-buildsystem anticipating python version update</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-01-20" data-time="06:23:23" data-timezone="UTC">06:23AM - 20 Jan 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 1 files with 3 additions and 3 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/416a492f0a87c88e32c064afe877c759ff18681d" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+3</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Summary:
- Add support for building CPython 3.7.x, 3.8.x and 3.9.x
- cmake: Upda<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/416a492f0a87c88e32c064afe877c759ff18681d" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">te minimum required version from 2.8.4 to 3.13.5
- 3.6.x: Add support for building asyncio module
- Deprecate SQLITE3_INCLUDE_PATH/SQLITE3_LIBRARY variables and prefer
  SQLite3_INCLUDE_DIR/SQLite3_LIBRARY.

List of python changes:

$ git shortlog dca8bee81..1feb43e4b --no-merges
Andras Lasso (1):
      Remove irrelevant comment

Dan Dees (3):
      cmake: Python 3.5.10 requires PY3_DLLNAME definition
      cmake: Display external libraries information
      3.7.x: Add USE_SYSTEM_FFI option

David Brooks (2):
      Add checksums for Python 3.5.6 to 3.5.10, 3.6.8 to 3.6.15. Set default to 3.6.15
      3.6.x: Add support for building asyncio module

Fernando Bordignon (6):
      circleci/linux: Expect tests to run in less than 360s
      circleci/linux: Install dependencies to build &amp; test more extensions
      circleci/win: Update config to include windows build using VS2019
      3.7.x: Update approach for using release OpenSSL in debug CPython
      cmake: Fix list of requirements associated with _bsddb module
      3.6.x: Add support for building _testconsole module

James Butler (4):
      cmake: Add checksums for Python 3.8.7 to 3.8.12
      cmake: Add checksum for Python 3.9.10
      ci: Test latest patch release versions
      cmake: Update default version to 3.9.10

Jean-Christophe Fillion-Robin (49):
      PythonApplyPatches: Refactor logic applying patch to Python 2.7.11 and 2.7.12
      lzma: Fix Python 2.7 build excluding lzma extension introduced in Python 3.3
      ci/appveyor: Explicitly specify GENERATOR and PLATFORM
      ci/appveyor: Remove testing of 2.7.3 to 2.7.14
      ci/appveyor: Update 3.6.5 to 3.6.7, 2.7.14 to 2.7.15, Remove 3.5.5
      ci: Add CircleCI 2.0 configuration
      ci: Remove obsolete Circle 1.0 configuration
      circleci/linux: Update python 2.7.14 -&gt; 2.7.15, 3.6.4 -&gt; 3.6.7, remove 3.5.5
      cmake: Update add_python_extension to support NEVER_BUILTIN option
      cmake: Append "-static" to fix executable linking when WITH_STATIC_DEPENDENCIES is ON
      cmake: Fix undefined reference to gss_* symbols when WITH_STATIC_DEPENDENCIES is ON
      cmake: Update minimum required version from 2.8.4 to 3.13.5
      cmake: Remove unused custom CMake module for detecting CMake features
      cmake/Extensions: Simplify removing workaround specific to CMake &lt; 2.8.8
      cmake: Fix undefined reference to gss_* symbols when libkrb5-dev package not installed
      PythonExtractVersionInfo: Support extracting version from patchlevel for alpha/beta/rc releases
      style: Simplify comparison using VERSION_GREATER_EQUAL if syntax
      audioop, _ctypes_test: Add missing libm dependency
      3.6.x: Update pyconfig.h.in and add missing configure checks
      ci: Remove obsolete travis configuration
      Add support for building Python 3.7.x
      Add checksums for 3.7.8 to 3.7.12, update CI and set default to 3.7.12
      PythonAutoDetectOSX: Fix query of SDK path converting SDK version into a two-component string
      ci: Add GitHub Actions config for building &amp; testing on macOS
      cmake/config-unix/pyconfig.h.in: Consistently specify #cmakedefine
      cmake/config-unix/pyconfig.h.in: Ensure HAVE_GLIBC_MEMMOVE_BUG is defined
      circleci: Fix download of dashboard scripts using "git@" protocol
      cmake: Find SQLite3 using module provided by CMake
      cmake/config-unix/pyconfig.h.in: Consistently specify #cmakedefine
      Add support for building Python 3.8.x
      Add support for building Python 3.9.x
      cmake: Add tests at configure time based on files matching "test/test_*.py"
      3.6.x: Fix test_regrtest installing Tools/scripts/run_tests.py
      3.8.x: Fix test_fcntl on macOS ensuring _posixshmem module is built
      3.7.x: Fix incorrect PYTHONFRAMEWORK value returned by sysconfig.get_config_var
      ci/appveyor: Speed up CI removing Python 3.x jobs
      README: Update default version from 3.8.5 to 3.9.9
      cmake: Add checksums for Python 3.9.0 to 3.9.7
      PythonApplyPatches: Remove duplicated set of patches
      cmake/patches-win32: Remove obsolete patches related to VS2008 Express and VS2010
      cmake/patches-win32: Manage MinGW 2.7.x patches using PythonApplyPatches module
      README: Remove "Remarks" subsection and add new entry to FAQ
      README: Improve readability of overview section adding blank lines
      README: Update windows build instruction using VS2019 generator
      _testconsole: Fix link error when attempting to build extension as builtin on Linux
      cmake: Prevent some of 3.x built-in extensions from being registered twice
      datetime, time: Fix build conditionally including _time.c or timemodule.c
      cmake: Remove duplicated sources between libpython and extensions
      cmake: Mark relevant modules as ALWAYS_BUILTIN

Kai Hainke (1):
      PythonApplyPatches: Patch 2.7.[11|12] to support VS2015

Marcel Metz (1):
      cmake: Update extension BUILTIN to match CPython autoconf defaults

Minmin Gong (2):
      cmake: Skip CMP0045 on CMake &gt;= 3.0.1
      cmake/extensions: Call set_target_properties only for enabled extensions

Walter Oggioni (1):
      Fix install specifying DESTDIR env. var

Co-authored-by: Fernando Bordignon &lt;fernando@ltrace.com.br&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And the build error:</p>
<pre><code class="lang-auto">[ 15%] Built target vtkITK
[ 15%] Building CXX object Libs/vtkITK/CMakeFiles/vtkITKPython.dir/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx.o
In file included from /opt/SB/build-test/Slicer-build/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx:10:
In file included from /opt/SB/Slicer/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilter.h:18:
In file included from /opt/SB/Slicer/Libs/vtkITK/vtkITKImageToImageFilterFF.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Bridge/VTK/include/itkVTKImageExport.h:143:
In file included from /opt/SB/build-test/ITK/Modules/Bridge/VTK/include/itkVTKImageExport.hxx:27:
In file included from /opt/SB/build-test/ITK/Modules/Core/Common/include/itkNumericTraitsDiffusionTensor3DPixel.h:22:
In file included from /opt/SB/build-test/ITK/Modules/Core/Common/include/itkDiffusionTensor3D.h:26:
In file included from /opt/SB/build-test/ITK/Modules/Core/Common/include/itkSymmetricSecondRankTensor.h:29:
/opt/SB/build-test/ITK/Modules/Core/Common/include/itkSymmetricEigenAnalysis.h:156:1: warning: control may reach end of non-void function [-Wreturn-type]
}
^
In file included from /opt/SB/build-test/Slicer-build/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx:10:
In file included from /opt/SB/Slicer/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilter.h:19:
In file included from /opt/SB/build-test/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkGradientAnisotropicDiffusionImageFilter.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkAnisotropicDiffusionImageFilter.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/FiniteDifference/include/itkDenseFiniteDifferenceImageFilter.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/FiniteDifference/include/itkFiniteDifferenceImageFilter.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/Common/include/itkInPlaceImageFilter.h:189:
/opt/SB/build-test/ITK/Modules/Core/Common/include/itkInPlaceImageFilter.hxx:97:5: error: use of undeclared identifier '__ASSERT_FUNCTION'
    itkAssertOrThrowMacro(inputAsOutput.IsNotNull(), "Unable to convert input image to output image as expected!");
    ^
/opt/SB/build-test/ITK/Modules/Core/Common/include/itkMacro.h:754:5: note: expanded from macro 'itkAssertOrThrowMacro'
    itkAssertInDebugOrThrowInReleaseMacro(msgstr.str().c_str());                                                       \
    ^
/opt/SB/build-test/ITK/Modules/Core/Common/include/itkMacro.h:740:95: note: expanded from macro 'itkAssertInDebugOrThrowInReleaseMacro'
#    define itkAssertInDebugOrThrowInReleaseMacro(msg) __assert_fail(msg, __FILE__, __LINE__, __ASSERT_FUNCTION);
                                                                                              ^
In file included from /opt/SB/build-test/Slicer-build/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx:10:
In file included from /opt/SB/Slicer/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilter.h:19:
In file included from /opt/SB/build-test/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkGradientAnisotropicDiffusionImageFilter.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkAnisotropicDiffusionImageFilter.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/FiniteDifference/include/itkDenseFiniteDifferenceImageFilter.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/FiniteDifference/include/itkFiniteDifferenceImageFilter.h:380:
In file included from /opt/SB/build-test/ITK/Modules/Core/FiniteDifference/include/itkFiniteDifferenceImageFilter.hxx:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/Common/include/itkImageRegionIterator.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/Common/include/itkImageRegionConstIterator.h:21:
In file included from /opt/SB/build-test/ITK/Modules/Core/Common/include/itkImageIterator.h:21:
/opt/SB/build-test/ITK/Modules/Core/Common/include/itkImageConstIterator.h:210:7: error: use of undeclared identifier '__ASSERT_FUNCTION'
      itkAssertOrThrowMacro((bufferedRegion.IsInside(m_Region)),
      ^
/opt/SB/build-test/ITK/Modules/Core/Common/include/itkMacro.h:754:5: note: expanded from macro 'itkAssertOrThrowMacro'
    itkAssertInDebugOrThrowInReleaseMacro(msgstr.str().c_str());                                                       \
    ^
/opt/SB/build-test/ITK/Modules/Core/Common/include/itkMacro.h:740:95: note: expanded from macro 'itkAssertInDebugOrThrowInReleaseMacro'
#    define itkAssertInDebugOrThrowInReleaseMacro(msg) __assert_fail(msg, __FILE__, __LINE__, __ASSERT_FUNCTION);
                                                                                              ^
1 warning and 2 errors generated.
make[5]: *** [Libs/vtkITK/CMakeFiles/vtkITKPython.dir/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx.o] Error 1
make[4]: *** [Libs/vtkITK/CMakeFiles/vtkITKPython.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2
make: *** [all] Error 2
</code></pre>

---

## Post #15 by @hherhold (2022-02-17 02:36 UTC)

<p>Also, why the nightly builds aren’t broken, I have no idea. My guess is that machine isn’t running Monterey? I’m running 12.1 right now.</p>

---

## Post #16 by @hherhold (2022-02-24 14:34 UTC)

<p>Hi Steve <a class="mention" href="/u/pieper">@pieper</a> ,</p>
<p>I saw the change to ITK in the most recent commit but I still get this error, the failing target is vtkITKPython. Any ideas?</p>
<p>Thanks!</p>

---

## Post #17 by @che85 (2022-04-06 20:25 UTC)

<p>I tried compiling again and getting the same errors:</p>
<pre><code class="lang-auto">In file included from /Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkInPlaceImageFilter.h:189:
/Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkInPlaceImageFilter.hxx:93:5: error: use of undeclared identifier '__ASSERT_FUNCTION'
    itkAssertOrThrowMacro(inputAsOutput.IsNotNull(), "Unable to convert input image to output image as expected!");
    ^
/Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkMacro.h:794:5: note: expanded from macro 'itkAssertOrThrowMacro'
    itkAssertInDebugOrThrowInReleaseMacro(msgstr.str().c_str()); \
    ^
/Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkMacro.h:780:95: note: expanded from macro 'itkAssertInDebugOrThrowInReleaseMacro'
#    define itkAssertInDebugOrThrowInReleaseMacro(msg) __assert_fail(msg, __FILE__, __LINE__, __ASSERT_FUNCTION);
                                                                                              ^
In file included from /Users/herzc/D/S4DD/Slicer-build/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx:10:
In file included from /Users/herzc/sources/cpp/Slicer/Libs/vtkITK/vtkITKGradientAnisotropicDiffusionImageFilter.h:19:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkGradientAnisotropicDiffusionImageFilter.h:21:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Filtering/AnisotropicSmoothing/include/itkAnisotropicDiffusionImageFilter.h:21:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Core/FiniteDifference/include/itkDenseFiniteDifferenceImageFilter.h:21:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Core/FiniteDifference/include/itkFiniteDifferenceImageFilter.h:380:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Core/FiniteDifference/include/itkFiniteDifferenceImageFilter.hxx:21:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkImageRegionIterator.h:21:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkImageRegionConstIterator.h:21:
In file included from /Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkImageIterator.h:21:
/Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkImageConstIterator.h:210:7: error: use of undeclared identifier '__ASSERT_FUNCTION'
      itkAssertOrThrowMacro((bufferedRegion.IsInside(m_Region)),
      ^
/Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkMacro.h:794:5: note: expanded from macro 'itkAssertOrThrowMacro'
    itkAssertInDebugOrThrowInReleaseMacro(msgstr.str().c_str()); \
    ^
/Users/herzc/D/S4DD/ITK/Modules/Core/Common/include/itkMacro.h:780:95: note: expanded from macro 'itkAssertInDebugOrThrowInReleaseMacro'
#    define itkAssertInDebugOrThrowInReleaseMacro(msg) __assert_fail(msg, __FILE__, __LINE__, __ASSERT_FUNCTION);
                                                                                              ^
1 warning generated.
1 warning and 2 errors generated.
make[5]: *** [Libs/vtkITK/CMakeFiles/vtkITKPython.dir/vtkITKGradientAnisotropicDiffusionImageFilterPython.cxx.o] Error 1
make[4]: *** [Libs/vtkITK/CMakeFiles/vtkITKPython.dir/all] Error 2
</code></pre>
<p>So far only reverting changes to early 2022 worked for me.</p>

---

## Post #18 by @jamesobutler (2022-04-06 20:54 UTC)

<p>Not a conflicting assert header in your path? re <a href="https://stackoverflow.com/a/64184500" class="inline-onebox" rel="noopener nofollow ugc">c++ - Message "error: use of undeclared identifier 'assert'" - Stack Overflow</a></p>

---

## Post #19 by @markasselin (2022-04-10 13:52 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> <a class="mention" href="/u/che85">@che85</a></p>
<p>I’ve experienced the same issue on Monterey. I dug a little deeper, and it looks like the root cause is the preprocessor identifier _POSIX_SOURCE being defined during compile of vtkITK.This causes itkMacro.h file to conditionally include code which depends on Linux specific details of assert.h.</p>
<p>I sent a <a href="https://github.com/Slicer/ITK/pull/6" rel="noopener nofollow ugc">PR</a> which uses the more granular __linux preprocessor identifier for this conditional to Slicer/ITK and once approved will duplicate this to the main ITK repository.</p>

---

## Post #20 by @hherhold (2022-04-10 23:04 UTC)

<p>Good catch! This appears to work on my machine as well - vtkITKPython target was the one failing, and it just finished. Rest of the build proceeding.</p>
<p>Nicely done!</p>

---
