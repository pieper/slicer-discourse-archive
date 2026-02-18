# Building custom module inside 3D slicer that contains pre trained models (built in tensorflow)

**Topic ID**: 27929
**Date**: 2023-02-20
**URL**: https://discourse.slicer.org/t/building-custom-module-inside-3d-slicer-that-contains-pre-trained-models-built-in-tensorflow/27929

---

## Post #1 by @rahulhere (2023-02-20 13:45 UTC)

<p>Hi All,</p>
<p>I have a few pre trained medical image segmentation models built in tensorflow. I would like to build modules which I can use to test their segmentation prediction on scans that I import into 3D slicer. I know there are extensions available like Monai, but I would want to build a module which can use my trained model (stored as a h5) and generate predictions within 3D slicer itself by connecting to GPU.</p>
<p>I tried searching within the community here, but i still do not have an idea of how to go about building this<br>
Could anyone please point to any resources or tutorial for this purpose?</p>

---

## Post #2 by @pieper (2023-02-20 15:44 UTC)

<p>You can start with the general programming tutorials linked from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">the web site</a>.  You can pip install tensorflow and move data back and forth using numpy arrays.  There are lots of example scripts available to learn from.  It sounds like you searched but didn’t find them - maybe we need to make this more obvious?  Or did you find these and still thought there should be more?</p>

---

## Post #3 by @rahulhere (2023-02-23 10:49 UTC)

<p>Thanks for the reply <a class="mention" href="/u/pieper">@pieper</a>. I did go through the resources and I did find the right resources.</p>
<p>However I still need some help. Thanks to <a class="mention" href="/u/lassoan">@lassoan</a> CLI blur image code, I was able to build a custom module myself.<br>
Here is my workflow</p>
<ol>
<li>Import a scan into 3D slicer</li>
<li>Pass the scan via argument as an input to my segmentation prediction python file
<ol>
<li>The segmentation python file has my pre-trained model (in tensorflow) with which I generate<br>
segmentations</li>
</ol>
</li>
<li>I take the segmentations and write it back to the slicer as a label map</li>
</ol>
<p>This workflow works and I am able to generate segmentations. However the time taken to generate predictions are way longer. I think it is because the python script is getting executed on a CPU and not a GPU. I tried to initialize and set up GPU within the python script using the below code</p>
<pre><code class="lang-auto">import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = '0' 
</code></pre>
<p>I also tried to check if the GPU is detected using the below code and I get the output “Not running on GPU” from it</p>
<pre><code class="lang-auto">import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)
else:
    print("Not running on GPU ")
</code></pre>
<p>Could you please help me with this ? Thanks a lot in advance</p>

---

## Post #4 by @pieper (2023-02-23 14:36 UTC)

<p>It looks like you’ve got a cuda installation problem or maybe you  didn’t get the right version of tensorflow for the cuda driver you have.  This isn’t really a Slicer issue, so you should find lots of information about this with some searching.  You can use the PythonSlicer interpreter, for testing, which is just a normal python build without the Slicer app.</p>

---

## Post #5 by @rahulhere (2023-02-23 14:46 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. But in terms of the process, all I want to do is, load a scan in slicer, use my tensorflow model to generate segmentations, get those back to slicer and overlay them with the scan. Apart from the workflow that I followed, do you think there is any other efficient way to do this ?</p>

---

## Post #6 by @pieper (2023-02-23 14:59 UTC)

<p>There are lots of options. If you have another python environment where tensorflow detects the GPU and runs faster then you can execute that with <code>slicer.util.launchConsoleProcess(args)</code> and read the results.  Or you could use a server like MONAI Label does.  Or you could use <code>slicerio</code> from an external process to send segmentations to Slicer.</p>

---
