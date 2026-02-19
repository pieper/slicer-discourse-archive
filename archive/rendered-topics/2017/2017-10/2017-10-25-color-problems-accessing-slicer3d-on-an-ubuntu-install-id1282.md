---
topic_id: 1282
title: "Color Problems Accessing Slicer3D On An Ubuntu Install"
date: 2017-10-25
url: https://discourse.slicer.org/t/1282
---

# Color problems accessing Slicer3D on an Ubuntu install

**Topic ID**: 1282
**Date**: 2017-10-25
**URL**: https://discourse.slicer.org/t/color-problems-accessing-slicer3d-on-an-ubuntu-install/1282

---

## Post #1 by @dcantor (2017-10-25 01:13 UTC)

<p>Problem report for Slicer 4.8.0 linux-amd64: [please describe expected and actual behavior]</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cce0cc6a80568c94d57b31b889ddbb7522be0b83.jpeg" data-download-href="/uploads/short-url/ter214qrINRG5kzXalGOgWnRcjN.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cce0cc6a80568c94d57b31b889ddbb7522be0b83_2_690x417.jpg" alt="image" data-base62-sha1="ter214qrINRG5kzXalGOgWnRcjN" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cce0cc6a80568c94d57b31b889ddbb7522be0b83_2_690x417.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cce0cc6a80568c94d57b31b889ddbb7522be0b83_2_1035x625.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cce0cc6a80568c94d57b31b889ddbb7522be0b83.jpeg 2x" data-dominant-color="938B8A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1363×824 376 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>the image shows the colors are completely off. I am using Slicer3D through a VNC connection. Slicer3D is hosted on a Ubuntu machine.</p>

---

## Post #2 by @ihnorton (2017-10-25 01:29 UTC)

<p>Did older versions of Slicer work ok? The gradients look kind of like compression artifact if VNC downgrades the quality due to insufficient bandwidth. Others might have suggestions, but this is may not be a Slicer problem per se.</p>
<p>Other people have used VNC successfully – see thread below. I’ve also used TeamViewer a few times and had good results, although usually with a Windows system hosting Slicer.</p>
<aside class="quote" data-post="9" data-topic="138">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/saving-images-from-slicer-views-in-headless-compute-node/138/9">Saving images from slicer views in headless compute node</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    (Edited the previous post to use display :11 rather than :1 to match Mike’s use case)
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2017-10-25 01:50 UTC)

<p>Looks like color quantization artifact to me, too. These instructions may help for setting up VNC appropriately: <a href="https://askubuntu.com/questions/281177/colours-background-messed-up-in-vnc-viewer">https://askubuntu.com/questions/281177/colours-background-messed-up-in-vnc-viewer</a></p>

---

## Post #4 by @dcantor (2017-10-25 02:00 UTC)

<p>I will try an older version. No VNC compression used as I configured it for maximum quality.</p>
<p>Thanks.</p>

---

## Post #5 by @dcantor (2017-10-25 02:14 UTC)

<p>I don’t think it is a quantization problem. The problem happens inside Slicer. Other than that the desktop looks totally fine. And inside Slicer it seems like the lookup tables are all wrong. Also I had already configured VNC for maximum quality… check this side to side between chrome and slicer. The background in Slicer looks off and as shown in my previous post the DICOM volume looks off too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddaf037c16e53443653e5657027d508577138d56.jpeg" data-download-href="/uploads/short-url/vD6u7OxMVFFtDQAIxP4YaPqRNae.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ddaf037c16e53443653e5657027d508577138d56_2_690x406.jpg" alt="image" data-base62-sha1="vD6u7OxMVFFtDQAIxP4YaPqRNae" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ddaf037c16e53443653e5657027d508577138d56_2_690x406.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ddaf037c16e53443653e5657027d508577138d56_2_1035x609.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddaf037c16e53443653e5657027d508577138d56.jpeg 2x" data-dominant-color="9F9B92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×812 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2017-10-25 02:46 UTC)

<p>It seems that only the OpenGL windows colors are off. Can you check other applications with OpenGL windows? Can you try with other VNC clients/servers and other remote desktop software (TeamViewer, etc)?</p>

---

## Post #7 by @dcantor (2017-10-25 04:46 UTC)

<p>Update:</p>
<p>TeamViewer did not install (problem with AWS).</p>
<p>Tried with Slicer 4.4 and had the same problem</p>
<p>Tried with Slicer 4.0 and it did not start because a Qt dependency.</p>

---

## Post #8 by @ihnorton (2017-10-25 10:39 UTC)

<p>Try something that is pure OpenGL (no VTK) like <a href="http://www.meshlab.net/">MeshLab</a>. It is small and should be in the package repository already.</p>

---
