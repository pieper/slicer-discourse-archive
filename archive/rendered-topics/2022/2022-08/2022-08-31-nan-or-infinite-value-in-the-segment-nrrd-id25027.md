# NaN or infinite value in the segment(.nrrd)

**Topic ID**: 25027
**Date**: 2022-08-31
**URL**: https://discourse.slicer.org/t/nan-or-infinite-value-in-the-segment-nrrd/25027

---

## Post #1 by @hourglassnam (2022-08-31 14:21 UTC)

<p>Hello,</p>
<p>I have been trying to train monailabel from scratch with 10 segmentations I created.</p>
<p>I changed the label_values in following 3 files and changed pretrained to false.</p>
<ol>
<li>Anaconda3\Lib\site-packages\monai\apps\deepedit/transforms.py</li>
<li>MONAILabel\monailabel\deepedit\multilabel\transforms.py</li>
<li>MONAILabel\sample-apps\histology\lib\configs\deepedit.py</li>
</ol>
<p>I used *.nrrd format for both of my volume and segments, but this gave me numpy.linalg.LinAlgError where SVD did not converge.</p>
<p>The module was unable to load my segmentations and <a href="https://discourse.slicer.org/u/diazandr3s">@diazandr3s</a> kindly suggested that this could mean I have NaN or infinite value in the segmentations.</p>
<p>I could not figure out how to check the segmentations for those value, so I tried exporting segments to binary labelmap and saving the segments as nifti(*.nii.gz) file.</p>
<p>When I do so, the MONAI label could load my datasets but created another problem(cuDNN error: CUDNN_STATUS_NOT_INITIALIZED).</p>
<p>I checked if my cuda is enabled with following code, which seems to be fine.</p>
<pre><code class="lang-auto">python -c "import torch; print(torch.cuda.is_available())"
True
</code></pre>
<p>I wondered if losing all the metadata while changing the format had caused this problem.</p>
<p>So I relabeled, saved the segments back to *.nrrd and tested training but ended up with the same cuDNN error.</p>
<p>Is there any way to check the segments(*.nrrd) for the NaN and infinite value and drop them?</p>
<p>Have anyone had this kind of problem?</p>
<p>Below is my error log and thank you in advance.</p>
<pre><code class="lang-auto">[2022-08-31 18:07:30,056] [44720] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:696) - Engine run resuming from iteration 0, epoch 0 until 50 epochs
2022-08-31 18:07:37,964 - INFO - Number of simulated clicks: 5
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [654,0,0], thread: [32,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [654,0,0], thread: [33,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [654,0,0], thread: [34,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [555,0,0], thread: [32,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [785,0,0], thread: [32,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [785,0,0], thread: [33,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [554,0,0], thread: [32,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1108,0,0], thread: [32,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1108,0,0], thread: [33,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1108,0,0], thread: [34,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1108,0,0], thread: [35,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1108,0,0], thread: [36,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1108,0,0], thread: [37,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1044,0,0], thread: [32,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1044,0,0], thread: [33,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1044,0,0], thread: [34,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1044,0,0], thread: [35,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1044,0,0], thread: [36,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1061,0,0], thread: [37,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1061,0,0], thread: [38,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1061,0,0], thread: [39,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1093,0,0], thread: [37,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1093,0,0], thread: [38,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1093,0,0], thread: [39,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1431,0,0], thread: [32,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1431,0,0], thread: [33,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1431,0,0], thread: [34,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [1431,0,0], thread: [35,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [459,0,0], thread: [26,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
C:/w/b/windows/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:312: block: [459,0,0], thread: [27,0,0] Assertion `idx_dim &gt;= 0 &amp;&amp; idx_dim &lt; index_size &amp;&amp; "index out of bounds"` failed.
[2022-08-31 18:07:38,965] [44720] [MainThread] [ERROR] (ignite.engine.engine.SupervisedTrainer:853) - Current run is terminating due to exception: cuDNN error: CUDNN_STATUS_NOT_INITIALIZED
[2022-08-31 18:07:38,965] [44720] [MainThread] [ERROR] (ignite.engine.engine.SupervisedTrainer:178) - Exception: cuDNN error: CUDNN_STATUS_NOT_INITIALIZED
Traceback (most recent call last):
File "C:\ProgramData\Anaconda3\lib\site-packages\ignite\engine\engine.py", line 840, in _run_once_on_dataset
self.state.output = self._process_function(self, self.state.batch)
File "C:\ProgramData\Anaconda3\lib\site-packages\monai\apps\deepedit\interaction.py", line 100, in __call__
return engine._iteration(engine, batchdata)
File "C:\ProgramData\Anaconda3\lib\site-packages\monai\engines\trainer.py", line 211, in _iteration
engine.scaler.scale(engine.state.output[Keys.LOSS]).backward()
File "C:\ProgramData\Anaconda3\lib\site-packages\torch\_tensor.py", line 255, in backward
torch.autograd.backward(self, gradient, retain_graph, create_graph, inputs=inputs)
File "C:\ProgramData\Anaconda3\lib\site-packages\torch\autograd\__init__.py", line 147, in backward
Variable._execution_engine.run_backward(
RuntimeError: cuDNN error: CUDNN_STATUS_NOT_INITIALIZED
[2022-08-31 18:07:38,978] [44720] [MainThread] [ERROR] (ignite.engine.engine.SupervisedTrainer:782) - Engine run is terminating due to exception: cuDNN error: CUDNN_STATUS_NOT_INITIALIZED
[2022-08-31 18:07:38,978] [44720] [MainThread] [ERROR] (ignite.engine.engine.SupervisedTrainer:178) - Exception: cuDNN error: CUDNN_STATUS_NOT_INITIALIZED
</code></pre>

---
