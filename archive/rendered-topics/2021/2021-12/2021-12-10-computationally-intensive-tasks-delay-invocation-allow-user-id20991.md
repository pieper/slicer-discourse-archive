---
topic_id: 20991
title: "Computationally Intensive Tasks Delay Invocation Allow User"
date: 2021-12-10
url: https://discourse.slicer.org/t/20991
---

# Computationally intensive tasks: delay invocation; allow user to abort

**Topic ID**: 20991
**Date**: 2021-12-10
**URL**: https://discourse.slicer.org/t/computationally-intensive-tasks-delay-invocation-allow-user-to-abort/20991

---

## Post #1 by @DIV (2021-12-10 03:47 UTC)

<p>Some tasks in Slicer are computationally intensive;  an example could be running the <code>Grow from seeds</code> effect in the <strong>Segment Editor</strong> module.</p>
<p><strong><em>Accidentally</em> invoking a computationally intensive task</strong><br>
When dragging the <code>Seed locality</code> slider for this effect, Slicer is prone to initiate running of the analysis before the user has released the slider knob. (I think it is being triggered when the user momentarily pauses the dragging, albeit <em>without</em> releasing the mouse button.)<br>
This should not happen.  The infelicity could be ignored if the task took milliseconds to run, but when it takes dozens of seconds (and potentially minutes) to run, it causes a problem for the user.</p>
<p>One solution may be along the following lines:<br>
“when the slider is pressed, I disconnect the valueChanged slot, and when the slider is released, I reconnect it and I throw a valueChanged signal”</p><aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/43152489/pyqt5-qslider-valuechanged-event-with-delay">
  <header class="source">

      <a href="https://stackoverflow.com/questions/43152489/pyqt5-qslider-valuechanged-event-with-delay" target="_blank" rel="noopener nofollow ugc">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/2924323/ramesh-x" target="_blank" rel="noopener nofollow ugc">
    <img alt="Ramesh-X" src="https://i.stack.imgur.com/6XBqj.jpg?s=256&amp;g=1" class="thumbnail onebox-avatar" width="256" height="256">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/43152489/pyqt5-qslider-valuechanged-event-with-delay" target="_blank" rel="noopener nofollow ugc">PyQt5: QSlider valueChanged event with delay</a>
</h4>

<div class="tags">
  <strong>python, python-3.x, pyqt5, qslider</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/2924323/ramesh-x" target="_blank" rel="noopener nofollow ugc">
    Ramesh-X
  </a>
  on <a href="https://stackoverflow.com/questions/43152489/pyqt5-qslider-valuechanged-event-with-delay" target="_blank" rel="noopener nofollow ugc">03:28AM - 01 Apr 17 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
A complication of this solution:  the current implementation of the widget seems to be to (sensibly) not execute the call until the user has stopped adjusting the value:  e.g. clicking several times in ‘quick’ succession on the slider’s rail only results in invocation once the series of clicks is completed (recognised as a pause in the sequence).  Reconnecting a disconnected slot prematurely might degrade this behaviour.</p>
<p><strong>Aborting a computationally intensive task</strong><br>
Another situation is where the user has genuinely changed a setting (by releasing the mouse button, or whatever) or otherwise (<em>intentionally or accidentally</em>) caused a computationally intensive task to be invoked.<br>
I have not seen any way to safely abort such tasks:  the only avenues I’m aware of are to wait for the task to finish, or close 3D Slicer entirely.  The former is time-consuming, and will not work in the (rare) case of a bug preventing the task from finishing at all.  The latter is tiresome even if all prior work was saved, and very troublesome if prior work was not saved (potentially minimised with <a href="https://discourse.slicer.org/t/autosave-option/17025">auto-save</a>).<br>
Is there an abort option?  If not, can one be added?</p>
<p>—DIV</p>

---

## Post #2 by @DIV (2021-12-10 04:04 UTC)

<p>Note:  the <code>Seed locality</code> slider setting seems to call the task regardless of whether <code>Auto-update</code> is ticked or not.  I’m not sure that that’s the expected behaviour.  But even if it isn’t, each of the above two points (in the original post) still stands.</p>

---

## Post #3 by @lassoan (2021-12-11 19:38 UTC)

<p>It is no problem at all to apply seed locality when the mouse button is released (by turning off <code>tracking</code> property of the slider). It would be great if you could send a pull request with this change, but if you are not sure how to do it then I can get to it early next week.</p>
<p>Grow from seeds update should take only a few seconds. Make sure you use the latest Slicer Preview Release. The latest Stable Release had some unnecessary extra updates. Seed locality may require a full recomputation, so that may take up to a few ten seconds, but that’s not a parameter that you need to tune often, but you need to determine the good value only once for a certain task and then the same value should be usable for all patients.</p>

---

