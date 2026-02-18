# Build failing in CTK on MacOS 10.12, Slicer nightly, Qt 5.9

**Topic ID**: 2551
**Date**: 2018-04-09
**URL**: https://discourse.slicer.org/t/build-failing-in-ctk-on-macos-10-12-slicer-nightly-qt-5-9/2551

---

## Post #1 by @mschumaker (2018-04-09 21:05 UTC)

<p>I’ve encountered some build errors with my Slicer build on MacOS 10.12. One I identified a suggested solution for:<br>
Installing Slicer nightly master on MacOS 10.12, Qt 5.9, VTK nightly. Build failure on python target. ~/Slicer-SuperBuild/python-build/bin/Release/Makefile and ~/Slicer-SuperBuild/python-build/bin/Release/pyconfig.h could not be found. Solution was that they were being placed in the directory one level up, ~/Slicer-SuperBuild/python-build/bin. I copied files to the Release folder, build successful.</p>
<p>Another is hard to tell if it is a warning or error. It is in the python-GitPython target. The error/warning messages are:</p>
<pre><code>running install_egg_info
running egg_info
writing requirements to GitPython.egg-info/requires.txt
writing GitPython.egg-info/PKG-INFO
writing top-level names to GitPython.egg-info/top_level.txt
writing dependency_links to GitPython.egg-info/dependency_links.txt
reading manifest file 'GitPython.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching 'README'
warning: no previously-included files matching '__pycache__' found anywhere in distribution
warning: no previously-included files matching '*.pyc' found anywhere in distribution
</code></pre>
<p>then farther down,</p>
<pre><code>/Applications/CMake.app/Contents/bin/cmake -E touch /Users/michaelschumaker/Packages/Slicer-SuperBuild/python-GitPython-prefix/src/python-GitPython-stamp/Debug/python-GitPython-done
Command /bin/sh emitted errors but did not return a nonzero exit code to indicate failure
</code></pre>
<p>The effect of this last one on the final executable is something I don’t know.</p>

---

## Post #2 by @mschumaker (2018-04-09 21:22 UTC)

<p>Also, in CMake, the dependency on the Qt5Network_DIR variable is not set in the Slicer project, but it is required by the CTK project and its sub-projects like PythonQt.</p>

---

## Post #3 by @mschumaker (2018-04-10 15:14 UTC)

<p>I’m currently unable to build the newest master branch Slicer. It’s failing at the CTK target. I can see in my CMake configuration that the value of Qt5Network_DIR is defined, but when Xcode attempts to build the CTK target within the CTK project, I get an error message that Qt5NetworkConfig.cmake can’t be found. How can I fix or work around this? Thanks.</p>
<pre><code>=== BUILD AGGREGATE TARGET CTK OF PROJECT CTK WITH CONFIGURATION Debug ===

Check dependencies

Write auxiliary files
write-file /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh
chmod 0755 /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh

PhaseScriptExecution CMake\ Rules /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh
    cd /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK
    /bin/sh -c /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh
echo "Performing configure step for 'CTK'"
Performing configure step for 'CTK'
cd /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-build &amp;&amp; /Applications/CMake.app/Contents/bin/cmake -C/Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-prefix/tmp/CTK-cache-Debug.cmake -GXcode /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK
loading initial cache file /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-prefix/tmp/CTK-cache-Debug.cmake
CMake Error at /Users/michaelschumaker/Qt/5.9/Src/qtxmlpatterns/lib/cmake/Qt5XmlPatterns/Qt5XmlPatternsConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "Qt5Network"
  (requested version 5.9.0) with any of the following names:

    Qt5NetworkConfig.cmake
    qt5network-config.cmake

  Add the installation prefix of "Qt5Network" to CMAKE_PREFIX_PATH or set
  "Qt5Network_DIR" to a directory containing one of the above files.  If
  "Qt5Network" provides a separate development package or SDK, be sure it has
  been installed.
Call Stack (most recent call first):
  /Users/michaelschumaker/Qt/5.9/Src/qtbase/lib/cmake/Qt5/Qt5Config.cmake:28 (find_package)
  CMake/ctkMacroSetupQt.cmake:50 (find_package)
  CMakeLists.txt:421 (ctkMacroSetupQt)


-- Configuring incomplete, errors occurred!
See also "/Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-build/CMakeFiles/CMakeOutput.log".
make[1]: *** [/Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-prefix/src/CTK-stamp/Debug/CTK-configure] Error 1
Command /bin/sh failed with exit code 2</code></pre>

