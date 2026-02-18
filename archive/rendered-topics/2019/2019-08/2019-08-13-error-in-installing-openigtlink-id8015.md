# Error in installing OpenIGTLink

**Topic ID**: 8015
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/error-in-installing-openigtlink/8015

---

## Post #1 by @ahmed_elshreif (2019-08-13 19:59 UTC)

<p>I use windows 10 with amd64 what is the version of the Cmake that should I use and which generator to use with is like the attached image <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5e0b9f9b1affa8b609c184a199b41bce51b5f07.png" data-download-href="/uploads/short-url/sevxe2OLPdtAiJ1a8VoAQnrHfGD.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5e0b9f9b1affa8b609c184a199b41bce51b5f07.png" alt="1" data-base62-sha1="sevxe2OLPdtAiJ1a8VoAQnrHfGD" width="507" height="367"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">507×367 4.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also after that I how tyo compile the sln as I tried to compile it with diffrent versions of Visual studio but I don’t get the 2 files that is needed as the build instructions here say:</p>
<p><a href="https://github.com/openigtlink/OpenIGTLink/blob/master/BUILD.md" rel="noopener nofollow ugc">github.com</a></p>
<h4><a name="p-28100-openigtlinkopenigtlinkblobmasterbuildmdhttpsgithubcomopenigtlinkopenigtlinkblobmasterbuildmd-1" class="anchor" href="#p-28100-openigtlinkopenigtlinkblobmasterbuildmdhttpsgithubcomopenigtlinkopenigtlinkblobmasterbuildmd-1" aria-label="Heading link"></a><a href="https://github.com/openigtlink/OpenIGTLink/blob/master/BUILD.md" rel="noopener nofollow ugc">openigtlink/OpenIGTLink/blob/master/BUILD.md</a></h4>
<pre><code class="lang-auto">The OpenIGTLink Library Build Instruction
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
<p>This file has been truncated. <a href="https://github.com/openigtlink/OpenIGTLink/blob/master/BUILD.md" rel="noopener nofollow ugc">show original</a></p>
<p>Also this is the logs of the configration and I don’t know whats wrong</p>
<p>Selecting Windows SDK version 10.0.14393.0 to target Windows 10.0.18362.<br>
The C compiler identification is MSVC 19.0.24215.1<br>
The CXX compiler identification is MSVC 19.0.24215.1<br>
Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe<br>
Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe – works<br>
Detecting C compiler ABI info<br>
Detecting C compiler ABI info - done<br>
Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe<br>
Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe – works<br>
Detecting CXX compiler ABI info<br>
Detecting CXX compiler ABI info - done<br>
Detecting CXX compile features<br>
Detecting CXX compile features - done<br>
Looking for pthread.h<br>
Looking for pthread.h - not found<br>
Found Threads: TRUE<br>
Looking for getsockname in socket<br>
Looking for getsockname in socket - not found<br>
Checking for getsockname with socklen_t<br>
Checking for getsockname with socklen_t – no<br>
Looking for strnlen<br>
Looking for strnlen - found<br>
Looking for SO_REUSEADDR<br>
Looking for SO_REUSEADDR - not found<br>
Looking for sys/types.h<br>
Looking for sys/types.h - found<br>
Looking for stdint.h<br>
Looking for stdint.h - found<br>
Looking for stddef.h<br>
Looking for stddef.h - found<br>
Check size of int<br>
Check size of int - done<br>
Check size of long<br>
Check size of long - done<br>
Check size of void*<br>
Check size of void* - done<br>
Check size of char<br>
Check size of char - done<br>
Check size of short<br>
Check size of short - done<br>
Check size of float<br>
Check size of float - done<br>
Check size of double<br>
Check size of double - done<br>
Check size of long long<br>
Check size of long long - done<br>
Check size of __int64<br>
Check size of __int64 - done<br>
Check size of int64_t<br>
Check size of int64_t - done<br>
CMake Warning (dev) at C:/Devel/OpenIGTLink_build/OpenIGTLinkConfig.cmake:67 (include):<br>
Policy CMP0024 is not set: Disallow include export result. Run “cmake<br>
–help-policy CMP0024” for policy details. Use the cmake_policy command to<br>
set the policy and suppress this warning.</p>
<p>The file</p>
<pre><code class="lang-auto">C:/Devel/OpenIGTLink_build/OpenIGTLinkTargets.cmake
</code></pre>
<p>was generated by the export() command. It should not be used as the<br>
argument to the include() command. Use ALIAS targets instead to refer to<br>
targets by alternative names.</p>
<p>Call Stack (most recent call first):<br>
Testing/CMakeLists.txt:4 (find_package)<br>
This warning is for project developers. Use -Wno-dev to suppress it.</p>
<p>– Selecting Windows SDK version 10.0.14393.0 to target Windows 10.0.18362.</p>
<p>– Configuring done</p>
<p>– Generating done</p>
<p>– Build files have been written to: C:/Devel/OpenIGTLink_build/Testing/googletest-download</p>
<p>Microsoft ® Build Engine version 14.0.25420.1<br>
Copyright © Microsoft Corporation. All rights reserved.</p>
<p>Build started 8/12/2019 12:55:01 PM.</p>
<p>Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj” on node 1 (default targets).</p>
<p>Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj” (1) is building “C:\Devel\OpenIGTLink_build\Testing\googletest-download\ZERO_CHECK.vcxproj” (2) on node 1 (default targets).<br>
PrepareForBuild:</p>
<p>Creating directory “x64\Debug\ZERO_CHECK”.</p>
<p>Creating directory “x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog”.</p>
<p>InitializeBuildStatus:</p>
<p>Creating “x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild” because “AlwaysCreate” was specified.</p>
<p>CustomBuild:</p>
<p>Checking Build System</p>
<p>CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.</p>
<p>FinalizeBuildStatus:</p>
<p>Deleting file “x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild”.</p>
<p>Touching “x64\Debug\ZERO_CHECK\ZERO_CHECK.tlog\ZERO_CHECK.lastbuildstate”.</p>
<p>Done Building Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\ZERO_CHECK.vcxproj” (default targets).</p>
<p>Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj” (1) is building “C:\Devel\OpenIGTLink_build\Testing\googletest-download\googlemock.vcxproj” (3) on node 1 (default targets).</p>
<p>PrepareForBuild:<br>
Creating directory “x64\Debug\googlemock”.</p>
<p>Creating directory “x64\Debug\googlemock\googlemock.tlog”.</p>
<p>InitializeBuildStatus:</p>
<p>Creating “x64\Debug\googlemock\googlemock.tlog\unsuccessfulbuild” because “AlwaysCreate” was specified.</p>
<p>ComputeCustomBuildOutput:</p>
<p>Creating directory “C:\Devel\OpenIGTLink_build\Testing\googletest-download\googlemock-prefix\src\googlemock-stamp\Debug”.</p>
<p>Creating directory “C:\Devel\OpenIGTLink_build\Testing\googletest-download\CMakeFiles\Debug”.</p>
<p>CustomBuild:</p>
<p>Creating directories for ‘googlemock’</p>
<p>Building Custom Rule C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeLists.txt</p>
<p>CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.</p>
<p>Performing download step (download, verify and extract) for ‘googlemock’</p>
<p>– Downloading…</p>
<pre><code class="lang-auto"> dst='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googlemock-prefix/src/release-1.7.0.zip'
 timeout='none'
