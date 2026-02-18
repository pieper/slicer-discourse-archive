# Error 'tf' not found

**Topic ID**: 10442
**Date**: 2020-02-26
**URL**: https://discourse.slicer.org/t/error-tf-not-found/10442

---

## Post #1 by @tkt8 (2020-02-26 14:44 UTC)

<p>I have installed tensorflow in the night build. And I am importing tensorflow as tf in my code. But I get an error stating “tf” not found. This is solved by importing tensorflow as tf in the python interpreter. Can you please tell me what I am doing wrong?</p>
<p>Thanks,<br>
Tanvi</p>

---

## Post #2 by @ungi (2020-02-26 17:17 UTC)

<p>Did you install TensorFlow with this command in a recent version of Slicer?<br>
<code>pip_install('tensorflow')</code><br>
Then, you should be able to import and use TensorFlow.<br>
We experienced an error recently on Windows, and the solution was to install Visual Studio on the same computer. Apparently, the Windows version of TensorFlow requires something from Visual Studio that it doesn’t package automatically.</p>

---

## Post #3 by @tkt8 (2020-02-26 17:25 UTC)

<p>I had installed tensorflow using slicer.util.pip_install(“tensorflow”). And i am using a Linux machine.<br>
I tried using the pip_install command but the same issue is there where I still have to manually import tensorflow in the python interpreter rather than it automatically being done in *.py file</p>

---

## Post #4 by @ungi (2020-02-26 17:53 UTC)

<p>If your .py file is a module for 3D Slicer, and you have installed TensorFlow with the slicer.util.pip_install() command, then you can just add import tensorflow at the beginning of your .py file, and that should work.</p>

---

## Post #5 by @tkt8 (2020-02-28 19:34 UTC)

<p>Traceback (most recent call last):<br>
File “/home/tpk11/Slicer_MimickNet/MimickNet/MimickNet.py”, line 118, in onApplyButton<br>
logic.run(self.inputSelector.currentNode(),self.modelPathEdit.currentPath)<br>
File “/home/tpk11/Slicer_MimickNet/MimickNet/MimickNet.py”, line 168, in run<br>
model = tf.keras.models.load_model(path)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/saving/save.py”, line 146, in load_model<br>
return hdf5_format.load_model_from_hdf5(filepath, custom_objects, compile)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/saving/hdf5_format.py”, line 168, in load_model_from_hdf5<br>
custom_objects=custom_objects)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/saving/model_config.py”, line 55, in model_from_config<br>
return deserialize(config, custom_objects=custom_objects)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/layers/serialization.py”, line 106, in deserialize<br>
printable_module_name=‘layer’)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/utils/generic_utils.py”, line 303, in deserialize_keras_object<br>
list(custom_objects.items())))<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/engine/network.py”, line 937, in from_config<br>
config, custom_objects)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/engine/network.py”, line 1903, in reconstruct_from_config<br>
process_node(layer, node_data)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/engine/network.py”, line 1851, in process_node<br>
output_tensors = layer(input_tensors, **kwargs)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/engine/base_layer.py”, line 773, in <strong>call</strong><br>
outputs = call_fn(cast_inputs, *args, **kwargs)<br>
File “/scratch/tpk11/Slicer/lib/Python/lib/python3.6/site-packages/tensorflow_core/python/keras/layers/core.py”, line 846, in call<br>
result = self.function(inputs, **kwargs)<br>
File “”, line 2, in custom_pad<br>
NameError: name ‘tf’ is not defined</p>
<p>This is the error i get. Tensorflow is being imported in the module .py file</p>

---
