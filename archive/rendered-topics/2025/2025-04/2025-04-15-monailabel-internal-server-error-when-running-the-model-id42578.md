---
topic_id: 42578
title: "Monailabel Internal Server Error When Running The Model"
date: 2025-04-15
url: https://discourse.slicer.org/t/42578
---

# MonaiLabel internal server error when running the model

**Topic ID**: 42578
**Date**: 2025-04-15
**URL**: https://discourse.slicer.org/t/monailabel-internal-server-error-when-running-the-model/42578

---

## Post #1 by @chz31 (2025-04-15 18:59 UTC)

<p>Hi,</p>
<p>I successfully trained a model using MonaiLabel for a simple skull segmentation. However, when I tested running the model on a volume, it reported <code>Status: 500; Response: Internal Server Error</code></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/ProgramData/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAILabel/lib/Slicer-5.8/qt-scripted-modules/MONAILabel.py", line 1565, in onClickSegmentation
    result_file, params = self.logic.infer(model, image_file, params, session_id=self.getSessionId())
  File "C:/ProgramData/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAILabel/lib/Slicer-5.8/qt-scripted-modules/MONAILabel.py", line 2397, in infer
    result_file, params = client.infer(model, image_in, params, label_in, file, session_id)
  File "C:\ProgramData\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAILabel\lib\Slicer-5.8\qt-scripted-modules\MONAILabelLib\client.py", line 344, in infer
    raise MONAILabelClientException(
MONAILabelLib.client.MONAILabelClientException: (1, 'Status: 500; Response: Internal Server Error')
</code></pre>
<p>I used the deepedit model. The only modification I did was simply changing the labels in deepedit.py to</p>
<pre><code class="lang-auto">self.labels = {
            "skull": 1,
            "background": 0,
        }
</code></pre>
<p>I also saved the model script as <code>deepedit_skull.py.</code></p>
<p>I could train and run the default deepedit model to segment a new abdominal volume with no problem.</p>
<p>Here is the full log of the Slicer session: <a href="https://drive.google.com/file/d/1g2NypYBYqVZUxdcR0s4hIvirIODwEmy_/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">Slicer_5.8.0_33216_20250415_124050_526.log - Google Drive</a></p>

---

## Post #2 by @muratmaga (2025-04-16 01:55 UTC)

<p><a class="mention" href="/u/chz31">@chz31</a> given that you are using 5.8.0, I would first suggest trying with the latest preview or the stable (5.8.1) to rule out issues that might have been already fixed.</p>

---

## Post #3 by @chz31 (2025-04-16 03:56 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thanks! I found the reason was because I still used the pretrained deepedit model, so it expected 9 labels instead of 2:</p>
<pre><code class="lang-auto">"C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\site-packages\torch\nn\modules\module.py", line 2581, in load_state_dict
    raise RuntimeError(
RuntimeError: Error(s) in loading state_dict for DynUNet:
        size mismatch for input_block.conv1.conv.weight: copying a param with shape torch.Size([32, 9, 3, 3, 3]) from checkpoint, the shape in current model is torch.Size([32, 3, 3, 3, 3]).
        size mismatch for input_block.conv3.conv.weight: copying a param with shape torch.Size([32, 9, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([32, 3, 1, 1, 1]).
        size mismatch for output_block.conv.conv.weight: copying a param with shape torch.Size([8, 32, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([2, 32, 1, 1, 1]).
        size mismatch for output_block.conv.conv.bias: copying a param with shape torch.Size([8]) from checkpoint, the shape in current model is torch.Size([2]).
        size mismatch for skip_layers.downsample.conv1.conv.weight: copying a param with shape torch.Size([32, 9, 3, 3, 3]) from checkpoint, the shape in current model is torch.Size([32, 3, 3, 3, 3]).
        size mismatch for skip_layers.downsample.conv3.conv.weight: copying a param with shape torch.Size([32, 9, 1, 1, 1]) from checkpoint, the shape in current model is torch.Size([32, 3, 1, 1, 1]).
</code></pre>
<p>I followed the instruction here <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1252#discussioncomment-4758944" class="inline-onebox" rel="noopener nofollow ugc">Error while Training from scratch · Project-MONAI/MONAILabel · Discussion #1252 · GitHub</a> to specify <code>--conf use_pretrained_model false</code> and removed the pt files in radiology/model. It worked now.</p>

---
