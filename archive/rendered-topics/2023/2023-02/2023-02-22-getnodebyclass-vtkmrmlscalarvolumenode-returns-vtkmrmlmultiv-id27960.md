---
topic_id: 27960
title: "Getnodebyclass Vtkmrmlscalarvolumenode Returns Vtkmrmlmultiv"
date: 2023-02-22
url: https://discourse.slicer.org/t/27960
---

# GetNodeByClass(vtkMRMLScalarVolumeNode) returns vtkMRMLMultiVolumeNode

**Topic ID**: 27960
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/getnodebyclass-vtkmrmlscalarvolumenode-returns-vtkmrmlmultivolumenode/27960

---

## Post #1 by @pearsonm (2023-02-22 00:23 UTC)

<p>Hi,</p>
<p>I am writing a module to process dynamic nuclear medicine images and I have an issue that might be a bug.</p>
<p>I load 2 DICOM datasets as vtkMRMLScalarVolumeNode but another module also creates a vtkMRMLMultiVolumeNode.</p>
<p>If I try to filter by GetNodesByClass all 3 nodes are returned. Is this the expected behavior?</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.mrmlScene.GetNodesByClass('vtkMRMLMultiVolumeNode').GetNumberOfItems()
1
&gt;&gt;&gt; slicer.mrmlScene.GetNodesByClass('vtkMRMLScalarVolumeNode').GetNumberOfItems()
3
</code></pre>
<p>Tested on Slicer stable and 5.3.0-2023-02-21</p>
<p>Mark</p>

---

## Post #2 by @jamesobutler (2023-02-22 01:44 UTC)

<p>What you’ve discovered is that vtkMRMLMultiVolumeNode is derived from vtkMRMLScalarVolumeNode. It is a type of vtkMRMLScalarVolumeNode.</p>
<p>If in your module you utilize a qMRMLNodeComboBox for selecting certain nodes in the mrml scene, you can specify to have show child nodes set to off which would exclude vtkMRMLMultiVolumeNodes from populating in this widget.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L125">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L125" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L125" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L125</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="115" style="counter-reset: li-counter 114 ;">
          <li>/// bypass the property and show the node anyway.</li>
          <li>inline void setShowHidden(bool);</li>
          <li>inline bool showHidden()const;</li>
          <li>
          <li>/// This property controls whether subclasses of \a nodeType</li>
          <li>/// are hidden or not. If false, only the nodes of 'final' type</li>
          <li>/// is \a nodeType are displayed, if true, all the nodes deriving</li>
          <li>/// from \a nodeType are visible except for the ones of</li>
          <li>/// type \a hideChildNodeTypes.</li>
          <li>/// true by default.</li>
          <li class="selected">inline void setShowChildNodeTypes(bool show);</li>
          <li>inline bool showChildNodeTypes()const;</li>
          <li>
          <li>/// If a node is a nodeType, hide the node if it is also</li>
          <li>/// a ExcludedChildNodeType. (this can happen if nodeType is a</li>
          <li>/// mother class of ExcludedChildNodeType)</li>
          <li>inline void setHideChildNodeTypes(const QStringList&amp; nodeTypes);</li>
          <li>inline QStringList hideChildNodeTypes()const;</li>
          <li>
          <li>/// Add node type attribute that filter the nodes to</li>
          <li>/// display. For example, colormap categories are defined with the "Category"</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I don’t believe the GetNodesByClass method has an option to exclude child nodes from being found. Therefore you might have to do this exclusion on your own afterwards.</p>

---

## Post #3 by @pearsonm (2023-02-22 03:32 UTC)

<p>Thanks,</p>
<p>In that case I will add a filter for ‘MultiVolume’ in GetClassName on my list of nodes.</p>

---
