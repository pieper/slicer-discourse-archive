---
topic_id: 542
title: "Cli Linking Error"
date: 2017-06-20
url: https://discourse.slicer.org/t/542
---

# CLI linking error

**Topic ID**: 542
**Date**: 2017-06-20
**URL**: https://discourse.slicer.org/t/cli-linking-error/542

---

## Post #1 by @prisgdd (2017-06-20 19:19 UTC)

<p>I am currently trying to package my extension with Qt scripted modules and CLI modules.<br>
The packaging process is successfull. Then, when I use the CLI, I have the following linking error:</p>
<blockquote>
<p>dyld: Library not loaded: <span class="mention">@rpath</span>/lib/Slicer-4.7/libITKFactoryRegistration.dylib<br>
Referenced from: /Users/prisgdd/ShapeVariationAnalyzer-build/_CPack_Packages/ShapeVariationAnalyzer/lib/Slicer-4.7/hidden-cli-modules/./computemean<br>
Reason: image not found<br>
Trace/BPT trap: 5</p>
</blockquote>
<p>Any suggestion on how to solve that?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2017-06-20 20:10 UTC)

<p>How do you package your extension?<br>
How do you attempt to run the CLI?<br>
Does the CLI work in Slicer if you <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Installing_an_extension_without_network_connection">install the extension from generated extension package file</a>?</p>

---

## Post #3 by @prisgdd (2017-06-20 20:29 UTC)

<p>I have a recently built Slicer on my computer, so I’m building my extension giving Slicer’s directory.<br>
<code>cmake -DSlicer_DIR=/path/to/Slicer-SuperBuild/Slicer-build -DCMAKE_OSX_ARCHITECTURES=x86_64 -DCMAKE_OSX_SYSROOT=&lt;sdkroot&gt; -DCMAKE_OSX_DEPLOYMENT_TARGET=&lt;deploy-target&gt; -DCMAKE_BUILD_TYPE=Release ../ShapeVariationAnalyzer</code></p>
<p>Then, I add the path to my extension’s modules (cli and qt scripted) and tried to run the CLI with the button dedicated to do so on my extension but also loading the cli-module in Slicer. Both actions gave the same issue.<br>
I tried to install the extension from the generated extension package file but it says it can’t copy the source folder to the destination folder and it aborts the process.</p>

---

## Post #4 by @lassoan (2017-06-20 20:56 UTC)

<p>It may be possible that the executables stored in the created extension package only work with an installed Slicer. So, either try running Slicer from the build tree and use binaries of your extension from the build tree; or install Slicer and install your extension from file.<br>
You can read a bit more about CMake’s RPATH handling <a href="https://cmake.org/Wiki/CMake_RPATH_handling">here</a>.</p>
<p>I don’t use MacOSX, so I cannot give any further help, but <a class="mention" href="/u/pieper">@pieper</a> or other Mac users should be able to give more information.</p>

---

## Post #5 by @pieper (2017-06-20 22:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> may be right about the extension only running from an install try.  Did you try making an installed version of your local mac build?</p>
<p>Run <code>make package</code> from the Slicer-superbuild/Slicer-build directory and then (eventually) you’ll get an _CPack_Packages with an install tree in it.  Let us know if you have the same path error.</p>
<p>-Steve</p>

---

## Post #6 by @prisgdd (2017-06-20 22:58 UTC)

<p>Thanks for your help!</p>
<p>This is how we initially tried, but the path error is the same…</p>

---

## Post #7 by @lassoan (2017-06-21 01:11 UTC)

<p>Have you been able to successfully install the extension package from file using extension manager in Slicer?</p>

---

## Post #8 by @prisgdd (2017-06-21 15:24 UTC)

<ul>
<li>
<p>When I install the extension from file on a downloaded nightly version, the following error occured:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b119cdd861f03859b8e17ed58e77e48a0fd2dbe9.png" data-download-href="/uploads/short-url/pgHNqFVKiSjH8VW9Hs0KRISpf1n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b119cdd861f03859b8e17ed58e77e48a0fd2dbe9_2_690x216.png" alt="image" data-base62-sha1="pgHNqFVKiSjH8VW9Hs0KRISpf1n" width="690" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b119cdd861f03859b8e17ed58e77e48a0fd2dbe9_2_690x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b119cdd861f03859b8e17ed58e77e48a0fd2dbe9_2_1035x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b119cdd861f03859b8e17ed58e77e48a0fd2dbe9.png 2x" data-dominant-color="E3E2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×366 37.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>When I use the built Slicer I used to build the extension, Slicer crashes and the extension isn’t installed when I restart it.</p>
</li>
</ul>
<p>I tried with the <code>make install</code> command, and I have a lot of that following warning for different libraries:</p>
<blockquote>
<p>–<br>
warning: cannot resolve item ‘<span class="mention">@rpath</span>/lib/Slicer-4.7/liboflog.8.dylib’</p>
</blockquote>
<blockquote>
<h2>possible problems:<br>
need more directories?<br>
need to use InstallRequiredSystemLibraries?<br>
run in install tree instead of build tree?</h2>
</blockquote>
<p>Which produces this error:</p>
<blockquote>
<p>– 260/522: copying ‘<span class="mention">@rpath</span>/lib/Slicer-4.7/liboflog.8.dylib’<br>
Error copying file “<span class="mention">@rpath</span>/lib/Slicer-4.7/liboflog.8.dylib” to “/usr/local/Slicer.app/Contents/Extensions-0ef0792/ShapeVariationAnalyzer/lib/Slicer-4.7/liboflog.8.dylib”.</p>
</blockquote>
<p>And then:</p>
<blockquote>
<p>– 521/522: fixing up ‘/usr/local/Slicer.app/Contents/Extensions-0ef0792/ShapeVariationAnalyzer/lib/Slicer-4.7/liboflog.8.dylib’<br>
warning: target ‘/usr/local/Slicer.app/Contents/Extensions-0ef0792/ShapeVariationAnalyzer/lib/Slicer-4.7/liboflog.8.dylib’ does not exist…<br>
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/objdump: ‘/usr/local/Slicer.app/Contents/Extensions-0ef0792/ShapeVariationAnalyzer/lib/Slicer-4.7/liboflog.8.dylib’: No such file or directory.<br>
fatal error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool: internal objdump command failed<br>
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/objdump: ‘/usr/local/Slicer.app/Contents/Extensions-0ef0792/ShapeVariationAnalyzer/lib/Slicer-4.7/liboflog.8.dylib’: No such file or directory.<br>
fatal error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool: internal objdump command failed<br>
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: can’t open file: /usr/local/Slicer.app/Contents/Extensions-0ef0792/ShapeVariationAnalyzer/lib/Slicer-4.7/liboflog.8.dylib (No such file or directory)</p>
</blockquote>

---

## Post #9 by @prisgdd (2017-06-21 20:41 UTC)

<p>Good news: After cleaning the repository and the different CMakeLists, it works well!</p>
<p>I don’t know what was exactly the problem. We started from the creation of a new extension with the Extension Wizard, to be sure we had the good architecture and set the variables correctly.</p>
<p>Thanks for your suggestion!</p>

---
