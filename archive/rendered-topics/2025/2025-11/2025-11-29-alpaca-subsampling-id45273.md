# ALPACA subsampling

**Topic ID**: 45273
**Date**: 2025-11-29
**URL**: https://discourse.slicer.org/t/alpaca-subsampling/45273

---

## Post #1 by @Lucy-create02 (2025-11-29 01:37 UTC)

<p>Hi Slicer Forum,</p>
<p>I’m trying out the automatic landmarking module ALPACA/ MALPACA in 3D Slicer. When running ALPACA subsampling the max density value is capped at 2 so I can only achieve a maximum subsampling of around 3’800 points (see screenshot 1) when my mesh has a resolution of around 50’000 points (screenshot 2). We previously heard that the recommended amount of points lie between 5 - 6k, so is there a reason for my subsampling not going that high?</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2976ddff11bfa181de1b13a565a5a8a4e093db94.png" data-download-href="/uploads/short-url/5UOfnr85kLkORNktAa7Iw1CVgZm.png?dl=1" title="MALPACA subsampling" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2976ddff11bfa181de1b13a565a5a8a4e093db94_2_690x329.png" alt="MALPACA subsampling" data-base62-sha1="5UOfnr85kLkORNktAa7Iw1CVgZm" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2976ddff11bfa181de1b13a565a5a8a4e093db94_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2976ddff11bfa181de1b13a565a5a8a4e093db94_2_1035x493.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2976ddff11bfa181de1b13a565a5a8a4e093db94_2_1380x658.png 2x" data-dominant-color="C2C4E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MALPACA subsampling</span><span class="informations">2364×1128 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e1ee374171890a6388579d705d27c1ee54c47ef.png" data-download-href="/uploads/short-url/fIaHoVMmOinA8TlZqyMctZGHD9Z.png?dl=1" title="Mesh properties" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e1ee374171890a6388579d705d27c1ee54c47ef.png" alt="Mesh properties" data-base62-sha1="fIaHoVMmOinA8TlZqyMctZGHD9Z" width="444" height="412"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Mesh properties</span><span class="informations">444×412 8.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-11-30 06:51 UTC)

<p>Most models we worked with has higher resolution than 50K points, so the value of 2 usually gave more than enough points to work with so never needed to  increase beyond that.</p>
<p>You can find the ALPACA.ui file under the Resources folder of your SlicerMorph extension, and manually increase the number of maximum value from 2.0, to whatever you like.</p>
<p>This is the line you need to change:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/75a274ca4c91c36c7b435e81b62465ae54379288/ALPACA/Resources/UI/ALPACA.ui#L225">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/75a274ca4c91c36c7b435e81b62465ae54379288/ALPACA/Resources/UI/ALPACA.ui#L225" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/75a274ca4c91c36c7b435e81b62465ae54379288/ALPACA/Resources/UI/ALPACA.ui#L225" target="_blank" rel="noopener nofollow ugc">ALPACA/Resources/UI/ALPACA.ui</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/75a274ca4c91c36c7b435e81b62465ae54379288/ALPACA/Resources/UI/ALPACA.ui#L225" rel="noopener nofollow ugc"><code>75a274ca4</code></a>
</div>



    <pre class="onebox"><code class="lang-ui">
      <ol class="start lines" start="215" style="counter-reset: li-counter 214 ;">
          <li>&lt;/item&gt;</li>
          <li>&lt;item row="0" column="1"&gt;</li>
          <li> &lt;widget class="ctkSliderWidget" name="pointDensitySlider" native="true"&gt;</li>
          <li>  &lt;property name="toolTip"&gt;</li>
          <li>   &lt;string&gt;Adjust the density of the pointclouds. Larger values increase the number of points, and vice versa.&lt;/string&gt;</li>
          <li>  &lt;/property&gt;</li>
          <li>  &lt;property name="singleStep" stdset="0"&gt;</li>
          <li>   &lt;double&gt;0.100000000000000&lt;/double&gt;</li>
          <li>  &lt;/property&gt;</li>
          <li>  &lt;property name="maximum" stdset="0"&gt;</li>
          <li class="selected">   &lt;double&gt;2.000000000000000&lt;/double&gt;</li>
          <li>  &lt;/property&gt;</li>
          <li>  &lt;property name="value" stdset="0"&gt;</li>
          <li>   &lt;double&gt;1.000000000000000&lt;/double&gt;</li>
          <li>  &lt;/property&gt;</li>
          <li> &lt;/widget&gt;</li>
          <li>&lt;/item&gt;</li>
          <li>&lt;item row="1" column="0" colspan="2"&gt;</li>
          <li> &lt;widget class="QPushButton" name="subsampleButton"&gt;</li>
          <li>  &lt;property name="enabled"&gt;</li>
          <li>   &lt;bool&gt;false&lt;/bool&gt;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
