---
topic_id: 39699
title: "Monailabel Issue Internal Server Error"
date: 2024-10-14
url: https://discourse.slicer.org/t/39699
---

# Monailabel issue - Internal Server Error

**Topic ID**: 39699
**Date**: 2024-10-14
**URL**: https://discourse.slicer.org/t/monailabel-issue-internal-server-error/39699

---

## Post #1 by @Daniel_Lo (2024-10-14 17:40 UTC)

<p>Facing a few issues while using monailabel training.<br>
1)<br>
[Python] Failed to run inference in MONAI Label Server.<br>
[Python] Message: Status: 500; Response: Internal Server Error</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/admin/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py”, line 1545, in onClickSegmentation<br>
result_file, params = self.logic.infer(model, image_file, params, session_id=self.getSessionId())<br>
File “C:/Users/admin/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py”, line 2321, in infer<br>
result_file, params = client.infer(model, image_in, params, label_in, file, session_id)<br>
File “C:\Users\admin\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\MONAILabel\lib\Slicer-5.6\qt-scripted-modules\MONAILabelLib\client.py”, line 344, in infer<br>
raise MONAILabelClientException(<br>
MONAILabelLib.client.MONAILabelClientException: (1, ‘Status: 500; Response: Internal Server Error’)</p>
<ol start="2">
<li>training bar and accuracy bar shows training error and accuracy 0.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab1f1b4f23445c018abee98db0d47d5840aa3307.jpeg" data-download-href="/uploads/short-url/opOib2bZf7IDi1es4QV1yk7qOxx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab1f1b4f23445c018abee98db0d47d5840aa3307_2_690x381.jpeg" alt="image" data-base62-sha1="opOib2bZf7IDi1es4QV1yk7qOxx" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab1f1b4f23445c018abee98db0d47d5840aa3307_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab1f1b4f23445c018abee98db0d47d5840aa3307_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab1f1b4f23445c018abee98db0d47d5840aa3307_2_1380x762.jpeg 2x" data-dominant-color="A0A1A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1503×831 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>3)happens during training<br>
RuntimeError: Error(s) in loading state_dict for SegResNet:<br>
size mismatch for conv_final.2.conv.weight: copying a param with shape torch.Size([26, 32, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([3, 32, 1, 1, 1]).<br>
size mismatch for conv_final.2.conv.bias: copying a param with shape torch.Size([26]) from checkpoint, the shape in current model is torch.Size([3]).</p>

---

## Post #2 by @diazandr3s (2024-10-17 21:51 UTC)

<p>Hi <a class="mention" href="/u/daniel_lo">@Daniel_Lo</a>,</p>
<p>It looks like the issue might be related to a mismatch between the number of labels the model was trained on and those defined in the config file. Could you please share a bit more detail so we can help replicate the issue?</p>
<p>Also, for any questions specifically about MONAI Label, it might be helpful to comment directly on the MONAI Label repository: <a href="https://github.com/Project-MONAI/MONAILabel" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>
<p>Best,</p>

---

## Post #3 by @Miro_Spiro (2025-02-14 19:13 UTC)

<p>So i have same trouble.</p>
<p>I make training from scratch, change segmentation file and made active learning 100%.</p>
<p>Monailabel is install on localhost Fujitsu Primergy with 192 GB RAM and nVidia GTX 1070 under Ubuntu 24.04.</p>
<p>Dataset for learning is from tutorial learning from scratch.</p>
<p>I want to autosegment data from <a href="https://academictorrents.com/details/f2175c4676e041ea65568bb70c2bcd15c7325fd2" class="inline-onebox" rel="noopener nofollow ugc">MosMedData: Chest CT Scans with COVID-19 Related Findings COVID19_1110 1.0 - Academic Torrents</a></p>
<p>Error in console: File “/home/mirospiro/anaconda3/lib/python3.12/site-packages/monailabel/tasks/infer/basic_infer.py”, line 479, in _get_network<br>
network.load_state_dict(model_state_dict, strict=self.load_strict)<br>
File “/home/mirospiro/anaconda3/lib/python3.12/site-packages/torch/nn/modules/module.py”, line 2584, in load_state_dict<br>
raise RuntimeError(<br>
RuntimeError: Error(s) in loading state_dict for SegResNet:<br>
size mismatch for conv_final.2.conv.weight: copying a param with shape torch.Size([26, 32, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([3, 32, 1, 1, 1]).<br>
size mismatch for conv_final.2.conv.bias: copying a param with shape torch.Size([26]) from checkpoint, the shape in current model is torch.Size([3]).<br>
[2025-02-14 19:56:02,928] [295788] [Thread-4] [INFO] (monailabel.utils.sessions:</p>

---

## Post #4 by @diazandr3s (2025-02-17 10:57 UTC)

<p>Hi <a class="mention" href="/u/miro_spiro">@Miro_Spiro</a>,</p>
<p>Thanks for sharing the logs.<br>
From the log, it seems you’re trying to train a model for a different number of labels/segments than the pretrained model. I suggest you remove the pretrained file (.pt file) from the model folder and set this flag to false before starting the server: <a href="https://github.com/Project-MONAI/MONAILabel/blob/b205e92d5e5fcd265c17e33eb13ccfd855b74e7f/sample-apps/radiology/lib/configs/segmentation.py#L77" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/radiology/lib/configs/segmentation.py at b205e92d5e5fcd265c17e33eb13ccfd855b74e7f · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Also, I strongly suggest you post future insights/comments dirently in the <a href="https://github.com/Project-MONAI/MONAILabel" rel="noopener nofollow ugc">MONAI Label repo</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Hope this helps</p>

---
