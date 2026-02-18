# Set displayNode color to Inferno

**Topic ID**: 29434
**Date**: 2023-05-12
**URL**: https://discourse.slicer.org/t/set-displaynode-color-to-inferno/29434

---

## Post #1 by @asyeda (2023-05-12 21:17 UTC)

<p>I’m trying to use:</p>
<p><code>displayNode.SetAndObserveColorNodeID(f'vtkMRMLColorTableNode{colorName}')</code></p>
<p>which works for some of the lookup table colors, but it does not work for Inferno. How can I make this work, i.e. setting the color for the display node to Inferno? I’m new to Slicer module development so any guidance would be appreciated!</p>

---

## Post #2 by @lassoan (2023-05-13 02:24 UTC)

<p>You can see the color node IDs in Data module in the last tab. Enable display of hidden nodes and node IDs.</p>
<p>Or you can run this in the Python console:</p>
<pre><code>print(getNode('*Inferno*').GetID())
</code></pre>

---

## Post #3 by @asyeda (2023-05-15 02:58 UTC)

<p>Thank you, this really helped!</p>

---
