# Configure segmentation defaults

**Topic ID**: 14207
**Date**: 2020-10-22
**URL**: https://discourse.slicer.org/t/configure-segmentation-defaults/14207

---

## Post #1 by @CaptainR (2020-10-22 09:13 UTC)

<p>I successfully changed the 3D view background color and the left-click and drag to window/level when starting slicer.</p>
<p>Unfortunately, I can’t see what goes wrong with the following (copied and paste directly from notepad):</p>
<pre><code class="lang-python"># Change default overwrite setting in segment editor
defaultSegmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
defaultSegmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
slicer.mrmlScene.AddDefaultNode(defaultSegmentEditorNode)

# Save LabelMaps as Nifti (.nii.gz)
requiredFileExtension = '.nii.gz'
originalFileExtension = '.nrrd'
volumeNodes = slicer.util.getNodesByClass('vtkMRMLLabelMapVolumeNode')
for volumeNode in volumeNodes:
  volumeStorageNode = volumeNode.GetStorageNode()
  if not volumeStorageNode:
    volumeNode.AddDefaultStorageNode()
    volumeStorageNode = volumeNode.GetStorageNode()
    volumeStorageNode.SetFileName(volumeNode.GetName()+requiredFileExtension)
  else:
    volumeStorageNode.SetFileName(volumeStorageNode.GetFileName().replace(originalFileExtension, requiredFileExtension))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48aa1035bd9608b329417e68e20ff9a78bd78bd5.png" data-download-href="/uploads/short-url/amOJGtbXoU0lXado0ufs8Ak6X1r.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48aa1035bd9608b329417e68e20ff9a78bd78bd5_2_690x388.png" alt="image" data-base62-sha1="amOJGtbXoU0lXado0ufs8Ak6X1r" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48aa1035bd9608b329417e68e20ff9a78bd78bd5_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48aa1035bd9608b329417e68e20ff9a78bd78bd5_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48aa1035bd9608b329417e68e20ff9a78bd78bd5_2_1380x776.png 2x" data-dominant-color="F3F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2160 703 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-10-23 01:53 UTC)

<p>Segment editor overlapping segments by default: Your code was correct. Segment Editor did not take into account default vtkMRMLSegmentEditorNode. I’ve fixed this now (see <a href="https://github.com/Slicer/Slicer/commit/49bcde1522c065a07c90da65d5b2737d88fc12b5">here</a>).</p>
<p>Setting default volume node save format to nifti: Your code only changed file format of existing nodes but did not change the default save format. To change the default, you need to run this code:</p>
<pre><code class="lang-python">defaultVolumeStorageNode = slicer.vtkMRMLVolumeArchetypeStorageNode()
defaultVolumeStorageNode.SetDefaultWriteFileExtension("nii.gz")
slicer.mrmlScene.AddDefaultNode(defaultVolumeStorageNode)
</code></pre>
<p>Since you want segments to overlap by default, most likely you are not in the neuroimaging field. Therefore, I would not recommend to use nifti, as it is not a general-purpose 3D file format, but it is specifically for neuroimaging and it has several limitations when it is used for other kind of 3D images. Unless you work with brain images, I would recommend nrrd file format for 3D image storage.</p>

---
