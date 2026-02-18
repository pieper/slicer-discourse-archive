# Improving Animator module

**Topic ID**: 32384
**Date**: 2023-10-23
**URL**: https://discourse.slicer.org/t/improving-animator-module/32384

---

## Post #1 by @muratmaga (2023-10-23 15:45 UTC)

<p>We would like to have a convenient interface to make movies of 3D visualizations from Slicer, particularly now what we are obtaining through the ColorizeVolume module. Animator module in <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Animator" rel="noopener nofollow ugc">SlicerMorph</a> provides that functionality to some extent.</p>
<p>The current problem with the Animator is that it is hard to learn and master, and has usability issues (e.g., forgetting to set the correct ROI or volume property out of multiple ones will result in no effect being produced).</p>
<p>An alternative is a visual interface in which the user takes a snapshot of the contents of 3D view, and this is interpreted as keyframe. Then the user modifies the visualization settings (e.g., change transparency, color, or ROI, and spins the object, etc) and takes another snapshot. The tool then interpolates the modified settings between these frames and provides as many frames as requested by the user.</p>
<p>Current SceneView module provides some of these functions already (e.g., restoring the scene to a saved state). However, it also has its own issues regarding making it a less attractive solution to build this feature on -at least its current state.</p>
<p>I suspect this is a feature that will be of interest to others, so I am soliciting for feedback and opinions on how we can improve the existing functionality.</p>

---

## Post #2 by @Dominick_Dickerson (2023-10-25 18:19 UTC)

<p>I have used Bruker’s CTVox for making videos before and find it to be very straightforward.</p>
<p>It functions similarly to how you describe the alternative version using keyframes and interpolation to create a video and it is very easy to use.</p>
<p>It’s very effective at making videos of models rotating and using the clipping box to cut through or grow a volume to reveal the internal anatomy.</p>

---
