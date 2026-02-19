---
topic_id: 29914
title: "Monailabel Cuda Out Of Memory With Bundle"
date: 2023-06-08
url: https://discourse.slicer.org/t/29914
---

# MonaiLabel CUDA out of memory with Bundle

**Topic ID**: 29914
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/monailabel-cuda-out-of-memory-with-bundle/29914

---

## Post #1 by @FloCo (2023-06-08 10:09 UTC)

<p>Hello everyone,</p>
<p>I am working with Slicer to do machine learning using MonaiLabel, the annotation and learning part work perfectly, it’s really nice tool !<br>
Unfortunately I have troubles when I run the automatic segmentation with medium and big CT scan (starting from around 256<em>256</em>256 pixels I would say).<br>
I got an error message :<br>
“torch.cuda. OutfMemoryError: CUDA out of memory. Tried to allocate 7.28 GiB (GPU 0; 23.65 GiB total capacity; 12.28 GiB already allocated; 2.67 GiB free; 19.48 GiB reserved in total by PyTorch”</p>
<p>I have a NVIDIA GeForce RTX 4090: 24GB memory, and I am using MonaiLabel -Zoo/Bundle (0.7.0rc6), note that I have tried other versions of Bundles with same result but if I use Radiology application it works well.</p>
<p>Since the training is working perfectly and since I have 24GB, I would have thought that it would be ok for CT scan of medium sizes.</p>
<p>Do you have any ideas if I do something wrong about the memory ?</p>
<p>Thank you for your help<br>
Florian COTTE</p>

---

## Post #2 by @ylcnkzy (2023-06-09 06:47 UTC)

<p>Hi Florian,<br>
Have you checked if you have the recent version of Cuda (or at least the cuda version you have supports RTX 4090)?</p>
<p>It is better to check it <a href="https://docs.nvidia.com/deploy/cuda-compatibility/" rel="noopener nofollow ugc">here</a></p>
<p>Best</p>

---

## Post #3 by @FloCo (2023-06-09 10:22 UTC)

<p>Hi ylcnkzy,</p>
<p>I have cuda version 11.8 and from what I have found on internet it seems that it supports well RTX4090.<br>
I can try to see if it’s a problem with the driver, I’ll look into that.</p>
<p>Best,</p>

---

## Post #4 by @rbumm (2023-06-09 11:11 UTC)

<p>Can <a class="mention" href="/u/diazandr3s">@diazandr3s</a> weigh in? Would also be curious about the boundaries.</p>

---

## Post #5 by @diazandr3s (2023-06-10 03:17 UTC)

<p>Thanks for the ping <a class="mention" href="/u/rbumm">@rbumm</a>.</p>
<p><a class="mention" href="/u/floco">@FloCo</a> which model are you using to run inference?</p>
<p>Here is the GPU memory usage for the two available models (1.5mm and 3mm): <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation#gpu-consumption-warning" class="inline-onebox" rel="noopener nofollow ugc">model-zoo/models/wholeBody_ct_segmentation at dev · Project-MONAI/model-zoo · GitHub</a></p>

---

## Post #6 by @FloCo (2023-06-10 05:10 UTC)

<p>Thank you for your response <a class="mention" href="/u/diazandr3s">@diazandr3s</a> , indeed I didn’t see this page on memory usage.<br>
I looked into totalsegmentator ressources and it was much less, it’s not the same model ?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/wasserth/TotalSegmentator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/wasserth/TotalSegmentator" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/bac40aee5327f852a51fdec710681ab3934639e8391b89f49ec430e0405989ca/wasserth/TotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/wasserth/TotalSegmentator" target="_blank" rel="noopener nofollow ugc">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104...</a></h3>

  <p>Tool for robust segmentation of 104 important anatomical structures in CT images - GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104 important anatomical structures in CT images</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I am using the model with 1.5mm so everything is normal then.</p>
<p>I have 2 GPUs 4090 of 24GB, is there a way a using both for inference and doing like one of 48GB ?</p>
<p>Thank you</p>

---

## Post #7 by @rbumm (2023-06-10 05:49 UTC)

<p>No, it is not the same model, but wholeBody_ct_segmentation was trained using TotalSegmentator data.</p>

---

## Post #8 by @FloCo (2023-06-10 06:16 UTC)

<p>Oh I see ! My mistake then .<br>
And about the fact that I have two GPUs ? I guess I can’t “merge” them but I want to be sure  I am not missing something simple to do ?</p>
<p>Thank you</p>

---

## Post #9 by @rbumm (2023-06-10 09:09 UTC)

<p>It seems to be possible to use two GPUs, although I never tried this, <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1400">see here</a>. The question is whether it has any impact on the CUDA Out of memory error. You could probably add a MONAILabel issue on GitHub or comment in the thread above.</p>

---

## Post #10 by @curtislisle (2023-06-10 14:11 UTC)

<p>There is complexity here, and I am not expert, but in my experience, pytorch DNN models can be configured to use two GPUs instead of one. I assume many MONAI models take advantage of this. Use of two GPUs generally divides memory requirements in half. In the link Rudolf posted, it shows how to set the available devices to include 0 and 1. This is necessary. It might be the configuration of MONAILabel does this for us. I could test on a two GPU server in two weeks if we don’t have an answer earlier.</p>

---

## Post #11 by @curtislisle (2023-06-10 16:44 UTC)

<p>After thinking about this. Using two GPUs halves memory only if the batch size for training or inferencing is greater than 1.  From the MONAILabel GitHub page, it looks like the 1.5mm totalsegmentator model requires more than 24G memory for some volumes. You<br>
Might split your volume into two sets of slices and separately segment each half then combine the segmentations.  You would want to examine the boundary to look for discontinuities.</p>
<p>Combining the memory of two GPUs into one has been done by NVIDIA but requires custom work.  Hope this helps.</p>

---

## Post #12 by @FloCo (2023-06-11 14:25 UTC)

<p>I was thinking about splitting dicom images in two but I am not very confident about the continuity, I can try this and see how it goes.</p>
<p>About merging merging memory of GPUs, it sounds that it would solve the problem on my case, I am not an expert so it might be too difficult for me but I’ll follow this idea too thank you !</p>

---

## Post #13 by @xiang_yao (2024-08-01 02:29 UTC)

<p>Can multi GPU inference be used on Windows or Linux systems? Currently, due to data size issues, it is evident that monailabel infers data in memory (i.e. CPU) without utilizing CUDA acceleration.</p>
<p>If I have multiple 4090 cards on a computer, how can I involve them in parallel computing for inference?</p>
<p>Have you solved the problem of merging the memory of two graphics cards mentioned above?</p>

---

## Post #14 by @ece (2024-08-01 02:50 UTC)

<p>Hello, have you solved this GPUs problem?<br>
I am also unable to GPUs inference Thanks for your help</p>

---

## Post #15 by @curtislisle (2024-08-01 03:31 UTC)

<p>It has been a while since I used MONAILabel, but if it uses CPU only and not GPU on your system, it might be that you have the cpu version of torch installed instead of the GPU equipped version of torch.  Or the Nvidia drivers are not installed correctly.</p>
<p>Whether a model uses multiple GPUs is generally controlled by how the inferencing python code is written, so you would need to look at the way the inferencing is performed inside the MONAILabel server to see if it is written for multi GPU.  In my limited experience, it is often possible to change the code of a PyTorch model to inference across multi GPUs on a single system.</p>
<p>Multi-GPU works on Linux systems when the Nvidia drivers and torch-gpu versions are installed correctly.  I have not personally tested multi-GPU on windows, but I assume it works as well.</p>
<p>Finally, deep learning, especially on 3D volumes, can be very memory intensive, whether it is run on CPU or GPU.  Even with a GPU, the system memory must still be large enough to hold the data being written or read from the GPU.  With small memory, it  may help to down sample the volume or segment several smaller ROIs and then combine the segmentations back together later.</p>

---

## Post #17 by @ece (2024-08-01 04:52 UTC)

<p>Hello, thank you for your reply. I use a Linux system. I’m using Nvidia drivers and a torch-gpu. I want to use multi-GPU inference. I saw that you mentioned that multiple Gpus work in Linux, how to modify the implementation of thank you for your reply</p>

---
