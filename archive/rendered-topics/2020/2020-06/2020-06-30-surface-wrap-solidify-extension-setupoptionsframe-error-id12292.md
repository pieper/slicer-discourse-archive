# Surface Wrap Solidify extension: setupOptionsFrame error

**Topic ID**: 12292
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/surface-wrap-solidify-extension-setupoptionsframe-error/12292

---

## Post #1 by @dmarquette (2020-06-30 12:00 UTC)

<p>Operating system: macOS Catalina 10.15.5<br>
Slicer version: 4.10.2<br>
Expected behavior: Open “Segment editor” module without any error displaying in the Python interactor<br>
Actual behavior: Each time I open the “Segment editor” module the same error message is displayed (see below)</p>
<p>Traceback (most recent call last):<br>
File “/Users/dianemarquette/Documents/3DSlicer/Slicer-SurfaceWrapSolidify-master/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py”, line 140, in updateGUIFromMRML<br>
widgetClassName = widget.metaObject().getClassName()<br>
AttributeError: QMetaObject has no attribute named ‘getClassName’</p>
<p>After checking the SegmentEditorEffect.py file, this error seems to imply that the Surface Wrap extension doesn’t manage to connect to the segment editor. Ticking boxes in the Surface wrap UI doesn’t seem to update the views.</p>
<p>Because the Surface Wrap extension isn’t available in the Extensions Manager of Slicer 4.10.2 (at least, I couldn’t find it), I downloaded the extension from Github and added it to Slicer using the “Select Extension” tool from “Extension Wizard”.</p>
<p>If you have any ideas on how to fix this error or if I missed something when installing the extension, all suggestions would be very helpful and highly appreciated!</p>

---

## Post #2 by @lassoan (2020-06-30 21:21 UTC)

<aside class="quote no-group" data-username="dmarquette" data-post="1" data-topic="12292">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/58956e/48.png" class="avatar"> dmarquette:</div>
<blockquote>
<p>Because the Surface Wrap extension isn’t available in the Extensions Manager of Slicer 4.10.2 (at least, I couldn’t find it), I downloaded the extension from Github and added it to Slicer using the “Select Extension” tool from “Extension Wizard”.</p>
</blockquote>
</aside>
<p>The extension is not available for Slicer-4.10 because it relies on features added in Slicer-4.11. I would recommend to upgrade to Slicer-4.11, as it has many more features and lots of fixes and soon will be release as the new stable version.</p>

---
