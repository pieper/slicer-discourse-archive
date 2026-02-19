---
topic_id: 37558
title: "Adding A New Color Table To Colors Permanently"
date: 2024-07-25
url: https://discourse.slicer.org/t/37558
---

# Adding a new color table to Colors, permanently

**Topic ID**: 37558
**Date**: 2024-07-25
**URL**: https://discourse.slicer.org/t/adding-a-new-color-table-to-colors-permanently/37558

---

## Post #1 by @phcerdan (2024-07-25 11:24 UTC)

<p>I want to add a custom color table to Slicer, and store it permanently, so I can open Volumes (Label Maps) with it.</p>
<p>Right now I am loading it on startup using <code>~/.slicerrc.py</code>, but I wonder if there is an alternative way?</p>
<pre data-code-wrap="python"><code class="lang-python">ctbl_file_path = '/path/mylut.ctbl'
# Create a new color node
color_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLColorTableNode')

# Read the color table from the file
color_table = slicer.vtkMRMLColorTableStorageNode()
color_table.SetFileName(ctbl_file_path)
color_table.ReadData(color_node)
color_node.SetName('MyAwesomeColorTable')
</code></pre>

---

## Post #2 by @cpinter (2024-08-02 12:33 UTC)

<p>In the past we added similar code to certain setup steps of our modules, such as</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx#L108">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx#L108" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx#L108" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx#L108</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="98" style="counter-reset: li-counter 97 ;">
          <li>//---------------------------------------------------------------------------
</li>
          <li>void vtkSlicerIsodoseModuleLogic::SetMRMLSceneInternal(vtkMRMLScene* newScene)
</li>
          <li>{
</li>
          <li>  vtkNew&lt;vtkIntArray&gt; events;
</li>
          <li>  events-&gt;InsertNextValue(vtkMRMLScene::NodeAddedEvent);
</li>
          <li>  events-&gt;InsertNextValue(vtkMRMLScene::NodeRemovedEvent);
</li>
          <li>  events-&gt;InsertNextValue(vtkMRMLScene::EndCloseEvent);
</li>
          <li>  events-&gt;InsertNextValue(vtkMRMLScene::EndBatchProcessEvent);
</li>
          <li>  this-&gt;SetAndObserveMRMLSceneEvents(newScene, events.GetPointer());
</li>
          <li>
</li>
          <li class="selected">  // Load (or create) default isodose color table
</li>
          <li>  vtkMRMLColorTableNode* isodoseColorTableNode = nullptr;
</li>
          <li>  if ( (isodoseColorTableNode = this-&gt;LoadDefaultIsodoseColorTable()) == nullptr )
</li>
          <li>  {
</li>
          <li>    isodoseColorTableNode = vtkSlicerIsodoseModuleLogic::GetDefaultIsodoseColorTable(newScene);
</li>
          <li>  }
</li>
          <li>  // Create a copy of default isodose color table. The copy can be edited.
</li>
          <li>  if (isodoseColorTableNode)
</li>
          <li>  {
</li>
          <li>    // Create a copy of isodose color table with unique name
</li>
          <li>    std::string uniqueName = this-&gt;GetMRMLScene()-&gt;GenerateUniqueName(vtkSlicerIsodoseModuleLogic::IsodoseColorNodeCopyUniqueName.c_str());
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The advantage of this to your approach is that anyone using the extension will have the custom color tables without extra steps. Of course this only works if you already maintain some modules that your group uses.</p>

---
