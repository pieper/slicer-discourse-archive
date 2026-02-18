# Volumes widget is too wide when there are many decimals

**Topic ID**: 1434
**Date**: 2017-11-10
**URL**: https://discourse.slicer.org/t/volumes-widget-is-too-wide-when-there-are-many-decimals/1434

---

## Post #1 by @Fernando (2017-11-10 19:10 UTC)

<p>Title and screenshot image say it all. The module widget takes more than 50% of my screen and I can’t resize it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d74a19aa4cbe28d5c8bb986551ff9ac190a492.png" data-download-href="/uploads/short-url/zdEIdLvcIIyI2gygd3YLSlS7Hma.png?dl=1" title="45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f6d74a19aa4cbe28d5c8bb986551ff9ac190a492_2_690x431.png" alt="45" data-base62-sha1="zdEIdLvcIIyI2gygd3YLSlS7Hma" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f6d74a19aa4cbe28d5c8bb986551ff9ac190a492_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f6d74a19aa4cbe28d5c8bb986551ff9ac190a492_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f6d74a19aa4cbe28d5c8bb986551ff9ac190a492_2_1380x862.png 2x" data-dominant-color="AAAAAB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">45</span><span class="informations">2560×1600 890 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It says 4 decimals here:<br>
<a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Libs/MRML/Widgets/Resources/UI/qMRMLVolumeInfoWidget.ui#L95-L98" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Libs/MRML/Widgets/Resources/UI/qMRMLVolumeInfoWidget.ui#L95-L98</a></p>
<p>When I try to access the widget, I get 3:</p>
<pre><code class="lang-python">v = slicer.modules.volumes.widgetRepresentation()
&gt;&gt;&gt; for cw in v.findChildren('qMRMLCoordinatesWidget'):
...     print(cw.decimals)
... 
0
3
3
</code></pre>
<p>But in Slicer there are many more.</p>
<p>P.S.: I’m not sure if it’s the right category or if I should’ve posted directly in the issue tracker.</p>

---

## Post #2 by @Fernando (2017-11-16 00:02 UTC)

<p>Should I report this somewhere else? I can try to help with some guidance.</p>

---

## Post #3 by @lassoan (2017-11-16 02:18 UTC)

<p>I cannot reproduce this. Can you give detailed instructions?</p>
<p>Does it help if you reduce the number of shown digits using <code>Ctrl</code>+<code>-</code> shortcut? Is it possible that you’ve accidentally hit <code>Ctrl</code>+<code>+</code> several times and that increased the number of shown digits?</p>

---

