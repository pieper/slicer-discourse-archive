---
topic_id: 40393
title: "Slicer Install Update Script"
date: 2024-11-27
url: https://discourse.slicer.org/t/40393
---

# Slicer install/update script

**Topic ID**: 40393
**Date**: 2024-11-27
**URL**: https://discourse.slicer.org/t/slicer-install-update-script/40393

---

## Post #1 by @d-vogel (2024-11-27 06:32 UTC)

<p>Dear all,<br>
I am happy to share the small shell script I built for myself to install and update slicer (either stable or nightly) : <a href="https://github.com/d-vogel/slicer-update/tree/main" rel="noopener nofollow ugc">slicer-update</a></p>
<p>It is a simple command line tool that downloads the binary archive, checksums it (somehow the md5 on nightly never matches…) and installs it in the specified directory. If installed system-wide, it will also chmod the extension directory so that users can install extensions and create a desktop file.</p>
<p>Both stable and nightly can co-exist and will both get a separate desktop file.</p>
<p>For now, only Linux is tested, the MacOS implementation is incomplete.</p>

---
