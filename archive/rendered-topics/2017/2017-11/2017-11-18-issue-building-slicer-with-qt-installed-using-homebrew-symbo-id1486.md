# Issue building Slicer with Qt installed using Homebrew: Symbol not found: __cg_jpeg_resync_to_restart

**Topic ID**: 1486
**Date**: 2017-11-18
**URL**: https://discourse.slicer.org/t/issue-building-slicer-with-qt-installed-using-homebrew-symbol-not-found-cg-jpeg-resync-to-restart/1486

---

## Post #1 by @Fernando (2017-11-18 18:00 UTC)

<p>Hi all,</p>
<p>I’m trying to build Slicer on my macOS Sierra 10.12.6 with this configuration:</p>
<pre><code class="lang-auto">cmake -DCMAKE_BUILD_TYPE:STRING=Release -DQT_QMAKE_EXECUTABLE:FILEPATH=/usr/local/Cellar/qt@4/4.8.7_2/bin/qmake -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.12 -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF ../Slicer
make -j8
</code></pre>
<p>But I get a build error (last 10 lines):</p>
<pre><code class="lang-auto">[100%] Built target SimpleITK
[ 96%] Performing install step for 'SimpleITK'
-- SimpleITK: Removing 'install' log files
-- SimpleITK: SimpleITK_WORKING_DIR: /Users/fernando/git/Slicer-SuperBuild-Release/SimpleITK-build/SimpleITK-build/Wrapping/Python
-- SimpleITK: /Users/fernando/git/Slicer-SuperBuild-Release/python-install/bin/SlicerPython;Packaging/setup.py;install
-- SimpleITK: 'install' step successfully completed.
[ 97%] Completed 'SimpleITK'
[ 97%] Built target SimpleITK
make: *** [all] Error 2
</code></pre>
<p>Here’s the complete output: <a href="https://www.dropbox.com/s/ankxbk4fx9n513w/build_log.txt.gz?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/ankxbk4fx9n513w/build_log.txt.gz?dl=0</a></p>
<p>Do you know what can be wrong? Please let me know if you need any other details about my system or the build.</p>
<p>Thanks,<br>
Fernando</p>

---

## Post #2 by @jcfr (2017-11-18 18:51 UTC)

<p>Hi,</p>
<p>Thanks for the report.</p>
<p>Would it be possible to re-upload the complete log ? The provided link ends up with a 404 error.</p>
<p>Jc</p>

---

## Post #3 by @Fernando (2017-11-18 19:06 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>Excuse me, I’ve edited my link. Can you try again?</p>

---

## Post #4 by @jcfr (2017-11-18 19:40 UTC)

<p>Looking at the log, we can see the following errors:</p>
<pre><code class="lang-auto">-- Looking for decorator header ctkVisualizationVTKWidgetsPythonQtDecorators.h
-- Looking for decorator header ctkVisualizationVTKWidgetsPythonQtDecorators.h - Found
dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /usr/local/lib/libJPEG.dylib
 in /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /usr/local/lib/libJPEG.dylib
 in /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
-- Looking for decorator header ctkQtTestingPythonQtDecorators.h
-- Looking for decorator header ctkQtTestingPythonQtDecorators.h - Not found
-- Found PythonLibs: /Users/fernando/git/Slicer-SuperBuild-Release/python-install/lib/libpython2.7.dylib (found version "2.7.13")
dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /usr/local/lib/libJPEG.dylib
 in /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /usr/local/lib/libJPEG.dylib
 in /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
CMake Warning at /usr/local/Cellar/cmake/3.9.6/share/cmake/Modules/FindDoxygen.cmake:396 (message):
  Unable to determine doxygen version: Child aborted
Call Stack (most recent call first):
  /usr/local/Cellar/cmake/3.9.6/share/cmake/Modules/FindDoxygen.cmake:551 (_Doxygen_find_doxygen)
  Documentation/CMakeLists.txt:1 (find_package)


dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /usr/local/lib/libJPEG.dylib
 in /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
CMake Error at /usr/local/Cellar/cmake/3.9.6/share/cmake/Modules/FindDoxygen.cmake:630 (message):
  Unable to generate Doxyfile template: Child aborted
Call Stack (most recent call first):
  Documentation/CMakeLists.txt:1 (find_package)


