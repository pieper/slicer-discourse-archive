# Issue Loading TensorFlow .h5 Model in 3D Slicer – "Unknown Layer: 'TensorFlowOpLayer

**Topic ID**: 42583
**Date**: 2025-04-16
**URL**: https://discourse.slicer.org/t/issue-loading-tensorflow-h5-model-in-3d-slicer-unknown-layer-tensorflowoplayer/42583

---

## Post #1 by @software (2025-04-16 10:39 UTC)

<p>Hi everyone,</p>
<p>I’m currently working on integrating an <strong>acute stroke detection model</strong> (originally trained in TensorFlow and saved as a <code>.h5</code> file) into the <strong>3D Slicer environment</strong>.</p>
<p>I tried running it within my Slicer module, but I’m getting the following error:<br>
Processing failed: Error loading lesion model: Unknown layer: ‘TensorFlowOpLayer’. Please ensure you are using a keras.utils.custom_object_scope and that this object is included in the scope.<br>
See: <a href="https://www.tensorflow.org/guide/keras/save_and_serialize#registering_the_custom_object" rel="noopener nofollow ugc">https://www.tensorflow.org/guide/keras/save_and_serialize#registering_the_custom_object</a><br>
…<br>
ValueError: Unknown layer: ‘TensorFlowOpLayer’<br>
We <strong>only have the <code>.h5</code> file</strong>, and unfortunately, we don’t have access to the model’s architecture code. I’ve looked into converting it to PyTorch, but as far as I know, it’s not feasible with just the <code>.h5</code> file alone.</p>
<h3><a name="p-124373-my-questions-1" class="anchor" href="#p-124373-my-questions-1" aria-label="Heading link"></a>My Questions:</h3>
<ul>
<li>Is this a <strong>limitation of 3D Slicer’s Python environment</strong> (maybe TensorFlow isn’t fully supported)?</li>
<li>Or is it strictly a <strong>TensorFlow model serialization issue</strong>, requiring access to the original custom layer definitions?</li>
<li>Is there a workaround for this inside Slicer (e.g., registering custom layers or running externally)?</li>
</ul>
<p>Any help or guidance would be really appreciated. Thanks in advance!</p>

---

## Post #2 by @pieper (2025-04-16 13:49 UTC)

<p>That sounds like a tensorflow version issue.</p>

---

## Post #3 by @software (2025-04-16 14:43 UTC)

<p>Sir, is it possible to use a TensorFlow <code>.h5</code> model in 3D Slicer?</p>

---

## Post #4 by @pieper (2025-04-16 15:00 UTC)

<p>An h5 file is just a container, like a zip file and tensorflow is a utility, so you can use both in Slicer but you need to know the software context to know if you can use it or not.  I’m not a tensorflow expert, but the “unknown layer” looks like something that would happen if you have a version mis-match between the creator or the h5 file and the version of tensorflow you are tying to use.</p>
<p>These days people mostly use PyTorch for medical imaging applications, so probably you can study the original design and other example models and port it and re-train.</p>

---

## Post #5 by @muratmaga (2025-04-16 18:29 UTC)

