# How to display markups node only in a specific slice view?

**Topic ID**: 36298
**Date**: 2024-05-21
**URL**: https://discourse.slicer.org/t/how-to-display-markups-node-only-in-a-specific-slice-view/36298

---

## Post #1 by @park (2024-05-21 14:20 UTC)

<p>Hi all</p>
<p>I would like to make marksupNode and marksupCurveNode visible only in the red slice. (I prefer them to remain invisible in the green and yellow slices.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8b62d738886d197fee071cb433041905a2a2269.gif" data-download-href="/uploads/short-url/o4uwM1OZvtY6fIjK0GYF9jQoo0F.gif?dl=1" title="스크린샷 2024-05-21 오후 11.20.16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8b62d738886d197fee071cb433041905a2a2269_2_690x249.gif" alt="스크린샷 2024-05-21 오후 11.20.16" data-base62-sha1="o4uwM1OZvtY6fIjK0GYF9jQoo0F" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8b62d738886d197fee071cb433041905a2a2269_2_690x249.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8b62d738886d197fee071cb433041905a2a2269.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8b62d738886d197fee071cb433041905a2a2269.gif 2x" data-dominant-color="424040"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2024-05-21 오후 11.20.16</span><span class="informations">801×290 84.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please provide an example for achieving this?</p>

---

## Post #2 by @Sunderlandkyl (2024-05-21 14:31 UTC)

<p>You can do it with something like this:</p>
<pre data-code-wrap="python"><code class="lang-python">markupsNode.GetDisplayNode().SetViewNodeIDs(["vtkMRMLSliceNodeRed"])
</code></pre>
<p>You just need to specify the ids for all of the views in which it should be visible.</p>
<p><a href="https://apidocs.slicer.org/main/classvtkMRMLDisplayNode.html#a8fd9a8d62109f08b3720edc8e174a546" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/main/classvtkMRMLDisplayNode.html#a8fd9a8d62109f08b3720edc8e174a546</a></p>

---
