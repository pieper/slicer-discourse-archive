---
topic_id: 20441
title: "Openigtlinkif Module Is Not Loaded"
date: 2021-11-01
url: https://discourse.slicer.org/t/20441
---

# OpenIGTLinkIF module is not loaded

**Topic ID**: 20441
**Date**: 2021-11-01
**URL**: https://discourse.slicer.org/t/openigtlinkif-module-is-not-loaded/20441

---

## Post #1 by @lb123 (2021-11-01 17:32 UTC)

<p>Hi,</p>
<p>I built Slicer 4.13.0 in Ubuntu 20.04.3 LTS and then I installed the following extensions using  the Extensions Manager:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b59476f854d330b0ca6c1a207355e6c9c36ace0f.png" data-download-href="/uploads/short-url/pUkvos514ZtnwAf8isRgx01eJen.png?dl=1" title="Untitled2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b59476f854d330b0ca6c1a207355e6c9c36ace0f_2_690x131.png" alt="Untitled2" data-base62-sha1="pUkvos514ZtnwAf8isRgx01eJen" width="690" height="131" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b59476f854d330b0ca6c1a207355e6c9c36ace0f_2_690x131.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b59476f854d330b0ca6c1a207355e6c9c36ace0f_2_1035x196.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b59476f854d330b0ca6c1a207355e6c9c36ace0f_2_1380x262.png 2x" data-dominant-color="D6D7DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled2</span><span class="informations">1922×366 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After the installation, I restarted Slicer but I noticed that only some IGT modules are present, as you can see from the following screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8b5516b83be2a343c6e8503b51c66faf0863975.jpeg" data-download-href="/uploads/short-url/zuaSR9qhpImv80pfQagH86t4pj7.jpeg?dl=1" title="thumbnail_Image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b5516b83be2a343c6e8503b51c66faf0863975_2_375x500.jpeg" alt="thumbnail_Image" data-base62-sha1="zuaSR9qhpImv80pfQagH86t4pj7" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b5516b83be2a343c6e8503b51c66faf0863975_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b5516b83be2a343c6e8503b51c66faf0863975_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b5516b83be2a343c6e8503b51c66faf0863975_2_750x1000.jpeg 2x" data-dominant-color="7B755F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_Image</span><span class="informations">960×1280 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Searching for OpenIGTLinkIF module I saw this message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d23a2978d9a29f86e6bfb41eca5092dc945945f0.png" data-download-href="/uploads/short-url/tZKSzTnivNuymyM06S1cfcH3o2Y.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d23a2978d9a29f86e6bfb41eca5092dc945945f0_2_690x479.png" alt="Untitled" data-base62-sha1="tZKSzTnivNuymyM06S1cfcH3o2Y" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d23a2978d9a29f86e6bfb41eca5092dc945945f0_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d23a2978d9a29f86e6bfb41eca5092dc945945f0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d23a2978d9a29f86e6bfb41eca5092dc945945f0.png 2x" data-dominant-color="C4C5C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">758×527 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know what I should do to use OpenIGTLinkIF?</p>
<p>Thank you</p>

---

## Post #2 by @Sunderlandkyl (2021-11-01 18:10 UTC)

<p>If you have built Slicer, then you will need to build all of the extensions that you need as well. The extensions downloaded from the Extension Manager won’t be compatible.</p>
<p>Some more info here:</p><aside class="quote quote-modified" data-post="2" data-topic="19899">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/mac-preview-release-build-failed-to-load-content-in-extension-manager/19899/2">Mac preview release build failed to load content in extension manager</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is the expected behavior. If you build Slicer then you also need to build all the extenions that you want to use to ensure ABI compatibility. 


After you have build Slicer on your computer (which is not very easy), building the extensions is trivial, just two CMake commands - see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-test-and-package" rel="noopener nofollow ugc">here</a>.
  </blockquote>
</aside>


---

## Post #3 by @lb123 (2021-11-02 11:22 UTC)

<p>Thank you! I did like you said, but now I have an other strange issue <a href="https://discourse.slicer.org/t/multiple-sessions-of-slicer-are-launched-in-a-loop/20454">Multiple sessions of Slicer are launched in a loop - Support - 3D Slicer Community</a></p>

---

## Post #4 by @SlicerIsGood (2022-08-16 09:56 UTC)

<p>but，if there are two modules are needed to be applied in customized Slicer app, how to build the two extensions?</p>

---
