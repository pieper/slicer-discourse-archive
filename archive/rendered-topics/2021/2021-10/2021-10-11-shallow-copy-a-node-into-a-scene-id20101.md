# Shallow copy a node into a scene

**Topic ID**: 20101
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/shallow-copy-a-node-into-a-scene/20101

---

## Post #1 by @ebrahim (2021-10-11 16:56 UTC)

<p>I’ve created a scene and I want to copy nodes from the current scene into my new scene.<br>
But I don’t want to copy any underlying bulk data in the nodes. I want new nodes that refer to the same underlying data when there is any. Is this possible in the current api with <code>vtkMRMLScene</code> or <code>vtkMRMLNode</code>?</p>
<p><code>vtkMRMLScene::CopyNode</code> seems to do a deep copy.</p>

---

## Post #2 by @jcfr (2021-10-11 17:19 UTC)

<p>Looking at the <code>CopyContent</code> function should be helpful:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/03e913587bf7b78990f0224bc77818e3ed31d5d3/Libs/MRML/Core/vtkMRMLNode.h#L237-L246">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/03e913587bf7b78990f0224bc77818e3ed31d5d3/Libs/MRML/Core/vtkMRMLNode.h#L237-L246" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/03e913587bf7b78990f0224bc77818e3ed31d5d3/Libs/MRML/Core/vtkMRMLNode.h#L237-L246" target="_blank" rel="noopener">Slicer/Slicer/blob/03e913587bf7b78990f0224bc77818e3ed31d5d3/Libs/MRML/Core/vtkMRMLNode.h#L237-L246</a></h4>



  <pre class="onebox">    <code class="lang-h">
      <ol class="start lines" start="237" style="counter-reset: li-counter 236 ;">
          <li>/// \brief Copy node contents from another node of the same type.</li>
          <li>/// Does not copy node ID, Scene, Name, SingletonTag, HideFromEditors, AddToScene, UndoEnabled,</li>
          <li>/// and node references.</li>
          <li>/// If deepCopy is set to false then a shallow copy of bulk data (such as image or mesh data) could be made;</li>
          <li>/// copying may be faster but the node may share some data with the source node instead of creating</li>
          <li>/// an independent copy.</li>
          <li>/// \note</li>
          <li>/// If a class implements this then make sure CopyContent and HasCopyContent methods are implemented</li>
          <li>/// in all parent classes by adding vtkMRMLCopyContentMacro(ClassName) to the class headers.</li>
          <li>virtual void CopyContent(vtkMRMLNode* node, bool deepCopy=true);</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ebrahim (2021-10-11 18:05 UTC)

<p>I thought this might help, but the <code>deepCopy</code> parameter <a href="https://github.com/Slicer/Slicer/blob/03e913587bf7b78990f0224bc77818e3ed31d5d3/Libs/MRML/Core/vtkMRMLNode.cxx#L132-L140" rel="noopener nofollow ugc">doesn’t get used</a>. And I’m not seeing <code>CopyContent</code> get overriden by descendants of <code>vtkMRMLNode</code>. Maybe I am missing something-- I will test and see if it really does a shallow copy.</p>

---

## Post #4 by @ebrahim (2021-10-11 19:14 UTC)

<p>I was indeed missing something:<br>
<code>CopyContent</code> does get overriden, the override was just tucked into the macro <code>vtkMRMLCopyContentMacro</code>.</p>
<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>, I think this should do what I need!</p>

---
