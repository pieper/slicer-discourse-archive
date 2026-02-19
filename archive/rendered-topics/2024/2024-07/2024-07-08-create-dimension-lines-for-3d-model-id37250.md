---
topic_id: 37250
title: "Create Dimension Lines For 3D Model"
date: 2024-07-08
url: https://discourse.slicer.org/t/37250
---

# Create dimension lines for 3D model

**Topic ID**: 37250
**Date**: 2024-07-08
**URL**: https://discourse.slicer.org/t/create-dimension-lines-for-3d-model/37250

---

## Post #1 by @park (2024-07-08 05:27 UTC)

<p>Hi all,</p>
<p>I would like to draw dimension lines on a model in the 3D view as shown in the following image.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/186167b8afb67d50fc6d669f5de84b60c8494533.png" alt="캡처" data-base62-sha1="3tG9ek4wSVc7TJaeDKn18eld7Tt" width="214" height="185"></p>
<p>Is there any existing feature in Slicer that provides similar functionality, or would it need to be created from scratch? If it needs to be created, would it be better to use markupsNode or vtkLine?</p>
<p>The dimension line does not need to be interactive, and the values will be provided as input. This feature is simply to provide intuitive model information to the user.</p>
<p>Any information would be very helpful to me.<br>
Thank you</p>

---

## Post #2 by @pieper (2024-07-08 12:43 UTC)

<p>I don’t think there’s anything quite like that.  You can definitely build something up from markups, but writing something custom is probably required.  Note that it’s very hard to make the layout of 3D annotations look like what people expect.</p>

---
