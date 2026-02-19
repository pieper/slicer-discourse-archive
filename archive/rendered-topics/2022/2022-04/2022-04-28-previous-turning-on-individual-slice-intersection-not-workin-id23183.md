---
topic_id: 23183
title: "Previous Turning On Individual Slice Intersection Not Workin"
date: 2022-04-28
url: https://discourse.slicer.org/t/23183
---

# Previous turning on individual slice intersection not working

**Topic ID**: 23183
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/previous-turning-on-individual-slice-intersection-not-working/23183

---

## Post #1 by @jamesobutler (2022-04-28 17:21 UTC)

<p>Using an older Slicer version 2021-09-14 I was able to turn on a single slice intersection with the following:</p>
<pre data-code-wrap="python"><code class="lang-python">slice_widget = slicer.app.layoutManager().sliceWidget("Red")
composite_node = slice_widget.sliceLogic().GetSliceCompositeNode()
composite_node.SetSliceIntersectionVisibility(True)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0277a258304e6c7b62383eee1af89d12c904dd9f.png" data-download-href="/uploads/short-url/lPgJESYshsDIJvfXeOV19yU1n9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0277a258304e6c7b62383eee1af89d12c904dd9f_2_690x366.png" alt="image" data-base62-sha1="lPgJESYshsDIJvfXeOV19yU1n9" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0277a258304e6c7b62383eee1af89d12c904dd9f_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0277a258304e6c7b62383eee1af89d12c904dd9f_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0277a258304e6c7b62383eee1af89d12c904dd9f_2_1380x732.png 2x" data-dominant-color="8E8E93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 75.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but now with a recent Slicer version (2022-04-26) it doesn’t produce the same output. There is no red line observed in the green and yellow slice view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6d5af4bec98662031d9932af89d7a334527369e.png" data-download-href="/uploads/short-url/wW3DpwOgsW8cenY8zhrCHAXcsHQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d5af4bec98662031d9932af89d7a334527369e_2_690x366.png" alt="image" data-base62-sha1="wW3DpwOgsW8cenY8zhrCHAXcsHQ" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d5af4bec98662031d9932af89d7a334527369e_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d5af4bec98662031d9932af89d7a334527369e_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6d5af4bec98662031d9932af89d7a334527369e_2_1380x732.png 2x" data-dominant-color="8E8E93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 74.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this a bug? Is there a better way to turn on a single slice intersection as was attempted before?</p>

---

## Post #2 by @lassoan (2022-04-28 18:02 UTC)

<p>Does this explain the change and helpful for updating your code?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_SliceIntersectionVisibility_was_moved_from_vtkMRMLSliceCompositeNode_to_vtkMRMLSliceDisplayNode">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_SliceIntersectionVisibility_was_moved_from_vtkMRMLSliceCompositeNode_to_vtkMRMLSliceDisplayNode</a></p>

---

## Post #3 by @jamesobutler (2022-04-28 18:27 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="23183">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<pre><code class="lang-auto">slice_widget = slicer.app.layoutManager().sliceWidget("Red")
composite_node = slice_widget.sliceLogic().GetSliceCompositeNode()
composite_node.SetSliceIntersectionVisibility(True)
</code></pre>
</blockquote>
</aside>
<p>^ Using the above code in latest Slicer preview I get the following warning which indicates that method is deprecated, but it doesn’t actually produce the same results as before. There seems to be broken backwards compatibility behavior introduced in <a href="https://github.com/Slicer/Slicer/commit/0798137cca6c4b93e683d88cff15bb76d338fd62" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add back vtkMRMLSliceCompositeNode::SetSliceIntersectionVisibili… · Slicer/Slicer@0798137 · GitHub</a>?</p>
<pre><code class="lang-auto">[WARNING][VTK] 28.04.2022 14:19:07 [vtkMRMLSliceCompositeNode (0000024DDED0EEB0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSliceCompositeNode.cxx:301) - SetSliceIntersectionVisibility method is deprecated. Use SetIntersectingSlicesVisibility method of vtkMRMLSliceDisplayNode object instead.
</code></pre>
<p>Attempting to use a newer method I’m still unable to achieve the same results as previously (there is no red line in the green and yellow slice views upon calling <code>SetIntersectingSlicesVisibility</code>.</p>
<pre data-code-wrap="python"><code class="lang-python">slice_widget = slicer.app.layoutManager().sliceWidget("Red")
slice_widget.sliceLogic().GetSliceDisplayNode().SetIntersectingSlicesVisibility(True)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cca726ad5f8c3cdb9cd37f9fbcc851ae4dfa220.png" data-download-href="/uploads/short-url/1P9t9wwjcbRopaNKFdQDRbGRIJO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cca726ad5f8c3cdb9cd37f9fbcc851ae4dfa220_2_690x366.png" alt="image" data-base62-sha1="1P9t9wwjcbRopaNKFdQDRbGRIJO" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cca726ad5f8c3cdb9cd37f9fbcc851ae4dfa220_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cca726ad5f8c3cdb9cd37f9fbcc851ae4dfa220_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cca726ad5f8c3cdb9cd37f9fbcc851ae4dfa220_2_1380x732.png 2x" data-dominant-color="8E8E93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-04-28 19:04 UTC)

<p>Both the deprecated and the new methods work, but the changes only take effect if a slice nodes are updated, for example like this:</p>
<pre><code class="lang-python">sliceNodes = getNodesByClass('vtkMRMLSliceNode')
for sliceNode in sliceNodes:
    sliceNode.Modified()
</code></pre>
<p>Of course this forced update should not be necessary. This is a regression introduced when the interactive slice intersection feature was introduced. We spent a lot of time trying to fix all the issues, but at some point we had to decide between rejecting this feature or get it in even though there are still problems with it. I think we fixed most of the issues that come up when using the GUI, but workarounds are needed when the feature is used programmatically.</p>
<p>You can submit a bug report and we’ll eventually get to it, but probably only when there is interest/funding for making interactive slice intersections fully functional (e.g., compatible with Segment Editor).</p>

---

## Post #5 by @jamesobutler (2022-04-28 20:57 UTC)

<p>The force update works. I’ve issued <a href="https://github.com/Slicer/Slicer/pull/6339" class="inline-onebox" rel="noopener nofollow ugc">DOC: Include workaround to force visual update of intersecting slices by jamesobutler · Pull Request #6339 · Slicer/Slicer · GitHub</a> to update the documentation around the script repository example to include this update.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="23183">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can submit a bug report and we’ll eventually get to it</p>
</blockquote>
</aside>
<p>I’ve written up the bug report at <a href="https://github.com/Slicer/Slicer/issues/6338" class="inline-onebox" rel="noopener nofollow ugc">Programmatically setting slice intersection visibility does not update slice views immediately · Issue #6338 · Slicer/Slicer · GitHub</a></p>
<p>For my specific case of updating a single slice view intersection the following works for me which is also using the non-deprecated API.</p>
<pre data-code-wrap="python"><code class="lang-python">slice_widget = slicer.app.layoutManager().sliceWidget("Red")
slice_widget.sliceLogic().GetSliceDisplayNode().SetIntersectingSlicesVisibility(True)
slice_widget.sliceLogic().GetSliceNode().Modified()
</code></pre>

---
