# Measurement problems

**Topic ID**: 26907
**Date**: 2022-12-24
**URL**: https://discourse.slicer.org/t/measurement-problems/26907

---

## Post #1 by @robin (2022-12-24 17:15 UTC)

<p>Operating system: Win 10<br>
Slicer version:5.2.1<br>
Expected behavior: measurement in millimetres<br>
Actual behavior: for some models gives a figure such as 6.0+04 for a measured value which must be circa 45 mm (eg max diameter of the acetabulum). The value if this is an exponent is quite impossible.</p>
<p>I can’ find any solution or explanation. Please help!</p>

---

## Post #2 by @lassoan (2022-12-24 17:19 UTC)

<p>You can increase the precision for length display in Units section in application settings.</p>
<p>Could you post a screenshot of how the unexpected value is displayed?</p>

---

## Post #3 by @robin (2022-12-24 17:22 UTC)

<p>Will do thankyou!</p>
<p>Robin</p>

---

## Post #4 by @robin (2022-12-24 17:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab15c50f305e35a78d6de74143398b2fdf0a5730.png" data-download-href="/uploads/short-url/opuhUICBJgOGtZyHRGttBce0IdW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab15c50f305e35a78d6de74143398b2fdf0a5730_2_690x425.png" alt="image" data-base62-sha1="opuhUICBJgOGtZyHRGttBce0IdW" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab15c50f305e35a78d6de74143398b2fdf0a5730_2_690x425.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab15c50f305e35a78d6de74143398b2fdf0a5730.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab15c50f305e35a78d6de74143398b2fdf0a5730.png 2x" data-dominant-color="9D9CB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">878×542 96.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thankyou Andras. Here is another example, The values given from length measurement do not seem to make sense even as exponentials.</p>
<p>Robin</p>

---

## Post #5 by @lassoan (2022-12-24 18:57 UTC)

<p>The values are 40mm and 200mm, which look reasonable. Increase the precision to make the values easier to read.</p>

---

## Post #6 by @robin (2022-12-24 19:03 UTC)

<p>I have done so and am getting consistent results now. Thank you very much for that.</p>
<p>Robin</p>

---

## Post #7 by @robin (2022-12-28 19:44 UTC)

<p>Does anyone know if the size of the length measurement/control point spheres can be reduced relative to the object being measured and if so how? I have not managed to find a way of doing so. I need to measure bone thicknesses of the ilium in different species and these can be quite small and the size of the spheres obstructs good measurement.</p>
<p>But I really do like 3DSlicer it is a powerful tool!</p>
<p>Many thanks</p>
<p>Robin Crompton</p>

---

## Post #8 by @pieper (2022-12-28 20:13 UTC)

<p>Yes, in Slicer that’s called “glyph size” and can be expressed either in mm or as a percent of the display size.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d2c153288e8d26bcd737f1920468943898bedde.png" data-download-href="/uploads/short-url/b0Hd9FxsJhD7En1YlL7YPRC1SiO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d2c153288e8d26bcd737f1920468943898bedde_2_526x500.png" alt="image" data-base62-sha1="b0Hd9FxsJhD7En1YlL7YPRC1SiO" width="526" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d2c153288e8d26bcd737f1920468943898bedde_2_526x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d2c153288e8d26bcd737f1920468943898bedde.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d2c153288e8d26bcd737f1920468943898bedde.png 2x" data-dominant-color="DFE5E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">553×525 48.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Glad Slicer is working for you <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2022-12-28 23:33 UTC)

<p>I would also recommend to switch to the “cross with a dot” glyph type for precise measurements. Note that if “absolute” button is not pressed then the glyph size is relative, so if you zoom in then the glyph does not occlude that much of the image anymore.</p>

---

## Post #10 by @robin (2022-12-29 08:08 UTC)

<p>Thankyou again!</p>
<p>Robin</p>

---

## Post #11 by @robin (2022-12-29 16:48 UTC)

<p>Please, I am sorry to be a nuisance but I can’t find where to do what you suggest, namely :</p>
<p>“I would also recommend to switch to the “cross with a dot” glyph type for precise measurements. Note that if “absolute” button is not pressed then the glyph size is relative, so if you zoom in then the glyph does not occlude that much of the image anymore.”</p>
<p>I should again be much obliged if you could tell me the procedure for doing what you suggest here!</p>
<p>Thanks so much in advance</p>
<p>Robin</p>

---

## Post #12 by @jamesobutler (2022-12-29 17:38 UTC)

<p>See the Markups module documentation linked below. The Display section has an “Advanced” area which includes “Glyph Type”. There is an option to change it to “CrossDot2D”.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#display-section" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#display-section</a></p>

---

## Post #13 by @robin (2022-12-29 17:51 UTC)

<p>Thankyou for such a quick response! The 2D cross glyph looks much better for accurate measurement.</p>
<p>Robin</p>

---

## Post #14 by @robin (2023-01-07 15:38 UTC)

<p>Can you actually section a model along a plane and make measurements especially thicknesses on the cutting plane? If so how?</p>
<p>Thanks very much</p>
<p>Robin</p>

---
