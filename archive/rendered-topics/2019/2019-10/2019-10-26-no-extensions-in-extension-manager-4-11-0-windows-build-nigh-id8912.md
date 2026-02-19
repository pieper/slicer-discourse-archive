---
topic_id: 8912
title: "No Extensions In Extension Manager 4 11 0 Windows Build Nigh"
date: 2019-10-26
url: https://discourse.slicer.org/t/8912
---

# No extensions in Extension Manager - 4.11.0 windows build (Nightly Also)

**Topic ID**: 8912
**Date**: 2019-10-26
**URL**: https://discourse.slicer.org/t/no-extensions-in-extension-manager-4-11-0-windows-build-nightly-also/8912

---

## Post #1 by @lausiv (2019-10-26 05:12 UTC)

<p>Thank you for your hard working</p>
<p>No extensions in Extension Manager - 4.11.0 build (Nightly Also) in Windows<br>
(I already did manual installation but it did not work.suspicious factor is that revision number was not seen in extension-manager)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c3bdac71e91e0a90aeb68929b8f2fbc451244eb.png" data-download-href="/uploads/short-url/mi6IQi5neJq2eUGHG0yXPwgwAJR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c3bdac71e91e0a90aeb68929b8f2fbc451244eb_2_680x500.png" alt="image" data-base62-sha1="mi6IQi5neJq2eUGHG0yXPwgwAJR" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c3bdac71e91e0a90aeb68929b8f2fbc451244eb_2_680x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c3bdac71e91e0a90aeb68929b8f2fbc451244eb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c3bdac71e91e0a90aeb68929b8f2fbc451244eb.png 2x" data-dominant-color="FDFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1017×747 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>Can you introduce stable revision number(like Slicer version 28257) for fixing no extensions in extension mangager in Windows build?</em></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e4fc0960b2f8e02b02473600a9be74d2a5fb28.png" data-download-href="/uploads/short-url/tNXUtzVV4iUUtQzVNz61k2fPkpO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e4fc0960b2f8e02b02473600a9be74d2a5fb28_2_266x499.png" alt="image" data-base62-sha1="tNXUtzVV4iUUtQzVNz61k2fPkpO" width="266" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e4fc0960b2f8e02b02473600a9be74d2a5fb28_2_266x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e4fc0960b2f8e02b02473600a9be74d2a5fb28.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e4fc0960b2f8e02b02473600a9be74d2a5fb28.png 2x" data-dominant-color="E9EFF7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">356×667 16.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-10-27 16:31 UTC)

<p>Extensions are built every night for latest stable and latest preview release. If something goes wrong ne night then for that day’s preview release there may not be extensions available. You can download Preview Releases built another day as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F</a></p>

---

## Post #3 by @Sam_Horvath (2019-10-28 14:42 UTC)

<p>What is the date on the installer that you downloaded that gave this “revision 0” error?</p>

---

## Post #4 by @lausiv (2019-10-30 09:17 UTC)

<p>Thank you : ) it is very time consuming job, so i try to build extension manager in my local folder.</p>

---

## Post #5 by @lausiv (2019-10-30 09:18 UTC)

<p>both ver did not work about extension manger</p>
<p>4.11 source 28565<br>
4.10.2 source 28257</p>

---

## Post #6 by @lassoan (2019-10-30 15:45 UTC)

<p>Have you built Slicer yourself? If yes, then make sure you checkout the source code from SVN and Slicer can find SVN executable (so that it can retrieve the revision number).</p>

---

## Post #7 by @lausiv (2019-10-30 23:54 UTC)

<p>i download from github<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/Slicer/Slicer" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/324362?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/Slicer/Slicer" target="_blank" rel="nofollow noopener">Slicer/Slicer</a></h3>

<p>Multi-platform, free open source software for visualization and image computing. - Slicer/Slicer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Clone or Download</p>
<p>I will try byh SVN Checkout instead of direct download<br>
Thank you^-^</p>

---

## Post #8 by @lassoan (2019-10-31 04:14 UTC)

<p>You can download Slicer’s source code from Github but not any executables. Have you built Slicer from source code yourself?</p>

---
