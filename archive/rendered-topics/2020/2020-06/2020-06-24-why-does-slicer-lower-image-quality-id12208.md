# Why does Slicer lower image quality?

**Topic ID**: 12208
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/why-does-slicer-lower-image-quality/12208

---

## Post #1 by @Pablo_Javier (2020-06-24 22:41 UTC)

<p>I´ve noticed SLICER lowers image quality ( for example DICOM or jpg images). When I compare images with other types of softwares the quality of that image is much better than with SLICER. Why does SLICER do that? Is there any way of avoiding it?</p>

---

## Post #2 by @pieper (2020-06-24 22:58 UTC)

<p>I’m afraid you will have to provide specific examples of what you mean here.  We go to great lengths to preserve image quality.</p>

---

## Post #3 by @Pablo_Javier (2020-06-26 00:30 UTC)

<p>For example nii images (NMR image). When I open it with Slicer and Brainstorm (Matlab), I´ve noticed that the resolution is worse in Slicer than in Brainstorm (particularly in 3D viewer).</p>

---

## Post #4 by @pieper (2020-06-26 00:43 UTC)

<p>Can you provide screenshots, data, and specific instructions to reproduce?</p>

---

## Post #5 by @Pablo_Javier (2020-06-26 21:15 UTC)

<p>For example a simple jpg image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7baafdcd116c62000181ca8cdadfb6856d7dd3c8.jpeg" data-download-href="/uploads/short-url/hE14JbPiFrvGqyu7CM4K42WJ6Ig.jpeg?dl=1" title="cosmos-galaxies" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7baafdcd116c62000181ca8cdadfb6856d7dd3c8_2_517x291.jpeg" alt="cosmos-galaxies" data-base62-sha1="hE14JbPiFrvGqyu7CM4K42WJ6Ig" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7baafdcd116c62000181ca8cdadfb6856d7dd3c8_2_517x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7baafdcd116c62000181ca8cdadfb6856d7dd3c8_2_775x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7baafdcd116c62000181ca8cdadfb6856d7dd3c8_2_1034x582.jpeg 2x" data-dominant-color="0E2044"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cosmos-galaxies</span><span class="informations">1920×1080 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In Slicer (3D Viewer) looks like that:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbaaac52c903271025e069657a37ef3e84743a57.jpeg" data-download-href="/uploads/short-url/zUlvEJ3ugMCZZVPbRNujd0oX4N1.jpeg?dl=1" title="123" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbaaac52c903271025e069657a37ef3e84743a57_2_517x305.jpeg" alt="123" data-base62-sha1="zUlvEJ3ugMCZZVPbRNujd0oX4N1" width="517" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbaaac52c903271025e069657a37ef3e84743a57_2_517x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbaaac52c903271025e069657a37ef3e84743a57_2_775x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbaaac52c903271025e069657a37ef3e84743a57_2_1034x610.jpeg 2x" data-dominant-color="343F69"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">123</span><span class="informations">1042×615 67.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Low resolution affects any medical images, too.</p>

---

## Post #6 by @lassoan (2020-06-26 22:00 UTC)

<p>By default, the same image resolution is shown in 3D views as in slice views. In extreme cases this may indeed result in lower resolution displayed in 3D views, which might not be want you expect:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58d094cc8d9ac601cde14800feef9bc8bf35c7ec.jpeg" data-download-href="/uploads/short-url/cFGTQ89CvCRJIB8fh2gICCUN9RW.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58d094cc8d9ac601cde14800feef9bc8bf35c7ec_2_690x497.jpeg" alt="image" data-base62-sha1="cFGTQ89CvCRJIB8fh2gICCUN9RW" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58d094cc8d9ac601cde14800feef9bc8bf35c7ec_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58d094cc8d9ac601cde14800feef9bc8bf35c7ec_2_1035x745.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58d094cc8d9ac601cde14800feef9bc8bf35c7ec_2_1380x994.jpeg 2x" data-dominant-color="646961"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1640×1183 547 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you want to decouple 3D view’s resolution from the slice view’s then you can choose one of the “Spacing match Volumes” options in slice view visibility submenu:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c48789697f356cfd0506090a9aebb30daed128.jpeg" data-download-href="/uploads/short-url/76gsqednMGVWwbaOZSWUTSHkJ9S.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31c48789697f356cfd0506090a9aebb30daed128_2_690x487.jpeg" alt="image" data-base62-sha1="76gsqednMGVWwbaOZSWUTSHkJ9S" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31c48789697f356cfd0506090a9aebb30daed128_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31c48789697f356cfd0506090a9aebb30daed128_2_1035x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31c48789697f356cfd0506090a9aebb30daed128_2_1380x974.jpeg 2x" data-dominant-color="70756E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1676×1184 835 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What kind of images do you work with? How large was your slice view?</p>

---

## Post #7 by @Pablo_Javier (2020-06-27 02:29 UTC)

<p>Thank you! Your answer has been really helpful.<br>
Doctors who work with me have problems with the resolution of 3D Slicer images. That´s why I had this question.</p>

---

## Post #8 by @lassoan (2020-06-27 06:27 UTC)

<p>No problem, feel free to ask whenever you have any questions.</p>

---
