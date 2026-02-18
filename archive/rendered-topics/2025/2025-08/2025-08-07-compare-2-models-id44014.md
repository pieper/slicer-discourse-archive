# Compare 2 models

**Topic ID**: 44014
**Date**: 2025-08-07
**URL**: https://discourse.slicer.org/t/compare-2-models/44014

---

## Post #1 by @michaelli (2025-08-07 21:02 UTC)

<p>I want to  compare two models in two 3D views, so that I can rotate the camera independently for each 3D view. But all the models show in all views, how can I load the first model into the first 3d view window and the second model into the second 3d view?</p>

---

## Post #2 by @muratmaga (2025-08-07 21:21 UTC)

<ol>
<li>Switch to Dual 3D layout.</li>
<li>Turn off visibility of all models in Data module</li>
<li>Drag one 3D model object from the Data module and drop into 3D viewer <span class="hashtag-raw">#1</span></li>
<li>Then the repeat the same for the second 3D model and drop onto viewer <span class="hashtag-raw">#2</span></li>
</ol>

---

## Post #3 by @pieper (2025-08-07 21:27 UTC)

<p>You can also turn on linking in the 3D view if you want.</p>

---

## Post #4 by @michaelli (2025-08-08 02:05 UTC)

<p>Thank you, <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/pieper">@pieper</a> . Dual 3D layout and dragging works. I also want to rotate the two models and save them to mp4. I first linked the two views, then use “Screen Capture” module and “3D rotation”, but only the model in the first view is rotating. Is there a way to let the two models rotate simultaneously?</p>

---

## Post #5 by @muratmaga (2025-08-08 02:14 UTC)

<p>You can sync the cameras as <a class="mention" href="/u/pieper">@pieper</a> mentioned above. However, if their orientation is not similar, that might be challenging. You might have to create a centering transform.</p>
<p>M</p>

---
