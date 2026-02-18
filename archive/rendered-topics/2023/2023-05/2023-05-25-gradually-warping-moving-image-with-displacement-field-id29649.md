# Gradually warping moving image with displacement field 

**Topic ID**: 29649
**Date**: 2023-05-25
**URL**: https://discourse.slicer.org/t/gradually-warping-moving-image-with-displacement-field/29649

---

## Post #1 by @derkleinejakob (2023-05-25 15:09 UTC)

<p>Hi!</p>
<p>I have two 3D volumes and a displacement field which was obtained by registering one of the volumes to the other.<br>
Is there a way in slicer to visualise how the moving image is warped into the target image? The visualisation should gradually apply the displacement field transformation to slowly warp the moving image.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2023-05-25 21:10 UTC)

<p>There’s no exposed interface for that, but I agree it would be a nice feature to have.</p>
<p>What you can do currently is write a small script that implements what you describe.  Easiest would be to create a duplicate of the displacement field and then use numpy to add fractions of the displacement field and render iteratively.</p>
<p>I don’t have an implementation in python, but here’s how I did it in javascript for another application:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/sites/blob/27a92195d18eec21a9fbc3585e0409a181eb7a07/step/index.html#L366-L390">
  <header class="source">

      <a href="https://github.com/pieper/sites/blob/27a92195d18eec21a9fbc3585e0409a181eb7a07/step/index.html#L366-L390" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/sites/blob/27a92195d18eec21a9fbc3585e0409a181eb7a07/step/index.html#L366-L390" target="_blank" rel="noopener">pieper/sites/blob/27a92195d18eec21a9fbc3585e0409a181eb7a07/step/index.html#L366-L390</a></h4>



    <pre class="onebox"><code class="lang-html">
      <ol class="start lines" start="366" style="counter-reset: li-counter 365 ;">
          <li>function animateTransform(options={}) {</li>
          <li>  // animate passed in field or first render field with a transform</li>
          <li>  let animatingField = options.field || (() =&gt; {</li>
          <li>    let returnField;</li>
          <li>    step.renderer.inputFields.forEach(field =&gt; {</li>
          <li>      if (field.transformField) {</li>
          <li>        returnField = field;</li>
          <li>      }</li>
          <li>    });</li>
          <li>    return returnField;</li>
          <li>  })();</li>
          <li>  let frame = 0;</li>
          <li>  let frames = options.frames || 100;</li>
          <li>  let maxGain = options.maxGain || 1;</li>
          <li>  let animationFrame = function (now) {</li>
          <li>    animatingField.transformGain = maxGain * Math.sin(Math.PI*frame/frames);</li>
          <li>    step.renderer.requestRender();</li>
          <li>    step.ui.bottomBar.progress = `Animation frame ${frame} of ${frames}`;</li>
          <li>    frame = frame + 1;</li>
          <li>    if (frame &lt;= frames) {</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/pieper/sites/blob/27a92195d18eec21a9fbc3585e0409a181eb7a07/step/index.html#L366-L390" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Using the sin function gives it a nice ease-in, ease-out as shown in this video: <a href="https://youtu.be/8dputUoKBTA" class="inline-onebox">MR US p3 2017 08 09 - YouTube</a></p>

---
