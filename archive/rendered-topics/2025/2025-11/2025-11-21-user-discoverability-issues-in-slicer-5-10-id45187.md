---
topic_id: 45187
title: "User Discoverability Issues In Slicer 5 10"
date: 2025-11-21
url: https://discourse.slicer.org/t/45187
---

# User Discoverability Issues in Slicer 5.10

**Topic ID**: 45187
**Date**: 2025-11-21
**URL**: https://discourse.slicer.org/t/user-discoverability-issues-in-slicer-5-10/45187

---

## Post #1 by @alireza (2025-11-21 18:45 UTC)

<p>Hey everyone,</p>
<p>I recently upgraded to Slicer 5.10, and I wanted to share some feedback regarding user discoverability. Specifically, I noticed that some commonly used buttons, such as “New Segmentation” and “New Transformation,” seem to have been removed from their previous locations. It took me quite a while to discover that these functionalities are now located under the “Nodes” section under right click. I suspect others might also experience similar difficulties in locating these features.</p>
<p>I’m fairly certain this is all documented, but even with good UI/UX documentation, I still prefer seeing a “create” button directly instead of having to right-click on a node.</p>
<p>With love, from a picky user</p>

---

## Post #2 by @chir.set (2025-11-21 19:20 UTC)

<aside class="quote no-group" data-username="alireza" data-post="1" data-topic="45187">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p>I still prefer</p>
</blockquote>
</aside>
<p>My 2 cents as a user.</p>
<p>Too many buttons clutter a UI, each widget is a call to the eye. A menu can group all these commands so that a module’s widget presents its main functionalities. Developers can’t satisfy each and every user, choices have to be made.</p>
<p>P.S: it’s not clear in what module resides the <code>Nodes</code> section you are referring to.</p>

---

## Post #3 by @alireza (2025-11-21 19:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c69f037d537ade4ba51ac7bf6dba3b62aa6b0771.jpeg" data-download-href="/uploads/short-url/sl5dU8K7VI26sbaAohiSP1n54TD.jpeg?dl=1" title="CleanShot 2025-11-21 at 14.26.52@2x" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c69f037d537ade4ba51ac7bf6dba3b62aa6b0771_2_612x500.jpeg" alt="CleanShot 2025-11-21 at 14.26.52@2x" data-base62-sha1="sl5dU8K7VI26sbaAohiSP1n54TD" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c69f037d537ade4ba51ac7bf6dba3b62aa6b0771_2_612x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c69f037d537ade4ba51ac7bf6dba3b62aa6b0771_2_918x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c69f037d537ade4ba51ac7bf6dba3b62aa6b0771_2_1224x1000.jpeg 2x" data-dominant-color="969695"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2025-11-21 at 14.26.52@2x</span><span class="informations">1920×1567 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Let’s look at this panel in segmentation. As a user, I can see three buttons are grayed out.</p>
<ol>
<li>Add Segment</li>
<li>Remove selected</li>
<li>Show 3D</li>
</ol>
<p>Showing a “Create Segmentation” button is way more helpful than three disabled ones, especially if they can’t be clicked. This is just my two cents, of course. You know your software best, but making things easy for users to find is super important in any UI/UX design.</p>

---

## Post #4 by @muratmaga (2025-11-21 19:42 UTC)

<aside class="quote no-group" data-username="alireza" data-post="3" data-topic="45187">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p>“Create Segmentation” button is way more helpful than three disabled ones,</p>
</blockquote>
</aside>
<p>I haven’t look into the segment editor changes in tdetail, but they are grayed out, since you don’t have a segmentation object in your scene (your node selector is empty).</p>
<p>If you right-click the Node field, you will find your “Create New Segmentation” object, that’s a behavior consistent with how things done in subject hierarchy. Devs are trying to bring consistency to operations in different modules. That makes sense to me.</p>

---

## Post #5 by @chir.set (2025-11-21 19:44 UTC)

<p>But a segmentation is created once and then there’s much to do, often implying creating/removing/showing segments. And all this happen in the <code>Segment editor</code> rather than in the <code>Segmentations</code> module. If we were to create segmentations like from a Gatling gun, then it would make sense to have a <code>Create segmentation</code> button, no offense. The <code>Segment editor</code> allows creating other segmentations very easily.</p>

