# Setting the grayscale model maker location

**Topic ID**: 7319
**Date**: 2019-06-26
**URL**: https://discourse.slicer.org/t/setting-the-grayscale-model-maker-location/7319

---

## Post #1 by @blackfish (2019-06-26 16:51 UTC)

<p>OS: Win 10<br>
Slicer version: 4.11</p>
<p>Expected behaviour: the model will inherit the spatial information (more specifically, the image origin) of the input volume</p>
<p>Actual behaviour: the model appears at a random position and I wasn’t able to use SetOrigin on the model as a vtkMRMLModelNode using python</p>
<p>Another question I have is about the output geometry parameter. I didn’t quite understand what the documentation meant by “Output geometry is the output that contains geometry model” and how this is different from the model itself.</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2019-06-27 04:18 UTC)

<aside class="quote no-group" data-username="blackfish" data-post="1" data-topic="7319">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/71e660/48.png" class="avatar"> blackfish:</div>
<blockquote>
<p>the model will inherit the spatial information (more specifically, the image origin) of the input volume</p>
</blockquote>
</aside>
<p>The volume and the generated model are located at the same physical space. Terefore their origin cannot be at the same position, except the special case when the volume’s origin is at (0,0,0) physical position.</p>
<aside class="quote no-group" data-username="blackfish" data-post="1" data-topic="7319">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/71e660/48.png" class="avatar"> blackfish:</div>
<blockquote>
<p>I didn’t quite understand what the documentation meant by “Output geometry is the output that contains geometry model” and how this is different from the model itself.</p>
</blockquote>
</aside>
<p>I agree, this is overcomplicated wording. “Output geometry” is the model node that will contain the generated surface mesh. Note that Segment Editor module in recent Slicer versions makes “Model maker” and “Grayscale model maker” modules redundant, since 3D surface representation is generated on-the-fly and can be exported to files or model nodes by a few clicks.</p>

---