-- Configuring incomplete, errors occurred!
See also "/Users/fernando/git/Slicer-SuperBuild-Release/CTK-build/CTK-build/CMakeFiles/CMakeOutput.log".
See also "/Users/fernando/git/Slicer-SuperBuild-Release/CTK-build/CTK-build/CMakeFiles/CMakeError.log".
</code></pre>
<p>There are two issues:</p>
<ul>
<li>(1) Doxygen: Unable to generate Doxyfile template: Child aborted</li>
<li>(2) Symbol not found: __cg_jpeg_resync_to_restart</li>
</ul>
<p>The issue (1) should be easy to address by fixing the install of Doxygen.</p>
<p>For the issue (2), it is discussed in  <a href="https://issues.slicer.org/view.php?id=3574">https://issues.slicer.org/view.php?id=3574</a> and was fixed.</p>
<p>The known workaround was to specify <code>-DSlicer_USE_SYSTEM_QT:BOOL=1</code>, then a fix was implemented in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26193">r26193</a>.</p>
<p>The problem is that the fix didn’t account for path starting with <code>/usr/local/Cellar</code>, this is now fixed in master.</p>
<p>See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26646">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26646</a></p>

---

## Post #5 by @Fernando (2017-11-19 14:04 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> for looking into this.</p>
<p>I did:</p>
<pre><code class="lang-auto">git -C ../Slicer pull
brew uninstall doxygen
brew install doxygen
cmake -DCMAKE_BUILD_TYPE:STRING=Release -DQT_QMAKE_EXECUTABLE:FILEPATH=/usr/local/Cellar/qt@4/4.8.7_2/bin/qmake -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.12 -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF ../Slicer
make -j8
</code></pre>
<p>But the build was unsuccessful again. I couldn’t find “<code>doxygen</code>” or “<code>__cg_jpeg_resync_to_restart</code>” in log: <a href="https://www.dropbox.com/s/3yg6d4n97dw9stj/build_log.txt.gz?dl=0" rel="nofollow noopener">Dropbox link to log</a></p>

---

## Post #6 by @jcfr (2017-11-19 14:58 UTC)

<p>Hi Fernando,</p>
<p>Look like you didn’t do a clean build. I suggest you first delete the build<br>
tree.</p>
<p>Hth<br>
Jc</p>

---

## Post #7 by @Fernando (2017-11-19 17:41 UTC)

<p>Do you mean removing everything from my <code>Slicer-SuperBuild-Release</code> dir before configuring and building? I just tried that with no luck.</p>

---

## Post #8 by @jcfr (2017-11-19 22:34 UTC)

<p>Hi,</p>
<p>Look like there is no errors in the last log. What make you think it failed ?  Is the log complete ?</p>
<p>Jc</p>

---

## Post #9 by @Fernando (2017-11-20 11:52 UTC)

<p>I think the export of my log was somehow wrong (I tried using <code>tee</code>). This time I just copied and pasted it: <a href="https://www.dropbox.com/s/o0teidq8nvckanf/build_log.txt.gz?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/o0teidq8nvckanf/build_log.txt.gz?dl=0</a></p>
<p>The <code>doxygen</code> and <code>__cg_jpeg_resync_to_restart</code> errors are still present.</p>
<p>What can I do? Maybe install Doxygen and Qt4 in a different way?</p>

---

## Post #10 by @jcfr (2017-11-21 19:43 UTC)

<p>It would be helpful if could narrow down which project is failing.</p>
<p>Only typing <code>make</code> will now stop to the first project having issue.</p>
<p>It looks like there is still some clash between system and brew libraries.</p>
<p>Could you also:</p>
<ul>
<li>
<p>check what is the content of <code>python-install/bin/SlicerPythonLauncherSettings.ini</code> ?</p>
</li>
<li>
<p>comment out CMake code trying to find and use Doxygen. Look like there is issues with the one shipped by brew.</p>
</li>
</ul>

---

