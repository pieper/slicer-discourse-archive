---
topic_id: 32555
title: "I Am Trying To Infer From A Model In Monai Label Using 3Dsli"
date: 2023-11-02
url: https://discourse.slicer.org/t/32555
---

# I am trying to infer from a model in monai label using 3DSlicer but I am running out of GPU memory

**Topic ID**: 32555
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/i-am-trying-to-infer-from-a-model-in-monai-label-using-3dslicer-but-i-am-running-out-of-gpu-memory/32555

---

## Post #1 by @Carl_alv (2023-11-02 13:14 UTC)

<p>I am using an AWS g5.12xlarge instance. This instance has 4 GPUs with a total of 96 GB of memory. Training works very well and all GPUs get utilised (checked using nvidia-smi, however for inference, I get an error.</p>
<p>Unfortunately I wasn’t able to save the stdout last time I tried running inference and it is getting quite expensive to try it out constantly, but the error I got is the same as below from this post (<a href="https://discourse.slicer.org/t/monai-label-cuda-out-of-memory/26161" class="inline-onebox">Monai label. CUDA out of memory</a>) just with different memory values.</p>
<p>RuntimeError: CUDA out of memory. Tried to allocate 4.06 GiB (GPU 0; 24 GiB total capacity; 4.37 GiB already allocated; 2.42 GiB free;<br>
4.51 GiB reserved in total by PyTorch) If reserved memory is &gt;&gt; allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF<br>
[2022-10-29 21:07:39,128] [14748] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:77) - Return code: 1</p>
<p>The images i am training and inferring are on the order of 2gb compressed (in nifti.gz format) and i cannot downsample them as I require this level of detail in the images.</p>
<p>Does anyone have any suggestions for what might fix this issue?</p>

---

## Post #2 by @pieper (2023-11-02 13:45 UTC)

<p>If you haven’t already, be sure to exit the training before running the inference to clear the memory.</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> may have more suggestions on this.</p>

---

## Post #3 by @diazandr3s (2023-11-02 14:03 UTC)

<p>Hi <a class="mention" href="/u/carl_alv">@Carl_alv</a>,</p>
<p>As <a class="mention" href="/u/pieper">@pieper</a> suggested, please make sure training or other processes do not keep the GPUs busy before running inference.</p>
<p>For training, MONAI Label uses <a href="https://pytorch.org/docs/stable/nn.html#module-torch.nn.parallel" rel="noopener nofollow ugc">DistributedDataParallel</a> (DDP).</p>
<p>For inference, you’ll need to make sure the image fits on a single GPU. Can you please comment more on the volume size and whether you are doing any image resampling?</p>
<p>Please let us know</p>

---