---

## Post #4 by @ihnorton (2018-04-10 15:42 UTC)

<p>What is your cmake configure command line? It needs to include <code>Qt5_DIR=/path/to/Qt5/cmake</code>. See</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Status" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Status</a></p>

---

## Post #5 by @mschumaker (2018-04-10 16:41 UTC)

<p>Thanks for replying.<br>
I’m using the CMake GUI (3.11.0) to generate an Xcode project file. Qt5_DIR is set to ~/Qt/5.9/Src/qtbase/lib/cmake/Qt5. Most of the Slicer package has compiled successfully, and been able to find Qt libraries, but CTK fails.</p>

---

## Post #6 by @ihnorton (2018-04-10 16:55 UTC)

<p>How did you build/acquire Qt5? Does the following directory exist: <code>~/Qt/5.9/Src/qtbase/lib/cmake/Qt5Network</code>?</p>
<p>If the folder above does exist, my only other suggestion would be to try building with the makefile or ninja generator target instead of XCode project.</p>
<p>Unfortunately I can’t do a clean test myself right now, so hopefully someone else will chime in if they’ve done a successful clean build on mac recently. However, the mac build was ok on the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">dashboard</a> last night, and I’m fairly sure that is a full clean build.</p>

---

## Post #7 by @mschumaker (2018-04-10 17:08 UTC)

<p>Thanks. The directory exists and Qt5NetworkConfig.cmake is in it, but for some reason CTK, and only CTK, isn’t finding it. I’ll investigate other build options.<br>
Has anyone else encountered this, or have a suggestion?</p>

---

## Post #8 by @mschumaker (2018-04-10 17:17 UTC)

<p>I’m also confused as to why the CTK project is built in Debug while the main Slicer project is being built in Release.</p>

---

## Post #9 by @mschumaker (2018-04-10 20:10 UTC)

<p>Looking at the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview" rel="nofollow noopener">dashboard</a>, the Mac builds were done with Qt 5.10. I’m compiling 5.10.1 now, and I’ll see if that changes the outcome of my Slicer build.</p>

---

## Post #10 by @fedorov (2018-04-10 21:23 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="8" data-topic="2551" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>I’m also confused as to why the CTK project is built in Debug while the main Slicer project is being built in Release.</p>
</blockquote>
</aside>
<p>It’s been my experience as well that cmake settings do not always propagate into sub-project. You might want to check and reset manually for sub-projects if that is important for you.</p>

---

## Post #11 by @pieper (2018-04-10 22:27 UTC)

<p>My Qt5.10 builds are fine on mac and I never had problems with Qt 5.9 in the past.  I always use Makefiles and not Xcode projects so you might give that a try.</p>

---

## Post #12 by @mschumaker (2018-04-11 16:30 UTC)

<p>Thanks. I’m now trying building using Makefiles with Qt 5.10.1. For some reason, it’s now failing at the tcl compilation step. The output from that step is below. It appears to be failing to find a file, but I can see the file in the directory. Also it is not recognizing the --with-tk option flag.<br>
Any thoughts?<br>
Thanks again.</p>
<pre><code>[ 45%] Generate version-incrTcl.txt and license-incrTcl.txt
[ 45%] Performing configure step for 'incrTcl'
-- incrTcl: Removing 'configure' log files
-- incrTcl: incrTcl_WORKING_DIR: /Users/michaelschumaker/Packages/Slicer-SuperBuild/tcl/incrTcl
-- incrTcl: sh;configure;--with-tcl=/Users/michaelschumaker/Packages/Slicer-SuperBuild/tcl-build/lib;--with-tk=/Users/michaelschumaker/Packages/Slicer-SuperBuild/tcl-build/lib;--prefix=/Users/michaelschumaker/Packages/Slicer-SuperBuild/tcl-build
-- incrTcl: Errors detected - See below.
checking for correct TEA configuration... ok (TEA 3.9)
configure: configuring itcl 4.0.1
checking whether ln -s works... yes
checking for Tcl configuration... found /Users/michaelschumaker/Packages/Slicer-SuperBuild/tcl-build/lib/tclConfig.sh
checking for gcc... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc accepts -g... yes
checking for /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc option to accept ISO C89... none needed
checking for existence of /Users/michaelschumaker/Packages/Slicer-SuperBuild/tcl-build/lib/tclConfig.sh... loading
checking platform... unix
configure: --exec-prefix defaulting to TCL_EXEC_PREFIX /Users/michaelschumaker/Packages/Slicer-SuperBuild/tcl-build
checking for gcc... (cached) /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc accepts -g... (cached) yes
checking for /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc option to accept ISO C89... (cached) none needed
checking how to run the C preprocessor... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -E
checking whether make sets $(MAKE)... yes
checking for ranlib... ranlib
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking if the compiler understands -pipe... yes
checking whether byte ordering is bigendian... no
checking for sin... yes
checking for main in -lieee... no
checking for main in -linet... no
checking net/errno.h usability... no
checking net/errno.h presence... no
checking for net/errno.h... no
checking for connect... yes
checking for gethostbyname... yes
checking dirent.h... yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking float.h usability... yes
checking float.h presence... yes
checking for float.h... yes
checking values.h usability... no
checking values.h presence... no
checking for values.h... no
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking dlfcn.h usability... yes
checking dlfcn.h presence... yes
checking for dlfcn.h... yes
checking sys/param.h usability... yes
checking sys/param.h presence... yes
checking for sys/param.h... yes

