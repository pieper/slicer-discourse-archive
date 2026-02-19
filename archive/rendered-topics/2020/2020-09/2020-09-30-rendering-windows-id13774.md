---
topic_id: 13774
title: "Rendering Windows"
date: 2020-09-30
url: https://discourse.slicer.org/t/13774
---

# Rendering windows

**Topic ID**: 13774
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/rendering-windows/13774

---

## Post #1 by @riep (2020-09-30 13:05 UTC)

<p>Hi everyone,</p>
<p>I would have a question on how we can set the rendering window layer of a specific marker.<br>
In the attached figure I have initialize 5 plane nodes with the interaction glyph visible only for the center one.<br>
We can see that the glyph is overlayed by adjacent planes wich is not the rendering I am looking for. I would prefer to have the glyph always in the forground<br>
One trick I have found is to create the central plane after all others. However, this cause me some troubles in my code because I initialize a lot of planes in a specific order.</p>
<p>Is there a way to set the rendering window layer of a specific marker directly.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddf1324125a2300a62903809256566ad653a136d.png" alt="Sans titre" data-base62-sha1="vFohsKvDNiC9bQ1addeB5udfyiN" width="281" height="325"></p>
<p>Thanks a lot for your help,<br>
Pierre</p>

---

## Post #2 by @cpinter (2020-10-03 15:56 UTC)

<p>Hi Pierre,</p>
<p>I have several things here I don’t understand.</p>
<p>So the main goal seems to be to be to interact with many planes grouped together using the glyph of the middle one. Is this correct?</p>
<p>And the problem is that the other planes are rendered on top of the glyph (it’s hard to see but I guess the second plane from the right is rendered above the interaction glyph). Right?</p>
<p>Is it important for you to use this particular glyph, or is it OK to use the one of the transforms? To test this, just create a folder in the Data module, move all planes there, and assign a transform to the folder, then show the interaction of the transform (I guess it’s possible from the right-click menu in Data module, but for sure it is from the Transforms module).</p>

---

## Post #3 by @riep (2020-10-04 06:47 UTC)

<p>Hi Csaba,</p>
<p>Thank you for your reply. You are right, I could have made the figure more demontrative, but you have fully understood the problem.<br>
I will test your proposition.</p>
<p>Meanwhile, I also came out with a solution:<br>
The idea is to update the display by using something like</p>
<blockquote>
<p>MyPlanWithGlyph.GetDisplayNode().clone(LastPlaneCreated.GetDisplayNode())</p>
</blockquote>

---

## Post #4 by @lassoan (2020-10-04 13:43 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you check if you can reproduce this (some interaction widgets in slice view appear below some markups) and if you can, then see if it is possible to fix it by tuning coincident topology offsets?</p>

---

## Post #5 by @riep (2020-10-04 15:02 UTC)

<p>Hi Andras,<br>
Just to clarify, please find attached a more illustrative picture.<br>
The rendering behavior depended also on the plane opacity and color.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a910c021e6839abaf360aa6091c52216e3b12565.png" alt="szd" data-base62-sha1="o7CzYLndZFMmJLu5GAkaeKLPdcN" width="258" height="257"></p>

---

## Post #6 by @riep (2020-10-14 06:06 UTC)

<p>HI Andreas,</p>
<p>I am interested to inverstigate your proposition to tune coincident topology offsets. I have several things that come into the scene (marker, glyph, segmentation) and for now the rendering is not as I would like.<br>
Do you know how can I set different offset for different node?</p>
<p>Best,<br>
Pierre</p>

---

## Post #7 by @lassoan (2020-10-15 04:02 UTC)

<p>We’ll fix order of widget and interaction arrows.</p>
<p>There is some randomness in order of actors appearing in slice views. Z order currently seem to depend on the order the actors are put in the renderer (which depends on the order nodes were added and the order of displayable managers). This randomness is certainly not ideal but users have not complained so far.</p>
<p>Is there any specific problem that you would like to address? Can you post screenshots?</p>
<p>As a workaround, you can bring any actor to the top in slice views by removing the display node from the scene and adding it back.</p>

---

## Post #8 by @riep (2020-10-15 07:43 UTC)

<p>Thanks for your reply,</p>
<p>I have only a little experience in Slicer or VTK library, so my opinion has a limited relevance .<br>
Still, It would be great if we could set the Z order of a displaynode directly from the displaynode API (of a segmentation, marker, model etc…).</p>
<p>I think your last point can effectively solve my rendering issue. However, (after crashing the display multiple times) I am not able to find a way to remove a specific display node (of a Markup Plane for instance) from the scene and adding it back.</p>
<p>Could you help me on this please ?<br>
Cheers!</p>

---

## Post #9 by @lassoan (2020-10-15 14:02 UTC)

<aside class="quote no-group" data-username="riep" data-post="8" data-topic="13774">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/riep/48/9933_2.png" class="avatar"> riep:</div>
<blockquote>
<p>However, (after crashing the display multiple times) I am not able to find a way to remove a specific display node (of a Markup Plane for instance) from the scene and adding it back.</p>
</blockquote>
</aside>
<p>Can you give step-by-step instructions/code snippets of how you managed to crash the application?</p>

---

## Post #10 by @riep (2020-10-15 15:02 UTC)

<p>It’s just that I do not know how to remove a display node from the scene and add it back. I know how to remove a node but not just the displaynode. And I can’t find a code snipped elsewhere.</p>
<p>I tried several things:<br>
getNode(“myplane”).RemoveAllDisplayNodeIDs()<br>
also thinks in class<br>
slicer.app.layoutManager().sliceWidget(“Red”).sliceView().renderWindow()</p>

---

## Post #11 by @lassoan (2020-10-15 20:43 UTC)

<p>Typically you use only one display node, so no need to worry about multiple ones. <code>getNode("myplane").RemoveAllDisplayNodeIDs()</code> does not remove the display nodes from the scene, only does not associate them with the data node anymore.</p>
<p>Instead, for each data node, call GetDisplayNode(), store the returned display node (so that it does not get deleted when it is temporarily removed from the scene), remove the display node from the scene (slicer.mrmlScene.RemoveNode), then add it back (slicer.mrmlScene.AddNode), and then associate it with the data node again (using SetAndObserveDisplayNodeID).</p>

---

## Post #12 by @riep (2020-10-20 13:38 UTC)

<p>Thank you Andras I will look into that.<br>
Cheers,</p>
<p>Pierre</p>

---

## Post #13 by @riep (2021-04-11 15:58 UTC)

<p>Hi Andras, hi all,<br>
I would like to dig up this post. Is there any news on this topic ?<br>
Cheers,</p>

---

## Post #14 by @lassoan (2021-04-18 05:12 UTC)

<p>We don’t plan to change anything related to this in the near future. You can change the Z order of 2D actors by removing the corresponding display nodes from the scene and then re-add them in the desired order.</p>

---