</code></pre>
<p>– Using src=‘<a href="https://github.com/google/googlemock/archive/release-1.7.0.zip%E2%80%99" rel="noopener nofollow ugc">https://github.com/google/googlemock/archive/release-1.7.0.zip’</a></p>
<p>– [download 1% complete]</p>
<p>– [download 2% complete]</p>
<p>– [download 4% complete]</p>
<p>– [download 5% complete]</p>
<p>– [download 8% complete]</p>
<p>– [download 11% complete]</p>
<p>– [download 14% complete]</p>
<p>– [download 15% complete]</p>
<p>– [download 16% complete]</p>
<p>– [download 20% complete]</p>
<p>– [download 24% complete]</p>
<p>– [download 26% complete]</p>
<p>– [download 30% complete]</p>
<p>– [download 35% complete]</p>
<p>– [download 38% complete]</p>
<p>– [download 50% complete]</p>
<p>– [download 54% complete]</p>
<p>– [download 56% complete]</p>
<p>– [download 57% complete]</p>
<p>– [download 58% complete]</p>
<p>– [download 61% complete]</p>
<p>– [download 62% complete]</p>
<p>– [download 65% complete]</p>
<p>– [download 68% complete]</p>
<p>– [download 72% complete]</p>
<p>– [download 73% complete]</p>
<p>– [download 82% complete]</p>
<p>– [download 91% complete]</p>
<p>– [download 100% complete]</p>
<p>– Downloading… done</p>
<p>– extracting…</p>
<pre><code class="lang-auto">   src='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googlemock-prefix/src/release-1.7.0.zip'
   dst='C:/Devel/OpenIGTLink_build/Testing/gmock'
