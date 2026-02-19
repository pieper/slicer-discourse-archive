---
topic_id: 31027
title: "Validation Set Accuracy In Monailabel"
date: 2023-08-07
url: https://discourse.slicer.org/t/31027
---

# Validation_set_Accuracy in MONAILabel

**Topic ID**: 31027
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/validation-set-accuracy-in-monailabel/31027

---

## Post #1 by @Spiros_Karkavitsas (2023-08-07 14:05 UTC)

<p>Hello</p>
<p>I am currently using MONAILabel extension with Slicer and I would like to ask how I can define which data is assigned for the calculation of the validation Dice similarity metric. I know I can adjust the percentage which is used for this calculation but can I also select on which data would this calculation based on?</p>
<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @diazandr3s (2023-08-08 20:43 UTC)

<p>Hi <a class="mention" href="/u/spiros_karkavitsas">@Spiros_Karkavitsas</a>,</p>
<p>Good question. Here is the method used to split the training and validation dataset: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L394-L412" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L394-L412</a></p>
<p>you could replace this method in the training file (BasicTrainTask class) like this:  <a href="https://github.com/Project-MONAI/MONAILabel/blob/testsMICCAI/sample-apps/deepedit_multilabel/lib/train.py#L242-L256" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/testsMICCAI/sample-apps/deepedit_multilabel/lib/train.py#L242-L256</a></p>
<p>hope this helps,</p>

---

## Post #3 by @Spiros_Karkavitsas (2023-12-01 11:38 UTC)

<p>Hello again,</p>
<p>Little bit late but thank you for your response <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Truth to be told, I made this question because I knew in advance I will have an issue there. Well the time has come to resolve my question.</p>
<p>However, the last time maybe I did not explain what I did. FIrst, I used MONAI app in Slicer. I used the radiology app and trained a model from scratch . I run the MONAI in a server with this command :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d93b68c4a408f28bf02b0d0a5a4469ef68b0dd19.png" data-download-href="/uploads/short-url/uZITtGzhjNeKnCo9BFERuYTRUgh.png?dl=1" title="MONAIquestion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93b68c4a408f28bf02b0d0a5a4469ef68b0dd19_2_690x17.png" alt="MONAIquestion" data-base62-sha1="uZITtGzhjNeKnCo9BFERuYTRUgh" width="690" height="17" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93b68c4a408f28bf02b0d0a5a4469ef68b0dd19_2_690x17.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93b68c4a408f28bf02b0d0a5a4469ef68b0dd19_2_1035x25.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93b68c4a408f28bf02b0d0a5a4469ef68b0dd19_2_1380x34.png 2x" data-dominant-color="111111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MONAIquestion</span><span class="informations">1823×45 6.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see I have a specific folder with the training volumes. I know the 20% of this dataset is used for validation. However, I cannot see when I call this command where exactly the validation dataset is defined.</p>
<p>I saw your answer, but I cannot find the script (train.py) which I must modify and when I start the server (with the command I provided) to use the specified validation dataset.</p>
<p>I know, it is a kind of stupid question but a I am a beginner here:)</p>
<p>Thank you and sorry for the long text.</p>

---

## Post #4 by @diazandr3s (2023-12-05 10:43 UTC)

<p>Hi <a class="mention" href="/u/spiros_karkavitsas">@Spiros_Karkavitsas</a>,</p>
<p>I see you are using the segmentation model. Here you can find the trainer file for this model: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/trainers/segmentation.py" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/trainers/segmentation.py</a></p>
<p>As you can see, the segmentation train class inherits the interface <strong>BasicTrainTask</strong>: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/trainers/segmentation.py#L41" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/trainers/segmentation.py#L41</a></p>
<p>In that class is where the training validation split happens: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L394" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L394</a></p>
<p>Hope this helps,</p>

---

## Post #5 by @Spiros_Karkavitsas (2023-12-05 13:35 UTC)

<p>Hello and thank you for your answers</p>
<p>I will check it and allow me to answer back if I cannot resolve it.</p>
<p>Thank you for the continued support <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Best<br>
Spiros</p>

---

## Post #6 by @Spiros_Karkavitsas (2023-12-06 12:11 UTC)

