---
topic_id: 14305
title: "Automate Converting Model To Segmentation"
date: 2020-10-29
url: https://discourse.slicer.org/t/14305
---

# Automate converting model to segmentation

**Topic ID**: 14305
**Date**: 2020-10-29
**URL**: https://discourse.slicer.org/t/automate-converting-model-to-segmentation/14305

---

## Post #1 by @lleewwiiss (2020-10-29 13:27 UTC)

<p>I have a set of MRI dicoms and STL model images, I am wanting to create binary segmentation maps from the models, which i can do fine manually using these steps:</p>
<ul>
<li>
<pre><code>Go to Segmentations module
</code></pre>
</li>
<li>
<pre><code>Create new segmentation node
</code></pre>
</li>
<li>
<pre><code>Change master to Closed surface
</code></pre>
</li>
<li>
<pre><code>In Import/Export section import the model node to the segmentation node
</code></pre>
</li>
<li>
<pre><code>Export visible segments to binary labels map
</code></pre>
</li>
</ul>
<p>But i have a lot of cases i need to do, so was wondering what is the actual code being executed to load in the STL files and convert them to a segmentation map? So i can automate the process</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2020-10-30 04:34 UTC)

<p>See several examples of how to automate these conversions in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations</a></p>

---

## Post #3 by @mohammed_Chekroun (2024-05-21 11:23 UTC)

<p>Did you please find the code for this automation, I tried it with slicer but it’s so slow</p>

---
