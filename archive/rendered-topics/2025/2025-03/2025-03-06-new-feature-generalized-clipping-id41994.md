# New Feature: Generalized Clipping

**Topic ID**: 41994
**Date**: 2025-03-06
**URL**: https://discourse.slicer.org/t/new-feature-generalized-clipping/41994

---

## Post #1 by @Sunderlandkyl (2025-03-06 23:46 UTC)

<p>In the latest preview and stable release, it is now possible to apply clipping to the visualization of models, segmentations, and volume rendering using slice view planes or markup planes or ROI boxes.</p>
<p>Clipping options can be accessed in the Clipping section of the models, segmentations, or volume rendering sections of the markups modules:</p>
<p>Multiple clipping functions can be combined by specifying Markups Plane/ROI nodes, Slice nodes, or other clipping nodes as inputs. Each clipping function can be inverted or enabled/disabled individually.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6581bb68d4b3ea9fb6774776c870ad19397bc53.png" data-download-href="/uploads/short-url/z9gebuau4B23EyGOMz68GIOQYAH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6581bb68d4b3ea9fb6774776c870ad19397bc53.png" alt="image" data-base62-sha1="z9gebuau4B23EyGOMz68GIOQYAH" width="441" height="236"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">441×236 9.08 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Models and Segmentations</strong></p>
<p>The clipping widget also contains options for visualizing end caps when clipping model and segmentation nodes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88923ffe8459993682664edaad674fc388ffbf51.png" data-download-href="/uploads/short-url/juah3x0vguTVFCKK2DrJABUC8Nz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88923ffe8459993682664edaad674fc388ffbf51.png" alt="image" data-base62-sha1="juah3x0vguTVFCKK2DrJABUC8Nz" width="360" height="351"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">360×351 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This feature can be enabled/disabled using the “Cap visibility” option, as well as the opacity of the capped area. The outline around the clipped regions can also be visualized by enabling the “Outline visibility” option.</p>
<p>Volume Rendering</p>
<p>When applying clipping to volume rendering visualizations, it is also possible to specify a blur effect to the edges of the clipped region in order to reduce hash artifacts caused by binary masking of the volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a7888effa401e3445bdfce6f952a3d451f1364b.jpeg" data-download-href="/uploads/short-url/cUldsUkAKlS1G2XXTrarhcmGajV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a7888effa401e3445bdfce6f952a3d451f1364b.jpeg" alt="image" data-base62-sha1="cUldsUkAKlS1G2XXTrarhcmGajV" width="371" height="351"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">371×351 50.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>For Developers</strong></p>
<p>The new clipping visualization options can be controlled through the Slicer API:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = getNode("Model")
planeNode = getNode("P")

clipNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLClipNode") # Add clip node
clipNode.AddAndObserveClippingNodeID(planeNode.GetID()) # Assign clip function(s)
clipNode.SetClippingNodeState(planeNode, slicer.vtkMRMLClipNode.ClipNegativeSpace) # Set inside/outside

modelDisplayNode = modelNode.GetDisplayNode()
modelDisplayNode.SetAndObserveClipNodeID(clipNode.GetID()) # Attach clip node to a display node. Can be used in multiple display nodes.
modelDisplayNode.ClippingOn() # Enable clipping
modelDisplayNode.ClippingCapSurfaceOn() # Enable end-capping visualization
modelDisplayNode.ClippingOutlineOn() # Enable end-capping outline
</code></pre>
<p>The input to the clipping node can be any sort of vtkMRMLTransformableNode that implements the <a href="https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fapidocs.slicer.org%2Fmain%2FclassvtkMRMLTransformableNode.html%23ae3f7351d4604489c9d9923812d6fb86d&amp;data=05%7C02%7Ckyle.sunderland%40queensu.ca%7Ca9281e5b30994e137bc308dd5cf97d45%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638768948819673257%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=4SWT5lytFBlcGUnZZNbbSlBCT0QvcjCSzatSzOeGaQE%3D&amp;reserved=0" rel="noopener nofollow ugc">GetImplicitFunctionWorld()</a> function. Currently this includes vtkMRMLMarkupsPlaneNode, vtkMRMLMarkupsROINode, vtkMRMLSliceNode, vtkMRMLClipNode, and vtkMRMLModelNode (though performance is poor for model nodes).</p>
<p><strong>Acknowledgements</strong></p>
<p>Development was funded in part by a Children’s Hospital of Philadelphia (CHOP) Cardiac Center Innovation Grant, a CHOP Cardiac Center Research Grant, a CHOP Frontier Grant, NIH R01 HL153166 and T32GM008562.</p>

---