</code></pre>
<p>– extracting… [tar xfz]</p>
<p>– extracting… [analysis]</p>
<p>– extracting… [rename]</p>
<p>– extracting… [clean up]</p>
<p>– extracting… done</p>
<p>No update step for ‘googlemock’</p>
<p>No patch step for ‘googlemock’</p>
<p>No configure step for ‘googlemock’</p>
<p>No build step for ‘googlemock’</p>
<p>No install step for ‘googlemock’</p>
<p>No test step for ‘googlemock’</p>
<p>Completed ‘googlemock’</p>
<p>FinalizeBuildStatus:</p>
<p>Deleting file “x64\Debug\googlemock\googlemock.tlog\unsuccessfulbuild”.</p>
<p>Touching “x64\Debug\googlemock\googlemock.tlog\googlemock.lastbuildstate”.</p>
<p>Done Building Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\googlemock.vcxproj” (default targets).</p>
<p>Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj” (1) is building “C:\Devel\OpenIGTLink_build\Testing\googletest-download\googletest.vcxproj” (4) on node 1 (default targets).</p>
<p>PrepareForBuild:<br>
Creating directory “x64\Debug\googletest”.</p>
<p>Creating directory “x64\Debug\googletest\googletest.tlog”.</p>
<p>InitializeBuildStatus:</p>
<p>Creating “x64\Debug\googletest\googletest.tlog\unsuccessfulbuild” because “AlwaysCreate” was specified.</p>
<p>ComputeCustomBuildOutput:</p>
<p>Creating directory “C:\Devel\OpenIGTLink_build\Testing\googletest-download\googletest-prefix\src\googletest-stamp\Debug”.</p>
<p>CustomBuild:</p>
<p>Creating directories for ‘googletest’</p>
<p>Building Custom Rule C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeLists.txt</p>
<p>CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.</p>
<p>Performing download step (download, verify and extract) for ‘googletest’</p>
<p>– Downloading…</p>
<pre><code class="lang-auto"> dst='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googletest-prefix/src/release-1.7.0.zip'
 timeout='none'
</code></pre>
<p>– Using src=‘<a href="https://github.com/google/googletest/archive/release-1.7.0.zip%E2%80%99" rel="noopener nofollow ugc">https://github.com/google/googletest/archive/release-1.7.0.zip’</a></p>
<p>– [download 0% complete]</p>
<p>– [download 2% complete]</p>
<p>– [download 4% complete]</p>
<p>– [download 5% complete]</p>
<p>– [download 6% complete]</p>
<p>– [download 7% complete]</p>
<p>– [download 8% complete]</p>
<p>– [download 10% complete]</p>
<p>– [download 12% complete]</p>
<p>– [download 13% complete]</p>
<p>– [download 15% complete]</p>
<p>– [download 18% complete]</p>
<p>– [download 20% complete]</p>
<p>– [download 23% complete]</p>
<p>– [download 25% complete]</p>
<p>– [download 29% complete]</p>
<p>– [download 32% complete]</p>
<p>– [download 33% complete]</p>
<p>– [download 34% complete]</p>
<p>– [download 35% complete]</p>
<p>– [download 36% complete]</p>
<p>– [download 37% complete]</p>
<p>– [download 40% complete]</p>
<p>– [download 42% complete]</p>
<p>– [download 43% complete]</p>
<p>– [download 46% complete]</p>
<p>– [download 56% complete]</p>
<p>– [download 61% complete]</p>
<p>– [download 64% complete]</p>
<p>– [download 66% complete]</p>
<p>– [download 69% complete]</p>
<p>– [download 72% complete]</p>
<p>– [download 79% complete]</p>
<p>– [download 87% complete]</p>
<p>– [download 90% complete]</p>
<p>– [download 97% complete]</p>
<p>– [download 100% complete]</p>
<p>– Downloading… done</p>
<p>– extracting…</p>
<pre><code class="lang-auto">   src='C:/Devel/OpenIGTLink_build/Testing/googletest-download/googletest-prefix/src/release-1.7.0.zip'
   dst='C:/Devel/OpenIGTLink_build/Testing/gtest'
