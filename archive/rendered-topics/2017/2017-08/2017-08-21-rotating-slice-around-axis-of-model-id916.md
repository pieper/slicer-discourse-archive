---
topic_id: 916
title: "Rotating Slice Around Axis Of Model"
date: 2017-08-21
url: https://discourse.slicer.org/t/916
---

# Rotating Slice around Axis of Model

**Topic ID**: 916
**Date**: 2017-08-21
**URL**: https://discourse.slicer.org/t/rotating-slice-around-axis-of-model/916

---

## Post #1 by @danielbr (2017-08-21 21:18 UTC)

<p>Hi all,<br>
Having a slight problem and can’t for the life of me figure it out.  Was hoping that one of you could help me out.  Let me explain the problem.</p>
<p>I have a 3d model loaded into the scene.  That model has two transforms applied to it.</p>
<p>RegistrationTransform-&gt;RotationTransform-&gt;Model</p>
<p>The registration transform registers the model to image space(offset and rotation).  The RotationTransform controls how the model is rotated about its axes.  I am trying to make a slider which will rotate the model about the model Y axis and have the axial slice follow this rotation.  Currently I have a slider which is connected to the following method and the model rotation is working perfectly by applying a Y rotation to the RotationTransform.  See code:</p>
<pre><code>void onModelRotationSliderChanged(double value){
     vtkMRMLLinearTransformNode* registrationTransform = this-&gt;mrmlScene()-&gt;GetNodeByID('vtkMRMLLinearTransformNode1');
     vtkMRMLLinearTransformNode* rotationTransform = this-&gt;mrmlScene()-&gt;GetNodeByID('vtkMRMLLinearTransformNode2');
     rotationTransform-&gt;RotateWXYZ(d-&gt;previousRotation - value, 0, 1, 0);
     d-&gt;previousRotation = value;
}
</code></pre>
<p>The above code works perfectly.  No matter what RegistrationTransform is used the model always rotates around the model Y axis.  The problem I am having is getting the slice to then follow that same rotation.  I have the following code which I added to the end of the above function, but it doesn’t rotate the axial slice in the desired manner:</p>
<pre><code>vtkSmartPointer&lt;vtkMatrix4x4&gt; currentSliceToRAS = d-&gt;redViewer-&gt;GetSliceToRAS();
vtkSmartPointer&lt;vtkMatrix4x4&gt; registrationMatrix = registrationTransform-&gt;GetMatrixTransformToParent();
vtkSmartPointer&lt;vtkMatrix4x4&gt; newResliceMatrix = vtkSmartPointer&lt;vtkMatrix4x4&gt;::New();
newResliceMatrix-&gt;Multiply4x4(rotationTransform-&gt;GetMatrix(), registrationMatrix, newResliceMatrix);
currentSliceToRAS-&gt;SetElement(0, 0, newResliceMatrix-&gt;GetElement(0, 0));
currentSliceToRAS-&gt;SetElement(0, 1, newResliceMatrix-&gt;GetElement(0, 1));
currentSliceToRAS-&gt;SetElement(0, 2, newResliceMatrix-&gt;GetElement(0, 2));
currentSliceToRAS-&gt;SetElement(0, 3, registrationMatrix-&gt;GetElement(0, 3));
currentSliceToRAS-&gt;SetElement(1, 0, newResliceMatrix-&gt;GetElement(1, 0));
currentSliceToRAS-&gt;SetElement(1, 1, newResliceMatrix-&gt;GetElement(1, 1));
currentSliceToRAS-&gt;SetElement(1, 2, newResliceMatrix-&gt;GetElement(1, 2));
currentSliceToRAS-&gt;SetElement(1, 3, registrationMatrix-&gt;GetElement(1, 3));
currentSliceToRAS-&gt;SetElement(2, 0, newResliceMatrix-&gt;GetElement(2, 0));
currentSliceToRAS-&gt;SetElement(2, 1, newResliceMatrix-&gt;GetElement(2, 1));
currentSliceToRAS-&gt;SetElement(2, 2, newResliceMatrix-&gt;GetElement(2, 2));
currentSliceToRAS-&gt;SetElement(2, 3, registrationMatrix-&gt;GetElement(2, 3));
d-&gt;redViewer-&gt;UpdateMatrices();

The axial slice lines up perfect with the model in the beginning, but when I start to rotate, the slice does not rotate around the Y axis of the model.  Any help would be greatly appreciated.  Thanks!</code></pre>

---

## Post #2 by @lassoan (2017-08-22 02:12 UTC)

<p>Despite compositing matrices is a really simple operation (you just have to get the order of the matrices right and invert them as needed), you  may easily spend a couple of days figuring out the correct combination.</p>
<p>We’ve found that a very good way of getting the correct solution quickly is following these steps:</p>
<ol>
<li>
<p>Define each coordinate system: what is the unit (mm, pixel, …), where is the origin, what are the coordinate system axis directions. It also helps if you draw a sketch of the origin position and axis directions relative to physical objects. See an <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CommonCoordinateSystems.html">example in Plus toolkit’s user manual</a>.</p>
</li>
<li>
<p>Name each transformation as a transformation from coordinate system <code>A</code> to <code>B</code> as AToB (you may add Transform or Matrix suffix to make it even more clear that it is a transform). For example, <code>SliceToRAS</code> is a well-defined transformation. <code>newResliceMatrix</code> and <code>registrationMatrix</code> names are not usable because they don’t specify what coordinate systems they are transforming between and in what order.</p>
</li>
<li>
<p>Create chain of matrices using the following rules:</p>
</li>
</ol>
<ul>
<li>AToC = BToC * AToB</li>
<li>AToB = inv(BToA)</li>
</ul>
<p>Alternatively, in some simple cases when you need to place a slice view to a based on a position and a normal vector, you may also find <a href="http://apidocs.slicer.org/master/classvtkMRMLSliceNode.html#a0e8251eb55cfb40e316c2e22894b140c">vtkMRMLSliceNode::SetSliceToRASByNTP</a> method useful. See how it is used for <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py">rotating slice views in ValveView module</a>.</p>
<p>For real-time positioning of a slice view using a transform, use <code>VolumeResliceDriver</code> module of <code>SlicerIGT</code> extension.</p>

---

## Post #3 by @danielbr (2017-08-22 13:43 UTC)

<p>Thanks for the explanation.  Turns out it was something extremely simple.  Matrix multiplication is not commutative.  For my example above I was specifying AToC = AToB * BToC.  Changing the order fixed the problem right away!  Thanks!</p>

---
