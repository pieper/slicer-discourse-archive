# How to align brain CT and MR images？

**Topic ID**: 22080
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/how-to-align-brain-ct-and-mr-images/22080

---

## Post #1 by @yllgl (2022-02-21 04:42 UTC)

<p>I have tried brain rigid image base registration in slicer3d. But the result is not very good. Could any body give my some suggestions about how to register the brain CT and MR image? I don’t want to use landmark method, because I want to do it automatically using python code.<br>
here is my  data.<a href="https://icedrive.net/s/iF8j9w46ZCNw1ZxD2BZR5NRu3B5a" rel="noopener nofollow ugc">download</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4f9c82b6d082e5453aed1b9ac27e56be698145d.png" alt="image" data-base62-sha1="nxrsxU9HHFNYCl33EDAynibGQDX" width="295" height="267"></p>

---

## Post #2 by @simonoxen (2022-02-21 18:36 UTC)

<p>Hi, I just run a rigid registration with SlicerANTs and got a good result. You can probably achieve the same with SlicerElastix.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45c54d071e72c7ba3c6a863887d010cc950a7cf2.jpeg" data-download-href="/uploads/short-url/9XdEXBGoMenvFlEYLTggoTx9b7I.jpeg?dl=1" title="Screenshot 2022-02-21 at 19.30.00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c54d071e72c7ba3c6a863887d010cc950a7cf2_2_690x437.jpeg" alt="Screenshot 2022-02-21 at 19.30.00" data-base62-sha1="9XdEXBGoMenvFlEYLTggoTx9b7I" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c54d071e72c7ba3c6a863887d010cc950a7cf2_2_690x437.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c54d071e72c7ba3c6a863887d010cc950a7cf2_2_1035x655.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c54d071e72c7ba3c6a863887d010cc950a7cf2_2_1380x874.jpeg 2x" data-dominant-color="909097"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-02-21 at 19.30.00</span><span class="informations">3808×2414 664 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can see the ants command in the slicer log and then run the antsRegistrationCLI module from python. Alternatively, you can the see the test in General Registration (ANTs) to see how to run it’s logic.</p>

---
