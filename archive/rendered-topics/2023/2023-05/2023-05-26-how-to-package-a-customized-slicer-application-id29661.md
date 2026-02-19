---
topic_id: 29661
title: "How To Package A Customized Slicer Application"
date: 2023-05-26
url: https://discourse.slicer.org/t/29661
---

# How to package a Customized Slicer Application?

**Topic ID**: 29661
**Date**: 2023-05-26
**URL**: https://discourse.slicer.org/t/how-to-package-a-customized-slicer-application/29661

---

## Post #1 by @nnzzll (2023-05-26 07:48 UTC)

<p>I have developed a customized slicer application using <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a>.</p>
<p>I want to package my app into a <code>.deb</code> file on <code>ubuntu18.04</code>, however, I have less knowledge about software packaging. So I am wondering is there any tutorial or template CMake Script that can let me know how to package the whole application?</p>

---

## Post #2 by @pieper (2023-05-26 12:41 UTC)

<p>We don’t make deb files for Slicer, but it seems cpack should support it.<br>
<a href="https://cmake.org/cmake/help/latest/cpack_gen/deb.html" class="onebox" target="_blank" rel="noopener">https://cmake.org/cmake/help/latest/cpack_gen/deb.html</a></p>

---
