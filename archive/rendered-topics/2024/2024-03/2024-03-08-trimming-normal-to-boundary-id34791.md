# Trimming normal to boundary

**Topic ID**: 34791
**Date**: 2024-03-08
**URL**: https://discourse.slicer.org/t/trimming-normal-to-boundary/34791

---

## Post #1 by @Beth_Thompson (2024-03-08 20:11 UTC)

<p>Hi,</p>
<p>I have a 3D model of a pulmonary artery generated in SimVascular. I am trying to add extensions to it, but first I need to clip the ends to open it. I would like to trim the ends just the tiniest bit to open them, and it would be ideal if this were done perpendicular to the inlet/outlet face. I’ve done this manually but I find it rather tedious (can do this if necessary, but it seems like VMTK would have the functionality to clip a small distance perpendicular to normal).</p>
<p>I’ve tried using the tutorial here: <a href="http://www.vmtk.org/tutorials/SurfaceForMeshing.html" class="inline-onebox" rel="noopener nofollow ugc">Prepare a surface for mesh generation | vmtk - the Vascular Modelling Toolkit</a><br>
to automatically clip, but I cannot figure out its behavior as it seems to clip randomly. I’ve changed the numberofendpointspheres from 1 to 3, but vmtk freezes when I try to do 4 or more endpoint spheres.</p>
<p>I’ve also tried using “vmtksurfaceendclipper,” but it freezes too.</p>
<p>Another method I tried was to delete the caps in SimVascular, and then add flow extensions to that model in VMTK. However, the resulting vtp ended up with non-triangular elements, somehow? Which made simvascular crash.</p>
<p>Does anyone have advice for how to make this work? Experience with adding flow extensions and re-importing into Simvascular?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2024-03-08 20:16 UTC)

<p>Maybe <a class="mention" href="/u/chir.set">@chir.set</a> can help. He has exposed several VMTK features in 3D Slicer’s VMTK extension - even a <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/BranchClipper.md">vessel clipping module</a> recently (although you need end clipping not branch clipping).</p>
<p>Alternatively, you can also try Dynamic Modeler module in 3D Slicer. It has a number of clipping tools that may be usable. If the mesh integrity is good then automatically aligning the clipping plane could be automated easily.</p>

---

## Post #3 by @chir.set (2024-03-08 20:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="34791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe <a class="mention" href="/u/chir.set">@chir.set</a> can help.</p>
</blockquote>
</aside>
<p>Please check <a href="https://discourse.slicer.org/t/vmtk-surface-clipping-contribution/30456/7">this thread</a> throughout.</p>
<p><a class="mention" href="/u/davidm">@DavidM</a> wrote a <a href="https://github.com/dmolony3/ClipVessel" rel="noopener nofollow ugc">module</a> that does just that.</p>
<p>Alternatively, other manual methods are suggested in the <a href="https://discourse.slicer.org/t/vmtk-surface-clipping-contribution/30456">thread</a> pointed to.</p>

---
