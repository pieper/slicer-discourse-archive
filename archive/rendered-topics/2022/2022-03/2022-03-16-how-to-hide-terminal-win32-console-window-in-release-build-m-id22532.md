---
topic_id: 22532
title: "How To Hide Terminal Win32 Console Window In Release Build M"
date: 2022-03-16
url: https://discourse.slicer.org/t/22532
---

# How to hide terminal(WIN32_CONSOLE) window in release build mode?

**Topic ID**: 22532
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/how-to-hide-terminal-win32-console-window-in-release-build-mode/22532

---

## Post #1 by @Dhaval (2022-03-16 03:47 UTC)

<p>I build  release mode. When i run Slicer, it still have terminal window. How to hide terminal in release build mode?( Windows 10)</p>
<p>Slicer_BUILD_WIN32_CONSOLE = OFF  (But the terminal still exists.)</p>

---

## Post #2 by @lassoan (2022-03-16 19:54 UTC)

<p>Check out the application options in CMake:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/CMake/SlicerApplicationOptions.cmake#L47-L48">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/CMake/SlicerApplicationOptions.cmake#L47-L48" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/CMake/SlicerApplicationOptions.cmake#L47-L48" target="_blank" rel="noopener">Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/CMake/SlicerApplicationOptions.cmake#L47-L48</a></h4>



    <pre class="onebox">      <code class="lang-cmake">
        <ol class="start lines" start="47" style="counter-reset: li-counter 46 ;">
            <li>option(Slicer_BUILD_WIN32_CONSOLE "Build ${PROJECT_NAME} executable as a console app on windows (allows capturing console output)" ON)</li>
            <li>option(Slicer_BUILD_WIN32_CONSOLE_LAUNCHER "Build ${PROJECT_NAME} launcher executable as a console app on windows (displays console at application start)" ON)</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><code>Slicer_BUILD_WIN32_CONSOLE</code> controls if Slicer executable (SlicerApp-real.exe) is a console application or not. You need to turn off <code>Slicer_BUILD_WIN32_CONSOLE_LAUNCHER</code> if you don’t want to see the console.</p>

---

## Post #3 by @zhang_ming (2022-08-09 09:56 UTC)

<p>I set this OFF, then run cmake gui again, but still exeists.</p>

---

## Post #4 by @lassoan (2022-08-09 10:05 UTC)

<p>Make sure you build ALL_BUILD target in the top-level Slicer.sln with the correct configuration (Release, Debug,…) and that Slicer.exe is not running (do not use <code>Slicer.exe --VisualStudio</code> to start Visual Studio for this build l, just simply open the .sln file by double-clicking on it).</p>

---

## Post #5 by @zhang_ming (2022-08-09 09:50 UTC)

<p><span class="hashtag-raw">#-----------------------------------------------------------------------------</span></p>
<h1><a name="p-81897-terminal-support-1" class="anchor" href="#p-81897-terminal-support-1" aria-label="Heading link"></a>Terminal support</h1>
<p><span class="hashtag-raw">#-----------------------------------------------------------------------------</span><br>
if(WIN32)<br>
option(Slicer_BUILD_WIN32_CONSOLE “Build ${PROJECT_NAME} executable as a console app on windows (allows capturing console output)” OFF)<br>
option(Slicer_BUILD_WIN32_CONSOLE_LAUNCHER “Build ${PROJECT_NAME} launcher executable as a console app on windows (displays console at application start)” OFF)</p>
<p>and I have turned off the option</p>

---

## Post #6 by @zhang_ming (2022-08-09 13:03 UTC)

<p>I’m realllly sure, I make the this code to turn off console:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/CMake/SlicerApplicationOptions.cmake#L47-L48" rel="noopener nofollow ugc">Slicer/SlicerApplicationOptions.cmake at 8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3 · Slicer/Slicer (github.com)</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3ba3e01443df937a79accc6f350eae1cbfbd559e.png" data-download-href="/uploads/short-url/8vBgRwaPRmA39GtYr4guxO0NoQK.png?dl=1" title="20220809210011" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba3e01443df937a79accc6f350eae1cbfbd559e_2_690x106.png" alt="20220809210011" data-base62-sha1="8vBgRwaPRmA39GtYr4guxO0NoQK" width="690" height="106" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba3e01443df937a79accc6f350eae1cbfbd559e_2_690x106.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba3e01443df937a79accc6f350eae1cbfbd559e_2_1035x159.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba3e01443df937a79accc6f350eae1cbfbd559e_2_1380x212.png 2x" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20220809210011</span><span class="informations">1574×242 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then redo cmake gui operation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7190321a99413ef6f68a68980a96201b0dfc94.png" data-download-href="/uploads/short-url/mBEKpfeQV93iT2tv8PHFTsBPF1W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7190321a99413ef6f68a68980a96201b0dfc94.png" alt="image" data-base62-sha1="mBEKpfeQV93iT2tv8PHFTsBPF1W" width="690" height="107" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1551×241 6.38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>then follow the steps:<br>
configure<br>
generate<br>
open sln<br>
package</p>
<p>but still can’t hide console</p>

