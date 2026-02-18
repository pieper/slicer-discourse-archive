# Finding the resolution of the data set

**Topic ID**: 42450
**Date**: 2025-04-06
**URL**: https://discourse.slicer.org/t/finding-the-resolution-of-the-data-set/42450

---

## Post #1 by @Chamini (2025-04-06 02:09 UTC)

<p>Hi, I am a new user. I have scanned data sets, reconstructed with NRecon. I want to make them all in the same resolution. For that how can I check the resolution of the data set? I have loaded data set like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6403261a6ba641cc733983cf99e9e1836858d73.jpeg" data-download-href="/uploads/short-url/nIINFsRpaHIg4hnYeswNaWJ3gYP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6403261a6ba641cc733983cf99e9e1836858d73_2_690x419.jpeg" alt="image" data-base62-sha1="nIINFsRpaHIg4hnYeswNaWJ3gYP" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6403261a6ba641cc733983cf99e9e1836858d73_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6403261a6ba641cc733983cf99e9e1836858d73_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6403261a6ba641cc733983cf99e9e1836858d73_2_1380x838.jpeg 2x" data-dominant-color="E6E6EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1400×852 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t see the resolution under ‘Information’. How can I check the resolution of the data set, before proceeding to the next steps.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3be1fc0ccdb7f3c6998feb7a7953cfa40ccd1d0.jpeg" data-download-href="/uploads/short-url/nmxakdKIBm897BmIFQp9XtGP94c.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3be1fc0ccdb7f3c6998feb7a7953cfa40ccd1d0_2_559x500.jpeg" alt="image" data-base62-sha1="nmxakdKIBm897BmIFQp9XtGP94c" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3be1fc0ccdb7f3c6998feb7a7953cfa40ccd1d0_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3be1fc0ccdb7f3c6998feb7a7953cfa40ccd1d0_2_838x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3be1fc0ccdb7f3c6998feb7a7953cfa40ccd1d0.jpeg 2x" data-dominant-color="E9EBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">936×836 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>TIA</p>

---

## Post #2 by @muratmaga (2025-04-06 02:42 UTC)

<aside class="quote no-group" data-username="Chamini" data-post="1" data-topic="42450">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecb155/48.png" class="avatar"> Chamini:</div>
<blockquote>
<p>reconstructed with NRecon. I</p>
</blockquote>
</aside>
<p>Please install the SlicerMorph extension, then open the <code>SkyscanReconImport</code> module, and simply provide the path to the <code>*__rec.log**</code> created by Nrecon.</p>
<p>You can find a sample tutorial here: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/SkyscanReconImport at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #3 by @Chamini (2025-04-07 00:53 UTC)

<p>Hi, Thank you so much. It worked.</p>

---
