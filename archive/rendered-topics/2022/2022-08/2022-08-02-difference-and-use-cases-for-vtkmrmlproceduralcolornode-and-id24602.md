# Difference and use cases for `vtkMRMLProceduralColorNode` and `vtkMRMLColorTableNode`

**Topic ID**: 24602
**Date**: 2022-08-02
**URL**: https://discourse.slicer.org/t/difference-and-use-cases-for-vtkmrmlproceduralcolornode-and-vtkmrmlcolortablenode/24602

---

## Post #1 by @keri (2022-08-02 10:35 UTC)

<p>Hi,</p>
<p>I’m wondering what is the difference between <code>vtkMRMLProceduralColorNode</code> and <code>vtkMRMLColorTableNode</code>?<br>
For example I can see that <code>vtkMRMLColorTableNode</code> creates discrete color map while <code>vtkMRMLProceduralColorNode</code> creates continous.</p>
<p>Maybe they serve to different purposes?</p>

---

## Post #2 by @lassoan (2022-08-02 10:57 UTC)

<p>All these mode types can store both discrete and continuous (depending on what you set inside - color transfer function or lookup table).</p>
<p>Procedural color node is a special kind of color node that does not need to be saved into a file because the color function or table entries are generated programmatically.</p>

---

## Post #3 by @keri (2022-08-02 14:56 UTC)

<p>Thank you, that make sense</p>
<p>I just can’t find a method that triggers discrete or contigous color.<br>
This is my attemt that results in discrete color map:</p>
<pre><code class="lang-auto">  vtkNew&lt;vtkMRMLColorTableNode&gt; bwrColorTable;

  bwrColorTable-&gt;SetType(vtkMRMLColorTableNode::User);
  bwrColorTable-&gt;HideFromEditorsOff();  // make the color table selectable in the GUI outside Colors module
  bwrColorTable-&gt;SetSaveWithScene(true);
  bwrColorTable-&gt;SetNumberOfColors(5);
  bwrColorTable-&gt;GetLookupTable()-&gt;SetTableRange(0.,1.);

  bwrColorTable-&gt;SetColor(0, 0.0,     0.0,    0.5,    1.0);
  bwrColorTable-&gt;SetColor(1, 0.0,     0.375,  0.8314, 0.5);
  bwrColorTable-&gt;SetColor(2, 1.0,     1.0,    1.0,    0.0);
  bwrColorTable-&gt;SetColor(3, 0.8314,  0.375,  0.0,    0.5);
  bwrColorTable-&gt;SetColor(4, 0.5,     0.0,    0.0,    1.0);

  bwrColorTable-&gt;SetName("BWR");
  bwrColorTable-&gt;SetScene(this-&gt;GetMRMLScene());
  bwrColorTable-&gt;SetHideFromEditors(false);
  this-&gt;GetMRMLScene()-&gt;AddNode(bwrColorTable);
</code></pre>

---

## Post #4 by @lassoan (2022-08-29 03:34 UTC)

<p>You can find examples in the script repository:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-color-table-node">Create discrete color table</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-map-and-display-color-legend">Create continuous colormap</a></li>
</ul>

---
