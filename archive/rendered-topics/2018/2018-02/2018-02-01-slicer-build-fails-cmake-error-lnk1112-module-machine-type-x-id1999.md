# Slicer build fails cmake error: LNK1112 module machine type 'X86' conflicts with target machine type 'x64'

**Topic ID**: 1999
**Date**: 2018-02-01
**URL**: https://discourse.slicer.org/t/slicer-build-fails-cmake-error-lnk1112-module-machine-type-x86-conflicts-with-target-machine-type-x64/1999

---

## Post #1 by @drusmanbashir (2018-02-01 13:52 UTC)

<p>Hi,</p>
<p>I am trying to build slicer 4.8 on Windows 7 using:<br>
Visual studio 2013 update 5<br>
CMake 3.10.1<br>
Qt 4.8.7 using easy build option ‘Visual Studio 2013 64-bit Debu<br>
g’:<br>
<span class="mention">@powershell</span> -Command “$destDir=‘C:\D\Support’;$buildType=‘Debug’;$qtPlatform=‘win32-msvc2013’;$bits=‘64’;iex ((new-object net.webclient).DownloadString(‘<a href="https://raw.githubusercontent.com/jcfr/qt-easy-build/4.8.7/windows_build_qt.ps1" rel="nofollow noopener">https://raw.githubusercontent.com/jcfr/qt-easy-build/4.8.7/windows_build_qt.ps1</a>’))”</p>
<p>I had to add Visual studio 2013 native command prompt to the Tools menu of VS 2013 following instructions on this link <a href="https://stackoverflow.com/questions/21476588/where-is-developer-command-prompt-for-vs2013" rel="nofollow noopener">https://stackoverflow.com/questions/21476588/where-is-developer-command-prompt-for-vs2013</a> like so:<br>
/k “C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools\VsDevCmd.bat”</p>
<p>Then i set cmake up with the VS 2013 -64 bit c++ toolkit.<br>
Since, i was building for debuggin, I selected cmake-gui option cmake_configuration_types and deleted all types except ‘Debug’, selected the newly built qmake.exe in the previuos step. Then configuration and generation proceeded</p>
<p>Fired up VS 2013, opened Slicer.sln, in the side-bar right clicked ‘Slicer’ and selected option ‘Set as startup project’ and then did Build.</p>
<p>I don’t see where i selected any x86 build in all of this but it crashes with numerous errors starting with the LNK1112 conflict above, mostly with libraries having Qt in them. Any help will be appreciated.</p>

---

## Post #2 by @jcfr (2018-02-01 14:26 UTC)

<p>Hi <a class="mention" href="/u/drusmanbashir">@drusmanbashir</a>,</p>
<p>Thanks for reporting the issue.</p>
<p>It looks like you built Qt as a 32-bit libraries. Could you confirm you open and built Qt from a <strong>64-bit</strong> windows comment prompt <a href="https://github.com/jcfr/qt-easy-build/tree/4.8.7#readme">to build it</a> ?</p>
<p>This screenshot illustrates what you should check:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c481db74403708d513b9c2c784e2efc31984f013.png" data-download-href="/uploads/short-url/s2nNJ93IYWI7IlmIeM2mGXxvsuD.png?dl=1" title="Screenshot%20from%202018-02-01%2009-24-26"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c481db74403708d513b9c2c784e2efc31984f013_2_690x196.png" alt="Screenshot%20from%202018-02-01%2009-24-26" data-base62-sha1="s2nNJ93IYWI7IlmIeM2mGXxvsuD" width="690" height="196" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c481db74403708d513b9c2c784e2efc31984f013_2_690x196.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c481db74403708d513b9c2c784e2efc31984f013.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c481db74403708d513b9c2c784e2efc31984f013.png 2x" data-dominant-color="101415"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-02-01%2009-24-26</span><span class="informations">970×276 16.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @drusmanbashir (2018-02-01 15:17 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="1999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Qt as a 32-bit lib</p>
</blockquote>
</aside>
<p>I think that is it! It was indeed an x86 command prompt. I am running the build again and hopefully it will work out this time.</p>
<p>I will intend to build slicer again for release later. Can you also tell me how to choose either a debug or a release build in cmake-gui? The only option i can see remotely related is taking the cmake_configuration_types and deleting all entries except for ‘debug’ (or release if I want a release build - though I havent tried a release build yet)</p>

---

## Post #4 by @jcfr (2018-02-01 15:22 UTC)

<aside class="quote no-group" data-username="drusmanbashir" data-post="3" data-topic="1999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drusmanbashir/48/1282_2.png" class="avatar"> drusmanbashir:</div>
<blockquote>
<p>Can you also tell me how to choose either a debug or a release build in cmake-gui?</p>
</blockquote>
</aside>
<p>On windows, you do not select the build type at configuration time. Since IDE like Visual Studio are “multi-configuration”, you will select it from within the IDE.</p>
<p>To avoid ambiguity, you could set the string option <a href="https://cmake.org/cmake/help/latest/variable/CMAKE_CONFIGURATION_TYPES.html">CMAKE_CONFIGURATION_TYPES</a> to <code>Release</code> (or <code>Debug</code>) in cmake-gui.</p>
<p>Doing so, will ensure only one option is available in visual studio. Note that it need to match the build type of the selected path for <code>QT_QMAKE_EXECUTABLE</code></p>

---

## Post #5 by @drusmanbashir (2018-02-01 15:25 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="1999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>do not select the build type</p>
</blockquote>
</aside>
<p>Ok that makes sense. Yes, I will select the relevant qmake (build / release) for the final slicer build. Thanks for sorting this out!</p>

---
