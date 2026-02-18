# Change reference system

**Topic ID**: 15840
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/change-reference-system/15840

---

## Post #1 by @lorenzo_bennati (2021-02-04 14:56 UTC)

<p>Hi everyone,<br>
I have a Dicom image that is represented in Slicer using the Anatomical coordinate system (RAS namely Right, Anterior and Superior).<br>
I was wondering if it is possible in Slicer to change the reference system moving from the Anatomical coordinate system, to the world reference system, namely XYZ.</p>
<p>Thank you in advice</p>
<p>Lorenzo</p>

---

## Post #2 by @pieper (2021-02-04 15:32 UTC)

<aside class="quote no-group" data-username="lorenzo_bennati" data-post="1" data-topic="15840">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorenzo_bennati/48/8831_2.png" class="avatar"> lorenzo_bennati:</div>
<blockquote>
<p>world reference system, namely XYZ</p>
</blockquote>
</aside>
<p>what do your X, Y, and Z refer to?</p>

---

## Post #3 by @mhalle (2021-02-04 15:58 UTC)

<p>Lorenzo,</p>
<p>To expand on what Steve said, you need to provide a conceptual basis for what you want your final coordinate system to be. X, Y, and Z are just labels.</p>
<p>For example if X, Y, and Z represent world-space coordinates in another software tool like Unity, threejs, or babylonjs, it’s better to think in terms of “up”, “right”, and “front” since toolkits/software often have different mappings of XYZ to those concepts.</p>
<p>A natural mapping of “S” is to “up”, since superior generally refers to “up” on a patient. “A” or anterior is usually “front”. “R”, which is “right” from the patient’s perspective (and left someone looking at the patient from the front) will map to either left or right in your coordinate system.</p>
<p>Once you have the conceptual mapping from RAS to “up”, “front”, and “right” for your destination coordinate system, you can map those concepts whatever XYZ conventions you’d like. You can do this mapping with a change of basis matrix transform, which simply consists of a matrix of unit vectors that transform RAS to whatever XYZ convention you may have. I find that much easier than thinking about the problem as rotations or anything like that.</p>
<p>Also keep in mind that RAS is a right handed coordinate system, and your destination XYZ coordinate system may be left handed. That makes no difference for the change of basis matrix (one of the elements will be negative), but depending on what you’re doing with the data it may impact things like shading.</p>
<p>—Mike</p>

---

## Post #4 by @lassoan (2021-02-04 16:23 UTC)

<p>Yes, labels of the renderer world coordinate system are set to “RAS” by default, but you can just ignore, hide, or <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_view_axis_labels">change them</a> as needed.</p>
<p>You can set any spatial mapping from RAS to world coordinate system (including non-linear warping) for any node by specifying a parent transform.</p>

---
