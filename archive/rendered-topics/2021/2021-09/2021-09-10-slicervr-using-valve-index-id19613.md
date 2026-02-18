# SlicerVR using Valve Index

**Topic ID**: 19613
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/slicervr-using-valve-index/19613

---

## Post #1 by @siqueirl (2021-09-10 18:54 UTC)

<p>Dear all,</p>
<p>I have attempted to use the SlicerVR Module, but it appears that the HMD is not being tracked when the “Show scene in Virtual Reality” button is toggled. I have tried making different adjustments to the scene, but only my controller gets tracked. Could anyone tell me if Valve Index is supported, and, if that’s the case, how to render a volume correctly on it? I have uploaded what I see in VR View:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="otD_uxo3ijc" data-video-title="VR View 2021 09 10 19 31 18" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=otD_uxo3ijc" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/otD_uxo3ijc/maxresdefault.jpg" title="VR View 2021 09 10 19 31 18" width="" height="">
  </a>
</div>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c19610dc46d68bc03324b805f5a0e851fe3571.jpeg" data-download-href="/uploads/short-url/7nR6FeOZILiSicYFozcsTNupj1L.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c19610dc46d68bc03324b805f5a0e851fe3571_2_690x375.jpeg" alt="image" data-base62-sha1="7nR6FeOZILiSicYFozcsTNupj1L" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c19610dc46d68bc03324b805f5a0e851fe3571_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c19610dc46d68bc03324b805f5a0e851fe3571_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c19610dc46d68bc03324b805f5a0e851fe3571_2_1380x750.jpeg 2x" data-dominant-color="7C7D8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1046 82.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-09-11 01:54 UTC)

<p>Does head tracking work in other SteamVR applications?</p>

---

## Post #3 by @siqueirl (2021-09-11 07:03 UTC)

<p>Thank you for your answer. Yes, I tested different applications to make sure it wasn’t the device. What is shown in my video is that as soon as I disable Slicer’s VR rendering, Steam’s “waiting for the application” view appears, and tracking works fine, including displaying the controllers from the correct perspective, which is not happening in Slicer.</p>

---

## Post #4 by @lassoan (2021-09-11 12:58 UTC)

<p>Which Slicer version do you use?</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> have you tried the official factory builds of SlicerVirtualReality with recent SteamVR versions?</p>

---

## Post #5 by @siqueirl (2021-09-11 14:02 UTC)

<p>I’m using 4.11.20210226 revision 29738 built 2021-03-01.</p>
<p>I didn’t find releases on the Kitware’s GitHub repo. Could you please point me to it?</p>

---

## Post #6 by @lassoan (2021-09-11 17:44 UTC)

<p>The releases are built nightly by Kitware computers and stored in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions-server">Extensions Server</a>.</p>
<p>It would be nice if you could test the latest Slicer Preview Release, too, as OpenVR libraries are bundled in the extension and older OpenVR libraries are often become incompatible as SteamVR is updated. The Slicer Preview Release might use a more recent OpenVR library version.</p>

---

## Post #7 by @cpinter (2021-09-13 09:16 UTC)

<p>I have not tried SlicerVR with a headset for months, since our only headset broke. The new ones are on their way…</p>
<p>If it doesn’t work with the latest preview, maybe it can be fixed by updating the OpenVR library.</p>
<p><a class="mention" href="/u/siqueirl">@siqueirl</a> let us know.</p>

---

## Post #8 by @siqueirl (2021-09-13 15:34 UTC)

<p>Thank you for your answers. I couldn’t get any binaries on the Extensions Server. The Download button on <a href="https://extensions.slicer.org/view/SlicerVirtualReality/30117/win" rel="noopener nofollow ugc">this page</a>, for example, does not seem to work.</p>
<p>I tried building the code on your repo, but this is the first time I build a Slicer extension, so I didn’t manage to follow your developer guide. I built Slicer and VTK without a problem, Qt is installed, but when I tried to build your extension, I got this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5b6e31383971952edb3a555a5bd803336c785e9.png" data-download-href="/uploads/short-url/wM9aOex6cN99o95dJkGBhq9GIuR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5b6e31383971952edb3a555a5bd803336c785e9.png" alt="image" data-base62-sha1="wM9aOex6cN99o95dJkGBhq9GIuR" width="690" height="70" data-dominant-color="2A6085"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1565×161 9.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I believe it is because I did not have a VTK OpenVR reference set in the project, but since this step is summarized as “Build the extension against the newly built Slicer with Qt5 and VTK9 enabled”, I didn’t manage to set it up.</p>

---

## Post #9 by @lassoan (2021-09-13 17:30 UTC)

<aside class="quote no-group" data-username="siqueirl" data-post="8" data-topic="19613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/siqueirl/48/12320_2.png" class="avatar"> siqueirl:</div>
<blockquote>
<p>Thank you for your answers. I couldn’t get any binaries on the Extensions Server. The Download button on <a href="https://extensions.slicer.org/view/SlicerVirtualReality/30117/win">this page </a>, for example, does not seem to work.</p>
</blockquote>
</aside>
<p>The Extensions Server is being migrated to a new system, so some errors are expected. <a class="mention" href="/u/jcfr">@jcfr</a> are you aware of this issue?</p>
<p>Anyway, you should be able to download the extension package from the Extensions Manager in Slicer - and most likely you need to rebuild the SlicerVirtualReality extension anyway if you want to try a new OpenVR library version. I’ve just tested and SlicerVirtualReality extension builds without errors for me on Windows in both Debug and Release mode, by following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension">these instructions</a>.</p>

---
