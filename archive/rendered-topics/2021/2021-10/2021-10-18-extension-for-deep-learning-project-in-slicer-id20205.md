# Extension for deep learning project in Slicer

**Topic ID**: 20205
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/extension-for-deep-learning-project-in-slicer/20205

---

## Post #1 by @AMK (2021-10-18 12:21 UTC)

<p>Hi,</p>
<p>I am trying to develop a deep learning based module, whereby a few clicks would allow to segment the CT volume. I am using the nnUNET for my implementation, which is basically a UNET with fixed hyperparameter and this architecture has been quite successful in various medical decathlon challenges/competition. The code flow works for my purpose in normal Python outside Slicer. I have read about the different options available in the Slicer forum, such as using Pytorch directly (presented in PW35), or going with MONAI framework. But I am struggling a bit with the workflow as some of the options available confuses me and where they need to come into the picture.</p>
<p>From what I have understood during my reading, the workflow pipeline would be something like following:</p>
<ol>
<li>
<p>Convert the CT volume data images into the format compatible with the nnUNET.</p>
</li>
<li>
<p>Maually segement some data into the required segments using the Slicer. Divide these data into training, testing and validation dataset.</p>
</li>
<li>
<p>Now I can train the network in the Slicer itself using the Pytorch extension provided in PW-35 in the command line interface. Or more suitably I can transfer these dataset outside Slicer and do all the AI stuff outside Slicer.</p>
</li>
<li>
<p>After doing all these AI stuff, I would create an extension by following the tuitorials available for creating simple extension. These extension would basically present a few buttons which would basically perform model inferance and segment new data, after these new data have been converted to the format in which they were trained.</p>
</li>
</ol>
<p>Now my questions are:</p>
<ol>
<li>Am I right about my workflow or am I forgetting somethings?</li>
<li>Maybe I can work without using MONAI. From what I understand MONAI is a framework which is being used in the medical imaging community to create a uniformity in the workflow and provides pre-built functions.</li>
<li>Are there any available opensource deep learning project related to Slicer or some form of documentation or workflow etc for creating these extensions.</li>
</ol>
<p>Best regards,<br>
Khan</p>

---

## Post #2 by @ungi (2021-10-18 14:02 UTC)

<ol>
<li>
<p>I think you are mostly right.</p>
</li>
<li>
<p>MONAI contains useful tools for AI training with PyTorch, especially for 3D image segmentation. Once you have trained your UNet, you will need to decide how to deploy them in Slicer. Some people prefer running trained models on servers, so users don’t need to install an AI environment. But it’s also easy to install PyTorch or TensorFlow in Slicer’s python. If a model is already trained, it usually runs fine on all computers even without GPU. I personally use this second solution so I can run my trained AI modules without internet connection.</p>
</li>
<li>
<p>I think the best AI tutorials are outside the Slicer community, sometimes even outside the medical imaging community. I recommend exporting your images from Slicer, then forget about Slicer while you train your AI models. It only takes a few lines of code to later load your trained models and run them on images in Slicer.</p>
</li>
</ol>

---

## Post #3 by @AMK (2021-10-18 14:16 UTC)

<p>Thanks Mr Ungi. I was also thinking of this approach of exporting the data from Slicer to train the neural network and bringing it back afterwards.</p>

---

## Post #4 by @keyurradia (2024-02-10 05:19 UTC)

<p>Hei,</p>
<p>I am looking for something like that only, can you share the available tutorial for extension?</p>
<p>best regards<br>
Keyur</p>

---

## Post #5 by @muratmaga (2024-02-10 05:35 UTC)

<p>Try MONAI project <a href="https://monai.io/">https://monai.io/</a><br>
and specifically MONAILabel <a href="https://docs.monai.io/projects/label/en/latest/index.html" class="inline-onebox">MONAI Label — MONAI Label 0.8.1 Documentation</a></p>
<p>as a starting point. You can find more examples on the web.</p>

---

## Post #6 by @keyurradia (2024-02-10 05:44 UTC)

<p>Thank you for the prompt response.</p>

---
