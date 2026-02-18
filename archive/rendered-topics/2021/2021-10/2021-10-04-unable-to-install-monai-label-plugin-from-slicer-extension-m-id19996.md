# unable to install MONAI Label plugin from Slicer Extension Manager

**Topic ID**: 19996
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/unable-to-install-monai-label-plugin-from-slicer-extension-manager/19996

---

## Post #1 by @poonam1 (2021-10-04 18:19 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: to install plugin <strong>View</strong> → <strong>Extension Manager</strong> → <strong>Active Learning</strong> → <strong>MONAI Label</strong><br>
Actual behavior: but In extension manager Active learning module is not found.</p>

---

## Post #2 by @lassoan (2021-10-04 18:21 UTC)

<p>As it is described in the <a href="https://github.com/Project-MONAI/MONAILabel#3d-slicer">MONAILabel installation instructions</a>, you must use the latest Slicer Preview Release. MONAILabel is not available for Slicer-4.11.20210226.</p>

---

## Post #3 by @poonam1 (2021-10-04 20:38 UTC)

<p>Thank you Andras for your reply!<br>
Now, when I am trying to annotate then getting following error<br>
‘RuntimeError: Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False. If you are running on a CPU-only machine, please use torch.load with map_location=torch.device(‘cpu’) to map your storages to the CPU.’</p>
<p>So, Could you please tell me how I can set this value in my cpu based system.<br>
Thanks in advance!</p>

---

## Post #4 by @lassoan (2021-10-05 12:32 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> could you help with this question?</p>

---

## Post #5 by @diazandr3s (2021-10-05 19:50 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a> for ping me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
<a class="mention" href="/u/poonam1">@poonam1</a> thanks for your interest in MONAI Label.<br>
We’ve developed MONAI Label to work on a computer with a GPU. Even a small one. They are important because the training/inference will be very slow otherwise.</p>

---

## Post #6 by @poonam1 (2021-10-06 14:18 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a> thank you for response!<br>
I get that it is for GPU based system, but I am willing to try on my CPU based system once and then I will transfer that to GPU one.<br>
So please if you can help me setting up on my system, then it would be really grateful.<br>
Thanks,</p>

---

## Post #7 by @lassoan (2021-10-06 14:48 UTC)

<p>Some inference tasks work perfectly well on a CPU. For example ultrasound segmentation - the images are quite small and just 2D. Does MONAILabel enforces the presence of a GPU or a model/sample app imposes this limitation?</p>

---

## Post #8 by @diazandr3s (2021-10-06 16:06 UTC)

<p>The type of device used for inference and training is a variable configuration that is set by default to GPU. Depending on which MONAI Label App (i.e. DeepEdit, DeepGrow or segmentation), you should change that … for instance, if you want to train any App, you should change this to CPU (<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/monailabel/tasks/train/basic_train.py#L255" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/basic_train.py at main · Project-MONAI/MONAILabel · GitHub</a>)<br>
If you want to do inference in the “segmentation” App, you should change this line: <a href="https://github.com/Project-MONAI/MONAILabel/blob/ca9ffe553889f0ea9d99e0133c359851a5ea2003/monailabel/interfaces/tasks/infer.py#L220" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/infer.py at ca9ffe553889f0ea9d99e0133c359851a5ea2003 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>If using a pre-trained model in the segmentation App, don’t forget to also change this line (<a href="https://github.com/Project-MONAI/MONAILabel/blob/ca9ffe553889f0ea9d99e0133c359851a5ea2003/monailabel/interfaces/tasks/infer.py#L316" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/infer.py at ca9ffe553889f0ea9d99e0133c359851a5ea2003 · Project-MONAI/MONAILabel · GitHub</a>) so the model is loaded to work on the CPU.</p>

---
