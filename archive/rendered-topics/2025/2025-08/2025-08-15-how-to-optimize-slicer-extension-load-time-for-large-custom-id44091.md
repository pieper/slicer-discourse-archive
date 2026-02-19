---
topic_id: 44091
title: "How To Optimize Slicer Extension Load Time For Large Custom"
date: 2025-08-15
url: https://discourse.slicer.org/t/44091
---

# How to Optimize Slicer Extension Load Time for Large Custom Toolsets

**Topic ID**: 44091
**Date**: 2025-08-15
**URL**: https://discourse.slicer.org/t/how-to-optimize-slicer-extension-load-time-for-large-custom-toolsets/44091

---

## Post #1 by @fopodon (2025-08-15 08:07 UTC)

<p>Hello</p>
<p>I am developing a custom Slicer extension that bundles many specialized tools &amp; modules for a specific medical imaging workflow.<img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=14" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20">  While the extension works well once loaded; the startup time of Slicer has increased noticeably especially on systems with slower disks / limited RAM. <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=14" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20"></p>
<p>I am looking for ways to reduce this load time without removing key features from the extension.</p>
<p>I have considered breaking the extension into smaller, on-demand modules but I am not sure of the best way to structure that within the Slicer extension framework.<img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=14" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20">  Another idea is to lazy-load certain resources (icons, data files, Python scripts) only when a module is opened for the first time.</p>
<p>If anyone has tried similar optimizations, tips or example repositories would be great. A good starting point for those interested in this topic might be the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" rel="noopener nofollow ugc">Slicer Developer Guide on Extensions</a>, but I am looking for more practical, performance-focused advice based on real-world use cases.<img src="https://emoji.discourse-cdn.com/twitter/innocent.png?v=14" title=":innocent:" class="emoji" alt=":innocent:" loading="lazy" width="20" height="20">  While working on these optimizations; I found <a href="https://www.igmguru.com/blog/what-is-java" rel="noopener nofollow ugc">what is java</a> often linked with discussions about startup speed.</p>
<p>I’d like to hear from others who have worked on large extensions what patterns / optimizations helped you keep Slicer startup fast?<img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=14" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"></p>
<p>Thank you !!</p>

---

## Post #2 by @cpinter (2025-08-22 09:45 UTC)

<p>One option could be making a custom app from your extension where you can specify all the modules you don’t need in the main CMakeLists file.</p>
<p>I suppose lazy loading could be an option, but in that case (if you use Slicer and not custom app) the problem would be that the module list wouldn’t contain the not-yet-loaded module and thus the user wouldn’t be able to choose it. You’d need to add a button in your module to load and switch to that module.</p>

---
