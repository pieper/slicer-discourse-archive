# New release 5.0.3, unable to download extension

**Topic ID**: 24524
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/new-release-5-0-3-unable-to-download-extension/24524

---

## Post #1 by @ni5h (2022-07-27 10:36 UTC)

<p>Operating system: windows<br>
Slicer version: 5.0.3<br>
Expected behavior: attempting to download MONAI, NVIDIA, slicerdevelopmenttoolbox etc etc<br>
Actual behavior: failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/62dfc5e5e911182f1dc9c00c/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/62dfc5e5e911182f1dc9c00c/download</a><br>
Categories</p>
<p>It’s likely I am doing something very obvious but unsure why this is happening, should I revert back to an older version? I have not used 3d slicer for some months and attempted to install the newest version, but cannot download basic extensions,</p>

---

## Post #2 by @lassoan (2022-07-27 10:48 UTC)

<p>What operating system do you use? Which extension download provided you this invalid download link?</p>
<p>Does download work using the Extensions Catalog website? <a href="https://extensions.slicer.org/catalog/All/30893/win">https://extensions.slicer.org/catalog/All/30893/win</a></p>

---

## Post #3 by @ni5h (2022-07-27 14:52 UTC)

<p>hi,<br>
[a] Windows 10, same as what I have used for all previous versions. [b] I had the invalid download link for all of the aforementioned extensions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/524342a5ca2e17cb9d710196310ce13c2dac67b3.png" data-download-href="/uploads/short-url/bJJfWET0lxD1t7ssyK5NFKWFnNx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/524342a5ca2e17cb9d710196310ce13c2dac67b3_2_690x371.png" alt="image" data-base62-sha1="bJJfWET0lxD1t7ssyK5NFKWFnNx" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/524342a5ca2e17cb9d710196310ce13c2dac67b3_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/524342a5ca2e17cb9d710196310ce13c2dac67b3_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/524342a5ca2e17cb9d710196310ce13c2dac67b3.png 2x" data-dominant-color="F5F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1353×729 98.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks<br>
Nish</p>

---

## Post #4 by @lassoan (2022-07-27 15:12 UTC)

<p>These all work well for me. Are you behind a hospital/corporate firewall or proxy server?</p>
<p>If that’s the case then report this issue to your network administrators. While they fix the issue, you can download the extensions from the Extensions Catalog website and install from file.</p>

---

## Post #5 by @ferhue (2022-11-07 16:15 UTC)

<p>I solved something similar by adding 8.8.8.8 and 8.8.4.4 to the DNS nameservers, without having to use any VPN.</p>

---
