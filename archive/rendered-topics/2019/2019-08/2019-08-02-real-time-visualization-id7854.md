---
topic_id: 7854
title: "Real Time Visualization"
date: 2019-08-02
url: https://discourse.slicer.org/t/7854
---

# Real Time Visualization

**Topic ID**: 7854
**Date**: 2019-08-02
**URL**: https://discourse.slicer.org/t/real-time-visualization/7854

---

## Post #1 by @ahmed_elshreif (2019-08-02 20:13 UTC)

<p>Hello all,</p>
<p>I am using a Software for OCT that send me a real time frames that it takes and I want to use Slicer to make a real time 3D object Visualization. I need to modify in my software to open Slicer and start sending data feme by frame and start to view the 3D while time.</p>
<p>The problem that I don’t know how to interface with Slicer to make it do this from the Code or how to deal with slicer in real time.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-08-02 20:21 UTC)

<p>Slicer can receive real-time data through <a href="http://openigtlink.org/" rel="nofollow noopener">OpenIGTLink</a>, a very simple socket-based protocol. Image display, processing, sequence recording/replay, etc. are all already implemented. You can learn more about these features in <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a>.</p>
<p>We typically use <a href="https://www.plustoolkit.org" rel="nofollow noopener">PLUS toolkit</a> to receive image streams from various imaging devices. It may be usable for you as is, if you plan to acquire image from the OCT using a framegrabber. PLUS can also acquire data from various optical, electromagnetic, and other position trackers and reconstruct 3D volumes from 2D image slices in real-time.</p>

---

## Post #3 by @ahmed_elshreif (2019-08-05 20:38 UTC)

<p>Could you explain more how can I use this and generate the 3D object by sending my 2D frames.</p>

---

## Post #4 by @lassoan (2019-08-06 01:13 UTC)

<p>Until recently, volume reconstruction was always performed by PlusServer, see demo below and step-by-step instructions in <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a>:</p>
<div class="lazyYT" data-youtube-id="lfZeXabDjMg" data-youtube-title="Live ultrasound volume reconstruction in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>In recent Slicer versions, you can reconstruct volumes in Slicer process, too. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can provide more details if you need this.</p>

---

## Post #5 by @ahmed_elshreif (2019-08-07 15:48 UTC)

<p>I have a device that not supported by the Plus tool here<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html" class="onebox" target="_blank" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html</a></p>
<p>So I need to send frames from the code and I Can’t find how to make this. The code generate frame by frame and if I have a API that I can use it to send the frame and make volume reconstruction this will be great.</p>
<p>Sorry for to many questions.</p>

---

## Post #6 by @lassoan (2019-08-07 17:24 UTC)

<p>You can implement <a href="http://www.openigtlink.org" rel="nofollow noopener">OpenIGTLink</a> protocol to send real-time image, transform, point, etc. data to Slicer. There are <a href="http://openigtlink.org/developers/" rel="nofollow noopener">libraries for C++, Python, Java, Matlab</a> that can help implementing sending of OpenIGTLink messages. You may also add a new device to Plus toolkit (by cloning and modifying source code of a similar device).</p>

---

## Post #7 by @ahmed_elshreif (2019-08-08 22:53 UTC)

<p>Can you help me in this issue<br>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/openigtlink/MatlabIGTL/issues/2" target="_blank" rel="nofollow noopener">github.com/openigtlink/MatlabIGTL</a>
  </header>
  <article class="onebox-body">
    <a href="https://github.com/EL-SHREIF" rel="nofollow noopener">
<img src="https://avatars1.githubusercontent.com/u/36492402?v=2&amp;s=96" class="thumbnail onebox-avatar" width="60" height="60">
</a>

<h4><a href="https://github.com/openigtlink/MatlabIGTL/issues/2" target="_blank" rel="nofollow noopener">Issue: Error while building</a></h4>

