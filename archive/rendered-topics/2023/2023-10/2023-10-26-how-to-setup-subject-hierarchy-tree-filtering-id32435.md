# How to setup subject hierarchy tree filtering?

**Topic ID**: 32435
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/how-to-setup-subject-hierarchy-tree-filtering/32435

---

## Post #1 by @jamesobutler (2023-10-26 22:53 UTC)

<p>I’m currently having difficulty filtering the subject hierarchy using the attribute filter API. The following illustrates the unexpected behavior upon using <code>setAttributeFilter</code>. Does anyone know why this may be happening?</p>
<pre><code class="lang-python">tree_view = slicer.qMRMLSubjectHierarchyTreeView()
tree_view.setMRMLScene(slicer.mrmlScene)
line_node_1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "Line1")
line_node_2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "Line2")
line_node_1.SetAttribute("Name", "Value")
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b5779bf066d4a36d0e6790275f4c303342b6360.png" alt="image" data-base62-sha1="3TSj33Z6BCnFtxhemXu8P1EE1XO" width="431" height="224"></p>
<p><code>tree_view.displayedItemCount()</code> is 2</p>
<pre><code class="lang-python">tree_view.setAttributeFilter("Name", "Value")
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8ff42fcdd4396867cdabc388de9cfdbc74f16bb9.png" alt="image" data-base62-sha1="kxtrEbYA8PrmfFjkSy79ns9jhbj" width="431" height="224"></p>
<p><code>tree_view.displayedItemCount()</code> is 0, although it was expected to be 1.</p>

---

## Post #2 by @jcfr (2023-10-27 01:53 UTC)

<p>You may also want to look in the recent  changes related to filtering that were introduced in <a href="https://github.com/Slicer/Slicer/pull/7289" class="inline-onebox">BUG: Fix SubjectHierarchyGenericSelfTest by cpinter · Pull Request #7289 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @cpinter (2023-10-27 08:47 UTC)

<p>The <code>setAttributeFilter</code> method sets an attribute filter for <em>items</em> and not nodes. This is why when you set a node attribute but then were filtering on item attribute it did not show anything. It is also deprecated. See</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L88-L90">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L88-L90" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L88-L90" target="_blank" rel="noopener">Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L88-L90</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="88" style="counter-reset: li-counter 87 ;">
          <li>/// Filter to show only items that contain an attribute with this name. Empty by default</li>
          <li>/// Note: Deprecated, kept only for backwards compatibility. Sets and returns the first attribute in \sa includeNodeAttributeNamesFilter</li>
          <li>Q_PROPERTY(QString attributeNameFilter READ attributeNameFilter WRITE setAttributeNameFilter)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please use these properties instead:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L73-L86">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L73-L86" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L73-L86" target="_blank" rel="noopener">Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L73-L86</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="73" style="counter-reset: li-counter 72 ;">
          <li>/// Filter to show only items that contain any of the given attributes with this name. Empty by default.</li>
          <li>/// When setting it, all the include filters are overwritten.</li>
          <li>Q_PROPERTY(QStringList includeItemAttributeNamesFilter READ includeItemAttributeNamesFilter WRITE setIncludeItemAttributeNamesFilter)</li>
          <li>/// Filter to show only items for data nodes that contain any of the given attributes with this name. Empty by default.</li>
          <li>/// When setting it, all the include filters are overwritten.</li>
          <li>Q_PROPERTY(QStringList includeNodeAttributeNamesFilter READ includeNodeAttributeNamesFilter WRITE setIncludeNodeAttributeNamesFilter)</li>
          <li>/// Filter to hide items that contain any of the given attributes with this name. Empty by default.</li>
          <li>/// When setting it, all the include filters are overwritten.</li>
          <li>/// Overrides \sa includeItemAttributeNamesFilter</li>
          <li>Q_PROPERTY(QStringList excludeItemAttributeNamesFilter READ excludeItemAttributeNamesFilter WRITE setExcludeItemAttributeNamesFilter)</li>
          <li>/// Filter to hide items for data nodes that contain any of the given attributes with this name. Empty by default.</li>
          <li>/// When setting it, all the include filters are overwritten.</li>
          <li>/// Overrides \sa includeNodeAttributeNamesFilter</li>
          <li>Q_PROPERTY(QStringList excludeNodeAttributeNamesFilter READ excludeNodeAttributeNamesFilter WRITE setExcludeNodeAttributeNamesFilter)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The node and item attribute filters have their different properties, as well as their include and exclude variants.</p>

---

## Post #4 by @jamesobutler (2023-10-27 11:37 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Is that deprecation comment wrong in that it says <code>Sets and returns the first attribute in \sa includeNodeAttributeNamesFilter</code> when actually it should be <code>Sets and returns the first attribute in \sa includeItemAttributeNamesFilter</code>?</p>
<p>Also does this mean the non-deprecated API can only filter by attribute name and not also by attribute value like <code>SetAttributeFilter</code> could do?</p>

---

## Post #5 by @cpinter (2023-10-27 12:06 UTC)

