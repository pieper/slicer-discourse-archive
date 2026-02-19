---
topic_id: 2406
title: "Slice Widget Size In Custom Layouts"
date: 2018-03-22
url: https://discourse.slicer.org/t/2406
---

# Slice widget size in custom layouts

**Topic ID**: 2406
**Date**: 2018-03-22
**URL**: https://discourse.slicer.org/t/slice-widget-size-in-custom-layouts/2406

---

## Post #1 by @mschumaker (2018-03-22 20:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/150fce0ed13d9e0c18a429af2ad36e2b985ece94.png" data-download-href="/uploads/short-url/30jT6ma2A8cj6F3AdAMHUxGYhpy.png?dl=1" title="custom-layout" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/150fce0ed13d9e0c18a429af2ad36e2b985ece94_2_690x420.png" alt="custom-layout" data-base62-sha1="30jT6ma2A8cj6F3AdAMHUxGYhpy" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/150fce0ed13d9e0c18a429af2ad36e2b985ece94_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/150fce0ed13d9e0c18a429af2ad36e2b985ece94.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/150fce0ed13d9e0c18a429af2ad36e2b985ece94.png 2x" data-dominant-color="0A0A09"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">custom-layout</span><span class="informations">990×603 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>I’m trying to change slice view sizes as part of the setup of a custom layout. For instance:</p>
<pre><code>def formatCustomLayout(self):
    customLayout = ( XML code )
    layoutNode = slicer.app.layoutManager().layoutLogic().GetLayoutNode()
    customLayoutId = 500
    layoutNode.AddLayoutDescription(customLayoutId, customLayout)
    slicer.app.layoutManager().setLayout(customLayoutId)

    slicer.app.layoutManager().sliceWidget('Long2').mrmlSliceNode().SetDimensions(100, 100, 1)
#end formatCustomLayout
</code></pre>
<p>A picture is attached, rather than including all the XML code for the custom layout. I didn’t see any property tags that set the initial size of the slice widgets.<br>
What I’d like to do is make the height of L1 twice the height of L2, without having to manually adjust the slider between them. However, it seems that packing the MRML widget happens after the line where I set the dimensions.<br>
How do I change the size of slice widgets within a layout from a script, or alternatively, specify relative size in XML property tags?<br>
Thanks for any assistance.</p>

---

## Post #2 by @lassoan (2018-03-22 23:19 UTC)

<p>You cannot specify size hints in the XML, but it would be certainly very useful to add that. The relevant code is <a href="https://github.com/commontk/CTK/blob/550eef7d6ce3e2376dfe14010e11dade50830274/Libs/Widgets/ctkLayoutManager.cpp#L404">here</a>.</p>
<p>Alternatively, you can use grid layouts and with row and column spans you may be able to get the view sizes you need. Also, you may try to access widgets and set size policies (you can access the widgets by <code>slicer.app.layoutManager().sliceWidget(name)</code> and <code>slicer.app.layoutManager().threeDWidget(n)</code>).</p>

---

## Post #3 by @mschumaker (2018-03-23 19:12 UTC)

<p>Thanks, I’d forgotten that the slice and threeD widgets inherit from QWidget, so their size policies can be changed. I can adjust the initial size that way.<br>
Thanks again,</p>

---

## Post #4 by @talmazov (2019-06-28 19:26 UTC)

<p>Hey Michael,<br>
Can you please post a snippet of the XML code layout you used to generate this view? Thank you!</p>

---

## Post #5 by @cpinter (2019-06-29 15:29 UTC)

<p>You can use the splitSize attribute to determine relative height/width of views in layouts. For example:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLLayoutLogic.cxx#L246" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLLayoutLogic.cxx#L246" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLLayoutLogic.cxx#L246</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="236" style="counter-reset: li-counter 235 ;">
<li>  " &lt;/item&gt;"</li>
<li>  "&lt;/layout&gt;";</li>
<li>
</li>
<li>const char* conventionalWidescreenView =</li>
<li>  "&lt;layout type=\"horizontal\" split=\"true\" &gt;"</li>
<li>  " &lt;item splitSize=\"500\"&gt;"</li>
<li>  "  &lt;view class=\"vtkMRMLViewNode\" singletontag=\"1\"&gt;"</li>
<li>  "   &lt;property name=\"viewlabel\" action=\"default\"&gt;1&lt;/property&gt;"</li>
<li>  "  &lt;/view&gt;"</li>
<li>  " &lt;/item&gt;"</li>
<li class="selected">  " &lt;item splitSize=\"300\"&gt;"</li>
<li>  "  &lt;layout type=\"vertical\"&gt;"</li>
<li>  "   &lt;item&gt;"</li>
<li>  "    &lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Red\"&gt;"</li>
<li>  "     &lt;property name=\"orientation\" action=\"default\"&gt;Axial&lt;/property&gt;"</li>
<li>  "     &lt;property name=\"viewlabel\" action=\"default\"&gt;R&lt;/property&gt;"</li>
<li>  "     &lt;property name=\"viewcolor\" action=\"default\"&gt;#F34A33&lt;/property&gt;"</li>
<li>  "    &lt;/view&gt;"</li>
<li>  "   &lt;/item&gt;"</li>
<li>  "   &lt;item&gt;"</li>
<li>  "    &lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Yellow\"&gt;"</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
