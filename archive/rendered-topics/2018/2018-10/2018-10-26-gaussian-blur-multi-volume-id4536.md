---
topic_id: 4536
title: "Gaussian Blur Multi Volume"
date: 2018-10-26
url: https://discourse.slicer.org/t/4536
---

# Gaussian blur multi-volume

**Topic ID**: 4536
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/gaussian-blur-multi-volume/4536

---

## Post #1 by @Nicholas.jacobson (2018-10-26 04:33 UTC)

<p>Hello,<br>
We are creating an animation from a multi volume of a beating heart. In order to visualize this properly we need to create a gaussian blur on the image and/or modify frames with in this multi volume. Because we want to keep this in an animation mode, we need all the frames to remain in sequence.</p>
<p>Any advice for how to modify individual frames yet keeping them in the sequence to play?</p>
<p>nick</p>

---

## Post #2 by @lassoan (2018-10-26 05:17 UTC)

<p>You can modify frames of a volume sequence, you just need to enable saving of node modifications into the sequence: go to <em>Sequence browser</em> module and in <em>Synchronized nodes</em> section check the <em>Save changes</em> checkbox in the table (in row of the volume sequence).</p>
<p>Why do you think Gaussian blur would improve visualization? Do you use volume rendering? Do you use Screen Capture module to create video?</p>

---

## Post #3 by @Nicholas.jacobson (2018-10-26 20:34 UTC)

<p>This helps, thanks. The scans we are getting has some noise because they are blood pool based, so we have found a really great result comes from a series of blurs to smooth out the inside of the heart. Then yeah I use volume render and take a screen grab. Its proving to be a very useful tool for our pediatric cardiac medical team.</p>

---

## Post #4 by @lassoan (2018-10-26 21:30 UTC)

<p>Gaussian smoothing makes you lose useful image details. You may obtain better quality images by using non-linear methods, such as median filter or various anisotropic smoothing filters.</p>
<p>We work quite a bit with cardiac MRIs, too. It would be great to share results, best practices, etc. We make our Slicer modules publicly available when we manage to get in sufficient papers. There are a couple of them already in SlicerHeart extension. We’ll make a new module public for cardiac device placement simulation in a few weeks, and we have several other modules in the pipeline.</p>

---

## Post #5 by @Nicholas.jacobson (2018-10-26 22:02 UTC)

<p>This is great. We are using the mulivolume because with infant hearts its hard to get a good noise free image. However, the surgeons want a hollow model with out the blood pool and 3d printed in a flex material so they can dig around in the model. I’ve collaborated with Ahmed Hosney and James Weaver have been using voxel / png printing to get these models printed with more accuracy. However the noise left in the heart after segmentation is not desirable so we have found some success in a slight blur, but I’m open to trying the non-linear based stuff. I work with a team of radiologists, cardiologist and a perdiactric cardio thoracic surgeon and we in the process of utilizing this work in practice for numerous pediatric surgeries. So, yes, any collaboration and advice is welcome and because I work for Colorado University as a researcher, I’m happy to contribute our research.</p>

---

## Post #6 by @rkikinis (2018-10-27 05:53 UTC)

<p>Would it make sense to schedule a hangout to discuss this topic?</p>

---

## Post #7 by @lassoan (2018-10-27 16:10 UTC)

<p>Great idea, I’ll set up a meeting with <a class="mention" href="/u/nicholas.jacobson">@Nicholas.jacobson</a> in a private message.</p>

---

## Post #8 by @sarvpriya1985 (2018-12-27 15:46 UTC)

<p>Hi Nicholas,</p>
<p>I am also working on heart segmentation and creating hollow models. But I have so far worked only on single best phase. Would you pls share how you are segmenting the entire frames and hollowing them to see them as a motion.</p>
<p>Also has anyone tried virtual surgery (I mean creating 3d patches for vsd closure or arterioplasty). I wish to create the exact 3d models for them.</p>
<p>would appreciate all thoughts.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #9 by @Nicholas.jacobson (2018-12-28 01:43 UTC)

<p>Sure we have used the sequences module and modified each frame with similar settings established in the segment editor. Using sequences you can extract each frame individually.</p>
<p>Yes! we are working on getting 3d patches for VSD closures at the moment with initial success.</p>

---

## Post #10 by @sarvpriya1985 (2018-12-28 10:34 UTC)

<p>Thanks for replying Nick. By modifying each frame do you mean segmenting each frame individually. How would then we add them to play as a cine. If possible can u pls share some screenshots of the workflow. Would appreciate.</p>
<p>Also if u can share screenshots of how u go about creating a vsd patch and then apply it.</p>
<p>I saw a virtual reality pedicle screw insertion yesterday and was wondering if I can do the same with vsd patch.</p>
<p>Would appreciate the help.</p>
<p>Thanks</p>
<p>Sarv</p>

---
