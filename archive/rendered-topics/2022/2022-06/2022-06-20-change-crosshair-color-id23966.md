---
topic_id: 23966
title: "Change Crosshair Color"
date: 2022-06-20
url: https://discourse.slicer.org/t/23966
---

# Change crosshair color?

**Topic ID**: 23966
**Date**: 2022-06-20
**URL**: https://discourse.slicer.org/t/change-crosshair-color/23966

---

## Post #1 by @hherhold (2022-06-20 15:35 UTC)

<p>Is there a way in python to change the color of the crosshair from yellow to something else?</p>

---

## Post #2 by @RafaelPalomar (2022-06-20 17:48 UTC)

<p>The color of the crosshair seems to be hardcoded here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L95">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L95" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L95" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L95</a></h4>



    <pre class="onebox">      <code class="lang-cxx">
        <ol class="start lines" start="85" style="counter-reset: li-counter 84 ;">
            <li>  this-&gt;External = external;</li>
            <li>  this-&gt;CrosshairMode = -1;</li>
            <li>  this-&gt;CrosshairThickness = -1;</li>
            <li>  this-&gt;CrosshairPosition[0] = 0.0;</li>
            <li>  this-&gt;CrosshairPosition[1] = 0.0;</li>
            <li>  this-&gt;CrosshairPosition[2] = 0.0;</li>
            <li>
            </li>
<li>  this-&gt;CrosshairRepresentation = vtkSmartPointer&lt;vtkPointHandleRepresentation3D&gt;::New();</li>
            <li>  this-&gt;CrosshairRepresentation-&gt;SetPlaceFactor(2.5);</li>
            <li>  this-&gt;CrosshairRepresentation-&gt;SetHandleSize(30);</li>
            <li class="selected">  this-&gt;CrosshairRepresentation-&gt;GetProperty()-&gt;SetColor(1.0, 0.8, 0.1);</li>
            <li>
            </li>
<li>  this-&gt;CrosshairWidget = vtkSmartPointer&lt;vtkHandleWidget&gt;::New();</li>
            <li>  this-&gt;CrosshairWidget-&gt;SetRepresentation(this-&gt;CrosshairRepresentation);</li>
            <li>  this-&gt;CrosshairWidget-&gt;EnabledOff();</li>
            <li>  this-&gt;CrosshairWidget-&gt;ProcessEventsOff();</li>
            <li>}</li>
            <li>
            </li>
<li>//---------------------------------------------------------------------------</li>
            <li>vtkMRMLCrosshairDisplayableManager3D::vtkInternal::~vtkInternal()</li>
            <li>{</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There are other properties that are not harcoded (e.g., crosshairThickness):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L180">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L180" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L180" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0a037160dcca3cdc57e7a272631bbb9450395dde/Libs/MRML/DisplayableManager/vtkMRMLCrosshairDisplayableManager3D.cxx#L180</a></h4>



    <pre class="onebox">      <code class="lang-cxx">
        <ol class="start lines" start="170" style="counter-reset: li-counter 169 ;">
            <li>      this-&gt;CrosshairRepresentation-&gt;GetProperty()-&gt;SetLineWidth(baseWidth * 2);</li>
            <li>      break;</li>
            <li>    case vtkMRMLCrosshairNode::Thick:</li>
            <li>      this-&gt;CrosshairRepresentation-&gt;GetProperty()-&gt;SetLineWidth(baseWidth * 3);</li>
            <li>      break;</li>
            <li>    case vtkMRMLCrosshairNode::Fine:</li>
            <li>    default:</li>
            <li>      this-&gt;CrosshairRepresentation-&gt;GetProperty()-&gt;SetLineWidth(baseWidth);</li>
            <li>      break;</li>
            <li>    }</li>
            <li class="selected">  this-&gt;CrosshairThickness = this-&gt;CrosshairNode-&gt;GetCrosshairThickness();</li>
            <li>}</li>
            <li>
            </li>
