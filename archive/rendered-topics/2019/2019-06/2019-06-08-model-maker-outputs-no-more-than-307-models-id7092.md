---
topic_id: 7092
title: "Model Maker Outputs No More Than 307 Models"
date: 2019-06-08
url: https://discourse.slicer.org/t/7092
---

# Model maker outputs no more than 307 models

**Topic ID**: 7092
**Date**: 2019-06-08
**URL**: https://discourse.slicer.org/t/model-maker-outputs-no-more-than-307-models/7092

---

## Post #1 by @quakberto (2019-06-08 23:53 UTC)

<p>Hi,</p>
<p>I’ve started to use Slicer as it creates such beautiful 3D renderings!</p>
<p>I stumbled upon the following problem: I’m trying to use ‘model maker’ to create models from a label map. Label making works fine for less than 307 labels, however for some reason above that number it would simply not create new labels. And my map includes 5000 labels…</p>
<p>Oh, I’m using Slicer 4.10.2 on Mac.</p>
<p>Thanks a lot for any help!</p>
<p>Best,<br>
Marvin</p>

---

## Post #2 by @lassoan (2019-06-09 12:25 UTC)

<p>The maximum limit should only be the amount of memory you have, but you may experience slowdowns if you have thousands of labels.</p>
<p>What kind of images do you work with? Do you need each label to be represented by a separate model node? What would you like to achieve?</p>

---

## Post #3 by @quakberto (2019-06-09 12:56 UTC)

<blockquote>
<p>The maximum limit should only be the amount of memory you have, but you may experience slowdowns if you have thousands of labels.</p>
</blockquote>
<p>There’s clearly enough memory available and the model maker reproducibly stops after 307 labels.</p>
<blockquote>
<p>What kind of images do you work with? Do you need each label to be represented by a separate model node? What would you like to achieve?</p>
</blockquote>
<p>I’m working with template images (from fluorescence microscopy) which are segmented into thousands of superpixels (small regions). New samples are registered against the template and probed at the superpixels. My aim with Slicer is to visualise the division into superpixels and show the superpixels in different colors. I could also go for a volumetric rendering, however since I’m dealing with well defined objects, meshes look much nicer.</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2019-06-09 13:08 UTC)

<p>To achieve your goal, you can create a single model node using “Grayscale model maker” module then assign label value to each surface point using “Probe volume with model” module, and set up coloring in Models module’s Scalars section.</p>
<p>We’ll look into why there seems to be a limit in Model maker. Maybe you need to choose a colormap that has more entries.</p>

---

## Post #5 by @quakberto (2019-06-09 13:28 UTC)

<blockquote>
<p>To achieve your goal, you can create a single model node using “Grayscale model maker” module then assign label value to each surface point using “Probe volume with model” module, and set up coloring in Models module’s Scalars section.</p>
</blockquote>
<p>That’s a good idea! I wouldn’t have all the surfaces surrounding all small regions coloured, but just the encompassing one is okay for now.</p>
<blockquote>
<p>We’ll look into why there seems to be a limit in Model maker. Maybe you need to choose a colormap that has more entries.</p>
</blockquote>
<p>When setting the parameters of model maker there’s no colormap yet, is there? Or maybe you mean the one associated to the label map.</p>
<p>Thanks for the help!</p>

---

## Post #6 by @lassoan (2019-06-09 17:43 UTC)

<aside class="quote no-group" data-username="quakberto" data-post="5" data-topic="7092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/q/9e8a1a/48.png" class="avatar"> quakberto:</div>
<blockquote>
<p>maybe you mean the one associated to the label map</p>
</blockquote>
</aside>
<p>Yes, you need to associate a color node with your labelmap volume node that has an entry for each label (or enable “Generate All Models” option).</p>

---