## Post #4 by @Carl_alv (2023-11-08 08:37 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a>,</p>
<p>Thanks for getting back to me and apologies for my late response. I have been on break.</p>
<p>The compressed volume is 2.72 gb in a nifti file (nii.gz). This image was upsampled by 2x from a 181.28 MB file. I realise this is quite big but I need this resolution for my work.</p>
<p>I was able to recreate the error message and it is attached below.</p>
<pre><code class="lang-txt">[2023-11-08 08:20:26,087] [4269] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - PRE - Run Transform(s)
[2023-11-08 08:20:26,087] [4269] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - PRE - Input Keys: ['largest_cc', 'device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path']
[2023-11-08 08:27:09,827] [4269] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (LoadImaged): Time: 403.739; image: torch.Size([1024, 1024, 2749])(torch.float32)
[2023-11-08 08:27:12,588] [4269] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureTyped): Time: 2.7612; image: torch.Size([1024, 1024, 2749])(torch.float32)
[2023-11-08 08:27:12,589] [4269] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureChannelFirstd): Time: 0.0002; image: torch.Size([1, 1024, 1024, 2749])(torch.float32)
[2023-11-08 08:27:16,269] [4269] [MainThread] [ERROR] (uvicorn.error:369) - Exception in ASGI application
Traceback (most recent call last):
  File "/opt/conda/lib/python3.10/site-packages/uvicorn/protocols/http/h11_impl.py", line 366, in run_asgi
    result = await app(self.scope, self.receive, self.send)
  File "/opt/conda/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 75, in __call__
    return await self.app(scope, receive, send)
  File "/opt/conda/lib/python3.10/site-packages/fastapi/applications.py", line 269, in __call__
    await super().__call__(scope, receive, send)
  File "/opt/conda/lib/python3.10/site-packages/starlette/applications.py", line 124, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/opt/conda/lib/python3.10/site-packages/starlette/middleware/errors.py", line 184, in __call__
    raise exc
  File "/opt/conda/lib/python3.10/site-packages/starlette/middleware/errors.py", line 162, in __call__
    await self.app(scope, receive, _send)
  File "/opt/conda/lib/python3.10/site-packages/starlette/middleware/cors.py", line 84, in __call__
    await self.app(scope, receive, send)
  File "/opt/conda/lib/python3.10/site-packages/starlette/exceptions.py", line 93, in __call__
    raise exc
  File "/opt/conda/lib/python3.10/site-packages/starlette/exceptions.py", line 82, in __call__
    await self.app(scope, receive, sender)
  File "/opt/conda/lib/python3.10/site-packages/fastapi/middleware/asyncexitstack.py", line 21, in __call__
    raise e
  File "/opt/conda/lib/python3.10/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/opt/conda/lib/python3.10/site-packages/starlette/routing.py", line 670, in __call__
    await route.handle(scope, receive, send)
  File "/opt/conda/lib/python3.10/site-packages/starlette/routing.py", line 266, in handle
    await self.app(scope, receive, send)
  File "/opt/conda/lib/python3.10/site-packages/starlette/routing.py", line 65, in app
    response = await func(request)
  File "/opt/conda/lib/python3.10/site-packages/fastapi/routing.py", line 227, in app
    raw_response = await run_endpoint_function(
  File "/opt/conda/lib/python3.10/site-packages/fastapi/routing.py", line 160, in run_endpoint_function
    return await dependant.call(**values)
  File "/opt/conda/lib/python3.10/site-packages/monailabel/endpoints/infer.py", line 179, in api_run_inference
    return run_inference(background_tasks, model, image, session_id, params, file, label, output)
  File "/opt/conda/lib/python3.10/site-packages/monailabel/endpoints/infer.py", line 161, in run_inference
    result = instance.infer(request)
  File "/opt/conda/lib/python3.10/site-packages/monailabel/interfaces/app.py", line 307, in infer
    result_file_name, result_json = task(request)
  File "/opt/conda/lib/python3.10/site-packages/monailabel/tasks/infer/basic_infer.py", line 297, in __call__
    data = self.run_pre_transforms(data, pre_transforms)
  File "/opt/conda/lib/python3.10/site-packages/monailabel/tasks/infer/basic_infer.py", line 388, in run_pre_transforms
    return run_transforms(data, transforms, log_prefix="PRE", use_compose=False)
  File "/opt/conda/lib/python3.10/site-packages/monailabel/interfaces/utils/transform.py", line 106, in run_transforms
    data = t(data)
  File "/opt/conda/lib/python3.10/site-packages/monai/transforms/spatial/dictionary.py", line 416, in __call__
    d[key] = self.spacing_transform(
  File "/opt/conda/lib/python3.10/site-packages/monai/utils/deprecate_utils.py", line 221, in _wrapper
    return func(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/monai/transforms/spatial/array.py", line 606, in __call__
    data_array = self.sp_resample(
  File "/opt/conda/lib/python3.10/site-packages/monai/utils/deprecate_utils.py", line 221, in _wrapper
    return func(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/monai/transforms/spatial/array.py", line 247, in __call__
    img = convert_to_tensor(data=img, track_meta=get_track_meta(), dtype=_dtype)
  File "/opt/conda/lib/python3.10/site-packages/monai/utils/type_conversion.py", line 149, in convert_to_tensor
    return _convert_tensor(data).to(dtype=dtype, device=device, memory_format=torch.contiguous_format)
  File "/opt/conda/lib/python3.10/site-packages/monai/data/meta_tensor.py", line 268, in __torch_function__
    ret = super().__torch_function__(func, types, args, kwargs)
  File "/opt/conda/lib/python3.10/site-packages/torch/_tensor.py", line 1279, in __torch_function__
    ret = func(*args, **kwargs)
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 21.48 GiB (GPU 0; 22.06 GiB total capacity; 10.74 GiB already allocated; 10.58 GiB free; 10.74 GiB reserved in total by PyTorch) If reserved memory is &gt;&gt; allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

I have also attached the nvidia-smi run below to show you the GPU memory usage.

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 515.65.01    Driver Version: 515.65.01    CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA A10G         On   | 00000000:00:1B.0 Off |                    0 |
|  0%   24C    P0    56W / 300W |  11755MiB / 23028MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA A10G         On   | 00000000:00:1C.0 Off |                    0 |
|  0%   20C    P0    44W / 300W |      2MiB / 23028MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   2  NVIDIA A10G         On   | 00000000:00:1D.0 Off |                    0 |
|  0%   21C    P0    41W / 300W |      2MiB / 23028MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   3  NVIDIA A10G         On   | 00000000:00:1E.0 Off |                    0 |
|  0%   21C    P0    40W / 300W |      2MiB / 23028MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      4269      C   python                          11753MiB |
</code></pre>

---

## Post #5 by @mangotee (2023-11-08 13:15 UTC)

<p>Wow! <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=12" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:" loading="lazy" width="20" height="20"><br>
<code>image: torch.Size([1024, 1024, 2749])</code><br>
This is certainly higher than anything I have worked with so far. I am glad that you got the training to run. What crop/ROI size does your model operate on? E.g. 128x128x128 or higher?<br>
For inference, you may need to run sliding window inference and aggregate the patch-wise predictions into a large tensor that is hosted on the CPU (afaik, inference itself can run on the GPU). Please note that this may be considerably slower than processing fully on the GPU. If speed is not a major concern, I think that <a class="mention" href="/u/diazandr3s">@diazandr3s</a> can give you more detailed instructions on how to achieve that.</p>

---

## Post #6 by @diazandr3s (2023-11-08 20:50 UTC)

<p>Hi <a class="mention" href="/u/carl_alv">@Carl_alv</a>,</p>
<p>This image is huge <img src="https://emoji.discourse-cdn.com/twitter/open_mouth.png?v=12" title=":open_mouth:" class="emoji" alt=":open_mouth:" loading="lazy" width="20" height="20"></p>
<p>Which model are you using here? DeepEdit or the vanilla Segmentation model? Can you please share the command you use to start the MONAI Label server?</p>
<p>In any case, hosting ONLY this volume requires around 21GB of memory - either RAM or GPU memory (1024x1024x2749x8 = ~21GB).</p>
<p>To have an idea of the total memory you’ll need, multiply 21GB by the number of labels.</p>
<p>Both DeepEdit and the Segmentation model predict more than 5 labels, which means more than 100GB of memory is needed - again either RAM or GPU memory.</p>
<p>Hope this helps,</p>

---

## Post #7 by @ag_gan (2023-11-09 01:22 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a> ,<br>
I am also working on this project with <a class="mention" href="/u/carl_alv">@Carl_alv</a> .</p>
<p><strong>- What model are you using here?</strong><br>
We are using the segmentation model, the one that comes in the radiology app.</p>
<p><strong>- The command we are using to start the MONAI Label Server:</strong><br>
<code>monailabel start_server --app radiology --studies &lt;path-to-images&gt; --conf models segmentation</code></p>
<p>We have only been resampling to 2x using the Slicer software because we wanted a higher-resolution label. We didn’t know how to increase the resolution of the label only, so we increased the resolution of the input image, which resulted in the resolution of the label improving as well.</p>
<p>If you have any guidance or advice on how we can go about increasing the resolution of the label that would be helpful.</p>
<p>Thank you in advance!</p>

---

## Post #8 by @diazandr3s (2023-11-09 16:02 UTC)

<p>Hi <a class="mention" href="/u/ag_gan">@ag_gan</a>,</p>
<p>Thanks for the details.</p>
<p>The default Segmentation model predicts 25 regions: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation.py#L37-L62" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation.py#L37-L62</a></p>
<p>Using this volume size you’ll need a huge memory.</p>
<p>My suggestion would be to make a prediction with the original volume size and then postprocess the predicted mask.</p>
<p>Maybe <a class="mention" href="/u/lassoan">@lassoan</a> could comment on how we can use 3DSlicer to smooth a mask?</p>

---

## Post #9 by @lassoan (2023-11-09 16:38 UTC)

<p>After you get your segmentation, you can increase the resolution of your segmentation and smooth the segments (using “Specify geometry”, as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>).</p>

---
