---
topic_id: 18121
title: "Volumereconstruction Module How Can The Output Volume Be Sav"
date: 2021-06-14
url: https://discourse.slicer.org/t/18121
---

# VolumeReconstruction module: how can the output volume be saved?

**Topic ID**: 18121
**Date**: 2021-06-14
**URL**: https://discourse.slicer.org/t/volumereconstruction-module-how-can-the-output-volume-be-saved/18121

---

## Post #1 by @sunshine (2021-06-14 18:11 UTC)

<p>Operating system:  Win64<br>
Slicer version:  Slicer 4.11.20210226<br>
Expected behavior: Build and save ultrasound volume through module VolumeReconstruction<br>
Actual behavior: The expected output volume is always empty.</p>
<p>Hello everyone,</p>
<p>I am following this <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" rel="noopener nofollow ugc">tutorial video</a>, trying to generate Ultrasound volume.</p>
<p>However, in the Volume Reconstruction module, I was not able to find any function to save the volume, nor rendering the three anatomy planes of the volume.</p>
<p>Here is <a href="https://imgbb.com/mbfRNzF" rel="noopener nofollow ugc">a screenshot</a> of what I have done.</p>
<p>As shown in the screenshot, the output “volume” is a created new volume. I have tried to save/rendering it after “start” reconstruction, after “stop” reconstruction; however, the input “Image_Transducer” image can never be collected by the “Volume.”</p>
<p>I can currently only save an empty volume.</p>
<p>Could anyone please share some idea about how to collect 2D scans into the volume, and then save it as an ultrasound volume data (.nrrd) file?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @lassoan (2021-06-14 18:41 UTC)

<p>It seems that you have not reconstructed any volume. Could you record a sequence into the scene and share that scene as a .mrb file (upload it somewhere and post the link here) so that we can check what’s wrong?</p>

---

## Post #3 by @sunshine (2021-06-14 20:16 UTC)

<p>Hi Iassoan,</p>
<p>Thank you for your reply!</p>
<p>I know how to save a scene, however, I have no idea about how to record a sequence.</p>
<p>Could you please let me know how to record a sequence? It that using the VolumeReconstruction module, or some module else? And is there any relationship between the recorded sequence (saved inside the .mrd file, or a separate file) and a scene?</p>

---

## Post #4 by @lassoan (2021-06-15 14:50 UTC)

<p>You can record tracking and image data using Sequences module as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#recording-node-changes-into-a-sequence-node">here</a>.</p>

---

## Post #5 by @sunshine (2021-06-15 23:25 UTC)

<p>Hi Iassoan,</p>
<p>I recorded a sequence into the scene, however, only with Image_Transducer recorded; I was not able to find the way to record the reformated node with the transform ProbeToTracker applied.</p>
<p>You can find and download the scene file <a href="https://www.dropbox.com/s/j9oi6ys34fj304u/2021-06-15-Scene.mrb?dl=0" rel="noopener nofollow ugc">from here</a>.</p>
<p>In the recorded sequence, you will see the stream without moving, while in reality, the 2D scan was moving inside the ROI from one side to the other.</p>
<p>Please kindly teach me how to record the sequence with the transform ProbeToTracker applied.</p>
<p>You will also see that the output volume from the module VolumeReconstruction is always empty.<br>
Please help me with that problem.</p>
<p>I really appreciate your help!<br>
And please help me</p>

---

## Post #6 by @lassoan (2021-06-17 04:06 UTC)

<p>Add all the nodes that you want to record to the same sequence browser node. If you have trouble with this then tell exactly what you tried (each mouse click), or record a screen capture video of what you did.</p>

---

## Post #7 by @sunshine (2021-06-21 02:43 UTC)

<p>Hi Iassoan,</p>
<p>Please find the <a href="https://www.dropbox.com/s/q4bmd8n0ccxa1j5/2021-06-20-Scene.mrb?dl=0" rel="noopener nofollow ugc">new scene file</a>.<br>
And please watch the <a href="https://www.youtube.com/watch?v=mbT1t1-IiFM" rel="noopener nofollow ugc">detailed screen video</a> that matched that scene file above (.mrb), which shows how exactly I was trying to generate ultrasound volume and record sequence.</p>
<p>Please share any idea that how can I generate non-empty ultrasound volume, and save it.</p>

---

## Post #8 by @lassoan (2021-06-25 21:39 UTC)

<p>Thanks a lot, these scene is very helpful. Except the transformed ROI, everything looks good to me, but even if I remove the transform from the ROI I don’t see the volume being reconstructed.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you please have a look at this?</p>

---

## Post #9 by @sunshine (2021-07-18 23:42 UTC)

<p>Do we have any updates on this problem, please?</p>
<p>Thank you so much in advance!</p>

---

## Post #10 by @Sunderlandkyl (2021-07-19 22:18 UTC)

