---
topic_id: 33175
title: "Monailabel Does Training Data Need To Be Registered"
date: 2023-12-02
url: https://discourse.slicer.org/t/33175
---

# MonaiLabel-does training data need to be registered?

**Topic ID**: 33175
**Date**: 2023-12-02
**URL**: https://discourse.slicer.org/t/monailabel-does-training-data-need-to-be-registered/33175

---

## Post #1 by @nick_george_jones (2023-12-02 02:31 UTC)

<p>Have set up a label server and starting training. One question I had, as someone relatively new to deep learning based segmentation model development, is if the input images need to be co-registered to some sort of standard? or should the model take care of that? I am using the segmentation.py file.</p>

---

## Post #2 by @muratmaga (2023-12-02 03:38 UTC)

<p>This is hard to answer without knowing how different the images are from each other. In my experience, the augmentation pipeline in MonaiLabel is quite robust to rotational and translational differences between samples. If your dataset is substantially variable, training may take somewhat longer though…</p>

---

## Post #3 by @nick_george_jones (2023-12-04 21:47 UTC)

<p>Thanks for your input! these are all thin cut temporal bone CT’s so I don’t think there is that much variability but there are certainly some.</p>

---

## Post #4 by @diazandr3s (2023-12-05 11:07 UTC)

<p>Hi <a class="mention" href="/u/nick_george_jones">@nick_george_jones</a>,</p>
<p>Can you please expand on what is the type of dataset you’re using? What do you mean by co-register? Do you have more than one modality per case?</p>
<p>Let us know,</p>

---

## Post #5 by @nick_george_jones (2023-12-07 20:10 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a> ,<br>
No, it is just a thin-cut temporal bone CT scan. Given variability in patient positioning and such, I thought it might improve accuracy to have them registered to a common atlas image, but in my training so far using deepedit.py it seems unnecessary per muratmaga’s thoughts</p>
<p>One question I do have is that I was wondering if it/s possible to train the model server side only, ie not issuing a request through the Slicer gui? I have access to a linux server with a much larger graphics card, but because of firewall restrictions I can’t access it from my usual machine and would have to run it all there as well as move the images there.</p>

---

## Post #6 by @diazandr3s (2023-12-11 17:00 UTC)

<p>Hi <a class="mention" href="/u/nick_george_jones">@nick_george_jones</a>,</p>
<p>Thanks for the update.</p>
<blockquote>
<p>One question I do have is that I was wondering if it/s possible to train the model server side only, ie not issuing a request through the Slicer GUI?</p>
</blockquote>
<p>Yes, you can run MONAI Label without starting the server. Here I explained how this can be done for batch inference: <a href="https://discourse.slicer.org/t/can-totalsegmentator-segment-maxillofacial-ct-as-well/32484/9" class="inline-onebox">Can TotalSegmentator segment maxillofacial CT as well? - #9 by diazandr3s</a></p>
<p>But you can do the same for any task. For training, just change this argument to train: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py#L297" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py#L297</a></p>
<p>It just works as a standard Python script.</p>
<p>Hope this helps,</p>

---

## Post #7 by @nick_george_jones (2023-12-12 19:46 UTC)

<p>Yes, thank you very much! I have it working (for now). I really appreciate all the past discussions as well as your help with this question.</p>
<p>I am wondering now, is there away to customize/set certain samples to be train vs validation? or get some insight as to which samples are validation/train in each run?</p>

---

## Post #8 by @diazandr3s (2023-12-20 21:45 UTC)

<p>By default, MONAI Label splits the dataset into 80% for training and 20% for validation.</p>
<p>Here is the method that does this split: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L394" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/monailabel/tasks/train/basic_train.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>You could overwrite this method and specify a custom validation set instead. As it is done here: <a href="https://github.com/Project-MONAI/MONAILabel/blob/testsMICCAI/sample-apps/deepedit_multilabel/lib/train.py#L242" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/deepedit_multilabel/lib/train.py at testsMICCAI · Project-MONAI/MONAILabel · GitHub</a></p>
<p>If using the Segmentation mode, this method should be overwritten in the <strong>lib/trainers/segmentation.py</strong> file</p>
<p>I hope this helps,</p>

---
