# SetMatrixTransformToParent consume much time

**Topic ID**: 19455
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/setmatrixtransformtoparent-consume-much-time/19455

---

## Post #1 by @xianger-qi (2021-09-01 07:23 UTC)

<p>There are a problem about my application when i invoke the method SetMatrixTransformToParent of vtkMRMLLinearTransformNode every times. In my MRMLScene there are more than 500 nodes, and executing the method SetMatrixTransformToParent consumes 330 ms.</p>

---

## Post #2 by @pieper (2021-09-01 12:24 UTC)

<p>There must be something else going on in the code, because setting the matrix should not add new nodes.  Please provide exact steps to reproduce what you are seeing.</p>

---

## Post #3 by @lassoan (2021-09-02 05:09 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="19455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>setting the matrix should not add new nodes</p>
</blockquote>
</aside>
<p>As I understand it, there are 500 nodes in the scene, intentionally (that are probably all being transformed).</p>
<aside class="quote no-group" data-username="xianger-qi" data-post="1" data-topic="19455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xianger-qi/48/11944_2.png" class="avatar"> xianger-qi:</div>
<blockquote>
<p>MRMLScene there are more than 500 nodes, and executing the method SetMatrixTransformToParent consumes 330 ms.</p>
</blockquote>
</aside>
<p>There are many ways to improve the performance and the best solution depends on what you would like to achieve.</p>
<p>Can you tell a bit more about your use case?<br>
What kind of nodes are those 500 nodes and what do they represent?<br>
What do you use the transform for?</p>

---

## Post #4 by @xianger-qi (2021-09-02 05:45 UTC)

<p>THANKS FOR YOUR REPLYING!! My case description below.<br>
step 1. In my application, there are only one vtkMRMLScene, and six qMRMLThreeDWidget which reference the same vtkMRMLScene.<br>
step 2. In the scene, i create 126 vtkSphereSource instance, each corresponding one vtkMRMLModelNode， one vtkMRMLModelDisplayNode， one vtkMRMLLinearTransformNode. so all of these will create 378 vtkMRMLNode in the scene. Every vtkMRMLModelNode observes  the vtkMRMLLinearTransformNode and vtkMRMLModelDisplayNode.</p>
<p>step 3. i read 7 stl format files from local, each corresponding one vtkMRMLModelNode， one vtkMRMLModelDisplayNode， one vtkMRMLLinearTransformNode. so all of these will create 21 vtkMRMLNode in the scene. Every vtkMRMLModelNode observes  the vtkMRMLLinearTransformNode and vtkMRMLModelDisplayNode.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/effa17a841a60189715a343f18169c1c4ec3ad40.png" data-download-href="/uploads/short-url/yeVW1OLikNuHV6EiR7zt3PBKo4E.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/effa17a841a60189715a343f18169c1c4ec3ad40_2_690x250.png" alt="image" data-base62-sha1="yeVW1OLikNuHV6EiR7zt3PBKo4E" width="690" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/effa17a841a60189715a343f18169c1c4ec3ad40_2_690x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/effa17a841a60189715a343f18169c1c4ec3ad40.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/effa17a841a60189715a343f18169c1c4ec3ad40.png 2x" data-dominant-color="252827"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">972×353 66.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>step 4 And there are more than 100 vtkMRMLNode created by vtkMRMLScene default. so there are more than 500 vtkMRMLNodes in the scene totally.</p>
<p>step 5. When i trigger the button which will make some linear transform about position and rotation for vtkMRMLLinearTransformNode in step 3. when invokes the method SetMatrixTransformToParent of vtkMRMLLinearTransformNode which will always consume much time.</p>
<p>step6. I print the time consumed for every calls, found this invoke consume more than 300ms. picture below:<br>
file:///home/qxe-work/Pictures/Screenshot%20from%202021-09-02%2001-36-22.png</p>

---

