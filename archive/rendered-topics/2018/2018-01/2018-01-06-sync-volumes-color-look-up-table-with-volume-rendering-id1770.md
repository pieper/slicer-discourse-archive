# Sync “Volumes” color look-up table with “Volume Rendering”

**Topic ID**: 1770
**Date**: 2018-01-06
**URL**: https://discourse.slicer.org/t/sync-volumes-color-look-up-table-with-volume-rendering/1770

---

## Post #1 by @Hamburgerfinger (2018-01-06 02:10 UTC)

<p>In the Volume Rendering module there is an option to sync the scalar color mapping with the active color mapping in the Volumes module. Can I do the opposite, i.e. create a custom color mapping in the Volume Rendering module and import it for use with Volumes module?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-01-06 14:45 UTC)

<p>You can do it by copy-pasting this code to the Python console:</p>
<pre><code>volumeNode = getNode('CTChest')
volumeRenderingDisplayNode = slicer.modules.volumerendering.logic().GetFirstVolumeRenderingDisplayNode(volumeNode)
volumeRenderingPropertyNode = volumeRenderingDisplayNode.GetVolumePropertyNode()
colorTransferFunction = volumeRenderingPropertyNode.GetColor()
colorNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLProceduralColorNode')
colorNode.SetAndObserveColorTransferFunction(colorTransferFunction)
volumeNode.GetDisplayNode().SetAndObserveColorNodeID(colorNode.GetID())
</code></pre>
<p>The code snippet does not synchronize the lookup table range, so you have to adjust it by click-and-drag the mouse in the slice view up/down, left/right.</p>
<p>Also, color LUTs don’t contain opacity value. However, you can do a simple thresholding in Volumes module to remove background.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/339bc6f9e1d255bc00c54d1f8367219ab4e18c01.png" data-download-href="/uploads/short-url/7my6kU8g148yeiYV4OlE0OsJgUp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339bc6f9e1d255bc00c54d1f8367219ab4e18c01_2_690x441.png" alt="image" data-base62-sha1="7my6kU8g148yeiYV4OlE0OsJgUp" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339bc6f9e1d255bc00c54d1f8367219ab4e18c01_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339bc6f9e1d255bc00c54d1f8367219ab4e18c01_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339bc6f9e1d255bc00c54d1f8367219ab4e18c01_2_1380x882.png 2x" data-dominant-color="A58B9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3000×1920 1.15 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Hamburgerfinger (2018-01-06 20:38 UTC)

<p>This almoooost works perfectly… The issue is that if the dataset contains entirely, for example, scalars between 0 and 1, it assigns one color to everything, instead of continuous colors.</p>
<p>On the other hand, if I apply a calibration factor to scale the values to, for example, 0 to 1000, the slices look “correct”.</p>
<p>Any ideas why this is?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2018-01-08 04:06 UTC)

<p>The code snippet does not synchronize the lookup table range, so you have to adjust it by click-and-drag the mouse in the slice view up/down, left/right.</p>
<p>If the scalar range of the volume is very extreme (e.g., 0.0-1.0) then maybe you have to adjust a lot and it could be easier to adjust it using window/level sliders in Volumes module.</p>

---