</code></pre>
<p>– extracting… [tar xfz]</p>
<p>– extracting… [analysis]</p>
<p>– extracting… [rename]</p>
<p>– extracting… [clean up]</p>
<p>– extracting… done</p>
<p>No update step for ‘googletest’</p>
<p>No patch step for ‘googletest’</p>
<p>No configure step for ‘googletest’</p>
<p>No build step for ‘googletest’</p>
<p>No install step for ‘googletest’</p>
<p>No test step for ‘googletest’</p>
<p>Completed ‘googletest’</p>
<p>FinalizeBuildStatus:</p>
<p>Deleting file “x64\Debug\googletest\googletest.tlog\unsuccessfulbuild”.</p>
<p>Touching “x64\Debug\googletest\googletest.tlog\googletest.lastbuildstate”.</p>
<p>Done Building Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\googletest.vcxproj” (default targets).</p>
<p>PrepareForBuild:</p>
<p>Creating directory “x64\Debug\ALL_BUILD”.</p>
<p>Creating directory “x64\Debug\ALL_BUILD\ALL_BUILD.tlog”.</p>
<p>InitializeBuildStatus:</p>
<p>Creating “x64\Debug\ALL_BUILD\ALL_BUILD.tlog\unsuccessfulbuild” because “AlwaysCreate” was specified.</p>
<p>CustomBuild:</p>
<p>Building Custom Rule C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeLists.txt</p>
<p>CMake does not need to re-run because C:/Devel/OpenIGTLink_build/Testing/googletest-download/CMakeFiles/generate.stamp is up-to-date.</p>
<p>FinalizeBuildStatus:</p>
<p>Deleting file “x64\Debug\ALL_BUILD\ALL_BUILD.tlog\unsuccessfulbuild”.</p>
<p>Touching “x64\Debug\ALL_BUILD\ALL_BUILD.tlog\ALL_BUILD.lastbuildstate”.</p>
<p>Done Building Project “C:\Devel\OpenIGTLink_build\Testing\googletest-download\ALL_BUILD.vcxproj” (default targets).</p>
<p>Build succeeded.</p>
<pre><code class="lang-auto">0 Warning(s)
0 Error(s)
</code></pre>
<p>Time Elapsed 00:00:03.70</p>
<p>Found PythonInterp: C:/Users/diigi/Anaconda2/python.exe (found version “2.7.15”)<br>
Configuring done</p>

---

## Post #2 by @jamesobutler (2019-08-13 20:35 UTC)

<p>A response was added to your original thread where this same message was posted.</p><aside class="quote" data-post="13" data-topic="7854">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/real-time-visualization/7854/13">Real Time Visualization</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/ahmed_elshreif">@ahmed_elshreif</a> Your OpenIGTLink build succeeded as evident by the following: 
Build succeeded.

0 Warning(s)
0 Error(s)

igtlSocketTest.cxx is currently <a href="https://github.com/openigtlink/OpenIGTLink/blob/eb71a36a0603db4971771738b4afde63a034c596/Testing/CMakeLists.txt#L59-L61" rel="noopener nofollow ugc">commented out</a> from the OpenIGTLinkTesting project. Someone had a similar issue and the developer that previously spent a lot of time on the project responded <a href="https://github.com/openigtlink/OpenIGTLink/issues/187#issuecomment-398576462" rel="noopener nofollow ugc">here</a>. As you have noticed the build instructions are not completely up-to-date, however you have built the project successfully.
  </blockquote>
</aside>


---

## Post #3 by @ahmed_elshreif (2019-08-14 17:22 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="8015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>onse was added to your original thread where this same message was posted.</p>
<p><span alt="" role="presentation" class="broken-image" title="This image is broken"><svg class="fa d-icon d-icon-unlink svg-icon" aria-hidden="true"><use href="#unlink"></use></svg></span> <a href="https://discourse.slicer.org/t/real-time-visualization/7854/13">Real Time Visualization</a> <a href="/c/support">Support</a></p>
</blockquote>
</aside>
<p>how can I run this example or start using the OpenIGTLink in sending data to the slicer?</p>

---
