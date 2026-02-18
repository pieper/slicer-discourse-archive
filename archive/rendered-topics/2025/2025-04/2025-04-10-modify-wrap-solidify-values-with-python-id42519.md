# Modify Wrap Solidify values with Python

**Topic ID**: 42519
**Date**: 2025-04-10
**URL**: https://discourse.slicer.org/t/modify-wrap-solidify-values-with-python/42519

---

## Post #1 by @Kalman (2025-04-10 12:58 UTC)

<p>Hi! I have a question regarding accessing the <strong>Wrap Solidify</strong> extension through scripting - in a certain step it uses predefined values to perform a wrapping on the active segment.  (I’m using Slicer version 5.8.1)</p>
<p><strong>Background:</strong> I have tried many different approaches in the coding, but I couldn’t find a way to modify the slider values through the Python console. I attach a basic script below to show how it was given to the console.</p>
<p><strong>The issue:</strong> What I have found, that even though the parameters were given directly, the execution still uses those values which are shown in the UI window of the wrap solidify.</p>
<p><strong>The question</strong>: what should be modified to be able to change the individual floating value parameters?</p>
<p>Thank you for your help!</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
effect = segmentEditorWidget.activeEffect()

if not effect:
    raise RuntimeError("❌ Wrap Solidify effect not found!")

effect.setParameter("region", "largestCavity")
effect.setParameter("splitCavities", True)
effect.setParameter("splitCavitiesDiameterMm", 2.0)  
effect.setParameter("smoothingFactor", 0.3)       
effect.setParameter("oversamplingFactor", 1.0)    
effect.setParameter("numberOfIterations", 1)     
effect.setParameter("outputType", "newSegment")      
effect.setParameter("saveIntermediateResults", False)

effect.self().onApply()

print("Wrap Solidify applied with predefined parameters.")
slicer.app.processEvents()


</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d707d3cecd3678021a291e5dc50354707c4d5ab.jpeg" data-download-href="/uploads/short-url/6tYuzPHYIgEE6W8N3ZPkRwUskqL.jpeg?dl=1" title="wrap_img" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d707d3cecd3678021a291e5dc50354707c4d5ab.jpeg" alt="wrap_img" data-base62-sha1="6tYuzPHYIgEE6W8N3ZPkRwUskqL" width="500" height="423"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">wrap_img</span><span class="informations">500×423 32.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-04-10 13:17 UTC)

<p>Pass strings to <code>setParameter</code>, ex <code>str(1)</code>.</p>

---

## Post #3 by @Kalman (2025-04-10 13:27 UTC)

<p>Dear <a class="mention" href="/u/chir.set">@chir.set</a>,</p>
<p>Thank you for the quick response! I have tried it (script attached), but the program still uses those values written in the UI boxes and not the one given via the Python script.</p>
<p>What is your suggestion?</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
effect = segmentEditorWidget.activeEffect()

if not effect:
    raise RuntimeError("❌ Wrap Solidify effect not found!")

effect.setParameter("region", "largestCavity")
effect.setParameter("splitCavities", True)
effect.setParameter("splitCavitiesDiameterMm", str(2.0))  
effect.setParameter("smoothingFactor", str(0.3))       
effect.setParameter("oversamplingFactor", str(1.0))    
effect.setParameter("numberOfIterations", str(1))     
effect.setParameter("outputType", "newSegment")      
effect.setParameter("saveIntermediateResults", False)

effect.self().onApply()

print("Wrap Solidify applied with predefined parameters.")
slicer.app.processEvents()
</code></pre>

---

## Post #4 by @chir.set (2025-04-10 13:51 UTC)

<p>You can poke the right parameter names in <code>SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py</code>.</p>
<p>For example, <code>splitCavitiesDiameterMm</code> should have been <code>splitCavitiesDiameter</code>.</p>

---

## Post #5 by @Kalman (2025-04-10 13:58 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a>: Thank you very much! I’ve checked the source, revised it accordingly, and now it works fine!</p>
<p>I paste below the updated script for those who has similar issues that they could see the corrected version:</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
effect = segmentEditorWidget.activeEffect()

effect.setParameter("region", "largestCavity")
effect.setParameter("splitCavities", str(True))
effect.setParameter("splitCavitiesDiameter", str(2.0))
effect.setParameter("smoothingFactor", str(0.3))
effect.setParameter("remeshOversampling", str(1.0))
effect.setParameter("shrinkwrapIterations", str(1))
effect.setParameter("outputType", "newSegment")
effect.setParameter("saveIntermediateResults", str(False))

effect.self().onApply()

print("Wrap Solidify applied with corrected parameters.")
slicer.app.processEvents()

</code></pre>

---
