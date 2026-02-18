# Apply a nonlinear transform to model using Python code

**Topic ID**: 29896
**Date**: 2023-06-07
**URL**: https://discourse.slicer.org/t/apply-a-nonlinear-transform-to-model-using-python-code/29896

---

## Post #1 by @SANTIAGO_PENDON_MING (2023-06-07 13:10 UTC)

<p>Hi to everyone, on this occasion we are trying to automate a specific transform process. Our goal is to apply a transform we made before in a slicer 3D model. The workflow is the next one:</p>
<p>•	We use the module Curved Planar Reformat to straight the volume. This procedure yields two new nodes in the Slicer Scene: The straightened volume, and the Straighten Transform.</p>
<p>•	We want to apply this transform (which is nonlinear and non-computable in a 4x4 matrix) to a model we made before .</p>
<p>•	We use the transformed model for own purposes.</p>
<p>Apply this Straightening Transform is quite easy doing the usual ‘clicks’ in Tranforms module. The problem arises when we try to automate the transforming process using Python. The typical ways to interact with modules are not capable to use Transforms module as we need.</p>
<p>In case the module can be used with Python code, we also need to know how to select the inverse transform who appears in the Slicer GUI and apply/unapply a transform.</p>
<p>Is there a way to automate the process using code?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>
<p>Pd: We check the following related link:<br>
<a href="https://discourse.slicer.org/t/apply-nonlinear-transform-to-point-in-python/16701" class="inline-onebox">Apply nonlinear transform to point in python</a> ,<br>
but we don´t find anything useful on it.</p>

---

## Post #2 by @mikebind (2023-06-07 17:16 UTC)

<p>Something like the following should work for applying a nonlinear transform to a model:</p>
<pre><code class="lang-auto">straightenTransformNode = getNode('Straighten Transform')
# Get the model node that you want to transform
modelName = 'MyModel' # change this to whatever the name of your model is
modelNode = getNode(modelName)
# To apply transform to model
modelNode.SetAndObserveTransformNodeID(straightenTransformNode.GetID())
# To unapply a transform
modelNode.SetAndObserveTransformNodeID(None)
</code></pre>
<p>Separately, to invert a transform node, call <code>Inverse()</code> on it</p>
<pre><code class="lang-auto">straightenTransformNode.Inverse()
</code></pre>
<p>You might also find the following discussion helpful: <a href="https://discourse.slicer.org/t/invert-transform-elastix/14754" class="inline-onebox">Invert transform (Elastix)</a></p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2023-06-08 06:51 UTC)

<p>Thanks a lot, your post it´s so helpful and now we can apply nonlinear transforms to models.</p>

---
