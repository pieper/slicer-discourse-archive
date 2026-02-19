---
topic_id: 18305
title: "How To Create Custom Markup"
date: 2021-06-23
url: https://discourse.slicer.org/t/18305
---

# How to create custom markup?

**Topic ID**: 18305
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/how-to-create-custom-markup/18305

---

## Post #1 by @smallvalthoss (2021-06-23 15:51 UTC)

<p>For creating a custom markup, how do you open visual studio in the loadable markup source code, but with intellisense and all that from the slicer-build?</p>

---

## Post #2 by @lassoan (2021-06-23 16:07 UTC)

<p>You can just load the .sln file of your extension. Intellisense will work well. See details <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_run_extension_tests_.3F">here</a>.</p>
<p>Do not modify Slicer core if you just want to add custom markups. <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> implemented infrastructure for adding new markup types in any extension. Use the “loadablecustommarkups” module template in Extension Wizard.</p>

---

## Post #3 by @smallvalthoss (2021-06-23 18:15 UTC)

<p>I looked through that page before, but I may just not be understanding correctly from the instructions. Here are the steps I have taken:</p>
<ul>
<li>Built Slicer from source</li>
<li>Used the wizard to create a custom markup</li>
<li>Configured and Generated using cmake-gui into a build folder for the markup</li>
</ul>
<p>From there I am not sure, I am completely new to writing extensions to applications. Do I open to .sln, then open the folder with the source code in it? Do I modify code in the build folder? Do I open the source code folder, then load in the .sln file?<br>
Thanks again for your patience</p>

---

## Post #4 by @lassoan (2021-06-23 19:00 UTC)

<p>To develop custom C++ loadable modules, you need to build 3D Slicer first, and then you can build your extension.</p>

---

## Post #5 by @smallvalthoss (2021-06-23 19:09 UTC)

<p>Yes, Here are the steps I have already taken.<br>
I have:</p>
<ul>
<li>Built slicer from source to D:/D/S4R</li>
<li>Used the extension wizard to create the template for the loadable markup</li>
<li>Configured and generated the extension to a build folder using the Slicer_DIR in cmake gui</li>
</ul>
<p>I just don’t know how to go from there in editing the source folder. When I open the source folder in visual studio it gives me errors. So I am wondering if I have to reference the slicer-build folder while it is open in visual studio.</p>

---

## Post #6 by @lassoan (2021-06-23 19:12 UTC)

<p>You can go to the binary folder of your extension (that CMake generated), open that .sln file, choose build configuration (if you built Slicer in Release mode then you need to choose Release mode), and then build. The build should succeed.</p>

---

## Post #7 by @smallvalthoss (2021-06-23 22:36 UTC)

<p>I am getting these errors when trying to build using the solution file. I need to modify the source code before building it right? That is the part that I’m wondering about.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e98a1a1bd480f7eb71cd45b818a898fd6a92fa8.png" data-download-href="/uploads/short-url/duPTomaaG7MvSlR3LXnrMdxp4CY.png?dl=1" title="Slicer errors" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e98a1a1bd480f7eb71cd45b818a898fd6a92fa8_2_690x183.png" alt="Slicer errors" data-base62-sha1="duPTomaaG7MvSlR3LXnrMdxp4CY" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e98a1a1bd480f7eb71cd45b818a898fd6a92fa8_2_690x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e98a1a1bd480f7eb71cd45b818a898fd6a92fa8_2_1035x274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e98a1a1bd480f7eb71cd45b818a898fd6a92fa8_2_1380x366.png 2x" data-dominant-color="292D31"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer errors</span><span class="informations">3811×1016 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-06-25 21:51 UTC)

<p>Have you built Slicer successfully? Does it run? Have you build Slicer with the same build mode (Debug/Release/…) as you use for building your extension?</p>
<p>Make sure you build the top-level .sln file in your extension.</p>
<p>It may also be an issue that you have a space in your project path (and it is also way too long). Try to build your extension in <code>C:\D\MyExtension</code>.</p>

---

## Post #9 by @smallvalthoss (2021-07-19 17:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="18305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Make sure you build the top-level .sln file in your extension.</p>
</blockquote>
</aside>
<p>Thanks for all the help. Your last suggestion worked, I put it in D:\D\Extensions.</p>
<p>As for the actual code writing part. I am still a little confused as to where to start writing. I now have the solutions explorer open in visual studio. Do I add a source code folder to it? Do I open the src folder with the solution explorer open? Thanks again.</p>

---

## Post #10 by @lassoan (2021-08-28 03:23 UTC)

<p>You add new files into the source code folders and list the files in the CMakeLists.txt file.</p>

---
