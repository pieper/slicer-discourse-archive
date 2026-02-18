# About different versions of PRISM Rendering

**Topic ID**: 22390
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/about-different-versions-of-prism-rendering/22390

---

## Post #1 by @qiqi5210 (2022-03-09 01:27 UTC)

<p>Hello，everyone！<br>
I have a problem using the PRISM Rendering in the software version 2022-02-05, as shown in the following figure<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d8e8e4b081b3801a44f10866dbb2ac5ab6e7109.jpeg" data-download-href="/uploads/short-url/8Myy6Osra8nrDCu2Co3g61CaZjb.jpeg?dl=1" title="2022-02-05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d8e8e4b081b3801a44f10866dbb2ac5ab6e7109_2_690x376.jpeg" alt="2022-02-05" data-base62-sha1="8Myy6Osra8nrDCu2Co3g61CaZjb" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d8e8e4b081b3801a44f10866dbb2ac5ab6e7109_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d8e8e4b081b3801a44f10866dbb2ac5ab6e7109_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d8e8e4b081b3801a44f10866dbb2ac5ab6e7109_2_1380x752.jpeg 2x" data-dominant-color="3D3A3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-02-05</span><span class="informations">1920×1048 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I operate according to the sequence in the figure. When initializing the center, the volume rendering ROI in the fifth place in the figure appears instead of the endpoints of the previous version<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3ce1ad16a72bc532d80e9a43201259a8d6f38cf9.jpeg" data-download-href="/uploads/short-url/8GA9JT4tKbvNPHMhHbbMwnP503n.jpeg?dl=1" title="2021-09-25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ce1ad16a72bc532d80e9a43201259a8d6f38cf9_2_690x376.jpeg" alt="2021-09-25" data-base62-sha1="8GA9JT4tKbvNPHMhHbbMwnP503n" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ce1ad16a72bc532d80e9a43201259a8d6f38cf9_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ce1ad16a72bc532d80e9a43201259a8d6f38cf9_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ce1ad16a72bc532d80e9a43201259a8d6f38cf9_2_1380x752.jpeg 2x" data-dominant-color="3E3B3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-09-25</span><span class="informations">1920×1048 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What can I do to achieve the following results<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/aca203d04687a0851a6b32edde28f5c9c720220d.png" alt="result" data-base62-sha1="oDbeTsbiymEsAl5FoKmQQp1iUnX" width="620" height="430"><br>
I hope someone can help me. Thank you very much！</p>
<p>Best wishes, Mary</p>

---

## Post #2 by @pieper (2022-03-10 00:14 UTC)

<p>Yes, this was reported recently.  Apparently there’s nobody on the prism team able to work on it yet for the current version of Slicer so the older version must be used.</p>
<aside class="quote quote-modified" data-post="1" data-topic="22321">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qiqi5210/48/15920_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/in-the-latest-version-of-the-software-the-prism-rendering-module-cannot-be-used-normally/22321">In the latest version of the software, the prism rendering module cannot be used normally,。</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In the latest version of the software, the prism rendering module cannot be used normally, and the mouse pattern of ROI appears when points should be added. As shown in the following picture, after clicking the “initialize center” button, the ROI icon appears. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b84395f9b79def5c1cc6027ec4e312d212880628.jpeg" data-download-href="/uploads/short-url/qi4EHOKCqoYMEouqlvFv5xjwHvG.jpeg?dl=1" title="f6bac8bf6c2c8b71ea490e826463d61" rel="noopener nofollow ugc">[f6bac8bf6c2c8b71ea490e826463d61]</a>
  </blockquote>
</aside>


---