<aside class="quote no-group" data-username="software" data-post="1" data-topic="42583">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/software/48/79627_2.png" class="avatar"> software:</div>
<blockquote>
<p><strong>limitation of 3D Slicer’s Python environment</strong> (maybe TensorFlow isn’t fully supported</p>
</blockquote>
</aside>
<p>Tensorflow is notoriously difficult to get it installed and working even in a normal python environment. That’s probably the number one reason people migrate to pytorch even though tf has been around longer and probably was more mature at the time.</p>
<p>Last I checked, tf worked fine in Slicer. But I would suggest trying to make it work in normal python first to rule out other issues and then try in Slicer. Having said that, I agree with <a class="mention" href="/u/pieper">@pieper</a>. i don’t think this is an installation issue, but a model/version issue.</p>
<p>You might have better support if you ask this on tensorflow forum.</p>

---

## Post #6 by @software (2025-04-17 09:38 UTC)

<p>The pretrained model I’m using is from the open-source GitHub repo <a href="https://github.com/Chin-Fu-Liu/Acute-stroke_Detection_Segmentation" rel="noopener nofollow ugc"><strong>Chin-Fu-Liu / Acute-stroke_Detection_Segmentation</strong></a>. According to the requirements, it’s built using <strong>TensorFlow 2.0.0</strong> with <strong>Python 3.7</strong>.</p>
<p>I’ve set up a virtual environment in <strong>VS Code</strong> with the exact same dependencies:<br>
pip install tensorflow==2.0.0<br>
pip install tensorflow-gpu==2.0.0<br>
pip install numpy nibabel scipy scikit-image scikit-learn<br>
pip install dipy==1.4.0<br>
pip install h5py==2.10.0<br>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> With this setup, the model loads and runs <strong>perfectly fine</strong>.<br>
So now I’m wondering — is this issue specific to <strong>Slicer’s Python environment</strong>, or do I need to somehow <strong>register custom objects</strong> manually in the code?</p>
<p>Any suggestions on how to align Slicer’s environment to match the one where it’s working would be a huge help. <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @jamesobutler (2025-04-17 12:22 UTC)

<aside class="quote no-group" data-username="software" data-post="6" data-topic="42583">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/software/48/79627_2.png" class="avatar"> software:</div>
<blockquote>
<p>I’ve set up a virtual environment in <strong>VS Code</strong></p>
</blockquote>
</aside>
<p>I would suggest repeating this effort outside of Slicer, but using Python 3.9. This version of Python is what Slicer is currently using so if you can get ADS working with it outside of Slicer using Python 3.9 then you can then possibly get it working within Slicer’s environment.</p>

---

## Post #8 by @software (2025-04-17 13:16 UTC)

<p>Sir, I have tested the model in a new environment with Python 3.9, and it is working fine outside of Slicer in a regular Python environment. The following requirements were used:<br>
numpy==1.19.5<br>
scipy==1.7.3<br>
h5py==3.1.0<br>
nibabel==3.2.1<br>
tensorflow==2.7.0<br>
scikit-image==0.18.1<br>
scikit-learn==0.24.1<br>
dipy==1.5.0</p>

---

## Post #9 by @jamesobutler (2025-04-17 13:41 UTC)

<p>Based on the original error you ran into, I think it is likely tensorflow being an issue in Slicer. However, I don’t think many in this community use Tensorflow as it is almost exclusively PyTorch usage. You could try converting the keras h5 model to an onnx object with something like <a href="https://github.com/onnx/tensorflow-onnx" class="inline-onebox" rel="noopener nofollow ugc">GitHub - onnx/tensorflow-onnx: Convert TensorFlow, Keras, Tensorflow.js and Tflite models to ONNX</a>.</p>
<p>Based on the specific ADS model being GPL, there likely won’t be a lot of additional support here based on the type of discussion at:</p>
<aside class="quote quote-modified" data-post="1" data-topic="42340">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/software/48/79627_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/packaging-acute-stroke-detection-module-for-slicer/42340">Packaging Acute Stroke Detection Module for Slicer</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Repository: <a href="https://github.com/Chin-Fu-Liu/Acute-stroke_Detection_Segmentation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Chin-Fu-Liu/Acute-stroke_Detection_Segmentation</a> 
Problem: I want to package the Acute Stroke Detection and Segmentation (ADS) module for 3D Slicer with pre-trained models. 
Specific Challenges: 

Including pre-trained deep learning models in the Slicer extension
Managing specific Python library dependencies (TensorFlow, h5py, etc.)
Ensuring the module works across different systems

Key Questions: 

What’s the recommended way to include machine learning models in a Slicer ex…
  </blockquote>
</aside>


---

## Post #10 by @muratmaga (2025-04-17 17:03 UTC)

<aside class="quote no-group" data-username="software" data-post="8" data-topic="42583">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/software/48/79627_2.png" class="avatar"> software:</div>
<blockquote>
<p>numpy==1.19.5<br>
scipy==1.7.3<br>
h5py==3.1.0<br>
nibabel==3.2.1<br>
tensorflow==2.7.0<br>
scikit-image==0.18.1<br>
scikit-learn==0.24.1<br>
dipy==1.5.0</p>
</blockquote>
</aside>
<p>ok. Try installing these packages using the exact versions in Slicer. Does that work?</p>

---

## Post #11 by @muratmaga (2025-04-17 17:18 UTC)

<p>For example on my mac with Slicer 5.8.1, tensorflow==2.7.0 supposedly installs, but then bring this error message when I import it:</p>
<pre><code class="lang-auto">&gt;&gt; pip_install('tensorflow==2.7.0')
Collecting tensorflow==2.7.0
  Downloading tensorflow-2.7.0-cp39-cp39-macosx_10_11_x86_64.whl.metadata (2.9 kB)
Requirement already satisfied: numpy&gt;=1.14.5 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.26.4)
Collecting absl-py&gt;=0.4.0 (from tensorflow==2.7.0)
  Downloading absl_py-2.2.2-py3-none-any.whl.metadata (2.6 kB)
Collecting astunparse&gt;=1.6.0 (from tensorflow==2.7.0)
  Downloading astunparse-1.6.3-py2.py3-none-any.whl.metadata (4.4 kB)
