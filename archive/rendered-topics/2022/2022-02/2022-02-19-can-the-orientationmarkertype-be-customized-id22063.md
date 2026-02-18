# Can the OrientationMarkerType be customized?

**Topic ID**: 22063
**Date**: 2022-02-19
**URL**: https://discourse.slicer.org/t/can-the-orientationmarkertype-be-customized/22063

---

## Post #1 by @jumbojing (2022-02-19 09:20 UTC)

<p>Can the OrientationMarkerType be customized?<br>
我想用椎体代替<strong>human</strong>, 我该怎么做呢?</p>
<blockquote>
<p>I want to replace the OrientationMarkerType<strong>human</strong> with a vertebral body, how can I do that?</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a54aab8f1de1e2f229a51ecc6687aa8871fc9c66.png" alt="image" data-base62-sha1="nAeLhLVqjImWVpM6wB4aB445VvE" width="619" height="438"></p>

---

## Post #2 by @lassoan (2022-02-19 14:22 UTC)

<p>Yes, sure, you can use any model as orientation marker. See for example how it is done in SlicerHeart:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L69-L77">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L69-L77" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L69-L77" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L69-L77</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="69" style="counter-reset: li-counter 68 ;">
            <li>  moduleDir = os.path.dirname(slicer.modules.valveannulusanalysis.path)</li>
            <li>  orientationMarkerModelFilePath = os.path.join(moduleDir, 'Resources', 'HeartOrientationMarker.vtp')</li>
            <li>  orientationMarkerNode = slicer.util.loadModel(orientationMarkerModelFilePath)</li>
            <li>  orientationMarkerNode.HideFromEditorsOn()</li>
            <li>  orientationMarkerNode.GetDisplayNode().SetVisibility(False) # hide from the viewers, just use it as an orientation marker</li>
            <li>  orientationMarkerNode.SetName('HeartOrientationMarker')</li>
            <li>viewNode.SetOrientationMarkerHumanModelNodeID(orientationMarkerNode.GetID() )</li>
            <li>viewNode.SetOrientationMarkerType(slicer.vtkMRMLAbstractViewNode.OrientationMarkerTypeHuman)</li>
            <li>viewNode.SetOrientationMarkerSize(slicer.vtkMRMLAbstractViewNode.OrientationMarkerSizeMedium)</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jumbojing (2022-02-20 04:22 UTC)

<p>太好了, 可是,老师,我做的model导出后,再次导入就变成了黄色,怎么做带不同的颜色的vtp模型呢?就像这样:</p>
<blockquote>
<p>Great, but, teacher, after the model I made is exported, it turns yellow when I import it again. How can I make a vtp model with different colors? Like this:</p>
</blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a54aab8f1de1e2f229a51ecc6687aa8871fc9c66.png" alt="image" data-base62-sha1="nAeLhLVqjImWVpM6wB4aB445VvE" width="619" height="438"></p>

---

## Post #4 by @lassoan (2022-02-20 04:54 UTC)

<p>You can use VTK filters for this: add an RGB color vector to each model node (using vtkArrayCalculator) and then merge them into a single polydata (using vtkAppendPolyData).</p>

---

## Post #5 by @jumbojing (2022-02-20 14:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>vtkArrayCalculator</p>
</blockquote>
</aside>
<p>这个…太难了吧, 有现成的例子吗?</p>
<blockquote>
<p>This… is too difficult, is there a ready-made example?</p>
</blockquote>

---
