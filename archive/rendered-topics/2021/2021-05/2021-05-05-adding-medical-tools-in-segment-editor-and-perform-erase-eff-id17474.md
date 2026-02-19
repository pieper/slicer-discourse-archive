---
topic_id: 17474
title: "Adding Medical Tools In Segment Editor And Perform Erase Eff"
date: 2021-05-05
url: https://discourse.slicer.org/t/17474
---

# Adding medical tools in segment editor and perform erase effect!

**Topic ID**: 17474
**Date**: 2021-05-05
**URL**: https://discourse.slicer.org/t/adding-medical-tools-in-segment-editor-and-perform-erase-effect/17474

---

## Post #1 by @Raj_Kumar_Ranabhat (2021-05-05 15:37 UTC)

<p>Hi Experts,</p>
<p>In our project, instead of  sphere brush (default), we would like to import our own medical tools (obj) file and make an erase effect on 3D model from that medical tool. What will be the fastest and convenient way to do so.</p>
<p>Please provide some guidance .</p>
<p>Thank you.</p>

---

## Post #2 by @Raj_Kumar_Ranabhat (2021-05-10 13:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, By the way, we already have Virtual Reality version for this simulator, we would like to implement it also in the PC version. My current plan is to load the obj file (medical tool) and transform it to the sphere tool of the segment editor.</p>
<p>Secondly,<br>
Is the link primary source code which is controlling paint and erase effect of 3D Slicer ?</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/0daa3b92680706c1e98b6585a676545f41c0b8a2/Modules/Scripted/EditorLib/PaintEffect.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0daa3b92680706c1e98b6585a676545f41c0b8a2/Modules/Scripted/EditorLib/PaintEffect.py" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0daa3b92680706c1e98b6585a676545f41c0b8a2/Modules/Scripted/EditorLib/PaintEffect.py</a></h4>
<pre><code class="lang-py">from __future__ import print_function
import os
import vtk
import ctk
import qt
import slicer
from . import HelpButton
from . import EditUtil
from . import LabelEffectOptions, LabelEffectTool, LabelEffectLogic, LabelEffect
import numpy
from math import sqrt
from functools import reduce

__all__ = [
  'PaintEffectOptions',
  'PaintEffectTool',
  'PaintEffectLogic',
  'PaintEffect'
  ]

</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/0daa3b92680706c1e98b6585a676545f41c0b8a2/Modules/Scripted/EditorLib/PaintEffect.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Please feel free to write.</p>
<p>Thank you,</p>
<p>Sincerely<br>
Raj</p>

---

## Post #3 by @lassoan (2021-05-11 05:25 UTC)

<p>Segment Editor is not ideal for real-time simulation of drilling. For real-time volume removal, you are probably better off using volume rendering for 3D display and blanking out parts of the volume by combining your tool volume (rasterized volume of the tool model) with the displayed volume. This should be all doable in Python and since you can do everything with numpy array operations, it should be very fast.</p>

---

## Post #4 by @Raj_Kumar_Ranabhat (2021-05-11 15:00 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , thank you for reply. Actually our spine models are built/resected with uploading patient specific MR/CT scans and using Segment Editor module.</p>
<p>Yes for our Virtual Reality system there is huge latency during the resection and we tried to use volume rendering technique instead of using closed surface representation. The study is still going on.</p>
<p>In addition with VR simulation, we do have regular PC version simulation, right now we are just using 3D sphere or scissor effect for resection. Though it doesn’t look real time but is acceptable for training purpose.</p>
<p><strong>Our plan is instead of using  3d sphere or brush for erase effect, we planned to import medical tools like burr/ Kerrison as obj file and make a erase effect.</strong></p>
<p>(<a href="https://github.com/Slicer/Slicer/blob/0daa3b92680706c1e98b6585a676545f41c0b8a2/Modules/Scripted/EditorLib/PaintEffect.py" class="inline-onebox" rel="noopener nofollow ugc">Slicer/PaintEffect.py at 0daa3b92680706c1e98b6585a676545f41c0b8a2 · Slicer/Slicer · GitHub</a>)</p>
<p>I was trying modify and use the painteffect.py code from github but it seems there is no any effects of this code in the paint/erase in 3d slicer.</p>
<p>Please suggest for our approach.</p>
<p>Thank you !!!</p>

---

## Post #5 by @Raj_Kumar_Ranabhat (2021-05-19 14:30 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , <a class="mention" href="/u/pieper">@pieper</a> , <a class="mention" href="/u/muratmaga">@muratmaga</a> ,</p>
<p>Any suggestions, How can I use 3D obj file model as a brush in erase effect instead of 3D sphere.</p>
<p>Thank you !!</p>
<p>Sincerely,<br>
Raj</p>

---

## Post #6 by @lassoan (2021-05-19 14:35 UTC)

<p>You can apply a transform to your 3D model, import it into the segmentation, and erase from another segment using Logical operators effect. You can find examples for each of these steps in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>

---

## Post #7 by @Raj_Kumar_Ranabhat (2021-05-19 14:46 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you for the suggestions. Only one thing, I got stuck is how to get the node of the 3D sphere being used in paint/erase effect before apply transform to imported 3D model.</p>
<p>Thank you</p>

---

## Post #8 by @lassoan (2021-05-19 15:23 UTC)

<p>See this example for importing a loading a 3D model and importing it into segmentation: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files</a></p>

---

## Post #9 by @Raj_Kumar_Ranabhat (2021-05-19 16:47 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , Thank you for the scripts.</p>
<p>Last question, I am still struggling . In segment Editor 3D sphere brush is used for paint/erase effect. How can I access that  3D sphere Brush node so that I can transform my loaded obj to that model node.</p>
<p>Thank you</p>

---

## Post #10 by @lassoan (2021-05-19 16:57 UTC)

<p>You can use Logical operators effect to modify (paint or erase) another segment using your imported segment.</p>

---

## Post #11 by @Raj_Kumar_Ranabhat (2021-05-19 17:10 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>But there should be user-interactions with mouse to the imported model during erase as available in current paint effect .</p>

---

## Post #12 by @lassoan (2021-05-19 17:21 UTC)

<p>You can implement custom user interactions in your module (add observers to mouse events, etc. or create custom effect, using qSlicerSegmentEditorPaintEffect as base class and customizing the updateBrushModel method). I would not recommend doing this, though. Displaying the bone using volume rendering and blanking out regions that are being removed results in much higher quality rendering and a magnitude higher frame rate.</p>

---
