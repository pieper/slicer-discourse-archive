---
topic_id: 11934
title: "Viewers Do Not Appear In Openstack"
date: 2020-06-07
url: https://discourse.slicer.org/t/11934
---

# Viewers do not appear in OpenStack

**Topic ID**: 11934
**Date**: 2020-06-07
**URL**: https://discourse.slicer.org/t/viewers-do-not-appear-in-openstack/11934

---

## Post #1 by @kopachini (2020-06-07 20:49 UTC)

<p>Hello everyone… I didn’t want to open a new topic, but now I have a strange layout problem… So I got access to a powerful computer via a server so I could overcome my problem with memory loss… But when I open Slicer 10.2 on that remote computer I got a strange error on the layout. When I want to import STL files to slicer I can’t see them as before (they don’t appear as in pictures above), yet red, green, and yellow windows are black and 3d window is well, partially black… What could cause these problems?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/028a0df1912f2faf15e69025a04d2b38a1df9aac.jpeg" data-download-href="/uploads/short-url/msJAo7tAMzH8fSTaOd5YxHBtCs.jpeg?dl=1" title="4up window error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/028a0df1912f2faf15e69025a04d2b38a1df9aac_2_690x388.jpeg" alt="4up window error" data-base62-sha1="msJAo7tAMzH8fSTaOd5YxHBtCs" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/028a0df1912f2faf15e69025a04d2b38a1df9aac_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/028a0df1912f2faf15e69025a04d2b38a1df9aac_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/028a0df1912f2faf15e69025a04d2b38a1df9aac_2_1380x776.jpeg 2x" data-dominant-color="69696A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4up window error</span><span class="informations">1920×1080 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best regards,<br>
Vjekoslav.</p>

---

## Post #2 by @lassoan (2020-06-07 21:56 UTC)

<p>It looks like a screen scaling issue, which was fixed some time ago in Slicer-4.11. Could you try if the latest Preview Release works well?</p>
<p>What remote desktop software do you use? Windows Remote Desktop is known to have complications with 3D graphics, but RealVNC works well.</p>

---

## Post #3 by @kopachini (2020-06-08 18:49 UTC)

<p>I connect with OpenStack. I’ll try to download 4.11. version and try again. I Will let you know if it succeded.</p>
<p>EDIT:<br>
it’s worse than 4.10.2 version<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f052ea358eacc3152519541ce202f786aba85f9.png" data-download-href="/uploads/short-url/mGL1h4B9bWv6JLIMCvJNEiPN3VT.png?dl=1" title="layout 4.11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f052ea358eacc3152519541ce202f786aba85f9_2_690x388.png" alt="layout 4.11" data-base62-sha1="mGL1h4B9bWv6JLIMCvJNEiPN3VT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f052ea358eacc3152519541ce202f786aba85f9_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f052ea358eacc3152519541ce202f786aba85f9_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f052ea358eacc3152519541ce202f786aba85f9_2_1380x776.png 2x" data-dominant-color="7D98AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">layout 4.11</span><span class="informations">1920×1080 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-06-08 20:59 UTC)

<p>That explains it! You need to configure OpenGL support and maybe even GPU sharing support in OpenStack. I don’t know how to do that but it should be possible.</p>

---