## Post #11 by @Fernando (2017-11-21 20:12 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="1486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Only typing make will now stop to the first project having issue.</p>
</blockquote>
</aside>
<p>What do you mean? Can I narrow the search if I run <code>make</code> again in from the same folder?</p>
<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="1486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>comment out CMake code</p>
</blockquote>
</aside>
<p>I wouldn’t know where to start commenting CMake code, I don’t know almost anything about it. Would it help if I install Doxygen in a different way?</p>
<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="1486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>what is the content of python-install/bin/SlicerPythonLauncherSettings.ini ?</p>
</blockquote>
</aside>
<pre><code class="lang-auto"> Slicer-SuperBuild-Release  cat python-install/bin/SlicerPythonLauncherSettings.ini
[General]
launcherNoSplashScreen=true
launcherSplashImagePath=
launcherSplashScreenHideDelayMs=
additionalLauncherHelpShortArgument=
additionalLauncherHelpLongArgument=
additionalLauncherNoSplashArguments=
additionalPathVariables=PYTHONPATH



[Application]
path=&lt;APPLAUNCHER_DIR&gt;//python
arguments=
name=SlicerPython
revision=
organizationDomain=
organizationName=

[ExtraApplicationToLaunch]


[LibraryPaths]
1\path=/Users/fernando/git/Slicer-SuperBuild-Release/python-install/lib
2\path=/Users/fernando/git/Slicer-SuperBuild-Release/OpenSSL
size=2

[Paths]
1\path=&lt;APPLAUNCHER_DIR&gt;
size=1

[EnvironmentVariables]
PYTHONHOME=/Users/fernando/git/Slicer-SuperBuild-Release/python-install
PYTHONNOUSERSITE=1
SSL_CERT_FILE=&lt;APPLAUNCHER_DIR&gt;/../../Slicer-build/share/Slicer-4.9/Slicer.crt



[PYTHONPATH]
1\path=/Users/fernando/git/Slicer-SuperBuild-Release/python-install/lib/python2.7
2\path=/Users/fernando/git/Slicer-SuperBuild-Release/python-install/lib/python2.7/lib-dynload
3\path=/Users/fernando/git/Slicer-SuperBuild-Release/python-install/lib/python2.7/site-packages
size=3
</code></pre>

---

## Post #12 by @Fernando (2017-11-21 20:21 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="1486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Only typing make will now stop to the first project having issue.</p>
</blockquote>
</aside>
<p>I just ran <code>make -j8</code>, here’s the output: <a href="https://gist.github.com/fepegar/a6a2e7b4395fb081b5ac24c3a94e7619" rel="noopener nofollow ugc">https://gist.github.com/fepegar/a6a2e7b4395fb081b5ac24c3a94e7619</a></p>

---

## Post #13 by @jcfr (2017-11-21 20:33 UTC)

<h3><a name="p-6207-launcher-settings-1" class="anchor" href="#p-6207-launcher-settings-1" aria-label="Heading link"></a>Launcher settings</h3>
<blockquote>
<p>python-install/bin/SlicerPythonLauncherSettings.ini</p>
</blockquote>
<p>Everything looks fine, there is no system paths listed.</p>
<h3><a name="p-6207-doxygen-2" class="anchor" href="#p-6207-doxygen-2" aria-label="Heading link"></a>Doxygen</h3>
<aside class="quote no-group" data-username="Fernando" data-post="11" data-topic="1486">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Doxygen in a different way</p>
</blockquote>
</aside>
<p>I have no idea, I am not familiar with brew.</p>
<p>Slicer <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26653">r26653</a> introduces the option <code>Slicer_BUILD_DOCUMENTATION</code>, consider updating your source checkout and configuring with <code>-DSlicer_BUILD_DOCUMENTATION:BOOL=OFF</code></p>
<h2><a name="p-6207-single-process-make-to-find-out-cause-of-failure-3" class="anchor" href="#p-6207-single-process-make-to-find-out-cause-of-failure-3" aria-label="Heading link"></a>Single process make to find out cause of failure</h2>
<aside class="quote no-group" data-username="Fernando" data-post="11" data-topic="1486">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>What do you mean? Can I narrow the search if I run make again in from the same folder?</p>
</blockquote>
</aside>
<p>By simply running <code>make</code> I meant that you should run a single process <code>make</code>.</p>
<p>From the top level directory, try:</p>
<pre data-code-wrap="bash"><code class="lang-bash">cd Slicer-SuperBuild
make
</code></pre>
<p>instead of</p>
<pre data-code-wrap="bash"><code class="lang-bash">cd Slicer-SuperBuild
make -j&lt;number&gt;
</code></pre>
<p>Doing so ensure the build process fails at the first error.</p>
<p>When you know which target is faulty, it is useful to do:</p>
<pre><code class="lang-auto">make NameOfTarget/fast VERBOSE=1
</code></pre>
<p>this will give a lot more details</p>

