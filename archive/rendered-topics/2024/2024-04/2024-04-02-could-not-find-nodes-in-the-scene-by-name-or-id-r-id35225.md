---
topic_id: 35225
title: "Could Not Find Nodes In The Scene By Name Or Id R"
date: 2024-04-02
url: https://discourse.slicer.org/t/35225
---

# Could not find nodes in the scene by name or id 'R'

**Topic ID**: 35225
**Date**: 2024-04-02
**URL**: https://discourse.slicer.org/t/could-not-find-nodes-in-the-scene-by-name-or-id-r/35225

---

## Post #1 by @LucaB (2024-04-02 12:02 UTC)

<p>Operarting system: Macos Sonoma 14.1<br>
Slicer version: 5.6.1<br>
Expected behaviour Bounding box.</p>
<p>Hello,</p>
<p>I am trying to extract the bounding box from slicer. I am running in the python terminal all steps as previously mentioned in other topics. Namely</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np
bounds = np.zeros(6)
getNode("R").GetBounds(bounds)
</code></pre>
<p>where i receive the error.</p>
<pre><code class="lang-auto">raise MRMLNodeNotFoundException("could not find nodes in the scene by name or id '%s'" % (pattern if (isinstance(pattern, str)) else ""))

slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id 'R'
</code></pre>
<p>(as seen in the Screenshot)</p>
<p>I can not figure out what I am doing wrong. How can i prevent this error?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/471db6cf609724bf57473ff40e22a393aa210b73.jpeg" data-download-href="/uploads/short-url/a97ySwwBZjBscHuez1HemaBv2QX.jpeg?dl=1" title="Screenshot 2024-04-02 at 13.03.54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/471db6cf609724bf57473ff40e22a393aa210b73_2_690x409.jpeg" alt="Screenshot 2024-04-02 at 13.03.54" data-base62-sha1="a97ySwwBZjBscHuez1HemaBv2QX" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/471db6cf609724bf57473ff40e22a393aa210b73_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/471db6cf609724bf57473ff40e22a393aa210b73_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/471db6cf609724bf57473ff40e22a393aa210b73_2_1380x818.jpeg 2x" data-dominant-color="5D5D73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-02 at 13.03.54</span><span class="informations">1920×1139 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards,</p>
<p>Luca</p>

---

## Post #2 by @lassoan (2024-04-02 12:05 UTC)

<p>As you can see in your screenshot, the name of the node is “Volume rendering ROI”, not “R”.</p>
<p>If you wan to get the list of ROI markups in the scene, you can call:</p>
<pre><code class="lang-auto">roiNodes = getNodesByClass("vtkMRMLMarkupsROINode")
</code></pre>

---

## Post #3 by @LucaB (2024-04-02 12:07 UTC)

<p>Thank you. A silly oversight by me</p>

---