---

## Post #6 by @alireza (2025-11-21 19:53 UTC)

<p>There’s a similar discoverability issue in the Transformation section, which really highlights my point. It forces users to know about Nodes and their right-click interaction. Naturally, once they’re aware, they’ll use it, but I can’t picture how new users, who’ve never encountered Nodes before, would possibly get onboarded. I am a Slicer user for a long time and never bothered with Nodes. Anyway, as I mentioned in my first post, keep rocking with love!</p>
<p>(New GUI)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7c3cc12b1f1447ec12588e418ba04c0ecae212c.png" data-download-href="/uploads/short-url/zlPqzQWJIiTcvbKqpPB68nJwWm0.png?dl=1" title="CleanShot 2025-11-21 at 14.55.37@2x" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7c3cc12b1f1447ec12588e418ba04c0ecae212c_2_433x500.png" alt="CleanShot 2025-11-21 at 14.55.37@2x" data-base62-sha1="zlPqzQWJIiTcvbKqpPB68nJwWm0" width="433" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7c3cc12b1f1447ec12588e418ba04c0ecae212c_2_433x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7c3cc12b1f1447ec12588e418ba04c0ecae212c_2_649x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7c3cc12b1f1447ec12588e418ba04c0ecae212c_2_866x1000.png 2x" data-dominant-color="B0AFAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2025-11-21 at 14.55.37@2x</span><span class="informations">1666×1920 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>OLD GUI</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c36db5737d17c870a696190d6783bb2d921acfd.png" data-download-href="/uploads/short-url/aSdOI1IcivspfuS3NLflePgEkSV.png?dl=1" title="CleanShot 2025-11-21 at 14.52.14@2x" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c36db5737d17c870a696190d6783bb2d921acfd_2_374x500.png" alt="CleanShot 2025-11-21 at 14.52.14@2x" data-base62-sha1="aSdOI1IcivspfuS3NLflePgEkSV" width="374" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c36db5737d17c870a696190d6783bb2d921acfd_2_374x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c36db5737d17c870a696190d6783bb2d921acfd_2_561x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c36db5737d17c870a696190d6783bb2d921acfd_2_748x1000.png 2x" data-dominant-color="D2D2D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2025-11-21 at 14.52.14@2x</span><span class="informations">916×1222 97.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2025-11-21 19:58 UTC)

<aside class="quote no-group" data-username="alireza" data-post="6" data-topic="45187">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p>It forces users to know about Nodes and their right-click interaction.</p>
</blockquote>
</aside>
<p>I think that’s the point. We are trying to make node operations consistent across different core modules of the Slicer. These has been a part of the Data module for a long time and it is now becoming part of Volumes, Volume Rendering, Segmentaiton, Transforms etc.</p>
<p>It is actually less of a concern for new users. I think you find it an issue, because you are used to doing the way the way you did and now that has changed. New users will simply learn to right-click to do Node operations.</p>

---

## Post #8 by @jamesobutler (2025-11-22 02:48 UTC)

<p>The company that I’m at has a dedicated UX team and from them I have learned that redundancy is not a UX problem to avoid. Therefore Slicer can continue to move to qMRMLSubjectHierarchyTreeView objects consistently across modules instead of the more limited qMRMLNodeCombobox objects, but it can also have specific buttons to create new node types in a given module. Since creation of a node type is often one of the “primary” actions of the module, it is beneficial to have it both be clear and available as a button, but can also be available as a right-click context menu in the tree view. The tree view’s advantage was to provide context about other nodes in the subject hierarchy. It’s advantage was not about a better experience creating a node from an empty/minimal scene.</p>

---

## Post #9 by @alireza (2025-11-22 03:13 UTC)

<p>I agree mostly with you. My main point is that things are not discoverable anymore, and more importantly if we’re removing a feature that’s been around for a decade (or more?) from the GUI, it would be pretty helpful to include a welcome message, a hint, or a modal pop-up letting users know, “Hey, by the way, we’ve removed this, and you can now right-click instead.” maybe it is somewhere but again not discoverable enough?</p>

---
