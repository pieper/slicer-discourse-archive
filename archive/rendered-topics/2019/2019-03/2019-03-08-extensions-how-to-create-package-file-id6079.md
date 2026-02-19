---
topic_id: 6079
title: "Extensions How To Create Package File"
date: 2019-03-08
url: https://discourse.slicer.org/t/6079
---

# Extensions: How to create package file

**Topic ID**: 6079
**Date**: 2019-03-08
**URL**: https://discourse.slicer.org/t/extensions-how-to-create-package-file/6079

---

## Post #1 by @triple_axel (2019-03-08 21:55 UTC)

<p>Hi,<br>
I am trying to test out my extension by manually downloading it via the extension manager. I am currently following this tutorial:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions</a></p>
<p>Under testing, I was wondering what it means by "If you have built your extension then build the PACKAGE target to create a package file ".<br>
I currently created the folder containing all the contents required for an extension (CmakeLists, modules, etc.) using the Extension Wizard. I was wondering how to build a package file from the folder?</p>
<p>Thanks a bunch.</p>

---

## Post #2 by @jcfr (2019-03-08 23:00 UTC)

<blockquote>
<p>I was wondering how to build a package file from the folder?</p>
</blockquote>
<p>First, you have to build your extension. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F">How to build an extension ?</a></p>
<p>Then, you can generate the package building the corresponding target. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_package_an_extension_.3F"> How to package an extension ?</a></p>

---
