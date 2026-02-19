---
topic_id: 12964
title: "Openssl 1 1 1 Packaging Problem Libcrypto 1 1 X64 Dll Not Fo"
date: 2020-08-12
url: https://discourse.slicer.org/t/12964
---

# OpenSSL 1.1.1 packaging problem - libcrypto-1_1-x64.dll not found

**Topic ID**: 12964
**Date**: 2020-08-12
**URL**: https://discourse.slicer.org/t/openssl-1-1-1-packaging-problem-libcrypto-1-1-x64-dll-not-found/12964

---

## Post #1 by @cpinter (2020-08-12 13:11 UTC)

<p>Hi all,</p>
<p>I updated Slicer under a custom app after several months, and the generated installer wouldn’t start up, because <code>libcrypto-1_1-x64.dll</code> was not found.</p>
<p>It seems that in the new version of OpenSSL (1.1.1g) Slicer uses, the DLLs have different names, and maybe there are some differences in packaging that were not addressed? What is strange is that <code>libssl-1_1-x64.dll</code> is in the NSIS directory, but only <code>libcrypto-1_1-x64.dll</code> is not. If I manually copy the DLL from <code>Superbuild\OpenSSL-install\Release\bin</code> into the installed app’s bin directory, then it starts up fine.</p>
<p>I was not able to find where the install step for these DLLs are, and where this should be fixed. Does anyone have an idea? Thanks a lot!</p>

---

## Post #2 by @lassoan (2020-08-12 15:18 UTC)

<p>Yes, OpenSSL library names have completely changed in the new version. Both libcrypto-1_1-x64.dll and  libssl-1_1-x64.dll are correctly installed in latest Slicer Preview Releases.</p>
<p>Have you built your custom application completely from scratch?</p>

---

## Post #3 by @cpinter (2020-08-12 15:20 UTC)

<p>Yes I believe that I built it clean after changing the Slicer hash and not before. In any case I’ll do another clean build to make sure that this is the case.</p>

---

## Post #4 by @cpinter (2020-08-12 16:33 UTC)

<p>I packaged the Slicer (currently one commit behind, <a href="https://github.com/Slicer/Slicer/commit/077adec82e1fefc8c6ec38887fb8e306af1db987">this hash</a>) that I built (clean) locally with default CMake parameters except for disabled SimpleITK, and I have the same issue there: <code>libssl-1_1-x64.dll</code>  is in the NSIS directory, but <code>libcrypto-1_1-x64.dll</code> is not.</p>

---

## Post #5 by @lassoan (2020-08-13 13:17 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Do you have similar issues with your custom applications?</p>

---

## Post #6 by @cpinter (2020-08-13 13:19 UTC)

<p>Please see my last comment. This occurs with my local Slicer build as well, not just the custom app!</p>
<p>I’m not sure if there is a CMake parameter that is set in the factory build but not mine (as I said I use all defaults except that I disable SimpleITK). Or if there is anything specific to my environment that could cause this.</p>

---

## Post #7 by @lassoan (2020-08-13 13:59 UTC)

<p>In my regular Slicer build, I have both libcrypto-1_1-x64.dll and libssl-1_1-x64.dll in c:\D\S4R\Slicer-build_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-08-11-win-amd64\bin.</p>
<p>I haven’t disabled SimpleITK, but I would not expect that to make any difference. I’ll start a clean build with the latest master and see if I get the same result.</p>
<p>What Qt version and compiler version do you use? Do you have any third-party antivirus?<br>
Do you have both DLLs listed in c:\D\S4R\Slicer-build_CPack_Packages\win-amd64\NSIS\project.nsi?</p>

---

## Post #8 by @cpinter (2020-08-13 14:05 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a> for checking it!</p>
<p>I use Qt 5.15.0, VS 2019 with its default toolset, and I don’t use third party antivirus.</p>
<p>In <code>project.nsi</code> I only have <code>libssl-1_1-x64.dll</code>. So this is a difference.</p>

---

## Post #9 by @pieper (2020-08-13 14:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="12964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ll start a clean build with the latest master and see if I get the same result.</p>
</blockquote>
</aside>
<p>In case you want to experiment with getting a faster build, the 224 core cloud machine is available with windows for $16 hour <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @lassoan (2020-08-13 21:07 UTC)

<p>I’ve completed a clean build on my desktop from the latest master version, with Qt-5.15, with v140 toolset (for some reason this was still used in my build batch file), and both libraries were installed.</p>
<p>I’ve started another build using v142 toolset on another computer and will report back when I get the result.</p>

---

## Post #11 by @lassoan (2020-08-14 02:17 UTC)

<p>Clean build is complete on my other computer, too, and it has libcrypto, too.</p>
<p>I have reference to libcrypto in the following files:</p>
<pre><code class="lang-auto">c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\project.nsi 
c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-08-13-win-amd64\bin\Qt5Network.dll
c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-08-13-win-amd64\bin\Qt5WebEngineCore.dll
c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-08-13-win-amd64\lib\Python\Lib\ctypes\util.py
c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-08-13-win-amd64\lib\Python\Lib\lib-dynload\_hashlib.pyd
c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-08-13-win-amd64\lib\Python\Lib\lib-dynload\_ssl.pyd
c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-08-13-win-amd64\lib\Slicer-4.11\RemoteIO.dll 
c:\D\S4R\Slicer-build\bin\Release\RemoteIO.dll 
c:\D\S4R\Slicer-build\CMake\LastConfigureStep\cmake_install.cmake 
c:\D\S4R\Slicer-build\CMakeCache.txt 
c:\D\S4R\Slicer-build\install_manifest_Runtime.txt 
c:\D\S4R\Slicer-build\SlicerConfig.cmake 
c:\D\S4R\Slicer-build\SlicerTargets.cmake 
</code></pre>
<p>It seems that RemoteIO, curl, Qt, and/or some Python packages bring in the crypto dll as dependency.</p>

---

## Post #12 by @cpinter (2020-08-14 14:04 UTC)

<p>Thanks Andras! I did a clean build and packaging on my other computer, and it’s fine there. I’ll try to see the difference between the two environments. Maybe I have an OpenSSL installation by some other program that confuses the package script?</p>

---
