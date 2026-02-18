# No 3D model of the bone after I selected 3D rendering

**Topic ID**: 1080
**Date**: 2017-09-18
**URL**: https://discourse.slicer.org/t/no-3d-model-of-the-bone-after-i-selected-3d-rendering/1080

---

## Post #1 by @bogdan (2017-09-18 14:11 UTC)

<p>Hello guys,</p>
<p>First of all, it’s my first time when I’m using 3D Slicer, so please take me easy <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">. Okay, so I’m trying to use Volume rendering on a CT scan from a dog, but the scan doesn’t appear in the 3D model view. I tried several option, but no luck.</p>
<p>I attached a photo with the settings I did so far and I could use your support and advices. What I have to do in order to extract the 3D model from the CT scan?</p>
<p>Thank you.<br>
Bogdan.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c025e64012ec6fde8f784aa498b1d8821bd5e848.jpeg" data-download-href="/uploads/short-url/rpOS9xiBYeHmDjCVp5SJ6UFnWqY.jpg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c025e64012ec6fde8f784aa498b1d8821bd5e848_2_690x388.jpg" alt="1" data-base62-sha1="rpOS9xiBYeHmDjCVp5SJ6UFnWqY" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c025e64012ec6fde8f784aa498b1d8821bd5e848_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c025e64012ec6fde8f784aa498b1d8821bd5e848_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c025e64012ec6fde8f784aa498b1d8821bd5e848_2_1380x776.jpg 2x" data-dominant-color="87889D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1080 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-09-18 14:58 UTC)

<p>In the screenshot what you have looks like a 2D image slice that cannot be rendered as a volume. Use latest nightly version of Slicer. Go to Data module to see what data sets are loaded. Left-click on the eye icon to show/hide in slice views, right-click and choose “Show volume rendering” to show volume rendering of that image.</p>
<p>Click on the small rectangle icon in the title bar of the 3D view “Center the 3D view…” to make sure the volume is in the field of view.</p>

---