## Post #4 by @DIV (2022-01-18 05:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="20991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Grow from seeds update should take only a few seconds. Make sure you use the latest Slicer Preview Release. The latest Stable Release had some unnecessary extra updates.</p>
</blockquote>
</aside>
<p>Thank-you for the feedback, Andras.<br>
It definitely was very slow;  although admittedly I also had ended up with a very large number of manually painted regions, in an attempt to finesse the outcome.<br>
Generally I had only been using the Stable Releases up until now, as the idea of using an ‘unstable’ release was off-putting.  With most software I’ve encountered, regular users are mainly encouraged to use regular releases, rarely beta versions, and never alpha versions.<br>
<em>3D Slicer</em> seems to be different, so, following your advice, I will try the “Preview” releases in future.<br>
—DIV</p>

---

## Post #5 by @DIV (2022-01-18 05:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="20991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is no problem at all to apply seed locality when the mouse button is released (by turning off <code>tracking</code> property of the slider). It would be great if you could send a pull request with this change, but if you are not sure how to do it then I can get to it early next week.</p>
</blockquote>
</aside>
<p>I am not sure of how to code this.<br>
My best guess, following your comment, is something like <code>seedLocalityFactorSlider.tracking = 0</code> or <code>seedLocalityFactorSlider.tracking = 'off'</code> or <code>seedLocalityFactorSlider.tracking = False</code>…<br>
If you are able to get to this, would you be able to somehow link to the changes you’ve made?</p>
<p>Thanks,<br>
DIV</p>

---

## Post #6 by @lassoan (2022-01-18 14:15 UTC)

<aside class="quote no-group" data-username="DIV" data-post="4" data-topic="20991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p><em>3D Slicer</em> seems to be different, so, following your advice, I will try the “Preview” releases in future.</p>
</blockquote>
</aside>
<p>If we can release a new Slicer version in every quarter then you can use the latest stable. However, the stable release was delayed by due to complications with VTK update and other refactoring work in preparation for Slicer5, that’s why you are better off overall with the Slicer Preview Release in these months. If we release Slicer5 then you can get back to using the latest Slicer Stable Release.</p>
<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>My best guess, following your comment, is something like <code>seedLocalityFactorSlider.tracking = 0</code> or <code>seedLocalityFactorSlider.tracking = 'off'</code> or <code>seedLocalityFactorSlider.tracking = False</code> …</p>
</blockquote>
</aside>
<p>Type of the <code>tracking</code> property of the ctkSliderWidget is a <code>bool</code>:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/4839f18fb7cf1486b0f16e88f031137ce15ff550/Libs/Widgets/ctkSliderWidget.h#L63">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/4839f18fb7cf1486b0f16e88f031137ce15ff550/Libs/Widgets/ctkSliderWidget.h#L63" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/4839f18fb7cf1486b0f16e88f031137ce15ff550/Libs/Widgets/ctkSliderWidget.h#L63" target="_blank" rel="noopener">commontk/CTK/blob/4839f18fb7cf1486b0f16e88f031137ce15ff550/Libs/Widgets/ctkSliderWidget.h#L63</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="53" style="counter-reset: li-counter 52 ;">
          <li>  Q_PROPERTY(double pageStep READ pageStep WRITE setPageStep)</li>
          <li>  Q_PROPERTY(double minimum READ minimum WRITE setMinimum)</li>
          <li>  Q_PROPERTY(double maximum READ maximum WRITE setMaximum)</li>
          <li>  Q_PROPERTY(double value READ value WRITE setValue)</li>
          <li>  Q_PROPERTY(QString prefix READ prefix WRITE setPrefix)</li>
          <li>  Q_PROPERTY(QString suffix READ suffix WRITE setSuffix)</li>
          <li>  Q_PROPERTY(double tickInterval READ tickInterval WRITE setTickInterval)</li>
          <li>  Q_PROPERTY(QSlider::TickPosition tickPosition READ tickPosition WRITE setTickPosition)</li>
          <li>  Q_PROPERTY(SynchronizeSiblings synchronizeSiblings READ synchronizeSiblings WRITE setSynchronizeSiblings)</li>
          <li>  Q_PROPERTY(Qt::Alignment spinBoxAlignment READ spinBoxAlignment WRITE setSpinBoxAlignment)</li>
          <li class="selected">  Q_PROPERTY(bool tracking READ hasTracking WRITE setTracking)</li>
          <li>  Q_PROPERTY(bool spinBoxVisible READ isSpinBoxVisible WRITE setSpinBoxVisible);</li>
          <li>  Q_PROPERTY(bool popupSlider READ hasPopupSlider WRITE setPopupSlider);</li>
          <li>  Q_PROPERTY(bool invertedAppearance READ invertedAppearance WRITE setInvertedAppearance)</li>
          <li>  Q_PROPERTY(bool invertedControls READ invertedControls WRITE setInvertedControls)</li>
          <li></li>
          <li>public:</li>
          <li></li>
          <li>  /// Synchronize properties of the slider siblings:</li>
          <li>  /// NoSynchronize:</li>
          <li>  /// The slider widget siblings aren't updated and this widget does not update</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Therefore, the proper way to set it is to use the Python bool type (<code>True</code> or <code>False</code>). Automatic casting from integer probably works, too, so <code>1</code> and <code>0</code> may be usable, too. String values, such as <code>"on"</code> or <code>"off"</code> will not work. Add this single line where the slider is set up and see if it works as you expect. If it does then please create a pull request with that change. Thank you!</p>

---
