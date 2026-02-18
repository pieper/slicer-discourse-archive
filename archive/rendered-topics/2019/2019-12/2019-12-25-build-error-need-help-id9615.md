# build error need help ?

**Topic ID**: 9615
**Date**: 2019-12-25
**URL**: https://discourse.slicer.org/t/build-error-need-help/9615

---

## Post #1 by @appollosputnik (2019-12-25 18:35 UTC)

<p>Dear Friends</p>
<p>I am building Slicer 3D, and getting one error after building it for 24 hours in my Laptop. Only one error, I am writing the error log below. It seems it is failing with midas3 download. My internet connection is perfect, other downloadable modules are being downloaded perfectly. Only this one is creating problem. May be I am missing some thing with CMake configuration. Please advise what I am missing here.</p>
<p>Any help is highly appreciated.</p>
<p>///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////<br>
46&gt;                       – Fetching “<a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;checksum=32a988e290dcbb1f78e625e514efaba1" rel="nofollow noopener">http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;checksum=32a988e290dcbb1f78e625e514efaba1</a>” (TaskId:126)<br>
46&gt;                       – [download 0% complete] (TaskId:126)<br>
46&gt;                       – [download 1% complete] (TaskId:126)<br>
46&gt;                       – [download 2% complete] (TaskId:126)<br>
46&gt;                       – [download 3% complete] (TaskId:126)<br>
46&gt;                       – [download 4% complete] (TaskId:126)<br>
46&gt;                       – [download 5% complete] (TaskId:126)<br>
46&gt;                       – [download 6% complete] (TaskId:126)<br>
46&gt;                       – [download 7% complete] (TaskId:126)<br>
46&gt;                       – [download 8% complete] (TaskId:126)<br>
46&gt;                       – [download 9% complete] (TaskId:126)<br>
46&gt;                       – [download 10% complete] (TaskId:126)<br>
46&gt;                       – [download 11% complete] (TaskId:126)<br>
46&gt;                       – [download 12% complete] (TaskId:126)<br>
46&gt;                       – [download 13% complete] (TaskId:126)<br>
46&gt;                       – [download 14% complete] (TaskId:126)<br>
46&gt;                       – [download 15% complete] (TaskId:126)<br>
46&gt;                       – [download 16% complete] (TaskId:126)<br>
46&gt;                       – [download 17% complete] (TaskId:126)<br>
46&gt;                       – [download 18% complete] (TaskId:126)<br>
46&gt;                       – [download 19% complete] (TaskId:126)<br>
46&gt;                       – [download 20% complete] (TaskId:126)<br>
46&gt;                       – [download 21% complete] (TaskId:126)<br>
46&gt;                       – [download 22% complete] (TaskId:126)<br>
46&gt;                       – [download 23% complete] (TaskId:126)<br>
46&gt;                       CMake Error at C:/Slicer-master/CMake/ExternalData.cmake:1113 (message): (TaskId:126)<br>
46&gt;                          (TaskId:126)<br>
46&gt;                        (TaskId:126)<br>
46&gt;                         Object MD5=32a988e290dcbb1f78e625e514efaba1 not found at: (TaskId:126)<br>
46&gt;                        (TaskId:126)<br>
46&gt;                           <a href="https://github.com/Slicer/SlicerTestingData/releases/download/MD5/32a988e290dcbb1f78e625e514efaba1" rel="nofollow noopener">https://github.com/Slicer/SlicerTestingData/releases/download/MD5/32a988e290dcbb1f78e625e514efaba1</a> (“Timeout was reached”) (TaskId:126)<br>
46&gt;                           <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;checksum=32a988e290dcbb1f78e625e514efaba1" rel="nofollow noopener">http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;checksum=32a988e290dcbb1f78e625e514efaba1</a> (“Timeout was reached”) (TaskId:126)<br>
46&gt;                        (TaskId:126)<br>
46&gt;                        (TaskId:126)<br>
46&gt;00:42:58.886     1&gt;<br>
46&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: “cmd.exe” exited with code 1. [C:\Slicer-master\build\Slicer-build\SlicerData.vcxproj]<br>
46&gt;                       Configuring application launcher: SlicerDesigner (TaskId:126)<br>
46&gt;                       Building Custom Rule C:/Slicer-master/CMake/LastConfigureStep/CMakeLists.txt (TaskId:126)<br>
46&gt;                       Qt: Untested Windows version 6.2 detected! (TaskId:126)<br>
46&gt;                       Resource ico updated. (TaskId:126)<br>
46&gt;                       Building Custom Rule C:/Slicer-master/Applications/SlicerApp/CMakeLists.txt (TaskId:126)<br>
46&gt;                       Generating SmoothingCLP.h (TaskId:126)<br>
46&gt;                       Building Custom Rule C:/Slicer-master/build/SurfaceToolbox/Smoothing/CMakeLists.txt (TaskId:126)<br>
46&gt;                       GenerateCLP --InputXML C:/Slicer-master/build/SurfaceToolbox/Smoothing/Smoothing.xml --OutputCxx C:/Slicer-master/build/Slicer-build/E/SurfaceToolbox/Smoothing/SmoothingCLP.h (TaskId:126)<br>
46&gt;                       GenerateCLP: Found 1 parameters groups (TaskId:126)<br>
46&gt;                       GenerateCLP: Group “IO” has 6 parameters (TaskId:126)<br>
46&gt;                       Smoothing.cxx (TaskId:126)<br>
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////</p>

---

## Post #2 by @pieper (2019-12-26 15:37 UTC)

<p>The nightly <a href="http://slicer.cdash.org/buildSummary.php?buildid=1783527">builds on the dashboard look good</a>.  Maybe there was a transient issue.  Did you try again?</p>

