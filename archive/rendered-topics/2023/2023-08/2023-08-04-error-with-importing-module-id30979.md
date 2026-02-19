---
topic_id: 30979
title: "Error With Importing Module"
date: 2023-08-04
url: https://discourse.slicer.org/t/30979
---

# Error with importing module

**Topic ID**: 30979
**Date**: 2023-08-04
**URL**: https://discourse.slicer.org/t/error-with-importing-module/30979

---

## Post #1 by @slicer365 (2023-08-04 16:30 UTC)

<p>I have a custom module that encapsulates some functions. I can import it into the python script normally in vscode. Now I have made the script into a slicer module. When I put the pyd file in the same directory as the script, but import failed.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79d68f50b6a6cf614f78e5aeddb974c1097d2dea.png" alt="image" data-base62-sha1="hnPsUbFQqhIJVzrJQw0bdiuWBAe" width="409" height="177"></p>
<p>it means can’t find the file</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7ff690f2e4cb5a92dc7f606a62e44c7819c5457.png" data-download-href="/uploads/short-url/uONRXJELiNWScPwroHovz9TowJx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7ff690f2e4cb5a92dc7f606a62e44c7819c5457.png" alt="image" data-base62-sha1="uONRXJELiNWScPwroHovz9TowJx" width="690" height="118" data-dominant-color="FFF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1116×192 7.86 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8449db3d561cf0d4b1b968e6dbadea9087fa009e.png" data-download-href="/uploads/short-url/iShghSHfRtSZk6rntWs6PeWZ7Iy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8449db3d561cf0d4b1b968e6dbadea9087fa009e.png" alt="image" data-base62-sha1="iShghSHfRtSZk6rntWs6PeWZ7Iy" width="517" height="141" data-dominant-color="F5F5F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">807×221 6.36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-08-04 19:33 UTC)

<p>Python-3.8 toughened security in Windows, so it is not enough to have DLLs in the path. See more information for example here: <a href="https://stackoverflow.com/a/64303856" class="inline-onebox">python module dlls - Stack Overflow</a></p>

---