<div class="date" style="margin-top:10px;">
	<div class="user" style="margin-top:10px;">
	opened by <a href="https://github.com/EL-SHREIF" target="_blank" rel="nofollow noopener">EL-SHREIF</a>
	on <a href="https://github.com/openigtlink/MatlabIGTL/issues/2" target="_blank" rel="nofollow noopener">2019-08-08</a>
	</div>
	<div class="user">
	</div>
</div>

<pre class="content" style="white-space: pre-wrap;">I tried to put the relative address like this :
OpenIGTLink Library
IGTLSRC= ../OpenIGTMatlab/OpenIGTLink
IGTLBLD= ../OpenIGTMatlab/build
for Matlab
MEX = ../../Program Files/MATLAB/R2019a/interprocess/bin/win64/mex
MEXOPT =




















































I got this error
C:\Devel\MatlabIGTL&gt;make
/Program...</pre>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #8 by @lassoan (2019-08-09 17:45 UTC)

<p>I would not try to use mex files. Instead, you may try native Matlab implementations of OpenIGTLink, such as this: <a href="https://github.com/SlicerIGT/MatlabOpenIGTLink" rel="nofollow noopener">https://github.com/SlicerIGT/MatlabOpenIGTLink</a></p>
<p>We migrated all our projects from Matlab to Python, so we cannot help much with these Matlab implementations anymore. However, if Python is an option for you then we can definitely help you with that.</p>

---

## Post #9 by @ahmed_elshreif (2019-08-09 21:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="7854">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>migrated all our projects from Matlab to Python, so we cannot help much with these Matlab implementations anymore. However, if Python is an option for you then we can definitely help you with that.</p>
</blockquote>
</aside>
<p>actually my project is with cpp and now I just want any easy tool to make a prototype then I will work on the integration with the cpp software.</p>
<p>So if you can help in python I could make the prototype with it it’s fine to make this.</p>
<p>Also I see in one of your comments that there is a team in vanderbilt that work with this tool as I am in vanderbilt so can you tell me who to ask ?</p>
<p>Thanks</p>

---

## Post #10 by @ahmed_elshreif (2019-08-09 21:20 UTC)

<p>Also this : <a href="https://github.com/SlicerIGT/MatlabOpenIGTLink" rel="nofollow noopener">https://github.com/SlicerIGT/MatlabOpenIGTLink</a> in for only STRING, TRANSFORM and NDArray(1D Float Array) messages and I have a volume which is collection of 2D images .</p>

---

## Post #11 by @lassoan (2019-08-10 13:03 UTC)

<p>There have been several OpenIGTLink Matlab implementations, some of them able to transfer images, too, but if you need C++ then you can use this SDK: <a href="https://github.com/openigtlink/OpenIGTLink" rel="nofollow noopener">https://github.com/openigtlink/OpenIGTLink</a>. It has C++ examples that you can use as “prototypes” as is.</p>
<p>There is a small native Python OpenIGTLink implementation, which already supports a few basic message types: <a href="https://github.com/SlicerIGT/pyIGTLink" rel="nofollow noopener">https://github.com/SlicerIGT/pyIGTLink</a>.</p>

---

## Post #12 by @ahmed_elshreif (2019-08-12 17:55 UTC)

<p>I use windows 10 with amd64 what is the version of the Cmake that should I use and which generator to use with is like the attached image <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5e0b9f9b1affa8b609c184a199b41bce51b5f07.png" alt="1" data-base62-sha1="sevxe2OLPdtAiJ1a8VoAQnrHfGD" width="507" height="367"></p>
<p>Also after that I how tyo compile the sln as I tried to compile it with diffrent versions of Visual studio but I don’t get the 2 files that is needed as the build instructions here say:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/openigtlink/OpenIGTLink/blob/master/BUILD.md">
  <header class="source">

      <a href="https://github.com/openigtlink/OpenIGTLink/blob/master/BUILD.md" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/OpenIGTLink/blob/master/BUILD.md" target="_blank" rel="noopener nofollow ugc">openigtlink/OpenIGTLink/blob/master/BUILD.md</a></h4>


      <pre><code class="lang-md">The OpenIGTLink Library Build Instruction
