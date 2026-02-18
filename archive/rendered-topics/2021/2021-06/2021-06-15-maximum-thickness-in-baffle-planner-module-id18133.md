# Maximum thickness in Baffle Planner module

**Topic ID**: 18133
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/maximum-thickness-in-baffle-planner-module/18133

---

## Post #1 by @Aep93 (2021-06-15 02:41 UTC)

<p>Hello all,<br>
My maximum thickness in the Baffle Planner module is 10. How can I increase it?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/701b6e0893863c1d08ae7840a891ace958c49147.png" alt="image" data-base62-sha1="fZKfb1UrmgmaDD7AU5DEgjsfqoD" width="618" height="197"></p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-06-17 03:24 UTC)

<p>You probably don’t want to increase it much, because if the surface is curved and you make it too thick then you’ll have self-intersections. If the shape that you want to reconstruct is very thick then there better methods to use (e.g., Surface Cut effect and many other tools in Segment Editor module).</p>
<p>Anyway, you can easily change this by locating BafflePlanner.ui file in your Slicer folder and changing <code>10.0000</code> in this line to the value that you want to use:</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/BafflePlanner/Resources/UI/BafflePlanner.ui#L157" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/BafflePlanner/Resources/UI/BafflePlanner.ui#L157" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/master/BafflePlanner/Resources/UI/BafflePlanner.ui#L157</a></h4>



  <pre class="onebox">    <code class="lang-ui">
      <ol class="start lines" start="147" style="counter-reset: li-counter 146 ;">
          <li>  &lt;property name="singleStep"&gt;
</li>
          <li>   &lt;double&gt;0.100000000000000&lt;/double&gt;
</li>
          <li>  &lt;/property&gt;
</li>
          <li>  &lt;property name="pageStep"&gt;
</li>
          <li>   &lt;double&gt;1.000000000000000&lt;/double&gt;
</li>
          <li>  &lt;/property&gt;
</li>
          <li>  &lt;property name="minimum"&gt;
</li>
          <li>   &lt;double&gt;0.000000000000000&lt;/double&gt;
</li>
          <li>  &lt;/property&gt;
</li>
          <li>  &lt;property name="maximum"&gt;
</li>
          <li class="selected">   &lt;double&gt;10.000000000000000&lt;/double&gt;
</li>
          <li>  &lt;/property&gt;
</li>
          <li>  &lt;property name="value"&gt;
</li>
          <li>   &lt;double&gt;0.000000000000000&lt;/double&gt;
</li>
          <li>  &lt;/property&gt;
</li>
          <li> &lt;/widget&gt;
</li>
          <li>&lt;/item&gt;
</li>
          <li>&lt;item&gt;
</li>
          <li> &lt;widget class="ctkSliderWidget" name="thicknessSliderWidgetNegative"&gt;
</li>
          <li>  &lt;property name="toolTip"&gt;
</li>
          <li>   &lt;string&gt;Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.&lt;/string&gt;
</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Aep93 (2021-06-17 03:35 UTC)

<p>Thank you very much for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I have the same question about the CreateModels module and I asked this in the forum a few hours ago. Should I do the same thing for increasing the thresholds in that module as well?<br>
I cannot find any files with the name CreateModels.ui for that.<br>
Thanks in advance.</p>

---

## Post #4 by @lassoan (2021-06-17 03:55 UTC)

<p>CreateModels module was implemented before Python scripted modules existed. It is implemented in C++, so changing its source code is not an option. If you have any more questions about CreateModels module then then let’s discuss it in <a href="https://discourse.slicer.org/t/increasing-the-maximum-value-range-in-createmodels-module/18175/2">the topic that you created for it</a>.</p>

---

## Post #5 by @Aep93 (2021-06-17 05:17 UTC)

<p>OK, thank you very much for your explanations <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