configure: WARNING: unrecognized options: --with-tk
configure: error: could not find source file 'itcl2TclOO.c'

CMake Error at /Users/michaelschumaker/Packages/Slicer/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  incrTcl: configure step failed with exit code '1'.

  Outputs also captured in
  /Users/michaelschumaker/Packages/Slicer-SuperBuild/incrTcl_configure_step_output.txt
  and
  /Users/michaelschumaker/Packages/Slicer-SuperBuild/incrTcl_configure_step_error.txt.


  Setting env.  variable EP_EXECUTE_DISABLE_CAPTURE_OUTPUTS to 1 allows to
  disable file capture.

Call Stack (most recent call first):
  /Users/michaelschumaker/Packages/Slicer-SuperBuild/incrTcl_configure_step.cmake:3 (ExternalProject_Execute)


make[2]: *** [incrTcl-prefix/src/incrTcl-stamp/incrTcl-configure] Error 1
make[1]: *** [CMakeFiles/incrTcl.dir/all] Error 2
make: *** [all] Error 2</code></pre>

---

## Post #13 by @fedorov (2018-04-11 16:42 UTC)

<p>You should disable TCL in Cmake options.</p>

---

## Post #14 by @mschumaker (2018-04-11 16:51 UTC)

<p>Excellent, thank you. Skipping it makes life easier. The build is moving on to the next thing.</p>

---

## Post #15 by @mschumaker (2018-04-11 19:07 UTC)

<p>Using Makefiles I still had the same problem with CTK - the value of Qt5Network_DIR is not propagated down to CTK and its sub-projects. I was able to go down to the PythonQt sub-project and add the Qt5Network_DIR value to the cache for it. However, even though I set the value in the CMake GUI for source: ~/Slicer-SuperBuild/CTK and Build destination: ~/Slicer-SuperBuild/CTK-build, it still returns with the message that it Qt5Network was not found. Is there something else I should be doing with the configuration?<br>
Thanks for any assistance.</p>
<pre><code>[ 83%] Performing configure step for 'CTK'
loading initial cache file /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-prefix/tmp/CTK-cache-Release.cmake
CMake Error at /Users/michaelschumaker/Qt/5.10.1/Src/qtxmlpatterns/lib/cmake/Qt5XmlPatterns/Qt5XmlPatternsConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "Qt5Network"
  (requested version 5.10.1) with any of the following names:

    Qt5NetworkConfig.cmake
    qt5network-config.cmake

  Add the installation prefix of "Qt5Network" to CMAKE_PREFIX_PATH or set
  "Qt5Network_DIR" to a directory containing one of the above files.  If
  "Qt5Network" provides a separate development package or SDK, be sure it has
  been installed.
Call Stack (most recent call first):
  /Users/michaelschumaker/Qt/5.10.1/Src/qtbase/lib/cmake/Qt5/Qt5Config.cmake:28 (find_package)
  CMake/ctkMacroSetupQt.cmake:50 (find_package)
  CMakeLists.txt:421 (ctkMacroSetupQt)


