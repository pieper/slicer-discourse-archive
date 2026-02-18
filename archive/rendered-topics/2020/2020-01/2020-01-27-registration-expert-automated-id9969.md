# Registration - expert automated

**Topic ID**: 9969
**Date**: 2020-01-27
**URL**: https://discourse.slicer.org/t/registration-expert-automated/9969

---

## Post #1 by @RadioQuest (2020-01-27 15:08 UTC)

<p>Hi<br>
I am using an Expert Automated registration module to register MR head images with CT. I need this registration so that I can use other maps that are already registered to this CT image.<br>
It seems to be working in one group of my patients. However, for a few other patients, CT slices (DICOM) contain head and Spine. I am not able to do proper registration ( MR head appears to align itself in the chest region) .<br>
Can someone help me with the troubleshooting?<br>
Thanks.</p>

---

## Post #2 by @JanWitowski (2020-01-27 16:48 UTC)

<p>Hi <a class="mention" href="/u/radioquest">@RadioQuest</a><br>
Multimodal (MR to CT) registration is not trivial task unfortunately.</p>
<blockquote>
<p>I need this registration so that I can use other maps that are already registered to this CT image.</p>
</blockquote>
<p>Do you mean labelmaps that are made for CT?</p>
<blockquote>
<p>I am not able to do proper registration ( MR head appears to align itself in the chest region) .</p>
</blockquote>
<p>I had this problem, too, and didn’t find 100% reliable solution here. Maybe someone more experienced can comment, but I had most luck by using <code>General Registration (BRAINS)</code> module with Rigid registration only and higher percentage of samples (~0.02)</p>

---

## Post #3 by @pieper (2020-01-27 17:00 UTC)

<p>In case you didn’t find it:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/Registration" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/FAQ/Registration</a></p>

---

## Post #4 by @lassoan (2020-01-27 20:14 UTC)

<p>“Expert Automated registration module” is just a very simple wrapper over a basic ITK registration method, so it is not that easy to make it work. I would recommend to use SlicerElastix extension instead, which usually works as is, without any parameter tuning, with the default rigid or rigid+bspline parameter set.</p>
<p>Before registration, crop the volumes to cover approximately the same anatomical region. In this case, crop the CT to the head before starting registration. You can still apply the final transform to the original, non-cropped images.</p>

---

## Post #5 by @RadioQuest (2020-01-28 12:08 UTC)

<p>Hi… Yes this are radiation dose maps designed on crank-sacral CT. I need to superimpose them on MR images.<br>
Expert automated reg worked very well with CT  having only Cranial/brain region. Problem is CT has both brain and spinal cord while MR is only brain. I am afraid basic reg is not working. Thanks</p>

---

## Post #6 by @RadioQuest (2020-01-28 12:10 UTC)

<p>Hi Iassoan,<br>
Thanks for your reply. I am afraid Elastix is showing an error. and I am not sure how to crop Cranial region from scan. Even dose maps have both cranium and spinal column. Is there any way where I can just superimpose MR brain on the cranial/brain part of CT? Thanks.</p>

---

## Post #7 by @lassoan (2020-01-28 12:28 UTC)

<aside class="quote no-group" data-username="RadioQuest" data-post="6" data-topic="9969">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/85f322/48.png" class="avatar"> RadioQuest:</div>
<blockquote>
<p>Thanks for your reply. I am afraid Elastix is showing an error</p>
</blockquote>
</aside>
<p>What is the error? Can you attach the log file? (menu: Help / Report a bug)</p>
<aside class="quote no-group" data-username="RadioQuest" data-post="6" data-topic="9969">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/85f322/48.png" class="avatar"> RadioQuest:</div>
<blockquote>
<p>not sure how to crop Cranial region</p>
</blockquote>
</aside>
<p>You can use “Crop volume” module for this. Let us know if you cannot figure out how to use it.</p>
<aside class="quote no-group" data-username="RadioQuest" data-post="6" data-topic="9969">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/85f322/48.png" class="avatar"> RadioQuest:</div>
<blockquote>
<p>Is there any way where I can just superimpose MR brain on the cranial/brain part of CT?</p>
</blockquote>
</aside>
<p>Yes, sure you can do this already. However, if you want to compute the alignment then you may need to use cropped version of the images to guide the automatic registration method. Cropping should take less than a minute and you can use the computed alignment transform on the original (non-cropped) images.</p>

---

## Post #8 by @RadioQuest (2020-01-29 13:41 UTC)

<p>Dear Iasson,<br>
Thank you for your kind guidance. Expert automated registration worked well after cropping CT volume as per your suggestion. I could register Mr with CT properly.<br>
I am grateful for your help, Thanks !<br>
Kind Regards,<br>
RQ</p>

---

## Post #9 by @RadioQuest (2020-01-30 09:42 UTC)

<p>Hi…<br>
After rechecking I realised Expert automated registration was not accurate. and elastic modules was giving some error. Finally , elastic -generic preset worked really well to register MR on CT<br>
Thank you for valuable guidance.<br>
Kind Regards,<br>
RQ</p>

---
