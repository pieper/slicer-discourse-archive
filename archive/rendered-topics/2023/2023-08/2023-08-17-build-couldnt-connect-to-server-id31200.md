---
topic_id: 31200
title: "Build Couldnt Connect To Server"
date: 2023-08-17
url: https://discourse.slicer.org/t/31200
---

# Build Couldn't connect to server

**Topic ID**: 31200
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/build-couldnt-connect-to-server/31200

---

## Post #1 by @Kening_Zhang (2023-08-17 19:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8df18723efc42cfd0f4fa7dcee82e006c9af1f00.png" data-download-href="/uploads/short-url/kfGNfT0GKUVXreuBFVr1YkR112U.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8df18723efc42cfd0f4fa7dcee82e006c9af1f00_2_493x500.png" alt="image" data-base62-sha1="kfGNfT0GKUVXreuBFVr1YkR112U" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8df18723efc42cfd0f4fa7dcee82e006c9af1f00_2_493x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8df18723efc42cfd0f4fa7dcee82e006c9af1f00_2_739x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8df18723efc42cfd0f4fa7dcee82e006c9af1f00_2_986x1000.png 2x" data-dominant-color="ECEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1138×1154 278 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I try to build Slicer on my mac, but error happens, I try both http and https, and try open and close firewall, but cannot solve this problem.</p>

---

## Post #2 by @Kening_Zhang (2023-08-17 19:23 UTC)

<p>In China, If you use a proxy server, make sure CMake is able to use the proxy properly. You may need to set the proxy information in the CMake configuration option or adjust your network environment based on the proxy Settings.<br>
Here is an example,<br>
export https_proxy=<a href="http://127.0.0.1:33210" rel="noopener nofollow ugc">http://127.0.0.1:33210</a> http_proxy=<a href="http://127.0.0.1:33210" rel="noopener nofollow ugc">http://127.0.0.1:33210</a> all_proxy=socks5://127.0.0.1:33210</p>

---