<li>//---------------------------------------------------------------------------</li>
            <li>// vtkMRMLCrosshairDisplayableManager3D methods</li>
            <li>
            </li>
<li>//---------------------------------------------------------------------------</li>
            <li>vtkMRMLCrosshairDisplayableManager3D::vtkMRMLCrosshairDisplayableManager3D()</li>
            <li>{</li>
            <li>  this-&gt;Internal = new vtkInternal(this);</li>
            <li>}</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The latter property can be changed in python simply by:</p>
<pre><code class="lang-auto">crosshairNode = getNode('Crosshair')
crosshairNode.SetCrosshairThickness(10)
</code></pre>
<p>Parameterizing the color so it becomes available in python should be easy. <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a> does it make sense to parameterize the color?</p>

---

## Post #3 by @pieper (2022-06-20 17:58 UTC)

<p>Yes, it would make perfect sense to parameterize the color.  It could exactly follow the same pattern as the other parameters.</p>

---

## Post #4 by @jamesobutler (2022-06-20 18:03 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> What color are you interested in changing it to? A different color just on personal preference? Or different color based on a certain set of conditions?</p>

---

## Post #5 by @RafaelPalomar (2022-06-20 18:13 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="23966" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, it would make perfect sense to parameterize the color. It could exactly follow the same pattern as the other parameters.</p>
</blockquote>
</aside>
<p>Just out of curiosity. Shouldn’t the <code>vtkMRMLCrosshairNode</code> have a<code>vtkMRMLCrosshairDisplayNode</code>, and shouldn’t there be a <code>vtkMRMLCrosshairDisplayableManager2D</code>?</p>

---

## Post #6 by @pieper (2022-06-20 18:34 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="5" data-topic="23966">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>Just out of curiosity. Shouldn’t the <code>vtkMRMLCrosshairNode</code> have a<code>vtkMRMLCrosshairDisplayNode</code>,</p>
</blockquote>
</aside>
<p>We usually separate display properties into display nodes when there’s a lot of bulk data in the node itself but here it’s sort of intrinsic to the node itself and there isn’t much else.  One reason to separate would be if we wanted the same node to have different displays in different views (i.e. inherit from <code>vtkMRMLDisplayableNode</code> but I guess that hasn’t ever come up.</p>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="5" data-topic="23966">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>shouldn’t there be a <code>vtkMRMLCrosshairDisplayableManager2D</code>?</p>
</blockquote>
</aside>
<p>Looks like we weren’t completely consistent in the naming of the different types of displayable managers: <a href="https://apidocs.slicer.org/master/classvtkMRMLAbstractDisplayableManager.html" class="inline-onebox">Slicer: vtkMRMLAbstractDisplayableManager Class Reference</a></p>

---

## Post #7 by @hherhold (2022-06-20 19:04 UTC)

<p>Just a different color based on conditions, the ones at the moment being a screen capture for a figure for a paper. The yellow doesn’t show up that well, but I was able to work around it by annotating in Illustrator.</p>
<p>This isn’t super high priority - just wondering if there was something I was missing while grepping through the code.</p>

---

## Post #8 by @jamesobutler (2022-06-20 19:32 UTC)

<p>What color did you decide to use to improve the figure for your paper?</p>

---

## Post #9 by @hherhold (2022-06-20 20:01 UTC)

<p>I wound up leaving it in as yellow, rather than trying to draw over it in a different color. It was a bit obscured by other geometry, so I added a labeled line in Illustrator to point out the particular morphology I was trying to highlight.</p>

---

## Post #10 by @RafaelPalomar (2022-08-17 04:12 UTC)

<p>There is now a PR on this (<a href="https://github.com/Slicer/Slicer/pull/6496" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add functionality to change crosshair color by RafaelPalomar · Pull Request #6496 · Slicer/Slicer · GitHub</a>)</p>

---
