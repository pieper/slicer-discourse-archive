---
topic_id: 12773
title: "Slicer Roi Dimensions Input Numbers Autofill"
date: 2020-07-29
url: https://discourse.slicer.org/t/12773
---

# Slicer ROI dimensions Input numbers autofill

**Topic ID**: 12773
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/slicer-roi-dimensions-input-numbers-autofill/12773

---

## Post #1 by @manjula (2020-07-29 18:07 UTC)

<p>Hi,</p>
<p>it is bit annoying when we type in the dimensions of ROI box that it autofills the next number. I am not sure if I explain it properly.</p>
<p>For example if I want to type 0.75 and the moment I type 0.7 it fills the 0. So it is kind of annoying when we change the ROI frequently.  I noticed this in some other modules also but I cannot recall them now.</p>
<p>is this something that can be fixed ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f204754e07a5ed55a7ab6a42ad580f8fc4780c2a.png" data-download-href="/uploads/short-url/ywZ6aEmGaVEmVW2oQEHkHfwhDxU.png?dl=1" title="Screenshot from 2020-07-29 19-49-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f204754e07a5ed55a7ab6a42ad580f8fc4780c2a_2_690x190.png" alt="Screenshot from 2020-07-29 19-49-11" data-base62-sha1="ywZ6aEmGaVEmVW2oQEHkHfwhDxU" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f204754e07a5ed55a7ab6a42ad580f8fc4780c2a_2_690x190.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f204754e07a5ed55a7ab6a42ad580f8fc4780c2a_2_1035x285.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f204754e07a5ed55a7ab6a42ad580f8fc4780c2a_2_1380x380.png 2x" data-dominant-color="FAFAFA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-29 19-49-11</span><span class="informations">1417×391 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2020-07-29 18:28 UTC)

<p>Yes, it is annoying. ScalarOpacityMapping of the Volume Rendering module also shows some strange typing behaviors, when you try to manually enter values for points.</p>

---

## Post #3 by @pieper (2020-07-29 19:02 UTC)

<p>I believe those both use a <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkDoubleSpinBox.cpp"><code>ctkDoubleSpinBox</code></a> internially, so one could try changing it to use the <a href="https://doc.qt.io/qt-5/qlineedit.html#editingFinished"><code>editingFinished</code> signal</a>.  Might be a little work to dig through the layers since those range sliders have several modes to keep in sync.</p>

---

## Post #4 by @lassoan (2020-07-29 20:26 UTC)

<p>ctkDoubleSpinBox behavior is controlled by several flags and many combinations results in annoying behavior. Probably just a few of those flags would need to be flipped to fix this.</p>
<p>ScalarOpacityMapping has some extra complications - you need to remain between two two neighbor values and validation is necessary after each typed character to make the rendering update instantly.</p>

---

## Post #5 by @pieper (2020-07-29 22:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ScalarOpacityMapping has some extra complications - you need to remain between two two neighbor values and validation is necessary after each typed character to make the rendering update instantly.</p>
</blockquote>
</aside>
<p>The validation and re-rendering don’t need to happen on each typed character.  It would be fine to wait for editingFinished.</p>

---

## Post #6 by @lassoan (2020-07-29 22:25 UTC)

<p>Would waiting for editingFinished mean that you need to hit Tab and Shift+Tab to see the result of editing the value? That would be quite a lot of extra work. Also, the values are mainly intended to be visually adjusted by hitting the arrow up/down keys - waiting for editingFinished may break that, too (I haven’t tried).</p>

---

## Post #7 by @pieper (2020-07-30 00:04 UTC)

<p>I haven’t tried either, but the editingFinished is triggered either by losing focus (tab) or by hitting return, which I think is very conventional when entering text in a scenario like this.  Not sure what the arrow button behavior is, but that could be decoupled from the text input.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://doc.qt.io/qt-5/qlineedit.html#editingFinished">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" width="" height="">

      <a href="https://doc.qt.io/qt-5/qlineedit.html#editingFinished" target="_blank" rel="noopener">doc.qt.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://doc.qt.io/qt-5/qlineedit.html#editingFinished" target="_blank" rel="noopener">QLineEdit Class | Qt Widgets 6.6.1</a></h3>

  <p>The QLineEdit widget is a one-line text editor.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>[signal]void QLineEdit::editingFinished()<br>
This signal is emitted when the Return or Enter key is pressed or the line edit loses focus. Note that if there is a validator() or inputMask() set on the line edit and enter/return is pressed, the editingFinished() signal will only be emitted if the input follows the inputMask() and the validator() returns QValidator::Acceptable.</p>
</blockquote>

---
