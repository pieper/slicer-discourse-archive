# Apply transform matirx to only specific 2D view

**Topic ID**: 36273
**Date**: 2024-05-20
**URL**: https://discourse.slicer.org/t/apply-transform-matirx-to-only-specific-2d-view/36273

---

## Post #1 by @park (2024-05-20 07:14 UTC)

<p>Hi all,</p>
<p>I tried to apply a transform matirx to specific slice view. For example…</p>
<p>I have volume or model data A, B, C, D, and a transform matrix T (non-linear). I want to apply T only in the Red View and not in the Yellow and Green views.</p>
<p>The easiest way would be to copy A, B, C, D to create A’, B’, C’, D’, and then apply T to display them in the red view. However, this doesn’t seem efficient.</p>
<p>Is there any other way to implement this?</p>

---

## Post #2 by @pieper (2024-05-20 14:42 UTC)

<p>I don’t think there’s a way to only apply the transform in one view currently, although it’s conceivable that this could be added as a per-view display node option.</p>
<p>If this is all under the control of your custom code, then managing copies of the nodes is probably the easiest and depending on the application the extra data may not be a practical issue.  Or if the memory overhead is too great then another option could be to share the underlying <code>vtkImageData</code> or <code>vtkPolyData</code> between multiple nodes - we don’t usually do this but I believe it should work.</p>

---

## Post #3 by @park (2024-05-21 14:22 UTC)

<p>Thank you Steve !</p>
<p>I try to copy node form transformation</p>
<p>Best,</p>

---

## Post #4 by @park (2024-06-11 14:49 UTC)

<p>Hello Steve,</p>
<p>I tried to solve this issue through copying, but it seems too cumbersome to manage the data as there are over 10 nodes to copy, and all these nodes need to be synced.</p>
<p>Therefore, I’m considering implementing the application of gridTransform only to specific views. It seems applying module transform to the vtkactor entering that view would suffice, but is there a way to implement this?</p>
<p>If so, would it require modifying the slicer source?</p>

---

## Post #5 by @pieper (2024-06-13 21:31 UTC)

<p>Hi <a class="mention" href="/u/park">@park</a> - Yes, it makes sense that keeping nodes in sync would involve a lot of bookkeeping.  It’s probably doable with the right abstraction but may not be worth it for you.</p>
<p>Updating the slice display to enable/disable specific transforms is also possible.  It would involve updates to the C++ implementation, but since you have a custom app you have this option.  It would be best to follow the example of the other view-specific display options, perhaps generalizing to have multiple transform nodes just as there are multiple display nodes curently.</p>

---

## Post #6 by @hortakc (2024-06-15 18:28 UTC)

<p>Hello <a class="mention" href="/u/park">@park</a><br>
Please, can you tell me which version of Slicer are you using?<br>
I used to have the “Apply Matrix” extension on Slicer 4.0.0. But now that I am using Slicer 5.6.0 I can’t install the extension.</p>

---
