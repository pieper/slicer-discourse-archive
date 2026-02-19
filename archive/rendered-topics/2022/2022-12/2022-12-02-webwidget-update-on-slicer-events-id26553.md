---
topic_id: 26553
title: "Webwidget Update On Slicer Events"
date: 2022-12-02
url: https://discourse.slicer.org/t/26553
---

# Webwidget Update on Slicer Events

**Topic ID**: 26553
**Date**: 2022-12-02
**URL**: https://discourse.slicer.org/t/webwidget-update-on-slicer-events/26553

---

## Post #1 by @connorh (2022-12-02 14:32 UTC)

<p>Hello,</p>
<p>I’m using a qSlicerWebWidget to display some interactive plots in Slicer. I’m wondering if there’s a way to call a method within my javascript/html when something changes in the Slicer scene (add a listener within the webwidget). For example, I would like to update what is displayed in my qSlicerWebWidget if a sequence in my Slicer scene changes frame, or if the crosshair moves.</p>
<p>Is there a way to do this without reloading the entire html and assigning it to the WebWidget? Or is the only available interaction between webwidget and Slicer  <code>window.slicerPython.evalPython</code>?</p>
<p>I know I could achieve this my adding a listener within python and then re-loading the full HTML each time, I’m just trying to keep it fast.</p>

---

## Post #2 by @pieper (2022-12-02 16:02 UTC)

<p>Yes, you can communicate both ways.  <code>window.slicerPython.evalPython</code> lets the JavaScript execute Python code in Slicer’s environment, and <code>qSlicerWebWidget.evalJS</code> lets Python or C++ code execute JS code.</p>
<p>You can connect to the <code>qSlicerWebWidget.evalResult</code> signal to get the result of your computation.  Since the JS code runs asynchronously, the signal returns both the evaluated JS and the result so you can keep track of which code generated the result.</p>
<p>It’s all event driven and runs very fast.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/QTGUI/qSlicerWebWidget.h#L97">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/QTGUI/qSlicerWebWidget.h#L97" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/QTGUI/qSlicerWebWidget.h#L97" target="_blank" rel="noopener">Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/QTGUI/qSlicerWebWidget.h#L97</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="87" style="counter-reset: li-counter 86 ;">
          <li>  void setJavaScriptConsoleMessageLoggingEnabled(bool enable);</li>
          <li>
          </li>
<li>//  QWebEngineProfile* profile()const;</li>
          <li>//  void setProfile(QWebEngineProfile* profile);</li>
          <li>
          </li>
<li>  /// Return a reference to the QWebView used internally.</li>
          <li>  Q_INVOKABLE QWebEngineView * webView();</li>
          <li>
          </li>
<li>  /// Convenient function to evaluate JS in main frame context</li>
          <li>  /// from C++ or Python code</li>
          <li class="selected">  Q_INVOKABLE QString evalJS(const QString &amp;js);</li>
          <li>
          </li>
<li>  /// Convenience for setting the internal webView QUrl from a QString</li>
          <li>  Q_INVOKABLE QString url();</li>
          <li>
          </li>
<li>  /// Convenience for setting the internal webView html from a QString</li>
          <li>  Q_INVOKABLE void setHtml(const QString &amp;html, const QUrl &amp;baseUrl = QUrl());</li>
          <li>
          </li>
<li>public slots:</li>
          <li>
          </li>
<li>  /// Convenience for setting the internal webView QUrl from a QString</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Applications/SlicerApp/Testing/Python/WebEngine.py#L109-L221">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Applications/SlicerApp/Testing/Python/WebEngine.py#L109-L221" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Applications/SlicerApp/Testing/Python/WebEngine.py#L109-L221" target="_blank" rel="noopener">Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Applications/SlicerApp/Testing/Python/WebEngine.py#L109-L221</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="109" style="counter-reset: li-counter 108 ;">
          <li>class WebEngineTest(ScriptedLoadableModuleTest):</li>
          <li>    """</li>
          <li>    This is the test case for your scripted module.</li>
          <li>    Uses ScriptedLoadableModuleTest base class, available at:</li>
          <li>    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py</li>
          <li>    """</li>
          <li>
          </li>
<li>    def setUp(self):</li>
          <li>        """ Do whatever is needed to reset the state - typically a scene clear will be enough.</li>
          <li>        """</li>
          <li>        self.gotResponse = False</li>
          <li>        self.gotCorrectResponse = False</li>
          <li>
          </li>
<li>    def runTest(self):</li>
          <li>        """Run as few or as many tests as needed here.</li>
          <li>        """</li>
          <li>        self.setUp()</li>
          <li>        self.test_WebEngine1()</li>
          <li>
          </li>
<li>    def onEvalResult(self, js, result):</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Applications/SlicerApp/Testing/Python/WebEngine.py#L109-L221" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
