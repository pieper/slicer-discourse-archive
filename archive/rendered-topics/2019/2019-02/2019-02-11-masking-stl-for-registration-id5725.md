# Masking STL for Registration

**Topic ID**: 5725
**Date**: 2019-02-11
**URL**: https://discourse.slicer.org/t/masking-stl-for-registration/5725

---

## Post #1 by @miniBin (2019-02-11 14:42 UTC)

<p>Hello I need to do registration on a stl of a vessel but I only need to deform part of the stl because I need the top and bottom of it to be flat. Here is a picture<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc923c385a09779108d5df123b5838e4235ae5a2.png" alt="vessel" data-base62-sha1="A2lD46cSb3k7g9fI0d7ySoC4dUu" width="414" height="424"></p>
<p>I think I can use masking but I’m not sure how? I need to make sure that the top and bottom of the vessel are flat. Thank you.</p>

---

## Post #2 by @miniBin (2019-02-12 14:53 UTC)

<p>My procedure is…</p>
<p>FixedFrame = FrameA<br>
MovingFrame = FrameB</p>
<p>Use ElastiX so FrameB gets transformed into FrameA space.<br>
Change transform to Volume.<br>
Mask Transform Volume with Frame B segment.<br>
Import Masked Transform Volume as Transform.<br>
Apply Transform to FrameB stl.</p>
<p>I do it with masked vs. no mask transform and the results look different?</p>
<p>Frame B stl:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a63402839fb123f60e3773ad0b5a77975be5cd.png" alt="frameB" data-base62-sha1="xc6RqGaiFQAI2LB9JCimoQuyF3v" width="328" height="378"></p>
<p>Resulting stl from non-masked transform (gray)<br>
Resulting stl from masked transform (pink)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/048a36bc2774ad2e686482d1c56a1b737c5e06b7.png" data-download-href="/uploads/short-url/Ea1XtmirrTen7t5ya53q65qt27.png?dl=1" title="result" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/048a36bc2774ad2e686482d1c56a1b737c5e06b7.png" alt="result" data-base62-sha1="Ea1XtmirrTen7t5ya53q65qt27" width="513" height="500" data-dominant-color="837CAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">result</span><span class="informations">530×516 13.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why is there a difference between masked vs non-masked? Shouldn’t the transform only apply to the stl? I am currently masking the transform so I don’t have to deal with all the other data, but shouldn’t it have the same effect on the stl as the non-masked transform?</p>
<p>Sorry if this does not make sense. I can try to explain more.</p>

---

## Post #3 by @pieper (2019-02-13 19:51 UTC)

<aside class="quote no-group" data-username="miniBin" data-post="2" data-topic="5725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e79b87/48.png" class="avatar"> miniBin:</div>
<blockquote>
<p>I can try to explain more.</p>
</blockquote>
</aside>
<p>Yes, I think you need to provide more context - what are you trying to accomplish?</p>

---

## Post #4 by @miniBin (2019-02-13 20:06 UTC)

<p>Hello and thank you for your reply.</p>
<p>I am trying to transform only part of a stl geometry. I want the other part not to be transformed (1 mm down from the top).</p>
<p>Example picture:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7c912dc02c4164f22b8546d9838b24cc783b24.png" alt="scenario" data-base62-sha1="8lozMhqIgr0DMYDv0HRc3T3J2yU" width="684" height="344"></p>
<p>Here is what I have done:</p>
<p>-Create transform from two vessel volumes<br>
-Import transform as volume<br>
-Use segment to mask part that I want “static” and set inside to “0”<br>
-Export masked transform volume<br>
-import masked transform volume as transform<br>
-Import STL of segment of vessel<br>
-Apply transform to STL<br>
-Harden transform</p>
<p>It seems like the mask is not working.<br>
The static part does not stay static and it deforms so the top of the vessel is no longer flat like I need it to be.</p>
<p>I am not sure if my transform mask looks right. It is the gray circle but it seems like it still has a gradient and is not masking properly but I set the value to 0?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a65fbad558f8f3ee9d4c517ead6d8f49cb4832b0.png" alt="maskfail" data-base62-sha1="nJOmkVEzS4VZQRVgwMAnjrPeraU" width="212" height="176"></p>
<p>Sorry for the confusion.</p>

