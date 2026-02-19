---
topic_id: 36797
title: "Measures Of The Model Change After I Run Gpa Pca"
date: 2024-06-15
url: https://discourse.slicer.org/t/36797
---

# Measures of the model change after I run GPA+PCA

**Topic ID**: 36797
**Date**: 2024-06-15
**URL**: https://discourse.slicer.org/t/measures-of-the-model-change-after-i-run-gpa-pca/36797

---

## Post #1 by @Dani98 (2024-06-15 03:37 UTC)

<p>I have a problem with the module GPA+PCA<br>
I have to create a statistical model but when I run the module GPA+CPA the measures of my models change and in particular there is a reduction of these measures<br>
I don’t understand the reason because before the running of GPA+PCA the measures are correct…what can I do?<br>
Thank you!</p>

---

## Post #2 by @muratmaga (2024-06-15 03:53 UTC)

<aside class="quote no-group" data-username="Dani98" data-post="1" data-topic="36797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dani98/48/67536_2.png" class="avatar"> Dani98:</div>
<blockquote>
<p>the measures of my models change and in particular there is a reduction of these measures</p>
</blockquote>
</aside>
<p>By measures do you mean the scale of the landmarks change? That’s expected because Generalized Procrustes Analysis (GPA) requires the coordinates to be scaled by centroid size. If you want to preserve the scale of your data, make sure to check the “Enable Boas Coordinates” option before executing the GPA.</p>
<p>This will still conduct the GPA alignment in unit coordinates, but put the scale back after the superimposition is completed. Your PCA decomposition will then be conducted on properly scaled data.</p>

---

## Post #3 by @Dani98 (2024-06-15 08:57 UTC)

<p>Thank you very much!<br>
I have another question…I created a cut plane through the module “reformat” and I cut my model in the section “models” by using clipping<br>
But now after the cut, I do not know how to remove the plane as it remains visible…how can I do this?</p>

---

## Post #4 by @muratmaga (2024-06-15 15:30 UTC)

<p>You can control the visibility of the Markups (planes, ROIs, points, lines etc) by turning off/on the eye icon in the Data or Markups modules.</p>

---
