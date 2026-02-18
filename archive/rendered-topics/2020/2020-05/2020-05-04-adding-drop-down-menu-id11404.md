# Adding drop down menu

**Topic ID**: 11404
**Date**: 2020-05-04
**URL**: https://discourse.slicer.org/t/adding-drop-down-menu/11404

---

## Post #1 by @rohan_n (2020-05-04 17:11 UTC)

<p>I’m currently developing a Python scripted module. Shortly after the module starts running, it pauses to allow the user to select a region of interest from an image by adjusting a vtkMRMLAnnotationROINode. I would like to add a dropdown menu that appears only during this paused for ROI selection stage so that the user can choose which image they want to display during ROI selection. I know how to load an image from a numpy array into a vtkMRMLScalarVolumeNode and then display that node. What I don’t know is:</p>
<p>-How to choose your own names for each vtkMRMLScalarVolumeNode<br>
-Python code to create a dropdown menu and how to make each selection from dropdown menu prompt display of a different image in Slicer window</p>
<p>Any help with syntax for this would be greatly appreciated.<br>
Thanks,<br>
Rohan</p>

---

## Post #2 by @lassoan (2020-05-04 21:23 UTC)

<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="11404">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>Shortly after the module starts running, it pauses to allow the user to select a region of interest from an image by adjusting a vtkMRMLAnnotationROINode.</p>
</blockquote>
</aside>
<p>I would not recommend to block the user and force him to do something, as it can easily get really frustrating for the user. Instead, you could follow the usual approach of Slicer modules: select inputs (using node selectors, sliders, etc.) and then click a button to process the inputs.</p>
<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="11404">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>How to choose your own names for each vtkMRMLScalarVolumeNode</p>
</blockquote>
</aside>
<p>You can select nodes using <a href="http://apidocs.slicer.org/master/classqMRMLNodeComboBox.html"><code>vtkMRMLNodeComboBox</code></a>. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">programming tutorial</a>.</p>
<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="11404">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>Python code to create a dropdown menu and how to make each selection from dropdown menu prompt display of a different image in Slicer window</p>
</blockquote>
</aside>
<p>You can add a <code>vtkMRMLNodeComboBox</code> to select a volume and connect to its <a href="http://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a8dd8b549f1331b93074beaa4cc9919d2"><code>currentNodeChanged</code></a> signal to a method in your class that changes what volume is displayed in slice views using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers"><code>slicer.util.setSliceViewerLayers</code></a>.</p>

---
