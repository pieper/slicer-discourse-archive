---
topic_id: 42700
title: "How To Get A Scene Reliably And Why Is It Null"
date: 2025-04-26
url: https://discourse.slicer.org/t/42700
---

# How to get a scene reliably and why is it null?

**Topic ID**: 42700
**Date**: 2025-04-26
**URL**: https://discourse.slicer.org/t/how-to-get-a-scene-reliably-and-why-is-it-null/42700

---

## Post #1 by @chir.set (2025-04-26 17:07 UTC)

<p>Hello,</p>
<p>I am stumbling on getting a scene node in most functions of a class while it is not null elsewhere in the same class (<a href="https://github.com/chir-set/SlicerExtraMarkups/blob/2938b23ece62e3d8e58fb5afaf9ec1d118a6e453/Shape/MRML/vtkMRMLMarkupsShapeNode.cxx#L78" rel="noopener nofollow ugc">1</a>, <a href="https://github.com/chir-set/SlicerExtraMarkups/blob/2938b23ece62e3d8e58fb5afaf9ec1d118a6e453/Shape/MRML/vtkMRMLMarkupsShapeNode.cxx#L91" rel="noopener nofollow ugc">2</a>, <a href="https://github.com/chir-set/SlicerExtraMarkups/blob/2938b23ece62e3d8e58fb5afaf9ec1d118a6e453/Shape/MRML/vtkMRMLMarkupsShapeNode.cxx#L1228" rel="noopener nofollow ugc">3</a>).</p>
<p>In the constructor of the referenced class for example, it is always null, and in many functions also. The node is well <a href="https://github.com/chir-set/SlicerExtraMarkups/blob/2938b23ece62e3d8e58fb5afaf9ec1d118a6e453/Shape/Logic/vtkSlicerShapeLogic.cxx#L80" rel="noopener nofollow ugc">registered</a>.</p>
<p>Can a core developer provide a hint to resolve this?</p>
<p>Thank you.</p>

---

## Post #2 by @chir.set (2025-04-26 18:29 UTC)

<p>Precisions:</p>
<p>It 's on Linux and Slicer is built at de382bd89.</p>

---

## Post #3 by @Mik (2025-04-27 14:18 UTC)

<p>Have you tried this-&gt;Scene?<br>
Had your node already been added to the scene?</p>

---

## Post #4 by @pieper (2025-04-27 14:27 UTC)

<p>There’s a distinction between registering the node type so that the scene knows how to operate on it, and adding an instance of the node type to the scene.  The node class needs to know what scene it is in so it can do things like creating the default display and storage nodes, adding them to the scene, and referencing their IDs.</p>
<p>Some node methods, like <code>UpdateNumberOfControlPoints</code> you referenced, really should include a check for a null scene pointer.  Probably it’s not been added since that operation is unlikely to be called unless the node is already in use in a valid scene.</p>
<p>Does that address your question <a class="mention" href="/u/chir.set">@chir.set</a> ?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLScene.h#L131-L151">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLScene.h#L131-L151" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLScene.h#L131-L151" target="_blank" rel="noopener">Libs/MRML/Core/vtkMRMLScene.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLScene.h#L131-L151" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="131" style="counter-reset: li-counter 130 ;">
          <li>/// \brief Register a node class to the scene so that the scene can later</li>
          <li>/// create the same node type from a tag or a class name.</li>
          <li>///</li>
          <li>/// This is mainly used during scene loading.</li>
          <li>/// The XML element names are used to instantiate the nodes.</li>
          <li>///</li>
          <li>/// \a node is an instance of the class to instantiate when</li>
          <li>/// CreateNodeByClass() is called with a corresponding className retrieved</li>
          <li>/// using GetClassNameByTag().</li>
          <li>/// \a tagName can be 0 or an XML tag a custom tagName.</li>
          <li>/// If \a tagName is 0 (default), the \a node GetNodeTagName() is used.</li>
          <li>/// Otherwise, tagName is used.</li>
          <li>///</li>
          <li>/// The signature with tagName != 0 is useful to add support for</li>
          <li>/// scene backward compatibility. Calls with an obsolete tag should be</li>
          <li>/// wrapped with: &lt;code&gt;\#if MRML_APPLICATION_SUPPORT_VERSION &lt; 0x0X0Y0Z&lt;/code&gt; and &lt;code&gt;\#endif&lt;/code&gt;</li>
          <li>/// where X is the major version of Slicer scene to support, Y the minor and</li>
          <li>/// Z the patch version.</li>
          <li>///</li>
          <li>/// \sa CreateNodeByClass(), GetClassNameByTag()</li>
          <li>void RegisterNodeClass(vtkMRMLNode* node, const char* tagName);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @chir.set (2025-04-27 17:24 UTC)

<p>I have reworked parts of the project and things are more predictable now. Namely with <a href="https://github.com/chir-set/SlicerExtraMarkups/commit/afefb69878fc5d580e455c72e4d8ef7d3187de0a" rel="noopener nofollow ugc">this commit</a> that does nothing special now in a constructor, apart from an elementary assignment . A major cause of trouble was a <code>cout</code> statement in the constructor (the <code>cout</code> seemed elementary too <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=14" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"> ). This seemed very disturbing to whatever underneath, even the markups raw pointer was changing randomly. Once removed, things calmed down.</p>
<p>Thank you for having considered.</p>

---
