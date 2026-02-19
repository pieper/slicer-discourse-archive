---
topic_id: 29374
title: "Nvidia Aiaa Server"
date: 2023-05-09
url: https://discourse.slicer.org/t/29374
---

# Nvidia AIAA server

**Topic ID**: 29374
**Date**: 2023-05-09
**URL**: https://discourse.slicer.org/t/nvidia-aiaa-server/29374

---

## Post #1 by @marwanabb (2023-05-09 09:23 UTC)

<p>Hello,</p>
<p>It seems that the remote default server for the Nvidia AIAA module is offline. If I’m not wrong, the server address is : <a href="http://perklabseg.cs.queensu.ca:8000/" rel="noopener nofollow ugc">http://perklabseg.cs.queensu.ca:8000/</a> . Is It normal ?</p>

---

## Post #2 by @lassoan (2023-05-10 03:04 UTC)

<p>Developers of NVIDIA AIAA extension deprecated it and switched over to developing MONAILabel extension instead. MONAILabel is not only for running existing models but you can use it to train your own models.</p>
<p>For segmenting almost anything on CT (all major organs, bones, vessels, etc.) you can now use the <a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator">TotalSegmentator extension</a> (100+ structures, fully automatically in 2 minutes, even without a GPU).</p>

---

## Post #3 by @marwanabb (2023-05-10 08:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for you reply ! With the NVIDIA AIAA extension, I was using this model for tumor segmentation that was available on the remote server : <a href="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_ct_seg_liver_and_tumor_amp" class="inline-onebox" rel="noopener nofollow ugc">clara_ct_seg_liver_and_tumor_amp | NVIDIA NGC</a> , If I’m not wrong MONAILabel only provides pretained models from the MONAI Zoo, is there any way to use this liver and tumor segmentation model ?</p>

---

## Post #4 by @lassoan (2023-05-10 12:12 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> Is the <em>clara_ct_seg_liver_and_tumor_amp</em> model availble for MONAILabel?</p>

---

## Post #5 by @diazandr3s (2023-05-10 14:33 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>No, I’m afraid <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>
<p>These are the available models: <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models" class="inline-onebox" rel="noopener nofollow ugc">model-zoo/models at dev · Project-MONAI/model-zoo · GitHub</a></p>
<p>You also have the whole-body CT segmentation model that might be worth checking for this task: <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation" class="inline-onebox" rel="noopener nofollow ugc">model-zoo/models/wholeBody_ct_segmentation at dev · Project-MONAI/model-zoo · GitHub</a></p>
<p>Or just the segmentation model here: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#segmentation" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/radiology at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>It shouldn’t be difficult to get a trained model for liver and tumor using the MSD dataset: <a href="https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2" class="inline-onebox" rel="noopener nofollow ugc">MSD - Google Drive</a></p>
<p>Hope this helps,</p>

---

## Post #6 by @rbumm (2023-05-10 15:01 UTC)

<p>I find this response from GPT-4 rather interesting:</p>
<p>Human:<br>
Hey GPT, what is Clara CT Seg Liver and Tumor AMP?</p>
<p>ChatGPT:<br>
Clara CT Seg Liver and Tumor AMP is a pre-trained model developed by NVIDIA Clara, a platform for AI-driven medical imaging. The model is designed for volumetric (3D) segmentation of liver and lesion in portal venous phase CT (Computed Tomography) images. It leverages Mixed Precision mode during training, which combines the use of single-precision (FP32) and half-precision (FP16) formats to speed up training while maintaining model accuracy.</p>
<p>The pre-trained model can be fine-tuned with additional annotated data to improve performance in specific use cases or to adapt to variations in imaging protocols and patient populations. It can be used to assist radiologists and other medical professionals in detecting and delineating liver and tumor regions in CT scans, which can be crucial for diagnosis, treatment planning, and monitoring of patients with liver diseases or tumors.</p>
<p>Human:<br>
I would like to integrate this model into a 3D Slicer extension. Could you provide some Python code to get me started?</p>
<p>ChatGPT</p>
<p>To integrate the Clara CT Seg Liver and Tumor AMP model into a 3D Slicer extension, you’ll first need to have the pre-trained model available as a TensorFlow or ONNX model. Then, you can use the 3D Slicer Python environment to load the model, perform segmentation, and display the results. Here’s a Python template to help you get started:</p>
<ol>
<li>Install the required packages in the 3D Slicer Python environment.</li>
</ol>
<p>bashCopy code</p>
<pre><code class="lang-auto"># Open the 3D Slicer Python interactor and run:
slicer.util.pip_install("tensorflow")
slicer.util.pip_install("onnx")
slicer.util.pip_install("onnx-tf")
</code></pre>
<ol start="2">
<li>Create a new 3D Slicer extension and add the following Python code to perform segmentation using the Clara CT Seg Liver and Tumor AMP model:</li>
</ol>
<p>pythonCopy code</p>
<pre><code class="lang-auto">import numpy as np
import tensorflow as tf
import SimpleITK as sitk
import vtk.util.numpy_support as vtk_np

# Load the pre-trained model (e.g., TensorFlow SavedModel, frozen graph, or ONNX model)
def load_model(model_path):
    model = tf.saved_model.load(model_path)
    return model

# Preprocess the input volume (CT image) for the segmentation model
def preprocess_input(input_volume):
    # Implement any necessary preprocessing steps, such as normalization or resizing
    preprocessed_volume = input_volume
    return preprocessed_volume

# Postprocess the output volume (segmentation) for visualization in 3D Slicer
def postprocess_output(output_volume):
    # Implement any necessary postprocessing steps, such as thresholding or labeling
    postprocessed_volume = output_volume
    return postprocessed_volume

# Perform segmentation using the Clara CT Seg Liver and Tumor AMP model
def perform_segmentation(input_volume, model):
    preprocessed_input = preprocess_input(input_volume)
    segmentation = model(preprocessed_input)
    postprocessed_output = postprocess_output(segmentation)
    return postprocessed_output

# Convert the segmentation results to a 3D Slicer volume node
def create_volume_node_from_array(array, name, input_volume_node):
    volume_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', name)
    volume_node.CopyOrientation(input_volume_node)
    volume_node.SetSpacing(input_volume_node.GetSpacing())
    volume_node.SetOrigin(input_volume_node.GetOrigin())
    vtk_array = vtk_np.numpy_to_vtk(array.ravel(), deep=True, array_type=vtk.VTK_SHORT)
    slicer.util.updateVolumeFromArray(volume_node, vtk_array)
    return volume_node

# Main function
def main(input_volume_node, model_path):
    # Load the pre-trained model
    model = load_model(model_path)

    # Convert the input volume node to a NumPy array
    input_array = slicer.util.arrayFromVolume(input_volume_node)

    # Perform segmentation
    output_array = perform_segmentation(input_array, model)

    # Convert the output array to a 3D Slicer volume node and display it
    output_volume_node = create_volume_node_from_array(output_array, 'Segmentation', input_volume_node)
    slicer.util.setSliceViewerLayers(background=input_volume_node, foreground=output_volume_node, foregroundOpacity=0.5)

# Example usage:
# main(input_volume_node, "path/to/your/pretrained_model")
</code></pre>
<p>Replace the placeholders with the appropriate preprocessing and postprocessing steps based on the specific requirements of the Clara CT Seg Liver and Tumor AMP model. Also, make sure to provide the path to your pre-trained model when calling the main function.</p>
<hr>
<p>Not tested it in any way from my side, but I may try it in order to have a tensorflow-based prototype available</p>

---
