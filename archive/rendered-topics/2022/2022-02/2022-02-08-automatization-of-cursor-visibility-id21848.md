# Automatization of cursor visibility

**Topic ID**: 21848
**Date**: 2022-02-08
**URL**: https://discourse.slicer.org/t/automatization-of-cursor-visibility/21848

---

## Post #1 by @bserrano (2022-02-08 08:59 UTC)

<p>Hi,</p>
<p>I want to set the cursor visibility of a centerline automatically. It can be done in module Models → select cursor → Display → Slice Display → Visibility.<br>
I tryied to write a code that does it automatically but I cannot find the functions that do that.<br>
I am suck after setting the cursor node:</p>
<pre><code class="lang-auto">slicer.util.selectModule('Models')
cursorNode = slicer.util.getNode("Cursor-Centerline curve (0)")
slicer.modules.models.widgetRepresentation().setEditedNode(cursorNode)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/027cd46873f665a321aab9716de1074fbec0e3c0.png" data-download-href="/uploads/short-url/m0oSU6ekUA96Att8EWyaOTtneU.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/027cd46873f665a321aab9716de1074fbec0e3c0_2_565x500.png" alt="imagen" data-base62-sha1="m0oSU6ekUA96Att8EWyaOTtneU" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/027cd46873f665a321aab9716de1074fbec0e3c0_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/027cd46873f665a321aab9716de1074fbec0e3c0_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/027cd46873f665a321aab9716de1074fbec0e3c0.png 2x" data-dominant-color="3B3E3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">982×869 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,</p>

---

## Post #2 by @mikebind (2022-02-08 19:36 UTC)

<p>This centerline is a ModelNode, and its display properties are controlled through an associated display node.</p>
<pre><code class="lang-auto">centerlineModelNode = slicer.util.getNode("Cursor-Centerline curve (0)")
centerlineDisplayNode = centerlineModelNode.GetDisplayNode()
centerlineDisplayNode.SetVisibility(1) # make sure the model is visible overall (if this was 0, then the separate 2D and 3D settings would have no effect) 
centerlineDisplayNode.SetVisibility2D(1) # show model in 2D slice views
centerlineDisplayNode.SetSliceIntersectionVisibility(1) 
# Other display settings are also available, e.g.
centerlineDisplayNode.SetSliceIntersectionThickness(10) # change intersection line thickness
</code></pre>

---

## Post #3 by @bserrano (2022-02-10 16:29 UTC)

<p>Thank you so much.<br>
This was exactly what I was looking for <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
