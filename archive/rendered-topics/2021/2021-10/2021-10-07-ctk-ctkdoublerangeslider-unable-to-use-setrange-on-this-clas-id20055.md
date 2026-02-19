---
topic_id: 20055
title: "Ctk Ctkdoublerangeslider Unable To Use Setrange On This Clas"
date: 2021-10-07
url: https://discourse.slicer.org/t/20055
---

# [ctk.ctkDoubleRangeSlider()] Unable to use setRange() on this class

**Topic ID**: 20055
**Date**: 2021-10-07
**URL**: https://discourse.slicer.org/t/ctk-ctkdoublerangeslider-unable-to-use-setrange-on-this-class/20055

---

## Post #1 by @strider_hunter (2021-10-07 17:59 UTC)

<p>Hi,<br>
Im using Slicer 4.11.0-2020-09-05 and am building a python scriptable module.</p>
<p><strong>Issue</strong><br>
I wish to replicate the behavior of <code>slicer.qMRMLWindowLevelWidget()</code> as done on this <a href="https://github.com/Slicer/Slicer/blob/v4.11/Libs/MRML/Widgets/qMRMLWindowLevelWidget.cxx#L103" rel="noopener nofollow ugc">line</a>, but on my own using <code>ctk.ctkDoubleRangeSlider()</code>. I did not use the default <code>slicer.qMRMLRangeWidget()</code> since it does not seem to be using a spin box that allows floating values. But i am unable to use <code>setRange()</code> on  <code>ctk.ctkDoubleRangeSlider()</code> and hence it uses the default range of <code>[0,100]</code></p>
<p><strong>My Code</strong><br>
The erroneous line has been commented here</p>
<pre><code class="lang-auto">self.uncMinSpinBox  = qt.QDoubleSpinBox()
self.uncMinSpinBox.setRange(0.0, 10.0)
self.uncMinSpinBox.setValue(0.0)
self.uncMinSpinBox.setDecimals(1)
self.uncMinSpinBox.setSingleStep(0.1)
self.uncMinSpinBox.valueChanged.connect(self._uncMinSpinBoxChanged)

self.uncMaxSpinBox  = qt.QDoubleSpinBox()
self.uncMaxSpinBox.setRange(0, 10.0)
self.uncMaxSpinBox.setValue(10.0)
self.uncMaxSpinBox.setDecimals(1)
self.uncMaxSpinBox.setSingleStep(0.1)
self.uncMaxSpinBox.valueChanged.connect(self._uncMaxSpinBoxChanged)

self.uncSlider = ctk.ctkDoubleRangeSlider()
# self.uncSlider.setRange(0.0, 10.0) # &lt;&lt; -------------- ERRONEOUS LINE
self.uncSlider.orientation=qt.Qt.Horizontal
self.uncSlider.singleStep=0.1
self.uncSlider.setMinimumValue(0.0)
self.uncSlider.setMaximumValue(1.0)
self.uncSlider.positionsChanged.connect(self._onUncSliderChanged)
</code></pre>
<p>What am I missing here.</p>

---

## Post #2 by @lassoan (2021-10-07 18:15 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="1" data-topic="20055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>slicer.qMRMLRangeWidget()</p>
</blockquote>
</aside>
<p>The problem is just that <code>setRange</code> method is not a property setter and it was not declared as Q_INVOKABLE either:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkDoubleSlider.h#L93">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkDoubleSlider.h#L93" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkDoubleSlider.h#L93" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/Widgets/ctkDoubleSlider.h#L93</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="83" style="counter-reset: li-counter 82 ;">
          <li>/// This property holds the slider's maximum value.</li>
          <li>/// When setting this property, the minimum is adjusted if necessary to</li>
          <li>/// ensure that the range remains valid. Also the slider's current value</li>
          <li>/// is adjusted to be within the new range.</li>
          <li>void setMaximum(double max);</li>
          <li>double maximum()const;</li>
          <li></li>
          <li>///</li>
          <li>/// Sets the slider's minimum to min and its maximum to max.</li>
          <li>/// If max is smaller than min, min becomes the only legal value.</li>
          <li class="selected">void setRange(double min, double max);</li>
          <li></li>
          <li>///</li>
          <li>/// This property holds the slider's current value.</li>
          <li>/// The slider forces the value to be within the legal range:</li>
          <li>/// minimum &lt;= value &lt;= maximum.</li>
          <li>/// Changing the value also changes the sliderPosition.</li>
          <li>double value()const;</li>
          <li></li>
          <li>///</li>
          <li>/// This property holds the single step.</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It is a very easy fix (just add <code>Q_INVOKABLE</code> before <code>void</code>).</p>