-- Configuring incomplete, errors occurred!
See also "/Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-build/CMakeFiles/CMakeOutput.log".
make[2]: *** [CTK-prefix/src/CTK-stamp/CTK-configure] Error 1
make[1]: *** [CMakeFiles/CTK.dir/all] Error 2
make: *** [all] Error 2</code></pre>

---

## Post #16 by @mschumaker (2018-04-11 19:28 UTC)

<p>Got it at last. I manually added the line:<br>
<code>set(Qt5Network_DIR "/Users/michaelschumaker/Qt/5.10.1/Src/qtbase/lib/cmake/Qt5Network" CACHE PATH "Initial cache" FORCE)</code><br>
to the file ~/Slicer-SuperBuild/CTK-build/CTK-prefix/tmp/CTK-cache-Release.cmake<br>
Since the set value for Qt5Network_DIR wasn’t propagating down, when the temporary file was made, it didn’t include the set command for Qt5Network_DIR.<br>
Is this really not happening in other Mac builds?</p>

---

## Post #17 by @pieper (2018-04-12 12:41 UTC)

<p>Hi -</p>
<p>I just did a fresh build on mac 10.13.3 with the cmake command below and it succeeded with no errors.  I used the Slicer master as of last night.</p>
<p>HTH,<br>
Steve</p>
<pre><code class="lang-auto">cmake \
  -DQT_QMAKE_EXECUTABLE:FILEPATH=/Users/pieper/Qt/5.10.0/clang_64/bin/qmake \
  -DCMAKE_PREFIX_PATH:PATH=/Users/pieper/Qt/5.10.0/clang_64/ \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9 \
  -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DSlicer_USE_QtTesting:BOOL=OFF \
  -DSlicer_BUILD_EXTENSIONMANAGER_SUPPORT:BOOL=OFF \
  -DSlicer_VTK_VERSION_MAJOR:STRING=9 \
  -DSlicer_VTK_RENDERING_BACKEND:STRING=OpenGL2 \
  -DSlicer_BUILD_DataStore:BOOL=OFF \
  ../Slicer
make -j20
</code></pre>

---

## Post #18 by @mschumaker (2018-04-13 15:01 UTC)

<p>Thank you for testing that.<br>
I finally figured out what I was doing that was strange, and I completed a fresh build with no errors. I had both pre-built and compiled-from-source versions of Qt 5.10, in directories Qt/5.10.1/clang_64 and Qt/5.10.1/Src, respectively. In my CMake configuration, I ended up with a mix of references to the Qt directories, and so in a few cases, when a Qt library needed to reference another one, it couldn’t find it in the place it was expecting it. This mainly happened with the QtWeb-related libraries. When I made sure that the CMake cache consistently referenced the pre-built Qt in clang_64, everything worked out fine.</p>
<p>Thanks again everyone for your assistance.</p>

---

## Post #19 by @pieper (2018-04-13 15:31 UTC)

<p>Makes sense - glad it’s working for you now.</p>

---

## Post #20 by @mschumaker (2018-04-13 16:41 UTC)

<p>It’s compiling… but not quite working. I get the same errors described in:</p><aside class="quote quote-modified" data-post="1" data-topic="2339">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/macos-sierra-10-12-6-dynamic-linker-errors/2339">MacOS Sierra (10.12.6) dynamic linker errors</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hey guys, 
I’m running into some dynamic linker errors on startup with master built on 10.12.6: 
dlopen(/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerCropVolumeModuleLogicPython.so, 2): no suitable image found.  Did find:
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./vtkSlicerCropVolumeModuleLogicPython.so: malformed mach-o: load commands size (32872) &gt; 32768
/Users/hherhold/Development/slic…
  </blockquote>
</aside>
<p>
What I understand from this is that the initial pathname has to be short. How short does it need to be? I was compiling from /Users/michaelschumaker/Packages.</p>

---

## Post #21 by @pieper (2018-04-13 16:55 UTC)

<p>Yes, that issue is a pain.  I did my build in /tmp/q5 and didn’t get the path length errors.</p>

---

## Post #22 by @mschumaker (2018-04-13 17:46 UTC)

<p>Thanks. Maybe I’ll try from /usr/local.</p>

---

## Post #23 by @jcfr (2018-04-13 20:07 UTC)

<p>I suggest to avoid /usr/local as it is a system path</p>

---

## Post #24 by @mschumaker (2018-04-13 20:09 UTC)

<p>Ok. That makes sense. Thanks.</p>

---