---

## Post #5 by @pieper (2019-02-13 20:19 UTC)

<p>Okay, that helps.  At least I think I get it.  Did you turn on the arrows or grid features of the transform visualization to confirm that your masked transform is really what you think it is?</p>

---

## Post #6 by @miniBin (2019-02-13 20:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0d09d8ad034ce95e14f162450586ff4b0b76756.png" data-download-href="/uploads/short-url/mWDlNWPvMESob9wxrIAVNQajQy2.png?dl=1" title="results" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d09d8ad034ce95e14f162450586ff4b0b76756_2_690x293.png" alt="results" data-base62-sha1="mWDlNWPvMESob9wxrIAVNQajQy2" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d09d8ad034ce95e14f162450586ff4b0b76756_2_690x293.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d09d8ad034ce95e14f162450586ff4b0b76756_2_1035x439.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0d09d8ad034ce95e14f162450586ff4b0b76756.png 2x" data-dominant-color="F8F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">results</span><span class="informations">1322×562 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is a more detailed image of what is happening.</p>

---

## Post #7 by @miniBin (2019-02-13 20:26 UTC)

<p>Yes, I turned the grid on and it is black in those places which is why I am confused. Will update with pics in one second.</p>

---

## Post #8 by @miniBin (2019-02-13 20:41 UTC)

<p>Original:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/217bf0a74315bf4db9dafd00bceffce727eae06f.png" alt="1" data-base62-sha1="4Mdip8x9lNlHTpzn3V29GMeynSL" width="352" height="114"></p>
<p>Segment Mask:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c845e5212fda4223d8bf1331896aa176d881127d.png" alt="2" data-base62-sha1="szHf64ZM1B6H9nqCRDXYQpAFfid" width="400" height="192"></p>
<p>Transform Volume with Mask Applied:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f1751388b65c75ff22343d689117bdeddde8446.png" alt="3" data-base62-sha1="dzdjDr98Jb0br3yAEfnFuCqJ47c" width="412" height="366"></p>
<p>Parameters used:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/362ebaf5f8e4fde9e33a761df02b060bd8456c53.png" data-download-href="/uploads/short-url/7JjTXLkE0r9WDW2oxyUmvS040H9.png?dl=1" title="parameters" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/362ebaf5f8e4fde9e33a761df02b060bd8456c53_2_690x252.png" alt="parameters" data-base62-sha1="7JjTXLkE0r9WDW2oxyUmvS040H9" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/362ebaf5f8e4fde9e33a761df02b060bd8456c53_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/362ebaf5f8e4fde9e33a761df02b060bd8456c53_2_1035x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/362ebaf5f8e4fde9e33a761df02b060bd8456c53.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">parameters</span><span class="informations">1160×424 29.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result grid:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b24a1d34a3225941b0c4ba4db1f96a21c21c8616.png" alt="5" data-base62-sha1="prdMgiuVmo99zNoR2OuLoj4BnPE" width="378" height="372"><br>
Black is applied mostly to my target area but not all the way?</p>
<p>Transformed stl:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d0798c1fb2fb6ccc322b920ac4fea248aed97c8.png" alt="4" data-base62-sha1="aZr2xZoZyxv4ylEU2bC5sMdqLDq" width="451" height="106"></p>
<p>Masked part was transformed but it wasn’t supposed to be. Arrows show obvious transformation.</p>
<p>One possible error is that my transform has data to transform a much larger geometry (full heart) whereas I am only transforming part of the vessel. When I try to mask a transform to my specific stl shape/segment the result is very jagged and bumpy which is why I use the full transform.</p>

---

## Post #9 by @miniBin (2019-02-13 20:59 UTC)

<p>There are a few parts that are being completely ignored.</p>
<p>My mask (tan):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72027e415097957be7d5c0084f750c551810912c.png" alt="mymask" data-base62-sha1="ggzLWnYbwtyczAKViPW5OIfcofq" width="560" height="302"></p>
<p>grid result:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/107d2edd6d87c47acf6915224d8bf2a3e2f8aa1c.png" alt="sadness" data-base62-sha1="2lRQgwNqlCJCkbYar7YT2sFSwdm" width="482" height="368"></p>
<p>There is a clear green triangle where the mask is being ignored.</p>

---
