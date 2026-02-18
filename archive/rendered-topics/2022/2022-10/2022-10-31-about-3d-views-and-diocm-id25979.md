# About 3d views and diocm

**Topic ID**: 25979
**Date**: 2022-10-31
**URL**: https://discourse.slicer.org/t/about-3d-views-and-diocm/25979

---

## Post #1 by @miniminic (2022-10-31 09:32 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb15910009e548168a97972b7c0efeaebbb8ef5b.jpeg" data-download-href="/uploads/short-url/xxEpviLMQkIEs49WhmJiP6dztKb.jpeg?dl=1" title="屏幕截图 2022-10-31 172939" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb15910009e548168a97972b7c0efeaebbb8ef5b_2_460x500.jpeg" alt="屏幕截图 2022-10-31 172939" data-base62-sha1="xxEpviLMQkIEs49WhmJiP6dztKb" width="460" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb15910009e548168a97972b7c0efeaebbb8ef5b_2_460x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb15910009e548168a97972b7c0efeaebbb8ef5b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb15910009e548168a97972b7c0efeaebbb8ef5b.jpeg 2x" data-dominant-color="90AACE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-10-31 172939</span><span class="informations">591×641 51.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I don’t know what I accidentally changed, but when I added a scene and showed dicom, it was translucent like this…<br>
Another question, I want to hide this purple box that wraps the model, is there a way to hide it</p>

---

## Post #2 by @miniminic (2022-11-01 07:06 UTC)

<p>hide box<br>
viewNode = slicer.util.getNode(‘vtkMRMLViewNode1’)<br>
viewNode.SetAxisLabelsVisible(False)<br>
viewNode.SetBoxVisible(False)</p>

---

## Post #3 by @cpinter (2022-11-04 11:39 UTC)

<p>You can try this to make the slices opaque again:</p>
<pre><code class="lang-auto">y = getNode('Yellow Volume Slice')
y.GetDisplayNode().SetOpacity(1.0)
</code></pre>

---
