# Multiple node export now supported

**Topic ID**: 21681
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/multiple-node-export-now-supported/21681

---

## Post #1 by @ebrahim (2022-01-28 14:59 UTC)

<p>This is a follow up on <a href="https://discourse.slicer.org/t/new-export-functionality/20950" class="inline-onebox">New export functionality</a></p>
<p>Exporting multiple nodes is now supported. Right click on a node in the data subject hierarchy, and you should see “Export as…” show up if the clicked node can be exported, <em>or</em> if it has at least one descendant in the hierarchy that can be exported.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dadea59b12d2630c3445b49385a21ac687afc06e.png" alt="export_multiple_feature" data-base62-sha1="ved6EB7lCoYUw4U7feT6FqsTPaK" width="545" height="315"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/551b51d410f3c1f752530000921433b1c4b3284d.png" alt="export_multiple_feature2" data-base62-sha1="c8T7fWDT3078A3Z6T5RVj2sQgkl" width="469" height="500"></p>
<p>A format and options selector will show up for each node <em>type</em>. So, for example, if all the nodes under a folder have the same type, then there would only be one format and options selector.</p>
<p>As is visible in the screenshot, filename entry is disabled when exporting more than one node. Node name is used automatically.</p>
<p>When it is relevant, a checkbox will show up to let you choose whether or not to include children of the selected item. Another checkbox can also show up to let you choose whether to include children <em>recursively</em> (i.e. include all descendants in the subject hierarchy).</p>
<p>Thanks to <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, and <a class="mention" href="/u/pieper">@pieper</a> for their feedback and support throughout this work!</p>
<p>Comments and questions are welcome.</p>

---

## Post #2 by @agporto (2023-07-06 23:59 UTC)

<p>This is great. Is there a way to obtain similar functionality from the python interactor within Slicer?</p>

---

## Post #3 by @ebrahim (2023-07-07 10:53 UTC)

<p>Exporting a single node can be done with <code>slicer.util.exportNode</code>:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file</a></p>
<p>Exporting multiple nodes is not exposed through the nice <code>slicer.util</code> module, but you could always see how <code>qSlicerCoreIOManager::exportNodes</code> is accessed internally in <code>slicer.util.exportNode</code> and follow that as a guide:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/f541fb5e068169cf3709873471c88764630059f4/Base/Python/slicer/util.py#L1128">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/f541fb5e068169cf3709873471c88764630059f4/Base/Python/slicer/util.py#L1128" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f541fb5e068169cf3709873471c88764630059f4/Base/Python/slicer/util.py#L1128" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/f541fb5e068169cf3709873471c88764630059f4/Base/Python/slicer/util.py#L1128</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1118" style="counter-reset: li-counter 1117 ;">
          <li>    for fileFormat in fileWriterExtensions:</li>
          <li>        extension = vtkDataFileFormatHelper.GetFileExtensionFromFormatString(fileFormat)</li>
          <li>        if extension == currentExtension:</li>
          <li>            foundFileFormat = fileFormat</li>
          <li>            break</li>
          <li>    if not foundFileFormat:</li>
          <li>        raise ValueError(f"Failed to export {node.GetID()} - no known file format was found for filename {filename}")</li>
          <li>    properties["fileFormat"] = foundFileFormat</li>
          <li></li>
          <li>userMessages = vtkMRMLMessageCollection()</li>
          <li class="selected">success = app.coreIOManager().exportNodes(nodeIDs, fileNames, properties, hardenTransform, userMessages)</li>
          <li></li>
          <li>if not success:</li>
          <li>    import logging</li>
          <li>    errorMessage = f"Failed to export node to file: {filename}"</li>
          <li>    if userMessages.GetNumberOfMessages() &gt; 0:</li>
          <li>        errorMessage += "\n" + userMessages.GetAllMessagesAsString()</li>
          <li>    logging.error(errorMessage)</li>
          <li></li>
          <li>return success</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The script repository also shows a python implementation of a similar functionality using single node export:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-files-to-directory-structure-matching-subject-hierarchy-folders" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-files-to-directory-structure-matching-subject-hierarchy-folders</a></p>

---

## Post #4 by @agporto (2023-07-07 16:25 UTC)

<p>Perfect. Thanks <a class="mention" href="/u/ebrahim">@ebrahim</a></p>

---
