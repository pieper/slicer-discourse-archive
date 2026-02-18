# Issue when enabling the new interaction transform handler using script

**Topic ID**: 36509
**Date**: 2024-05-31
**URL**: https://discourse.slicer.org/t/issue-when-enabling-the-new-interaction-transform-handler-using-script/36509

---

## Post #1 by @chz31 (2024-05-31 01:24 UTC)

<p>Hi,</p>
<p>I met a strange issue when I tried to enable interaction transform handler using script using the newest preview Slicer 5.7.0-2024-05-28 in Mac.</p>
<p>The command <code>interactionTransformNode.GetDisplayNode().SetEditorVisibility(True)</code> can only enable the interaction transform handler when I switched to the <code>Transforms</code> module.</p>
<p>If I just created a blank vtkMRMLTransform node in the Data module, add the volume to the transform, then do  <code>interactionTransformNode.GetDisplayNode().SetEditorVisibility(True)</code>, it would not find <code>SetEditorVisibility</code> attribute. For example:</p>
<pre><code class="lang-auto">headNode = slicer.util.getNode('MRHead')
interactionTransformNode =  slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', "interaction_transform")
headNode.SetAndObserveTransformNodeID(self.interactionTransformNode.GetID())
interactionTransformNode.GetDisplayNode().SetEditorVisibility(True)
</code></pre>
<p>It would report:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bb158fe05f5e9412496aef054dac7fdf3194a89.png" data-download-href="/uploads/short-url/6ewuNzcFrJVIVbQwDfpndsJUDj3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bb158fe05f5e9412496aef054dac7fdf3194a89_2_517x61.png" alt="image" data-base62-sha1="6ewuNzcFrJVIVbQwDfpndsJUDj3" width="517" height="61" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bb158fe05f5e9412496aef054dac7fdf3194a89_2_517x61.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bb158fe05f5e9412496aef054dac7fdf3194a89_2_775x91.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bb158fe05f5e9412496aef054dac7fdf3194a89_2_1034x122.png 2x" data-dominant-color="F5E8ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1164×140 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Switching to the Transform module and the <code>SetEditorVisibility(True)</code> ran well to enable the interaction handle (see Python console).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bb08974911db1ae327aa1aa3dba18d4ec725e82.jpeg" data-download-href="/uploads/short-url/8w2oLh3tmcVAIMyrKcRJJ7XNaX8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb08974911db1ae327aa1aa3dba18d4ec725e82_2_517x265.jpeg" alt="image" data-base62-sha1="8w2oLh3tmcVAIMyrKcRJJ7XNaX8" width="517" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb08974911db1ae327aa1aa3dba18d4ec725e82_2_517x265.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb08974911db1ae327aa1aa3dba18d4ec725e82_2_775x397.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb08974911db1ae327aa1aa3dba18d4ec725e82_2_1034x530.jpeg 2x" data-dominant-color="ACAAAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×986 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I do not currently have access to Windows, but I believe I did not encounter an error in Windows.</p>

---

## Post #2 by @Sunderlandkyl (2024-05-31 02:09 UTC)

<p>You need to create the display node before trying to access it.</p>
<pre><code class="lang-auto">interactionTransformNode.CreateDefaultDisplayNodes()
</code></pre>

---

## Post #3 by @chz31 (2024-05-31 18:14 UTC)

<p>Thank you! It’s been solved!</p>

---
