---
topic_id: 6298
title: "Machine Learning Model Importing"
date: 2019-03-26
url: https://discourse.slicer.org/t/6298
---

# Machine Learning Model Importing

**Topic ID**: 6298
**Date**: 2019-03-26
**URL**: https://discourse.slicer.org/t/machine-learning-model-importing/6298

---

## Post #1 by @coolsocks (2019-03-26 20:07 UTC)

<p>Hi!</p>
<p>I am currently building a module which involves importing a deep learning model trained with keras to predict some segmentations. Initially, the question I had was how to go about running the keras/tensorflow packages in the module that I would like to create. I found an answe to that question here: <a href="https://discourse.slicer.org/t/loading-a-deep-learning-model-to-a-scripted-module/6068" class="inline-onebox">Loading a deep learning model to a scripted module</a></p>
<p>What I’m wondering is that if this approach is feasible if I were to package these modules into an extension. If a user were to download this extension on a different computer, and use it there, would the packages still install in their version of slicer-python? If not, do you have any recommendations on how to approach this issue or any resources on how to do this?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2019-03-26 21:08 UTC)

<p>It can be hard to distribute models given the constraints on computing environments.  We think that when Slicer moves to python 3 (maybe as soon as next week) it will be easier, but there are still some potential problems.  You might look at bundling through DeepInfer, which uses Docker for the computing.</p>
<p><a href="http://www.deepinfer.org/" class="onebox" target="_blank" rel="nofollow noopener">http://www.deepinfer.org/</a></p>

---

## Post #3 by @mlp6 (2019-08-28 18:01 UTC)

<p>Any updates on the “best practice” for developing a slicer module that uses tensorflow under the hood?  We’re looking to implement <a href="https://arxiv.org/abs/1908.05782" rel="nofollow noopener">https://arxiv.org/abs/1908.05782</a> as a module, and would like to start with our best foot forward.  The <code>DeepInfer</code> approach w/ a Docker backend seems attractive, but it would add some appreciable setup overhead on Windows client machines, which is our target.</p>

---

## Post #4 by @pieper (2019-08-28 18:26 UTC)

<p>Hi -</p>
<p>With the Slicer nightly you can use the <code>slicer.util.pip_install()</code> command to install tensorflow and many other standard packages directly.  This opens the door for a lot of interesting things but the exact practices haven’t yet been explored.  It would be great to see people try some experiments.  I’d love to see how things go because getting some of these models directly in slicer has been on my wishlist for quite a while.</p>

---

## Post #5 by @mlp6 (2019-08-28 18:48 UTC)

<p>We might be those guinea pigs… our decision point hinges on the most robust way to support CPU and GPU hardware with the package install since the latter would need to play nicely w/ CUDA library installs, etc.  We already have an existing pain point when doing that on a machine-to-machine basis, and Docker solves a lot of those problems.  Some packages like (I think) <code>pytorch</code> bundle the necessary libraries with the package install, which would be another approach.</p>

---

## Post #6 by @pieper (2019-08-28 19:11 UTC)

<p>I believe it should work if the user has the right other dependencies installed (e.g. CUDA).  I’ve tested with other python libraries pip installed in Slicer that access the GPU and it worked.</p>

---

## Post #7 by @lassoan (2019-08-28 20:44 UTC)

<p>We use both tensorflow CPU and GPU in Slicer on Windows without docker. You may need to copy some Cuda DLLs manually to make GPU work, which should be no problem for developers, but may need some work to make it fully automatic and robust for non-technical users.</p>
<p>Overall, there are many deployment options you can choose from, with several examples you can follow (DeepInfer, TOMAAT, <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/" rel="nofollow noopener">NVidia Clara segment editor effect</a>, <a href="https://github.com/SlicerIGT/aigt" rel="nofollow noopener">AIGT</a>). The best option depends on your constraints - what hardware you need to support, how computationally demanding your application is, what are your time constraints, network connectivity, privacy concerns, how many users you need to serve, who are your users, etc.</p>

---

## Post #8 by @JanWitowski (2019-08-29 00:04 UTC)

<p>I have been doing some experiments with connecting a few automatic segmentation&amp;object architectures (e.g. U-Net, RetinaNet) with TOMAAT and it seems like a simple tool for prototyping. Might post a short video of initial results next week.</p>

---

## Post #9 by @muratmaga (2020-02-27 00:12 UTC)

<p><a class="mention" href="/u/lassoan">@Lassoan</a> do you have specific instructions to get tensorflow with GPU enabled under Slicer?</p>

---

## Post #10 by @lassoan (2020-02-27 13:52 UTC)

<p>If you pip install tensorflow 2 on Windows or Linux then you can use both CPU and GPU. No special instructions are needed (other than in general setting up Cuda on Linux can be tricky). See details in <a href="https://github.com/tensorflow/tensorflow/releases/tag/v2.1.0">release notes</a>.</p>

---