---

## Post #7 by @jamesobutler (2022-08-09 13:09 UTC)

<p>I’m not entirely sure if you can do an incremental build to update from having console ON to then having it be OFF. You could always try a completely fresh build with the appropriate configuration set to OFF and then build.</p>

---

## Post #8 by @zhang_ming (2022-08-09 13:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78115dc5f60257bbecaf67e62f1698a962f5f235.png" data-download-href="/uploads/short-url/h8avdMbQbzvsWuo43OLdMsDmDfT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78115dc5f60257bbecaf67e62f1698a962f5f235.png" alt="image" data-base62-sha1="h8avdMbQbzvsWuo43OLdMsDmDfT" width="690" height="286" data-dominant-color="E8E7E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×290 7.67 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I found the flag Slicer_BUILD_QTLOADABLEMODULES everywhere even in <strong>Release</strong> folder ,to change the value of default <strong>ON</strong> to <strong>OFF</strong>. then clean and rebuild this, failed. still console appeared, what a shame, so I will try build from scratch , thank you</p>

---

## Post #9 by @cpinter (2022-08-09 14:10 UTC)

<p>My experience is that this flag only applies for installed packages. While you run Slicer from your build tree you will see the console. However, if you generate a package and install it, the console does not appear if you had the flag off when building.</p>

---

## Post #10 by @zhang_ming (2022-08-09 14:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f414f2780f2052da89d650a517b1b2a305935199.png" data-download-href="/uploads/short-url/yPfnFN41M1TennoQ5jVrphyTU6Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f414f2780f2052da89d650a517b1b2a305935199_2_690x169.png" alt="image" data-base62-sha1="yPfnFN41M1TennoQ5jVrphyTU6Z" width="690" height="169" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f414f2780f2052da89d650a517b1b2a305935199_2_690x169.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f414f2780f2052da89d650a517b1b2a305935199.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f414f2780f2052da89d650a517b1b2a305935199.png 2x" data-dominant-color="E9EEEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×210 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>should this be True?</p>

---

## Post #11 by @zhang_ming (2022-08-09 22:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I build from scratch, and even set this two args False, but the release version still have the console window. I’m wondering something in detail the docs may ignored to describe?</p>

---

## Post #12 by @lassoan (2022-08-11 20:11 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="22532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>My experience is that this flag only applies for installed packages. While you run Slicer from your build tree you will see the console.</p>
</blockquote>
</aside>
<p>I’ve checked the <a href="https://github.com/Slicer/Slicer/blob/da82798ad4fbcddd38e4dcb883ce9cf37615cc79/CMake/SlicerMacroBuildApplication.cmake#L688-L716">implementation</a> and this is indeed the case. <code>c:\D\S4R\Slicer-build\Slicer.exe</code> is always a console application. This is useful for development, as you can see the process output while you are running Slicer or tests.</p>
<p>If you set <code>Slicer_BUILD_WIN32_CONSOLE_LAUNCHER</code> variable to <code>OFF</code> in CMake, then configure, generate, build the project, and then build the <code>PACKAGE</code> target, then <code>Slicer.exe</code> in the install package will be created by copying <code>c:\D\S4R\CTKAPPLAUNCHER\bin\CTKAppLauncherW.exe</code> (while the flag is <code>ON</code> then the <code>c:\D\S4R\CTKAPPLAUNCHER\bin\CTKAppLauncher.exe</code> file is copied).</p>

---

## Post #13 by @pieper (2022-08-11 20:37 UTC)

<p>Then if there’s a need you should be able to easily switch between launcher types by just copying and renaming the executables with no rebuild required.</p>

---
