---
topic_id: 3544
title: "Having Difficulty Getting Mri To Show Up"
date: 2018-07-20
url: https://discourse.slicer.org/t/3544
---

# Having difficulty getting MRI to show up

**Topic ID**: 3544
**Date**: 2018-07-20
**URL**: https://discourse.slicer.org/t/having-difficulty-getting-mri-to-show-up/3544

---

## Post #1 by @Charles_Forsythe (2018-07-20 19:17 UTC)

<p>Hi everyone,</p>
<p>I am making 3D models of the knee. I ‘paint’ the bones of the knee (on a MRI), then make a 3D model but when I reopen the model the MRI images will not reopen but the paint is still there. Can someone please tell me how to get the MRI data to show back up. Also, I cannot scroll through the painted images when I reopen the file.</p>
<p>Thank you.</p>

---

## Post #2 by @cpinter (2018-07-20 19:37 UTC)

<p>You need to save the scene in order to load back all data that you used. The scene is either a .mrml file (but then many other files are also saved in the folder) or an .mrb file.</p>
<p>See in more detail:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SavingData" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SavingData</a></p>

---

## Post #3 by @Charles_Forsythe (2018-07-20 19:45 UTC)

<p>We are reopening the saved the scene but the MRI images will not come up and we cannot scroll  through the MRI slices. Is there a button I need to click/unclick in Segment Editor, etc? Thanks.</p>

---

## Post #4 by @cpinter (2018-07-20 20:18 UTC)

<p>There is no such button. You give very little information, so I can only guess at what the problem might be. Maybe you need to show the MRI in the slice views?<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/MainApplicationGUI#Slice_Viewers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/MainApplicationGUI#Slice_Viewers</a></p>
<p>You can check what data is available in Slicer in the Data module. There you can also show/hide them.</p>

---

## Post #5 by @Charles_Forsythe (2018-07-20 20:20 UTC)

<p>Cpinter: would you be available to do a screen share with me?</p>

---

## Post #6 by @cpinter (2018-07-20 20:34 UTC)

<p>It would be better if you posted some screenshots or made a short video.</p>

---

## Post #7 by @Charles_Forsythe (2018-07-20 20:37 UTC)

<p>Thanks. We’ll send the video over in 15-20 minutes.</p>

---

## Post #8 by @Charles_Forsythe (2018-07-20 20:59 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24d4245be71470ac29b47eebe1aeb1ea81551d72.jpeg" data-download-href="/uploads/short-url/5fNHt9KrCq4QXNGFT9FCcJytcvE.jpeg?dl=1" title="IMG_1660" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d4245be71470ac29b47eebe1aeb1ea81551d72_2_666x500.jpeg" alt="IMG_1660" data-base62-sha1="5fNHt9KrCq4QXNGFT9FCcJytcvE" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d4245be71470ac29b47eebe1aeb1ea81551d72_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d4245be71470ac29b47eebe1aeb1ea81551d72_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d4245be71470ac29b47eebe1aeb1ea81551d72_2_1332x1000.jpeg 2x" data-dominant-color="92948C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1660</span><span class="informations">2307×1730 1.52 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the first set of pictures. See the next reply for the next set of pictures. Thanks.</p>

---

## Post #9 by @Charles_Forsythe (2018-07-20 21:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe5fc8b6893fa670b57b86417c293ad8c5c2eef3.jpeg" data-download-href="/uploads/short-url/AiiuCkF39lSRpJkai8BbMXUDP7d.jpg?dl=1" title="IMG_1666%203" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe5fc8b6893fa670b57b86417c293ad8c5c2eef3_2_666x500.jpg" alt="IMG_1666%203" data-base62-sha1="AiiuCkF39lSRpJkai8BbMXUDP7d" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe5fc8b6893fa670b57b86417c293ad8c5c2eef3_2_666x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe5fc8b6893fa670b57b86417c293ad8c5c2eef3_2_999x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe5fc8b6893fa670b57b86417c293ad8c5c2eef3_2_1332x1000.jpg 2x" data-dominant-color="524C46"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1666%203</span><span class="informations">3264×2448 974 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The first two photos here show how we cannot see any paint or the MRI images. The last photo shows what we normally expect to see when we open a scene.</p>

---

## Post #10 by @cpinter (2018-07-20 21:16 UTC)

<p>I see you’re using 4.8.1. Could you please try it with the latest nightly version? We have done a lot of development since last November. Thanks!</p>

---

## Post #11 by @Charles_Forsythe (2018-07-20 21:18 UTC)

<p>Ok sounds good. I am downloading it right now and I will let you know how it goes. Thank you very much for your help.</p>

---

## Post #12 by @cpinter (2018-07-20 21:25 UTC)

<p>The way it should work is that whatever you see in Slicer when you save the scene, that’s what you should see when you load it back. So if you have the Four-Up showing the MRI and the segmentation on top when you click Save, then you should see the same thing when you load it back by drag&amp;drop or Add data.</p>
<p>If it doesn’t work with the nightly, then try loading the MRI and the segmentation separately, then save a new scene (in a new folder or an MRB file), then try to load that.</p>
<p>Let me know how it goes.</p>

---

## Post #13 by @Charles_Forsythe1 (2018-07-25 20:54 UTC)

<p>Hey. We ended up playing around with stuff and ultimately got everything figured out. Thank you again for your help and patience.</p>

---