<p>Hello again</p>
<p>Okay, as you can see in the image, I did find the trainer file for the model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c81997fcc6d72cfc63e0dba3e0a22728a48724b.png" data-download-href="/uploads/short-url/k2YvJ7GfmdZP8ACtwN9rHqrOUGv.png?dl=1" title="MONAIquestion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c81997fcc6d72cfc63e0dba3e0a22728a48724b_2_690x418.png" alt="MONAIquestion" data-base62-sha1="k2YvJ7GfmdZP8ACtwN9rHqrOUGv" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c81997fcc6d72cfc63e0dba3e0a22728a48724b_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c81997fcc6d72cfc63e0dba3e0a22728a48724b_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c81997fcc6d72cfc63e0dba3e0a22728a48724b.png 2x" data-dominant-color="F0F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MONAIquestion</span><span class="informations">1104×669 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Another, ‘‘stupid’’ or easy question <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> : How I can access the script basic_train.py file to change the val_datalist ?</p>
<p>I saw from your last image that this file is the folder named tasks.</p>
<p>However, the files inside the radiology app that I can see are those:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e044e1710de774f030b45c4b7b4f7bf5240950d.png" data-download-href="/uploads/short-url/dpI6ypDoM3iCHAbyzpjMlJalXv7.png?dl=1" title="MONAIquestion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e044e1710de774f030b45c4b7b4f7bf5240950d_2_690x78.png" alt="MONAIquestion" data-base62-sha1="dpI6ypDoM3iCHAbyzpjMlJalXv7" width="690" height="78" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e044e1710de774f030b45c4b7b4f7bf5240950d_2_690x78.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e044e1710de774f030b45c4b7b4f7bf5240950d_2_1035x117.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e044e1710de774f030b45c4b7b4f7bf5240950d.png 2x" data-dominant-color="F2F1EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MONAIquestion</span><span class="informations">1138×130 16.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As I saw from your last image this class is located is inside a folder named Tasks, however, I cannot find it.</p>
<p>I know, these are easy questions but forgive me in advance, I am not an expert on these.</p>

---

## Post #7 by @diazandr3s (2024-02-20 14:20 UTC)

<p>Hi <a class="mention" href="/u/spiros_karkavitsas">@Spiros_Karkavitsas</a>,</p>
<p>For some reason, I just saw this reply.</p>
<p>You don’t need to modify the basic_train file. You just modify the “<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L394" rel="noopener nofollow ugc">partition_datalist</a>” method in the trainer class.<br>
When you inherit a class, all methods defined there overwrite the ones from the father class.</p>
<p>Hope this makes sense and sorry for the late reply.</p>

---

## Post #8 by @Spiros_Karkavitsas (2024-03-01 18:13 UTC)

<p>Hey and thank you for your answer. I understand what you mean, however, still I can not find the partition_datalist method . I open up the segmentation.py file and I can see the BasicTrainTask.</p>
<p>But how can I access the class and change the partition_list.</p>
<p>In general, I have trained a couple of models using MONAILabel using MR images I provided without changing the partition list etc.<br>
I want to know which images are used automatically by MONAI to calculate the validation Dice similarity metric. Are they picked randomly ? Are the fisrt 20%?</p>
<p>Thank you again and I know, my question might seem simple <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @diazandr3s (2024-03-02 10:33 UTC)

<p>Hi <a class="mention" href="/u/spiros_karkavitsas">@Spiros_Karkavitsas</a>,</p>
<p>The <em>partition_datalist</em> method is not defined in the segmentation.py file. It is part of the BasicTrainTask class (parent class). If you want to see that method in the segmentation.py file, you have to write it there and modify it as you wish.</p>
<p>This is the default way MONAI Label splits the validation and training set: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L394-L412" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/monailabel/tasks/train/basic_train.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Hope this helps,</p>

---

## Post #10 by @apparrilla (2024-11-06 21:09 UTC)

<p>Question <a class="mention" href="/u/diazandr3s">@diazandr3s</a> ,<br>
Is ther any way to make a partition_datalist method to give the validation dataset path throw the init server command as we usially do with training dataset path (–studies)?<br>
It should be nice to use the same trainer with multiple models…</p>
<p>Thanks in advance!</p>

---

## Post #11 by @diazandr3s (2024-11-14 17:15 UTC)

<p>Hi <a class="mention" href="/u/apparrilla">@apparrilla</a>,</p>
<p>That’s a good idea.</p>
<p>You could add an argument to specify the validation path here: <a href="https://github.com/Project-MONAI/MONAILabel/blob/a5733ebcf113b6811a85eeaf75af0f9e929c3567/monailabel/config.py#L28" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/monailabel/config.py at a5733ebcf113b6811a85eeaf75af0f9e929c3567 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>and in the main class here: <a href="https://github.com/Project-MONAI/MONAILabel/blob/a5733ebcf113b6811a85eeaf75af0f9e929c3567/monailabel/main.py#L38" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/monailabel/main.py at a5733ebcf113b6811a85eeaf75af0f9e929c3567 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Then you should be able to use this argument in any MONAI Label app as it uses this main class: <a href="https://github.com/Project-MONAI/MONAILabel/blob/a5733ebcf113b6811a85eeaf75af0f9e929c3567/monailabel/interfaces/app.py#L75" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/monailabel/interfaces/app.py at a5733ebcf113b6811a85eeaf75af0f9e929c3567 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Hope this helps,</p>

---
