---
topic_id: 10920
title: "Improving Slice Overlay Functionality To Visualize Registrat"
date: 2020-03-30
url: https://discourse.slicer.org/t/10920
---

# Improving Slice overlay functionality to visualize registration differences using different color "channel" for fixed and moving

**Topic ID**: 10920
**Date**: 2020-03-30
**URL**: https://discourse.slicer.org/t/improving-slice-overlay-functionality-to-visualize-registration-differences-using-different-color-channel-for-fixed-and-moving/10920

---

## Post #1 by @jcfr (2020-03-30 21:59 UTC)

<p>To support generating overlay like this one (useful to visualize registration differences):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae353192447d09b913fd77cece86b3ee7c6f9f62.png" alt="image" data-base62-sha1="oR72TwrdOqJSUW4o5RJymc6CrZ0" width="516" height="160"></p>
<p><small>Image copied from <a href="https://dipy.org/documentation/1.1.0./examples_built/streamline_registration/">here</a></small></p>
<p>An idea would be to add a new blending mode. Currently we have the following:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9707dbfd6f41c7d98ddc73404044969ea4084bd.png" alt="image" data-base62-sha1="sK0YW7KJHc57MaBk2JOjvHBsWLz" width="355" height="131"></p>
<p>Would that generally be useful ?</p>
<p>cc: <a class="mention" href="/u/samuel_gerber">@Samuel_Gerber</a></p>

---

## Post #2 by @Samuel_Gerber (2020-03-30 22:01 UTC)

<p>Maybe the blending should be adding and you would pick colors that add together to white / gray. Then you’d a get grayscale image where the images are registered well and otherwise some of one or the other color</p>

---

## Post #3 by @pieper (2020-03-30 22:13 UTC)

<p>Hi - can you elaborate on what blend function that would be?</p>

---

## Post #4 by @jcfr (2020-03-30 22:16 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="10920">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>can you elaborate on what blend function that would be?</p>
</blockquote>
</aside>
<p>I am assuming we would have to write a custom blend function.</p>
<p>For reference, here is the code used to generate the figure above.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/dipy/dipy/blob/003c3b49f9db711a8101d03365d2e0ea1abd34d5/dipy/viz/regtools.py#L343-L424">
  <header class="source">

      <a href="https://github.com/dipy/dipy/blob/003c3b49f9db711a8101d03365d2e0ea1abd34d5/dipy/viz/regtools.py#L343-L424" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/dipy/dipy/blob/003c3b49f9db711a8101d03365d2e0ea1abd34d5/dipy/viz/regtools.py#L343-L424" target="_blank" rel="noopener">dipy/dipy/blob/003c3b49f9db711a8101d03365d2e0ea1abd34d5/dipy/viz/regtools.py#L343-L424</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="343" style="counter-reset: li-counter 342 ;">
          <li>def overlay_slices(L, R, slice_index=None, slice_type=1, ltitle='Left',</li>
          <li>                   rtitle='Right', fname=None):</li>
          <li>    r"""Plot three overlaid slices from the given volumes.</li>
          <li></li>
          <li>    Creates a figure containing three images: the gray scale k-th slice of</li>
          <li>    the first volume (L) to the left, where k=slice_index, the k-th slice of</li>
          <li>    the second volume (R) to the right and the k-th slices of the two given</li>
          <li>    images on top of each other using the red channel for the first volume and</li>
          <li>    the green channel for the second one. It is assumed that both volumes have</li>
          <li>    the same shape. The intended use of this function is to visually assess the</li>
          <li>    quality of a registration result.</li>
          <li></li>
          <li>    Parameters</li>
          <li>    ----------</li>
          <li>    L : array, shape (S, R, C)</li>
          <li>        the first volume to extract the slice from plotted to the left</li>
          <li>    R : array, shape (S, R, C)</li>
          <li>        the second volume to extract the slice from, plotted to the right</li>
          <li>    slice_index : int (optional)</li>
          <li>        the index of the slices (along the axis given by slice_type) to be</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/dipy/dipy/blob/003c3b49f9db711a8101d03365d2e0ea1abd34d5/dipy/viz/regtools.py#L343-L424" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @pieper (2020-03-30 22:35 UTC)

<p>Hmm, I see, yes that could be useful.  It would be easy enough to add a blend mode yes.  Also though very easy to have a scripted module or cli that just makes a red/green mix of the two volumes with hot update.  Could also be added as an extension to the CompareVolumes module.  I don’t have a strong preference.</p>

---

## Post #6 by @jcfr (2020-03-30 22:51 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="10920">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Could also be added as an extension to the CompareVolumes module. I don’t have a strong preference.</p>
</blockquote>
</aside>
<p>Agreed.</p>
<p>We currently do not need this feature, <a class="mention" href="/u/samuel_gerber">@Samuel_Gerber</a> and I discussed this in the context of a proposal and I wanted to have this documented so that we could refer to it at a later time.</p>

---
