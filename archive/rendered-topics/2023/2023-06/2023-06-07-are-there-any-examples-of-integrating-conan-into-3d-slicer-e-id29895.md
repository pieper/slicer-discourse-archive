---
topic_id: 29895
title: "Are There Any Examples Of Integrating Conan Into 3D Slicer E"
date: 2023-06-07
url: https://discourse.slicer.org/t/29895
---

# Are there any examples of integrating conan into 3d slicer extension?

**Topic ID**: 29895
**Date**: 2023-06-07
**URL**: https://discourse.slicer.org/t/are-there-any-examples-of-integrating-conan-into-3d-slicer-extension/29895

---

## Post #1 by @james94g (2023-06-07 12:44 UTC)

<p>Operating system: Ubuntu 22.04<br>
Slicer version: 5.3.0<br>
Expected behavior: After successfully building custom extension with conan cmake, I expect my modified OpenIGTLinkIF module to show up in modules.<br>
Actual behavior: However, after building my modified version of SlicerOpenIGTLink and its OpenIGTLinkIF module, it doesn’t show up in 3D Slicer.</p>
<p>Has anyone built a custom extension with conan cmake? Any help or guidance would be greatly appreciated as I am aiming to use 3D slicer for my master thesis on AI stroke diagnosis.</p>

---

## Post #2 by @pieper (2023-06-07 14:36 UTC)

<p>The conan option sounds interesting, but I don’t know that anyone has used it before.  Best to stick with the documented toolchain to make sure things are working, and then try out new tools</p>

---

## Post #3 by @james94g (2023-06-07 22:00 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> since I need to use conan for my project, I could create a tutorial or document how to do it when I get it working and share it with the Slicer Community. Any suggestions on contributing to 3D Slicer?</p>

---

## Post #4 by @pieper (2023-06-07 22:04 UTC)

<p>It would be great if you could make such a contribution.  Probably a PR to add info to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html">the extension instructions</a> would be good.  I’m not familiar with conan, but it sounds like something we might be able to use other places as well.</p>

---

## Post #5 by @lassoan (2023-06-07 22:27 UTC)

<p>Can you write a bit more about conan? What are the advantages compared to simply using CMake? What makes it required for you to use conan?</p>

---
