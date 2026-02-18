# The ordinal 4445 could not be located in the dynamic link library libeay32.dll

**Topic ID**: 12251
**Date**: 2020-06-28
**URL**: https://discourse.slicer.org/t/the-ordinal-4445-could-not-be-located-in-the-dynamic-link-library-libeay32-dll/12251

---

## Post #1 by @sunshine_boycn (2020-06-28 11:28 UTC)

<p>Hello, everybody, I recently build the Slicer on Win10. Everything goes fine until I installed some software which might related to SSL.</p>
<p>Now no matter how I rebuild my source code I could successfully build the Slicer.exe on windows but have the error “the ordinal 4445 could not be located in the dynamic link library SD\OpenSSL-INSTALL\Debug\bin\SSLEAY32.dll” and “SD\Slicer-build\bin\Debug\RemoteIO.dll” immediately after I double clicked my program.</p>
<p>Problems exist even I delete the suspected software.</p>
<p>What should I do?</p>

---

## Post #2 by @lassoan (2020-06-28 14:03 UTC)

<p>It looks like that software installed OpenSSL DLLs into Windows system location (most likely somewhere within C:\Windows), which may force applications to use it rather their own. It is possible to install different versions of the same shared DLL in C:\Windows\WinSxS with proper use of manifests, but it is somewhat complicated and still risky, as not all applications may be prepared for that.</p>
<p>Which Slicer version have you built?<br>
Do you have copies of SSLEAY32.dll on your computer anywhere (especially in Windows system folders or in other folders that are listed in your PATH environment variable)?</p>
<p>Possible solutions:</p>
<ul>
<li>If you have OpenSSL libraries in system locations then one solution is to remove them from there. If they are just dumped into an unmanaged folder like c:\Windows\System32 then it is the proper thing to do. If they are found in c:\Windows\WinSxS then you can leave them there and let us know (we could make sure Slicer ignores those).</li>
<li>As a workaround, you can copy all SSL related DLLs into the same folder as SlicerApp-real.exe. This ensures that Slicer will use those.</li>
</ul>

---

## Post #3 by @sunshine_boycn (2020-06-28 15:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>WinSxS</p>
</blockquote>
</aside>
<p>I have tried to search the whole system disk. and there is no ssleay32.dll in either C:\Windows\System32 or C:\Windows\WinSxS. Even the whole  C:\Windows has no ssleay32.dll.</p>
<p>I also tried to copy libeay32.dll and ssleay32.dll to the slicer-build directory with Slicer.exe. It didn’t work. Still the same error.</p>

---

## Post #4 by @lassoan (2020-06-28 16:02 UTC)

<p>It may be a different issue then. Does the most recent Slicer Preview Release work on your computer?</p>
<p>OpenSSL version has been very recently updated in Slicer. If you have your original Slicer build from earlier and then updated your source tree then maybe some parts of Slicer still expect the old version. If a top-level build does not fix the issue then I would recommend a complete rebuild of Slicer from scratch.</p>

---

## Post #5 by @sunshine_boycn (2020-06-29 00:12 UTC)

<p>My slicer’s version is :</p>
<p>Configuring Slicer version [4.11.0-2020-06-23]<br>
Configuring Slicer revision [29173]</p>
<p>When I tried to solve this problem, I would suspect the OpenSSL’s library is wrong during the building process. I tried to output the OpenSSL_LIBRARIES in the CMakeLists.txt which configures the RemoteIO to check whether CMake finds the correct libraries. But the CMake output is hidden during the CMake configuration. My output instruction didn’t work. I can’t verify that the CMake has found the correct OpenSSL_LIBRARIES during the building process.</p>

---

## Post #6 by @sunshine_boycn (2020-06-29 04:39 UTC)

<p>Thank you very much! Problem solved!</p>
<p>The problem is what you have told me that there are OpenSSL binaries in C:\Windows\System32. I didn’t find them before just because I only searched ssleay32.dll rather than libeay32.dll. Currently, Slicer use OpenSSL 1.0.1 and the current OpenSSL is updated to 1.1.1. And most important, it changed its binary name since the version 1.1.1. That is the reason that I missed OpenSSL binaries on my system directory.</p>
<p>I delete the libeay32.dll and libcrypto.dll on the system directory and problem solved.</p>
<p>I also noticed an interesting phenomenon that the Slicer.exe will firstly search the C:\Windows\System32 directory instead of current directory when requiring dll files. The Slicer.exe find the ssleay32.dll on its same directory but missing the libeay32.dll on the same directory. In return it refered to the libeay32.dll on the C:\Windows\System32.</p>
<p>Are there any way to compulsorily link the dll to our required ones?</p>

---

## Post #7 by @lassoan (2020-07-01 01:41 UTC)

<p>Thanks for the update. It is good to hear that the problem is resolved.</p>
<p>Slicer.exe is just a launcher. You need to copy DLLs into the same folder as the actual Slicer executable (SlicerApp-real.exe) is located to ensure preference over Windows system folders.</p>
<p>However, note that Slicer now uses OpenSSL 1.1, so it does not need libeay32.dll or ssleay32.sll. Did you install any extensions or Python packages? Probably they require an older OpenSSL version.</p>

---
