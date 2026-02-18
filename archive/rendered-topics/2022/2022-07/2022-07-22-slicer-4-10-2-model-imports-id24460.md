# Slicer 4.10.2 Model Imports

**Topic ID**: 24460
**Date**: 2022-07-22
**URL**: https://discourse.slicer.org/t/slicer-4-10-2-model-imports/24460

---

## Post #1 by @ChristophG123 (2022-07-22 20:33 UTC)

<p>I’m trying to import stl files from my PC on Slicer 4.10.2 because I’m modifying an old module that doesn’t work on newer versions of Slicer. However, it seems like the code I normally use on Slicer 5.1.0 doesn’t work for this, and I was wondering what the correct commands are. Here is what I have:</p>
<pre><code class="lang-auto">    self.stylusModel = slicer.util.loadModel('C:/calibrationClarius/Current_Models/stylusV2')
    self.stylusModelDisplayNode = self.stylusModel.GetDisplayNode()
    self.stylusModelDisplayNode.SetColor(0, 0.5, 0.1)
</code></pre>
<p>And here is the error on the Slicer python console:</p>
<pre><code class="lang-auto">File "C:/calibrationClarius/leahCalibModified/Calibration/Calibration.py", line 47, in __init__
    self.stylusModelDisplayNode = self.stylusModel.GetDisplayNode()
AttributeError: 'bool' object has no attribute 'GetDisplayNode'
</code></pre>
<p>Furthermore, I was wondering where I could find an old Script repository for code that works on 4.10.2 I can refer to in the future. Thanks</p>

---

## Post #2 by @pieper (2022-07-22 23:29 UTC)

<p>In older versions of <code>loadModel</code> you needed to provide an extra boolean parameter <code>returnNode=True</code> as <a href="https://discourse.slicer.org/t/simplifying-slicer-util-load-functions/7270">described here</a>.</p>

---

## Post #3 by @lassoan (2022-07-23 05:22 UTC)

<aside class="quote no-group" data-username="ChristophG123" data-post="1" data-topic="24460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/christophg123/48/15483_2.png" class="avatar"> ChristophG123:</div>
<blockquote>
<p>I’m modifying an old module that doesn’t work on newer versions of Slicer.</p>
</blockquote>
</aside>
<p>I would recommend to update the module instead of downgrade Slicer. Check out the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer">migration guide</a> for description of API changes and how to update old code. You can ask on this forum if you cannot figure out how to update any specific part in your module.</p>

---
