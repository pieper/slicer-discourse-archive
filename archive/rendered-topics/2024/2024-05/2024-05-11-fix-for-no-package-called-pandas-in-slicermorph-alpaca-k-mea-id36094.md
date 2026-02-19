---
topic_id: 36094
title: "Fix For No Package Called Pandas In Slicermorph Alpaca K Mea"
date: 2024-05-11
url: https://discourse.slicer.org/t/36094
---

# Fix for `no package called pandas` in SlicerMorph ALPACA k-means template selection - Apple ARM

**Topic ID**: 36094
**Date**: 2024-05-11
**URL**: https://discourse.slicer.org/t/fix-for-no-package-called-pandas-in-slicermorph-alpaca-k-means-template-selection-apple-arm/36094

---

## Post #1 by @jnations (2024-05-11 18:33 UTC)

<p>Hi community,</p>
<p>I’ve run into a problem with k-means template selection on 2 different mac machines. One is a 2020 MacBook Pro M1, and the second is a 2023 MacBook Pro M3 Max. Working through the tutorial <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MALPACA/K-means_templates_selection.md" rel="noopener nofollow ugc">here</a>, I can run steps 1 &amp; 2, generating the reference point cloud, and generating the point clouds for the rest of my samples that match the reference, without error. Everything looks fine.</p>
<p>When I go to the next step called <code>K-means based template selection</code>, I set my number of templates, my # of iterations, then push the button and nothing happens. Changing the settings doesn’t help. A red stop sign with an error message pops up in the corner. The python console it says:</p>
<p><code> no package called pandas found</code></p>
<p>anaconda is built correctly on both computers, and pandas is installed. Error still received.</p>
<p>I found that following the steps outlined in <a href="https://discourse.slicer.org/t/automatic-install-of-python-packages/7078/4">this discourse post from 2019</a> from <a class="mention" href="/u/pieper">@pieper</a> fixes the problem.</p>
<p>Go to the python terminal in Slicer, then:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import os
&gt;&gt;&gt; os.system('PythonSlicer -m pip install pandas')
0
&gt;&gt;&gt; import pandas
</code></pre>
<p>(This is <a class="mention" href="/u/pieper">@pieper</a> 's work, not mine <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> )</p>
<p>Restart, and everything works like normal! It took me a while to figure out a fix for this. I am hoping that anyone who has this problem will run across this post.</p>
<p>Cheers!</p>

---

## Post #2 by @muratmaga (2024-05-12 02:10 UTC)

<p>This is interesting, thanks for sharing.</p>
<p>ALPACA itself doesn’t use Pandas, but it calls GPA module, which uses. But I thought pandas is bundled with core SlicerPython. So you shouldn’t have to manually install it.</p>
<p>So I am not sure why this is happening. Is this a apple silicon specific issue?</p>

---

## Post #3 by @lassoan (2024-05-12 11:21 UTC)

<p>I don’t think pandas is bundled with Slicer core. Any module that needs it should pip install it.</p>

---

## Post #4 by @jnations (2024-05-12 20:11 UTC)

<blockquote>
<p>Is this a apple silicon specific issue?</p>
</blockquote>
<p>In my experience, k-means template selection and all the other SlicerMorph tools have worked out of the box on Windows machines. I found it interesting that no one else has reported this problem. Maybe the k-means selection isn’t commonly on Macs.</p>
<p>I should report that I’m using 3DSlicer 5.6.2, and I installed SlicerMorph on this machine within the past 2 days. The older M1 machine that had this same issue was using the stable 3DSlicer build from January 2024.</p>

---
