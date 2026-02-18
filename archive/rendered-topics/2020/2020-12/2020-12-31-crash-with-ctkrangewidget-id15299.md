# Crash with ctkRangeWidget

**Topic ID**: 15299
**Date**: 2020-12-31
**URL**: https://discourse.slicer.org/t/crash-with-ctkrangewidget/15299

---

## Post #1 by @xriobe (2020-12-31 14:26 UTC)

<p>Hi,</p>
<p>I have an issue with a wrong behavior of ctkRangeWidget that ends with the crash of Slicer 4.11.20200930 in Debug build (Ubuntu 20).</p>
<p>I think it is probably the same as this bug that has been closed without knowing how to reproduce:</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://mantisarchive.slicer.org/images/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://mantisarchive.slicer.org/view.php?id=2467" target="_blank" rel="noopener nofollow ugc">mantisarchive.slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://mantisarchive.slicer.org/view.php?id=2467" target="_blank" rel="noopener nofollow ugc">0002467: crash when scrolling through multivolumes - MantisBT</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>In my case it occurs in qMRMLVolumeThresholdWidget when using the sequence player if the frames have data with different scalar range values. At the change of frame, the threshold widget updates and call setRange(double min, double max), ending up in ctkRangeWidget::setRange where the slider and spinbox values are compared in a Q_ASSERT (ctkRangeWidget.cpp line 380):</p>
<p>Q_ASSERT(d-&gt;equal(d-&gt;Slider-&gt;maximumValue(), d-&gt;MaximumSpinBox-&gt;value()));</p>
<p>What happens is that a few lines above the call to<br>
d-&gt;Slider-&gt;setRange(d-&gt;MaximumSpinBox-&gt;minimum(), d-&gt;MinimumSpinBox-&gt;maximum());<br>
doesn’t always update the slider’s values.</p>
<p>As a side question about this line, shoudn’t it rather be d-&gt;Slider-&gt;setRange(d-&gt;<strong>Minimum</strong>SpinBox-&gt;minimum(), d-&gt;<strong>Maximum</strong>SpinBox-&gt;maximum());  ?</p>
<p>The reason why the values are not updated is because there are some rounding calculations with conversions to int during the process. It would be long to describe all here, but in ctkDoubleRangeSlider::setRange, the call to d-&gt;Slider-&gt;setRange(d-&gt;toInt(newMin), d-&gt;toInt(newMax)); converts the ranges to number of steps.</p>
<p>In an example with previous max range being 1272 and new one 1267, with a step of 10, it results in the same value rounded_int(1272/10) == rounded_int(1267/10) == 127, and in the implementation of the previous call to setRange, the “emit rangeChanged” is not done:</p>
<p>void QAbstractSlider::setRange(int min, int max)<br>
{<br>
Q_D(QAbstractSlider);<br>
int oldMin = d-&gt;minimum;<br>
int oldMax = d-&gt;maximum;<br>
d-&gt;minimum = min;<br>
d-&gt;maximum = qMax(min, max);<br>
if (oldMin != d-&gt;minimum || oldMax != d-&gt;maximum) {<br>
sliderChange(SliderRangeChange);<br>
emit rangeChanged(d-&gt;minimum, d-&gt;maximum);<br>
setValue(d-&gt;value); // re-bound<br>
}<br>
}</p>
<p>At the end, the slider (d-&gt;Slider-&gt;maximumValue()) and the spin box (d-&gt;MinimumSpinBox-&gt;maximum()) values are not synchronized and we are in the assert situation where 1267 != 1272.</p>
<p>I don’t really know what would be the correct fix for that.</p>
<ul>
<li>should the method QAbstractSlider::setRange be overridden in ctkRangeSlider and use more info for the condition check?</li>
<li>should ctkDoubleRangeSlider or ctkRangeWidget force call ctkRangeSlider::onRangeChanged or ctkRangeSlider::setValues in this situation?</li>
<li>something else ?</li>
</ul>

---

## Post #2 by @lassoan (2020-12-31 16:02 UTC)

<p>Thanks for the detailed analysis. Do you think the assert detects an actual error or it can normal that there are transient states during the check fails? We could simply remove this check or convert it to just logging a message if we find that it does not help but rather interferes with debugging.</p>

---

## Post #3 by @xriobe (2020-12-31 16:24 UTC)

<p>At the end of the process of all events and updates, those values for the slider and spin box are out of synchronization, so there is a real error if they have to be. For my case the crash is more annoying than this error, considering that it occurs only for some specific cases where it’s not a problem to have slightly different values so it is a very minor bug, but maybe other people needing exact match will have bigger issues…</p>
<p>Replacing the assert by a log could be a first easy step, better having a “polluted” log than a crash.</p>
<p>I see in different places of these ctk<em>Range</em> classes that sometimes the values are forced set for specific cases, so it could be a possibility if we can detect this rounding side effect, but i’m new to ctk/Slicer so i don’t know the impact of it in other cases, these widgets are pretty complex.</p>

---

## Post #4 by @xriobe (2021-02-01 17:10 UTC)

<p>Hi!<br>
Is there some decision about this among the core developers of CTK ?<br>
Or should we simply remove the asserts ?</p>
<p>Regards</p>

---

## Post #5 by @lassoan (2021-02-01 17:13 UTC)

<p>Please submit your proposed changes (e.g., replace plain assert by log assert) as a pull request to commontk/ctk. Thank you.</p>

---

## Post #6 by @xriobe (2021-02-01 18:50 UTC)

<p>Done here: <a href="https://github.com/commontk/CTK/pull/948" class="inline-onebox" rel="noopener nofollow ugc">Replace Q_ASSERT by qWarning to avoid crash in debug by xriobe · Pull Request #948 · commontk/CTK · GitHub</a><br>
I used qWarning as seen in other widgets</p>

---

## Post #7 by @jcfr (2021-02-01 20:07 UTC)

<p>Thanks for submitting the changes, the PR has been integrated.</p>
<p>Could  you know submit a PR updating CTK in Slicer ? Consider adding a commit similar to <a href="https://github.com/Slicer/Slicer/commit/3e650d3f8607323003bc5a624961a4c1b4f43291">this one</a></p>

---

## Post #8 by @xriobe (2021-02-01 21:20 UTC)

<p>Done: <a href="https://github.com/Slicer/Slicer/pull/5422" class="inline-onebox" rel="noopener nofollow ugc">BUG: Update CTK to fix a crash in ctkRangeWidget::SetRange in Debug mode by xriobe · Pull Request #5422 · Slicer/Slicer · GitHub</a></p>

---

## Post #9 by @jcfr (2021-02-01 21:30 UTC)

<p>Et voila, changes have been integrated into upstream Slicer<br>
<img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:">  <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=9" title=":rocket:" class="emoji" alt=":rocket:"></p>

---
