# CTA Willis registration failure

**Topic ID**: 45470
**Date**: 2025-12-13
**URL**: https://discourse.slicer.org/t/cta-willis-registration-failure/45470

---

## Post #1 by @Peter_Jan (2025-12-13 17:51 UTC)

<p>Hello everyone,</p>
<p>my goal is to register CTA Circle of Willis examinations of two patients acquired with a 4-year interval, using the skull as a reference, in order to evaluate changes in the position of the arterial tree over time.</p>
<p>I was successful in one patient using <strong>General Registration (Brains)</strong>, but unfortunately not in the others. I also tried <strong>manual registration</strong>, as well as the <strong>Elastix</strong> and <strong>ANTs</strong> extensions, without satisfactory results.</p>
<p>Could there be problem in sources CTs data? I attach the pre-registration pic.</p>
<p>Could you please advise on the most appropriate registration strategy or workflow for this type of longitudinal CTA data? Any tips or shared experience would be greatly appreciated.</p>
<p>Thank you very much,<br>
Peter<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba204c41a097577517064c0132d957d88d99578a.jpeg" data-download-href="/uploads/short-url/qyy0snWJ8K70mSYa0Qdu2TvG4C6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba204c41a097577517064c0132d957d88d99578a_2_690x481.jpeg" alt="image" data-base62-sha1="qyy0snWJ8K70mSYa0Qdu2TvG4C6" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba204c41a097577517064c0132d957d88d99578a_2_690x481.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba204c41a097577517064c0132d957d88d99578a_2_1035x721.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba204c41a097577517064c0132d957d88d99578a_2_1380x962.jpeg 2x" data-dominant-color="77767D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1609×1122 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @fedorov (2025-12-13 17:54 UTC)

<p>Have you tried using manual for the initial transformation and then refining with any of the automated tools?</p>
<p>When configuring the registration tools, did you configure multi-stage so that it tries to do affine first before deformable (if you want to do deformable at all)?</p>

---

## Post #3 by @pieper (2025-12-13 18:48 UTC)

<p>In addition to manually lining up the volumes, in the General Registration module I often find the default Percentage Of Samples parameter is too small.  I sometimes bump it up by two orders of magnitude and get better results.</p>

---

## Post #4 by @Peter_Jan (2025-12-14 20:57 UTC)

<p>Yes, I have tried to do it in this way, but it usally makes a bigger mess. I tried also multistage in General registration (BRAINS) rigid and affine.</p>
<p>At the moment I use point registration and then Elastix, it works in same patients, but not for all.</p>

---

## Post #5 by @Peter_Jan (2025-12-14 20:58 UTC)

<p>Maybe I do something wrong, but I am not moving forward.</p>

---

## Post #6 by @pieper (2025-12-14 21:14 UTC)

<p>If you can, share your data for others to try.  Otherwise just practice with the SampleData.</p>

---

## Post #7 by @Peter_Jan (2025-12-15 21:23 UTC)

<p>It is a perfect idea. I would be greatfull, if you would try. I share th CTs with you. Many thanks</p>

---

## Post #8 by @Peter_Jan (2025-12-15 21:47 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15oOc-zkzC66zlKT3tAyONwvApdo-7eUX%2Fview%3Fusp%3Ddrive_link&amp;dsh=S219002611%3A1765835276448229&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15oOc-zkzC66zlKT3tAyONwvApdo-7eUX%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ac2yZaULS5ZEPBfoApvvJh2j_iF8rCJWyDoqmcrjerVWPiE_00EvEle23KiISvQ4Z33Dv64Z4us30Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15oOc-zkzC66zlKT3tAyONwvApdo-7eUX%2Fview%3Fusp%3Ddrive_link&amp;dsh=S219002611%3A1765835276448229&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15oOc-zkzC66zlKT3tAyONwvApdo-7eUX%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ac2yZaULS5ZEPBfoApvvJh2j_iF8rCJWyDoqmcrjerVWPiE_00EvEle23KiISvQ4Z33Dv64Z4us30Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15oOc-zkzC66zlKT3tAyONwvApdo-7eUX%2Fview%3Fusp%3Ddrive_link&amp;dsh=S219002611%3A1765835276448229&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F15oOc-zkzC66zlKT3tAyONwvApdo-7eUX%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ac2yZaULS5ZEPBfoApvvJh2j_iF8rCJWyDoqmcrjerVWPiE_00EvEle23KiISvQ4Z33Dv64Z4us30Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2025-12-16 06:05 UTC)

