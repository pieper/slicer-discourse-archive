# Multi-GPU inference with MONAILabel

**Topic ID**: 37650
**Date**: 2024-08-01
**URL**: https://discourse.slicer.org/t/multi-gpu-inference-with-monailabel/37650

---

## Post #1 by @xiang_yao (2024-08-01 02:09 UTC)

<p>May I ask if multi GPUs inference can be used in Windows or Linux systems? Currently, due to data size issues, it is evident that monailabel infers data in memory, i.e. CPU, without utilizing CUDA acceleration.</p>
<p>If I have multiple 4090 cards in one computer, how can I make them participate in parallel computation for inference?</p>

---

## Post #2 by @muratmaga (2024-08-02 01:28 UTC)

<p>If you setup CUDA environment correctly, then MonaiLabel will use GPU. It is not using is a sign that torch is not detecting your GPU and driver for some reason. You should follow the pyTorch’s troubleshooting steps.</p>
<p>As for using multiple GPUs for inferring, I don;t think that’s common use case. Inference with a powerful GPU like 4090 is very fast, and shouldn’t be needed.</p>

---

## Post #3 by @curtislisle (2024-08-04 01:28 UTC)

<p>The question was how to use multiple 4090 cards for inferencing with MONAILabel. The answer is not a simple one: Depending on the application selected, MONAILabel can be serving different models. Whether a model uses single or multiple GPUs is up to the way each particular model was coded and is not a configurable parameter of the MONAILabel serving application. So you would have to modify the code in the particular model(s) that you are using in order to take advantage of multiple GPUs. If you want to pursue this, I suggest further questions will become more of an issue between you and the MONAILabel creators/maintainers at NVIDIA instead of this community. I don’t recommend spending time parallelizing the inference execution. Instead, you could take advantage of multiple GPUs if you are training a new model, since this is a more computationally expensive task.</p>

---

## Post #4 by @diazandr3s (2024-08-05 10:03 UTC)

<p>Good answers already.</p>
<p><a class="mention" href="/u/xiang_yao">@xiang_yao</a> could you please expand on the use case? How big is the image and which model are you using in MONAI Label?</p>

---
