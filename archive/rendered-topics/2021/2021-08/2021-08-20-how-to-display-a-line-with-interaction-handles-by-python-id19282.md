---
topic_id: 19282
title: "How To Display A Line With Interaction Handles By Python"
date: 2021-08-20
url: https://discourse.slicer.org/t/19282
---

# How to display a line with interaction handles by python?

**Topic ID**: 19282
**Date**: 2021-08-20
**URL**: https://discourse.slicer.org/t/how-to-display-a-line-with-interaction-handles-by-python/19282

---

## Post #1 by @jumbojing (2021-08-20 13:46 UTC)

<p>How to display a line (vtkMRMLMarkupsLineNode) with interaction handles by python?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>like that:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/deb177e7dc979c19c68bcfd577a3e65e510e3cf7.jpeg" data-download-href="/uploads/short-url/vM2dO2bjfTnCD7y9DNZdDeGQ91l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/deb177e7dc979c19c68bcfd577a3e65e510e3cf7_2_690x328.jpeg" alt="image" data-base62-sha1="vM2dO2bjfTnCD7y9DNZdDeGQ91l" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/deb177e7dc979c19c68bcfd577a3e65e510e3cf7_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/deb177e7dc979c19c68bcfd577a3e65e510e3cf7_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/deb177e7dc979c19c68bcfd577a3e65e510e3cf7_2_1380x656.jpeg 2x" data-dominant-color="78797B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×915 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2021-08-20 15:21 UTC)

