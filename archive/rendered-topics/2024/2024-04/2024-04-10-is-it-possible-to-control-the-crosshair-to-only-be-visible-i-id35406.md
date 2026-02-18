# Is it possible to control the crosshair to only be visible in certain views?

**Topic ID**: 35406
**Date**: 2024-04-10
**URL**: https://discourse.slicer.org/t/is-it-possible-to-control-the-crosshair-to-only-be-visible-in-certain-views/35406

---

## Post #1 by @matrosica0808 (2024-04-10 09:31 UTC)

<p>The extension is configured to enable tracking of data at various points in time.<br>
I want to use crosshair according to each point of view. Is there a way to create a crosshair instance as below? If you do this, they all have the same address value.</p>
<pre><code class="lang-auto">crosshairNode = slicer.util.getNode("Crosshair")
    crosshairNode.SetCrosshairColor(1.0,0.0,0.0)
    crosshairNode.SetCrosshairMode(slicer.vtkMRMLCrosshairNode.ShowSmallIntersection)
    crosshairNode.SetCrosshairToThick()

    crosshairNode2 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLCrosshairNode')
    crosshairNode2.SetCrosshairColor(0.0,1.0,0.0)
    crosshairNode2.SetCrosshairMode(slicer.vtkMRMLCrosshairNode.ShowSmallIntersection)
    crosshairNode2.SetCrosshairToThick()

    crosshairNode3 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLCrosshairNode')
    crosshairNode3.SetCrosshairColor(0.0,0.0,1.0)
    crosshairNode3.SetCrosshairMode(slicer.vtkMRMLCrosshairNode.ShowSmallIntersection)
    crosshairNode3.SetCrosshairToThick()

</code></pre>
<p>And I want to make them visible only to certain views.<br>
As shown in the picture below, when there are 9 views, I would like to display only 1 row each. What should I do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16feb50b4c744ff3b29f72204e1a7334a774cbad.jpeg" data-download-href="/uploads/short-url/3hqd8ZzoXPYVaGpUuAZ7CGUx5md.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16feb50b4c744ff3b29f72204e1a7334a774cbad_2_474x374.jpeg" alt="image" data-base62-sha1="3hqd8ZzoXPYVaGpUuAZ7CGUx5md" width="474" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16feb50b4c744ff3b29f72204e1a7334a774cbad_2_474x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16feb50b4c744ff3b29f72204e1a7334a774cbad_2_711x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16feb50b4c744ff3b29f72204e1a7334a774cbad_2_948x748.jpeg 2x" data-dominant-color="3D3B36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1227×970 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, when you hover the mouse over a specific view (Axial View at the top left in the picture above), is there a way to get the name and RAS coordinates of that view?</p>

---

## Post #2 by @koeglfryderyk (2024-04-23 09:48 UTC)

<p>to answer the RAS part of your second question:</p>
<p>you can get the RAS coordinates like so:</p>
<pre><code class="lang-auto">crosshairNode=slicer.util.getNode("Crosshair")
ras=[0,0,0]
crosshairNode.GetCursorPositionRAS(ras)
</code></pre>
<p>take a look at the script repository, I got this code from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-scalar-values-at-surface-of-a-model" rel="noopener nofollow ugc">here</a></p>
<p>(but I don’t know how to get the name of the view)</p>

---
