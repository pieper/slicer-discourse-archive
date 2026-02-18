# Implementing PyTest-qt

**Topic ID**: 28096
**Date**: 2023-02-28
**URL**: https://discourse.slicer.org/t/implementing-pytest-qt/28096

---

## Post #1 by @hannahm (2023-02-28 16:38 UTC)

<p>Are we able to implement PyTest-qt into our custom slicer app? I don’t know all of the discrepancies associated with the licensing but I would like to implement it to be able to run GUI based tests.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pytest-dev/pytest-qt">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pytest-dev/pytest-qt" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/c79789a20176997e1f6d016d61591718dd60bf4bb3fed87a054a5f3b84c3dd14/pytest-dev/pytest-qt" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pytest-dev/pytest-qt" target="_blank" rel="noopener nofollow ugc">GitHub - pytest-dev/pytest-qt: pytest plugin for Qt (PyQt5/PyQt6 and...</a></h3>

  <p>pytest plugin for Qt (PyQt5/PyQt6 and PySide2/PySide6) application testing - GitHub - pytest-dev/pytest-qt: pytest plugin for Qt (PyQt5/PyQt6 and PySide2/PySide6) application testing</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @jamesobutler (2023-02-28 17:41 UTC)

<p>PyTest-qt summary:</p>
<blockquote>
<p>The main usage is to use the <code>qtbot</code> fixture, responsible for handling <code>qApp</code> creation as needed and provides methods to simulate user interaction, like key presses and mouse clicks:</p>
</blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> Do you have any thoughts about python testing of Slicer modules and their usage of simulated user interaction?</p>
<p>How does QtTesting fit into current recommendations?</p>
<ul>
<li>QtTesting and Python: <a href="https://discourse.slicer.org/t/macro-xml-to-python/15803/2" class="inline-onebox">Macro XML to python - #2 by jcfr</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/QtTesting" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/SlicerApplication/QtTesting - Slicer Wiki</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/QtTesting" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/QtTesting - Slicer Wiki</a></li>
</ul>
<blockquote>
<p>Recording of macro using QtTesting should be considered experimental.<br>
We suggest to implement workflow automation through Python scripts operating at a lower level by changing properties of MRML nodes and calling module logic functions</p>
</blockquote>
<p>One of the above links has the above header. Does this mean it is not recommended to do this GUI level type of testing that uses simulated clicks and interactions? Slicer core appears to utilize some QtTesting in <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Widgets/Testing/qMRMLCheckableNodeComboBoxEventTranslatorPlayerTest1.xml" rel="noopener nofollow ugc">qMRMLCheckableNodeComboBoxEventTranslatorPlayerTest1.xml</a>. I assume this is because it is a qMRML QObject rather than say a Slicer module.</p>
<p>Are <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/selftests.html" rel="noopener nofollow ugc">Self-tests</a> the Slicer recommended way for scripted loadable module python testing? Is the <code>clickAndDrag</code> method the recommended manner for synthetic input into Slicer modules, or is something like PyTest-qt as mentioned in the original post a possibility for Slicer scripted module testing?</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/2db14ceb03248e0fea6610bcdf059f4f24f6cc5a/Base/Python/slicer/util.py#L3028-L3085">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/2db14ceb03248e0fea6610bcdf059f4f24f6cc5a/Base/Python/slicer/util.py#L3028-L3085" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/2db14ceb03248e0fea6610bcdf059f4f24f6cc5a/Base/Python/slicer/util.py#L3028-L3085" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/2db14ceb03248e0fea6610bcdf059f4f24f6cc5a/Base/Python/slicer/util.py#L3028-L3085</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="3028" style="counter-reset: li-counter 3027 ;">
          <li>def clickAndDrag(widget, button='Left', start=(10, 10), end=(10, 40), steps=20, modifiers=[]):</li>
          <li>    """Send synthetic mouse events to the specified widget (qMRMLSliceWidget or qMRMLThreeDView)</li>
          <li></li>
          <li>    :param button: "Left", "Middle", "Right", or "None"</li>
          <li>     start, end : window coordinates for action</li>
          <li>    :param steps: number of steps to move in, if &lt;2 then mouse jumps to the end position</li>
          <li>    :param modifiers: list containing zero or more of "Shift" or "Control"</li>
          <li>    :raises RuntimeError: in case of failure</li>
          <li></li>
          <li>    .. hint::</li>
          <li></li>
          <li>      For generating test data you can use this snippet of code::</li>
          <li></li>
          <li>        layoutManager = slicer.app.layoutManager()</li>
          <li>        threeDView = layoutManager.threeDWidget(0).threeDView()</li>
          <li>        style = threeDView.interactorStyle()</li>
          <li>        interactor = style.GetInteractor()</li>
          <li></li>
          <li>        def onClick(caller,event):</li>
          <li>            print(interactor.GetEventPosition())</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/2db14ceb03248e0fea6610bcdf059f4f24f6cc5a/Base/Python/slicer/util.py#L3028-L3085" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @pieper (2023-02-28 18:44 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="28096">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Are <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/selftests.html">Self-tests</a> the Slicer recommended way for scripted loadable module python testing?</p>
</blockquote>
</aside>
<p>I would say yes.  We have had good luck with the SelfTests and we are planning to extend it as part of our <a href="https://chanzuckerberg.com/eoss/proposals/3d-slicer-for-latin-america-localization-and-outreach/">CZI project for automating tutorial localization</a>, where we will support running the tests and generating screenshots in different languages.</p>
<p>The SelfTests probably supports most of what the PyTest-qt project provides, but if there are additional features we could look at either adding them or using PyTest-qt with PythonQt, which may not be too hard.</p>
<p>I agree with your statement <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that the QtTesting infrastructure for recording and replaying events is probably more suited to unit testing of widgets; SelfTests have proven easier for complex operations because they are debuggable scripts as opposed to xml files of mouse coordinates and button clicks.</p>

---

## Post #4 by @hannahm (2023-02-28 19:21 UTC)

<p>Hi Steve, thanks for the response. I think I’m still a bit lost. I’m not sure what the difference is between SelfTests and unittests?</p>
<p>Futhermore, I am currently utilizing the ScripedLoadableModuleTest for testing, which (from my understanding) is based on unittest. I have some test cases, but they tend to be very lengthy and dont simulate user interactions very well, which I think is what I am looking for. Are you saying there is a way to do that with SelfTests?</p>

---

## Post #5 by @pieper (2023-02-28 19:38 UTC)

<p>Yes, there’s not really a crisp distinction but we use the term unit test to mean checking one widget or API in isolation as part of the development and build process where the SelfTest refers to scripting the full application, specifically the SelfTest means that it’s part of the installed application, meaning that any user could run a SelfTest, e.g. to test their own hardware or OS without needing any additional tooling.</p>
<p>In Slicer we have <a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp/Testing/Python">some modules</a> that only exist to serve as SelfTests (you can look at these for examples).  These are hidden by default but are turned on in Developer Mode.  But as you’ve seen also any scripted module can include a class that inherits from <code>ScriptedLoadableModuleTest</code> to declare a set of tests that can be at whatever level the developer is able to provide.  Both types are integrated with the testing procedures on the factory builds and contribute results to the dashboard and use the python unittest module internally.  These can also be defined for extensions and results are <a href="https://slicer.cdash.org/index.php?project=SlicerStable">posted to the dashboard</a>.</p>
<p>Anyway, yes, with clickAndDrag and other methods you can script the user interface to simulate interactions with vtk render windows.  For Qt windows we typically call <code>clicked()</code> or other signals directly.</p>

---

## Post #6 by @jamesobutler (2023-02-28 20:10 UTC)

<p><a class="mention" href="/u/hannahm">@hannahm</a> Can you provide an example of a type of interaction that you might want to simulate? How were you thinking of doing this in PyTest-Qt and does the existing <code>slicer.util.clickAndDrag</code> or <code>qpushbutton.click()</code> type methods that exist in Slicer cover the same simulating user behavior?</p>

---

## Post #7 by @hannahm (2023-03-01 12:10 UTC)

<p>I may be mistaken, but when using <code>.clicked()</code> or <code>.click()</code>, it doesn’t act exactly as a person would. For example, when clicking a button or editing a text box, the focus isn’t set on that widget, which may affect the behavior of the rest of the app.</p>
<p>I ran the following test on slicer 5.0.3 this morning</p>
<ol>
<li>pop the console window out of the main window</li>
<li>load in a volume</li>
<li>create a segmentation on any of the slices using draw</li>
<li>confirm that the focus is on that slice viewer using <code>slicer.util.mainWindow().focusWidget()</code>. (I toggled the visibility to fully confirm)</li>
<li>find the AddSegmentationButton (<code>slicer.util.mainWindow().findChild(qt.QPushButton, 'AddSegmentButton')</code>) and use <code>.click()</code> on it.</li>
<li>Confirm that the mainWindows focusWidget is still the slice widget</li>
<li>Repeat steps 5 and 6 but with <code>.clicked()</code> instead of <code>.click()</code>
</li>
<li>Manually click the ‘AddSegmentationButton’</li>
<li>Confirm that the focusWidget of the mainWindow is now that push button</li>
</ol>
<p>Additionally, writing the tests with the current SelfTests framework can be long and tedious to write and review and require developers to know exactly which flags are going to be set with <code>clicked</code>, which makes writing and reviewing less beginner friendly.</p>
<p>Edit:<br>
Additionally x2, as far as I am aware, there is no way to test shortcut keys (ex, Ctrl+O to add new data). PyTest-qt seems to make that possible with the use of <code>qtbot.keyClick()</code></p>
<p>I have also noticed many times while using SelfTests that quite a few tracebacks are logged that wouldnt be there had the test been manually run. I suspect this may be a similar issue and that the UI is not properly updating, although its just a suspicion I have.<br>
For ex. <code>ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1</code></p>

---

## Post #8 by @jamesobutler (2023-03-01 13:55 UTC)

<p>So it appears the use of more Qt specific testing methods such as those in the <a href="https://doc.qt.io/qt-5/qtest.html#functions" rel="noopener nofollow ugc">QTest</a> module is what you are looking for. It appears QTest is used in some Slicer C++ testing, but this module appears to not be included in the PythonQt wrapping? or maybe hidden in a namespace I haven’t found? It would likely only be included in Slicer local builds with Testing built.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/af6d5fbbba8ee9b8c1da061c2c31e185199439f4/Modules/Loadable/Markups/Widgets/Testing/Cxx/qMRMLMarkupsOptionsWidgetsFactoryTest.cxx#L37">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/af6d5fbbba8ee9b8c1da061c2c31e185199439f4/Modules/Loadable/Markups/Widgets/Testing/Cxx/qMRMLMarkupsOptionsWidgetsFactoryTest.cxx#L37" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/af6d5fbbba8ee9b8c1da061c2c31e185199439f4/Modules/Loadable/Markups/Widgets/Testing/Cxx/qMRMLMarkupsOptionsWidgetsFactoryTest.cxx#L37" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/af6d5fbbba8ee9b8c1da061c2c31e185199439f4/Modules/Loadable/Markups/Widgets/Testing/Cxx/qMRMLMarkupsOptionsWidgetsFactoryTest.cxx#L37</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="27" style="counter-reset: li-counter 26 ;">
          <li>
          </li>
<li>// Markups tests includes</li>
          <li>#include "qMRMLMarkupsMalformedWidget.h"</li>
          <li>
          </li>
<li>// CTK includes</li>
          <li>#include "ctkTest.h"</li>
          <li>
          </li>
<li>// Qt includes</li>
          <li>#include &lt;QScopedPointer&gt;</li>
          <li>#include &lt;QSignalSpy&gt;</li>
          <li class="selected">#include &lt;QTest&gt;</li>
          <li>
          </li>
<li>//------------------------------------------------------------------------------</li>
          <li>class qMRMLMarkupsOptionsWidgetsFactoryTester : public QObject</li>
          <li>{</li>
          <li>  Q_OBJECT</li>
          <li>
          </li>
<li>  private slots:</li>
          <li>
          </li>
<li>    // Test registration of a valid additional widget without making use of it</li>
          <li>    void testOptionsWidgetRegistration1();</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @pieper (2023-03-01 18:58 UTC)

<p>There are definitely limitations to our current testing systems and any contributions are welcome!  Anything that helps developers create more useful tests would be great.</p>

---

## Post #10 by @lassoan (2023-03-02 06:14 UTC)

<p>It should not be hard to expose QTest methods in Python:</p>
<ul>
<li>Option A. Add QTest to PythonQt. You can <a href="https://github.com/MeVisLab/pythonqt">ask PythonQt developers</a> if they plan to add wrapping for QTest API this. If they don’t plan to do it then you can do it yourself (as it was done for <a href="https://github.com/commontk/PythonQt/commit/427f871d0156ad218ddb8a9d6c2840f079e4bcb6">adding QtMultimedia</a>).</li>
<li>Option  B. Add a Python-wrapped C++ tester class which calls QTest methods. Similarly how we added the <a href="https://github.com/Slicer/Slicer/blob/main/Base/QTGUI/qSlicerWebWidget.h">qSlicerWebWidget</a> to Slicer instead of adding the QWebengine to PythonQt.</li>
</ul>

---

## Post #11 by @hannahm (2023-03-02 10:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Is there a preferred method? I’m happy to do either</p>

---

## Post #12 by @lassoan (2023-03-02 12:42 UTC)

<p>First try A then if that does not work out then do B.</p>

---

## Post #13 by @pieper (2023-03-02 13:30 UTC)

<p>Improving PythonQt is definitely a good place to start.  Note that the generator <a href="https://github.com/MeVisLab/pythonqt/issues?q=is%3Aissue+is%3Aopen+generator">has some issues</a> that may complicate things.  Adding Slicer-specific subclasses may make sense in any case to handle things like VTK based views or application level flags like test mode or no-main-window mode.  These would be qSlicer subjclasses like we have elsewhere in the code.  So you may end up with A and some of B or just B.</p>

---
