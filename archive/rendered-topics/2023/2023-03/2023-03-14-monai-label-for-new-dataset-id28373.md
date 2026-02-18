# MONAI Label for New Dataset

**Topic ID**: 28373
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/monai-label-for-new-dataset/28373

---

## Post #1 by @S_Arbabi (2023-03-14 12:36 UTC)

<p>Hi,</p>
<p>I was able to run MONAI Label on server and connect through slicer, load images that I added to server (I haven’t tried adding segmentations to server though).<br>
I have a dataset that I have used for training nnUNet as it is described in their <a href="https://github.com/MIC-DKFZ/nnUNet" rel="noopener nofollow ugc">github page</a>.<br>
Now I wanted to use that dataset with MONAI Label. I have a few questions:<br>
1- is it possible to use my nnUNet trained model as a basis for what I can improve interactively in MONAI Label? (I can imagine that is not straightforward, if possible. although MONAI dynunet is similar to nnUNet but still a lot differences) I see an <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1277" rel="noopener nofollow ugc">issue in github of MONAI Label</a>, but seems not resolved.<br>
2-If I want to add my dataset (images, binary labels all .nii.gz the way nnUNet digests), to MONAI Label server, is there a tutorial helping out in there? I believe in that way even (let’s say I use deepedit) I will need to change self.labels dictionary somewhere, but I couldn’t find this in deepedit main.py.<br>
3-If it’s not possible to add my already done segmentation to server to help it start training from above zero, what should I change in the model?</p>
<p>Thanks,<br>
Saeed</p>

---

## Post #2 by @rbumm (2023-03-15 07:46 UTC)

<p>There are several threads concerning this topic here in Slicer discourse, maybe <a href="https://discourse.slicer.org/t/novice-guidance-for-using-monai-label-to-create-an-automatic-segmentation-app/27504/15">even this recent post</a> of <a class="mention" href="/u/diazandr3s">@diazandr3s</a> can get you started. We have been using the ML segmentation model for a while in similar approaches.</p>
<aside class="quote no-group quote-modified" data-username="S_Arbabi" data-post="1" data-topic="28373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/dfb087/48.png" class="avatar"> S_Arbabi:</div>
<blockquote>
<p>I was able to run MONAI Label on the server and connect through the slicer,</p>
</blockquote>
</aside>
<p>You should then have downloaded a demo dataset and in this dataset, you will find directories that you could duplicate for your own project and where you could put your pre-analyzed data. Another, maybe safer way would be to load each image and corresponding label into 3D Slicer first and upload each case to the MonaiLabel Server by the “Submit label” mechanism of the extension, then train.</p>

---

## Post #3 by @diazandr3s (2023-03-15 18:11 UTC)

<p>Thanks for the ping <a class="mention" href="/u/rbumm">@rbumm</a><br>
This is a very good question <a class="mention" href="/u/s_arbabi">@S_Arbabi</a>. At the moment, it is not straightforward to use nnUNET models in MONAI Label. However, for any model you have trained using nnUNET you could do the same using MONAI Label.</p>
<p>As an example of this, we’ve trained a whole-body CT segmentation model using the Total Segmentator dataset: <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation" class="inline-onebox" rel="noopener nofollow ugc">model-zoo/models/wholeBody_ct_segmentation at dev · Project-MONAI/model-zoo · GitHub</a></p>
<p>Here is the video where I briefly talk about the technical details of this implementation:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="KtPE8m0LvcQ" data-video-title="MONAI Label Workshop - Project Week 38" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=KtPE8m0LvcQ" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/KtPE8m0LvcQ/maxresdefault.jpg" title="MONAI Label Workshop - Project Week 38" width="" height="">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="KtPE8m0LvcQ" data-video-title="MONAI Label Workshop - Project Week 38" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=KtPE8m0LvcQ" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/KtPE8m0LvcQ/maxresdefault.jpg" title="MONAI Label Workshop - Project Week 38" width="" height="">
  </a>
</div>

<p>I used a single SegResNet network and get comparable results. If needed, you could also implement multiple networks and do ensembling as done in the nnUNET framework.</p>
<p>Here you can see how the dataset should be prepared to use MONAI Label: <a href="https://youtu.be/KtPE8m0LvcQ?t=500" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label Workshop - Project Week 38 - YouTube</a></p>
<p>I’d recommend you start with the segmentation model available on the latest MONAI Label version: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#segmentation" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/radiology at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Update these label names according to your task:<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation.py#L37-L63" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/segmentation.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>and put this to false so you start from scratch the training process: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation.py#L72" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/segmentation.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Hope this helps,</p>

---

## Post #4 by @S_Arbabi (2023-09-14 09:29 UTC)

<p>with the implementation of monai.apps.nnunet. nnunetv2_runner I believe now it should be easy(ier) to integrate nnunet into monailabel.<br>
Any ideas for a faster start? <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>

---

## Post #5 by @diazandr3s (2023-09-16 22:22 UTC)

<p>Hi <a class="mention" href="/u/s_arbabi">@S_Arbabi</a>,</p>
<p>Very good question!<br>
The possibility of training the nnUNet in MONAI is indeed a great benefit for the community.<br>
However, there is still work to do to use the nnUNet in MONAI Label. As you may know, nnUNet is not a network architecture, but rather a <strong>semantic segmentation method</strong> that automatically adapts to a given dataset. It involves multiple algorithms such as data fingerprints, ensembling using different network configurations, etc.</p>
<p>The integration of this method in MONAI Label isn’t a straightforward task.</p>
<p>If you don’t mind, please open an issue or discussion in the MONAI repo (<a href="https://github.com/Project-MONAI/MONAI/issues" class="inline-onebox" rel="noopener nofollow ugc">Issues · Project-MONAI/MONAI · GitHub</a>) so others can also comment.</p>
<p>Best,</p>

---

## Post #6 by @sfat (2023-12-23 12:01 UTC)

<p>This might sound like a basic questions thats’ been answered before but I’m kinda stuck.<br>
I want to train a model to detect epicardial adipose tissue (EAT)  on CCTA (I can’t seem to find anything reliable at the model … happy to be corrected if anyone can save me from spending my Christmas break segmenting <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">)<br>
I think the best course of action is to use the pre-trained wholeBody_ct_segmentation model along with deepEdit to get the cardiac structures, and then manually segment EAT and gradually train my model after a few hundred cases.<br>
Does this sound like a reasonable approach (consider the complexities of EAT) and if so, how do I add EAT as a new label in the model if I’m using a retrained model ?</p>

---

## Post #7 by @rbumm (2023-12-23 22:24 UTC)

<p>Thanks for your question, which is important and relevant.<br>
What I could contribute that you can use deepedit or segmentation model and do not need to label a few hundred cases before you train. You can start training after about 20, even aftler maybe five lableled cases, and then use MONAILabel to infer the “next dataset” that you load. I have exclusive experience with the “segmentation” technique of MONAILabel and good experiences. But you find more information of deepedit vs. segmentation in the <a href="https://chat.openai.com/share/d5b1b3fd-141a-47bc-9e42-7f17dbf516f6">ChatGPT conversation here</a>.</p>

---

## Post #8 by @diazandr3s (2024-01-01 21:18 UTC)

<p>Good question, <a class="mention" href="/u/sfat">@sfat</a>.<br>
Are you still working on this task? Would you be able to share a segmented case? I’d like to see an example so I can comment on more details of the best model/approach to use.<br>
Happy to meet and further discuss an approach.</p>

---
