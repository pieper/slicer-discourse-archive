---
topic_id: 9398
title: "Rotation Around Specific Point"
date: 2019-12-05
url: https://discourse.slicer.org/t/9398
---

# Rotation around specific point

**Topic ID**: 9398
**Date**: 2019-12-05
**URL**: https://discourse.slicer.org/t/rotation-around-specific-point/9398

---

## Post #1 by @Jmarcs (2019-12-05 13:54 UTC)

<p>Is it possible to change the center of rotation of an object in Transform when i move it</p>

---

## Post #2 by @aiden.zhu (2019-12-05 14:26 UTC)

<p>In theory, you  may do a translation by moving the center of object to the origin, do the rotation; then do a reverse-translation by moving back the object.</p>
<p>I am trying to do something on transform but I am also just hitting the road on this transform. I will follow this topic.</p>

---

## Post #3 by @lassoan (2019-12-05 15:07 UTC)

<p>I would not recommend to try to align objects using rotation around specified point, since landmark registration is much more reliable, faster, and accurate: you just specify a few corresponding points on the objects you want to align and you are done - no manual tuning of several sliders are necessary and result is guaranteed to be optimal. There are several landmark registration modules available in Slicer, but probably the most convenient and powerful is Fiducial registration wizard module in SlicerIGT extension.</p>
<p>Anyway, if you still want to do rotation around centerpoint (there are valid uses cases, they are just rare) then you can use this example in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point</a></p>

---

## Post #5 by @lassoan (2019-12-05 18:25 UTC)

<p>The bounding box of the transform interaction widget is set to the boundaries of all the transformed nodes. Therefor you can change the boundary by adding other transformable nodes under the same transform. However, since aligning objects in 3D view by interactive translation and rotation is extremely inefficient (it is an iterative process of translations, rotations, changing view orientation) I would not recommend doing this instead doing direct positioning by placing landmarks on the object you want to align.</p>

---

## Post #6 by @Jmarcs (2019-12-05 18:32 UTC)

<p>I am agree with but my goal is not to align but to move a tooth like orthodontisc appliance with forces and center of rotation</p>

---

## Post #7 by @lassoan (2019-12-05 23:44 UTC)

<aside class="quote no-group" data-username="Jmarcs" data-post="6" data-topic="9398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/43a26b/48.png" class="avatar"> Jmarcs:</div>
<blockquote>
<p>my goal is not to align but to move a tooth like orthodontisc appliance with forces and center of rotation</p>
</blockquote>
</aside>
<p>For this, you can use the script that I referenced <a href="https://discourse.slicer.org/t/rotation-around-specific-point/9398/3">above</a>.</p>

---

## Post #8 by @alexk (2019-12-08 19:37 UTC)

<p>Hello Mr. Lasso, I tested the codes to create a new center of rotation. I do not get the desired result.<br>
When I make the first linear transformation, my object does not turn around the new point.<br>
Can you tell me the correct coding in my case? Here is the <a href="https://my.pcloud.com/publink/show?code=XZcm7bkZmsCKtP2i8hRWAeAOh1QyTHqdbPny" rel="nofollow noopener">model</a> that I’m studying.<br>
Cordially</p>

---

## Post #9 by @lassoan (2019-12-08 20:03 UTC)

<p>Pay attention to which transform you apply to the model and which one you are adjusting with sliders (they are not same).</p>
<p>Also check for any error messages in the console.</p>
<p>If you need more specific help, share a screen capture video of what you do, or save the scene as a bundle (mrb) file and share that.</p>

---

## Post #10 by @alexk (2019-12-19 09:36 UTC)

<p>Hello Mr. Lasso, my concern persists. I join <a href="https://my.pcloud.com/publink/show?code=kZLgUhkZbYOJxUaqt8FGuLK3QpwWr5pecUl7" rel="nofollow noopener">here</a> the model in vtk format and the scene.<br>
I want to rotate the model around himself and not about the axis of the skull base.<br>
Thank you for your help.</p>

---

## Post #11 by @lassoan (2019-12-19 17:27 UTC)

<p>I’ve just tried the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point">script</a> that I posted earlier and it worked well. I’ve recorded it on a <a href="https://1drv.ms/v/s!Arm_AFxB9yqHucN9pd6edw1a1cgxbg?e=x5SJOd">video</a> so that you can see all the steps.</p>

---

## Post #12 by @alexk (2019-12-20 10:06 UTC)

<p>Hello, thanks for the video.<br>
I don’t know why, but I have an error message :<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “”, line 5, in updateFinalTransform<br>
AttributeError: ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsFid’ object has no attribute ‘GetNthControlPointPositionWorld’</p>
<p>I am attaching the <a href="https://my.pcloud.com/publink/show?code=XZkJrhkZY5lhdnsMSX8r7A0Cj8zEJ5uzLTiy" rel="nofollow noopener">video to you.</a></p>
<p>cordially<br>
Alex</p>

---

## Post #13 by @lassoan (2019-12-20 13:52 UTC)

<p>The script is for recent Slicer Preview Releases (currently 4.11.x). Method names are slightly different in latest Slicer Stable Release (currently 4.10.2).</p>

---

## Post #14 by @alexk (2019-12-20 20:55 UTC)

<p>Perfect. Thanks a lot</p>

---

## Post #15 by @Mehran (2023-07-14 16:53 UTC)

<p>new link:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/transforms.html#rotate-a-node-around-a-specified-point" rel="noopener nofollow ugc">Transforms — 3D Slicer documentation</a></p>

---
