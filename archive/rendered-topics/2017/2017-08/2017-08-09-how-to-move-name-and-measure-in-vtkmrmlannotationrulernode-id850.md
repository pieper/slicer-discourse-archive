---
topic_id: 850
title: "How To Move Name And Measure In Vtkmrmlannotationrulernode"
date: 2017-08-09
url: https://discourse.slicer.org/t/850
---

# How to move name and measure in vtkMRMLAnnotationRulerNode

**Topic ID**: 850
**Date**: 2017-08-09
**URL**: https://discourse.slicer.org/t/how-to-move-name-and-measure-in-vtkmrmlannotationrulernode/850

---

## Post #1 by @PNardelli (2017-08-09 20:44 UTC)

<p>Hi guys,</p>
<p>I have created a new scripted module that uses two rulers to do measure airways and veins on a CT image.</p>
<p>I know the rulers’ name and measure are automatically placed next to the Ruler. However, many times these are on the way and make the measure difficult.</p>
<p>Do you know a way to make them selectable (I don’t see any appropriate function in the three display nodes of the rulers), so that they can be moved away when needed?</p>
<p>Thanks a lot,<br>
Pietro</p>

---

## Post #2 by @jcfr (2017-08-09 20:48 UTC)

<p>Hi Pietro,</p>
<p>It is not possible to directly move the text around. That said, as illustrated below, you could change the visibility, opacity or scale of the text.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44ce918753a1e4206798a384b09d6467ea6d6d2a.jpeg" data-download-href="/uploads/short-url/9OH2pwHibglXcJw4C98H63apWnU.jpg?dl=1" title="annotations-edit"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/44ce918753a1e4206798a384b09d6467ea6d6d2a_2_690x407.jpg" alt="annotations-edit" data-base62-sha1="9OH2pwHibglXcJw4C98H63apWnU" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/44ce918753a1e4206798a384b09d6467ea6d6d2a_2_690x407.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/44ce918753a1e4206798a384b09d6467ea6d6d2a_2_1035x610.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/44ce918753a1e4206798a384b09d6467ea6d6d2a_2_1380x814.jpg 2x" data-dominant-color="A8A8AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">annotations-edit</span><span class="informations">1440×851 326 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @PNardelli (2017-08-09 20:58 UTC)

<p>Hi JC,</p>
<p>thanks for your reply! OK, I see. And there is a way in python to at least remove the measure and just leave the name next to the ruler? Setting opacity to 0 removes both name and measure, but I need the name next to the ruler.</p>
<p>Thanks a lot,<br>
Pietro</p>

---

## Post #4 by @jcfr (2017-08-09 21:10 UTC)

<aside class="quote no-group" data-username="PNardelli" data-post="3" data-topic="850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c89c15/48.png" class="avatar"> PNardelli:</div>
<blockquote>
<p>remove the measure and just leave the name</p>
</blockquote>
</aside>
<p>Do you mean displaying only <code>41.7mm</code> instead of <code>M: 41.7mm</code> ?</p>

---

## Post #5 by @PNardelli (2017-08-09 21:14 UTC)

<p>Nope, the other way around, displaying only M instead of M: 41.7mm.</p>

---

## Post #6 by @jcfr (2017-08-09 21:33 UTC)

<p>It is not currently possible to selectively display one or the other.</p>
<p>The code responsible for formatting the “name: value” string can be found here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/2b815fafd3c730c189cc8b39bf453c669cab0c05/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationRulerDisplayableManager.cxx#L657-L688" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/2b815fafd3c730c189cc8b39bf453c669cab0c05/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationRulerDisplayableManager.cxx#L657-L688" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/2b815fafd3c730c189cc8b39bf453c669cab0c05/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationRulerDisplayableManager.cxx#L657-L688</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="657" style="counter-reset: li-counter 656 ;">
<li>std::string vtkMRMLAnnotationRulerDisplayableManager</li>
<li>::GetLabelFormat(vtkMRMLAnnotationRulerNode* rulerNode)</li>
<li>{</li>
<li>if (!rulerNode)</li>
<li>  {</li>
<li>  return "";</li>
<li>  }</li>
<li>
</li>
<li>std::string format = "%-#6.3g mm";</li>
<li>if (this-&gt;GetMRMLScene())</li>
<li>  {</li>
<li>  vtkMRMLSelectionNode* selectionNode = vtkMRMLSelectionNode::SafeDownCast(</li>
<li>    this-&gt;GetMRMLScene()-&gt;GetNodeByID("vtkMRMLSelectionNodeSingleton"));</li>
<li>
</li>
<li>  if (selectionNode)</li>
<li>    {</li>
<li>    vtkMRMLUnitNode* lengthUnit = vtkMRMLUnitNode::SafeDownCast(</li>
<li>      this-&gt;GetMRMLScene()-&gt;GetNodeByID(</li>
<li>        selectionNode-&gt;GetUnitNodeID("length")));</li>
<li>    if (lengthUnit)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/2b815fafd3c730c189cc8b39bf453c669cab0c05/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationRulerDisplayableManager.cxx#L657-L688" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>and here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/2b815fafd3c730c189cc8b39bf453c669cab0c05/Modules/Loadable/Annotations/VTKWidgets/vtkAnnotationRulerRepresentation3D.cxx#L85-L88" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/2b815fafd3c730c189cc8b39bf453c669cab0c05/Modules/Loadable/Annotations/VTKWidgets/vtkAnnotationRulerRepresentation3D.cxx#L85-L88" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/2b815fafd3c730c189cc8b39bf453c669cab0c05/Modules/Loadable/Annotations/VTKWidgets/vtkAnnotationRulerRepresentation3D.cxx#L85-L88</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="85" style="counter-reset: li-counter 84 ;">
<li>// Label</li>
<li>char string[512];</li>
<li>sprintf(string, this-&gt;LabelFormat, this-&gt;Distance);</li>
<li>this-&gt;LabelText-&gt;SetText(string);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>To achieve you describe, the annotation would have to be updated.</p>

---

## Post #7 by @lassoan (2017-08-09 21:50 UTC)

<p>We had a similar need in SlicerIGT extension’s BreachWarning module. We ended up creating a string with custom content and set it as node name. If this does not work for you then submit a feature request at <a href="https://issues.slicer.org/">https://issues.slicer.org/</a> .</p>

---

## Post #8 by @Nicole_Aucoin (2017-08-10 20:48 UTC)

<p>In the Modify Annotation properties pop up for the ruler, under Advanced,<br>
Lines, you can move the position of the text along the ruler, from 0 at one<br>
point to 1 at the other end point. From python:<br>
displayNode = ruler.GetDisplayNode()<br>
print displayNode.GetLabelPosition()<br>
displayNode.SetLabelPosition(0.8)<br>
So you’d have to set up a slider similar to the Label Position slider in<br>
your module if you wanted to have a GUI interface to it.</p>
<p>The label format got over written when the Units code was integrated, the<br>
ruler.Get/SetDistanceAnnotationFormat calls are there but the settings are<br>
ignored by the annotation ruler displayable manager in GetLabelFormat.</p>
<p>Nicole</p>

---
