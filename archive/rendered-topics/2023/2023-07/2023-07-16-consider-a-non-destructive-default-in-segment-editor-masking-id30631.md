# Consider a non-destructive default in segment editor masking options

**Topic ID**: 30631
**Date**: 2023-07-16
**URL**: https://discourse.slicer.org/t/consider-a-non-destructive-default-in-segment-editor-masking-options/30631

---

## Post #1 by @chir.set (2023-07-16 17:26 UTC)

<p>The item ‘Modify other segments’ in the masking options of the ‘Segment editor’ defaults to ‘Overwrite all’. When working with multiple segments, we may forget to switch to ‘Allow overlap’ so as to preserve prior work, and notices it when we can’t revert changes.</p>
<p>I hereby suggest that this item defaults to ‘Allow overlap’ rather. If it is forgotten as such, nothing is lost, and ‘Subtract’ in ‘Logical operators’ can still be used.</p>
<p>Thank you for considering.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2023-07-17 19:01 UTC)

<p>This default can be set in the application startup file as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-default-segmentation-options">here</a>.</p>
<p>If we get some votes on this feature request then we will add GUI for this. We would also welcome a pull request that adds this option to application settings.</p>

---

## Post #3 by @chir.set (2023-07-17 19:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="30631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-default-segmentation-options" rel="noopener nofollow ugc">here</a></p>
</blockquote>
</aside>
<p>This works perfectly well, thank you.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="30631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>a pull request that adds this option to application settings</p>
</blockquote>
</aside>
<p>Can you please hint the location of application settings in the source tree ?</p>

---

## Post #4 by @lassoan (2023-07-17 20:13 UTC)

<p>Segmentation settings are implemented in <code>qSlicerSegmentationsSettingsPanel.cxx</code>.</p>
<p>You can implement <code>GetOverwriteMode()</code> and <code>SetOverwriteMode(...)</code> methods in vtkSlicerSegmentationsModuleLogic.cxx to get/set the default <code>OverwriteMode</code> - very similarly how <code>vtkSlicerSegmentationsModuleLogic::GetDefaultSurfaceSmoothingEnabled()</code> and <code>vtkSlicerSegmentationsModuleLogic::SetDefaultSurfaceSmoothingEnabled()</code> are implemented. You can then use these methods in <code>qSlicerSegmentationsSettingsPanel</code>.</p>

---
