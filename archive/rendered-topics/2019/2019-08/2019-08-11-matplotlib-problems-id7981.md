---
topic_id: 7981
title: "Matplotlib Problems"
date: 2019-08-11
url: https://discourse.slicer.org/t/7981
---

# Matplotlib problems

**Topic ID**: 7981
**Date**: 2019-08-11
**URL**: https://discourse.slicer.org/t/matplotlib-problems/7981

---

## Post #1 by @garbulinskamaja (2019-08-11 12:14 UTC)

<p>Hi! I am new to Slicer. I am trying to save a plot by script</p>
<pre><code class="lang-python">plt.scatter(np.arange(1, 20, 1), np.arange(1,20, 1))
plt.savefig(os.path.join(results_path, "plotloss.png"))
</code></pre>
<p>from slicer. The plot has some additional values, I cannot figure out where they come from. When running the same script from Spyder everything works fine.</p>

---

## Post #2 by @pieper (2019-08-11 14:46 UTC)

<p>Can you provide a complete example, ideally with images to show what you mean by additional values?</p>

---

## Post #3 by @lassoan (2019-08-12 02:03 UTC)

<p>After adding the necessary imports, it all worked correctly for me:</p>
<pre><code class="lang-python">pip_install("matplotlib wxPython")

import matplotlib
matplotlib.use('WXAgg')

from matplotlib import pyplot as plt
import numpy as np

plt.scatter(np.arange(1, 20, 1), np.arange(1,20, 1))
plt.savefig("c:/tmp/plotloss.png")
</code></pre>
<p>Produced this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/923dac5c8ccaaa4c83531ae1095c5eb2786fe1a4.png" alt="image" data-base62-sha1="kRHQoxyLxOrQ7pz9lzSJ0pw0us4" width="640" height="480"></p>

---

## Post #4 by @garbulinskamaja (2019-08-12 07:40 UTC)

<p>Interesting. Thank you for your answer. Looks like restarting slicer was the solution. My loss was previously accumulating like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a12c687daa0841c7fe4574c4b3d765298636c2a8.jpeg" data-download-href="/uploads/short-url/mZO12AsSYpmhRnXUikftAo5gWTu.jpeg?dl=1" title="plotexample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a12c687daa0841c7fe4574c4b3d765298636c2a8_2_690x475.jpeg" alt="plotexample" data-base62-sha1="mZO12AsSYpmhRnXUikftAo5gWTu" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a12c687daa0841c7fe4574c4b3d765298636c2a8_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a12c687daa0841c7fe4574c4b3d765298636c2a8_2_1035x712.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a12c687daa0841c7fe4574c4b3d765298636c2a8_2_1380x950.jpeg 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">plotexample</span><span class="informations">1772×1220 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
