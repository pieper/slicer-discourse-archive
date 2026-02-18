# Monai label. CUDA out of memory

**Topic ID**: 26161
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/monai-label-cuda-out-of-memory/26161

---

## Post #1 by @dalv.silvermann (2022-11-09 15:03 UTC)

<p>I have a question about Monai Label. Maybe somebody has faced the similar problem.</p>
<ol>
<li>
<p>I use deepedit from radiology app without any global code changes on my tower-server with Asus Nvidia GeForce RTX 3080 10GiB.<br>
I try to start the inference with the batch size equal to 1.<br>
Input tensor is 512x512 with 512 images.<br>
But I’m stuck in the “CUDA out of memory” error.<br>
See IMG_5625.jpeg in the link from Google drive:<br>
<a href="https://drive.google.com/file/d/1RTsWL3fqNomNdGNPk26MFjel2-8Csasb/view?usp=share_link" rel="noopener nofollow ugc">IMG_5625.jpeg - Google Drive</a><br>
See output_cuda_out_of_memory.txt in the link from Google drive:<br>
<a href="https://drive.google.com/file/d/1RIvTuq3bmQ5uLgvuVD775lB_Utg6XoWL/view?usp=share_link" rel="noopener nofollow ugc">output_cuda_out_of_memory.txt - Google Drive</a></p>
</li>
<li>
<p>By the way, if I will uncomment line <span class="hashtag">#275</span> it will work on CPU successfully.<br>
See IMG_5623.PNG in the link from Google drive:<br>
<a href="https://drive.google.com/file/d/1roQDP4pL4S8VXZYQe6j7i_5w7ih-BSl2/view?usp=share_link" rel="noopener nofollow ugc">IMG_5623.PNG - Google Drive</a></p>
</li>
</ol>
<p>a) Is it real to work with Monai Label on Asus Nvidia GeForce RTX 3080 10GiB?<br>
b) Maybe it possible to make some changes in code somewhere that will help Monai to distribute the computation load im my GPU memory and do this job with it, instead of CPU?<br>
<img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji only-emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Kind regards,<br>
Dalv Silvermann.</p>

---

## Post #2 by @rbumm (2022-11-09 15:53 UTC)

