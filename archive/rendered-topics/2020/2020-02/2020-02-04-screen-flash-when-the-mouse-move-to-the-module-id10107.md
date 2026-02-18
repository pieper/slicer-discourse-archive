# Screen flash when the mouse move to the module

**Topic ID**: 10107
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/screen-flash-when-the-mouse-move-to-the-module/10107

---

## Post #1 by @timeanddoctor (2020-02-04 15:30 UTC)

<p>Screen flash when the mouse move to the module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57ff302be7c238b4c332deec4b2cbc8511eafaee.gif" data-download-href="/uploads/short-url/cysheRSczMyJaV2hYp3Mf0xLh5s.gif?dl=1" title="841ak-z5ra2 (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57ff302be7c238b4c332deec4b2cbc8511eafaee_2_690x388.gif" alt="841ak-z5ra2 (2)" data-base62-sha1="cysheRSczMyJaV2hYp3Mf0xLh5s" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57ff302be7c238b4c332deec4b2cbc8511eafaee_2_690x388.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57ff302be7c238b4c332deec4b2cbc8511eafaee_2_1035x582.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57ff302be7c238b4c332deec4b2cbc8511eafaee_2_1380x776.gif 2x"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">841ak-z5ra2 (2)</span><span class="informations">1920×1080 3.29 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code>class testWidget(object):
</code></pre>
<p>def <strong>init</strong>(self, parent = None):</p>
<pre><code>if not parent:
  self.parent = slicer.qMRMLWidget()
  self.parent.setLayout(qt.QVBoxLayout())
  self.parent.setMRMLScene(slicer.mrmlScene)
else:
  self.parent = parent
self.layout = self.parent.layout()
if not parent:
  self.setup()
  self.parent.show()
</code></pre>
<p>def setup(self):<br>
# Instantiate and connect widgets …</p>
<pre><code>#
#
# Parameters Area
#
parametersCollapsibleButton = ctk.ctkCollapsibleButton()
parametersCollapsibleButton.text = "Parameters"
self.layout.addWidget(parametersCollapsibleButton)
parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)
</code></pre>

---

## Post #2 by @lassoan (2020-02-04 16:31 UTC)

<p>This happens because there is nothing the module GUI that would constrain the width of the panel, so the   panel is resized to the minimum necessary. The minimum size depends only on “Data Probe” panel content (at the bottom), which is changing when you move over/away from a slice view.</p>
<p>At some point, we’ll rework the Data Probe panel to have more robust size policy, but until then you can fix this by setting a suitable size policy in widgets in your module (e.g., set preferred or minimum size for the button).</p>

---