Collecting libclang&gt;=9.0.1 (from tensorflow==2.7.0)
  Downloading libclang-18.1.1-py2.py3-none-macosx_10_9_x86_64.whl.metadata (5.2 kB)
Collecting flatbuffers&lt;3.0,&gt;=1.12 (from tensorflow==2.7.0)
  Downloading flatbuffers-2.0.7-py2.py3-none-any.whl.metadata (872 bytes)
Collecting google-pasta&gt;=0.1.1 (from tensorflow==2.7.0)
  Downloading google_pasta-0.2.0-py3-none-any.whl.metadata (814 bytes)
Collecting h5py&gt;=2.9.0 (from tensorflow==2.7.0)
  Downloading h5py-3.13.0-cp39-cp39-macosx_10_9_x86_64.whl.metadata (2.5 kB)
Collecting keras-preprocessing&gt;=1.1.1 (from tensorflow==2.7.0)
  Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl.metadata (1.9 kB)
Collecting opt-einsum&gt;=2.3.2 (from tensorflow==2.7.0)
  Downloading opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
Collecting protobuf&gt;=3.9.2 (from tensorflow==2.7.0)
  Downloading protobuf-6.30.2-cp39-abi3-macosx_10_9_universal2.whl.metadata (593 bytes)
Requirement already satisfied: six&gt;=1.12.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.16.0)
Collecting termcolor&gt;=1.1.0 (from tensorflow==2.7.0)
  Downloading termcolor-3.0.1-py3-none-any.whl.metadata (6.1 kB)
Requirement already satisfied: typing-extensions&gt;=3.6.6 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from tensorflow==2.7.0) (4.12.1)
Requirement already satisfied: wheel&lt;1.0,&gt;=0.32.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from tensorflow==2.7.0) (0.43.0)
Requirement already satisfied: wrapt&gt;=1.11.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.16.0)
Collecting gast&lt;0.5.0,&gt;=0.2.1 (from tensorflow==2.7.0)
  Downloading gast-0.4.0-py3-none-any.whl.metadata (1.1 kB)
Collecting tensorboard~=2.6 (from tensorflow==2.7.0)
  Downloading tensorboard-2.19.0-py3-none-any.whl.metadata (1.8 kB)
Collecting tensorflow-estimator&lt;2.8,~=2.7.0rc0 (from tensorflow==2.7.0)
  Downloading tensorflow_estimator-2.7.0-py2.py3-none-any.whl.metadata (1.2 kB)
Collecting keras&lt;2.8,&gt;=2.7.0rc0 (from tensorflow==2.7.0)
  Downloading keras-2.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting tensorflow-io-gcs-filesystem&gt;=0.21.0 (from tensorflow==2.7.0)
  Downloading tensorflow_io_gcs_filesystem-0.37.1-cp39-cp39-macosx_10_14_x86_64.whl.metadata (14 kB)
Collecting grpcio&lt;2.0,&gt;=1.24.3 (from tensorflow==2.7.0)
  Downloading grpcio-1.71.0-cp39-cp39-macosx_10_14_universal2.whl.metadata (3.8 kB)
Collecting markdown&gt;=2.6.8 (from tensorboard~=2.6-&gt;tensorflow==2.7.0)
  Downloading markdown-3.8-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: packaging in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from tensorboard~=2.6-&gt;tensorflow==2.7.0) (24.0)
Requirement already satisfied: setuptools&gt;=41.0.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from tensorboard~=2.6-&gt;tensorflow==2.7.0) (70.0.0)
Collecting tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 (from tensorboard~=2.6-&gt;tensorflow==2.7.0)
  Downloading tensorboard_data_server-0.7.2-py3-none-macosx_10_9_x86_64.whl.metadata (1.1 kB)
Collecting werkzeug&gt;=1.0.1 (from tensorboard~=2.6-&gt;tensorflow==2.7.0)
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting importlib-metadata&gt;=4.4 (from markdown&gt;=2.6.8-&gt;tensorboard~=2.6-&gt;tensorflow==2.7.0)
  Downloading importlib_metadata-8.6.1-py3-none-any.whl.metadata (4.7 kB)
Collecting MarkupSafe&gt;=2.1.1 (from werkzeug&gt;=1.0.1-&gt;tensorboard~=2.6-&gt;tensorflow==2.7.0)
  Downloading MarkupSafe-3.0.2-cp39-cp39-macosx_10_9_universal2.whl.metadata (4.0 kB)
Collecting zipp&gt;=3.20 (from importlib-metadata&gt;=4.4-&gt;markdown&gt;=2.6.8-&gt;tensorboard~=2.6-&gt;tensorflow==2.7.0)
  Using cached zipp-3.21.0-py3-none-any.whl.metadata (3.7 kB)
