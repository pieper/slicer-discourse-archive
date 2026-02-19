---
topic_id: 42807
title: "How To Hide Certain Modules And Customize Module Layout In M"
date: 2025-05-06
url: https://discourse.slicer.org/t/42807
---

# How to Hide Certain Modules and Customize Module Layout in My Custom Slicer Build

**Topic ID**: 42807
**Date**: 2025-05-06
**URL**: https://discourse.slicer.org/t/how-to-hide-certain-modules-and-customize-module-layout-in-my-custom-slicer-build/42807

---

## Post #1 by @software (2025-05-06 07:52 UTC)

<p>Hi everyone,</p>
<p>I’m working on a custom version of 3D Slicer and I want to customize it a bit:</p>
<ol>
<li><strong>Hide or disable certain modules:</strong><br>
I don’t want to use some modules like <em>Markups</em>, <em>Camera</em>, and <em>Data Probe</em> in my build. I want the ability to decide which modules are included or excluded.<br>
Is it possible to achieve this using <strong>Python scripts</strong>, or does it have to be handled from <strong>CMake configuration</strong> during the build process? I don’t have a clear idea of which path is better</li>
<li><strong>Move the top-left UI buttons (View, Edit, File):</strong><br>
In the original Slicer, the View, Edit, and File module selectors appear in the <strong>top-left corner</strong>. I want to <strong>reposition them</strong>, for example, to the <strong>bottom of the window or another location</strong> in the UI.<br>
How can I achieve this UI change? Is it done through Qt/C++ customization, Python scripts, or modifying specific Slicer source files?</li>
</ol>

---
