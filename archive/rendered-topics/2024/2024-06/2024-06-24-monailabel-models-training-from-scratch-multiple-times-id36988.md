---
topic_id: 36988
title: "Monailabel Models Training From Scratch Multiple Times"
date: 2024-06-24
url: https://discourse.slicer.org/t/36988
---

#  MonaiLabel Models; Training from Scratch multiple times

**Topic ID**: 36988
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/monailabel-models-training-from-scratch-multiple-times/36988

---

## Post #1 by @jessicasamir (2024-06-24 18:26 UTC)

<p>Hi everyone! I am a novice at 3D Slicer, but I am super excited to get started!</p>
<p>I have already completed the tutorials MonaiLabel offers with the Radiology App and the MONAIBundle app which are both consistent with 3D Slicer. However, I am struggling to implement a DeepEdit model. I have attached a picture of the error I keep receiving regardless of the dataset.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08db4ebd2c3bb90b0013b731cca55b91d2cd424.png" alt="runtimeerror" data-base62-sha1="yk2chJEavlbWZXzSYGyglx3LCIc" width="509" height="206"></p>
<p>I went into the config file of DeepEdit through text editor and changed it into single label and put the background as 0, pancreas as 1, and also put the use_pretrained_model as false. I am trying to attempt segmenting a bunch of different anatomical parts soon with the largest goal to be understanding Active Learning. Reading through the README.md file of the radiology app has made me realize that the DeepEdit model is the most useful for Active Learning strategies while the segmentation model is basic for automated segmentation (correct me if I’m wrong please!). I have watched the Youtube video by MonaiLabel on Training from Scratch which they use the segmentation model. However, if I do want to learn the most about Active Learning, what can I do to achieve this? Or if there is a tutorial someone can recommend me as I have been using the Training from Scratch video and the README.md files to steer me in the right direction. I would really appreciate any help!!</p>

---