---

## Post #3 by @appollosputnik (2019-12-29 10:48 UTC)

<p>yes I tried pieper, now I am able to build but in Linux, but getting error when debugging with Qt Creator. when I debug I get the following message</p>
<p>“THE GDB process terminated expectedly (exit code 1)”</p>
<p>Can you tell me what is the possible source of this error.</p>

---

## Post #4 by @pieper (2019-12-29 15:25 UTC)

<p>Did you follow the instructions here?<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtCreator" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtCreator</a></p>

---

## Post #5 by @appollosputnik (2019-12-30 12:00 UTC)

<p>I am trying to build with Qt5.6.0 and Visual studio 2015, with Cmake as the code generator. It is configuring well and generating is also OK. But when I am loading the project in Visual studio, it shows all the CMake files. No source files as in Applications/Main.cxx or other source files are not loaded in Visual studio solution explorer.</p>
<p>Some things is wrong, if I don’t see source files, then how can I debug it. Please help.<br>
I am generating the solution file using CMake.exe as it is described in build instructions in <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a>.</p>
<p>regards</p>

---

## Post #6 by @lassoan (2019-12-31 05:19 UTC)

<aside class="quote no-group" data-username="appollosputnik" data-post="5" data-topic="9615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/appollosputnik/48/5485_2.png" class="avatar"> appollosputnik:</div>
<blockquote>
<p>But when I am loading the project in Visual studio, it shows all the CMake files</p>
</blockquote>
</aside>
<p>Probably you have opened the top-level Slicer.sln file, which builds all the dependencies and then Slicer core. For debugging, you need to open (build-dir)\Slicer-build\Slicer.sln. See more information here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Windows" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/Debug Instructions - Slicer Wiki</a>.</p>

---

## Post #7 by @appollosputnik (2019-12-31 19:46 UTC)

<p>Iassoan, wish you happy new year first of all. But I checked once in Super-build folder, I think there was no sln file. It was all cmake files present inside. ? Are you sure what you’re saying. May be I need generate it once more and check.</p>

---

## Post #8 by @appollosputnik (2020-01-03 05:26 UTC)

<p>Dear Iassoan,</p>
<p>I misread your solution. Yes I followed it now, and able to build and debug the solution. Thanks a lot for your help.</p>
<p>Just one more question, ? How I can do it, in Linux. In Linux I am able to build, and trying to debug using gdb. I am using the command ’ gdb Slicer-build-Debug/Slicer-build/Slicer.exe’</p>
<p>and I am getting message that no debugging symbols found. I am trying to put break points as<br>
‘break Main.cxx : 35’, but it is showing message that no debugging symbols loaded.</p>
<p>If you have any solution, please suggest me.</p>

---

## Post #9 by @lassoan (2020-01-03 06:28 UTC)

<aside class="quote no-group" data-username="appollosputnik" data-post="8" data-topic="9615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/appollosputnik/48/5485_2.png" class="avatar"> appollosputnik:</div>
<blockquote>
<p>How I can do it, in Linux. In Linux I am able to build, and trying to debug using gdb. I am using the command ’ gdb Slicer-build-Debug/Slicer-build/Slicer.exe’</p>
</blockquote>
</aside>
<p>.exe files are Windows executables, so you should not see such files on your linux machine.</p>
<aside class="quote no-group" data-username="appollosputnik" data-post="8" data-topic="9615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/appollosputnik/48/5485_2.png" class="avatar"> appollosputnik:</div>
<blockquote>
<p>I am getting message that no debugging symbols found</p>
</blockquote>
</aside>
<p>See linux debugging instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#GDB_debug_with_launch_arguments" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/Debug Instructions - Slicer Wiki</a></p>

---

## Post #10 by @appollosputnik (2020-01-04 13:27 UTC)

<p>Hi Iassoan</p>
<p>Thanks a lot for all your valuable suggestion. I am now successful in debugging with GDB in Linux. But when I try it with Qt creator I am failing. I am following the steps below.</p>
<p>./Slicer  --launch  /path/to/qtcreator from the build directory, my project is built with make.</p>
<p>//This launches my Qt creator<br>
//Then I am opening the CMakeLists.txt from Slicer folder. And then it configures<br>
//automatically cmake for the project.</p>
<p>Finally it loads the header file, and cmake modules. No source files are being populated.<br>
What am I missing here.?</p>
<p>I still need your help on this. How can load all source files in Qt creator and debug.</p>

---

## Post #11 by @lassoan (2020-01-06 03:27 UTC)

<p>I never use Qt Creator, so I cannot help with that. If you have trouble using Qt Creator for debugging on Linux then you can use Visual Studio Code instead.</p>

---

## Post #12 by @appollosputnik (2020-01-07 08:39 UTC)

<p>Yes Iassoan that could be one possible solution. I will try with visual studio code into qt creator. and then debug.</p>
<p>Anyway, Thanks a lot for this loop of discussion, it is a lot useful. Thanks you very much.</p>

---

## Post #13 by @lassoan (2020-01-07 13:57 UTC)

<aside class="quote no-group" data-username="appollosputnik" data-post="12" data-topic="9615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/appollosputnik/48/5485_2.png" class="avatar"> appollosputnik:</div>
<blockquote>
<p>I will try with visual studio code into qt creator.</p>
</blockquote>
</aside>
<p>I’m not sure what you mean by this but Visual Studio Code has a nice built-in visual debugger that works in Linux.</p>

---

## Post #14 by @appollosputnik (2020-01-09 10:01 UTC)

<p>If I have to use clean Linux then I will prefer GDB, if Qt creator is possible that’s different. But I am OK for now with Visual studio debugger in Windows. I got very valuable break from you. Thanks a lot.</p>

---