<ol>
<li>
<p>You’re right, the comment is referencing the wrong function, it should be <code>includeItemAttributeNamesFilter</code>.</p>
</li>
<li>
<p>No, you can still filter by value, see</p>
</li>
</ol>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L115-L139">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L115-L139" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L115-L139" target="_blank" rel="noopener">Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L115-L139</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="115" style="counter-reset: li-counter 114 ;">
          <li>/// Add single item attribute filter specifying attribute name, value, include/exclude, and class name</li>
          <li>/// \param attributeName Name of the item attribute to filter</li>
          <li>/// \param attributeValue Value of the item attribute to filter</li>
          <li>/// \param include Flag indicating whether this is an include filter or exclude filter.</li>
          <li>///   - Include filter means that only the items are shown that match the filter.</li>
          <li>///   - Exclude filter hides items that match the filter. Overrides include filters.</li>
          <li>///   True by default (i.e. include filter).</li>
          <li>Q_INVOKABLE void addItemAttributeFilter(QString attributeName, QVariant attributeValue=QString(), bool include=true);</li>
          <li>/// Remove single item attribute filter specifying each attribute \sa addAttributeFilter</li>
          <li>Q_INVOKABLE void removeItemAttributeFilter(QString attributeName, QVariant attributeValue, bool include);</li>
          <li>/// Remove all item attribute filters specifying a given attribute name and include flag</li>
          <li>Q_INVOKABLE void removeItemAttributeFilter(QString attributeName, bool include);</li>
          <li>/// Add single node attribute filter specifying attribute name, value, include/exclude, and class name</li>
          <li>/// \param attributeName Name of the node attribute to filter</li>
          <li>/// \param attributeValue Value of the node attribute to filter</li>
          <li>/// \param include Flag indicating whether this is an include filter or exclude filter.</li>
          <li>///   - Include filter means that only the items are shown that match the filter.</li>
          <li>///   - Exclude filter hides items that match the filter. Overrides include filters.</li>
          <li>///   True by default (i.e. include filter).</li>
          <li>/// \param className Only filter attributes on a certain type. Empty by default (i.e. allow all classes)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/3f46b467d3cde16d0d60e0e059439eea2728a967/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.h#L115-L139" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I think the best thing to do would be to fix that comment in (1), and add an actual deprecation warning in the bodies of <code>setAttributeNameFilter</code> and <code>setAttributeValueFilter</code>.</p>

---

## Post #6 by @jamesobutler (2023-10-27 12:38 UTC)

<p>Yes I agree with those improvements.</p>
<p>Since there are some methods specific to items and others for nodes it was getting a bit confusing. I was thinking of “item” as a generic term about a thing in a list of things which could be a node object.</p>

---

## Post #7 by @jamesobutler (2023-10-27 14:05 UTC)

<p>Here’s an update to my original example code that shows how to successfully filter using node attributes.</p>
<pre><code class="lang-python">tree_view = slicer.qMRMLSubjectHierarchyTreeView()
tree_view.setMRMLScene(slicer.mrmlScene)
line_node_1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "Line1")
line_node_2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "Line2")
line_node_1.SetAttribute("Name", "Value")
tree_view.displayedItemCount()  # 2

tree_view.addNodeAttributeFilter("Name", "Value")
tree_view.displayedItemCount()  # 1

tree_view.removeNodeAttributeFilter("Name", "Value")
tree_view.displayedItemCount()  # 2
</code></pre>

---

## Post #8 by @jcfr (2023-10-31 02:10 UTC)

<p>The following should help clarify</p>
<ol>
<li>
<p>Create the tree view</p>
<pre data-code-wrap="python"><code class="lang-python">tree_view = slicer.qMRMLSubjectHierarchyTreeView()
tree_view.setMRMLScene(slicer.mrmlScene)
line_node_1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "Line1")
line_node_2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "Line2")

assert tree_view.displayedItemCount() == 2
</code></pre>
</li>
<li>
<p>Set the node attribute</p>
<p><em><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> Adding a node attribute is different from a subject hierarchy item attribute</em></p>
<pre data-code-wrap="python"><code class="lang-python">line_node_1.SetAttribute("Name", "Value")
</code></pre>
</li>
<li>
<p>Add a subject hierarchy item attribute fltter</p>
<pre data-code-wrap="python"><code class="lang-python">tree_view.addItemAttributeFilter("Name", "Value")
</code></pre>
<p>… and as “expected” there are no item displayed</p>
<pre data-code-wrap="python"><code class="lang-python">assert tree_view.displayedItemCount() == 0
</code></pre>
</li>
<li>
<p>Set the subject hierarchy item attribute</p>
<pre data-code-wrap="python"><code class="lang-python">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
shItem1 = shNode.GetItemByDataNode(line_node_1)
shItem2 = shNode.GetItemByDataNode(line_node_2)

shNode.SetItemAttribute(shItem1, "Name", "Value")

# After setting the corrresponding item attribute, the items are filtered as expected
assert tree_view.displayedItemCount() == 1
</code></pre>
</li>
</ol>

---

## Post #9 by @jcfr (2023-11-15 18:14 UTC)

<p>For reference, deprecation warnings and improved documentation are being integrated through the following pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7314">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7314" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7314" target="_blank" rel="noopener">Improve documentation of obsolete filtering API in SH proxy model</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>cpinter:sh-attribute-filter-deprecation</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-30" data-time="13:31:07" data-timezone="UTC">01:31PM - 30 Oct 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="2 commits changed 4 files with 22 additions and 15 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7314/files" target="_blank" rel="noopener">
            <span class="added">+22</span>
            <span class="removed">-15</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Re https://discourse.slicer.org/t/problems-filtering-subject-hierarchy-tree/3243<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7314" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">5/5</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
