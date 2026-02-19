---
topic_id: 5318
title: "Overlaying A Dot On The Camera Stream Using Plus Server And"
date: 2019-01-09
url: https://discourse.slicer.org/t/5318
---

# Overlaying a dot on the camera stream using plus server and slicer module

**Topic ID**: 5318
**Date**: 2019-01-09
**URL**: https://discourse.slicer.org/t/overlaying-a-dot-on-the-camera-stream-using-plus-server-and-slicer-module/5318

---

## Post #1 by @blackfish (2019-01-09 14:00 UTC)

<p>Operating system: win 10<br>
Slicer version: 4.11.0</p>
<p>Expected behavior: be able to draw a dot on top of the RGB camera feed that is input to the slicer module using plus server. Imagine being able to draw a dot on the video feed from this tutorial (<a href="https://www.youtube.com/watch?v=MOqh6wgOOYs" rel="nofollow noopener">https://www.youtube.com/watch?v=MOqh6wgOOYs</a>).<br>
Actual behavior: not able to access the video feed and therefore not able to draw a dot.</p>

---

## Post #2 by @lassoan (2019-01-09 14:04 UTC)

<p>You have access to the video feed in both Plus and Slicer. Where you would like to access the image data?</p>
<p>If you want to access the video feed to burn in the dot, then I would recommend a much better solution: Specify a transform (either in Plus or Slicer) that specifies marker position in the image coordinate system. Then in Slicer, you apply that transform to a small sphere or a markup fiducial point (no programming is needed).</p>

---

## Post #3 by @blackfish (2019-01-09 15:08 UTC)

<p>Hi Andras,</p>
<p>Thanks for your reply!</p>
<p>We would just like to access the stream from Slicer as it is where we establish our transformation pipeline. Is there more specific documentation or command you can guide us to for accessing the video stream?</p>
<p>In this demo video that we have (<a href="https://drive.google.com/file/d/1Za8kdEBrkVg7q2_7IV2kwp_1N11RMfDi/view?usp=sharing" rel="nofollow noopener">here</a>), we put a fiducial on the CT and want to relay that information on the video stream (bottom left window) by leveraging the Aruco marker cube that exists in both CT and real world. However, we were unsuccessful in doing that, which is why our current solution is launching an OpenCV window (the black window in the middle, bottom of the view).</p>
<p>Thank you so much in advance.</p>
<p>Regards,</p>
<p>Tina</p>

---

## Post #4 by @lassoan (2019-01-09 15:24 UTC)

<p>Do you use <a href="https://plustoolkit.github.io/" rel="nofollow noopener">Plus toolkit</a>? It can take care all the tracking, using basically any tracker - from inexpensive Aruco-based tracking to commercial surgical navigation systems.</p>

---

## Post #5 by @blackfish (2019-01-11 14:48 UTC)

<p>Hi Andras,</p>
<p>My team members have attempted to perform the steps you mentioned and these are their follow up questions.</p>
<ol>
<li>
<p>You mentioned that we have access to the video feed. We are trying to develop a custom module (so our own python script) which we can run on Slicer and we would like to grab frames from the video feed using the module and then update them/overlay them with something. What would be the best method to do this?</p>
</li>
<li>
<p>You had also mentioned another solution in which we specify a transform which “specifies marker position in the image coordinate system”. How exactly do we do this?  So far, we have a created a new transform and linked it to a sphere model. As Tina mentioned earlier, we would like a dot to appear on top of our video feed whose position would be updated programmatically in our custom module. By playing around with the "Transforms"module in slicer, we understand that we have the ability to visualize the transform in the form of an array of arrows, spheres, etc but what we are after is a dot appearing in a specific pixel position which we set through our module.</p>
</li>
</ol>
<p>Below is what we were able to display with the Transforms module. The red slice shows our camera feed. This is where we would like our dot to appear. Right now, as you can see from the array of spheres, is just showing the visualization of the transform.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b6aa90c9d9eb622c84a98f59874550e60f57541.png" alt="image" data-base62-sha1="d2HY37ztai9KD9uZgt9d9pz9pm1" width="497" height="280"></p>
<p>Thank you so much for your time. We hope to hear from you soon.</p>
<p>Regards,</p>
<p>Tina</p>

---

## Post #6 by @lassoan (2019-01-11 14:59 UTC)

<aside class="quote no-group" data-username="blackfish" data-post="5" data-topic="5318">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/71e660/48.png" class="avatar"> blackfish:</div>
<blockquote>
<p>We are trying to develop a custom module (so our own python script) which we can run on Slicer and we would like to grab frames from the video feed using the module and then update them/overlay them with something</p>
</blockquote>
</aside>
<p>I would not recommend to burn in modifications into the pixel data, as you can display objects overlaid in slice and 3D views instead. But of course you have easy access to the pixel data from Python (as a numpy array), which allows you to do anything: see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="inline-onebox">Documentation/Nightly/Developers/Python scripting - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="blackfish" data-post="5" data-topic="5318">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/71e660/48.png" class="avatar"> blackfish:</div>
<blockquote>
<p>what we are after is a dot appearing in a specific pixel position which we set through our module</p>
</blockquote>
</aside>
<p>You can create a model node that contains a small sphere marker (see this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">example</a>) and apply the transform to this model to set its position. To make the sphere appear in the slice view, enable slice intersection display in the model’s display node.</p>

---
