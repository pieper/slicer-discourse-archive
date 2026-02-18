# On Model Cutting, I want to get the cut part and the cut part when cutting the model

**Topic ID**: 26295
**Date**: 2022-11-18
**URL**: https://discourse.slicer.org/t/on-model-cutting-i-want-to-get-the-cut-part-and-the-cut-part-when-cutting-the-model/26295

---

## Post #1 by @miniminic (2022-11-18 04:29 UTC)

<p>vtkClipPolyData can get two outputs, so at first, I used vtkClipPolyData to cut the model, but the model cut out by vtkClipPolyData was hollow, and the sum of the volumes of the two outputs had a big error with the original model.</p>
<p>So I used vtkClipClosedSurface to cut the model instead, but vtkClipClosedSurface only produced one output. In order to solve the problem of my idea is to use vtkBooleanOperationPolyDataFilter on the original model and the generated model for poor.</p>
<p>But I seem to be stuck in the vtkBooleanOperationPolyDataFilter: : update method.</p>
<p>My code is as follows:</p>
<pre><code class="lang-auto">vtkMRMLModelNode* sourceNode = vtkMRMLModelNode::SafeDownCast(mrmlScene-&gt;GetNodeByID(charNodeID));
	if (nullptr != sourceNode)
	{
		this-&gt;isClipped = true;
		d-&gt;appendButton-&gt;setEnabled(false);
		d-&gt;deleteButton-&gt;setEnabled(true);
		d-&gt;clipButton-&gt;setEnabled(!this-&gt;isClipped);

		
		this-&gt;appendPlane();
#if 1
		auto result1 = clipHelp(sourceNode);

		vtkSmartPointer&lt;vtkBooleanOperationPolyDataFilter&gt; boolFilter = vtkSmartPointer&lt;vtkBooleanOperationPolyDataFilter&gt;::New();
		boolFilter-&gt;SetOperation(vtkBooleanOperationPolyDataFilter::VTK_DIFFERENCE);

		boolFilter-&gt;SetInputData(0, sourceNode-&gt;GetPolyData());
		boolFilter-&gt;SetInputData(1, result1-&gt;GetPolyData());
		boolFilter-&gt;Update();	//It's stuck here
		auto result2PolyData = boolFilter-&gt;GetOutput();

		vtkSmartPointer&lt;vtkMRMLModelNode&gt; result2 = vtkSmartPointer&lt;vtkMRMLModelNode&gt;::New();
		QString resultName = tr("Result Part_");
		resultName.append(QString::number(this-&gt;timeOfClip));
		result2-&gt;SetName(resultName.toLatin1().data());
		result2-&gt;SetAndObservePolyData(result2PolyData);
		result2-&gt;SetScene(mrmlScene);

		vtkSmartPointer&lt;vtkMRMLModelDisplayNode&gt; resultDisplay = vtkSmartPointer&lt;vtkMRMLModelDisplayNode&gt;::New();
		vtkSmartPointer&lt;vtkMRMLModelStorageNode&gt; resultStorage = vtkSmartPointer&lt;vtkMRMLModelStorageNode&gt;::New();
		resultDisplay-&gt;SetScene(mrmlScene);
		resultStorage-&gt;SetScene(mrmlScene);
		resultDisplay-&gt;SetInputPolyDataConnection(result2-&gt;GetPolyDataConnection());
		resultStorage-&gt;SetFileName(resultName.toLatin1().data());
		mrmlScene-&gt;AddNode(resultDisplay);
		mrmlScene-&gt;AddNode(resultStorage);
		resultDisplay-&gt;SetColor(1.0, 0.0, 0.0);
		result2-&gt;SetAndObserveDisplayNodeID(resultDisplay-&gt;GetID());
		result2-&gt;SetAndObserveStorageNodeID(resultStorage-&gt;GetID());
		mrmlScene-&gt;AddNode(result2);

		this-&gt;deleteSurface();

		//设置在同一分组下
		auto shNode = mrmlScene-&gt;GetSubjectHierarchyNode();
		if (nullptr != shNode)
		{
			auto groupName = std::string(sourceNode-&gt;GetName()) + "_Clip";
			auto parent = shNode-&gt;GetItemByName(groupName);
			if (0 == parent)
				parent = mrmlScene-&gt;GetSubjectHierarchyNode()-&gt;CreateFolderItem(mrmlScene-&gt;GetSubjectHierarchyNode()-&gt;GetSceneItemID(), groupName);

			if (0 != parent &amp;&amp; nullptr != result1)
				mrmlScene-&gt;GetSubjectHierarchyNode()-&gt;SetItemParent(mrmlScene-&gt;GetSubjectHierarchyNode()-&gt;GetItemByDataNode(result1), parent);

			if (0 != parent &amp;&amp; nullptr != result2)
				mrmlScene-&gt;GetSubjectHierarchyNode()-&gt;SetItemParent(mrmlScene-&gt;GetSubjectHierarchyNode()-&gt;GetItemByDataNode(result2), parent);
		}

		auto sourceDisplayNode = sourceNode-&gt;GetModelDisplayNode();
		//隐藏被剪切的model
		if (nullptr != sourceDisplayNode)
			sourceDisplayNode-&gt;SetVisibility(false);
</code></pre>
<p>Can someone help me, or do I have a better way to get two closed cut solid models and cut solid models after cutting models?</p>

---

## Post #2 by @lassoan (2022-11-19 17:39 UTC)

<p>vtkBooleanOperationPolyDataFilter does not work: it fails randomly for completely valid inputs, therefore I would not recommend using that.</p>
<p>Instead, you can use the much more robust Combine Models module in Sandbox extension.</p>

---

## Post #3 by @miniminic (2022-11-20 02:16 UTC)

<p>Thank you. I’ll try this extension</p>

---

## Post #4 by @miniminic (2022-11-22 03:10 UTC)

<p>Sorry to bother you, I didn’t find Combine Models in the extension module, where do I get it<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82c01bc313528a44f4087d6ed5fca182c10b6314.jpeg" data-download-href="/uploads/short-url/iEFF1cPZH7wZ4FFsE6o4qwwc2c4.jpeg?dl=1" title="屏幕截图 2022-11-22 111028" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c01bc313528a44f4087d6ed5fca182c10b6314_2_690x426.jpeg" alt="屏幕截图 2022-11-22 111028" data-base62-sha1="iEFF1cPZH7wZ4FFsE6o4qwwc2c4" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c01bc313528a44f4087d6ed5fca182c10b6314_2_690x426.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c01bc313528a44f4087d6ed5fca182c10b6314_2_1035x639.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82c01bc313528a44f4087d6ed5fca182c10b6314.jpeg 2x" data-dominant-color="DFE0E2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-11-22 111028</span><span class="informations">1246×771 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-11-22 03:13 UTC)

<p>The extension’s name is <code>Sandbox</code>. You will find <code>Combine models</code> module in the module finder after you installed the extension.</p>

---

## Post #6 by @miniminic (2022-11-22 03:21 UTC)

<p>All right, thank you very much</p>

---
