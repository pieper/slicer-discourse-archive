# How to bypass the git clone operations during the 3D Slicer build?

**Topic ID**: 42926
**Date**: 2025-05-14
**URL**: https://discourse.slicer.org/t/how-to-bypass-the-git-clone-operations-during-the-3d-slicer-build/42926

---

## Post #1 by @MarkLiu (2025-05-14 16:20 UTC)

<p>Dear Community,</p>
<p>I’m developing an application based on 3D Slicer. And I have locally built 3D Slicer successfully with superbuild set to true.  It is known that for the very first build, the git clone operations will be triggered to download the source code remotely for some modules.</p>
<p>However, when I try to rebuild the 3D Slicer or when I change the build folder location, the git clone operations will always be triggered. This makes some troubles to me because the git clone operations are time-consumping or even fail sometimes due to the network situations on my side.</p>
<p>So are there any solutions to bypass the git clone operations during the 3D slicer build, it will really help when the source code is already available locally.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2025-05-14 16:24 UTC)

<p>Usually we just build the inner-build project (<code>&lt;Slicer-build-tree&gt;/Slicer-build/Slicer.sln</code>) and not the top-level project (<code>&lt;Slicer-build-tree&gt;/Slicer.sln</code>). The inner-build does not perform any git operation. We only build the top-level project if we want to get updates for dependencies (e.g., if CTK update is needed for some new Slicer features then we run the top-level build once to fetch all those updates).</p>

---

## Post #3 by @MarkLiu (2025-05-15 02:12 UTC)

<p>Hi Andras,<br>
Many thanks for the reply. If I want to build the 3D Slicer in a different folder or on another computer, are there any good ways to directly use the local downloaded packages instead of performing the git operations again? On one hand, this can fix the trouble that I have mentioned in the first post. On the other hand, this can ensure that the build is always performed based on the same source code with different build folders or different computers, which is very important from the version control point of view.</p>
<p>Thanks in advance.</p>

---

## Post #4 by @lassoan (2025-05-18 00:31 UTC)

<p>Manual downloading, configuring, and building of all the packages would be very error-prone, that’s why we use CMake to automate these. I would not recommend trying to invest time into this for ensuring consistent build (you can achieve that by using containers, virtual machines, or standardized developer computer images in a much easier way).</p>
<p>If you absolutely have no other choice, for example for fulfilling some security or regulatory requirements then you can give it a try. At a very high level, <code>Slicer_USE_SYSTEM_&lt;project&gt;</code> and <code>&lt;project&gt;_DIR</code> CMake variables can be passed to the superbuild for each project (<code>VTK</code>, <code>ITK</code>, …) to use a prebuilt dependency already on your system, but there are many complicated details. Some people, such as <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> ventured into this field with considerable success, so if you decide to go for it and you get stuck with some issues then you might get some help.</p>

---

## Post #5 by @MarkLiu (2025-05-19 02:11 UTC)

<p>Hi Andras,<br>
Thanks for the information! I will give a try if necessary and ask for help if needed.</p>

---
