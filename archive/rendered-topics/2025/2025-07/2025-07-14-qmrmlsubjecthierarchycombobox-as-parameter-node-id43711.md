---
topic_id: 43711
title: "Qmrmlsubjecthierarchycombobox As Parameter Node"
date: 2025-07-14
url: https://discourse.slicer.org/t/43711
---

# qMRMLSubjectHierarchyComboBox as parameter node

**Topic ID**: 43711
**Date**: 2025-07-14
**URL**: https://discourse.slicer.org/t/qmrmlsubjecthierarchycombobox-as-parameter-node/43711

---

## Post #1 by @Amy_Morton (2025-07-14 14:53 UTC)

<p>I’d like to programmatically assign a subject hierarchy group to a qMRMLSubjectHierarchyComboBox in my module. After setting SlicerParameterName property to hNode, in designer I add hNode to my parameterNodeWrapper</p>
<pre><code class="lang-auto">hNode:  vtkMRMLSubjectHierarchyNode
</code></pre>
<p>with appropriate import.</p>
<p>However… at module reload:</p>
<pre><code class="lang-auto">RuntimeError: Unable to create GUI connector from datatype '&lt;class 'MRMLCorePython.vtkMRMLSubjectHierarchyNode'&gt;' to widget type '&lt;class 'PythonQt.qSlicerSubjectHierarchyModuleWidgets.qMRMLSubjectHierarchyComboBox'&gt;'. To determine which data types can be connected to which widget types, please check 'canRepresent' methods in 'GuiConnector' classes in these files: C:\Users\amorton1\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\SubjectHierarchyLib\parameterNodeWrapper\guiConnectors.py,
</code></pre>
<p>Which indicates</p>
<pre><code class="lang-auto"> def canRepresent(widget, datatype) -&gt; bool:
        return type(widget) == qMRMLSubjectHierarchyTreeView and isNodeOrUnionOfNodes(datatype)
</code></pre>
<p>I’m a bit stuck</p>
<p>Is there an appropriate data type I can assign to hNode in my parameterNodeWrapper ?</p>

---

## Post #2 by @lassoan (2025-07-15 03:19 UTC)

<p>GUI connectors are not implemented for some less-frequently used widgets. I’ve added a GUI connector for this that can connect a MRML node to the subject hierarchy combobox:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8573">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8573" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8573" target="_blank" rel="noopener">ENH: Add parameter node GUI connector for qMRMLSubjectHierarchyComboBox</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:sh-combobox-gui-connector</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-15" data-time="03:17:08" data-timezone="UTC">03:17AM - 15 Jul 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 63 additions and 7 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8573/files" target="_blank" rel="noopener">
            <span class="added">+63</span>
            <span class="removed">-7</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Parameter node wrapper GUI connector was not implemented for many widgets (#7308<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8573" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">), including qMRMLSubjectHierarchyComboBox. This commit adds a connector that can read/write qMRMLSubjectHierarchyComboBox as a MRML node.

fixes #7905</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It would be great if you could test it.</p>

---

## Post #3 by @Amy_Morton (2025-07-15 13:52 UTC)

<p>Will do! Thank-you <a class="mention" href="/u/lassoan">@lassoan</a> !</p>

---
