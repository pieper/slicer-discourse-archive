---
topic_id: 28706
title: "Save Transforms And Models As Batch"
date: 2023-04-01
url: https://discourse.slicer.org/t/28706
---

# Save transforms and models as batch

**Topic ID**: 28706
**Date**: 2023-04-01
**URL**: https://discourse.slicer.org/t/save-transforms-and-models-as-batch/28706

---

## Post #1 by @Melanie (2023-04-01 03:52 UTC)

<p>Hi</p>
<p>I have a series of models, indexed from 1 to 10.<br>
I use the model registration module to register model 1 to all the subsequent models.<br>
Then I want to save the transformation matrices as .mat files from 1-10.</p>
<p>Could someone pls let me know how to create a loop within the python console</p>
<ol>
<li>To apply model registration to each model (fixed=model 01, moving =2:10)</li>
<li>Generate transformation matrix for each iteration</li>
<li>save each matrix as . mat file.</li>
</ol>
<p>Thanks very much</p>

---

## Post #3 by @rbumm (2023-04-03 09:17 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="28706">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>I have a series of models, indexed from 1 to 10.<br>
I use the model registration module to register model 1 to all the subsequent models.<br>
Then I want to save the transformation matrices as .mat files from 1-10.</p>
<p>Could someone pls let me know how to create a loop within the python console</p>
<ol>
<li>To apply model registration to each model (fixed=model 01, moving =2:10)</li>
<li>Generate transformation matrix for each iteration</li>
<li>save each matrix as . mat file.</li>
</ol>
</blockquote>
</aside>
<p>Here is what ChatGPT-3.5 suggests, looks at least reasonable and may get you started:</p>
<pre><code class="lang-auto">import os
import slicer
from slicer.util import NodeModifyTransform

# Set up the file path for saving the .mat files
output_dir = "/path/to/output/directory/"

# Set the fixed model to model 1
fixed_model = slicer.util.getNode("Model_01")

# Loop over the moving models (models 2-10)
for i in range(2, 11):
    # Set the moving model
    moving_model = slicer.util.getNode("Model_{:02d}".format(i))
    
    # Set up the model registration node
    reg_node = slicer.vtkMRMLLinearTransformNode()
    slicer.mrmlScene.AddNode(reg_node)
    reg_node.SetName("Registration_{:02d}".format(i))
    
    # Apply model registration
    logic = slicer.modules.modelregistration.logic()
    logic.SetModeToRigid()
    logic.RegisterModels(fixed_model, moving_model, reg_node)
    
    # Save the transformation matrix as a .mat file
    output_path = os.path.join(output_dir, "Transformation_{:02d}.mat".format(i))
    NodeModifyTransform.SaveMatrixToMatFile(reg_node, output_path)
</code></pre>

---

## Post #4 by @Melanie (2023-04-07 07:32 UTC)

<p>Thanks ever so much</p>
<p>I tried this,</p>
<p>Always get<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘SlicerBaseLogicPython.vtkSlicerScriptedLoadableMod’ object has no attribute ‘registerModel’</p>
<p>I have tried ‘registerModel’ and ‘registerModels’ both<br>
Gives the same error</p>
<p>Any thought please</p>
<p>Thanks very much</p>

---

## Post #5 by @rbumm (2023-04-07 10:43 UTC)

<p>Hi Melanie, here is what GPT-4 suggests. I can not test the code right now, but I hope it brings you closer to achieving your goal.</p>
<p>Me:<br>
asking your question.</p>
<p>GPT-4:<br>
This code assumes that you’ve already loaded your models and their respective nodes are available in the scene.</p>
<p>Before running the code snippet, make sure you’ve installed and enabled the SlicerElastix extension, as it provides the necessary registration tools.</p>
<pre><code class="lang-auto">import os

# Set the output directory for the transformation matrices
output_dir = 'path/to/your/output/directory'
fixed_node = slicer.util.getNode('model_01')

for i in range(2, 11):
    moving_node = slicer.util.getNode(f'model_{i:02d}')

    # Set up the registration parameters
    parameter_set = slicer.vtkMRMLScriptedModuleNode()
    slicer.mrmlScene.AddNode(parameter_set)
    parameter_set.SetName(f'Registration_Parameters_{i:02d}')
    parameter_set.SetParameter('fixed', fixed_node.GetID())
    parameter_set.SetParameter('moving', moving_node.GetID())

    # Perform the registration
    elastix_logic = slicer.modules.elastix.logic()
    elastix_logic.RegisterVolumes(parameter_set)

    # Get the output transformation node
    transform_node_id = parameter_set.GetParameter('outputTransform')
    transform_node = slicer.mrmlScene.GetNodeByID(transform_node_id)

    # Save the transformation matrix as a .mat file
    output_filename = os.path.join(output_dir, f'transformation_{i:02d}.mat')
    slicer.util.saveNode(transform_node, output_filename)

    # Remove the parameter set and transformation nodes from the scene
    slicer.mrmlScene.RemoveNode(transform_node)
    slicer.mrmlScene.RemoveNode(parameter_set)
</code></pre>
<p>This code snippet performs the following steps:</p>
<ol>
<li>Sets the output directory for the transformation matrices.</li>
<li>Loops through the models from 2 to 10.</li>
<li>Sets up the registration parameters.</li>
<li>Performs the registration using the Elastix registration module.</li>
<li>Retrieves the output transformation node.</li>
<li>Saves the transformation matrix as a .mat file.</li>
<li>Removes the parameter set and transformation nodes from the scene to keep it clean.</li>
</ol>
<p>Don’t forget to replace <code>'path/to/your/output/directory'</code> with the actual path where you want to save the transformation matrices.</p>

---

## Post #6 by @Melanie (2023-04-07 10:45 UTC)

<p>Thaks so much,</p>
<p>I will trial it</p>
<p>Thanks again</p>

---