<p>I’ve made some fixes and updated the volume reconstruction module to work with transformed ROI nodes.<br>
You should be able to try them in the preview build tomorrow.</p>
<p>I noticed that in the scene, you have your reconstructed output in the same sequence browser as your input data. If you are reconstructing from recorded data you will need to remove that sequence from the sequence browser, as it will overwrite the reconstruction results.</p>

---

## Post #11 by @lassoan (2021-07-19 23:57 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="10" data-topic="18121">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>I noticed that in the scene, you have your reconstructed output in the same sequence browser as your input data. If you are reconstructing from recorded data you will need to remove that sequence from the sequence browser, as it will overwrite the reconstruction results.</p>
</blockquote>
</aside>
<p>Good catch! This probably does not happen often, but if it is easy to add a check (maybe when the user starts volume reconstruction) then we could display a warning popup: If user presses OK then the module removes the reconstructed output volume from the sequence; if the user clicks Cancel then nothing happens, the reconstruction does not get started (I don’t think it can ever make sense to have the reconstruction result in the same browser node as the input).</p>

---

## Post #12 by @sunshine (2021-07-20 00:21 UTC)

<p>(post deleted by author)</p>

---

## Post #13 by @Sunderlandkyl (2021-07-20 00:52 UTC)

<aside class="quote no-group quote-modified" data-username="sunshine" data-post="12" data-topic="18121">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3ec8ea/48.png" class="avatar"> sunshine:</div>
<blockquote>
<p>I am not sure I get your point, because the “Volume” is always constructed from new input data. I believe you can verify this from the video I provided, just in the same post where you download the scene file. I never try generating “Volume from recorded data”.</p>
</blockquote>
</aside>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d207ac09d0d97b93790d11f37d47437a0234a77.png" alt="image" data-base62-sha1="b0ilPZDfm8GjP1kKQSV6Vc1qUn5" width="547" height="326"></p>
<p>If you are reconstructing using the sequence browser in the scene, Sequence_2 will overwrite the output node (“Volume”) when the reconstruction has completed.</p>
<aside class="quote no-group quote-modified" data-username="sunshine" data-post="12" data-topic="18121">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3ec8ea/48.png" class="avatar"> sunshine:</div>
<blockquote>
<p>Actually, I believe the problem is not about transformed ROI. I mentioned from the very beginning that, the constructed volume is always EMPTY as I start from sratch (not from recorded data), no matter using transformed ROI or not. The screenshot without using transformed ROI had been uploaded earlier in the Github post, as you requested.</p>
</blockquote>
</aside>
<p>Yes, there were additional fixes to the way that the input transforms were concatenated which should solve the problem. The ability to use transformed a ROI is a new feature. Please try the  preview release tomorrow and let us know if the issue persists.</p>

---

## Post #14 by @sunshine (2021-07-20 14:14 UTC)

<p>Hi Sunderlandkyl,</p>
<p>I just did a test on the preview version.</p>
<p>The good news is, the volume is not empty anymore.<br>
However, the results seem to be weird. Please check <a href="https://ibb.co/bgHJtg0" rel="noopener nofollow ugc">this screenshot</a>.</p>
<p>I have no idea why the volume seems to be super noisy everywhere. I was no able to get even one interpretable cross-section. It seems far from the transducer input.</p>
<p>Could you please share your idea?</p>

---

## Post #15 by @Sunderlandkyl (2021-07-20 16:20 UTC)

<p>Is this a reconstruction from the recorded sequence in the scene?</p>
<p>The tracking in the first 2/3rds of the sequence is quite unstable, causing the ultrasound position to jump around significantly. That would result in a lot of noise in the reconstructed volume.</p>

---

## Post #16 by @sunshine (2021-07-20 19:43 UTC)

<p>Hi Sunderlandkyl,</p>
<p>No, it is from a live stream.</p>
<p>To make everything clear, I did a procedure recording again.<br>
Please check <a href="https://www.youtube.com/watch?v=WV3qAXCXMqA" rel="noopener nofollow ugc">this video recording</a> with the test of the preview version just now.</p>
<p>And here is <a href="https://www.dropbox.com/s/17l3gaufcxi5qdo/2021-07-20-Scene.mrb?dl=0" rel="noopener nofollow ugc">the saved scene file</a>.</p>
<p>If you watch my recorded video, you can see that “Volume_1” is super noisy almost everywhere. To avoid noises, I did just one round volume collection, with no repeat at all.</p>
<p>However, if you load the scene file and replay the saved “Volume_1”, the volume seems fine. Not that Noisy.</p>
<p>Here are two questions:<br>
1. Why so noisy before reloading?<br>
2. Why do the Volume cross-sections seem so “lower-resolution” than the 2D view? Like a down-sampling from the 2D view?</p>
<p>Thank you so much for your help in advance!</p>

---
