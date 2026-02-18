# In Dynamic Modeler, is it possible to use a sphere ROI node to perform ROI cut?

**Topic ID**: 45768
**Date**: 2026-01-13
**URL**: https://discourse.slicer.org/t/in-dynamic-modeler-is-it-possible-to-use-a-sphere-roi-node-to-perform-roi-cut/45768

---

## Post #1 by @Vincent (2026-01-13 09:51 UTC)

<p>Hi,</p>
<p>I would like to use a sphere ROI node to perform ROI cut. However I cannot figure out how to create a sphere ROI.</p>
<p>In Dynamic Modeler, is it possible to use a sphere ROI node to perform ROI cut ?</p>
<p>Thanks in advance,</p>
<p>Best regards,</p>
<p>Vincent</p>

---

## Post #2 by @cpinter (2026-01-13 10:37 UTC)

<p>In Slicer the ROI markup node is a box, there is no sphere option. If your model is closed, then you can convert it to a segmentation and edit it as you wish.</p>

---

## Post #3 by @Vincent (2026-01-13 12:08 UTC)

<p>Thank you so much for your advise.</p>
<p>In <a href="https://discourse.slicer.org/t/in-3d-slicer-is-it-possible-to-simulate-femur-cut-in-real-time-without-imst">this thread</a> , Dynamic Modeler is suggested. I need to simulate bone drilling in real-time. Segment editing is not fast enough.</p>
<p>Is it possible to add sphere option to ROI markup node?</p>

---

## Post #4 by @cpinter (2026-01-13 12:14 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="45768">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>In Slicer the ROI markup node is a box, there is no sphere option.</p>
</blockquote>
</aside>
<p>This from above is still true. It is always possible to add more options, but it requires contributing C++ code.</p>

---

## Post #5 by @Esteban_Barreiro (2026-01-14 13:35 UTC)

<p>Hi!</p>
<p>For rendering in version 5.10.0 you can use the AnatomyCarve extension:<br>
<a href="https://github.com/andrey-titov/SlicerAnatomyCarve" rel="noopener nofollow ugc">https://github.com/andrey-titov/SlicerAnatomyCarve</a></p>

---

## Post #6 by @Vincent (2026-01-15 01:41 UTC)

<p>Hi <a class="mention" href="/u/esteban_barreiro">@Esteban_Barreiro</a> thank you so much for your advise. I cannot figure out how to use AnatomyCarve extension to simulate bone drilling in real-time. Would you mind giving me simple code to demonstrate how to use AnatomyCarve extension to simulate bone drilling in real-time?</p>

---

## Post #7 by @cpinter (2026-01-15 12:55 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="45768">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If your model is closed, then you can convert it to a segmentation and edit it as you wish.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/vincent">@Vincent</a> I have the sensation that you did’t see this. Have you explored this option?</p>

---

## Post #8 by @Vincent (2026-01-16 02:04 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> , yes I have explored this option. That is why I said segment editing is not fast enough to simulate bone cutting in real-time. In <a href="https://discourse.slicer.org/t/in-3d-slicer-is-it-possible-to-simulate-femur-cut-in-real-time-without-imstk/45543">this thread</a>, <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a> recommended the Dynamic Modeler.</p>

---

## Post #9 by @lassoan (2026-01-20 16:38 UTC)

<p>You can try Combine Models module in Sandbox extension. It can combine meshes using Boolean operations. If the mesh resolution is not too high and you cut the edited mesh to the minimum size then it may be fast enough.</p>
<p>You can also go meshless and use direct volume rendering. You can start from the original CT and set values of voxels that you remove to -1000. Then the only thing that takes time is to update the CT voxels, which can be very quick (as you just need a single <code>np.minimum</code> operation to combine the CT array with the small 3D array of the drill).</p>

---

## Post #10 by @Vincent (2026-01-21 10:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  thank you so much.</p>
<p>I tried Combine Models module. It may produce wrong empty mesh when performing Difference operation multiple times.</p>
<p>For example, two sphere Difference</p>
<pre><code class="lang-auto">sphere = vtk.vtkSphereSource()
sphere.SetRadius(10)
modelNode = slicer.modules.models.logic().AddModel(sphere.GetOutputPort())

sphere2 = vtk.vtkSphereSource()
sphere2.SetRadius(10)
sphere2.SetCenter(3.0, 0, 0)
modelNode2 = slicer.modules.models.logic().AddModel(sphere2.GetOutputPort()) 
</code></pre>
<p>How to prevent Combine Models module from producing wrong empty mesh ?</p>

---
