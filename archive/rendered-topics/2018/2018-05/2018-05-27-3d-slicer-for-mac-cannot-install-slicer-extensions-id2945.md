# 3D slicer for MAC cannot install slicer extensions

**Topic ID**: 2945
**Date**: 2018-05-27
**URL**: https://discourse.slicer.org/t/3d-slicer-for-mac-cannot-install-slicer-extensions/2945

---

## Post #1 by @danceward (2018-05-27 13:45 UTC)

<p>Operating system:Mac OS X<br>
Slicer version:4.8.1<br>
Expected behavior:install slicer extensions<br>
Actual behavior:Extensions can not be installed</p>

---

## Post #2 by @lassoan (2018-05-27 13:48 UTC)

<p>The most common issue is that you are behind a hospital or corporate firewall and proxy settings are not configured at operating system level, but only in your web browser.</p>
<p>You can follow these instructions for downloading and installing extensions manually: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F</a></p>

---

## Post #3 by @danceward (2018-05-27 14:24 UTC)

<p>The problem has been solved.<br>
Thank you<br>
danceward</p>

---

## Post #4 by @pieper (2018-05-28 18:22 UTC)

<p>Not sure if this is what fixed it for <a class="mention" href="/u/danceward">@danceward</a>, but a common scenario on mac is opening Slicer from the read-only disk image and then not being able to install extensions (since they are saved in the app folder on mac).</p>

---
