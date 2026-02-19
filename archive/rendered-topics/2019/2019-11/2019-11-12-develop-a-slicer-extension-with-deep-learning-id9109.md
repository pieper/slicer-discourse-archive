---
topic_id: 9109
title: "Develop A Slicer Extension With Deep Learning"
date: 2019-11-12
url: https://discourse.slicer.org/t/9109
---

# Develop a slicer extension with Deep Learning

**Topic ID**: 9109
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/develop-a-slicer-extension-with-deep-learning/9109

---

## Post #1 by @mikecsu (2019-11-12 01:45 UTC)

<p>Operating system: win 10<br>
Slicer version:4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi, everyone. I am doing some investigations to know about if it is possible to develop a slicer extension with Deep Learning on the current version slicer 4.11.0.</p>
<p>Also，Deep Learning Framework, such as tensorflow, Keras and Pytorch.  Which one is better or more compatiable for a slicer extension development  ?</p>
<p>Any references or examples are welcome.</p>
<p>Any help would be appreciated.</p>

---

## Post #2 by @ungi (2019-11-12 03:42 UTC)

<p>Hi,</p>
<p>We made a tutorial that guides you through how to train a deep learning model with data exported from Slicer, and how to use the trained model in a Slicer module for predictions:<br>
<a href="http://www.slicerigt.org/wp/cars-2019-tutorial/" class="onebox" target="_blank" rel="nofollow noopener">http://www.slicerigt.org/wp/cars-2019-tutorial/</a><br>
This example uses webcam images, but you can use 99% of the examples for any medical image type.</p>
<p>You will find some example code in this project too, mostly on ultrasound segmentation:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerIGT/aigt" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/2845029?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/SlicerIGT/aigt" target="_blank" rel="nofollow noopener">SlicerIGT/aigt</a></h3>

<p>Deep learning software modules for image-guided medical procedures - SlicerIGT/aigt</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Slicer can use TensorFlow, so I suggest you use Keras (now officially part of TensorFlow). I couldn’t figure out how to use PyTorch in Slicer, but it must be possible somehow. Keras seems to be more popular anyway.</p>
<p>I hope this helps,<br>
Tamas</p>

---

## Post #3 by @mholden8 (2019-11-12 16:21 UTC)

<p>Thanks <a class="mention" href="/u/ungi">@ungi</a> for the great resources! I will check them out too.</p>
<p>I would just like to add that I use PyTorch from Slicer sometimes, so I can explain how I have gotten it to work…</p>
<p>If you go to <a href="http://pytorch.org" rel="nofollow noopener">pytorch.org</a>, it will provide the proper install command for your configuration.<br>
Then you can install PyTorch in Slicer’s Python via:</p>
<pre><code class="lang-auto">C:\path\to\Slicer\bin\PythonSlicer -m &lt;install-command&gt;
</code></pre>
<p>For example, I use Windows 10 and do not have GPU, so I used the command:</p>
<pre><code class="lang-auto">C:\path\to\Slicer\bin\PythonSlicer -m pip install torch==1.3.1+cpu torchvision==0.4.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
</code></pre>
<p>Once installed, you can import PyTorch into Slicer’s Python interactor with the standard command:</p>
<pre><code class="lang-auto">import torch
import torchvision
</code></pre>

---
