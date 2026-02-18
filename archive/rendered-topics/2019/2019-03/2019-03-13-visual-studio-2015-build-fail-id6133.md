# Visual Studio 2015 Build Fail

**Topic ID**: 6133
**Date**: 2019-03-13
**URL**: https://discourse.slicer.org/t/visual-studio-2015-build-fail/6133

---

## Post #1 by @triple_axel (2019-03-13 13:27 UTC)

<p>Machine: Windows 10<br>
Compiler: “Visual Studio 14 2015”<br>
Hi, I am having issues attempting to build the latest stable version of Slicer (Slicer 4.10.1). I have attempted git cloning, configuring, generating, and building 3 times  and I get these same errors, I was wondering if anyone has encountered any before and how to solve them?</p>
<ol>
<li>
<p>Multiple “error 9009” problems:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/681535e6750bb7f2ad99dec7c730b181870c3905.png" data-download-href="/uploads/short-url/eQL6dC21MtMDFAoKs3KxB0lUrdz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/681535e6750bb7f2ad99dec7c730b181870c3905_2_690x189.png" alt="image" data-base62-sha1="eQL6dC21MtMDFAoKs3KxB0lUrdz" width="690" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/681535e6750bb7f2ad99dec7c730b181870c3905_2_690x189.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/681535e6750bb7f2ad99dec7c730b181870c3905_2_1035x283.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/681535e6750bb7f2ad99dec7c730b181870c3905_2_1380x378.png 2x" data-dominant-color="B3D7FC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2226×611 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46d91ba8a82c4243250203cbb8440f71bbbb3d6.png" data-download-href="/uploads/short-url/ujdYr2us5RFyJfv2rcv7SheMI3I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46d91ba8a82c4243250203cbb8440f71bbbb3d6.png" alt="image" data-base62-sha1="ujdYr2us5RFyJfv2rcv7SheMI3I" width="690" height="239" data-dominant-color="FBFBFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1715×595 9.03 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Module machine x86 conflicts with with target machine type x64 for SimpleITK<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52798a7d61c449bce0d455bd9788768c9e5f09b1.png" data-download-href="/uploads/short-url/bLByhpqmeFAI8BCizABojKXgzRv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52798a7d61c449bce0d455bd9788768c9e5f09b1.png" alt="image" data-base62-sha1="bLByhpqmeFAI8BCizABojKXgzRv" width="690" height="236" data-dominant-color="FAFAFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1161×398 4.95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>This CTK issue, with I think has to do with the “error 9009” problems:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/000498cc7e76370d0f6f4b61df69c58267b13539.png" data-download-href="/uploads/short-url/9QCAIgCR7XBMyDAIsBGGpIOet.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/000498cc7e76370d0f6f4b61df69c58267b13539.png" alt="image" data-base62-sha1="9QCAIgCR7XBMyDAIsBGGpIOet" width="690" height="325" data-dominant-color="DBDCDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1056×498 13.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>Thanks a lot!</p>

---

## Post #2 by @lassoan (2019-03-13 13:35 UTC)

<p>You only showed the superbuild result, which does not contain information about why the particular subproject failed to build. Open the .sln file of the <em>first</em> failed subproject and build it to see the actual errors.</p>

---

## Post #3 by @cpinter (2019-03-13 13:43 UTC)

<aside class="quote no-group" data-username="triple_axel" data-post="1" data-topic="6133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>Visual Studio 14 2015</p>
</blockquote>
</aside>
<p>Please make sure that your configuration is actually “Visual Studio 14 2015 Win64”, and not the 32 bit one indicated above.</p>

---

## Post #4 by @triple_axel (2019-03-13 13:56 UTC)

