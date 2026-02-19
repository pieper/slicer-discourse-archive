---
topic_id: 40178
title: "Scale Factor On Images Taken From A Scene Not Working"
date: 2024-11-13
url: https://discourse.slicer.org/t/40178
---

# Scale factor on images taken from a scene not working

**Topic ID**: 40178
**Date**: 2024-11-13
**URL**: https://discourse.slicer.org/t/scale-factor-on-images-taken-from-a-scene-not-working/40178

---

## Post #1 by @OwenProulx (2024-11-13 17:52 UTC)

<p>Whenever I try to increase the scale factor of an image I’m taking of a scene, the resolution doesn’t increase and the image is split into many identical images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f2d7c2b2a79642870ab5deabad2548a7c7e936d.png" data-download-href="/uploads/short-url/biraCRzBpFi9YijxXFS8oFVyHi5.png?dl=1" title="Screenshot 2024-11-13 094829" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f2d7c2b2a79642870ab5deabad2548a7c7e936d.png" alt="Screenshot 2024-11-13 094829" data-base62-sha1="biraCRzBpFi9YijxXFS8oFVyHi5" width="593" height="490"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-13 094829</span><span class="informations">593×490 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7874eacf9ea9af4ef1d60bc886cb8bccdd393322.jpeg" data-download-href="/uploads/short-url/hbBN0xWMesZnkJ6l9SgferFPaqm.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7874eacf9ea9af4ef1d60bc886cb8bccdd393322_2_690x401.jpeg" alt="Screenshot_2" data-base62-sha1="hbBN0xWMesZnkJ6l9SgferFPaqm" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7874eacf9ea9af4ef1d60bc886cb8bccdd393322_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7874eacf9ea9af4ef1d60bc886cb8bccdd393322_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7874eacf9ea9af4ef1d60bc886cb8bccdd393322_2_1380x802.jpeg 2x" data-dominant-color="110E0A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1920×1117 94.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-11-13 18:08 UTC)

<p>That functionality is broken. Please use the HiResScreenCapture module in SlicerMorph instead.</p>
<p>See the tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/HiResScreenCapture" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/HiResScreenCapture at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #3 by @OwenProulx (2024-11-13 18:24 UTC)

<p>I’m not able to find that module. I have the latest version of Slicer Morph, and have looked at  the tutorial<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de8fca12fe0bf2c0f9362960100bbffe5296410e.png" data-download-href="/uploads/short-url/vKS44zCVzeh10QaFYNisiIbtjNs.png?dl=1" title="Screenshot 2024-11-13 102125" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de8fca12fe0bf2c0f9362960100bbffe5296410e_2_690x320.png" alt="Screenshot 2024-11-13 102125" data-base62-sha1="vKS44zCVzeh10QaFYNisiIbtjNs" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de8fca12fe0bf2c0f9362960100bbffe5296410e_2_690x320.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de8fca12fe0bf2c0f9362960100bbffe5296410e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de8fca12fe0bf2c0f9362960100bbffe5296410e.png 2x" data-dominant-color="202327"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-13 102125</span><span class="informations">781×363 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/734505f33c8ebe526a1e6a456e3540d49de8ddb4.png" data-download-href="/uploads/short-url/grIN1w31PThwyJSoJSqYytCM13S.png?dl=1" title="Screenshot 2024-11-13 102407" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/734505f33c8ebe526a1e6a456e3540d49de8ddb4.png" alt="Screenshot 2024-11-13 102407" data-base62-sha1="grIN1w31PThwyJSoJSqYytCM13S" width="661" height="442"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-13 102407</span><span class="informations">661×442 6.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-11-13 18:34 UTC)

<p>That module is only available for Preview versions, since I requires some recent changes to the Slicer.</p>

---
