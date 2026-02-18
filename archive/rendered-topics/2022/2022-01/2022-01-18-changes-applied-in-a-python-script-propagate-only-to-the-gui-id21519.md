# Changes applied in a python script propagate only to the GUI but don't get displayed

**Topic ID**: 21519
**Date**: 2022-01-18
**URL**: https://discourse.slicer.org/t/changes-applied-in-a-python-script-propagate-only-to-the-gui-but-dont-get-displayed/21519

---

## Post #1 by @koeglfryderyk (2022-01-18 18:28 UTC)

<p>I’m trying to write a script that applies a color gradient to a markups curve.</p>
<p>All the changes are visible in the GUI, but the displayed curve does not change. To change the curve I have to manually click on something in the GUi (to update it?).</p>
<p>This is my code</p>
<pre><code class="lang-auto"># get color table
iron = slicer.util.getFirstNodeByName("Iron")

curveNode = slicer.mrmlScene.GetFirstNodeByName("MarkupsCurve_2")
dispNode = curveNode.GetDisplayNode()
dispNode.SetActiveScalarName("PedigreeIDs")
dispNode.SetAndObserveColorNodeID(iron.GetID())
dispNode.SetScalarVisibility(1)
</code></pre>
<p>This is how it looks after the code is executed (the Iron color table is not applied):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/878a6e97933e1e0a7effb41ee2e372fe6a167b72.png" data-download-href="/uploads/short-url/jl32Xn5jhTXUZsrUmxBiTRY08a6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/878a6e97933e1e0a7effb41ee2e372fe6a167b72_2_690x200.png" alt="image" data-base62-sha1="jl32Xn5jhTXUZsrUmxBiTRY08a6" width="690" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/878a6e97933e1e0a7effb41ee2e372fe6a167b72_2_690x200.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/878a6e97933e1e0a7effb41ee2e372fe6a167b72_2_1035x300.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/878a6e97933e1e0a7effb41ee2e372fe6a167b72.png 2x" data-dominant-color="CDCCE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×369 26.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then, if I e.g. click twice on the  ‘Visibile:’ checkbox, the view gets updated (the Iron color table is applied):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9950ebe1a5b41844ea815ecc6287309b5b90be2.png" data-download-href="/uploads/short-url/qtJGyGAUSTblaUf4CpjpKFTj2cW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9950ebe1a5b41844ea815ecc6287309b5b90be2_2_690x188.png" alt="image" data-base62-sha1="qtJGyGAUSTblaUf4CpjpKFTj2cW" width="690" height="188" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9950ebe1a5b41844ea815ecc6287309b5b90be2_2_690x188.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9950ebe1a5b41844ea815ecc6287309b5b90be2_2_1035x282.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9950ebe1a5b41844ea815ecc6287309b5b90be2.png 2x" data-dominant-color="CECDE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1250×341 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-01-18 20:31 UTC)

<p>You can make the coloring appear like this:</p>
<pre><code class="lang-python">iron = slicer.util.getFirstNodeByName("Iron")
curveNode = slicer.mrmlScene.GetFirstNodeByName("OC")
dispNode = curveNode.GetDisplayNode()
dispNode.SetAndObserveColorNodeID(iron.GetID())
dispNode.SetActiveScalarName("PedigreeIDs")
dispNode.SetScalarVisibility(1)
dispNode.UpdateAssignedAttribute()
dispNode.Modified()
</code></pre>
<p>The last two lines should not be needed (should be called automatically internally) - I’ll fix that soon in Slicer core.</p>

---

## Post #3 by @lassoan (2022-01-18 21:09 UTC)

<p>The issue is now <a href="https://github.com/Slicer/Slicer/commit/60042b1ef63ef262289a6d1ea0eaa6399d5cbcde">fixed</a>, in Slicer Preview Releases downloaded tomorrow or later the last two lines of the script above will not be necessary anymore.</p>

---
