# FreeSurfer output loading on slicer via command line

**Topic ID**: 22055
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/freesurfer-output-loading-on-slicer-via-command-line/22055

---

## Post #1 by @Tejasvi0409 (2022-02-18 17:47 UTC)

<p>I have been able to load freesurfer volume outputs on the slicer, import segmentations, and perform radiomic feature extraction using the slicer application. However, I would like to do the same using the command line in MacBook Air in batch mode for multiple subjects. Could someone please direct me in the right direction?</p>

---

## Post #2 by @lassoan (2022-02-18 18:43 UTC)

<p>You can use the <a href="https://github.com/PerkLab/SlicerFreeSurfer/blob/ecdc500aa8a53f2733c4cb4d5340331286422fc7/FreeSurferImporter/Logic/vtkSlicerFreeSurferImporterLogic.h#L58-L63">FreeSurferImporterLogic module’s logic</a> in Python scripts to load freesurfer data then process, quantify, export, etc. Something like this can work for data loading:</p>
<pre><code class="lang-python">fsImporterLogic = slicer.util.getModuleLogic('FreeSurferImporter')
volume = fsImporterLogic.LoadFreeSurferVolume('path/to/myfile')
</code></pre>

---

## Post #3 by @ysakato (2022-03-09 06:35 UTC)

<p>I’m also trying to load FreeSurfer data with Python command line.<br>
I succeeded to load volume, segmentation and model(pial) with this approach.<br>
However, I cannot load annotation file by LoadFreeSurferScalarOverlay with error below. (This process can work with GUI.)<br>
Would you suggest some solution for this problem?</p>
<blockquote>
<blockquote>
<blockquote>
<p>fsImporterLogic = slicer.util.getModuleLogic(‘FreeSurferImporter’)<br>
pial = fsImporterLogic.LoadFreeSurferModel(‘fsaverage/surf/lh.pial’)<br>
modelNode=slicer.util.getNode(“lh_pial”)<br>
fsImporterLogic.LoadFreeSurferScalarOverlay(‘fsaverage/label/lh.aparc.annot’, modelNode.GetID())<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘vtkSlicerFreeSurferImporterModuleLogicPython.vtkSl’ object has no attribute ‘LoadFreeSurferScalarOverlay’</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #4 by @lassoan (2022-03-09 06:47 UTC)

<p><code>LoadFreeSurferScalarOverlay</code> method is not Python-wrapped (VTK’s Python wrapper does not support vector of VTK objects).</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you add a Python-wrappable variant of this method?</p>

---

## Post #5 by @Sunderlandkyl (2022-03-09 15:43 UTC)

<p>New python wrapped methods should be available tomorrow  in the nightly.</p>
<p>There are two function signatures, one that can load the overlay on many model nodes, and one that loads the overlay on a single model node:</p>
<pre><code class="lang-auto">bool LoadFreeSurferScalarOverlay(std::string filePath, vtkCollection* modelNodes);
bool LoadFreeSurferScalarOverlay(std::string filePath, vtkMRMLModelNode* modelNode);
</code></pre>

---

## Post #6 by @ysakato (2022-03-11 04:36 UTC)

<p>Thank you for your kind support!</p>

---
