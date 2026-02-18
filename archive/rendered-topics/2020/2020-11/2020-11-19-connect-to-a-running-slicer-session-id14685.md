# Connect to a running Slicer session

**Topic ID**: 14685
**Date**: 2020-11-19
**URL**: https://discourse.slicer.org/t/connect-to-a-running-slicer-session/14685

---

## Post #1 by @pll_llq (2020-11-19 12:19 UTC)

<p>Is there a way to connect to a running Slicer session from a standalone script?</p>
<pre><code class="lang-auto">Given I have Slicer open
And I have an image open in Slicer
And I have a python script resting on my desktop
When I execute the python script
Then the script connects to the running slicer
And performs a python action on the opened image
And I see the result on the Slicer screen
</code></pre>
<p>But I didn’t use Slicers python interpreter nor I passed the script to slicer as a parameter during launch</p>

---

## Post #2 by @pll_llq (2020-11-19 12:48 UTC)

<p>After a bit more research I guess this is not how slicer or python works.</p>

---