=========================================

Linux / Mac OS X
----------------

First, obtain the source code from the repository using Git. To simply download
the code, run the following command from a terminal:

~~~~
$ git clone https://github.com/openigtlink/OpenIGTLink.git
~~~~

Then configure using CMake. The library requires CMake version higher than 2.4.

~~~~
$ mkdir OpenIGTLink-build
$ cd OpenIGTLink-build
$ cmake -DBUILD_EXAMPLES:BOOL=ON ../OpenIGTLink
$ make
</code></pre>



  This file has been truncated. <a href="https://github.com/openigtlink/OpenIGTLink/blob/master/BUILD.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also this is the logs of the configration and I don’t know whats wrong</p>
<details>
<summary>
Configuration log</summary>
<pre><code>Selecting Windows SDK version 10.0.14393.0 to target Windows 10.0.18362.
The C compiler identification is MSVC 19.0.24215.1
The CXX compiler identification is MSVC 19.0.24215.1
Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe
Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe -- works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe
Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Detecting CXX compile features
Detecting CXX compile features - done
Looking for pthread.h
Looking for pthread.h - not found
Found Threads: TRUE  
Looking for getsockname in socket
Looking for getsockname in socket - not found
Checking for getsockname with socklen_t
Checking for getsockname with socklen_t -- no
Looking for strnlen
Looking for strnlen - found
Looking for SO_REUSEADDR
Looking for SO_REUSEADDR - not found
Looking for sys/types.h
Looking for sys/types.h - found
Looking for stdint.h
Looking for stdint.h - found
Looking for stddef.h
Looking for stddef.h - found
Check size of int
Check size of int - done
Check size of long
Check size of long - done
Check size of void*
Check size of void* - done
Check size of char
Check size of char - done
Check size of short
Check size of short - done
Check size of float
Check size of float - done
Check size of double
Check size of double - done
Check size of long long
Check size of long long - done
Check size of __int64
Check size of __int64 - done
Check size of int64_t
Check size of int64_t - done
CMake Warning (dev) at C:/Devel/OpenIGTLink_build/OpenIGTLinkConfig.cmake:67 (include):
  Policy CMP0024 is not set: Disallow include export result.  Run "cmake
  --help-policy CMP0024" for policy details.  Use the cmake_policy command to
  set the policy and suppress this warning.

  The file

    C:/Devel/OpenIGTLink_build/OpenIGTLinkTargets.cmake

  was generated by the export() command.  It should not be used as the
  argument to the include() command.  Use ALIAS targets instead to refer to
  targets by alternative names.

Call Stack (most recent call first):
  Testing/CMakeLists.txt:4 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Selecting Windows SDK version 10.0.14393.0 to target Windows 10.0.18362.

-- Configuring done

-- Generating done

-- Build files have been written to: C:/Devel/OpenIGTLink_build/Testing/googletest-download

Microsoft (R) Build Engine version 14.0.25420.1
Copyright (C) Microsoft Corporation. All rights reserved.


Build started 8/12/2019 12:55:01 PM.

Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj" on node 1 (default targets).

Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj" (1) is building "C:\Devel\OpenIGTLink_build\Testing\googletest-download\ZERO_CHECK.vcxproj" (2) on node 1 (default targets).
PrepareForBuild:

  Creating directory "x64\Debug\ZERO_CHECK\".

  Creating directory "x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog\".

InitializeBuildStatus:

  Creating "x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.

CustomBuild:

  Checking Build System

  CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.

FinalizeBuildStatus:

  Deleting file "x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild".

  Touching "x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog\ZERO_CHECK.lastbuildstate".