<p>Hi, I built the first subproject (CTKAppLauncherLib) that failed and got this error:</p>
<p>1&gt;------ Build started: Project: CTKAppLauncherLib, Configuration: Release x64 ------<br>
1&gt;  Creating directories for ‘CTKAppLauncherLib’<br>
1&gt;  Building Custom Rule C:/S4/CMakeLists.txt<br>
1&gt;  CMake does not need to re-run because C:/S4R/CMakeFiles/generate.stamp is up-to-date.<br>
1&gt;  Performing download step (git clone) for ‘CTKAppLauncherLib’<br>
1&gt;  – Avoiding repeated git clone, stamp file is up to date: ‘C:/S4R/CTKAppLauncherLib-prefix/src/CTKAppLauncherLib-stamp/CTKAppLauncherLib-gitclone-lastrun.txt’<br>
1&gt;  Performing update step for ‘CTKAppLauncherLib’<br>
1&gt;  No patch step for ‘CTKAppLauncherLib’<br>
1&gt;  Generate version-CTKAppLauncherLib.txt and license-CTKAppLauncherLib.txt<br>
1&gt;  Performing configure step for ‘CTKAppLauncherLib’<br>
1&gt;  loading initial cache file C:/S4R/CTKAppLauncherLib-prefix/tmp/CTKAppLauncherLib-cache-Release.cmake<br>
1&gt;  – Selecting Windows SDK version  to target Windows 10.0.17763.<br>
1&gt;  – CTKAppLauncher version: 0.1.25-gec98a50<br>
1&gt;  – Configuring done<br>
1&gt;  – Generating done<br>
1&gt;  – Build files have been written to: C:/S4R/CTKAppLauncherLib-build<br>
1&gt;  Performing build step for ‘CTKAppLauncherLib’<br>
1&gt;  Microsoft ® Build Engine version 14.0.25420.1<br>
1&gt;  Copyright © Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;    Generating moc_ctkAppLauncherEnvironment.cpp<br>
1&gt;    ‘C:\ProgramFiles’ is not recognized as an internal or external command,<br>
1&gt;    operable program or batch file.<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: “cmd.exe” exited with code 9009. [C:\S4R\CTKAppLauncherLib-build\Base\CTKAppLauncherLib.vcxproj]<br>
========== Build: 0 succeeded, 1 failed, 1 up-to-date, 0 skipped ==========</p>
<p>Additionally, I configured keeping in mind that “x64” must be chosen.</p>

---

## Post #5 by @lassoan (2019-03-13 14:04 UTC)

<aside class="quote no-group" data-username="triple_axel" data-post="4" data-topic="6133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>Generating moc_ctkAppLauncherEnvironment.cpp</p>
</blockquote>
</aside>
<p>Qt moc (meta object compiler) fails. Which Qt version do you use? Where is it installed? Do you have a “C:\ProgramFiles” folder? Can you find <code>ProgramFiles</code> text any of the *.txt, *.cmake, *.in files in the build tree?</p>

---

## Post #6 by @triple_axel (2019-03-13 14:17 UTC)

<p>I installed Qt 5.10.0 x64 and its installed in a folder called “C:\ProgramFiles(x86)”. I do not have a “C:\ProgramFiles” folder.The only other ones I have are “C:\Program Files” and “C\Program Files (x86)”. I will try reinstalling Qt if anything perhaps went wrong with my installation.</p>

---

## Post #7 by @cpinter (2019-03-13 14:28 UTC)

<aside class="quote no-group" data-username="triple_axel" data-post="4" data-topic="6133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>Additionally, I configured keeping in mind that “x64” must be chosen</p>
</blockquote>
</aside>
<p>I think you refer to the build configuration within Visual Studio. It is not enough, you need to make sure the the right configuration is used for CMake. For example</p>
<p><code>cmake -G "Visual Studio 14 2015 Win64" -DQt5_DIR=C:/Qt/5.10.1/msvc2015_64/lib/cmake/Qt5 c:/d/Slicer</code></p>
<p>The moc problem might be related, so please do a completely clean build with fresh CMake configuration and generation, and let us know.</p>

---

## Post #8 by @triple_axel (2019-03-14 16:54 UTC)

<p>After I rebuilt it (keeping in mind that x64 is chosen for my configuration and redownloading qt) I was able to successfully build slicer although 1 subproject failed being "module machine type “x86” conflicted with target machine type “x64” for the Simple-ITK build.</p>
<p>I think the problem was that I previously downloaded a 5.10.0 qt mirror because the qt installer was always failing for me, but I attempted to redownload qt yesterday using the same installer, and it worked just fine.</p>
<p>Thanks for all the help!!</p>

---