## Post #4 by @Fernando (2017-11-16 08:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you give detailed instructions?</p>
</blockquote>
</aside>
<ol>
<li>Open Slicer</li>
<li>Open <a href="https://we.tl/5vKhQXgIbi" rel="noopener nofollow ugc">this volume</a></li>
<li>Go to <code>Volumes</code> module</li>
<li>Click on <code>Volume Information</code></li>
</ol>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="3" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does it help if you reduce the number of shown digits using Ctrl± shortcut?</p>
</blockquote>
</aside>
<p>Nothing happens when I click <code>Ctrl + -</code> or <code>Cmd + -</code> (I’m on a MacBook Pro Retina 13").</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is it possible that you’ve accidentally hit Ctrl++ several times and that increased the number of shown digits?</p>
</blockquote>
</aside>
<p>No, and this is something that has happened to me as long as I can remember. Just hadn’t reported it yet.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I cannot reproduce this.</p>
</blockquote>
</aside>
<p>Maybe a macOS user can reproduce. <a class="mention" href="/u/fedorov">@fedorov</a>?</p>

---

## Post #5 by @fedorov (2017-11-16 16:37 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> I cannot reproduce it either</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68dc1b0cc8e9c518ee725a7b6ea84839010f2e0d.png" data-download-href="/uploads/short-url/eXDekujNyVnJm6dauHxs300VXBP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68dc1b0cc8e9c518ee725a7b6ea84839010f2e0d_2_690x269.png" alt="image" data-base62-sha1="eXDekujNyVnJm6dauHxs300VXBP" width="690" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68dc1b0cc8e9c518ee725a7b6ea84839010f2e0d_2_690x269.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68dc1b0cc8e9c518ee725a7b6ea84839010f2e0d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68dc1b0cc8e9c518ee725a7b6ea84839010f2e0d.png 2x" data-dominant-color="9F9D9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">930×363 84.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @fedorov (2017-11-16 16:40 UTC)

<p>I can also confirm that if I put the cursor into a field from Image Origin, I can then use <code>Command + +</code> / <code>Command + -</code> to increase/decrease the number of decimals.</p>

---

## Post #7 by @Fernando (2017-11-16 16:55 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/fernando">@Fernando</a> I cannot reproduce it either</p>
</blockquote>
</aside>
<p>That’s probably because MRHead has fewer decimals in its header than the image I shared.</p>
<aside class="quote no-group" data-username="fedorov" data-post="6" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>if I put the cursor into a field from Image Origin</p>
</blockquote>
</aside>
<p>I didn’t know I was supposed to enable one of the widget’s spin boxes. I can decrease the number of decimals of one spin box now, but as soon as I do the same on another one, the former goes back to its initial length so the module widget’s width stays the same.</p>

---

## Post #8 by @fedorov (2017-11-16 17:11 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="7" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>That’s probably because MRHead has fewer decimals in its header than the image I shared.</p>
</blockquote>
</aside>
<p>No, I checked that:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fafbdfbdc8e55a7adcb14647d9a5ce68cc6189a5.png" alt="image" data-base62-sha1="zOj0jMv62bm2VktCIYaQbdmMFkF" width="529" height="215"></p>

---

## Post #9 by @fedorov (2017-11-16 17:12 UTC)

<p>I don’t know if this detail matters, but for this experiment I was using a nightly build from August.</p>

---

## Post #10 by @lassoan (2017-11-16 18:22 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> Have you adjusted units in your application (Edit/Application Settings/Units)? It may effect how length values are displayed.</p>

---

## Post #11 by @pieper (2017-11-16 21:33 UTC)

<p>I was able to replicate the behavior reported by <a class="mention" href="/u/fernando">@Fernando</a> using the volume he provided.</p>
<p>As a workaround I can change the behavior by changing the decimalsOption like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; for w in findChildren(className='qMRMLCoordinatesWidget'):
...   w.decimalsOption = 0
</code></pre>
<p>I didn’t look deeper but there are a number of options and maybe we should pick a different default (or debug the version we are using which is 7 =  DecimalsByShortcuts | DecimalsByKey | DecimalsByValue) for the ImageOrigin.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/cdb75ce742f618112b8a0f299a484d00baa4e8ff/Libs/Widgets/ctkDoubleSpinBox.h#L110-L152" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/cdb75ce742f618112b8a0f299a484d00baa4e8ff/Libs/Widgets/ctkDoubleSpinBox.h#L110-L152" target="_blank" rel="nofollow noopener">commontk/CTK/blob/cdb75ce742f618112b8a0f299a484d00baa4e8ff/Libs/Widgets/ctkDoubleSpinBox.h#L110-L152</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="110" style="counter-reset: li-counter 109 ;">
<li>/// DecimalsOption enums the input style of the spinbox decimals.</li>
<li>/// Default option is DecimalsByShortcuts.</li>
<li>/// \sa decimals(), currentDecimals()</li>
<li>enum DecimalsOption</li>
<li>  {</li>
<li>  /// Behaves just like a QDoubleSpinBox. The maximum number of decimals</li>
<li>  /// allowed is given by decimals().</li>
<li>  FixedDecimals = 0x000,</li>
<li>  /// When the spinbox has focus, entering the shortcut "CTRL +"</li>
<li>  /// adds decimals to the current number of decimals. "CTRL -" decreases the</li>
<li>  /// number of decimals and "CTRL 0" returns it to its original decimals()</li>
<li>  /// value.</li>
<li>  DecimalsByShortcuts = 0x001,</li>
<li>  /// Allow the number of decimals to be controlled by adding/removing digits</li>
<li>  /// with key strokes.</li>
<li>  /// \sa InsertDecimals, ReplaceDecimals</li>
<li>  DecimalsByKey = 0x002,</li>
<li>  /// Allow the number of decimals to be controlled by the value set by</li>
<li>  /// setValue().</li>
<li>  DecimalsByValue = 0x004,</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/cdb75ce742f618112b8a0f299a484d00baa4e8ff/Libs/Widgets/ctkDoubleSpinBox.h#L110-L152" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #12 by @fedorov (2017-11-16 22:47 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>using the volume he provided</p>
</blockquote>
</aside>
<p>Sorry, I missed that link! Interesting that the issue is specific to the dataset.</p>

---

## Post #13 by @Fernando (2017-11-17 10:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you adjusted units in your application (Edit/Application Settings/Units)? It may effect how length values are displayed.</p>
</blockquote>
</aside>
<p>This didn’t have any effect.</p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="11" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>As a workaround I can change the behavior by changing the decimalsOption like this:</p>
<p>&gt;&gt;&gt; for w in findChildren(className=‘qMRMLCoordinatesWidget’):<br>
…   w.decimalsOption = 0</p>
</blockquote>
</aside>
<p>This made the <code>Image Spacing</code> widget use 4 decimals and 1 out of 3 spin boxes from  <code>Image Origin</code> use 3.</p>

---

## Post #14 by @pieper (2017-11-17 15:47 UTC)

<p>The snippet I pasted will change the modes for all the coordinate widgets.  If there’s a good combination of ‘decimals’ and ‘decimalsOption’ that works well we could make that the new default.  I didn’t try all the enum combinations for decimalsOptions.</p>

---

## Post #15 by @Fernando (2018-04-08 22:37 UTC)

<p>Hi Steve,</p>
<p>I just tried again your snippet and it helped me reduce the size of the widget, but it still takes a lot of space (around 45% of the screen) and it feels like it should need much less, maybe 30%. Shall I work on a PR to change the defaults of the module?</p>

---

## Post #16 by @Fernando (2018-04-08 22:41 UTC)

<p>By the way, when I collapse the <code>Volume Information</code> button, I can reduce a the size of the widget to a reasonable width.</p>

---

## Post #17 by @lassoan (2018-04-08 23:19 UTC)

<p>It could be also possible to change the coordinate widget to use flow layout (<a href="http://www.commontk.org/docs/html/classctkFlowLayout.html">http://www.commontk.org/docs/html/classctkFlowLayout.html</a>), which automatically places widgets into several rows if horizontal space is limited.</p>

---

## Post #18 by @pieper (2018-04-09 12:06 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="15" data-topic="1434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Shall I work on a PR to change the defaults of the module?</p>
</blockquote>
</aside>
<p>Yes, if you find a new set of defaults or other change (like layout as <a class="mention" href="/u/lassoan">@lassoan</a> suggested) it would be great to have a PR to test.</p>

---
