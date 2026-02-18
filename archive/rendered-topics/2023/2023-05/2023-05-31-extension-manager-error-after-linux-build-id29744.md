# Extension manager error after linux build

**Topic ID**: 29744
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/extension-manager-error-after-linux-build/29744

---

## Post #1 by @Adama_w (2023-05-31 07:06 UTC)

<p>Operating system: Linux Ubuntu 22.04.2 LTS 64-bit<br>
Slicer version: 5.0.2 &amp; 5.2.1<br>
Expected behavior: Installed extension<br>
Actual behavior: Error message: Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/63e348f3893957" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/63e348f3893957</a></p>
<p>I successfully ran the builds and when I open the extension manager, the extensions display correctly (I looked into <a href="https://github.com/Slicer/Slicer/issues/6577" rel="noopener nofollow ugc">this</a> solution but the issue is not the same as, in my case, the extension manager is not empty) but then when I click “install” for any extension, I get the error mentioned above.<br>
Also when I download the extension manually from the <a href="https://extensions.slicer.org/catalog/All/30893/" rel="noopener nofollow ugc">extension catalog</a>, the extension is removed every time I restart Slicer</p>

---

## Post #2 by @lassoan (2023-05-31 14:22 UTC)

<p>If you build Slicer then you also need to build all the extensions you want to use. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html#extensions-for-developer-builds-of-slicer">here</a>.</p>

---
