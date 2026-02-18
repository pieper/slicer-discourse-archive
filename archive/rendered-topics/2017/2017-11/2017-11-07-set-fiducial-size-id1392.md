# Set fiducial size?

**Topic ID**: 1392
**Date**: 2017-11-07
**URL**: https://discourse.slicer.org/t/set-fiducial-size/1392

---

## Post #1 by @hherhold (2017-11-07 00:23 UTC)

<p>Apologies if this has been asked or addressed elsewhere - I looked through the docs but didn’t see anything.</p>
<p>Is there a way to set the size of the fiducial markers in the 3D view? Many of the specimens I work on (CT of fossil insects) are millimeters in size, and the fiducial markers show as these giant spheres in 3D.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-11-07 00:32 UTC)

<p>Markups module -&gt; Advanced / Glyph scale</p>

---

## Post #3 by @hherhold (2017-11-07 00:37 UTC)

<p>Hmm, that doesn’t seem to change the fiducial markers placed when using the Surface Cut tool in the Segment Editor Expansion module. Is there a way to tweak those?</p>
<p>Thanks!!!</p>

---

## Post #4 by @lassoan (2017-11-07 01:55 UTC)

<p>Surface cut tool creates temporary markup nodes, so by the time you would open the Markups module, the markup node is gone. I’ve modified the effect a little bit so to use default markups properties that are defined in the scene (new version is available in the nightly build that you download tomorrow or later).</p>
<p>To change default markup size, add these lines to the Slicer startup script (you can edit it by opening Application Settings and clicking the “open” icon next to “Application startup script”):</p>
<pre><code>defaultMarkupsDisplayNode = slicer.vtkMRMLMarkupsDisplayNode()
defaultMarkupsDisplayNode.SetGlyphScale(9.0)
slicer.mrmlScene.AddDefaultNode(defaultMarkupsDisplayNode)
</code></pre>
<p>In general, if you work with images where the complete image is under a millimeter, you might try to change your image spacing to be 1000x larger (in Volumes module); and in Application Settings, set unit to micrometer. That way your images may have a more similar scale than the commonly used human anatomical images, so you will be less likely to run into these kind of issues.</p>

---