<ol>
<li>First get the reference to vtkMRMLMarkupsLineNode (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-mrml-node-from-the-scene" rel="noopener nofollow ugc">get-mrml-node-from-the-scene</a>)</li>
<li>Get the DisplayNode for that Line Node. (similar to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-fiducial-display-properties" rel="noopener nofollow ugc">change-markup-fiducial-display-properties</a>)</li>
<li>The interactive handles can be set from the DisplayNode. <code>SetHandlesInteractive</code>.</li>
</ol>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Markups/Widgets/qMRMLMarkupsDisplayNodeWidget.cxx#L666">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Markups/Widgets/qMRMLMarkupsDisplayNodeWidget.cxx#L666" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Markups/Widgets/qMRMLMarkupsDisplayNodeWidget.cxx#L666" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Markups/Widgets/qMRMLMarkupsDisplayNodeWidget.cxx#L666</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="656" style="counter-reset: li-counter 655 ;">
          <li>}</li>
          <li>
          </li>
<li>//-----------------------------------------------------------------------------</li>
          <li>void qMRMLMarkupsDisplayNodeWidget::onInteractionCheckBoxChanged(int state)</li>
          <li>{</li>
          <li>  Q_D(qMRMLMarkupsDisplayNodeWidget);</li>
          <li>  if (!d-&gt;MarkupsDisplayNode)</li>
          <li>    {</li>
          <li>    return;</li>
          <li>    }</li>
          <li class="selected">  d-&gt;MarkupsDisplayNode-&gt;SetHandlesInteractive(state);</li>
          <li>}</li>
          <li>
          </li>
<li>//-----------------------------------------------------------------------------</li>
          <li>void qMRMLMarkupsDisplayNodeWidget::setFillVisibility(bool visibility)</li>
          <li>{</li>
          <li>  Q_D(qMRMLMarkupsDisplayNodeWidget);</li>
          <li>  if (!d-&gt;MarkupsDisplayNode)</li>
          <li>    {</li>
          <li>    return;</li>
          <li>    }</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jumbojing (2021-08-20 15:34 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="19282">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The interactive handles can be set from the DisplayNode. <code>SetHandlesInteractive</code> .</p>
</blockquote>
</aside>
<p>Great! Thanks!<br>
DisplayNode.SetHandlesInteractive(True)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f84cf43b5b21489cbac1f55af66591f46468bd81.jpeg" data-download-href="/uploads/short-url/zqzhJ59TzpbbBfylG7mWOQ4gNRD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84cf43b5b21489cbac1f55af66591f46468bd81_2_622x500.jpeg" alt="image" data-base62-sha1="zqzhJ59TzpbbBfylG7mWOQ4gNRD" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84cf43b5b21489cbac1f55af66591f46468bd81_2_622x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84cf43b5b21489cbac1f55af66591f46468bd81_2_933x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84cf43b5b21489cbac1f55af66591f46468bd81_2_1244x1000.jpeg 2x" data-dominant-color="545554"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1488×1196 89.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jumbojing (2021-08-20 15:54 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>Is it possible to further control the position of the “origin” and “rotation” or “translate” of the handle?<br>
是否可以进一步控制handle的"原点"的位置以及"rotation"或者"translate"呢?</p>

---

## Post #5 by @jamesobutler (2021-08-20 16:00 UTC)

<p>Yes. They are all methods in the Markups Display Node class.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/39be4408f084b3e5d632b373a4985cd7fa6c661b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.cxx#L1044-L1061">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/39be4408f084b3e5d632b373a4985cd7fa6c661b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.cxx#L1044-L1061" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/39be4408f084b3e5d632b373a4985cd7fa6c661b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.cxx#L1044-L1061" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/39be4408f084b3e5d632b373a4985cd7fa6c661b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.cxx#L1044-L1061</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="1044" style="counter-reset: li-counter 1043 ;">
          <li>void vtkMRMLMarkupsDisplayNode::SetHandleVisibility(int componentType, bool visibility)</li>
          <li>{</li>
          <li>  switch (componentType)</li>
          <li>    {</li>
          <li>    case vtkMRMLMarkupsDisplayNode::ComponentTranslationHandle:</li>
          <li>      this-&gt;SetTranslationHandleVisibility(visibility);</li>
          <li>      break;</li>
          <li>    case vtkMRMLMarkupsDisplayNode::ComponentRotationHandle:</li>
          <li>      this-&gt;SetRotationHandleVisibility(visibility);</li>
          <li>      break;</li>
          <li>    case vtkMRMLMarkupsDisplayNode::ComponentScaleHandle:</li>
          <li>      this-&gt;SetScaleHandleVisibility(visibility);</li>
          <li>      break;</li>
          <li>    default:</li>
          <li>      vtkErrorMacro("Unknown handle type");</li>
          <li>      break;</li>
          <li>    }</li>
          <li>}</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jumbojing (2021-08-20 16:07 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>I want the “Origin” of this Handle to be at the end of the line segment instead of the midpoint, how to do it?</p>
<p>我想让这个Handle的原点,在线段的一端而不是中点,怎么做呢?</p>

---

## Post #7 by @jamesobutler (2021-08-20 16:24 UTC)

<p>That’s not something that I believe is possible at the moment.</p>

---

## Post #8 by @jumbojing (2021-08-20 16:44 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
Thanks</p>

---

## Post #9 by @lassoan (2021-08-20 18:01 UTC)

<p>You can position a line shaped actor (e.g., that you generated using SlicerIGT extension’s Create Models module) using a transform. You can update the transform from a markups plane node by a few lines of Python code. This technique is used in the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">Bone Reconstruction Planner extension</a>.</p>

---

## Post #11 by @seanchoi0519 (2022-08-21 10:07 UTC)

<p>Hello, I am trying to find a way to grab 2 planes (generated from markups module) and lock (?) combine them together so when I transform them in position, they move in harmony.</p>
<p>How can I do this <strong>programmatically?</strong> assuming I have displayNodes of both planes.<br>
Thanks in advance!</p>

---

## Post #12 by @seanchoi0519 (2022-08-21 13:59 UTC)

<p>Also would there be a way to adjust the size of the interactive handles programmatically?<br>
Thank you &amp; sorry for many questions</p>

---

## Post #13 by @jumbojing (2022-08-21 14:47 UTC)

<p>没太看懂你的问题, 不过可以看看这个👇或许对你有帮助</p>
<blockquote>
<p>I don’t understand your question very well, but you can take a look at this👇 maybe it will help you…<br>
<a href="https://discourse.slicer.org/t/how-to-rotate-orthogonalslicesdeg-in-slices/20892/2">How to rotate OrthogonalSlicesDeg in slices?</a>, <a href="https://github.com/SlicerHeart/SlicerHeart/blob/5be64b4b68fcbfbdc7ed463913f52a74208b6d07/ValveView/ValveView.py#L213-L273" rel="noopener nofollow ugc">getPlaneIntersectionPoint</a></p>
</blockquote>

---

## Post #15 by @seanchoi0519 (2022-08-21 14:52 UTC)

<p>Thank you, but I do not think it is similar to my problem.<br>
My problem is:</p>
<ul>
<li>I have 2 plane nodes. I want the relationship between the 2 planes to be fixed. If I move 1 of them, I want the other to move by the same amount, if I rotate 1 of them, I want the other to rotate by the same amount</li>
</ul>

---

## Post #16 by @seanchoi0519 (2022-08-21 14:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1de698f9d1a8bd030c56b41e95041ee2f5ee2692.png" data-download-href="/uploads/short-url/4gvTMdCwmhcpvHJs15GM4zITWkG.png?dl=1" title="Screen Shot 2022-08-22 at 12.57.55 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1de698f9d1a8bd030c56b41e95041ee2f5ee2692_2_690x379.png" alt="Screen Shot 2022-08-22 at 12.57.55 AM" data-base62-sha1="4gvTMdCwmhcpvHJs15GM4zITWkG" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1de698f9d1a8bd030c56b41e95041ee2f5ee2692_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1de698f9d1a8bd030c56b41e95041ee2f5ee2692.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1de698f9d1a8bd030c56b41e95041ee2f5ee2692.png 2x" data-dominant-color="EBEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-22 at 12.57.55 AM</span><span class="informations">884×486 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There appears to be a way to do it on the user interface under “Markups module” then “Interactive handles.” How can I do this programmatically?</p>

---
