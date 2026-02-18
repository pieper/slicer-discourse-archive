# Event about vtkMRMLModelNode

**Topic ID**: 25744
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/event-about-vtkmrmlmodelnode/25744

---

## Post #1 by @miniminic (2022-10-18 03:24 UTC)

<p>In the logic of my custom module, I can know that a new node has been added to the scene by OnMRMLSceneNodeAdded. For example, vtkMRMLModelNode, I can tell that a vtkMRMLMOdelNode was created and its displayNode was created, but they are not bound together at this point, So I can’t get displayNode from vtkMRMLModelNode in OnMRMLSceneNodeAdded or vtkMRMLDisplayableNode from displayNode. What event should I use to get a vtkMRMLModelNode that has completed initialization。 thaks。<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73ed2a863a901a6d66b9942af5dbeb44139ca3ca.jpeg" data-download-href="/uploads/short-url/gxx2b7iA4KEzd87NgDD8voTEDpM.jpeg?dl=1" title="屏幕截图 2022-10-18 112243" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73ed2a863a901a6d66b9942af5dbeb44139ca3ca_2_690x261.jpeg" alt="屏幕截图 2022-10-18 112243" data-base62-sha1="gxx2b7iA4KEzd87NgDD8voTEDpM" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73ed2a863a901a6d66b9942af5dbeb44139ca3ca_2_690x261.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73ed2a863a901a6d66b9942af5dbeb44139ca3ca_2_1035x391.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73ed2a863a901a6d66b9942af5dbeb44139ca3ca.jpeg 2x" data-dominant-color="232524"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-10-18 112243</span><span class="informations">1044×395 61.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
displayNode and displayableNode are nullptr</p>

---

## Post #2 by @cpinter (2022-10-18 10:52 UTC)

<aside class="quote no-group" data-username="miniminic" data-post="1" data-topic="25744">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miniminic/48/16647_2.png" class="avatar"> miniminic:</div>
<blockquote>
<p>new node has been added to the scene</p>
</blockquote>
</aside>
<p>In your case what adds new nodes to the scene? What is the use case?</p>

---

## Post #3 by @miniminic (2022-10-19 02:53 UTC)

<p>I wanted to make it possible to move when a model was added, so I added the following code to logic.</p>
<pre><code class="lang-auto">	void vtkSlicerMaterialDatabaseLogic
::OnMRMLSceneNodeAdded(vtkMRMLNode* node)
{
	auto modelNode = vtkMRMLModelNode::SafeDownCast(node);
	if (nullptr != modelNode)
	{
		auto* transform = vtkMRMLTransformNode::SafeDownCast(node-&gt;GetScene()-&gt;AddNewNodeByClass("vtkMRMLTransformNode"));
		if (nullptr != transform)
		{
			transform-&gt;CreateDefaultDisplayNodes();
			modelNode-&gt;SetAndObserveTransformNodeID(transform-&gt;GetID());
			auto transformDisplay = vtkMRMLTransformDisplayNode::SafeDownCast(transform-&gt;GetDisplayNode());
			if (nullptr != transformDisplay)
			{
				transformDisplay-&gt;SetEditorVisibility(true);
				transformDisplay-&gt;UpdateEditorBounds();
			}
		}
	}
}
</code></pre>
<p>But when I call UpdateEditorBounds, modelNode doesn’t have a displayNode yet.<br>
But I am now using vtkMRMLModelNode: : DisplayModifiedEvent solved the problem。</p>
<pre><code class="lang-auto">void qSlicerMaterialDatabaseModule::onVtkMRMLModelDisplayNodeAdd(vtkMRMLModelNode* node)
{
	Q_D(qSlicerMaterialDatabaseModule);

	if (nullptr != node &amp;&amp; nullptr != d-&gt;Widget &amp;&amp; 0 != d-&gt;Widget-&gt;getLastDorpAction())
	{
		d-&gt;Widget-&gt;resetLastDropAction();

		d-&gt;ModelNode = node;
		this-&gt;qvtkConnect(d-&gt;ModelNode, vtkMRMLModelNode::DisplayModifiedEvent, this, SLOT(onDisplayModifiedEvent()));
	}
}

void qSlicerMaterialDatabaseModule::onDisplayModifiedEvent()
{
	Q_D(qSlicerMaterialDatabaseModule);
	if (nullptr != d-&gt;ModelNode)
	{
		this-&gt;qvtkDisconnect(d-&gt;ModelNode, vtkMRMLModelNode::DisplayModifiedEvent, this, SLOT(onDisplayModifiedEvent()));

		auto* transform = vtkMRMLTransformNode::SafeDownCast(d-&gt;ModelNode-&gt;GetScene()-&gt;AddNewNodeByClass("vtkMRMLTransformNode"));
		if (nullptr != transform)
		{
			transform-&gt;CreateDefaultDisplayNodes();
			d-&gt;ModelNode-&gt;SetAndObserveTransformNodeID(transform-&gt;GetID());
			auto transformDisplay = vtkMRMLTransformDisplayNode::SafeDownCast(transform-&gt;GetDisplayNode());
			if (nullptr != transformDisplay)
			{
				transformDisplay-&gt;SetEditorVisibility(true);
				transformDisplay-&gt;UpdateEditorBounds();
			}
		}

		d-&gt;ModelNode = nullptr;
	}
}
</code></pre>

---

## Post #4 by @lassoan (2022-10-19 04:59 UTC)

<p>It probably makes sense to not react immediately when the new node is created but when the application has performed all the processing and becomes idle. You can do that by using QTimer as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">this script repository example</a>.</p>

---