<p>Your images have several strange properties, any of them may can cause an automatic intensity-base image registration methods to struggle:</p>
<ul>
<li>Most registration methods generally require the images cover the same region. Your images do not meet this requirement. To fix this, probably the easiest is to crop the images to approximately to the same region.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9840325ef433d256291362077ddda9e3337dc162.jpeg" data-download-href="/uploads/short-url/lIS7dzLplE0RACCFW4KkzGkgvvA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/9840325ef433d256291362077ddda9e3337dc162_2_690x409.jpeg" alt="image" data-base62-sha1="lIS7dzLplE0RACCFW4KkzGkgvvA" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/9840325ef433d256291362077ddda9e3337dc162_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9840325ef433d256291362077ddda9e3337dc162.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9840325ef433d256291362077ddda9e3337dc162.jpeg 2x" data-dominant-color="003E1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">936×556 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>The image edges coincide edge of anatomy (skull touches the image edge). This is an issue because image processing methods often need to extrapolate a little bit beyond the image region and this extrapolation will fail if the intensity near the image edge is non-uniform (it is fine if the image edge cuts through the middle of tissue or cuts through the middle of air, but the image edge should not be at an anatomical region boundary).</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b0b09c2ded977b0101a7e58f7e45e1850085318.jpeg" data-download-href="/uploads/short-url/cZp689obAet7cBpkdNHvHLPR8gM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b0b09c2ded977b0101a7e58f7e45e1850085318_2_690x410.jpeg" alt="image" data-base62-sha1="cZp689obAet7cBpkdNHvHLPR8gM" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b0b09c2ded977b0101a7e58f7e45e1850085318_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b0b09c2ded977b0101a7e58f7e45e1850085318.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b0b09c2ded977b0101a7e58f7e45e1850085318.jpeg 2x" data-dominant-color="04421E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">909×541 65.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>There is resampling artifact near the image edges. It would be better to cut them off.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922417eb84792807d85d92280a5c09e2ca3ebf6c.jpeg" data-download-href="/uploads/short-url/kQP2vKJErBcNezD3ZsMyTHNjfdO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/922417eb84792807d85d92280a5c09e2ca3ebf6c_2_690x468.jpeg" alt="image" data-base62-sha1="kQP2vKJErBcNezD3ZsMyTHNjfdO" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/922417eb84792807d85d92280a5c09e2ca3ebf6c_2_690x468.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922417eb84792807d85d92280a5c09e2ca3ebf6c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922417eb84792807d85d92280a5c09e2ca3ebf6c.jpeg 2x" data-dominant-color="A09F9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">806×547 43.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Image intensity range is off. Most medical images are in the range of +/- few thousand, while yours are in few ten thousands. This may result in default registration presets not working ideally on the images.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9f09857812af7346c070d5030c972fd180f16b5.png" data-download-href="/uploads/short-url/v5Z5bFksRIzeOv2RESyfMwu6kxT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9f09857812af7346c070d5030c972fd180f16b5_2_690x266.png" alt="image" data-base62-sha1="v5Z5bFksRIzeOv2RESyfMwu6kxT" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9f09857812af7346c070d5030c972fd180f16b5_2_690x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9f09857812af7346c070d5030c972fd180f16b5_2_1035x399.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9f09857812af7346c070d5030c972fd180f16b5.png 2x" data-dominant-color="CCD0D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1067×412 18.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As a general advice, try to go back to the original DICOM images as they don’t have these issues. All the problems above are due to incorrect post-processing.</p>
<p>Registration toolkits such as Elastix are quite robust, so it may still be able to register your images successfully, especially if you simplify the registration problem. If you need to register skulls of adults a few years apart then rigid registration should align them well and that is a much simpler task than deformable registration. Therefore, you can increase the chance of successful registration by using a rigid registration preset (<code>generic rigid (all)</code>).</p>

---

## Post #10 by @Peter_Jan (2025-12-16 23:23 UTC)