## Post #5 by @xianger-qi (2021-09-02 05:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41575a6ce7a0dfaf691fafaaabc7f4a73e2b7dff.png" data-download-href="/uploads/short-url/9k2bIvKVdsQy9gJqd1qrBFMs5pt.png?dl=1" title="Screenshot from 2021-09-02 01-36-22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41575a6ce7a0dfaf691fafaaabc7f4a73e2b7dff_2_690x448.png" alt="Screenshot from 2021-09-02 01-36-22" data-base62-sha1="9k2bIvKVdsQy9gJqd1qrBFMs5pt" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41575a6ce7a0dfaf691fafaaabc7f4a73e2b7dff_2_690x448.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41575a6ce7a0dfaf691fafaaabc7f4a73e2b7dff_2_1035x672.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41575a6ce7a0dfaf691fafaaabc7f4a73e2b7dff.png 2x" data-dominant-color="202020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-09-02 01-36-22</span><span class="informations">1262×820 78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
supplied for step 6</p>

---

## Post #6 by @lassoan (2021-09-02 06:24 UTC)

<p>Normally you don’t create 126 actors for 126 spheres, but you render them all using a single vtkMRMLMarkupsFiducialNode.</p>
<p>You may call slicer.app.pauseRender() before changing the transform and call slicer.app.resumeRender() after it is changed to ensure no rendering is started while the transform is being updated.</p>
<p>If you need more ideas for optimization then run your code with a profiler and let us know which lines in the code are the performance bottlenecks. A profiler can point out what exactly takes time, not just identify a very high-level calls, such as EndModify().</p>

---

## Post #8 by @xianger-qi (2021-09-02 07:49 UTC)

<p>This is mine conclusion for SetMatrixTransformToParent function:</p>
<p>step1: current transform node block the event response</p>
<p>step2: current transform node set the parent node matrix</p>
<p>step3: parent node sent the modified event (TransformModifiedEvent)   event id = 15000</p>
<p>step4: current node receive the modified event and cache it</p>
<p>step5: current node modify himself maxtrix   (TransformToParent)</p>
<p>step6: current node turn on the event response</p>
<p>step7: current node response the cached event in step4 which is  (TransformModifiedEvent)   for all observers interesting for this event.</p>
<p>AND the step 7 will consume much time now, i don’t know what’s the reason. Is it i add to many nodes which are more than 500 in the scene ?</p>

---

## Post #9 by @lassoan (2021-09-02 19:48 UTC)

<p>Yes, you definitely much more than the average amount of nodes in your scene, so you run into performance issues that normally we just don’t notice. There are many ways to optimize it but it is quite likely that you can just rearrange the information so that it is more efficiently represented in the scene.</p>
<p>Can you tell a bit more about your use case?<br>
What kind of nodes are those 500 nodes? What do they represent?<br>
What do you use the transform for?</p>

---

## Post #10 by @xianger-qi (2021-09-03 01:25 UTC)

<p>there are 126 fiducial point and 7 bone model, every one corresponding one transform node, one display node, one model node, and the model node observes transform node and display node.</p>
<p>transform is about translation and rotation.</p>
<p>there are a question confusing me when i make some transform for transform node, in my view , only the node who observes this transform node will be modify. so why other nodes will response this transform node?</p>

---

## Post #11 by @lassoan (2021-09-03 01:41 UTC)

<aside class="quote no-group" data-username="xianger-qi" data-post="10" data-topic="19455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xianger-qi/48/11944_2.png" class="avatar"> xianger-qi:</div>
<blockquote>
<p>there are 126 fiducial point</p>
</blockquote>
</aside>
<p>Do you have 126 fiducial nodes, each containing a single point? Why don’t you store all the points in one fiducial node?</p>
<p>What do you use the 126 fiducial points for?</p>
<p>Since we don’t know what your overall goal is, it is very hard to help you effectively. We are bogged down with discussing small details, which may not be relevant at all if the problem was approached in a different way. If you tell us what you want to achieve and then we can tell you how it was addressed in the past by others.</p>
<aside class="quote no-group" data-username="xianger-qi" data-post="10" data-topic="19455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xianger-qi/48/11944_2.png" class="avatar"> xianger-qi:</div>
<blockquote>
<p>only the node who observes this transform node will be modify. so why other nodes will response this transform node?</p>
</blockquote>
</aside>
<p>Only those transformable nodes will be notified about transform changes that the transform is applied to. What makes you think that there are more observations?</p>

---

## Post #12 by @xianger-qi (2021-09-06 01:09 UTC)

<p>Thanks a lot, I have find the reason for the problem and fix the bug. the reason for that is I instance too many transform node, actually, i just need to instance one transform node in application.</p>

---
