---
topic_id: 2355
title: "Fade In Between Images"
date: 2018-03-19
url: https://discourse.slicer.org/t/2355
---

# Fade In Between Images

**Topic ID**: 2355
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/fade-in-between-images/2355

---

## Post #1 by @asheu (2018-03-19 05:29 UTC)

<p>Hi there,</p>
<p>Was wondering if there was any existing module in Slicer that allow us to load 2 data sets and then fade in and out between the data sets?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @brhoom (2018-03-19 08:22 UTC)

<p>you can blend two volumes using these steps as this <a href="https://mtixnat.uni-koblenz.de/owncloud/index.php/s/HxzYWoaIRZ4BxwD" rel="nofollow noopener">video</a> shows. The two volumes should be aligned first if you want to see them in the same location. The slider controls the influence of each volume e.g. .5 means equal blending.</p>
<p>If you want to do it programmatically, it is just matrix addition e.g. imageC=  imageA + imageB.</p>

---

## Post #3 by @lassoan (2018-03-19 14:30 UTC)

<p>You can also fade between foreground/background volume by holding down Ctrl-LeftClick-MouseMove up/down. Or, hit ‘T’ key to show/hide foreground volume.</p>
<p>You can also find “Reveal cursor” feature usable in Compare Volumes module.</p>

---

## Post #4 by @asheu (2018-03-19 22:51 UTC)

<p>thanks a lot for the responses!</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> is it possible to pull out the specific slider widget that controls the fading in and fading out and allows us to select the different volumes as the foreground and background? for loadable modules, i was able to create a widget representation and then pull specific widgets from the UI, is this also the case for the opacity model?</p>
<p>thanks a lot!</p>
<p>edit: i think the better way to phrase it is that i know i need to access the MRML scene over here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/48cdc292056274112aca1d1fd4204d97729248fd/Libs/MRML/Widgets/Resources/UI/qMRMLSliceControllerWidget.ui" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/48cdc292056274112aca1d1fd4204d97729248fd/Libs/MRML/Widgets/Resources/UI/qMRMLSliceControllerWidget.ui" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/48cdc292056274112aca1d1fd4204d97729248fd/Libs/MRML/Widgets/Resources/UI/qMRMLSliceControllerWidget.ui</a></h4>
<pre><code class="lang-ui">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;ui version="4.0"&gt;
 &lt;class&gt;qMRMLSliceControllerWidget&lt;/class&gt;
 &lt;widget class="ctkPopupWidget" name="qMRMLSliceControllerWidget"&gt;
  &lt;property name="geometry"&gt;
   &lt;rect&gt;
    &lt;x&gt;0&lt;/x&gt;
    &lt;y&gt;0&lt;/y&gt;
    &lt;width&gt;329&lt;/width&gt;
    &lt;height&gt;138&lt;/height&gt;
   &lt;/rect&gt;
  &lt;/property&gt;
  &lt;property name="windowTitle"&gt;
   &lt;string&gt;Slice Controller&lt;/string&gt;
  &lt;/property&gt;
  &lt;layout class="QGridLayout" name="gridLayout"&gt;
   &lt;property name="margin"&gt;
    &lt;number&gt;0&lt;/number&gt;
   &lt;/property&gt;
   &lt;property name="spacing"&gt;
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/48cdc292056274112aca1d1fd4204d97729248fd/Libs/MRML/Widgets/Resources/UI/qMRMLSliceControllerWidget.ui" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>but do not know where it lies in the slicer documentation.</p>

---

## Post #5 by @lassoan (2018-03-20 18:00 UTC)

<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_a_Slice_View">examples in the script repository</a> and the <a href="http://apidocs.slicer.org/master/classes.html">Slicer API documentation</a>.</p>

---
