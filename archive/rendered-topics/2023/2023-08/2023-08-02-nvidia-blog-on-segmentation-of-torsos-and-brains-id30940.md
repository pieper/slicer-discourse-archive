---
topic_id: 30940
title: "Nvidia Blog On Segmentation Of Torsos And Brains"
date: 2023-08-02
url: https://discourse.slicer.org/t/30940
---

# Nvidia blog on segmentation of torsos and brains

**Topic ID**: 30940
**Date**: 2023-08-02
**URL**: https://discourse.slicer.org/t/nvidia-blog-on-segmentation-of-torsos-and-brains/30940

---

## Post #1 by @pieper (2023-08-02 19:23 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://developer.nvidia.com/blog/visual-foundation-models-for-medical-image-analysis/?ncid=em-news-567375&amp;mkt_tok=MTU2LU9GTi03NDIAAAGNUM4mLq1GZezP086CyGsOkwkpr2KMgqH0lo0_b6E38F0ZJiKRcMBZD6ZTTyjF4MyNhqohQn10EXQmSe2ZL_O_DYh1GxRsnwvwXyrM-OEwmwbznRWjZg">
  <header class="source">
      <img src="https://developer-blogs.nvidia.com/wp-content/themes/nvidia/dist/images/favicon_300a1064.ico" class="site-icon" width="48" height="48">

      <a href="https://developer.nvidia.com/blog/visual-foundation-models-for-medical-image-analysis/?ncid=em-news-567375&amp;mkt_tok=MTU2LU9GTi03NDIAAAGNUM4mLq1GZezP086CyGsOkwkpr2KMgqH0lo0_b6E38F0ZJiKRcMBZD6ZTTyjF4MyNhqohQn10EXQmSe2ZL_O_DYh1GxRsnwvwXyrM-OEwmwbznRWjZg" target="_blank" rel="noopener" title="04:00PM - 20 June 2023">NVIDIA Technical Blog – 20 Jun 23</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/388;"><img src="https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/MONAI-3D-Torso-1600x900-1.jpg" class="thumbnail" width="690" height="388"></div>

<h3><a href="https://developer.nvidia.com/blog/visual-foundation-models-for-medical-image-analysis/?ncid=em-news-567375&amp;mkt_tok=MTU2LU9GTi03NDIAAAGNUM4mLq1GZezP086CyGsOkwkpr2KMgqH0lo0_b6E38F0ZJiKRcMBZD6ZTTyjF4MyNhqohQn10EXQmSe2ZL_O_DYh1GxRsnwvwXyrM-OEwmwbznRWjZg" target="_blank" rel="noopener">Visual Foundation Models for Medical Image Analysis | NVIDIA Technical Blog</a></h3>

  <p>The analysis of 3D medical images is crucial for advancing clinical responses, disease tracking, and overall patient survival. Deep learning models form the backbone of modern 3D medical…</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @rbumm (2023-08-03 05:24 UTC)

<p>If anybody is interested <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/MONAIBundleIntegrationTutorial/">how to use MONAI bundle to integrate models from MONAI model ZOO</a></p>

---

## Post #3 by @evaherbst (2023-08-03 07:28 UTC)

<p>Thank you very much for sharing this!<br>
Do you know if anyone has done any head to head comparisons of TotalSegmentator vs the Monai complete body segmentation trained with the TotalSegmentator annotated dataset?</p>
<p>I will do some tests soon too.</p>
<p>Thanks,<br>
Eva</p>

---

## Post #4 by @rbumm (2023-08-03 09:36 UTC)

<p>No, Eva, not aware of this, I only know that the Monai complete body segmentation has been trained using the TotalSegmentator training dataset. But it would be interesting to see a comparison in segmentation quality,  segmentation time, and necessary hardware requirements.</p>

---

## Post #5 by @lassoan (2023-08-03 12:09 UTC)

<p>As far as I know they have very similar output, but MONAILabel’s model is slower and requires more memory. You could probably optimize the model to reduce its resource needs and computation time.</p>
<p>TotalSegmentator model quality will be further improved and more segments and body parts will be added. I don’t know if there is any plan or capacity of the MONAILabel team to further improve their model - keep improving the training data and retraining the model while keeping it fast, robust, and accurate would be a full-time job for someone.</p>

---

## Post #6 by @evaherbst (2023-08-07 16:07 UTC)

<p>Thank you so much Andras for this information, it is very helpful.</p>

---
