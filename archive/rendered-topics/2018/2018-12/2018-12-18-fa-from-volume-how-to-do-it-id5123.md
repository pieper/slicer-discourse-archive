# FA from volume- how to do it

**Topic ID**: 5123
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/fa-from-volume-how-to-do-it/5123

---

## Post #1 by @Ania (2018-12-18 12:37 UTC)

<p>Dear all,</p>
<p>I am completely new to 3dSlicer, and I’m wondering: Is it possible to estimate FA from concrete ROI/Volume?<br>
I’ve got nii Fractional Anisotropy maps as input. I am able to draw a volume, but I’ve got no idea what’s next.</p>
<p>I would be grateful for any advice.</p>
<p>Ania</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2018-12-18 18:53 UTC)

<p>Hi - it sounds like you just need the Segment Editor and Segment Statistics modules.</p>

---

## Post #3 by @Ania (2018-12-19 11:41 UTC)

<p>Thank you for you reply, Steve.</p>
<p>The problem is, that as I see, with Segment Statistic module I can not obtain Fractional Anisotropy or mean diffusivity.<br>
I tried to use the Diffusion Tensor Scalar Maps segment ( as I can see you can estimate both FA and MD here), but it always says: " No input data assigned to Input DTI Volume" . I try to assign the input but I dont really know how.</p>
<p>Ania</p>

---

## Post #4 by @ihnorton (2018-12-19 12:43 UTC)

<aside class="quote no-group" data-username="Ania" data-post="1" data-topic="5123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/58f4c7/48.png" class="avatar"> Ania:</div>
<blockquote>
<p>I’ve got nii Fractional Anisotropy maps as input.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Ania" data-post="3" data-topic="5123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/58f4c7/48.png" class="avatar"> Ania:</div>
<blockquote>
<p>I tried to use the Diffusion Tensor Scalar Maps segment ( as I can see you can estimate both FA and MD here)</p>
</blockquote>
</aside>
<p>If you already have an FA map calculated in nifti, as in the first quote, then those maps can be used directly as input to the statistics – no need to use the Scalar Maps module.</p>

---

## Post #5 by @Ania (2018-12-19 13:14 UTC)

<p>Thank you Isaiah, I tried to do this, but after I create a volume on this FA maps I cannot choose it as an input…</p>

---

## Post #6 by @Ania (2018-12-20 15:14 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06c20ec02aa13f637e5e630caade6dd27699965a.jpeg" data-download-href="/uploads/short-url/XMD8VGwJJItxbmWQafogNtpqJA.jpeg?dl=1" title="Bez%C2%A0tytu%C5%82u" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06c20ec02aa13f637e5e630caade6dd27699965a_2_690x414.jpeg" alt="Bez%C2%A0tytu%C5%82u" data-base62-sha1="XMD8VGwJJItxbmWQafogNtpqJA" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06c20ec02aa13f637e5e630caade6dd27699965a_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06c20ec02aa13f637e5e630caade6dd27699965a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06c20ec02aa13f637e5e630caade6dd27699965a.jpeg 2x" data-dominant-color="8D8B81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bez%C2%A0tytu%C5%82u</span><span class="informations">941×565 71.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I manage to create that table but I am not sure if the ‘minimum, maximum, mean’ relates to FA.<br>
Of course it is based on FA maps, from which I created a segmentation which I took as an input.</p>
<p>Ania</p>

---

## Post #7 by @ihnorton (2018-12-20 15:17 UTC)

<aside class="quote no-group" data-username="Ania" data-post="6" data-topic="5123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/58f4c7/48.png" class="avatar"> Ania:</div>
<blockquote>
<p>I am not sure if the ‘minimum, maximum, mean’ relates to FA.</p>
</blockquote>
</aside>
<p>Those statistics are calculated for all of the voxels in the selected segment.</p>

---

## Post #8 by @Ania (2018-12-20 15:21 UTC)

<p>Okay, that’s good. Thank you!  But still I don’t know what’s the maximum and minimum (max and min FA or not really?)</p>

---
