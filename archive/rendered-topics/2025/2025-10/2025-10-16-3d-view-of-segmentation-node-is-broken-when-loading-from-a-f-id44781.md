# 3D view of segmentation node is broken when loading from a file

**Topic ID**: 44781
**Date**: 2025-10-16
**URL**: https://discourse.slicer.org/t/3d-view-of-segmentation-node-is-broken-when-loading-from-a-file/44781

---

## Post #1 by @Victor_Wayne (2025-10-16 10:30 UTC)

<p>Hello,</p>
<p>I am facing an issue of segmentation node being broken when loading from a file. When I segment it and work with it, it is being displayed pretty accurately. But when I load it from a mrml file it has some extra pieces in the parts where it should be an empty pit.</p>
<p>Setting the segmentation node’s master representation to a closed surface representation fixes that, but it messes up the 2d view. I used the function <code>SetSourceRepresentationToClosedSurface()</code> to change the master/source representation.</p>
<p>I found two functions in the in the vtkMRMLSegmentationDisplayNode. That functions are<br>
<code>void SetPreferredDisplayRepresentation2D(const char*</code><em><code>)</code><br>
<code>void SetPreferredDisplayRepresentation3D(const char</code></em><code>*)</code></p>
<p>But I can’t seem to find what string I should pass in this function. There is no additional docstring in the .h file. In fact, there is no declarationg of this function in the .h file.</p>
<p>Is there any way to fix it?</p>
<p>Thanks for your help in advance.</p>

---

## Post #2 by @lassoan (2025-10-16 12:28 UTC)

<p>Rendering of the closed surface representation in slice views may have rendering artifacts if the surface is too complex. You can try to smooth and simplify the surface to avoid this.</p>
<p>Alternatively, you can use binary labelmap as source representation. In that case, 2D views are always correct. However, you may need to set higher resolution to preserve more details.</p>
<aside class="quote no-group" data-username="Victor_Wayne" data-post="1" data-topic="44781">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar"> Victor_Wayne:</div>
<blockquote>
<p>I found two functions in the in the vtkMRMLSegmentationDisplayNode. That functions are<br>
<code>void SetPreferredDisplayRepresentation2D(const char*</code> <em><code>)</code><br>
<code>void SetPreferredDisplayRepresentation3D(const char</code></em> <code>*)</code></p>
<p>But I can’t seem to find what string I should pass in this function.</p>
</blockquote>
</aside>
<p>There is no fixed set of representation names, because any extension can specify additional representations. However, for convenience, the most commonly used representation names are available from the <code>vtkSegmentationConverter</code> class. For example:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.vtkSegmentationConverter.GetBinaryLabelmapRepresentationName()
'Binary labelmap'
&gt;&gt;&gt; slicer.vtkSegmentationConverter.GetClosedSurfaceRepresentationName()
'Closed surface'
</code></pre>

---

## Post #3 by @Victor_Wayne (2025-10-17 05:28 UTC)

<p>Can you pleas explain about setting higher resolution? you want me to set it to the mesh? how do I do it programmatically?</p>

---

## Post #4 by @lassoan (2025-10-17 18:58 UTC)

<p>You can set the segmentation higher resolution labelmap when importing a model as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">here</a>. If you confirm that this solves your problems and you cannot figure out how to achieve it using Python scripting then let us know.</p>

---
