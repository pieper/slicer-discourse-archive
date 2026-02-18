# Create Axes Model using CreateModels CLI

**Topic ID**: 674
**Date**: 2017-07-11
**URL**: https://discourse.slicer.org/t/create-axes-model-using-createmodels-cli/674

---

## Post #1 by @hgueziri (2017-07-11 22:20 UTC)

<p>Hi all,</p>
<p>I trying to create a coordinate system model using CreateModels CLI called from a Python terminal. I tried the followings code (inspired from vtkSlicerCreateModelsLogic.h) but I could not guess what are the exact input/output parameters to give to the cli.</p>
<pre><code>modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
param = {'axisLength':20.0, 'axisRadius':2.0, 'modelNodeToUpdate':modelNode}
slicer.cli.run( slicer.modules.createmodels, 'CreateCoordinate', None, param, wait_for_completion=True )
</code></pre>
<p>Where can I find the documentation showing the input/output parameters of the createmodels CLI module (and to any given CLI module in general)?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2017-07-11 22:35 UTC)

<p>It is not a CLI module but a loadable module. You can verify that by printing the module’s class name:</p>
<pre><code>&gt;&gt;&gt; slicer.modules.createmodels.className()
'qSlicerCreateModelsModule'
</code></pre>
<p>You can use loadable modules by calling methods of their logic class:</p>
<pre><code>logic = slicer.modules.createmodels.logic()
logic.CreateNeedle(100,5,0,True)
</code></pre>
<p>To get a description of all methods and their parameters, type <code>help(logic)</code> and you get a description like this:</p>
<pre><code>class vtkSlicerCreateModelsLogic(vtkSlicerModuleLogic)
 |  vtkSlicerCreateModelsLogic - slicer logic class for creating simple
 |  models
 |  
 |  Superclass: vtkSlicerModuleLogic
 |  
 |  This class contains methods that create model nodes useful for
 |  setting up IGT scenes. These methods can be called from other
 |  modules.
 |  
 ...
 |  Methods defined here:
 |  
 |  CreateCoordinate(...)
 |      V.CreateCoordinate(float, float, vtkMRMLModelNode)
 |          -&gt; vtkMRMLModelNode
 |      C++: vtkMRMLModelNode *CreateCoordinate(double axisLength,
 |          double axisRadius, vtkMRMLModelNode *modelNodeToUpdate=NULL)
 |  
 |  CreateCube(...)
 |      V.CreateCube(float, float, float, vtkMRMLModelNode)
 |          -&gt; vtkMRMLModelNode
 |      C++: vtkMRMLModelNode *CreateCube(double x, double y, double z,
 |          vtkMRMLModelNode *modelNodeToUpdate=NULL)
 |  
 |  CreateCylinder(...)
 |      V.CreateCylinder(float, float, vtkMRMLModelNode)
 |          -&gt; vtkMRMLModelNode
 |      C++: vtkMRMLModelNode *CreateCylinder(double height,
 |          double radius, vtkMRMLModelNode *modelNodeToUpdate=NULL)
 |  
 |  CreateNeedle(...)
 |      V.CreateNeedle(float, float, float, bool, vtkMRMLModelNode)
 |          -&gt; vtkMRMLModelNode
 |      C++: vtkMRMLModelNode *CreateNeedle(double length, double radius,
 |          double tipRadius, bool markers,
 |          vtkMRMLModelNode *modelNodeToUpdate=NULL)
 |  
 |  CreateSphere(...)
 |      V.CreateSphere(float, vtkMRMLModelNode) -&gt; vtkMRMLModelNode
 |      C++: vtkMRMLModelNode *CreateSphere(double radius,
 |          vtkMRMLModelNode *modelNodeToUpdate=NULL)
 |  
 ...</code></pre>

---

## Post #3 by @hgueziri (2017-07-11 23:31 UTC)

<p>Perfect. I’ll try that tomorrow.</p>
<p>Thanks Andras</p>

---
