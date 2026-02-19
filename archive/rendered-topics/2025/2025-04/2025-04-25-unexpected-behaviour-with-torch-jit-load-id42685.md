---
topic_id: 42685
title: "Unexpected Behaviour With Torch Jit Load"
date: 2025-04-25
url: https://discourse.slicer.org/t/42685
---

# Unexpected behaviour with torch.jit.load

**Topic ID**: 42685
**Date**: 2025-04-25
**URL**: https://discourse.slicer.org/t/unexpected-behaviour-with-torch-jit-load/42685

---

## Post #1 by @ciro.raggio (2025-04-25 10:50 UTC)

<p>Hi everyone!</p>
<p>I’m trying to use a custom pre-trained torch model in a scripted module, but I encountered a problem that I couldn’t fix. Following the guide “<a href="https://www.kitware.com/deploying-your-monai-machine-learning-model-within-3d-slicer/" rel="noopener nofollow ugc">Deploying your MONAI machine learning model within 3D Slicer</a>”, I exported my model with <code>torch.jit.script</code>, and I am now trying to reload it using <code>torch.load</code>.<br>
When I try to load the model in a scripted module, the <code>MemoryError: std::bad_alloc</code> error is generated. Here the detailed error:</p>
<pre><code class="lang-auto">[...]
    self.model = torch.jit.load(modelPath)
  File "/home/yyy/Slicer-5.8.0-linux-amd64/lib/Python/lib/python3.9/site-packages/torch/jit/_serialization.py", line 162, in load
    cpp_module = torch._C.import_ir_module(cu, str(f), map_location, _extra_files, _restore_shapes)  # type: ignore[call-arg]
MemoryError: std::bad_alloc
</code></pre>
<p>The same error is generated if I repeat the operation inside the Python terminal within Slicer.</p>
<p>However, if I run PythonSlicer in a terminal using: <code>[slicer_path]/Slicer --launch PythonSlicer</code> and I run: <code>torch.jit.load(modelPath)</code>, the model loads <strong>without any problems</strong>.</p>
<p>I have tried exporting the model both as a zip file and as a pt file.<br>
I have enough memory to allocate the model.<br>
I’m working on Ubuntu 24.10. The Slicer version is <code>5.8.1</code>, the model was exported using torch <code>2.1.0</code>. The torch version in Slicer is <code>2.1.0</code>.</p>
<p>What could be the load within Slicer or the scripted module?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @ciro.raggio (2025-07-30 16:24 UTC)

<p>Hi again!</p>
<p>I’m following up on this issue as I haven’t been able to resolve it yet. I’m hoping that someone in the community might have more insight into it. The problem appears to be specific to loading TorchScript models within Slicer’s embedded GUI rather than its CLI backend.</p>
<p>I tried exporting a dummy model using this code to confirm that the problem was not with my model or memory.</p>
<pre data-code-wrap="python"><code class="lang-python">import torch
import torch.nn as nn

class DummyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(10, 20),
            nn.ReLU(),
            nn.Linear(20, 1)
        )

    def forward(self, x):
        return self.net(x)

model = DummyModel()
model.eval()
model.cpu()

example_input = torch.randn(1, 10)
traced_model = torch.jit.script(model)
traced_model.save("dummy_model.pt")

</code></pre>
<p>Once again, I got the same error message:</p>
<pre data-code-wrap="python"><code class="lang-python">File "/home/yyy/Slicer-5.8.0-linux-amd64/lib/Python/lib/python3.9/site-packages/torch/jit/_serialization.py", line 161, in load
    cpp_module = torch._C.import_ir_module(cu, str(f), map_location, _extra_files)
MemoryError: std::bad_alloc
</code></pre>
<p>Could someone replicate and confirm the error? Does anyone have another solution to recommend?</p>

---

## Post #3 by @ciro.raggio (2025-07-31 09:38 UTC)

<p>The problem has not been solved and the incompatibility with Torch JIT remains. In the meantime, however, I have found a workaround using <a href="https://onnxruntime.ai/docs/" rel="noopener nofollow ugc">onnxruntime</a>, which I used after exporting the Torch model with <code>torch.onnx.export</code>.</p>

---
