---
topic_id: 20733
title: "Multiple Display Nodes Observed By Scalar Volume Or Model"
date: 2021-11-22
url: https://discourse.slicer.org/t/20733
---

# Multiple display nodes observed by scalar volume or model

**Topic ID**: 20733
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/multiple-display-nodes-observed-by-scalar-volume-or-model/20733

---

## Post #1 by @Mik (2021-11-22 18:56 UTC)

<p>A couple of questions how things work:</p>
<ol>
<li>
<p>What class of object is responsible for visibility of display nodes when i click on visibility icon in subject hierarchy node browser?</p>
</li>
<li>
<p>What is the role of SubjectHierarchy plugin in selecting what display node will be displayed if there are many display node observed by a single scalar volume or model?</p>
</li>
</ol>
<p>I try to add support for <a href="https://github.com/Slicer/Slicer/issues/4891" rel="noopener nofollow ugc">color bars</a>, and after adding color bar display node to volume or model the behavior becomes very strange and possibly buggy.</p>
<p>Example for vtkMRMLScalarVolumeNode adds color bar display node, so volume node will have two display nodes (vtkMRMLScalarVolumeDisplayNode with index 0 and vtkMRMLColorBarDisplayNode with index 1), but when i click in subject hierarchy visibility icon the color bar display node is ignored and  a volume rendering display node is added and i can see a volume rendering on a 3D view. A list nodes is subject hierarchy node also shows that a volume rendering display node was added.</p>
<pre><code class="lang-auto">// Create color bar and observe color bar by displayable node
vtkMRMLColorBarDisplayNode* colorBarNode = vtkMRMLColorBarDisplayNode::SafeDownCast(mrmlScene-&gt;AddNewNodeByClass("vtkMRMLColorBarDisplayNode"));
if (colorBarNode)
  {
  colorBarNode-&gt;SetVisibility(true);
  dispNode-&gt;AddAndObserveDisplayNodeID(colorBarNode-&gt;GetID());
  return colorBarNode;
  }

</code></pre>
<p>Color bar for scalar volume by means of display node<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60915d7c710369cff3803db8a4546f17c1776d37.jpeg" data-download-href="/uploads/short-url/dMhhoIOaWrBOcMR9VDLnNZi2Hqf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60915d7c710369cff3803db8a4546f17c1776d37_2_690x345.jpeg" alt="image" data-base62-sha1="dMhhoIOaWrBOcMR9VDLnNZi2Hqf" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60915d7c710369cff3803db8a4546f17c1776d37_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60915d7c710369cff3803db8a4546f17c1776d37_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60915d7c710369cff3803db8a4546f17c1776d37_2_1380x690.jpeg 2x" data-dominant-color="5F5F68"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×961 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Subject hierarchy shows volume, volume display and color bar display nodes<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3da32a08cabe8e52241abdc8d7fad950ec35fe05.png" alt="image" data-base62-sha1="8NgHBMjlWDGtIeG7yjo5zOngzTT" width="368" height="163"></p>
<p>After toggle visibility on/off in subject hierarchy browser the volume rendering appears<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3def36a03f569546b3de726390c06c67eea5ada5.jpeg" data-download-href="/uploads/short-url/8PTDyuIAFt6vUChRBD8nFodpSVT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3def36a03f569546b3de726390c06c67eea5ada5_2_690x376.jpeg" alt="image" data-base62-sha1="8PTDyuIAFt6vUChRBD8nFodpSVT" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3def36a03f569546b3de726390c06c67eea5ada5_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3def36a03f569546b3de726390c06c67eea5ada5_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3def36a03f569546b3de726390c06c67eea5ada5_2_1380x752.jpeg 2x" data-dominant-color="65646B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1047 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-11-23 18:11 UTC)

<p>Thank you for your efforts on this. You have arrived to some intricate details that are indeed not easy to figure out.</p>
<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="20733">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>What class of object is responsible for visibility of display nodes when i click on visibility icon in subject hierarchy node browser?</p>
</blockquote>
</aside>
<p>The click is processed by the showVolumeInAllViews method of the subject hierarchy plugin that owns the associated data node. For volumes, it is the <a href="https://github.com/Slicer/Slicer/blob/56ebd8ee84557fe0c67e9db8fe0ddd771d799751/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L596"><code>qSlicerSubjectHierarchyVolumesPlugin</code></a>.</p>
<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="20733">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>What is the role of SubjectHierarchy plugin in selecting what display node will be displayed if there are many display node observed by a single scalar volume or model?</p>
</blockquote>
</aside>
<p>Most of Slicer’s GUI only modifies the first display node of each displayable node. Volume node is an exception, because it often has multiple display nodes (one for slice display in 2D and 3D views; and another one for volume rendering in 3D views). <code>qSlicerSubjectHierarchyVolumesPlugin</code> handles the eye button clicks (which toggles visibility of all display nodes), but <code>qSlicerSubjectHierarchyVolumeRenderingPlugin</code> plugin adds some more visibility menu items (“Show in 3D views as volume rendering”, “Volume rendering options”) and the volumes plugin calls the volume rendering plugin to handle showing of the item in 3D views.</p>
<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="20733">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>when i click in subject hierarchy visibility icon the color bar display node is ignored and a volume rendering display node is added</p>
</blockquote>
</aside>
<p>Volume rendering gets enabled because before your changes, if a display node was added for a volume that was not a vtkMRMLVolumeDisplayNode, it meant that it was a volume rendering display node. So, <a href="https://github.com/Slicer/Slicer/blob/56ebd8ee84557fe0c67e9db8fe0ddd771d799751/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L692">this</a> condition was correct. However, now that we can have color bar display nodes, this logic is not correct anymore. You can fix it by implementing these:</p>
<ul>
<li>Change <code>vtkMRMLVolumeDisplayNode::SafeDownCast(displayNode)</code> to <code>!displayNode-&gt;IsA("vtkMRMLVolumeRenderingDisplayNode")</code> so that the volume rendering plugin’s <a href="https://github.com/Slicer/Slicer/blob/56ebd8ee84557fe0c67e9db8fe0ddd771d799751/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L709">showItemInView</a> is only called if there is already a vtkMRMLVolumeRenderingDisplayNode.</li>
<li>Add a section below that is very similar to the volume rendering, but it manages display of the scalar bar for the volume, by delegating the task to the qSlicerSubjectHierarchyScalarBarPlugin’s showItemInView method. If you haven’t added a qSlicerSubjectHierarchyScalarBarPlugin then you need to add it now. It should be relatively easy to create a new subject hierarchy plugin (you can start with copying and modifying Modules\Loadable\VolumeRendering\SubjectHierarchyPlugins) and this plugin is useful anyway, for example it can add menu options to quickly show/hide scalar bar; or control basic display properties of the scalar bar.</li>
</ul>

---

## Post #3 by @Mik (2021-11-25 13:13 UTC)

<p>I will add the modifications for volumes and volume rendering.</p>
<p>Much more problem is adding a color bar display node to a model. The application is just crash if i add color bar to visible model.  I will try to debug the cause of it. It could be subject hierarchy plugin, some widget in models module or even model displayable manager.</p>

---
