# How to compile and run the files.

**Topic ID**: 33835
**Date**: 2024-01-17
**URL**: https://discourse.slicer.org/t/how-to-compile-and-run-the-files/33835

---

## Post #1 by @Arun03Kumar (2024-01-17 16:19 UTC)

<p>my build is completed just now, now I have two folders one contains the repository cloned file and another one contains the build files, the build folder now has a lot more folders, now I am totally confused that in which directory I have to change the source code??<br>
and let’s suppose I changed some code in a file then how can I see the reflection of it? by building it again or what commands should I use to compile the whole file or what is the procedure because till now I’ve worked with only one or two c++ files which I simply compile and run, but here I have no clue.</p>

---

## Post #2 by @RafaelPalomar (2024-01-17 17:45 UTC)

<p>Hello <a class="mention" href="/u/arun03kumar">@Arun03Kumar</a>.</p>
<p>Directly modifying 3D Slicer can be overwhelming and may not always be sustainable. Given the fast-paced development of the main repository, your changes might not align with the ongoing updates, making them challenging to integrate.</p>
<p>Perhaps a better approach would be to explore development through extensions. Extensions allow you to add functionality to 3D Slicer without altering the core codebase of 3D Slicer. This method ensures (to a large degree) your work remains compatible with future updates of 3D Slicer and is easier to manage. You can get more information in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" rel="noopener nofollow ugc">extensions documentation</a></p>
<p>However, if you still wish to modify the core code, remember that the repository you cloned is where you make changes. Your build directory is for compiled files and shouldn’t be modified for code changes. After editing the source code in the repository, return to the build directory and recompile to see your changes. The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/index.html" rel="noopener nofollow ugc">developer guide</a> will help you understand the structure of the project.</p>
<p>I hope this helps.</p>

---

## Post #3 by @Arun03Kumar (2024-01-17 20:08 UTC)

<p>Thank you so much <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>.</p>
<p>so if I want to change some thing then I’ll change in the source directory, then go back to my build directory and just run “cmake --build” in build directory. then run the slicer.exe from slicer-build folder to see the changes.<br>
is this the correct process or should I have to do something else??<br>
can you please elaborate in step by step manner, till now I have just compiled only single c++ file using gcc command.</p>
<p>Thank you.</p>

---

## Post #4 by @RafaelPalomar (2024-01-18 05:51 UTC)

<aside class="quote no-group" data-username="Arun03Kumar" data-post="3" data-topic="33835">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arun03kumar/48/68980_2.png" class="avatar"> Arun03Kumar:</div>
<blockquote>
<p>so if I want to change some thing then I’ll change in the source directory, then go back to my build directory and just run “cmake --build” in build directory. then run the slicer.exe from slicer-build folder to see the changes.</p>
</blockquote>
</aside>
<p>That’s correct. The cmake build command may require specification of a directory i.e., <code>cmake --build .</code>.</p>
<aside class="quote no-group" data-username="Arun03Kumar" data-post="3" data-topic="33835">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arun03kumar/48/68980_2.png" class="avatar"> Arun03Kumar:</div>
<blockquote>
<p>can you please elaborate in step by step manner, till now I have just compiled only single c++ file using gcc command.</p>
</blockquote>
</aside>
<p>3D Slicer uses the CMake build system to manage the project. Manually compiling individual files is not a good idea, introducing changes require updating the project output in a wider manner.  You can refer to the <a href="https://cmake.org/cmake/help/latest/index.html" rel="noopener nofollow ugc">CMake documentation</a> to understand the workflow used in CMake-based projects.</p>

---

## Post #5 by @Arun03Kumar (2024-01-18 09:58 UTC)

<p>okay, thank you. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @Arun03Kumar (2024-01-20 19:06 UTC)

<p>I tried to recompile the source after a small change with 'cmake --build ." command in SD folder which is build folder as specified on slice build documentation, but it still took the same time to build (around 9 hours).</p>
<p>I am not following that if I change something then should I have to wait until the next build.</p>
<p>or you just please the steps involved in compiling and seeing the output after a change in source directory.</p>
<p>my directory structure is same as specified on github build documentation<br>
source - "C:/D/S<br>
debug build - "C:/D/SD/</p>

---

## Post #7 by @Thibault_Pelletier (2024-01-21 07:30 UTC)

<p>Hi <a class="mention" href="/u/arun03kumar">@Arun03Kumar</a>,</p>
<p>Slicer’s build system works with a superbuild, meaning that the “C:/D/S” folder contains both Slicer’s build tree and Slicer’s dependencies build trees.</p>
<p>After the first build, if you want to build only Slicer, you can navigate to the “C:/D/S/Slicer-build” dir and build only this one.</p>
<p>Note also that Slicer is modularized which can help if you want to build only the target you have modified (which will be much faster).</p>
<p>Best,<br>
Thibault</p>

---

## Post #8 by @RafaelPalomar (2024-01-24 16:02 UTC)

<aside class="quote no-group" data-username="Arun03Kumar" data-post="6" data-topic="33835">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arun03kumar/48/68980_2.png" class="avatar"> Arun03Kumar:</div>
<blockquote>
<p>but it still took the same time to build (around 9 hours).</p>
</blockquote>
</aside>
<p>Building 3D Slicer implies building many of its dependencies. You can improve the building time of Slicer (first-time, but also subsequent builds by the use parallel jobs i.e., <code>cmake --build -j9</code> where 9 was the number of parallel jobs). The rule of thumb is to use <code>number_of_threads+1</code>, but there is absolutely no science behind it  and depends on what you build. In addition increasing the number of parallel jobs, generally, increases the memory required (if you go above, your computer can “freeze” while compiling). More info at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#build-slicer" class="inline-onebox" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a></p>

---
