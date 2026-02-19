---
topic_id: 21469
title: "Model Visualization"
date: 2022-01-14
url: https://discourse.slicer.org/t/21469
---

# Model visualization

**Topic ID**: 21469
**Date**: 2022-01-14
**URL**: https://discourse.slicer.org/t/model-visualization/21469

---

## Post #1 by @Luca (2022-01-14 21:01 UTC)

<p>Dear community,</p>
<p>I imported a model by python scripting with the following lines:</p>
<p>inputModel = slicer.util.loadModel(model_path)<br>
inputModel.SetDisplayVisibility(1)<br>
inputModel.GetDisplayNode().SetOpacity(0.25)<br>
inputModel.GetDisplayNode().SetColor(1,1,1)</p>
<p>then I did some operations in it and now I want to see if my pipeline worked well. I have a vtkpolydata object as output and, starting from here <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-simple-surface-mesh-as-a-model-node" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>, I import my result back in Slicer with the following function:</p>
<p>def slicer_model_node(model, node_name, visibility=0, opacity=1, color=(255,0,0)):<br>
model_Node = slicer.modules.models.logic().AddModel(model)<br>
model_Node.SetName(node_name)<br>
model_Node.SetDisplayVisibility(visibility)<br>
model_Node.GetDisplayNode().SetOpacity(opacity)<br>
model_Node.GetDisplayNode().SetColor(color)<br>
model_Node.GetDisplayNode().SetLighting(1)#<br>
model_Node.GetDisplayNode().SetAmbient(0.0)#<br>
model_Node.GetDisplayNode().SetDiffuse(1)#<br>
model_Node.GetDisplayNode().SetPower(1)#<br>
model_Node.GetDisplayNode().SetLighting(1)#<br>
model_Node.GetDisplayNode().SetInterpolation(1)#<br>
model_Node.GetDisplayNode().SetShading(1)#<br>
return model_Node</p>
<p>However the result is the following: left=new model, right=input model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ee0a0feed692a753bce5999a3b770ad5cf45671.png" data-download-href="/uploads/short-url/i6pqrhPrRvv1HylbDIX4FRZJ6X7.png?dl=1" title="immagine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee0a0feed692a753bce5999a3b770ad5cf45671_2_690x338.png" alt="immagine" data-base62-sha1="i6pqrhPrRvv1HylbDIX4FRZJ6X7" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee0a0feed692a753bce5999a3b770ad5cf45671_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee0a0feed692a753bce5999a3b770ad5cf45671_2_1035x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee0a0feed692a753bce5999a3b770ad5cf45671_2_1380x676.png 2x" data-dominant-color="367D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine</span><span class="informations">1918×942 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please tell me which lines I miss or which I wrongly wrote? (Lines with “#” at the end were added later to verify if they were the missing ones). I think it is a problem of shading or lighting but I didn’t manage to find the right way.</p>
<p>Thank you in advance</p>

---

## Post #2 by @Luca (2022-01-16 21:28 UTC)

<p>Solved: color components must be between 0 and 1, not 0-255</p>

---
