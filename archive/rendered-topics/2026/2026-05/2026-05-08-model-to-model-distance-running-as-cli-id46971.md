---
topic_id: 46971
title: "Model To Model Distance running as CLI"
date: 2026-05-08
url: https://discourse.slicer.org/t/46971
last_bumped: 2026-05-11T13:27:52.090Z
---

# Model To Model Distance running as CLI

**Topic ID**: 46971
**Date**: 2026-05-08
**URL**: https://discourse.slicer.org/t/model-to-model-distance-running-as-cli/46971

---

## Post #1 by @Mrdlev (2026-05-08 13:09 UTC)

<p>Hi everyone,</p>
<p>I’m trying to use the <strong>Model-to-Model Distance</strong> extension in 3D Slicer to quantify the <strong>average displacement between two structures</strong> (one with deformation and one without).</p>
<p>However, I’ve run into an issue:</p>
<ul>
<li>
<p>I’ve installed the extension multiple times and restarted Slicer each time</p>
</li>
<li>
<p>The module does not appear to function correctly in the GUI</p>
</li>
<li>
<p>The only way I can access it is via the CLI</p>
</li>
</ul>
<p>The problem is that running it through the CLI does not provide the specific output I need, particularly the <strong>average displacement metric</strong> between the models.</p>
<p>Has anyone encountered a similar issue or knows:</p>
<ol>
<li>
<p>How to properly enable/use the extension through the GUI?</p>
</li>
<li>
<p>How to retrieve average displacement (or equivalent statistics) using this tool or an alternative workflow?</p>
</li>
</ol>
<p>Any guidance would be greatly appreciated.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @ebrahim (2026-05-11 13:27 UTC)

<aside class="quote no-group" data-username="Mrdlev" data-post="1" data-topic="46971">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7ab992/48.png" class="avatar"> Mrdlev:</div>
<blockquote>
<p>The module does not appear to function correctly in the GUI</p>
</blockquote>
</aside>
<p>Can you elaborate? In what way does it not function correctly?</p>
<p>I hope the below AI generated response is helpful; I have verified the snippets work.</p>
<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post contains AI-generated content.</p>
</blockquote>
<p>ModelToModelDistance is a <strong>CLI module</strong>, so it does not have a custom GUI. In Slicer, its “GUI” is the automatically generated CLI module panel. After installing the extension and restarting Slicer, search for:</p>
<p><code>Model To Model Distance</code></p>
<p>or look under the <strong>Quantification</strong> category.</p>
<p>The module does not print an average distance as a CLI return value. Instead, it writes distance arrays into the <strong>output model’s point data</strong>. You can then compute the average from those arrays in the Python console.</p>
<p>First, inspect the available arrays:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = slicer.util.getNode("VTK Output File")  # use your output model name

pointData = modelNode.GetPolyData().GetPointData()
for i in range(pointData.GetNumberOfArrays()):
    print(i, pointData.GetArrayName(i))
</code></pre>
<p>The array name depends on the selected distance mode.</p>
<p>For <code>corresponding_point_to_point</code>, use:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np

distances = slicer.util.arrayFromModelPointData(
    modelNode, "AbsolutePointToPointDistance"
)

print("mean displacement:", np.mean(distances))
print("std:", np.std(distances))
print("min:", np.min(distances))
print("max:", np.max(distances))
print("median:", np.median(distances))
print("95th percentile:", np.percentile(distances, 95))
</code></pre>
<p>Or compute the magnitude from the displacement vectors:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np

vectors = slicer.util.arrayFromModelPointData(modelNode, "PointToPointVector")
magnitudes = np.linalg.norm(vectors, axis=1)

print("mean displacement:", np.mean(magnitudes))
</code></pre>
<p>For <code>absolute_closest_point</code>, use:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np

distances = slicer.util.arrayFromModelPointData(modelNode, "Absolute")
print("mean closest-point distance:", np.mean(distances))
</code></pre>
<p>For <code>signed_closest_point</code>, use:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np

distances = slicer.util.arrayFromModelPointData(modelNode, "Signed")
print("mean signed closest-point distance:", np.mean(distances))
</code></pre>
<p>One caveat: if the option <strong>Save target name in distance fields</strong> / <code>--targetInFields</code> is enabled, the array name gets a suffix based on the target filename, for example:</p>
<pre data-code-wrap="python"><code class="lang-python">Absolute_to_targetModelName
Signed_to_targetModelName
</code></pre>
<p>That is why it is best to print the point-data array names first.</p>
<p>Also, be careful about the interpretation. If the two models have matching point order, <code>corresponding_point_to_point</code> gives a true pointwise displacement. If they do not have corresponding points, use closest-point distance, but that is a surface-to-surface distance, not necessarily a physical displacement vector.</p>

---
