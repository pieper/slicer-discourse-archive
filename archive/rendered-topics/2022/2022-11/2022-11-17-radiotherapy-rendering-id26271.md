# Radiotherapy Rendering

**Topic ID**: 26271
**Date**: 2022-11-17
**URL**: https://discourse.slicer.org/t/radiotherapy-rendering/26271

---

## Post #1 by @Nafise_Hasoomi (2022-11-17 01:02 UTC)

<p>Hello every one<br>
Thank you for your great software<br>
How can I use the segmentation features or use some rendering features after loading a radiotherapy machine? Does it need any programming, python input or any other actions…?<br>
Any help appreciated<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5755790aa64ca86a15f3cac51fdfdf1c245dd435.png" data-download-href="/uploads/short-url/csAFcItmPFNE0adKLg9jcVQpUah.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5755790aa64ca86a15f3cac51fdfdf1c245dd435_2_690x357.png" alt="image" data-base62-sha1="csAFcItmPFNE0adKLg9jcVQpUah" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5755790aa64ca86a15f3cac51fdfdf1c245dd435_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5755790aa64ca86a15f3cac51fdfdf1c245dd435_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5755790aa64ca86a15f3cac51fdfdf1c245dd435.png 2x" data-dominant-color="9496B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1313×680 33.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Mik (2022-11-17 16:31 UTC)

<p>That feature is mainly used for visualization purposes of beam geometry, collision detection between various parts of radiotheraphy machine, but it’s quite unfinished.</p>
<p>You can create a dummy RTPlan in “External Beam Planning” module, and beam with required orientation: gantry, couch, collimator angles, and visualize the beam as well.</p>
<p>What would you like to do with segmentation or rendering?</p>

---

## Post #3 by @Nafise_Hasoomi (2022-11-17 23:03 UTC)

<p>Thank you for your reply<br>
I would like to show different fields on the patient’s body when I load the accelerator and use it for VR.Is that possible or need programming?<br>
Thank you in advance</p>

---

## Post #4 by @Mik (2022-11-18 08:59 UTC)

<p>Can’t say anything about VR. May be <a class="mention" href="/u/cpinter">@cpinter</a> could help?<br>
If you have a CT data with a DICOM RTPlan with according RTSTRUCT and RTDOSE files, you can show segmentation, visualize beam orientation and setup beam eye view. Of course you can use volume rendering to show a CT volume data.</p>

---

## Post #5 by @cpinter (2022-11-18 13:30 UTC)

<p>Whatever you can visualize in the 3D view you can also show in VR, because it just shows the same Slicer scene. More info on <a href="https://slicervr.org">https://slicervr.org</a> including compatible devices, setup, features. No programming required. There is currently no possibility to control Slicer from within VR other than moving the objects, so you’ll need someone who moves the sliders for you etc, or you’ll need to take the headset off and on.</p>

---

## Post #6 by @Nafise_Hasoomi (2022-11-18 22:20 UTC)

<p>Thank you for your great explanation.<br>
I will work on it <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @Nafise_Hasoomi (2022-11-18 23:31 UTC)

<p>Thank you Mik for your help.<br>
With each other, we can provide a better result in our research. Much appreciated.</p>

---