---

## Post #14 by @Fernando (2017-11-21 22:30 UTC)

<p>When I run <code>make</code>, the last lines of the output are:</p>
<pre><code class="lang-auto">[ 13%] Performing build step for 'python'
[  0%] Built target extension_array
[  1%] Built target extension_audioop
[  1%] Built target extension_bisect
[  2%] Built target extension_cmath
[  2%] Built target extension_codecs_cn
[  3%] Built target extension_codecs_hk
[  4%] Built target extension_codecs_iso2022
[  5%] Built target extension_codecs_jp
[  5%] Built target extension_codecs_kr
[  6%] Built target extension_codecs_tw
[  7%] Built target extension_cPickle
[  8%] Built target extension_cStringIO
[  9%] Built target extension_csv
[  9%] Built target extension_ctypes_test
[  9%] Built target extension_functools
[ 10%] Built target extension_future_builtins
[ 10%] Built target extension_heapq
[ 11%] Built target extension_hotshot
[ 12%] Built target extension_itertools
[ 13%] Built target extension_json
[ 13%] Built target extension_locale
[ 14%] Built target extension_lsprof
[ 15%] Built target extension_math
[ 16%] Built target extension_mmap
[ 17%] Built target extension_multibytecodec
[ 18%] Built target extension_operator
[ 19%] Built target extension_parser
[ 19%] Built target extension_random
[ 20%] Built target extension_strop
[ 20%] Built target extension_struct
[ 21%] Built target extension_testcapi
[ 21%] Built target extension_unicodedata
[ 22%] Built target extension_fcntl
[ 23%] Built target extension_grp
[ 24%] Built target extension_resource
[ 25%] Built target extension_syslog
[ 26%] Built target extension_termios
make[5]: *** No rule to make target `/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/SystemConfiguration.framework', needed by `lib/python2.7/lib-dynload/_scproxy.so'.  Stop.
make[4]: *** [CMakeBuild/extensions/extension_scproxy/CMakeFiles/extension_scproxy.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [python-prefix/src/python-stamp/python-build] Error 2
make[1]: *** [CMakeFiles/python.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>So I ran <code>make python/fast VERBOSE=1</code> and got this: <a href="https://gist.github.com/fepegar/a6a2e7b4395fb081b5ac24c3a94e7619" rel="nofollow noopener">https://gist.github.com/fepegar/a6a2e7b4395fb081b5ac24c3a94e7619</a></p>

---

## Post #15 by @jcfr (2017-11-22 00:38 UTC)

<p>Thanks for the details.</p>
<p>Since I am travelling until Sunday, unless someone else help you out. I<br>
will have a look next week.</p>

---

## Post #16 by @ihnorton (2017-11-22 03:24 UTC)

<aside class="quote no-group quote-modified" data-username="Fernando" data-post="14" data-topic="1486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>`/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/SystemConfiguration.framework’</p>
</blockquote>
</aside>
<p>Does this path exist? Note that the SDK and the OS version can be different, and Apple updater may have automatically moved you up to 10.13 SDK (this happened to me, things broke, and I manually rolled back – haven’t dared to try again yet).</p>

---

## Post #17 by @Fernando (2017-11-22 09:57 UTC)

<p>Hi <a class="mention" href="/u/ihnorton">@ihnorton</a>,</p>
<p>I think that has happened to me as well. How did you roll back?</p>

---

## Post #18 by @ihnorton (2017-11-22 10:39 UTC)

<p>I think the issue I hit has been fixed because I know some other Mac users<br>
have upgraded — I didn’t want the hours of rebuilding. So try setting the<br>
sdk target to 10.13 first. I don’t have the rollback steps I used at hand,<br>
but will try to find again.</p>

---

## Post #19 by @jcfr (2017-11-27 14:12 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Thanks for your input</p>
<p><a class="mention" href="/u/fernando">@Fernando</a> Was the issue finally resolved ?</p>

---
