# Trouble with Extension "SurfaceWrapSolidify" 

**Topic ID**: 28331
**Date**: 2023-03-12
**URL**: https://discourse.slicer.org/t/trouble-with-extension-surfacewrapsolidify/28331

---

## Post #1 by @German.Men.Rev (2023-03-12 16:31 UTC)

<p>Hi everybody <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> , first time here on this forum. Hope I chose the right category.<br>
I was having some trouble with the Extension “SurfaceWrapSolidify” . It’s a pelvic CT with a superior pubic ramus fracture , and I think I must be doing something wrong when selecting the “Preserve cracks” option, since I’m getting a bridge of bone where a fracture lines should be ( Image attached)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b659065703354169c80269e1abe99ec247eeb28b.jpeg" data-download-href="/uploads/short-url/q17DkfOpWBEUSQ3f6s5btqcf8DN.jpeg?dl=1" title="Captura de pantalla 2023-03-11 a las 14.52.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b659065703354169c80269e1abe99ec247eeb28b_2_690x431.jpeg" alt="Captura de pantalla 2023-03-11 a las 14.52.13" data-base62-sha1="q17DkfOpWBEUSQ3f6s5btqcf8DN" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b659065703354169c80269e1abe99ec247eeb28b_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b659065703354169c80269e1abe99ec247eeb28b_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b659065703354169c80269e1abe99ec247eeb28b_2_1380x862.jpeg 2x" data-dominant-color="525456"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-03-11 a las 14.52.13</span><span class="informations">1920×1200 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And also after exporting the segmented shell  to Cura software  I’m still getting only support structure on the inner space of the pelvic bone (purple arrow) instead of the infill I set up (100% infill , and 5% support density + line support pattern., and choosing  100% infill , and 5% support density + line support pattern.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9353db86d00bd49ac61cc1fd8c446d78607d1c73.jpeg" data-download-href="/uploads/short-url/l1jQPnGC01AIlS8pCwYRqRf0wUj.jpeg?dl=1" title="Captura de pantalla 2023-03-11 a las 15.42.21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9353db86d00bd49ac61cc1fd8c446d78607d1c73_2_690x431.jpeg" alt="Captura de pantalla 2023-03-11 a las 15.42.21" data-base62-sha1="l1jQPnGC01AIlS8pCwYRqRf0wUj" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9353db86d00bd49ac61cc1fd8c446d78607d1c73_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9353db86d00bd49ac61cc1fd8c446d78607d1c73_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9353db86d00bd49ac61cc1fd8c446d78607d1c73_2_1380x862.jpeg 2x" data-dominant-color="AB9F9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-03-11 a las 15.42.21</span><span class="informations">1920×1200 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance for any tips to get this right.</p>
<p>All best</p>

---

## Post #2 by @lassoan (2023-03-12 17:23 UTC)

<p>To create a model for 3D printing that preserves cracks use “Model” output. The binary labelmap representation of a segmentation may not be able to preserve enough details that are needed for thin cracks.</p>

---

## Post #3 by @tsehrhardt (2023-03-13 17:45 UTC)

<p>For the 3D printing, because you created a shell in SurfaceWrapSolidify with a thickness, Cura is reading that as an outward facing surface basically. You can use SurfaceWrapSolidify to create a solid filled model–when you export the STL, it will be a hollow shell. Then in Cura, you can specify your infill and wall thickness or number of walls.</p>

---

## Post #4 by @German.Men.Rev (2023-03-13 18:36 UTC)

<p>Thanks to you both. I’ll try to make it work <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @German.Men.Rev (2023-03-14 21:33 UTC)

<p>Dear Terrie,</p>
<p>I tried it without clicking on the “create shell” option and got this beautiful solid segmentation ( screenshot number 1).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb7c80aae0729fe337bdf3543ce0cbf22040a0ff.jpeg" data-download-href="/uploads/short-url/t27FFzYkRRRkcf3uCORXBE0iORN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb7c80aae0729fe337bdf3543ce0cbf22040a0ff_2_690x348.jpeg" alt="image" data-base62-sha1="t27FFzYkRRRkcf3uCORXBE0iORN" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb7c80aae0729fe337bdf3543ce0cbf22040a0ff_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb7c80aae0729fe337bdf3543ce0cbf22040a0ff_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb7c80aae0729fe337bdf3543ce0cbf22040a0ff_2_1380x696.jpeg 2x" data-dominant-color="5C5A56"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×971 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And now after exporting it to cura, I was able to control the inside of the pelvis with the infill and got the printing time down to 11h ( 5 h less than the last time) <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20">  (screenshot number 2)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b55a668e12d6b9a015ebdf3f0da7195c19a69ff8.jpeg" data-download-href="/uploads/short-url/pSk6tUohFBHzq17bOTLClrzzOdi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b55a668e12d6b9a015ebdf3f0da7195c19a69ff8_2_690x381.jpeg" alt="image" data-base62-sha1="pSk6tUohFBHzq17bOTLClrzzOdi" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b55a668e12d6b9a015ebdf3f0da7195c19a69ff8_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b55a668e12d6b9a015ebdf3f0da7195c19a69ff8_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b55a668e12d6b9a015ebdf3f0da7195c19a69ff8_2_1380x762.jpeg 2x" data-dominant-color="BAB791"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1061 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So now I was wondering , Is there a way I could get that nice solid segmentation and still preserve the fracture lines  ( green arrow on screenshot number 3), because now they are kind of faded. Maybe something to do with the “split cavities”  ?. The 3d model looks like a healed bone without visible fracture gaps.</p>
<p>PS: love your RibApp ! <img src="https://emoji.discourse-cdn.com/twitter/star_struck.png?v=12" title=":star_struck:" class="emoji" alt=":star_struck:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5dd9cdaf2b24ae69dd44658ba248592fe80e4a8.jpeg" data-download-href="/uploads/short-url/uvWvgnc7zM3kbcXq3WrGBqlDGkg.jpeg?dl=1" title="Captura de pantalla 2023-03-14 a las 22.22.07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5dd9cdaf2b24ae69dd44658ba248592fe80e4a8_2_690x361.jpeg" alt="Captura de pantalla 2023-03-14 a las 22.22.07" data-base62-sha1="uvWvgnc7zM3kbcXq3WrGBqlDGkg" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5dd9cdaf2b24ae69dd44658ba248592fe80e4a8_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5dd9cdaf2b24ae69dd44658ba248592fe80e4a8_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5dd9cdaf2b24ae69dd44658ba248592fe80e4a8_2_1380x722.jpeg 2x" data-dominant-color="5A5A55"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-03-14 a las 22.22.07</span><span class="informations">1920×1006 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @tsehrhardt (2023-03-15 13:02 UTC)

<p>You can adjust the “Carve Holes” to a smaller value like 5.0 mm to see if that gives you what you need. The default of 10mm seems to fill in everything. You might still end up with some holes that need filling.</p>
<p>Thanks for checking out my rib app! Hand bones are next! <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @German.Men.Rev (2023-03-17 12:48 UTC)

<p>Thanks ! I’l try with 5.0mm</p>

---
