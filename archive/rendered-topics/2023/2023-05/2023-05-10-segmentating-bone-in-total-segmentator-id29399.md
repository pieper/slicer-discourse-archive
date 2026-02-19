---
topic_id: 29399
title: "Segmentating Bone In Total Segmentator"
date: 2023-05-10
url: https://discourse.slicer.org/t/29399
---

# Segmentating bone in Total Segmentator

**Topic ID**: 29399
**Date**: 2023-05-10
**URL**: https://discourse.slicer.org/t/segmentating-bone-in-total-segmentator/29399

---

## Post #1 by @KEF (2023-05-10 12:14 UTC)

<p>Hello<br>
I am new to 3D slicer and I am currently testing it to segment bone. I just downloaded the Total segmentator extention and tried to apply it to a CT of two legs. When the prosess finished it curiously only chose the femur, but I also need the tibia, fibia and the foot. Does anyone know why this happen? What do I need to do for it to also segment the rest?<br>
I am using slicer version 5.2.2<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/260a6a5a08d6ceccf3a776cabdaa3e39aa71472a.jpeg" alt="3D" data-base62-sha1="5qwsrNXsoGuRnvXnyTbPkB8Qvc6" width="564" height="352"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/164fcdb538ccf36c59e4d2ae05097c2525f1ab8f.jpeg" alt="bein" data-base62-sha1="3bntVljkrlPrOB8w77UvXO1Lya3" width="580" height="376"></p>

---

## Post #2 by @lassoan (2023-05-10 12:15 UTC)

<p>Unofrtunately, lower extremitties are only <a href="https://github.com/wasserth/TotalSegmentator#subtasks">available in the paying version of TotalSegmentator</a>.</p>

---

## Post #3 by @KEF (2023-05-10 12:25 UTC)

<p>Ok, thank you.<br>
Where would I find the prices for these applications?</p>

---

## Post #4 by @rbumm (2023-05-10 15:42 UTC)

<p>Please contact Jakob Wasserthal, as far as we know there are academic licenses available too.<br>
<a href="https://github.com/wasserth/TotalSegmentator#subtasks">His email is in this text</a>.</p>

---

## Post #5 by @diazandr3s (2023-05-13 19:26 UTC)

<p>Hi <a class="mention" href="/u/kef">@KEF</a>,</p>
<p>You may also consider retraining the whole-body CT segmentation model freely available in the MONAI model zoo: <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation" class="inline-onebox" rel="noopener nofollow ugc">model-zoo/models/wholeBody_ct_segmentation at dev · Project-MONAI/model-zoo · GitHub</a></p>
<p>You could take advantage of the active learning capabilities of the MONAI Label library to get a model for the lower extremities segmentation.</p>
<p>We could consider presenting this as a Slicer project: <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/" class="inline-onebox" rel="noopener nofollow ugc">NA-MIC Project Weeks | Website for NA-MIC Project Weeks</a></p>
<p>Happy to help. Let me know.</p>
<p>Andres</p>

---

## Post #6 by @zariliusra (2023-10-01 03:48 UTC)

<p>Is there any tutorial on how to use it?</p>
<p>Or if i already have TotalSegmentator bone weigth , how to use it with monailabel?</p>

---

## Post #7 by @diazandr3s (2023-10-03 19:39 UTC)

<p>Hi <a class="mention" href="/u/zariliusra">@zariliusra</a>,</p>
<p>Have you tried the whole-body CT segmentation model? <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation" rel="noopener nofollow ugc">https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation</a></p>
<p>You can use this model in MONAI Label like any other MONAI Bundle. Here is more information: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle</a></p>
<p>Another option is to create the label files from the TotalSegmentator dataset with only bones (or the labels you wish) and train the segmentation model from the <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#segmentation" rel="noopener nofollow ugc">radiology app</a> in MONAI Label.</p>
<p>Once you create the label files, please these steps: <a href="https://youtu.be/KtPE8m0LvcQ?si=Ol2AMebXCdjRLgQ_&amp;t=456" rel="noopener nofollow ugc">https://youtu.be/KtPE8m0LvcQ?si=Ol2AMebXCdjRLgQ_&amp;t=456</a></p>
<p>Hope this helps</p>

---

## Post #8 by @diazandr3s (2023-10-09 11:11 UTC)

<p>Hi <a class="mention" href="/u/zariliusra">@zariliusra</a>,</p>
<p>I’ve trained a MONAI Label model to segment only bone: <a href="https://drive.google.com/drive/folders/1yQ3Yy89uwPPmm3zr3ekV5jg37Y7_hF0j?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">radiology_bone - Google Drive</a></p>
<p>It uses the TotalSegmentatorV1 dataset. The model isn’t perfect but it works decently.</p>
<p>Download those files, place them in a folder (i.e. radiology_bone) and start a MONAI Label server using this command:</p>
<blockquote>
<p>monailabel start_server --app /PATH_TO_FOLDER_radiology_bone --studies /PATH_TO_YOUR_NIFTI_OR_NRRD_IMAGES --conf models segmentation</p>
</blockquote>

---

## Post #9 by @mau_igna_06 (2023-10-09 13:48 UTC)

<p>Hi</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="8" data-topic="29399">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>I’ve trained a MONAI Label model to segment only bone: <a href="https://drive.google.com/drive/folders/1yQ3Yy89uwPPmm3zr3ekV5jg37Y7_hF0j?usp=sharing" rel="noopener nofollow ugc">radiology_bone - Google Drive</a></p>
</blockquote>
</aside>
<p>May be it would be of the interest of the community to have such training command/script <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Could you share it? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @diazandr3s (2023-10-09 14:19 UTC)

<p>Hi <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>,</p>
<p>The folder I’ve shared is a MONAI Label app (radiology app) that works for bone segmentation.<br>
With this app, you can do both inference and training - as with any other MONAI Label app.</p>
<p>In the <em>lib/configs/segmentation.py</em> file you can see the labels this model can segment and the network used.</p>

---

## Post #11 by @zariliusra (2023-10-09 14:43 UTC)

<p>Thank you very much. It is really amazing how the experts are helping newbie researchers in this forum.  <img src="https://emoji.discourse-cdn.com/twitter/flushed.png?v=12" title=":flushed:" class="emoji" alt=":flushed:" loading="lazy" width="20" height="20"></p>

---
