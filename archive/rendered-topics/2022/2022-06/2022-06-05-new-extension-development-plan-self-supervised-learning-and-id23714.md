# New Extension Development Plan: self-supervised learning and liver segmentation

**Topic ID**: 23714
**Date**: 2022-06-05
**URL**: https://discourse.slicer.org/t/new-extension-development-plan-self-supervised-learning-and-liver-segmentation/23714

---

## Post #1 by @LingFeng (2022-06-05 14:42 UTC)

<p>Hi everyone! I’m interested in developing a liver segmentation extension enabled by self-supervised learning (Vision Transformer as the backbone structure) for 3D slicer. I’m still fine-tuning the model and it is now able to achieve a dice score as high as 0.95 on the validation dataset. Does my plan sounds reasonable to you? I would appreciate any suggestions from the community <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2022-06-05 15:47 UTC)

<p>That sounds very useful, yes. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>I’m curious if it could work together with what <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> and team <a href="https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/SlicerLiver/">have been putting together</a>.</p>

---

## Post #3 by @RafaelPalomar (2022-06-14 05:02 UTC)

<p>That sounds fantastic! <a class="mention" href="/u/lingfeng">@LingFeng</a> I have a team working on liver resection and ablation applications. We are currently working on our first release for a liver resection planning extension. We are also looking into segmentation.</p>
<p>I would suggest that you join <a href="https://projectweek.na-mic.org/" rel="noopener nofollow ugc">project week</a>. You are welcome to join the <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerLiver/" rel="noopener nofollow ugc">Slicer-Liver project</a> for further discussion.</p>
<p>Rafael.</p>

---

## Post #4 by @jcfr (2022-06-14 06:21 UTC)

<p>It may be worth reaching out to <a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a> who worked on <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation">SlicerRVXLiverSegmentation</a> extension and see how your work could complement and/or leverage that extension.</p>

---

## Post #5 by @RafaelPalomar (2022-06-14 06:48 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> for the suggestion!</p>
<p><a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a>, would you or someone in your team like to join the  <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerLiver/" rel="noopener nofollow ugc">Slicer-Liver</a> project during Project Week?</p>
<p>Rafael.</p>

---

## Post #6 by @Thibault_Pelletier (2022-06-15 07:14 UTC)

<p>Hi <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>,</p>
<p>Unfortunately I will not be available to participate during the project week.<br>
I can most certainly make some time to discuss what we did in our extension and how we could work together moving forward.</p>
<p>I will also forward the invitation to the other members of the RVesselX project. Hopefully some will be available to participate for the NA-MIC week <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @Thibault_Pelletier (2022-06-15 07:21 UTC)

<p><a class="mention" href="/u/lingfeng">@LingFeng</a> and <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> regarding the liver segmentation using machine learning, we have added an extra segment editor effect which does just that to our extension.</p>
<p>The code for the extension is accessible here  :</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/c3fceba66af0f2f9739d5e1d31ab1652f257fe93cec7aee57685c9ff8ba5df2a/R-Vessel-X/SlicerRVXLiverSegmentation" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub - R-Vessel-X/SlicerRVXLiverSegmentation: 3D Slicer plugin for Liver...</a></h3>

  <p>3D Slicer plugin for Liver Anatomy Annotation by R-Vessel-X - GitHub - R-Vessel-X/SlicerRVXLiverSegmentation: 3D Slicer plugin for Liver Anatomy Annotation by R-Vessel-X</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The specifics of the ML model and the associated Slicer integration is available here :</p><aside class="onebox githubblob" data-onebox-src="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/blob/main/RVXLiverSegmentationEffect/RVXLiverSegmentationEffectLib/SegmentEditorEffect.py">
  <header class="source">

      <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/blob/main/RVXLiverSegmentationEffect/RVXLiverSegmentationEffectLib/SegmentEditorEffect.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/blob/main/RVXLiverSegmentationEffect/RVXLiverSegmentationEffectLib/SegmentEditorEffect.py" target="_blank" rel="noopener nofollow ugc">R-Vessel-X/SlicerRVXLiverSegmentation/blob/main/RVXLiverSegmentationEffect/RVXLiverSegmentationEffectLib/SegmentEditorEffect.py</a></h4>


      <pre><code class="lang-py">import gc
import os.path

from SegmentEditorEffects import *
import monai
from monai.inferers.utils import sliding_window_inference
from monai.networks.layers import Norm
from monai.networks.nets.unet import UNet
from monai.transforms import (AddChanneld, Compose, Orientationd, ScaleIntensityRanged, Spacingd, ToTensord)
from monai.transforms.compose import MapTransform
from monai.transforms.post.array import AsDiscrete, KeepLargestConnectedComponent
import numpy as np
import qt
import slicer
from slicer.ScriptedLoadableModule import *
import slicer.modules
from slicer.util import VTKObservationMixin
import torch
import vtk

</code></pre>



  This file has been truncated. <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/blob/main/RVXLiverSegmentationEffect/RVXLiverSegmentationEffectLib/SegmentEditorEffect.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>On our end, we used a UNET model implemented using MONAI and trained on the Medical Decathlon and IRCAD dataset for CT volumes reaching DICE scores of about .95 as well.</p>
<p>Hope this helps.</p>

---
