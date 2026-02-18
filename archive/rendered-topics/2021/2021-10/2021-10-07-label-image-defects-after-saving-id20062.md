# Label image defects after saving

**Topic ID**: 20062
**Date**: 2021-10-07
**URL**: https://discourse.slicer.org/t/label-image-defects-after-saving/20062

---

## Post #1 by @MachadoL (2021-10-07 21:05 UTC)

<p>Guys, I am not sure if that is the correct place to ask that, BUT I have nowhere to run.</p>
<p>I used <code>nrrd</code> and <code>slicerio</code> extensions to separate <code>.seg.nrrd</code> files into separated segments or label images.<br>
Great. It gives me array images. I, then, proceed SAVING those labels into local image files (<code>.jpeg</code>). Good.</p>
<p>The problem arises when I load such images back into say jupyter notebook for Deep Learning application.</p>
<p>I created a binary, <code>1 and 0</code>, label image and saved in <code>.jpeg</code>, however when I load them back into python, some random pixels with value 2 appears. Yes! 2. How come?</p>
<p>I checked loading with both <code>matplotlib</code> <code>(imread)</code> and <code>Pillow</code>. By the way, I saved those images with Pillow in <code>.jpeg</code> format. I’ve tracked the whole code and everything sounds ok. The crashing happens after saving and loading it back.</p>
<p>I am working with deep learning semantic segmentation and it is crucial that the image have only 0 and 1`s.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2021-10-07 21:23 UTC)

<p>I’d guess those are compression artifacts from the jpg encoding.  Maybe you can use .png instead?</p>

---

## Post #3 by @jamesobutler (2021-10-07 21:47 UTC)

<p>The current recommendation for Medical Imaging Deep Learning is to use <a href="https://github.com/Project-MONAI/MONAI" rel="noopener nofollow ugc">Monai</a> where you are using the medical imaging file directly such as a nrrd file. You are likely to run into issues using simple image formats like jpeg.</p>
<p>Tutorials for Monai are available at <a href="https://github.com/Project-MONAI/tutorials" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/tutorials: MONAI Tutorials</a>.</p>

---

## Post #4 by @MachadoL (2021-10-08 14:02 UTC)

<p>That was it. Thanks a lot, <a class="mention" href="/u/pieper">@pieper</a>!</p>

---
