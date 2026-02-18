# Is there a better AI tool than totalsegmentator for pulmonary vessel segmentation?

**Topic ID**: 41042
**Date**: 2025-01-11
**URL**: https://discourse.slicer.org/t/is-there-a-better-ai-tool-than-totalsegmentator-for-pulmonary-vessel-segmentation/41042

---

## Post #1 by @Dobmod (2025-01-11 20:48 UTC)

<p>It’s widely known that TotalSegmentator performs poorly on pulmonary vessels. Does anyone konow better AI tools? I have made some good datasets, but the training results of nnUNet are always unsatisfactory. Thanks</p>

---

## Post #2 by @mau_igna_06 (2025-01-12 01:10 UTC)

<p>Please try with MONAI Auto3DSeg</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Project-MONAI/tutorials/blob/main/auto3dseg/README.md">
  <header class="source">

      <a href="https://github.com/Project-MONAI/tutorials/blob/main/auto3dseg/README.md" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Project-MONAI/tutorials/blob/main/auto3dseg/README.md" target="_blank" rel="noopener nofollow ugc">Project-MONAI/tutorials/blob/main/auto3dseg/README.md</a></h4>


      <pre><code class="lang-md">&lt;h1 align="center"&gt; Auto3DSeg &lt;/h1&gt;

&lt;div align="center"&gt; &lt;img src="figures/workflow_v1.png" width="800"/&gt; &lt;/div&gt;

## Introduction

**Auto3DSeg** is a comprehensive solution for large-scale 3D medical image segmentation. It leverages the latest advances in **MONAI** and GPUs to efficiently develop and deploy algorithms with state-of-the-art performance for beginners or advanced researchers in the field. 3D medical image segmentation is an important task with great potential for clinical understanding, disease diagnosis, and surgical planning. According to the statistics of the recent [MICCAI](http://www.miccai.org/) conferences, more than 60% of the papers are applications of segmentation algorithms, and more than half of them use 3D datasets. After working in this field for many years, we have released the state-of-the-art segmentation solution **Auto3DSeg**, which requires minimal user input (e.g., data root and list).

**Auto3DSeg** first analyzes the global information such as intensity, data size, and data spacing of the dataset, and then generates algorithm folders in MONAI bundle format based on data statistics and algorithm templates. Next, all algorithms initiate model training to obtain checkpoints with the best validation accuracy. Finally, the ensemble module selects the algorithms via ranking trained checkpoints and creates ensemble predictions. Meanwhile, the solution offers different levels of user experience for beginners and advanced researchers. It has been tested on large-scale 3D medical imaging datasets in several different modalities.

&lt;details open&gt;
&lt;summary&gt;Major features&lt;/summary&gt;

- **Unified Framework**

  **Auto3DSeg** is a self-contained solution for 3D medical image segmentation with minimal user input.

- **Flexible Modular Design**

  **Auto3DSeg** components can be used independently to meet different needs of users.
</code></pre>



  This file has been truncated. <a href="https://github.com/Project-MONAI/tutorials/blob/main/auto3dseg/README.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Let us know how it goes <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
