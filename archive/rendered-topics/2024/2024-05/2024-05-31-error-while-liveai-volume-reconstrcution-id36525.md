# Error while liveAI volume reconstrcution

**Topic ID**: 36525
**Date**: 2024-05-31
**URL**: https://discourse.slicer.org/t/error-while-liveai-volume-reconstrcution/36525

---

## Post #1 by @MReza (2024-05-31 18:38 UTC)

<p>Hello everyone,</p>
<p>I am trying to work with the live AI segmentation as shown in the YouTube video and the related PowerPoint. Although I have followed the exact same procedure, after inputting the mrb file, when I try to run the segmentation through Segmentation UNet, I keep getting the below error.</p>
<p>Failed to start live segmentation: ‘inputLayer’ object has no attribute ‘input_shape’</p>
<p>Additionally, my Python console shows:</p>
<p>[VTK] GetSliceOrientationPreset: invalid orientation preset name: Reformat<br>
[FD] 2024-05-31 14:35:01.106830: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.<br>
[FD] To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.<br>
[Python] Failed to start live segmentation: ‘InputLayer’ object has no attribute ‘input_shape’<br>
Traceback (most recent call last):<br>
File “C:/Users/effatpar/Desktop/SlicerIGT aigt master SlicerExtension-LiveUltrasoundAi_SegmentationUNet/<a href="https://segmentationunet.py/" rel="noopener nofollow ugc">SegmentationUNet.py</a>”, line 296, in onApplyButton<br>
self.logic.setRealTimePrediction(toggled)<br>
File “C:/Users/effatpar/Desktop/SlicerIGT aigt master SlicerExtension-LiveUltrasoundAi_SegmentationUNet/<a href="https://segmentationunet.py/" rel="noopener nofollow ugc">SegmentationUNet.py</a>”, line 516, in setRealTimePrediction<br>
model_input_shape = layer.input_shape[0]<br>
AttributeError: ‘InputLayer’ object has no attribute 'input_shape’02:37 PM</p>
<p>I would be grateful for any help</p>

---

## Post #2 by @lassoan (2024-06-01 12:30 UTC)

<p>We moved on from TensorFlow to PyTorch and MONAI. Probably the best would be to train your own ultrasound segmentation model using MONAI.</p>
<p><a class="mention" href="/u/ungi">@ungi</a> is now developing the <a href="https://github.com/SlicerUltrasound/SlicerUltrasound">Ultrasound extension</a> for Slicer that has useful tools to help with this.</p>

---

## Post #3 by @ungi (2024-06-01 13:20 UTC)

<p>Yes, the answer is a bit complex. We left the SegmentationUNet Slicer module in the aigt repository because some systems still use tensorflow and that example also shows how to start a separate process for inference from Slicer. But that is not how I would implement a new system today.</p>
<p>In new systems, the ultrasound machine (or PLUS) directly streams the images to an inference program that runs the AI model on the images in real time (not in Slicer). The inference program can stream the segmentations to Slicer using the pyigtl package and an OpenIGTLink connector in Slicer.</p>
<p>We don’t have comprehensive tutorials yet, mainly because systems are still evolving. But an example inference program can be found here:<br>
<a href="https://github.com/SlicerIGT/aigt/blob/master/UltrasoundSegmentation/Inference/ScanConversionInference.py" rel="noopener nofollow ugc">aigt/UltrasoundSegmentation/Inference/ScanConversionInference.py at master · SlicerIGT/aigt (github.com)</a></p>
<p>MONAI is a great help in creating and training pytorch models. The example above does not depend on MONAI for inference, but we should adopt more modules of MONAI. E.g. the example above uses a separate custom config file to specify how to preprocess the images before they can be used by the trained model. It would be better to use standard methods and format for that to ensure that trained models are compatible across inference programs.</p>

---

## Post #4 by @MReza (2024-06-01 16:32 UTC)

<p>Thank you very much for your reply. It’s great to hear that the available procedures are developing. However, since I have already started a new study based on what I had seen and learned from your current model, is there any way I can use the TensorFlow method in its current format? Alternatively, how can I adapt my own system to work with TensorFlow?</p>
<p>Honestly, I don’t have enough samples at the moment to train my own segmentation model.</p>
<p>Thanks in advance for your help.</p>

---