<p>Hi Dalv,</p>
<p>you should be able to run MONAILabel deepedit inference in GPU mode with the system settings you specified.</p>
<p>Please look for the following file and line in your local MONAILabel installation:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/blob/5a076c8a08ce18244681f1b0a748db4f8807da4a/sample-apps/radiology/lib/infers/deepedit.py#L52">
  <header class="source">

      <a href="https://github.com/Project-MONAI/MONAILabel/blob/5a076c8a08ce18244681f1b0a748db4f8807da4a/sample-apps/radiology/lib/infers/deepedit.py#L52" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Project-MONAI/MONAILabel/blob/5a076c8a08ce18244681f1b0a748db4f8807da4a/sample-apps/radiology/lib/infers/deepedit.py#L52" target="_blank" rel="noopener">Project-MONAI/MONAILabel/blob/5a076c8a08ce18244681f1b0a748db4f8807da4a/sample-apps/radiology/lib/infers/deepedit.py#L52</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="42" style="counter-reset: li-counter 41 ;">
          <li>dataset.</li>
          <li>"""</li>
          <li>
          </li>
<li>def __init__(</li>
          <li>    self,</li>
          <li>    path,</li>
          <li>    network=None,</li>
          <li>    type=InferType.DEEPEDIT,</li>
          <li>    labels=None,</li>
          <li>    dimension=3,</li>
          <li class="selected">    spatial_size=(128, 128, 64),</li>
          <li>    target_spacing=(1.0, 1.0, 1.0),</li>
          <li>    number_intensity_ch=1,</li>
          <li>    description="A DeepEdit model for volumetric (3D) segmentation over 3D Images",</li>
          <li>    **kwargs,</li>
          <li>):</li>
          <li>    super().__init__(</li>
          <li>        path=path,</li>
          <li>        network=network,</li>
          <li>        type=type,</li>
          <li>        labels=labels,</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Try to set the spatial size lower to avoid memory errors, maybe starting with</p>
<pre><code class="lang-auto">spatial_size=(32, 32, 0),
</code></pre>
<p>Hope that helps</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>

---

## Post #3 by @diazandr3s (2022-11-09 16:41 UTC)

<p>Hi <a class="mention" href="/u/dalv.silvermann">@dalv.silvermann</a>,</p>
<p>Thanks for reporting this.</p>
<p>I’ve checked the logs and saw that the image size is (550, 550, 450) - quite a big image for the GPU you have.</p>
<p>DeepEdit model uses the whole image to train and perform inference and that’s why it needs more GPU memory than other models.</p>
<p>As <a class="mention" href="/u/rbumm">@rbumm</a> recommended, you could reduce the image size <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L77" rel="noopener nofollow ugc">here</a>. But in that case you won’t be able to use the pretrained model as the input size changes - you should re train the model.</p>
<p>Otherwise, I’d recommend you use the segmentation model instead, which works on patches: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#segmentation" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/radiology at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Hope that helps,</p>

---

## Post #4 by @mangotee (2022-11-09 16:57 UTC)

<p>Hi all,<br>
interesting thread, huge images indeed! However, from the logs it seems that the image already gets downsampled to (1,128,128,128), but that might still be too large for backprop. I would try (96,96,96) first, and if that’s still too large, maybe (80,80,80), or worst case (64,64,64) should work (but at that point you’d probably notice considerable staircase artifacts in the prediction).<br>
To work at a higher resolution, it is probably best to work with the segmentation model, as <a class="mention" href="/u/diazandr3s">@diazandr3s</a> recommended. In that case you can set your patch size to e.g. (96,96,96) (whatever fits into GPU VRAM), and play around with the <code>target_spacing</code> parameter (<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L76-L77" rel="noopener nofollow ugc">here</a>) to make sure that you get a good compromise between resolution and FOV of the patches.<br>
Good luck!</p>

---

## Post #5 by @muratmaga (2022-11-09 19:27 UTC)

<aside class="quote no-group" data-username="mangotee" data-post="4" data-topic="26161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>interesting thread, huge images indeed! However, from the logs it seems that the image already gets downsampled to (1,128,128,128), but that might still be too large for backprop. I would try (96,96,96) first, and if that’s still too large, maybe (80,80,80), or worst case (64,64,64) should work (but at that point you’d probably notice considerable staircase artifacts in the prediction).</p>
</blockquote>
</aside>
<p>As I recall, number of labels also factor in the memory usage. So if you have a multi-labeled image your memory usage will be higher than a model that uses a single label.</p>

---

## Post #6 by @dalv.silvermann (2022-12-08 12:05 UTC)

<p>Sorry for taking so long for reply.</p>
<ol>
<li>Now we use (64,64,64) and it still goes “Out of Memory”.</li>
<li>Now I’m thinking about the second GPU for example Msi GeForce RTX 3090 Ventus 3x 24G OC.<br>
And then we will have GPU0 and GPU1 with 34G in total. What do you think about this way?</li>
<li>Does anybody works with Monai with more than one GPU with computation distribution? How we can configure this scheme?<br>
Do you have some links for examples?</li>
</ol>
<p>Thanks for all of you for support!</p>

---

## Post #7 by @muratmaga (2022-12-08 17:13 UTC)

<p>There are tweaks you can do, one of which I think is to reduce the precision of floating points so you double memory, but the reality is the Nvidia is knowingly keeping the geforce line of gpus with insufficient memory for them not to compete in this domain (ML). You will make yourself a favor if you can move to something like RTX A6000 which provides double memory at 48GB.</p>
<p>I do not know about distributed workload, but I suspect if your model doesn’t fit in the memory of one gpu, it won’t work. I dont think they “pool” the memory.</p>

---
