# Dental segmentator output editing

**Topic ID**: 44144
**Date**: 2025-08-20
**URL**: https://discourse.slicer.org/t/dental-segmentator-output-editing/44144

---

## Post #1 by @scarlet (2025-08-20 07:08 UTC)

<p>When I use dental segmentator module on CBCT, some gaps are still left inside the jaw bones. What is the easiest way to fill in that empty space.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8104afba7d864c73003c03e1b43410aa9f23f812.png" data-download-href="/uploads/short-url/iplDkouTek0yHackbxFsFwhSrVU.png?dl=1" title="Screenshot 2025-08-19 163851" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8104afba7d864c73003c03e1b43410aa9f23f812.png" alt="Screenshot 2025-08-19 163851" data-base62-sha1="iplDkouTek0yHackbxFsFwhSrVU" width="398" height="382"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-08-19 163851</span><span class="informations">398×382 76.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Esteban_Barreiro (2025-08-20 21:38 UTC)

<p>You can use the Paint Effect in Segment Editor module, setting an Editable Intensity Range, Inside All Visible Segments.<br>
Also, you can set a Threshold that fill the gaps, so you can know the pixel value of the area you want to to fill, and set the Use For Masking from there, that will automatically create the Editable Intensity Range.<br>
Don’t forget to uncheck the box from the Editable Intensity Range when you finish, otherwise you’ll not be able to work with other pixel values.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/670f8e270344006816204713076514a8bd59ca70.png" data-download-href="/uploads/short-url/eHIvoY9VgyNZjKfSQTAR7wgKcec.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/670f8e270344006816204713076514a8bd59ca70_2_411x499.png" alt="1" data-base62-sha1="eHIvoY9VgyNZjKfSQTAR7wgKcec" width="411" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/670f8e270344006816204713076514a8bd59ca70_2_411x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/670f8e270344006816204713076514a8bd59ca70.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/670f8e270344006816204713076514a8bd59ca70.png 2x" data-dominant-color="333637"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">510×620 30 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc557b89842c63501689293bba5606e2b642fe3e.png" data-download-href="/uploads/short-url/vrabIIT0y6L7S5Ca75irU3SjSuW.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc557b89842c63501689293bba5606e2b642fe3e_2_370x500.png" alt="2" data-base62-sha1="vrabIIT0y6L7S5Ca75irU3SjSuW" width="370" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc557b89842c63501689293bba5606e2b642fe3e_2_370x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc557b89842c63501689293bba5606e2b642fe3e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc557b89842c63501689293bba5606e2b642fe3e.png 2x" data-dominant-color="343738"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">514×694 34.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Thibault_Pelletier (2025-08-26 06:47 UTC)

<p>Hi <a class="mention" href="/u/scarlet">@scarlet</a>,</p>
<p>You may also want to try out the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" rel="noopener nofollow ugc">surface wrap solidify extension</a> for your use case.</p>
<p>Best,<br>
Thibault</p>

---
