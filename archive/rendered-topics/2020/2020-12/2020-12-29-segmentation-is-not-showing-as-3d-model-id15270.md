---
topic_id: 15270
title: "Segmentation Is Not Showing As 3D Model"
date: 2020-12-29
url: https://discourse.slicer.org/t/15270
---

# Segmentation is not showing as 3d model

**Topic ID**: 15270
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/segmentation-is-not-showing-as-3d-model/15270

---

## Post #1 by @Auguris (2020-12-29 15:03 UTC)

<p>Operating system: MacOS 11.1<br>
Slicer version: Slicer 4.10.2<br>
Expected behavior: Showing 3 Model<br>
Actual behavior: Only showing 2d model</p>
<p>Dear all,<br>
I am trying to manually segment the liver using slicer. With the older versions I was able to direcly create 3D Models of the liver, however when using the new version and using the command “grow from seeds” only a 2d model appears (see attached picture). Maybe one of you can help me, thank you so much in advance <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c48c19fe2ea32c83d4ebbb84b8cffd39bba1f492.jpeg" data-download-href="/uploads/short-url/s2JKwofqdm4v75HAP6BtnhbWrOa.jpeg?dl=1" title="Bildschirmfoto 2020-12-29 um 13.12.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c48c19fe2ea32c83d4ebbb84b8cffd39bba1f492_2_536x500.jpeg" alt="Bildschirmfoto 2020-12-29 um 13.12.36" data-base62-sha1="s2JKwofqdm4v75HAP6BtnhbWrOa" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c48c19fe2ea32c83d4ebbb84b8cffd39bba1f492_2_536x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c48c19fe2ea32c83d4ebbb84b8cffd39bba1f492_2_804x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c48c19fe2ea32c83d4ebbb84b8cffd39bba1f492.jpeg 2x" data-dominant-color="726E69"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2020-12-29 um 13.12.36</span><span class="informations">849×791 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @manjula (2020-12-29 16:05 UTC)

<p>have you not applied the initialization? So the preview segment replaces the original segment.</p>

---

## Post #3 by @Auguris (2020-12-29 16:20 UTC)

<aside class="quote no-group" data-username="manjula" data-post="2" data-topic="15270">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>initialization</p>
</blockquote>
</aside>
<p>Hi Manjula, thanks for your kind and quick reply. No so far I have not known initialization and neither applied it. The normal steps I follow are:</p>
<ul>
<li>drawing the liver and outer segment</li>
<li>growing from seeds</li>
<li>manually finetuning by erasing overlapping volume<br>
and this always worked (see attached picture).<br>
How can I use initialization?<br>
Thank you very much for your help <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d8077a82503229b89bdf45b628100bc0865d7d2.jpeg" data-download-href="/uploads/short-url/dl9DZ1pFdzJIKmXSEFD7VmDFMVs.jpeg?dl=1" title="Bildschirmfoto 2020-12-29 um 17.18.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8077a82503229b89bdf45b628100bc0865d7d2_2_590x500.jpeg" alt="Bildschirmfoto 2020-12-29 um 17.18.46" data-base62-sha1="dl9DZ1pFdzJIKmXSEFD7VmDFMVs" width="590" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8077a82503229b89bdf45b628100bc0865d7d2_2_590x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d8077a82503229b89bdf45b628100bc0865d7d2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d8077a82503229b89bdf45b628100bc0865d7d2.jpeg 2x" data-dominant-color="4C4E53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2020-12-29 um 17.18.46</span><span class="informations">765×648 84.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>

---

## Post #4 by @manjula (2020-12-29 16:23 UTC)

<p>This tutorial shows the liver segmentation with grow from seed</p>
<div class="youtube-onebox lazy-video-container" data-video-id="R-lBsqAvSTA" data-video-title="3D Slicer Tutorial #3: Scissors. Grow from seeds." data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=R-lBsqAvSTA" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/R-lBsqAvSTA/maxresdefault.jpg" title="3D Slicer Tutorial #3: Scissors. Grow from seeds." width="" height="">
  </a>
</div>


---
