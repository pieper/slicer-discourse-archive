---
topic_id: 44669
title: "Body Composition Abdominal Muscle Segmentation With Total Se"
date: 2025-10-05
url: https://discourse.slicer.org/t/44669
---

# Body composition - abdominal muscle segmentation with total segmentator

**Topic ID**: 44669
**Date**: 2025-10-05
**URL**: https://discourse.slicer.org/t/body-composition-abdominal-muscle-segmentation-with-total-segmentator/44669

---

## Post #1 by @CS1 (2025-10-05 09:51 UTC)

<p>Heya, I’m currently using total segmentator subtask - tissue 4 type for abdominal muscle segmentation, however I noticed it doesn’t pick up transverse abdominis at all and is not the best at segmentating iliacus. I’ve just been manually painting the TA layer which takes ages, any good suggestions on how to approach this? does everyone else also have the same issue? (But otherwise this is a perfect segmentation subtask!)</p>

---

## Post #2 by @pieper (2025-10-05 19:56 UTC)

<p>You might have better luck with the original model.  If you noticed different results please report back.  It’s not directly integrated with Slicer but it shouldn’t be hard to install and use.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter">
  <header class="source">

      <a href="https://github.com/Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/c95201688e3395ef26e52a85d19ae6dd/Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter" class="thumbnail">

  <h3><a href="https://github.com/Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter" target="_blank" rel="noopener">GitHub - Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter</a></h3>

    <p><span class="github-repo-description">Contribute to Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @CS1 (2025-11-02 13:13 UTC)

<p>Hi Thank you Pieper, I initially was using the original model  but looks like the transverse abdominis layer is also not included, and I found Total segmentator’s “tissue 4 types” subtask gives me better iliacs/psoas segmentation result. is there a model that includes the TA layer?</p>

---

## Post #4 by @pieper (2025-11-02 13:21 UTC)

<p>No, only what’s published is available.  But with modern freely available infrastructure you could train a model with some effort and I’m guessing it would work, although I’ve never tried it with that muscle.  You could use nnInteractive to create training cases and nnU-Net to train a model.  These methods are all well described.</p>

---