Done Building Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\ZERO_CHECK.vcxproj" (default targets).

Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj" (1) is building "C:\Devel\OpenIGTLink_build\Testing\googletest-download\googlemock.vcxproj" (3) on node 1 (default targets).

PrepareForBuild:
  Creating directory "x64\Debug\googlemock\".

  Creating directory "x64\Debug\googlemock\googlemock.tlog\".

InitializeBuildStatus:

  Creating "x64\Debug\googlemock\googlemock.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.

ComputeCustomBuildOutput:

  Creating directory "C:\Devel\OpenIGTLink_build\Testing\googletest-download\googlemock-prefix\src\googlemock-stamp\Debug\".

  Creating directory "C:\Devel\OpenIGTLink_build\Testing\googletest-download\CMakeFiles\Debug\".

CustomBuild:

  Creating directories for 'googlemock'

  Building Custom Rule C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeLists.txt

  CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.

  Performing download step (download, verify and extract) for 'googlemock'

  -- Downloading...

     dst='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googlemock-prefix/src/release-1.7.0.zip'
     timeout='none'

  -- Using src='https://github.com/google/googlemock/archive/release-1.7.0.zip'

  -- [download 1% complete]

  -- [download 2% complete]

  -- [download 4% complete]

  -- [download 5% complete]

  -- [download 8% complete]

  -- [download 11% complete]

  -- [download 14% complete]

  -- [download 15% complete]

  -- [download 16% complete]

  -- [download 20% complete]

  -- [download 24% complete]

  -- [download 26% complete]

  -- [download 30% complete]

  -- [download 35% complete]

  -- [download 38% complete]

  -- [download 50% complete]

  -- [download 54% complete]

  -- [download 56% complete]

  -- [download 57% complete]

  -- [download 58% complete]

  -- [download 61% complete]

  -- [download 62% complete]

  -- [download 65% complete]

  -- [download 68% complete]

  -- [download 72% complete]

  -- [download 73% complete]

  -- [download 82% complete]

  -- [download 91% complete]

  -- [download 100% complete]

  -- Downloading... done

  -- extracting...

       src='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googlemock-prefix/src/release-1.7.0.zip'
       dst='C:/Devel/OpenIGTLink_build/Testing/gmock'

  -- extracting... [tar xfz]

  -- extracting... [analysis]

  -- extracting... [rename]

  -- extracting... [clean up]

  -- extracting... done

  No update step for 'googlemock'

  No patch step for 'googlemock'

  No configure step for 'googlemock'

  No build step for 'googlemock'

  No install step for 'googlemock'

  No test step for 'googlemock'

  Completed 'googlemock'

FinalizeBuildStatus:

  Deleting file "x64\Debug\googlemock\googlemock.tlog\unsuccessfulbuild".

  Touching "x64\Debug\googlemock\googlemock.tlog\googlemock.lastbuildstate".

Done Building Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\googlemock.vcxproj" (default targets).

Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj" (1) is building "C:\Devel\OpenIGTLink_build\Testing\googletest-download\googletest.vcxproj" (4) on node 1 (default targets).

PrepareForBuild:
  Creating directory "x64\Debug\googletest\".

  Creating directory "x64\Debug\googletest\googletest.tlog\".

InitializeBuildStatus:

  Creating "x64\Debug\googletest\googletest.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.

ComputeCustomBuildOutput:

  Creating directory "C:\Devel\OpenIGTLink_build\Testing\googletest-download\googletest-prefix\src\googletest-stamp\Debug\".

