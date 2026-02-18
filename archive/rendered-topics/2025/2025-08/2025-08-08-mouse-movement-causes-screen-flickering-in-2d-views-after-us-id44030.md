# Mouse movement causes screen flickering in 2D views after using slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNodeWithTerminology()

**Topic ID**: 44030
**Date**: 2025-08-08
**URL**: https://discourse.slicer.org/t/mouse-movement-causes-screen-flickering-in-2d-views-after-using-slicer-modules-segmentations-logic-importlabelmaptosegmentationnodewithterminology/44030

---

## Post #1 by @baderstine (2025-08-08 16:14 UTC)

<p>When I add a node using slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode() everything is normal. However, when I use slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNodeWithTerminology() instead, I get a lot of screen flickering whenever I move my mouse cursor over the 2D view (axial, sagittal, coronal).  Is there some reason why importing using a terminology would cause screen flickering?  I’m on a M3 MacBook Pro, Sequoia 15.6, Slicer v5.8.1.</p>

---

## Post #2 by @cpinter (2025-08-13 13:44 UTC)

<p>Do you also see flickering when you load a sample dataset that has terminology information?</p>
<p>What is the resolution of the labelmap you use?</p>
<p>I’ve been thinking what to answer for days but this is so little information that it is basically impossible. Please provide a lot more information, given the special nature of your question. We need to know about your dataset, your use case, your algorithm, etc. Thanks.</p>

---

## Post #3 by @baderstine (2025-08-13 17:28 UTC)

<p>Apologies for the lack of detail.  I experimented with this quite a bit more and found that I was getting the flickering seemingly randomly with either function.  The flickering is intermittent and rather unpredictable.  Restarting Slicer seems to fix it.  I wish I knew more about what caused it but at this point, it does not seem to be related to this particular function.</p>

---

## Post #4 by @baderstine (2025-08-13 17:29 UTC)

<p>I am using 1.5x1.5x1.5mm images, segmentations, and label maps</p>

---

## Post #5 by @cpinter (2025-08-14 13:55 UTC)

<p>Could you please share a video? I thought it was due to slowness (like time of computation of getting terminology of segment in voxel under mouse) but now it does not seem so.</p>
<aside class="quote no-group" data-username="baderstine" data-post="4" data-topic="44030">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/baderstine/48/79333_2.png" class="avatar"> baderstine:</div>
<blockquote>
<p>I am using 1.5x1.5x1.5mm images, segmentations, and label maps</p>
</blockquote>
</aside>
<p>Yes but are they large volumes? I was asking because I thought it was a performance issue. I guess they are smaller then a normal CT (which are 512x512x150ish)</p>
<p>Has anyone else using Mac has seen flickering?</p>

---

## Post #6 by @baderstine (2025-12-15 21:21 UTC)

<p>I have not noticed the flickering since switching to 5.10.0</p>
<p>I have noticed a different issue with very large volumes (high slice count) in which certain Segment Editor operations will take a very long time (several seconds rather than nearly immediate).  Limiting the number of visible segments and applying to ‘only visible segments’ can speed these operations up so that one at least does seem to be a computation issue.</p>

---

## Post #7 by @cpinter (2025-12-16 09:40 UTC)

<p>Thanks for reporting back! I’ll mark your answer as solution because the particular issue for which you opened the topic has solved itself.</p>
<aside class="quote no-group" data-username="baderstine" data-post="6" data-topic="44030">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/baderstine/48/79333_2.png" class="avatar"> baderstine:</div>
<blockquote>
<p>certain Segment Editor operations will take a very long time (several seconds rather than nearly immediate)</p>
</blockquote>
</aside>
<p>This is a separate problem but seems important. Can you please start a new post (or issue on GitHub, whichever seems easier for you) with this? Ideally, if you want the community (who work on the Slicer core in their free time) to help in an efficient manner, we’d need a simple way to reproduce it. For example if you could find a short sequence of steps with one of the sample data that brings this out, it would be super helpful. Thanks a lot!</p>

---
