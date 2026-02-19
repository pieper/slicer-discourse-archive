---
topic_id: 35072
title: "Deletion Of Vtkmrmlfolderdisplaynode"
date: 2024-03-25
url: https://discourse.slicer.org/t/35072
---

# Deletion of "vtkMRMLFolderDisplayNode"

**Topic ID**: 35072
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/deletion-of-vtkmrmlfolderdisplaynode/35072

---

## Post #1 by @Aamir_Khan1 (2024-03-25 19:54 UTC)

<p>Hi,</p>
<p>In my module, I create a folder using the following code:</p>
<pre><code class="lang-auto">    @staticmethod
    def create_folder_item_in_subject_hierarchy(serial_number):
        shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
        folder_name = serial_number + 'models'
        exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), folder_name)
        return exportFolderItemId
</code></pre>
<p>Then after performing some manipulations, I delete this folder using the following code:</p>
<pre><code class="lang-auto">    @staticmethod
    def remove_folder_display_node() -&gt; None:
       # folderDisplayNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLFolderDisplayNode")
        folderDisplayNode = slicer.util.getNodesByClass("vtkMRMLFolderDisplayNode")

        for node in folderDisplayNode:
            slicer.mrmlScene.RemoveNode(node)
</code></pre>
<p>The problem is that it doesn’t works.</p>
<p>It works after:</p>
<ol>
<li>Go to the Data Module.</li>
<li>Check the “Show MRML ID” box,</li>
<li>Toggle the visibility On then OFF then ON again</li>
<li>Then run the code for removing</li>
</ol>
<p>Is there a way that I can execute this without resorting to this 4 step hack?</p>

---

## Post #2 by @cpinter (2024-04-01 12:10 UTC)

<aside class="quote no-group" data-username="Aamir_Khan1" data-post="1" data-topic="35072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aamir_khan1/48/68485_2.png" class="avatar"> Aamir_Khan1:</div>
<blockquote>
<p><code>vtkMRMLFolderDisplayNode</code></p>
</blockquote>
</aside>
<p>The folder display node is only created if the user uses the show/hide function of the folder, or creates the display node explicitly (btw I’m pretty sure step 2 is not necessary).</p>
<p>To create the folder display node explicitly you can call this function</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Modules/Loadable/Models/Widgets/qMRMLModelDisplayNodeWidget.cxx#L323-L329">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Modules/Loadable/Models/Widgets/qMRMLModelDisplayNodeWidget.cxx#L323-L329" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Modules/Loadable/Models/Widgets/qMRMLModelDisplayNodeWidget.cxx#L323-L329" target="_blank" rel="noopener">Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Modules/Loadable/Models/Widgets/qMRMLModelDisplayNodeWidget.cxx#L323-L329</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="323" style="counter-reset: li-counter 322 ;">
          <li>// get folder plugin (can fail if subject hierarchy logic is not instantiated)</li>
          <li>qSlicerSubjectHierarchyFolderPlugin* folderPlugin = qobject_cast&lt;qSlicerSubjectHierarchyFolderPlugin*&gt;(</li>
          <li>  qSlicerSubjectHierarchyPluginHandler::instance()-&gt;pluginByName("Folder") );</li>
          <li>if (folderPlugin &amp;&amp; folderPlugin-&gt;canOwnSubjectHierarchyItem(currentItemID) &gt; 0.0)</li>
          <li>{</li>
          <li>  displayNode = folderPlugin-&gt;createDisplayNodeForItem(currentItemID);</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
