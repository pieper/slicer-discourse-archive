---
topic_id: 44654
title: "Cloning A Composite Transform Yields Incorrect Result"
date: 2025-10-02
url: https://discourse.slicer.org/t/44654
---

# Cloning a composite transform yields incorrect result

**Topic ID**: 44654
**Date**: 2025-10-02
**URL**: https://discourse.slicer.org/t/cloning-a-composite-transform-yields-incorrect-result/44654

---

## Post #1 by @mikebind (2025-10-02 23:40 UTC)

<p>A composite transform node, such as those created by an ANTs QuickSyN registration, is not cloned correctly by the subject hierarchy node.  I am using Slicer 5.8.1 on Windows 11. I have been working on taking apart and reassembling composite transforms and initially thought that my code must have errors somewhere, but I have now reproduced the problems without using any of my code.</p>
<p>Steps to reproduce:</p>
<ol>
<li>Add the following composite transform to the scene: <a href="https://drive.google.com/file/d/1AH9RWsc5dIsRNxah0p4COLteh7VvCZs_/view?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/file/d/1AH9RWsc5dIsRNxah0p4COLteh7VvCZs_/view?usp=drive_link</a></li>
<li>Load the MRHead image volume from SampleData.</li>
<li>Clone the transform (e.g. by right-clicking on it in the subject hierarchy and clicking “Clone”)</li>
<li>Alternately soft-apply the original and the cloned transformation to MRHead. Note the visible shifts in the image distortion in the slice views</li>
</ol>
<p>This particular transform was created using the QuickSyN preset in the “General Registration (ANTs)” module, but it shouldn’t matter how it was created: a cloned MRML node should behave just like the original. I wonder if the problem might arise from the fact that the component transforms of this composite transform are both defined in the inverse (“FromParent”) direction, and maybe something in the cloning isn’t respecting or appreciating that?  It looks like the actual copying in CloneSubjectHierarchyItem is done with a call to CopyContent(), which in turn involves a call to DeepCopyTransform in vtkMRMLTransformNode.cxx.  I would speculate that the problem is here, but I don’t follow the C++ well enough to pinpoint the issue.</p>
<p>I do regard this as a relatively serious bug.  I have never had cause previously to doubt the reliability of cloning a node in Slicer.</p>

---

## Post #2 by @pieper (2025-10-03 15:01 UTC)

<p>It sounds like your guess is correct about where the bug is.  It would help if you could write a small self contained script to reproduce this and file an issue on github.  There’s probably just a small change needed in the mrml code.</p>

---

## Post #3 by @mikebind (2025-10-03 18:55 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="44654">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Alternately soft-apply the original and the cloned transformation to MRHead. Note the visible shifts in the image distortion in the slice views</p>
</blockquote>
</aside>
<p>Issue reported here: <a href="https://github.com/Slicer/Slicer/issues/8766" rel="noopener nofollow ugc">Cloning a composite transform yields incorrect result · Issue #8766 · Slicer/Slicer</a></p>

---

## Post #4 by @muratmaga (2025-10-04 02:41 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="44654">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I wonder if the problem might arise from the fact that the component transforms of this composite transform are both defined in the inverse (“FromParent”) direction, and maybe something in the cloning isn’t respecting or appreciating that? It</p>
</blockquote>
</aside>
<p>That’s probably the case. Looks like the order of linear and grid transforms are swapped in cloned and original one. Transforms are exactly the same, but the order is not preserved during the cloning for some reason.</p>
<pre><code class="lang-auto">Transform 1: Displacement field:
  Grid size: 256 256 160
  Grid origin: -73.532 179.936 144.715
  Grid spacing: 0.976562 0.976562 1
  Grid orientation:
    -0.018713  -0.00334281  0.999819
    -0.992177  -0.123387  -0.0189825
    0.123428  -0.992353  -0.00100772
Transform 2: Linear
    1.00532  -0.0569842  0.0847543  -2.886
    0.0525922  0.98656  -0.067834  -13.2129
    -0.0846486  0.0587005  0.992948  -39.5675
    0  0  0  1
</code></pre>
<p>cloned:</p>
<pre><code class="lang-auto">Transform 1: Linear
    1.00532  -0.0569842  0.0847543  -2.886
    0.0525922  0.98656  -0.067834  -13.2129
    -0.0846486  0.0587005  0.992948  -39.5675
    0  0  0  1
Transform 2: Displacement field:
  Grid size: 256 256 160
  Grid origin: -73.532 179.936 144.715
  Grid spacing: 0.976562 0.976562 1
  Grid orientation:
    -0.018713  -0.00334281  0.999819
    -0.992177  -0.123387  -0.0189825
    0.123428  -0.992353  -0.00100772
</code></pre>

---

## Post #5 by @mikebind (2025-10-06 17:05 UTC)

<p>This is now fixed here: <a href="https://github.com/Slicer/Slicer/pull/8768" rel="noopener nofollow ugc">BUG: Fixed cloning of composite transforms by lassoan · Pull Request #8768 · Slicer/Slicer</a><br>
Thanks for the quick response and fix!</p>

---

## Post #6 by @mikebind (2025-10-06 17:08 UTC)

<p>Thanks, that’s what it looked like, but I was hoping that someone would be able to look at the C++ code and fix it so it worked appropriately in all cases.  In this case, it was reversed, but I wasn’t sure if there were other cases where reversing the order would not be the right thing to do. It seems like Andras took a look and was able to fix it, hopefully in a general way.</p>

---

## Post #7 by @lassoan (2025-10-14 03:03 UTC)

<p>Yes, the problem is fixed, not just in a special case but in general: cloning of composite transforms should work well now.</p>

---
