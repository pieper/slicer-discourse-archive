# Alter Individual Image Slice Origins in a Node

**Topic ID**: 16905
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/alter-individual-image-slice-origins-in-a-node/16905

---

## Post #1 by @Gabriel (2021-04-01 13:09 UTC)

<p>Hello Everyone, I am working on a project where I will receive UltraSound images (in TIFF format). However the US images are taken from a robotic arm so will not all have the same origin or spacing between images. The origin and spacing data is encoded into the file name (using the end effector position) . Is it possible to take this information and alter individual slices’ origin and spacing?</p>
<p>I am very new to 3D slicer so apologies if this is trivial but I would be extremely grateful for any directions to head in.</p>
<p>(NB. Attempting to add these to a module but learning about that too)</p>

---

## Post #2 by @lassoan (2021-04-01 17:29 UTC)

<p>Yes, you can reconstruct volumes from arbitrarily oriented ultrasound slices, either in real-time, as the frames are required, or retrospectively from a set of recorded position-tracked ultrasound frames.</p>
<p>As far as I remember this video shows all the steps how to set this up, but if you have any questions then let us know:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>


---

## Post #3 by @Gabriel (2021-04-04 17:05 UTC)

<p>Thank you Andras. I think perhaps I oversold how in depth I was going/ overestimated how much I could do myself!</p>
<p>Forgetting about the 3D model, would there be a way to simply make a volume (only thinking about slice model), where I change individual slice spacing and the x,y co-ordinate? (The yaw value/ orientation is the same for all slices)</p>

---

## Post #4 by @lassoan (2021-04-18 13:49 UTC)

<p>If you only need to shift by whole voxels and don’t need to rotate then you can get the volume as numpy array and use standard numpy array operations to shift values.</p>

---

## Post #5 by @Gabriel (2021-04-19 13:58 UTC)

<p>I assume Slicer discourse wants to discourage simple posts of ‘thank you’ by sending me to the like button, but as I have a few questions and you seem to be incredibly helpful and engaged, I’ll say<br>
Thank you very much for all of your help, it’s very much appreciated that you’re taking your time to help me better understand this software. It’s exciting to learn and get to grips with what it can do.<br>
In future I’ll just leave the like and avoid cluttering anyone’s inbox!</p>

---

## Post #6 by @lassoan (2021-04-19 14:28 UTC)

<p>Thank you very much, it is great to hear this. It would be awesome if you could write a short post in the <a href="https://discourse.slicer.org/c/community/success-stories/29">Success stories</a> category where you describe what was your task and how you could accomplish it with help of 3D Slicer and the community.</p>

---

## Post #7 by @Gabriel (2021-04-19 14:40 UTC)

<p>Yes I will definitely do that! I’m currently working through a particular project with a deadline of next week. Hoping to build in as much functionality as I can before then, and will write a summary of how you all have helped. Mid writing this reply someone (James Butler) has just answered a question - so quick!! So hopefully over the next week I can get a lot done and post a great success story.</p>

---
