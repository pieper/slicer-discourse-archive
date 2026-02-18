# Node changes MRML ID after saving and loading, which makes value saved in module parameter node invalid

**Topic ID**: 18332
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/node-changes-mrml-id-after-saving-and-loading-which-makes-value-saved-in-module-parameter-node-invalid/18332

---

## Post #1 by @mikebind (2021-06-24 18:47 UTC)

<p>In a module I have developed, the user loads a surface model node from a file, and the MRML ID of that model node is saved as a parameter in the parameter node for the model. The user can then control the visibility of that model by checking or unchecking a checkbox in the module.  However, after saving the scene and reloading it, the MRML ID associated with the loaded model changes, from ‘vtkMRMLModelNode4’ to ‘vtkMRMLModelNode7’.  After loading, ‘vtkMRMLModelNode4’ is the ID of a slice representation in the 3D view.  It’s name is “Slice Volume Slice”.  I’m not really sure how this happens, but my guess that perhaps Slicer gives out model ID’s 1-6 for slice views on load, and then when it wants to load the surface model node and it is supposed to have model ID 4, but ID 4 is already taken, the surface model is assigned the first non-taken model ID at that point, which is 7. However, my module parameter node does not know this happened, so it still has the model ID 4 stored.</p>
<p>Does anyone have a suggestion for the best way to avoid this behavior?  One idea I had was to give the loaded model node a non-default ID when it is initially loaded, and then that would avoid a name collision with the default node naming scheme, but I don’t see how to do this (or if it is even possible). Supplying an ID does not seem to be an option with slicer.util.loadNodeFromFile, which I use so that I can use the ‘FreeSurferModelFile’ filetype and supply a reference node in the parameters. I don’t see a way to SetID() on a node (which makes sense because it would, in general, cause the kind of problems I’m trying to fix).</p>

---

## Post #2 by @pieper (2021-06-24 19:43 UTC)

<p>Yes, the node IDs change based on scene load/save operations and you need to let the MRML Scene handle that part.</p>
<p>Instead, you should use Node References as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#mrml-node-references">here</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/MRML/NodeReferences">here</a> to get an idea of the design and <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py">the scripted module template</a> to see example usage in a parameter node.  This takes a little getting used to, but it automates a lot of complexity under the hood.</p>

---

## Post #3 by @mikebind (2021-06-24 20:17 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>.  I saw the changed template in more recent modules I’ve created, and had started using those there, but I hadn’t switched over older modules which had been based on earlier templates. I hadn’t seen a good reason to, until now. I didn’t realize that I had always essentially just been lucky that the IDs didn’t change over save/load cycles. I’ll need to think about how to handle updating to the new structure when loading old saved scenes and parameter nodes, but I want those links to be persistent, so I definitely need to do this.</p>

---

## Post #4 by @mikebind (2021-06-24 21:23 UTC)

<p>I’m working on implementing this, which is straightforward so far for the module parameter node.  However, I’m not sure what to do when I have a python object which should keep track of a link to a MRML node.  Previously, I just stored the MRML ID of the referred-to MRML node in a property of the python object, but this method obviously relies on the MRML IDs being stable across save/load cycles, which they sometimes aren’t. How can I do something similar to storing Node References instead of storing MRML ID strings in a python object?  I’m hoping there’s a simple solution…</p>

---

## Post #5 by @pieper (2021-06-24 21:31 UTC)

<p>I’d suggest always getting the node via the reference.  That is, you would know your current parameter node (e.g. selected via a combo box in your module) and then use that to get all the nodes to use for your computation.  With the right observers in place this should simplify keeping everything in sync.</p>

---

## Post #6 by @mikebind (2021-06-24 21:36 UTC)

<p>Thanks, that seems reasonable.  I’ll route all node finding for the python objects through the module’s parameter node, which can hold the node references, which will point to the right nodes even through save/load cycles.  I appreciate the help and quick responses very much!</p>

---
