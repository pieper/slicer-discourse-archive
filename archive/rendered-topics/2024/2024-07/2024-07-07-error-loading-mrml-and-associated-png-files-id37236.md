---
topic_id: 37236
title: "Error Loading Mrml And Associated Png Files"
date: 2024-07-07
url: https://discourse.slicer.org/t/37236
---

# Error loading .mrml and associated .png files

**Topic ID**: 37236
**Date**: 2024-07-07
**URL**: https://discourse.slicer.org/t/error-loading-mrml-and-associated-png-files/37236

---

## Post #1 by @pamelaeck (2024-07-07 15:15 UTC)

<p>Slicer 5.6.2, MacBook Pro Ventura 13.6.7<br>
I am newbie with using Slicer, hoping to run SlicerMorph for 3D morphometrics.  I added some landmarks on a vertebra and saved. But when I try to open the .mrml and .png files I get this error msg:</p>
<pre><code class="lang-auto">- Error: Loading /Users/Terra-2/EQUUS-SOMA/ECCMV/ECVM-PUBLICATION/MELA'S MS/MORPHOMETRICS/BELLA/BELLA-LMs_C5/Bella-LM-C5-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326

vtkMRMLMarkupsFiducialNode (0x7f8fc5452350): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Bel-C5 (vtkMRMLMarkupsFiducialNode1) using storage node vtkMRMLMarkupsFiducialStorageNode1.

- Error: Loading /Users/Terra-2/EQUUS-SOMA/ECCMV/ECVM-PUBLICATION/MELA'S MS/MORPHOMETRICS/BELLA/BELLA-LMs_C5/Bella-LM-C5-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326

vtkMRMLVectorVolumeNode (0x7f8fc545fe10): vtkMRMLStorableNode::UpdateScene failed: Failed to read node 2024-07-05-Scene (vtkMRMLVectorVolumeNode2) using storage node vtkMRMLVolumeArchetypeStorageNode2.

- Error: Loading /Users/Terra-2/EQUUS-SOMA/ECCMV/ECVM-PUBLICATION/MELA'S MS/MORPHOMETRICS/BELLA/BELLA-LMs_C5/Bella-LM-C5-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326

vtkMRMLVectorVolumeNode (0x7f8fc546b640): vtkMRMLStorableNode::UpdateScene failed: Failed to read node 2024-07-05-Scene_1 (vtkMRMLVectorVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode4.
</code></pre>
<p>Please advise, thank you!!</p>

---

## Post #2 by @lassoan (2024-07-07 15:20 UTC)

<p>If you only have mrml and png files then you have not saved the actual data files (in nrrd, json, … formats). What files do you have in your scene file folder?</p>
<p>Normally all data files are saved automatically. Have you manually disabled saving of data files (unchecked checkboxes) when you saved the scene? Is it possible that you loaded some data sets from removable drives or network drives that you then disconnected?</p>

---

## Post #3 by @pamelaeck (2024-07-07 17:34 UTC)

<p>Thank you for your quick reply.</p>
<p>I started from scratch and marked up the vertebra model, this time with fewer points as a test. I saved the mrml, png and json files in the scene folder.</p>
<p>When I try to open the model with markups again, any combination of these 3 files results in another error msg. This time it specifies “UpdateScene failed: Failed to read node Bella_C5_mesh copy (vtkMRMLModelNode4) using storage node vtkMRMLModelStorageNode1.”</p>
<p>The “Bella_C5-mesh copy” is the only file listed in the Node window.</p>

---

## Post #4 by @lassoan (2024-07-07 22:38 UTC)

<p>Can you show a screenshot of the <code>Save data</code>  window just before you click <code>Save</code>?</p>

---

## Post #5 by @pamelaeck (2024-07-07 22:50 UTC)

<p>I discovered the problem, since it seemed to revolve around the mesh file. When the Save dial box opens, that file is not checked (by default?) so I didn’t think it was needed.  When I select it to be saved with the others, now I can re-open the model with the LMs.</p>
<p>Your previous suggestion helped me reason through it, thanks!  Now I am on to the next steps of the learning curve with more questions, LOL.</p>

---