Downloading tensorflow-2.7.0-cp39-cp39-macosx_10_11_x86_64.whl (207.1 MB)

Downloading absl_py-2.2.2-py3-none-any.whl (135 kB)

Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Downloading flatbuffers-2.0.7-py2.py3-none-any.whl (26 kB)
Downloading gast-0.4.0-py3-none-any.whl (9.8 kB)
Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)

Downloading grpcio-1.71.0-cp39-cp39-macosx_10_14_universal2.whl (11.3 MB)

Downloading h5py-3.13.0-cp39-cp39-macosx_10_9_x86_64.whl (3.4 MB)

Downloading keras-2.7.0-py2.py3-none-any.whl (1.3 MB)

Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)

Downloading libclang-18.1.1-py2.py3-none-macosx_10_9_x86_64.whl (26.5 MB)

Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)

Downloading protobuf-6.30.2-cp39-abi3-macosx_10_9_universal2.whl (417 kB)

Downloading tensorboard-2.19.0-py3-none-any.whl (5.5 MB)

Downloading tensorflow_estimator-2.7.0-py2.py3-none-any.whl (463 kB)

Downloading tensorflow_io_gcs_filesystem-0.37.1-cp39-cp39-macosx_10_14_x86_64.whl (2.5 MB)

Downloading termcolor-3.0.1-py3-none-any.whl (7.2 kB)
Downloading markdown-3.8-py3-none-any.whl (106 kB)

Downloading tensorboard_data_server-0.7.2-py3-none-macosx_10_9_x86_64.whl (4.8 MB)

Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)

Downloading importlib_metadata-8.6.1-py3-none-any.whl (26 kB)
Downloading MarkupSafe-3.0.2-cp39-cp39-macosx_10_9_universal2.whl (14 kB)
Using cached zipp-3.21.0-py3-none-any.whl (9.6 kB)
Installing collected packages: tensorflow-estimator, libclang, keras, flatbuffers, zipp, termcolor, tensorflow-io-gcs-filesystem, tensorboard-data-server, protobuf, opt-einsum, MarkupSafe, keras-preprocessing, h5py, grpcio, google-pasta, gast, astunparse, absl-py, werkzeug, importlib-metadata, markdown, tensorboard, tensorflow
Successfully installed MarkupSafe-3.0.2 absl-py-2.2.2 astunparse-1.6.3 flatbuffers-2.0.7 gast-0.4.0 google-pasta-0.2.0 grpcio-1.71.0 h5py-3.13.0 importlib-metadata-8.6.1 keras-2.7.0 keras-preprocessing-1.1.2 libclang-18.1.1 markdown-3.8 opt-einsum-3.4.0 protobuf-6.30.2 tensorboard-2.19.0 tensorboard-data-server-0.7.2 tensorflow-2.7.0 tensorflow-estimator-2.7.0 tensorflow-io-gcs-filesystem-0.37.1 termcolor-3.0.1 werkzeug-3.1.3 zipp-3.21.0
&gt;&gt;&gt; import tensorflow as tf
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/__init__.py", line 41, in &lt;module&gt;
    from tensorflow.python.tools import module_util as _module_util
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/python/__init__.py", line 41, in &lt;module&gt;
    from tensorflow.python.eager import context
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/python/eager/context.py", line 33, in &lt;module&gt;
    from tensorflow.core.framework import function_pb2
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/core/framework/function_pb2.py", line 16, in &lt;module&gt;
    from tensorflow.core.framework import attr_value_pb2 as tensorflow_dot_core_dot_framework_dot_attr__value__pb2
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/core/framework/attr_value_pb2.py", line 16, in &lt;module&gt;
    from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/core/framework/tensor_pb2.py", line 16, in &lt;module&gt;
    from tensorflow.core.framework import resource_handle_pb2 as tensorflow_dot_core_dot_framework_dot_resource__handle__pb2
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/core/framework/resource_handle_pb2.py", line 16, in &lt;module&gt;
    from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/tensorflow/core/framework/tensor_shape_pb2.py", line 36, in &lt;module&gt;
    _descriptor.FieldDescriptor(
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/google/protobuf/descriptor.py", line 621, in __new__
    _message.Message._CheckCalledFromGeneratedFile()
TypeError: Descriptors cannot be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc &gt;= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
</code></pre>
<p>You will will have to work one by one until you can find the right combination of packages that will work with tensorflow 2.7.0, which is a fairly old version…</p>

---

## Post #12 by @software (2025-04-18 07:15 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="11" data-topic="42583">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>Downgrade the protobuf package to 3.20.x or lower</code></p>
</blockquote>
</aside>
<p>try to install protobuf  3.20.0</p>

---
