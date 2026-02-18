# Apply stylesheet for `ctkRangeSlider`

**Topic ID**: 20604
**Date**: 2021-11-12
**URL**: https://discourse.slicer.org/t/apply-stylesheet-for-ctkrangeslider/20604

---

## Post #1 by @keri (2021-11-12 17:37 UTC)

<p>Hi,</p>
<p>Is there a way to change <code>ctkRangeSlider</code> color filled between min and max values?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3de6e5ba22703f1e9040653e941c7140b24653b8.png" alt="image" data-base62-sha1="8PBOU3r0vFsXW3yw89RJ7AyqGgw" width="342" height="74"></p>
<p>I look in the source code of <code>ctkRangeSlider</code> and I can’t understand what parameter controls this.<br>
The original <a href="https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider" rel="noopener nofollow ugc">QSlider</a> seems to have no option to control this color.</p>
<p>Also where are Slicer dark and light themes are defined?<br>
I’m not much familiar with styling but I expected that Slicer use some Qt Style Sheet (probably some <code>.css</code> file) but instead I can see classes like (slicersources-src/Base/QTGUI) <code>qSlicerStyle</code>, <code>qSlicerDarkStyle</code>, <code>qSlicerLightStyle</code> inherited form <code>ctkProxyStyle</code> → <code>QProxyStyle</code>. Are these classes are fully responsible (or almost fully responsible) for Slicer GUI style?</p>

---

## Post #2 by @jamesobutler (2021-11-12 17:55 UTC)

<p>Widgets use colors based on the ColorRole from the Palette. This provides a theme of colors used consistently across the GUI.</p>
<p>I believe a Qt slider’s active range uses the <a href="https://doc.qt.io/qt-5/qpalette.html#ColorRole-enum" rel="noopener nofollow ugc">QPalette::Highlight</a> specification. You’re showing Slicer when it is using the Slicer Dark mode, so the Highlight color of the QPalette for Slicer Dark is at:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/6582c1f0b0ec5772776564e5c2704e78b82ea261/Base/QTGUI/qSlicerStyle.cxx#L270">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/6582c1f0b0ec5772776564e5c2704e78b82ea261/Base/QTGUI/qSlicerStyle.cxx#L270" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6582c1f0b0ec5772776564e5c2704e78b82ea261/Base/QTGUI/qSlicerStyle.cxx#L270" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/6582c1f0b0ec5772776564e5c2704e78b82ea261/Base/QTGUI/qSlicerStyle.cxx#L270</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="260" style="counter-reset: li-counter 259 ;">
          <li>  palette.setColor(QPalette::ButtonText, Qt::white);</li>
          <li>  palette.setColor(QPalette::Disabled, QPalette::ButtonText, "#b4b4b4");</li>
          <li>  palette.setColor(QPalette::BrightText, "#ff4444"); // Lighter than Qt::red</li>
          <li>  // Color roles used mostly for 3D bevel and shadow effects.</li>
          <li>  palette.setColor(QPalette::Light, "#828284");  // Lighter than Button color.</li>
          <li>  palette.setColor(QPalette::Midlight, "#5a5a5b");  // Between Button and Light.</li>
          <li>  palette.setColor(QPalette::Dark, "#232323");  // Darker than Button.</li>
          <li>  palette.setColor(QPalette::Mid, "#2b2b2b");  // Between Button and Dark.</li>
          <li>  palette.setColor(QPalette::Shadow, "#141414");  // A very dark color.</li>
          <li>  // Color roles relate to selected (marked) items</li>
          <li class="selected">  palette.setColor(QPalette::Highlight, "#3ca4ff");</li>
          <li>  palette.setColor(QPalette::Disabled, QPalette::Highlight, "#505050");</li>
          <li>  palette.setColor(QPalette::HighlightedText, Qt::white);</li>
          <li>  palette.setColor(QPalette::Disabled, QPalette::HighlightedText, "#6d6d6d");</li>
          <li>  // Color roles related to hyperlinks</li>
          <li>  palette.setColor(QPalette::Link, "#3ca4ff");</li>
          <li>  return palette;</li>
          <li>}</li>
          <li>
          </li>
<li>//------------------------------------------------------------------------------</li>
          <li>int qSlicerStyle::styleHint(StyleHint hint, const QStyleOption *opt, const QWidget *widget,</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @keri (2021-11-12 20:22 UTC)

<p>Thank you very much,</p>
<p>You were right!</p>
<p>It took some time to understand how to create custom style plugin so that it is visible in Slicer-&gt;Edit-&gt;Application Settings-&gt;Appearance-&gt;Themes but after I did that I could change the color of <code>ctkRangeSlicer</code><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/937b8b5701b00e25501f1d8b0bf71a118345270f.png" alt="image" data-base62-sha1="l2GSAZj2zixRPSS539MBcm4htBJ" width="278" height="27"></p>

---
