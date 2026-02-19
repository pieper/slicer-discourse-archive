---
topic_id: 42741
title: "Dynamic Modeler Curve Cut Creates Output Model Node But Its"
date: 2025-04-29
url: https://discourse.slicer.org/t/42741
---

# Dynamic Modeler "Curve cut" creates output model node, but it's empty (no surface)

**Topic ID**: 42741
**Date**: 2025-04-29
**URL**: https://discourse.slicer.org/t/dynamic-modeler-curve-cut-creates-output-model-node-but-its-empty-no-surface/42741

---

## Post #1 by @JohnWick (2025-04-29 23:17 UTC)

<p>Hi everyone,</p>
<p>I’m trying to use the Dynamic Modeler module via Python scripting in 3D Slicer to cut a model using a curve. My goal is to keep only the inside portion of the model, and I’m not using the Straight Cut option. The script successfully creates a <code>vtkMRMLDynamicModelerNode</code> and the output model node (<code>CurveCutOutput</code>), but the output model does not contain any geometry – it’s an empty surface model.</p>
<p>Here is the core of my script:</p>
<pre><code class="lang-auto">modelNode = getNode("Model")
curveNode = getNode("Curve")
insidePointNode = getNode("F") 

curveCutModeler = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDynamicModelerNode")
curveCutModeler.SetToolName("Curve cut")
curveCutModeler.SetNodeReferenceID("CurveCut.InputModel", modelNode.GetID())
curveCutModeler.SetNodeReferenceID("CurveCut.CuttingCurve", curveNode.GetID())

cutModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "CurveCutOutput")
curveCutModeler.SetNodeReferenceID("CurveCut.OutputModel", cutModelNode.GetID())

curveCutModeler.SetAttribute("CurveCut.UseStraightCut", "false")
curveCutModeler.SetAttribute("CurveCut.KeepCellsInside", "true")
curveCutModeler.SetAttribute("CurveCut.KeepCellsOutside", "false")
curveCutModeler.SetContinuousUpdate(True)

if not cutModelNode.GetDisplayNode():
    displayNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")
    cutModelNode.SetAndObserveDisplayNodeID(displayNode.GetID())

cutModelNode.GetDisplayNode().SetOpacity(0.5)
</code></pre>
<p>I also tried this manually but the output is still empty:<br>
slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(curveCutModeler)</p>
<p>What am I missing to get the surface generated in <code>CurveCutOutput</code>?<br>
Is there a required event or trigger I’m not calling in the script? Or is there a known limitation or requirement of the Curve Cut tool when used programmatically?</p>
<p>Any advice or example of working code that produces a non-empty output model would be greatly appreciated!</p>
<p>Thanks in advance!</p>

---

## Post #2 by @cpinter (2025-04-30 09:57 UTC)

<p>Is there any error in the console?</p>
<p>Curve cut does not always, work, it fails with some inputs. I don’t remember the exact error message but there was one about not finding a path or similar. You need to make yourself familiar with the tool and you’ll have an idea what is supposed to work and what is not.</p>
<p>Find some inputs on which it works when running from the GUI. Then you can verify your code and make sure it does the same thing.</p>

---

## Post #3 by @JohnWick (2025-04-30 23:00 UTC)

<p>Thank you for your response!</p>
<p>There is no error in the console, and the output model node <strong>is generated</strong>, but it’s marked with the comment: <strong>“Model !Invalid Model”</strong>. Please see the enclosed screenshot for reference.</p>
<p>Interestingly, when I use the <strong>Curve Cut</strong> tool manually through the GUI on the same model, curve, and point node, it works perfectly and produces the expected result. So the data itself seems fine, and the problem only arises during scripted execution.</p>
<p>I’ve tried multiple variations in the script (including toggling <code>SetContinuousUpdate(False)</code>, changing the order of assignments, and manually calling <code>slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(curveCutModeler)</code>), but none led to a valid surface in <code>CurveCutOutput</code>.</p>
<p>As an alternative, I found a working approach using <strong>Kyle Sunderland’s clipping script</strong>:<br>
<img src="https://emoji.discourse-cdn.com/twitter/link.png?v=14" title=":link:" class="emoji" alt=":link:" loading="lazy" width="20" height="20"> <a href="https://gist.github.com/Sunderlandkyl/b1e9c4def887a480eb6de8d45187f958" rel="noopener nofollow ugc">https://gist.github.com/Sunderlandkyl/b1e9c4def887a480eb6de8d45187f958</a><br>
This script reliably clips the model using a plane and a closed curve, and fits my use case well.</p>
<p>I initially hoped to use the Dynamic Modeler tool for this task due to its integration and GUI correspondence, but unfortunately, the scripted version does not yield usable output in this scenario.</p>
<p>If anyone has insights into why the scripted Curve Cut doesn’t work despite the GUI version succeeding, I’d greatly appreciate further tips.</p>
<p>Thanks again!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a79d97d2b060750062a4add9ad532011a4ab79b0.jpeg" data-download-href="/uploads/short-url/nUNnvoH4pBOp0DCT0lQyefzBqQ8.jpeg?dl=1" title="screenShot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a79d97d2b060750062a4add9ad532011a4ab79b0.jpeg" alt="screenShot" data-base62-sha1="nUNnvoH4pBOp0DCT0lQyefzBqQ8" width="499" height="278"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenShot</span><span class="informations">499×278 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mikebind (2025-05-01 17:22 UTC)

<p>Just a tip, I have found that sometimes when I see the “Model !Invalid model” message, actually most of the processing worked and there is data in the model node, but it failed some final validation check.  It’s worth looking in the Models module to see if there are greater than zero Points and Cells listed in the model Information section.  Sometimes you can even visualize the mesh.  None of that turns it into a valid model node, but it can be helpful during debugging.<br>
The most common issue I have run into is non-manifold edges.  Sometimes some additional cleaning steps can resolve those.  Is there a chance that curveCutModeler automatically applies some of that when called through the GUI but not through the methods you are calling?</p>

---
