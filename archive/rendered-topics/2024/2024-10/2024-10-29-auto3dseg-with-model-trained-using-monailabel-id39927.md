---
topic_id: 39927
title: "Auto3Dseg With Model Trained Using Monailabel"
date: 2024-10-29
url: https://discourse.slicer.org/t/39927
---

# Auto3DSeg with model trained using MONAILabel

**Topic ID**: 39927
**Date**: 2024-10-29
**URL**: https://discourse.slicer.org/t/auto3dseg-with-model-trained-using-monailabel/39927

---

## Post #1 by @h_z1 (2024-10-29 19:59 UTC)

<p>Hi,<br>
I came across this discussion <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1701" rel="noopener nofollow ugc">post</a> that referenced another post in SlicerMONAIAuto3DSeg about using inference only, which is what I am currently interested in. So, I was wondering if it was possible to use a model that was trained and annotated using the radiology app of MONAILabel to do the inference (using auto3dseg_segresnet_inference.py). I followed the format of the example command, but I keep getting the same erorr when I tried to run the command. I tried putting the path to the model that I have for segmentation using radiology sample app for MONAI Label, but also with wholeBody_ct_segmentation_v0.1.9 (pretty sure used SegResNet), and they both give me the same error:</p>
<pre><code class="lang-auto">(venv) C:\Users\hz\Documents\auto3dseg_script&gt;python auto3dseg_segresnet_inference.py --model_file "C:\Users\hz\Documents\auto3dseg_script\wholeBody_ct_segmentation_v0.1.9\wholeBody_ct_segmentation\models\model.pt" --image_file "C:\Users\hz\Documents\datasets\Task09_Spleen\imagesTr\spleen_2.nii.gz" --result_file .
C:\Users\hz\AppData\Local\Programs\Python\Python39\lib\site-packages\ignite\handlers\checkpoint.py:17: DeprecationWarning: `TorchScript` support for functional optimizers is deprecated and will be removed in a future PyTorch release. Consider using the `torch.compile` optimizer instead.
  from torch.distributed.optim import ZeroRedundancyOptimizer
You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
Traceback (most recent call last):
  File "C:\Users\hz\Documents\auto3dseg_script\auto3dseg_segresnet_inference.py", line 361, in &lt;module&gt;
    fire.Fire(main)
  File "C:\Users\hz\AppData\Local\Programs\Python\Python39\lib\site-packages\fire\core.py", line 143, in Fire
    component_trace = _Fire(component, args, parsed_flag_args, context, name)
  File "C:\Users\hz\AppData\Local\Programs\Python\Python39\lib\site-packages\fire\core.py", line 477, in _Fire
    component, remaining_args = _CallAndUpdateTrace(
  File "C:\Users\hz\AppData\Local\Programs\Python\Python39\lib\site-packages\fire\core.py", line 693, in _CallAndUpdateTrace
    component = fn(*varargs, **kwargs)
  File "C:\Users\hz\AppData\Local\Programs\Python\Python39\lib\site-packages\torch\utils\_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "C:\Users\hz\Documents\auto3dseg_script\auto3dseg_segresnet_inference.py", line 69, in main
    raise ValueError('Config not found in checkpoint (not a auto3dseg/segresnet model):' + str(model_file))
ValueError: Config not found in checkpoint (not a auto3dseg/segresnet model):C:\Users\hz\Documents\auto3dseg_script\wholeBody_ct_segmentation_v0.1.9\wholeBody_ct_segmentation\models\model.pt
</code></pre>
<p>I am not sure if I just misunderstood what should I put for the path to my model or if the model just does not work with auto3dseg_segresnet_inference.py <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>Thank you!</p>

---

## Post #2 by @diazandr3s (2024-11-26 15:02 UTC)

<aside class="quote no-group" data-username="h_z1" data-post="1" data-topic="39927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> h_z1:</div>
<blockquote>
<p>using the radiology app of MONAILabel to do the inference</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/h_z1">@h_z1</a>,</p>
<p>Thanks for asking this.</p>
<p>If you trained a model using the radiology app of MONAILabel, you could use the main script withing the radiology app/folder to run inference without starting the server: <a href="https://github.com/Project-MONAI/MONAILabel/blob/da0247ee54651014e841d6261f6d00908f4108cc/sample-apps/radiology/main.py#L286-L371" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/radiology/main.py at da0247ee54651014e841d6261f6d00908f4108cc · Project-MONAI/MONAILabel · GitHub</a></p>
<p>The script <em><a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py" rel="noopener nofollow ugc">auto3dseg_segresnet_inference.py</a></em> is mainly for Auto3DSeg models: <a href="https://discourse.slicer.org/t/new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation/35680" class="inline-onebox">New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation</a></p>
<p>Hope this helps,</p>

---
