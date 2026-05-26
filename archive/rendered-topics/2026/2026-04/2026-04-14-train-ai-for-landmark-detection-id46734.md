---
topic_id: 46734
title: "Train AI for landmark detection"
date: 2026-04-14
url: https://discourse.slicer.org/t/46734
last_bumped: 2026-04-17T18:16:18.186Z
---

# Train AI for landmark detection

**Topic ID**: 46734
**Date**: 2026-04-14
**URL**: https://discourse.slicer.org/t/train-ai-for-landmark-detection/46734

---

## Post #1 by @mau_igna_06 (2026-04-14 18:29 UTC)

<p>Hi,</p>
<p>I’d like to ask here which are community suggestions about selecting an AI model and setting up training data for a medical landmark detection task.</p>
<p>In my use case, I need to detect the superior tip of healthy kidneys on CBCTs. I have a training dataset with around 150 CBCTs with the corresponding landmarks (CBCT on .nrrd files and points in .mrk.json files). I think my training data (i.e. sup kidney tips) could have till a 1cm error. Current training shows 70% accuracy and I don’t expect it to get higher. So I assume the model won’t work after training but that will have to wait a few days (till the training ends)</p>
<p>More information: same use case with same AI model but targeting CTs instead of CBCTs for training, even with halve of training data (e.g. around 70 CTs), had 95% accuracy during training and my tests show it working</p>

---

## Post #2 by @IVarha (2026-04-15 08:12 UTC)

<p>Hello,</p>
<p>could you please elaborate what is in your case accuracy? I am curious because from reading your description you have to use distance metrics instead of accuracy.</p>

---

## Post #3 by @JBeninca (2026-04-16 12:24 UTC)

<p>if the points are paired, you can use the algorithm:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://learnopencv-com.translate.goog/iterative-closest-point-icp-explained/?_x_tr_sl=en&amp;_x_tr_tl=es&amp;_x_tr_hl=es&amp;_x_tr_pto=tc">
  <header class="source">
      <img src="https://learnopencv.com/wp-content/uploads/2017/04/cropped-favicon-512x512-32x32.png" class="site-icon" alt="" width="32" height="32">

      <a href="https://learnopencv-com.translate.goog/iterative-closest-point-icp-explained/?_x_tr_sl=en&amp;_x_tr_tl=es&amp;_x_tr_hl=es&amp;_x_tr_pto=tc" target="_blank" rel="noopener nofollow ugc" title="12:36PM - 30 April 2025">LearnOpenCV – Learn OpenCV, PyTorch, Keras, Tensorflow with code, &amp; tutorials – 30 Apr 25</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:600/338;"><img src="https://learnopencv.com/wp-content/uploads/2025/05/Iterative-Closest-Point-ICP-Explained.gif" class="thumbnail" alt="" width="690" height="388"></div>

<h3><a href="https://learnopencv-com.translate.goog/iterative-closest-point-icp-explained/?_x_tr_sl=en&amp;_x_tr_tl=es&amp;_x_tr_hl=es&amp;_x_tr_pto=tc" target="_blank" rel="noopener nofollow ugc">Iterative Closest Point (ICP) for 3D Explained with Code</a></h3>

  <p>Iterative Closest Point (ICP) explained with code in Python and Open3D which is a widely used classical algorithm for 2D or 3D point cloud registration</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www-sciencedirect-com.translate.goog/topics/engineering/iterative-closest-point-algorithm?_x_tr_sl=en&amp;_x_tr_tl=es&amp;_x_tr_hl=es&amp;_x_tr_pto=tc">
  <header class="source">
      <img src="https://sdfestaticassets-us-east-1.sciencedirectassets.com/shared-assets/103/images/favSD.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://www-sciencedirect-com.translate.goog/topics/engineering/iterative-closest-point-algorithm?_x_tr_sl=en&amp;_x_tr_tl=es&amp;_x_tr_hl=es&amp;_x_tr_pto=tc" target="_blank" rel="noopener nofollow ugc">www-sciencedirect-com.translate.goog</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www-sciencedirect-com.translate.goog/topics/engineering/iterative-closest-point-algorithm?_x_tr_sl=en&amp;_x_tr_tl=es&amp;_x_tr_hl=es&amp;_x_tr_pto=tc" target="_blank" rel="noopener nofollow ugc">Iterative Closest Point Algorithm - an overview | ScienceDirect Topics</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2026-04-17 15:27 UTC)

<p>Kidney detection on CBCT is a hard problem, while on CT it is an easy problem. First of all, the field of view of a CBCT is much smaller (just 20-30cm, so you don’t always see the whole kidney and surroundings), CBCT soft tissue contrast is much worse (mainly due to physics - scattering of the cone beam), and CBCT images are less standardized (voxel values may not correspond accurately to HU). So, the 70% vs 95% accuracy is expected. You may need much more data to get much better results.</p>
<p>What model do you use now?</p>
<p>You can try <a href="https://github.com/MIC-DKFZ/nnLandmark">nnLandmark</a>, an nnU-Net based landmark detection model. Unfortunately, it is not packaged cleanly (they forked and modified nnU-Net), but it should worth a try.</p>

---

## Post #5 by @mau_igna_06 (2026-04-17 17:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="46734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Kidney detection on CBCT is a hard problem, while on CT it is an easy problem.</p>
</blockquote>
</aside>
<p>Yes, I realized this while exploring my datasets and the early results I had.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="46734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may need much more data to get much better results.</p>
</blockquote>
</aside>
<p>Yes, I expect the training loss to be reduced logarithmically by doubling the training data by the experience I have.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="46734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What model do you use now?</p>
</blockquote>
</aside>
<p>I’m using a RL model.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="46734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can try <a href="https://github.com/MIC-DKFZ/nnLandmark" rel="noopener nofollow ugc">nnLandmark</a>, an nnU-Net based landmark detection model.</p>
</blockquote>
</aside>
<p>Yes, I have been researching other models (as well as hyperparameters optimization for the current model I’m using) for this task and I did find nnLandmark suggested.</p>
<p>Thanks a lot for your feedback</p>

---

## Post #6 by @muratmaga (2026-04-17 17:53 UTC)

<p>Are your CBCT’s are as standardized as your CTs?</p>
<p>In my experiments, I found the training for landmark detection being quite sensitive to positional differences. You may want to check whether CBCTs are more variable compared to CT, and if they are try normalizing the difference by registering to a standard orientation (and of course update your landmark coordinates accordingly) and then redo the training. Additionally some CBCTs i have seen  are not normalized for intensities (ie., in 16 bit values exceeding HU values). You might also check  whether your pipeline is doing standardization of intensities.</p>

---

## Post #7 by @mau_igna_06 (2026-04-17 18:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="46734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Are your CBCT’s are as standardized as your CTs?<br>
In my experiments, I found the training for landmark detection being quite sensitive to positional differences.</p>
</blockquote>
</aside>
<p>I’ve tried that. I have tried to be rigorous in the creation and review of the training data pairs (i.e. images and landmarks).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="46734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>You may want to check whether CBCTs are more variable compared to CT</p>
</blockquote>
</aside>
<p>I’ve found that around 5% of the original CBCTs in my dataset are out of distribution (i.e. outliers) and I have just skipped them during training as I don’t expect to be doing inference on such bad quality CBCTs.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="46734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>You might also check whether your pipeline is doing standardization of intensities.</p>
</blockquote>
</aside>
<p>Yes, as far as I remember that is being taken cared of</p>

---
