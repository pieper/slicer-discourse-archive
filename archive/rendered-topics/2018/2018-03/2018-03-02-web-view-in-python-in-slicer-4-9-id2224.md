---
topic_id: 2224
title: "Web View In Python In Slicer 4 9"
date: 2018-03-02
url: https://discourse.slicer.org/t/2224
---

# Web view in Python in Slicer-4.9

**Topic ID**: 2224
**Date**: 2018-03-02
**URL**: https://discourse.slicer.org/t/web-view-in-python-in-slicer-4-9/2224

---

## Post #1 by @lassoan (2018-03-02 03:27 UTC)

<p>In Qt4, I used to use <code>qt.QWebView()</code> to show html content on the GUI, but this does not seem to be available in Qt5 in Slicer. I’ve tried to access Qt WebEngine from Python but it is either not wrapped or I just could not find it.</p>
<p>Is there an equivalent in Qt5?</p>

---

## Post #2 by @jcfr (2018-03-02 03:52 UTC)

<p>This should work on both Qt4 and Qt5:</p>
<pre><code class="lang-auto">w = slicer.qSlicerWebWidget()
w.webView().url = qt.QUrl("https://eff.org/")
w.show()
</code></pre>

---

## Post #3 by @jcfr (2018-03-02 07:51 UTC)

<p>This approach also has the advantage of abstracting the interface.</p>
<p>Following <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26986">r26986</a>, executing javascript on the page can be done from python using:</p>
<pre><code class="lang-auto">w.evalJS("window.alert('Hello')")
</code></pre>

---

## Post #4 by @lassoan (2018-03-03 15:07 UTC)

<p>Thank you very much! The web widget appears, with a small style error that scrollbars (both horizontal and vertical) have about 2x larger than anywhere else in the application:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e146afbb9fb4a6e0c021e0340d3992879440ab6.jpeg" data-download-href="/uploads/short-url/4i64igZEWAoUKOdOgE2PZu2AYZ0.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e146afbb9fb4a6e0c021e0340d3992879440ab6_2_558x500.jpg" alt="image" data-base62-sha1="4i64igZEWAoUKOdOgE2PZu2AYZ0" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e146afbb9fb4a6e0c021e0340d3992879440ab6_2_558x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e146afbb9fb4a6e0c021e0340d3992879440ab6_2_837x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e146afbb9fb4a6e0c021e0340d3992879440ab6.jpeg 2x" data-dominant-color="C8D2DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1062×950 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, a bigger issue is that webView’s <code>page</code> member (QWebEnginePage) is not accessible from Python. This severely limits usability.</p>
<p>For example, we used this code before, to set the widget size to show a HTML page in the layout without scrollbars (make the widget height as large as the content after content was loaded):</p>
<pre><code>frame = webView.page().mainFrame()
webView.page().setViewportSize(frame.contentsSize)
webView.setMinimumHeight(frame.contentsSize.height())
</code></pre>
<p>Why <code>page</code> is not accessible in Python? Why I cannot instantiate a QWebEngineView object directly in Python?</p>

---

## Post #5 by @jcfr (2018-03-03 22:55 UTC)

<p>We rely on PythonQt for wrapping the Qt base class.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> At some point did you look into enabling the wrapping for webengine ?</p>

---

## Post #6 by @pieper (2018-03-04 14:39 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="2224">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> At some point did you look into enabling the wrapping for webengine ?</p>
</blockquote>
</aside>
<p>Right, I believe PythonQt does not yet wrap all the classes we would need and not clear yet when it will.</p>
<p>Instead it seemed we could get by with writing higher level methods in C++ and expose them in qSlicerWebWidget for use in python.  Something like <code>webWidget.setSizeToContentSize()</code> for similar for the situation Andras mentioned.</p>
<p>I think we have a fairly short list of requirements at that level.</p>

---

## Post #7 by @lassoan (2018-03-04 14:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="2224">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I believe PythonQt does not yet wrap all the classes we would need and not clear yet when it will</p>
</blockquote>
</aside>
<p>Just out of curiosity, how difficult it is to add wrapping for a class? Isn’t it automatic? Is there something particularly problematic with the web view? Do they accept pull requests if we implement wrapping for some new classes?</p>
<p>In the short term, I’ll just add functions in our own wrapper class in Slicer.</p>

---

## Post #8 by @pieper (2018-03-05 12:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="2224">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Just out of curiosity, how difficult it is to add wrapping for a class? Isn’t it automatic? Is there something particularly problematic with the web view? Do they accept pull requests if we implement wrapping for some new classes?</p>
</blockquote>
</aside>
<p>There is a custom wrapper generator and it can be run on any Qt source tree to generate the wrapping.  I hadn’t looked into it much until recently there was <a href="https://sourceforge.net/p/pythonqt/discussion/631392/thread/c989429c/">an issue with the socket types</a>.  To avoid needing to compile and run the generator when building PythonQt, the generated sources are in the repository and they are only updated as needed (as needed by Florian for MeVislab basically), but it’s not that hard to build the generator and experiment.  There are already some QtWebEngine files in the repository but they aren’t enabled and didn’t completely work last time I checked (early in the Slicer Qt5 porting process).</p>
<p>So, yes, it may be that updating PythonQt’s generator to work well with QtWebEngine would be a more general fix.  And yes probably the key elements of that would be possible to put back into PythonQt.  But PythonQt uses qmake, so the CMake parts that we would need would still be in the commontk fork.</p>

---

## Post #9 by @lassoan (2018-03-05 13:42 UTC)

<p>Thanks for the information!</p>
<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="2224">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>There are already some QtWebEngine files in the repository but they aren’t enabled and didn’t completely work</p>
</blockquote>
</aside>
<p>OK, probably I won’t try to enable it then. I’ll just add what I specifically need to the Slicer wrapper.</p>

---
