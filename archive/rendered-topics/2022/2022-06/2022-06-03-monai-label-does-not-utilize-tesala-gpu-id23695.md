# MONAI label does not utilize Tesala GPU

**Topic ID**: 23695
**Date**: 2022-06-03
**URL**: https://discourse.slicer.org/t/monai-label-does-not-utilize-tesala-gpu/23695

---

## Post #1 by @Ron (2022-06-03 20:39 UTC)

<p>I have been working with Andres to train a MONAI label spine segmentation on a windows 10 pro workstation (Lenovo p610, 64 core CPU AMD Threadripper pro, Nvidia Tesla V100, Quadro 1000 GPU, 256Gb Ram).  We have tried several times to run the model, and although it runs and trains, it appears to run on the CPU only.  Running Nvidia SMI recognizes both GPUs. I have installed the server driver version of the Tesla card (V100).  I wonder if anyone had the same issue/found a solution.<br>
Thanks, Ron</p>

---

## Post #2 by @muratmaga (2022-06-04 02:07 UTC)

<p>In my experience, this is almost always due to incorrect CUDA installation and/or insufficient environmental variable settings. Nvidia-smi can only confirm that the Nvidia driver is installed correctly and that GPU is operational. CUDA set up is different.<br>
First you have to confirm that:</p>
<ol>
<li>You are using a torch that is cuda enabled</li>
<li>Torch is indeed using the GPU (incorrect environment setup can block this).</li>
</ol>
<p>See this answer, and follow the steps and see if you are seeing your V100 being reported.</p><aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu">
  <header class="source">

      <a href="https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu" target="_blank" rel="noopener nofollow ugc">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/5446749/vinzee" target="_blank" rel="noopener nofollow ugc">
    <img alt="vinzee" src="https://i.stack.imgur.com/fzsuf.jpg?s=256&amp;g=1" class="thumbnail onebox-avatar" width="256" height="256">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu" target="_blank" rel="noopener nofollow ugc">How to check if pytorch is using the GPU?</a>
</h4>

<div class="tags">
  <strong>python, memory-management, gpu, nvidia</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/5446749/vinzee" target="_blank" rel="noopener nofollow ugc">
    vinzee
  </a>
  on <a href="https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu" target="_blank" rel="noopener nofollow ugc">02:50PM - 08 Jan 18 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Ron (2022-06-04 23:39 UTC)

<p>Dear Murat<br>
Thanks for the suggestion, I will work with Andres on Monday and see if we can find and fix what is the issue. Will post our solution.  Thanks, Ron</p>

---

## Post #4 by @mau_igna_06 (2022-06-05 10:55 UTC)

<p>We were able to use gpus on docker enviroments using virtualgl with vglrun…<br>
I have read that this methos was also used for AI.<br>
So you need to set up a docker image test.</p>
<p>Maybe <a class="mention" href="/u/lassoan">@lassoan</a> has some experience woth this</p>
<p>Hope it helps</p>

---

## Post #5 by @RafaelPalomar (2022-06-05 12:24 UTC)

<p>Hello <a class="mention" href="/u/Ron">@Ron</a>,</p>
<p>a while ago I asked the same question in the MONAI Label discussions (<a href="https://github.com/Project-MONAI/MONAILabel/discussions/282" class="inline-onebox" rel="noopener nofollow ugc">Generic deepgrow -- High CPU usage and low GPU usage · Discussion #282 · Project-MONAI/MONAILabel · GitHub</a>). My feeling was that some operators in some MONAI Label applications were GPU-based while others were only CPU-based. The answer that I got points to that direction. I hope this helps.</p>

---

## Post #7 by @mau_igna_06 (2022-06-05 13:00 UTC)

<p>sohuld work on gpu—</p>

---
