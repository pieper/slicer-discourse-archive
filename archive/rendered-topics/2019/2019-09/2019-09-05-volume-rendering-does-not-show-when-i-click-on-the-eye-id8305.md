# Volume rendering does not show when I click on the eye

**Topic ID**: 8305
**Date**: 2019-09-05
**URL**: https://discourse.slicer.org/t/volume-rendering-does-not-show-when-i-click-on-the-eye/8305

---

## Post #1 by @Nerea_Lund (2019-09-05 02:52 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 3D slicer 4.10.2<br>
Expected behavior: After loading dicom files, I cannot have a visualization with the rendering volume<br>
Actual behavior:</p>
<p>Once the images are loaded, When I click on the eye-icon in the Volume Rendering module, all I see is “nothing” . There is no rendering of the data.</p>
<p>I have the multiple volume rendering, so i must to toggle between two volumes using the Volume Rendering module (I need to select one, turn it off, then select the other and turn it on). I was thinking that perhaps with multiple volumes, it’s easy for the software get confused about which volume’s rendering properties are selected for editing so you can mess up your settings by accident.<br>
But then I can use the segment editor module and edit over the image. And in the end I can’t generate the 3d model because nothing appears in the visualization.</p>
<p>Someone who can give me an idea?<br>
Thank u</p>

---

## Post #2 by @muratmaga (2019-09-05 04:32 UTC)

<p>There might be couple things going on. We need more information to help you.<br>
How big are your volumes? Are you using GPU or CPU raycasting? Do volume rendering work with the provided sample data (e.g., MRHead.nrrd).</p>
<p>probably best to start working with single volume until you better understand the settings involved.</p>

---

## Post #3 by @lassoan (2019-09-05 13:18 UTC)

<p>You can try clicking on the small rectangle icon in the title bar of the 3D view “Center the 3D view…” to make sure the volume is in the field of view. If it does not help then please answer the questions above by <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>

---

## Post #4 by @Nerea_Lund (2019-09-05 20:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a>   Thank you for comment .</p>
<p>Yesterday, I had a solution. .Yes, I made sure specifying the GPU rendering option.<br>
The problem was that my data is heavy so it doesn´t match the scaling volume specified by the slicer, I had to put the “advanced option” in dicom to adjust. Now everything is fine…</p>
<p>Regards</p>

---