<p>Thanks you very much for your detail analysis. I try it, source DICOM data, Elastix registration, generic rigid (all), no better outcome.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23af018fcc5beb49fdd3d68fa9ade51efd6bbb24.jpeg" data-download-href="/uploads/short-url/55FEWdz3o2yvnVtmdOT7HfIcGnG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23af018fcc5beb49fdd3d68fa9ade51efd6bbb24_2_676x500.jpeg" alt="image" data-base62-sha1="55FEWdz3o2yvnVtmdOT7HfIcGnG" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23af018fcc5beb49fdd3d68fa9ade51efd6bbb24_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23af018fcc5beb49fdd3d68fa9ade51efd6bbb24_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23af018fcc5beb49fdd3d68fa9ade51efd6bbb24_2_1352x1000.jpeg 2x" data-dominant-color="808186"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1386×1025 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2025-12-16 23:28 UTC)

<p>Interesting. For me, Elastix registered the images you shared with the rigid preset.</p>
<p>If you share another pair that you have problem with registering then we can have a look.</p>

---

## Post #12 by @Peter_Jan (2025-12-20 08:19 UTC)

<p>It is not a problem, I can share another patient. Basically, I pass another patients, tried to change generic, generic rigid (all), 3D CT monomodal head and neck. Every option work with different accurancy.</p>
<p>I’m wondering if it wouldn’t be a good idea to review my approach.</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d4183ea7b8f054a0d60303ba83fa63ea850a611.jpeg" data-download-href="/uploads/short-url/8JTutBE24UzIpoKTzMn2oAmCCUV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d4183ea7b8f054a0d60303ba83fa63ea850a611_2_690x304.jpeg" alt="image" data-base62-sha1="8JTutBE24UzIpoKTzMn2oAmCCUV" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d4183ea7b8f054a0d60303ba83fa63ea850a611_2_690x304.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d4183ea7b8f054a0d60303ba83fa63ea850a611_2_1035x456.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d4183ea7b8f054a0d60303ba83fa63ea850a611_2_1380x608.jpeg 2x" data-dominant-color="AEAEB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2544×1123 356 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/270fa5f505249824b3e45519b18acaf20e62f8cc.jpeg" data-download-href="/uploads/short-url/5zy99pTSwYf79TXvb5v2f8YaJAM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/270fa5f505249824b3e45519b18acaf20e62f8cc_2_690x305.jpeg" alt="image" data-base62-sha1="5zy99pTSwYf79TXvb5v2f8YaJAM" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/270fa5f505249824b3e45519b18acaf20e62f8cc_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/270fa5f505249824b3e45519b18acaf20e62f8cc_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/270fa5f505249824b3e45519b18acaf20e62f8cc_2_1380x610.jpeg 2x" data-dominant-color="B1B0B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2528×1119 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Peter_Jan (2025-12-20 08:27 UTC)

<p>link for another CT scan:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1nyB_Rd90ErfAsCI30vep_jcQozRS5s7F%2Fview%3Fusp%3Ddrive_link&amp;dsh=S1796447439%3A1766219205431820&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1nyB_Rd90ErfAsCI30vep_jcQozRS5s7F%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ac2yZaX1azCRIBnIfA6CrUYmlz-fVnPCCWxI3B6QBmlzY3-pAARFzh5Zg0S-Xd2qTn23AYUc0arZWw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1nyB_Rd90ErfAsCI30vep_jcQozRS5s7F%2Fview%3Fusp%3Ddrive_link&amp;dsh=S1796447439%3A1766219205431820&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1nyB_Rd90ErfAsCI30vep_jcQozRS5s7F%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ac2yZaX1azCRIBnIfA6CrUYmlz-fVnPCCWxI3B6QBmlzY3-pAARFzh5Zg0S-Xd2qTn23AYUc0arZWw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1nyB_Rd90ErfAsCI30vep_jcQozRS5s7F%2Fview%3Fusp%3Ddrive_link&amp;dsh=S1796447439%3A1766219205431820&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1nyB_Rd90ErfAsCI30vep_jcQozRS5s7F%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ac2yZaX1azCRIBnIfA6CrUYmlz-fVnPCCWxI3B6QBmlzY3-pAARFzh5Zg0S-Xd2qTn23AYUc0arZWw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>thanks a lot</p>

---
