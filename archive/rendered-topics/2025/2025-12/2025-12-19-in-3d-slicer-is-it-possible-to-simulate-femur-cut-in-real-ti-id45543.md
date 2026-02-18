# In 3D Slicer, is it possible to simulate femur cut in real-time without iMSTK?

**Topic ID**: 45543
**Date**: 2025-12-19
**URL**: https://discourse.slicer.org/t/in-3d-slicer-is-it-possible-to-simulate-femur-cut-in-real-time-without-imstk/45543

---

## Post #1 by @Vincent (2025-12-19 08:09 UTC)

<p>Hi,</p>
<p>Support and development of <a href="https://gitlab.kitware.com/iMSTK/iMSTK" rel="noopener nofollow ugc">iMSTK</a> has been discontinued since May-02-2025.</p>
<p>I would like to simulate <a href="https://imstk.gitlab.io/Examples/FemurCut.html" rel="noopener nofollow ugc">femur cut</a> in real-time with 3D Slicer. I have tried Mask volume effect, but it is not fast enough (the FPS is very low).</p>
<p>In 3D Slicer, is it possible to simulate femur cut in real-time without iMSTK?</p>
<p>Thanks in advance,</p>
<p>Best regards,</p>
<p>Vincent</p>

---

## Post #2 by @Vincent (2025-12-29 01:43 UTC)

<p>Hi,</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>  , <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>  would you mind giving me some advice ?</p>
<p>Thanks in advance,</p>
<p>Best regards,</p>
<p>Vincent</p>

---

## Post #3 by @pieper (2025-12-29 14:11 UTC)

<p>Maybe you want <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dynamicmodeler.html">the Dynamic Modeler</a> or maybe you can get by with <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/models.html#:~:text=inside%20the%20model.-,Clipping,-%3A%20Enable%20clipped%20display">just Clipping</a>.</p>

---

## Post #4 by @lassoan (2025-12-31 02:11 UTC)

<p>Yes, you can use Dynamic Modeler module’s ROI cut tool to simulate bone cut in real-time.</p>
<p>Just a simple demo (with a little Python scripting you can make the cut incremental, apply constraints, etc.):</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26a9ff53479e6a9fba14388cb1eab395f702bd2a.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92bd6424590b7433795250fe408a1150e56f7b60.jpeg" data-video-base62-sha1="5w2mpNFkrvAkiyIVc78Jg4Sb60a.mp4">
  </div><p></p>

---

## Post #5 by @Vincent (2025-12-31 04:35 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  <a class="mention" href="/u/lassoan">@lassoan</a> Thank you so much for your help.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> would you mind sharing your code with me?</p>
<p>I have tried the Dynamic Modeler widget. When I click Continuous update of Apply button for ROI cut, the FPS of 3D Slicer becomes very low instantly.</p>

---

## Post #6 by @lassoan (2025-12-31 13:17 UTC)

<p>I didn’t do any scripting, so there is nothing to share. M</p>
<p>About performance: Image segmentation provides an extremely dense mesh. You can usually remove 95 to 99.9% of the points without any visible difference (using Surface Toolbox’s uniform remeshing or decimation tools). You can also some off parts into separate models that you are sure the user will not cut into (e.g., the femur head and the lower half of the femur). This way the model your will have to interactively cut will have 100-1000x less points, so the updates will be extremely fast. In general, when you are doing real-time simulation, the default high- accuracy computations would take to much time, so you often need to do similar tricks and various fast approximations.</p>

---

## Post #7 by @Vincent (2026-01-02 05:20 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you so much. I will try the ticks you suggests later.</p>
<p>I have one more question. How to set the same model as both of input model node and Clipped output model node (outside) for running Continuous update of ROI cut.?</p>
<p>Dynamic Modeler widget does not allow me to set the same model as both of input model node and Clipped output model node (outside) for running Continuous update of ROI cut.</p>
<p>If I clone my bone model and set the cloned bone model as Clipped output model node (outside) and then set my bone model invisible, the consequence is that the removed part of bone recovers when ROI node move away from the bone model. Therefore I think I need to set the same model as both of input model node and Clipped output model node (outside) for running Continuous update of ROI cut.</p>

---
