# Slicer Extension With Custom ITK

**Topic ID**: 3769
**Date**: 2018-08-14
**URL**: https://discourse.slicer.org/t/slicer-extension-with-custom-itk/3769

---

## Post #1 by @aangelos28 (2018-08-14 01:30 UTC)

<p>Greetings,</p>
<p>I am trying to build an extension for Slicer which utilizes SuperBuild and contains a CLI module.</p>
<p>For the CLI module to work, I need to use a custom ITK version (based on an old ITK release) which I build via the SuperBuild system. However, when attempting to build the CLI module with the custom ITK version I am encountering many redefinition issues with the standard ITKv4 that ships with Slicer. It seems that the two versions are conflicting.</p>
<p><strong>Is it possible to build a Slicer extension that utilizes a custom ITK version other than the one that Slicer ships with, that is downloaded and built via the SuperBuild system without leading to conflicts with the ITK version of Slicer?</strong></p>
<p>Thank you for the help.</p>
<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.19</p>

---

## Post #2 by @pieper (2018-08-14 13:58 UTC)

<aside class="quote no-group" data-username="aangelos28" data-post="1" data-topic="3769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aangelos28/48/2037_2.png" class="avatar"> aangelos28:</div>
<blockquote>
<p>Is it possible to build a Slicer extension that utilizes a custom ITK version other than the one that Slicer ships with, that is downloaded and built via the SuperBuild system without leading to conflicts with the ITK version of Slicer?</p>
</blockquote>
</aside>
<p>Unfortunately that sounds pretty difficult.  You might be able to make it work by building your CLI with the old version of ITK statically linked, but even then you may run into issues with the ITK IO libraries which have a dynamic factory.</p>
<p>The ITK community is pretty good about helping people port their code.  Did you ask on the ITK discourse for suggestions?</p>

---

## Post #3 by @aangelos28 (2018-08-14 14:36 UTC)

<p>Hi Steve,</p>
<p>Thank you for the reply.</p>
<p>The problem is that I cannot simply port to the new ITK version because the old ITK version I am using has a lot of custom code optimized especially for the module, particularly in the FEM Solver, and this code is not present in the newer ITK versions. Furthermore, these changes might break other applications utilizing the FEM solver if I tried to merge the main ITK branch with the custom one. I attempted to merge the two and build Slicer from source using the resulting ITK code base, but as you might guess a lot of new problems appeared.</p>
<p>I guess the only thing I can try is to statically link and perhaps rename conflicting symbols.</p>

---
