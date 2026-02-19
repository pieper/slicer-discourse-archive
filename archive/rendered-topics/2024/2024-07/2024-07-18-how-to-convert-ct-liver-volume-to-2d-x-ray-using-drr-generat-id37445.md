---
topic_id: 37445
title: "How To Convert Ct Liver Volume To 2D X Ray Using Drr Generat"
date: 2024-07-18
url: https://discourse.slicer.org/t/37445
---

# How to convert CT liver volume to 2d X ray using Drr generation in 3d slicer

**Topic ID**: 37445
**Date**: 2024-07-18
**URL**: https://discourse.slicer.org/t/how-to-convert-ct-liver-volume-to-2d-x-ray-using-drr-generation-in-3d-slicer/37445

---

## Post #1 by @ebin1234 (2024-07-18 09:17 UTC)

<p>Hello, I have doubt about using drr generation in 3d slicer.I am attaching the result I got after using DRR generation. What are the parameters I have to set for proper display of the 2d Xray image in 2d views?.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d15bd839ecbdd98fc838c28cbd9a1aa3b7497feb.jpeg" data-download-href="/uploads/short-url/tS4zbDIr9oGDgUWi1ixe2R5ELtV.jpeg?dl=1" title="CT-LIVER" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d15bd839ecbdd98fc838c28cbd9a1aa3b7497feb_2_690x288.jpeg" alt="CT-LIVER" data-base62-sha1="tS4zbDIr9oGDgUWi1ixe2R5ELtV" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d15bd839ecbdd98fc838c28cbd9a1aa3b7497feb_2_690x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d15bd839ecbdd98fc838c28cbd9a1aa3b7497feb_2_1035x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d15bd839ecbdd98fc838c28cbd9a1aa3b7497feb_2_1380x576.jpeg 2x" data-dominant-color="656364"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CT-LIVER</span><span class="informations">1918×802 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Mik (2024-07-19 09:59 UTC)

<p>Have you tried to use <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Docs/user_guide/modules/drr.md" rel="noopener nofollow ugc"><code>DRR Image Computation</code></a> module which is a also a part of SlicerRT extension? It has an additional markups elements that visualize imager, normal and view-up vectors,  but you have to setup a dummy RTplan and RTBeam nodes in order to use that module properly.</p>
<p>Or you cat to use a python script below, where <code>isocenterPosition</code> variable is RAS coordinates of the beam isocenter.</p>
<pre data-code-wrap="python"><code class="lang-python"># Create dummy plan
rtImagePlan = slicer.mrmlScene.AddNewNodeByClass( 'vtkMRMLRTPlanNode', 'rtImagePlan')
# Create RTImage dummy beam
rtImageBeam = slicer.mrmlScene.AddNewNodeByClass( 'vtkMRMLRTBeamNode', 'rtImageBeam')
# Set required beam parameters 
rtImageBeam.SetGantryAngle(90.)
rtImageBeam.SetCouchAngle(12.)
# Add beam to the plan
rtImagePlan.AddBeam(rtImageBeam)
# Get CT volume
ctVolume = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
# Set and observe CT volume by the plan
rtImagePlan.SetAndObserveReferenceVolumeNode(ctVolume)

# Set required isocenter position as a point
rtImagePlan.SetIsocenterSpecification(slicer.vtkMRMLRTPlanNode.ArbitraryPoint)
isocenterPosition = [ -1., -2., -3. ]
if (rtImagePlan.SetIsocenterPosition(isocenterPosition)):
  print('New isocenter position is set')

# Create DRR image computation node for user imager parameters
rtImageParameters = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLDrrImageComputationNode', 'rtImageBeamParams')
# Set and observe RTImage beam by the DRR node
rtImageParameters.SetAndObserveBeamNode(rtImageBeam)
# Set required DRR parameters
rtImageParameters.SetHUThresholdBelow(50)
# Get DRR computation logic
drrLogic = slicer.modules.drrimagecomputation.logic()
# Update imager markups for the 3D view and slice views (optional)
drrLogic.UpdateMarkupsNodes(rtImageParameters)
# Update imager normal and view-up vectors (mandatory)
drrLogic.UpdateNormalAndVupVectors(rtImageParameters) # REQUIRED
# Compute DRR image
drrLogic.ComputePlastimatchDRR( rtImageParameters, ctVolume)
</code></pre>

---

## Post #3 by @Mik (2024-07-19 10:06 UTC)

<aside class="quote no-group" data-username="ebin1234" data-post="1" data-topic="37445">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebin1234/48/70096_2.png" class="avatar"> ebin1234:</div>
<blockquote>
<p>What are the parameters I have to set for proper display of the 2d Xray image in 2d views?.</p>
</blockquote>
</aside>
<p>After successful DRR image calculation you can click on the <code>Rotate to volume plane</code> button,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71348837ae2ee244d6b9fd387d96a4da7b46300c.png" alt="image" data-base62-sha1="g9sve5uHdTtmp7HkNYUEU56EZeQ" width="684" height="177"></p>
<p>and when <code>Reset field of view</code> button.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b1d55af5702a583d3f913b16fc11e37788864b2.png" data-download-href="/uploads/short-url/d02ixR5N4RXP7yGTQ0df2WPkmkO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b1d55af5702a583d3f913b16fc11e37788864b2_2_690x181.png" alt="image" data-base62-sha1="d02ixR5N4RXP7yGTQ0df2WPkmkO" width="690" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b1d55af5702a583d3f913b16fc11e37788864b2_2_690x181.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b1d55af5702a583d3f913b16fc11e37788864b2_2_1035x271.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b1d55af5702a583d3f913b16fc11e37788864b2.png 2x" data-dominant-color="636277"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1369×361 61.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
