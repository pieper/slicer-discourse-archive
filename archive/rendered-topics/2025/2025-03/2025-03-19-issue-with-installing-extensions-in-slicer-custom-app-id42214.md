---
topic_id: 42214
title: "Issue With Installing Extensions In Slicer Custom App"
date: 2025-03-19
url: https://discourse.slicer.org/t/42214
---

# Issue with Installing Extensions in Slicer Custom App

**Topic ID**: 42214
**Date**: 2025-03-19
**URL**: https://discourse.slicer.org/t/issue-with-installing-extensions-in-slicer-custom-app/42214

---

## Post #1 by @software (2025-03-19 07:01 UTC)

<p>I turned <strong>Slicer_BUILD_EXTENSIONMANAGER_SUPPORT</strong> ON in the top-level <code>CMakeLists.txt</code>, then configured and generated the project using CMake GUI. After that, I opened the project from CMake GUI in Visual Studio and built <em>All Build</em> in the <code>SlicerCustomAppTemplate</code>, as I wanted to download some extensions.</p>
<p>I tried installing the <em>HD Brain Extraction Tool</em> extension. I even received a pop-up notification at the top right of the screen saying <em>“Installed Extension: HD Brain Extraction Tool.”</em> However, the restart button at the bottom right corner of the screen does not get activated.</p>
<p>When I manually close and reopen Slicer, I cannot find the extension anywhere.</p>
<p>Has anyone encountered this issue before? Any help or guidance would be greatly appreciated!</p>

---

## Post #2 by @pieper (2025-03-19 13:25 UTC)

<p>Check the application log.  It’s very unlikely that extensions built for the regular Slicer will work in a custom app because of compilation differences.</p>

---

## Post #3 by @software (2025-03-19 18:58 UTC)

<p>First of all, thanks for the reply.i have another question sir plz guide me<br>
I have built a <strong>custom template of Kitware</strong> in <strong>Release mode</strong> using <strong>CMake GUI</strong> with the following directories:</p>
<ul>
<li><strong>Source code:</strong> <code>E:/Safe</code></li>
<li><strong>Binary build:</strong> <code>E:/Safe/build</code></li>
</ul>
<p>After configuring and generating the project, the build was successful. Now, I have two <strong>.sln</strong> files:</p>
<ol>
<li><code>build/safe.sln</code></li>
<li><code>build/slicer_build/slicer.sln</code></li>
</ol>
<p>I am confused about which <strong>.sln</strong> file I should open in <strong>Visual Studio</strong> to continue compiling and customizing 3D Slicer.</p>

---
