---
topic_id: 19921
title: "Detect The Collosion Of Models And Change Model Outlook Real"
date: 2021-09-30
url: https://discourse.slicer.org/t/19921
---

# Detect the collosion of models, and change model outlook realtime

**Topic ID**: 19921
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/detect-the-collosion-of-models-and-change-model-outlook-realtime/19921

---

## Post #1 by @xianger-qi (2021-09-30 03:01 UTC)

<p>Hi:<br>
Thanks for your reading. There are a question confused me. In mine scene, there are a femur model, and probe model. I control the probe to grind the femur. I can capture the collision caused by probe and femur. BUT I want to change the femur model outlook realtime. JUSH LIKE BELOW PICTURE</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/020142641c0b3735490a467fc4ed05373310e7d3.png" alt="Screenshot from 2021-09-29 22-45-23" data-base62-sha1="hJEunyFnW8OSrS17B6Yv1OmoTh" width="300" height="200"></p>
<p>the white part is femur bone, and the green part is grinded region, if the probe model contacts the green part,  the triangle cell will be change, the green part will disappear gradually.</p>
<p>how can i implement this effect?</p>

---

## Post #2 by @xianger-qi (2021-09-30 03:02 UTC)

<p>I use vtkcollosiondetectfilter to capture the collosion caused by model nodes.</p>

---

## Post #3 by @mau_igna_06 (2021-09-30 13:36 UTC)

<p>You can detect collisions with that filter you mention inside a periodic timer callback function supposing you have probe position tracked and you can update the femur model polydata using combineModel’s logic to make a boolean difference operation that would remove the material the probe is touching but I have my concers regarding implementation of that, I think it would be easier to use the segmentEditor erase effect to get what you want, you just need a way to get the mouse to move where the probe is. Maybe this last thing is easier to achieve.</p>

---
