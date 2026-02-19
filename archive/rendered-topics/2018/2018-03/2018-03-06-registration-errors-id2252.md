---
topic_id: 2252
title: "Registration Errors"
date: 2018-03-06
url: https://discourse.slicer.org/t/2252
---

# Registration errors

**Topic ID**: 2252
**Date**: 2018-03-06
**URL**: https://discourse.slicer.org/t/registration-errors/2252

---

## Post #1 by @Olof (2018-03-06 16:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b7fd3a26b2574a682bea73782ec67750d020660.png" data-download-href="/uploads/short-url/hCwAYb8lzIf7yTVAcN6Iaq2XqLe.png?dl=1" title="registration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b7fd3a26b2574a682bea73782ec67750d020660_2_690x239.png" alt="registration" data-base62-sha1="hCwAYb8lzIf7yTVAcN6Iaq2XqLe" width="690" height="239" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b7fd3a26b2574a682bea73782ec67750d020660_2_690x239.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b7fd3a26b2574a682bea73782ec67750d020660_2_1035x358.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b7fd3a26b2574a682bea73782ec67750d020660_2_1380x478.png 2x" data-dominant-color="4E3C49"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">registration</span><span class="informations">1907×661 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi Bea,</p>
<p>running shape on large number of hippocampus again, And it seems that registration is going wrong - look at attached image.</p>
<p>I think I asked you before but I am a bit confused why it is doing a such a bad job on getting this aligned.  Any hint on what to do? If it means hands on  - on each HC I cannot do it as the dataset contains almost 800 HC.</p>
<p>I used one HC as template for registration  … wondering if I somehow should create a mean template to get a more characteristic shape to register against … if so how?</p>
<p>Thanks!<br>
Olof</p>

---

## Post #2 by @styner (2018-03-08 18:49 UTC)

<p>Hi Olof<br>
Not sure why you see so many flipping issues, usually we do not see that with hippocampi (as the head and tail sections look quite differently). Can you tell us which version you are using?</p>
<p>Re using a mean shape: that’s only for the procrustes alignment. The parametrization is based mainly on the first order ellipsoid which should not be affected (much) whether you use a mean or individual shape. What you could do is to select a subject that has quite a large hippocampal head as flip template, though not sure that will help necessarily.</p>
<p>Worst case, you would need to manually flip them Anterior-posterio using the -FinalFlip option. It’s actually not too time consuming, as you need to do the QC in any case and the FinalFlip option would be consistent for all the badly oriented data. Of course, it would be much better if you do not need to do the manual flipping.</p>
<p>Martin</p>

---

## Post #3 by @Olof (2018-03-09 13:43 UTC)

<p>Dear Martin,<br>
thanks for your answer! What I´ve done is to download the latest version of Slicer … and SlicerSalt and from their chosen the SPHARM extension. So the tool should be an updated version …. Right?<br>
My thoughts is like yours …. It is a bit confusing that the orientation gets mixed up since … as you say there are quite distinct features in the anterior-posterior, superior-inferior part of the hippocampus.</p>
<p>Am I understanding you correctly? I do the QC, I identify all participants with Flipped hippocampus. I then rerun then using the same registration template but chose the flip option?</p>
<p>Or is there a way to manually edit the registration in images that already been run in SPHARM?</p>
<p>Best<br>
Olof</p>

---

## Post #4 by @styner (2018-03-09 14:22 UTC)

<p>Yes, the latest version of SlicerSalt should be best. Maybe sent us here 3-4 surfaces that show flipped parametrization.</p>
<p>Re flipping them yourself: 2 possibilities:<br>
a) since already computed surfaces are not recomputed, you could remove the SPHARM surfaces of the bad ones, enable the final flip option that you need to make the parametrization correctly aligned and then rerun the whole thing (it should only recompute those that you removed)<br>
b) you could run ParaToSPHARMMeshCLP manually on the command line (or in a script). That tool is the one that performs the parametrization flips.</p>
<p>Option a is likely better/simpler. Maybe there are other options (SPHARM Team, any other input?)</p>
<p>Martin</p>

---
