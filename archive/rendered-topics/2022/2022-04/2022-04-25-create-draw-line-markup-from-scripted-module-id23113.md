# Create/draw line markup from scripted module

**Topic ID**: 23113
**Date**: 2022-04-25
**URL**: https://discourse.slicer.org/t/create-draw-line-markup-from-scripted-module/23113

---

## Post #1 by @llafitte007 (2022-04-25 11:48 UTC)

<p>Hello Slicer Community,</p>
<p>I’m new to the Slicer world so I apologize in advance if I make any mistakes.</p>
<p>I am creating a small module that allows you to manage needles on images (import, visual control, modification, export). Basically, a needle is a line markup.</p>
<p>here a preview of the module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2fa1966e3e6388c0aff5e07c9d84f352ebe5292.jpeg" data-download-href="/uploads/short-url/wnVK5N9hqNT28wKuz0MchxIK1Wi.jpeg?dl=1" title="Capture d’écran de 2022-04-25 12-35-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2fa1966e3e6388c0aff5e07c9d84f352ebe5292_2_690x281.jpeg" alt="Capture d’écran de 2022-04-25 12-35-24" data-base62-sha1="wnVK5N9hqNT28wKuz0MchxIK1Wi" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2fa1966e3e6388c0aff5e07c9d84f352ebe5292_2_690x281.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2fa1966e3e6388c0aff5e07c9d84f352ebe5292_2_1035x421.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2fa1966e3e6388c0aff5e07c9d84f352ebe5292_2_1380x562.jpeg 2x" data-dominant-color="828188"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran de 2022-04-25 12-35-24</span><span class="informations">1843×753 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Currently, I can load a control file, create needles (line markup) in the scene, and re-export the data from the scene.</p>
<p>My biggest problem now is that I want to create a line markup from scratch (no coordinates). In fact I have to repeat/simulate the click on the “create line markup” button in the Markups module : this activates the “drawing mode” which allows to select the 2 control points of the line on the scenes.</p>
<p>I don’t see how to do it, nor if it is possible from a scripted module,</p>
<p>Could someone help me ?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-04-25 12:51 UTC)

<p>You can use the markup place widget for this. See this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-a-button-to-module-gui-to-activate-control-point-placement">script repository example</a>.</p>

---

## Post #3 by @llafitte007 (2022-04-26 08:41 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> it was exactly was I excepted !</p>
<p>For those interested the code used</p>
<pre><code class="lang-auto">selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsLineNode")
interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
interactionNode.SwitchToSinglePlaceMode()
</code></pre>

---
