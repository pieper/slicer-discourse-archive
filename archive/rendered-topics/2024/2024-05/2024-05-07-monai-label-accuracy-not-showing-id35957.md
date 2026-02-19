---
topic_id: 35957
title: "Monai Label Accuracy Not Showing"
date: 2024-05-07
url: https://discourse.slicer.org/t/35957
---

# Monai Label: accuracy not showing

**Topic ID**: 35957
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/monai-label-accuracy-not-showing/35957

---

## Post #1 by @ILB (2024-05-07 07:58 UTC)

<p>Hi!<br>
I’m currently training a new model using Monai Label.</p>
<p>I start using this configuration:</p>
<p><code>monailabel start_server --app apps/radiology --studies datasets/Task07_Pancreas/imagesTr --conf models deepedit --conf use_pretrained_model false</code></p>
<p>I have already submitted 26 labels, and the accuracy bar is still 0. Is that normal?</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9dbc352dae8e14f0902ca2b0e1b3947a532e54c.png" data-download-href="/uploads/short-url/zElJgJUMHLaXkEJletmi503DuaM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9dbc352dae8e14f0902ca2b0e1b3947a532e54c.png" alt="image" data-base62-sha1="zElJgJUMHLaXkEJletmi503DuaM" width="457" height="500" data-dominant-color="EFF3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">651×712 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ILB (2024-05-07 09:05 UTC)

<p>i get this error:</p>
<pre><code class="lang-auto">raise RuntimeError('Error(s) in loading state_dict for {}:\n\t{}'.format(
RuntimeError: Error(s) in loading state_dict for DynUNet:
        size mismatch for input_block.conv1.conv.weight: copying a param with shape torch.Size([32, 5, 3, 3, 3]) from checkpoint, the shape in current model is torch.Size([32, 2, 3, 3, 3]).
        size mismatch for input_block.conv3.conv.weight: copying a param with shape torch.Size([32, 5, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([32, 2, 1, 1, 1]).
        size mismatch for output_block.conv.conv.weight: copying a param with shape torch.Size([4, 32, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 32, 1, 1, 1]).
        size mismatch for output_block.conv.conv.bias: copying a param with shape torch.Size([4]) from checkpoint, the shape in current model is torch.Size([1]).
        size mismatch for skip_layers.downsample.conv1.conv.weight: copying a param with shape torch.Size([32, 5, 3, 3, 3]) from checkpoint, the shape in current model is torch.Size([32, 2, 3, 3, 3]).
        size mismatch for skip_layers.downsample.conv3.conv.weight: copying a param with shape torch.Size([32, 5, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([32, 2, 1, 1, 1]).
[2024-05-07 11:00:27,144] [12688] [ThreadPoolExecutor-1_0] [INFO] (monailabel.utils.async_tasks.utils:83) - Return code: 1
</code></pre>
<p>i don’t know how to solve this</p>

---
