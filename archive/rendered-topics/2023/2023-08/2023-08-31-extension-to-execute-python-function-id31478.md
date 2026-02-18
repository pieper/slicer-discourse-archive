# Extension to execute python function

**Topic ID**: 31478
**Date**: 2023-08-31
**URL**: https://discourse.slicer.org/t/extension-to-execute-python-function/31478

---

## Post #1 by @Deep_Learning (2023-08-31 15:35 UTC)

<p>Is there a simple extension available to execute python code.</p>
<p>Would be a great way to customize 3DSlicer and allow execution of custom code with a button.</p>
<p>I find my self using code such as this and it would be great to have a button up top…</p>
<p>def threeDDIsplay():<br>
import slicer<br>
segmentationNode = slicer.mrmlScene.GetFirstNodeByClass(‘vtkMRMLSegmentationNode’)<br>
segmentationNode.CreateClosedSurfaceRepresentation()<br>
layoutManager = slicer.app.layoutManager()<br>
threeDWidget = layoutManager.threeDWidget(0)<br>
threeDView = threeDWidget.threeDView()<br>
threeDView.resetFocalPoint()<br>
displayNode = segmentationNode.GetDisplayNode()<br>
displayNode.SetOpacity3D(0.3)<br>
print(‘3D’)</p>

---

## Post #2 by @pieper (2023-08-31 15:44 UTC)

<p>This example may help:</p>
<aside class="quote quote-modified" data-post="2" data-topic="31174">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-add-button-on-2d-or-3d-window/31174/2">How to add button on 2d or 3d window?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Good question - this code seems to work.  You’d need to add some extra code if you want to have it show up in the lower right corner and track window resizes and things. 
&gt;&gt;&gt; sliceButton = qt.QPushButton("Slice")
&gt;&gt;&gt; sliceButton.setParent(slicer.app.layoutManager().sliceWidget("Red"))
&gt;&gt;&gt; sliceButton.geometry = qt.QRect(0,0,200,200)
&gt;&gt;&gt; sliceButton.show()
&gt;&gt;&gt; 

 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c54542a96ae92de0579391f23d68793ac03ac01.png" data-download-href="/uploads/short-url/miX9R1SJPi8R861GTx51pdmPKCJ.png?dl=1" title="image">[image]</a>
  </blockquote>
</aside>


---
