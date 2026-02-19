---
topic_id: 28447
title: "3D Slicer Build Error"
date: 2023-03-19
url: https://discourse.slicer.org/t/28447
---

# 3D slicer build error

**Topic ID**: 28447
**Date**: 2023-03-19
**URL**: https://discourse.slicer.org/t/3d-slicer-build-error/28447

---

## Post #1 by @Anjalimukundan (2023-03-19 12:01 UTC)

<p>Hello Everyone,</p>
<p>I am trying to use slicer modules any create an application.</p>
<p>The compilation of the slicer is done, but I am unable to find the installed folder for header, lib and dll files.</p>
<p>Can we use the slicer modules as library and build a separate application?</p>
<p>Any suggestion will be appreciated.</p>
<p>Regards,<br>
Anjali</p>

---

## Post #2 by @pieper (2023-03-19 17:08 UTC)

<p>You can use the built code from the slicer source to build new libraries and even full executables and applications.  This is essentially what the Extension build system does so just using CMake you should be able to add anything you need.</p>
<p>Another option could be to create a custom application <a href="https://discourse.slicer.org/t/creating-a-custom-3d-slicer/21245">as discussed here</a>.</p>

---

## Post #3 by @Anjalimukundan (2023-03-26 07:51 UTC)

<p>Thank you for your kind reply, but I would like to know if there is any documentation regarding how to use the slicer files to create my own application.</p>

---

## Post #4 by @lassoan (2023-03-26 13:35 UTC)

<p>You can use 3D Slicer files any way you want. You can copy whole files or code snippets, but of course we cannot help you with that. If you plan to reuse a major component of the application, such as using MRML as data model then we may be able to help (we are planning to gradually move out some Slicer core components to standalone packages that can be used in C++ and pip-installed in Python), but this requires quite significant software engineering effort on both your and our side.</p>
<p>The simplest, most efficient and least risky solution is build on the experience that we gathered during the past 20 years - by building your application by extending and customizing Slicer core. Slicer was designed for this purpose and several companies use this approach successfully for their product development. We even have a <a href="https://github.com/KitwareMedical/SlicerCAT">template</a> that makes it easy to get started. It allows you to develop your extensions/customizations independently yet making possible to benefit from new Slicer core developments by separating your custom code from the application platform code.</p>

---

## Post #5 by @Anjalimukundan (2023-04-10 11:04 UTC)

<p>Thank u for your reply . I was able to build successfully.</p>

---