CustomBuild:

  Creating directories for 'googletest'

  Building Custom Rule C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeLists.txt

  CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.

  Performing download step (download, verify and extract) for 'googletest'

  -- Downloading...

     dst='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googletest-prefix/src/release-1.7.0.zip'
     timeout='none'

  -- Using src='https://github.com/google/googletest/archive/release-1.7.0.zip'

  -- [download 0% complete]

  -- [download 2% complete]

  -- [download 4% complete]

  -- [download 5% complete]

  -- [download 6% complete]

  -- [download 7% complete]

  -- [download 8% complete]

  -- [download 10% complete]

  -- [download 12% complete]

  -- [download 13% complete]

  -- [download 15% complete]

  -- [download 18% complete]

  -- [download 20% complete]

  -- [download 23% complete]

  -- [download 25% complete]

  -- [download 29% complete]

  -- [download 32% complete]

  -- [download 33% complete]

  -- [download 34% complete]

  -- [download 35% complete]

  -- [download 36% complete]

  -- [download 37% complete]

  -- [download 40% complete]

  -- [download 42% complete]

  -- [download 43% complete]

  -- [download 46% complete]

  -- [download 56% complete]

  -- [download 61% complete]

  -- [download 64% complete]

  -- [download 66% complete]

  -- [download 69% complete]

  -- [download 72% complete]

  -- [download 79% complete]

  -- [download 87% complete]

  -- [download 90% complete]

  -- [download 97% complete]

  -- [download 100% complete]

  -- Downloading... done

  -- extracting...

       src='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googletest-prefix/src/release-1.7.0.zip'
       dst='C:/Devel/OpenIGTLink_build/Testing/gtest'

  -- extracting... [tar xfz]

  -- extracting... [analysis]

  -- extracting... [rename]

  -- extracting... [clean up]

  -- extracting... done

  No update step for 'googletest'

  No patch step for 'googletest'

  No configure step for 'googletest'

  No build step for 'googletest'

  No install step for 'googletest'

  No test step for 'googletest'

  Completed 'googletest'

FinalizeBuildStatus:

  Deleting file "x64\Debug\googletest\googletest.tlog\unsuccessfulbuild".

  Touching "x64\Debug\googletest\googletest.tlog\googletest.lastbuildstate".

Done Building Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\googletest.vcxproj" (default targets).

PrepareForBuild:

  Creating directory "x64\Debug\ALL_BUILD\".

  Creating directory "x64\Debug\ALL_BUILD\ALL_BUILD.tlog\".

InitializeBuildStatus:

  Creating "x64\Debug\ALL_BUILD\ALL_BUILD.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.

CustomBuild:

  Building Custom Rule C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeLists.txt

  CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.

FinalizeBuildStatus:

  Deleting file "x64\Debug\ALL_BUILD\ALL_BUILD.tlog\unsuccessfulbuild".

  Touching "x64\Debug\ALL_BUILD\ALL_BUILD.tlog\ALL_BUILD.lastbuildstate".

Done Building Project "C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj" (default targets).



Build succeeded.

    0 Warning(s)
    0 Error(s)


Time Elapsed 00:00:03.70

Found PythonInterp: C:/Users/diigi/Anaconda2/python.exe (found version "2.7.15") 
Configuring done
</code></pre>
</details>

---

## Post #13 by @jamesobutler (2019-08-13 20:34 UTC)

<p><a class="mention" href="/u/ahmed_elshreif">@ahmed_elshreif</a> Your OpenIGTLink build succeeded as evident by the following:</p>
<pre><code class="lang-auto">Build succeeded.

0 Warning(s)
0 Error(s)
</code></pre>
<p>igtlSocketTest.cxx is currently <a href="https://github.com/openigtlink/OpenIGTLink/blob/eb71a36a0603db4971771738b4afde63a034c596/Testing/CMakeLists.txt#L59-L61" rel="nofollow noopener">commented out</a> from the OpenIGTLinkTesting project. Someone had a similar issue and the developer that previously spent a lot of time on the project responded <a href="https://github.com/openigtlink/OpenIGTLink/issues/187#issuecomment-398576462" rel="nofollow noopener">here</a>. As you have noticed the build instructions are not completely up-to-date, however you have built the project successfully.</p>

---