<p>However, you don’t need this, as slicer.qMRMLRangeWidget() uses a double spinbox and sliders. If you set a quantity then the unit and number of decimals will be determined by the unit settings in the application. If you don’t set a quantity then it will be determined automatically (and you can probably add more decimals by typing and/or by hitting <kbd>Ctrl</kbd> + <kbd>+</kbd>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a72d187fabbeab4dd4c2d99a6acfe06fe17125ab.png" data-download-href="/uploads/short-url/nQUlZhDKpnYKd0VsclV8vuFmFK3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a72d187fabbeab4dd4c2d99a6acfe06fe17125ab_2_690x252.png" alt="image" data-base62-sha1="nQUlZhDKpnYKd0VsclV8vuFmFK3" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a72d187fabbeab4dd4c2d99a6acfe06fe17125ab_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a72d187fabbeab4dd4c2d99a6acfe06fe17125ab_2_1035x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a72d187fabbeab4dd4c2d99a6acfe06fe17125ab_2_1380x504.png 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1554×569 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2021-10-07 21:31 UTC)

<p>+1 for making range a property</p>

---

## Post #4 by @jamesobutler (2021-10-07 21:58 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="1" data-topic="20055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>Im using Slicer 4.11.0-2020-09-05</p>
</blockquote>
</aside>
<p>If you are looking to create a widget similar to <code>slicer.qMRMLWindowLevelWidget</code> where you are also using it to manage Window Level, I would suggest that your try out the latest Slicer Preview as this widget has changed since the version that you are using which is over a year old.</p>
<p>In the latest Slicer Preview you can do the following to set the range of the Window level bounds. Note the difference between setting the bounds versus setting the upper and lower values of the active range.</p>
<pre data-code-wrap="python"><code class="lang-python"># Load sample volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()

widget = slicer.qMRMLWindowLevelWidget()
widget.setMRMLVolumeNode(mrHead)
widget.setMinMaxBounds(-200, 200)
widget.setMinMaxRangeValue(-100,100)
widget.show()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec7b8b14e8166c31c695c75ad060783816a2f0b5.png" data-download-href="/uploads/short-url/xK1n8XFkluSJ3PXnKAjpNqyCsEB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec7b8b14e8166c31c695c75ad060783816a2f0b5_2_690x75.png" alt="image" data-base62-sha1="xK1n8XFkluSJ3PXnKAjpNqyCsEB" width="690" height="75" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec7b8b14e8166c31c695c75ad060783816a2f0b5_2_690x75.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec7b8b14e8166c31c695c75ad060783816a2f0b5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec7b8b14e8166c31c695c75ad060783816a2f0b5.png 2x" data-dominant-color="A3A5A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">808×88 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @strider_hunter (2021-10-08 10:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>qMRMLRangeWidget</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> !<br>
I followed your suggestion and did the following.</p>
<pre><code class="lang-auto">self.uncSlider2 = slicer.qMRMLRangeWidget()
self.uncSlider2.setRange(0.0, 1.0)
self.uncSlider2.singleStep=0.1 # &lt;----- this did the trick
self.uncSlider2.valuesChanged.connect(self._onUncSliderChanged2)
viewParametersFormLayout.addRow(self.uncSlider2)
</code></pre>
<p>It now looks like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d5fc657e5f0c6f075dc5207def0378c56d7e225.png" alt="qMRMLRangeWidget" data-base62-sha1="hT6SzXF94XPBnjiUJ0zlAJKuBrT" width="458" height="60"></p>
<p>But, I was unable to find (<a href="https://apidocs.slicer.org/v4.11/classqMRMLRangeWidget.html" rel="noopener nofollow ugc">here</a> or <a href="https://github.com/Slicer/Slicer/blob/v4.11/Libs/MRML/Widgets/qMRMLRangeWidget.cxx" rel="noopener nofollow ugc">here</a>) a function to avoid showing the circled item.<br>
I may sound too pedantic, but given that I am designing this interface for clinicians, I would prefer keeping the interface as minimal as possible. I do not want the users playing with the min and max values of the range.</p>

---

## Post #6 by @lassoan (2021-10-08 14:33 UTC)

<p>We don’t always expose specific API to manipulate such small details, but you can always have full access to all Qt widgets that you can use (at your won risk). Hiding the button has no risk, and probably it is not a very common need (so there would be no need to create a specific API for it), so you can just get that button and hide it:</p>
<pre><code class="lang-python">tripleDotButton = slicer.util.findChildren(self.uncSlider2, className='QToolButton')[0]
tripleDotButton.hide()
</code></pre>
<p>If you need a list of child widgets (so that you know the type and name of the object), you can use <code>slicer.util.findChildren</code> method, specifying just the parent widget.</p>

---
