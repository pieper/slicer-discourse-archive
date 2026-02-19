---
topic_id: 10817
title: "Hide Radio Button Or Collapsible Item Slice"
date: 2020-03-24
url: https://discourse.slicer.org/t/10817
---

# Hide radio button or collapsible item slice

**Topic ID**: 10817
**Date**: 2020-03-24
**URL**: https://discourse.slicer.org/t/hide-radio-button-or-collapsible-item-slice/10817

---

## Post #1 by @Tokai (2020-03-24 15:58 UTC)

<p>Hi ,<br>
I want to hide some option for use, in slicer shown in below.  This is from Landmark registration module.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d3e5e38ab8d2bb29dd59dfcb946b670f7b88ce.png" alt="Capture" data-base62-sha1="inF6xUpsCmAkjy6HJcZKHjLY7hA" width="505" height="251"></p>
<p>Technically it should be possible to hide or show any part of the module. I have seen an example given in documentation to control widget view like this:</p>
<pre><code>sliceController = slicer.app.layoutManager().sliceWidget("Red").sliceController()
# hide what is not needed
sliceController.pinButton().hide()
#sliceController.viewLabel().hide()
sliceController.fitToWindowToolButton().hide()
sliceController.sliceOffsetSlider().hide()
</code></pre>
<p>However, if I do not know the name, such as ‘Red’ in the given example, I can not hide.<br>
So, my question is how can I get the names of radio buttons or collapsible items and sub-items(shown in picture)  so that I can hide them to control the view?</p>

---

## Post #2 by @pieper (2020-03-24 19:07 UTC)

<p>It’s not considered good practice to rely on “reaching inside” other modules to turn on and off parts of the display, because this makes your code brittle code (it can break if the other module’s GUI changes even a little).  Better practice would be to study the code you are using and generate pull requests to modularize the interface to make it more reusable (work with the developer of the module to find a good way to do this - it will probably make the original code cleaner too).</p>
<p>That said, for debugging and testing we do have utilities to find widgets within the application.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L204-L267" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L204-L267" target="_blank">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L204-L267</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="204" style="counter-reset: li-counter 203 ;">
<li>def findChildren(widget=None, name="", text="", title="", className=""):</li>
<li>  """ Return a list of child widgets that meet all the given criteria.</li>
<li>  If no criteria are provided, the function will return all widgets descendants.</li>
<li>  If no widget is provided, slicer.util.mainWindow() is used.</li>
<li>  :param widget: parent widget where the widgets will be searched</li>
<li>  :param name: name attribute of the widget</li>
<li>  :param text: text attribute of the widget</li>
<li>  :param title: title attribute of the widget</li>
<li>  :param className: className() attribute of the widget</li>
<li>  :return: list with all the widgets that meet all the given criteria.</li>
<li>  """</li>
<li>  # TODO: figure out why the native QWidget.findChildren method does not seem to work from PythonQt</li>
<li>  import slicer, fnmatch</li>
<li>  if not widget:</li>
<li>    widget = mainWindow()</li>
<li>  if not widget:</li>
<li>    return []</li>
<li>  children = []</li>
<li>  parents = [widget]</li>
<li>  kwargs = {'name': name, 'text': text, 'title': title, 'className': className}</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L204-L267" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Tokai (2020-03-24 19:49 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
Thanks, I already tried with that .<br>
The ‘findChildren’ take atleast two arguments. So, I tried like below code and it returns an empty list:</p>
<pre><code>w = slicer.modules.LandmarkRegistrationWidget
slicer.util.findChildren(w,'LandmarkRegistration')
[]
</code></pre>
<p>So, the list is empty. Do you have any suggestion why is happening that?</p>

---

## Post #4 by @lassoan (2020-03-24 20:00 UTC)

<p>We also have a number of high-level <code>set...Visible()</code> functions in slicer.util for showing/hiding various parts of the application GUI. We keep maintaining these functions, so they will work even if underlying widgets slightly change.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L2144-L2230" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L2144-L2230" target="_blank">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L2144-L2230</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="2144" style="counter-reset: li-counter 2143 ;">
<li>def setToolbarsVisible(visible, ignore=None):</li>
<li>  """Show/hide all existing toolbars, except those listed in</li>
<li>  ignore list.</li>
<li>  """</li>
<li>
</li>
<li>  for toolbar in mainWindow().findChildren('QToolBar'):</li>
<li>    if ignore is not None and toolbar in ignore:</li>
<li>      continue</li>
<li>    toolbar.setVisible(visible)</li>
<li>
</li>
<li>  # Prevent sequence browser toolbar showing up automatically</li>
<li>  # when a sequence is loaded.</li>
<li>  # (put in try block because Sequence Browser module is not always installed)</li>
<li>  try:</li>
<li>    import slicer</li>
<li>    slicer.modules.sequencebrowser.autoShowToolBar = visible</li>
<li>  except:</li>
<li>    # Sequences module is not installed</li>
<li>    pass</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L2144-L2230" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @jcfr (2020-03-24 20:14 UTC)

<aside class="quote no-group" data-username="Tokai" data-post="3" data-topic="10817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tokai/48/4851_2.png" class="avatar"> Tokai:</div>
<blockquote>
<p>Do you have any suggestion why is happening that?</p>
</blockquote>
</aside>
<p>To answer that specific question, you would have to do this:</p>
<pre><code class="lang-auto">w = slicer.modules.landmarkregistration.widgetRepresentation()
slicer.util.findChildren(w)

slicer.util.findChildren(w, name='LandmarkRegistration')  # Always specify keyword like 'name' 
</code></pre>
<p>That said, note that the <code>LandmarkRegistration</code> module is not available in the latest version of Slicer.</p>

---

## Post #6 by @lassoan (2020-03-24 20:18 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="10817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>the <code>LandmarkRegistration</code> module is not available in the latest version of Slicer.</p>
</blockquote>
</aside>
<p>I’ve added an issue to fix it for latest Slicer version:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4764">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4764" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4764" target="_blank" rel="noopener">Make Landmark registration module available</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-24" data-time="20:17:48" data-timezone="UTC">08:17PM - 24 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-05-28" data-time="13:47:21" data-timezone="UTC">01:47PM - 28 May 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: Medium
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Landmark Registration module needs to be updated to work with redesigned markups<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> module. Currently it is excluded from the build.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Tokai (2020-03-24 20:23 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a> ,<br>
I tried your code.<br>
So the the line “slicer.util.findChildren(w)” returns a big list.</p>
<p><code>&gt; [qSlicerScriptedLoadableModuleWidget(0x1afaa382430, name="LandmarkRegistrationModuleWidget") , QWidget(0x1afabfb0390) , ctkCollapsibleButton(0x1afb1e6a5a0) , ctkCollapsibleButton(0x1afc6173fa0) , QRadioButton(0x1afc6173420) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC61736E0), QRadioButton(0x1afc6173620) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC6173DA0), QRadioButton(0x1afc61732a0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC6173FE0), QLabel(0x1afc6173d60) , QFormLayout (QFormLayout at: 0x000001AFB21C3DC0), QVBoxLayout (QVBoxLayout at: 0x000001AFB21C4390), QFrame(0x1afc6173c20, name="EditOptionsFrame") , QVBoxLayout (QVBoxLayout at: 0x000001AFB21C3D60), QGroupBox(0x1afb1e6a6e0) , QRadioButton(0x1afb1e6a8e0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6C0A0), QRadioButton(0x1afb1e6a720) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6AA20), QFormLayout (QFormLayout at: 0x000001AFB1EDE110), QFormLayout (QFormLayout at: 0x000001AFB1EDDDB0), ctkCollapsibleButton(0x1afb1e6b020) , ctkCollapsibleButton(0x1afc6173320) , QRadioButton(0x1afc61735a0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC6173A20), QRadioButton(0x1afc61731a0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC6173F20), QLabel(0x1afc6173aa0) , QRadioButton(0x1afc6174060) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC6173960), QRadioButton(0x1afc6173760) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC61734A0), QLabel(0x1afc6173ce0) , QFormLayout (QFormLayout at: 0x000001AFB21C26B0), QVBoxLayout (QVBoxLayout at: 0x000001AFB21C3370), QVBoxLayout (QVBoxLayout at: 0x000001AFB21C2230), QFrame(0x1afc6173460, name="EditOptionsFrame") , QVBoxLayout (QVBoxLayout at: 0x000001AFB21C0AF0), QGroupBox(0x1afb1e6a660) , QRadioButton(0x1afb1e6a3e0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6AEE0), QRadioButton(0x1afb1e6a920) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6A420), QFormLayout (QFormLayout at: 0x000001AFB1EDD600), QPushButton(0x1afb1e6afe0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6A3A0), QFormLayout (QFormLayout at: 0x000001AFB1EDD0F0), ctkCollapsibleButton(0x1afabfb0810) , QWidget(0x1afb1e6ae20) , QWidget(0x1afb1e6aea0) , QGroupBox(0x1afc6c2f6b0) , QPushButton(0x1afc6c310b0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC6C2BA30), QPushButton(0x1afc6c2fb70) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFC6C310F0), QFormLayout (QFormLayout at: 0x000001AFC59170D0), QHBoxLayout (QHBoxLayout at: 0x000001AFC5917A60), QVBoxLayout (QVBoxLayout at: 0x000001AFB1EDD090), QFormLayout (QFormLayout at: 0x000001AFB1EDD3F0), QWidget(0x1afb1e693e0) , QWidget(0x1afb1e699a0) , QGroupBox(0x1afb1e69560) , QWidget(0x1afb1e6a360) , QPushButton(0x1afb1e6af20) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6ACA0), QPushButton(0x1afb1e6a9a0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6A1E0), QPushButton(0x1afb1e6ab20) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6A1A0), QHBoxLayout (QHBoxLayout at: 0x000001AFB1EDC790), QLabel(0x1afb1e6a960) , QWidget(0x1afb1e696e0) , QWidget(0x1afb1e6ae60) , QCheckBox(0x1afb1e6aaa0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6B120), QCheckBox(0x1afb1e6af60) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6B0E0), QVBoxLayout (QVBoxLayout at: 0x000001AFB1EDC430), ctkSliderWidget(0x1afb1e69720, name="ctkSliderWidget") , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6AD60), ctkDoubleSpinBox(0x1afb1e698a0, name="SpinBox") , QHBoxLayout (QHBoxLayout at: 0x000001AFB1EDB410), ctkQDoubleSpinBox(0x1afb1dc48e0) , QLineEdit(0x1afb1e6aba0, name="qt_spinbox_lineedit") , QWidgetLineControl (QWidgetLineControl at: 0x000001AFAF476580), QValidator (QValidator at: 0x000001AFB1EDB500), ctkDoubleSlider(0x1afb1e697a0, name="Slider") , QHBoxLayout (QHBoxLayout at: 0x000001AFB1EDBB30), QSlider(0x1afb1e697e0) , QHBoxLayout (QHBoxLayout at: 0x000001AFB1EDB710), QHBoxLayout (QHBoxLayout at: 0x000001AFB1EDBCE0), QLabel(0x1afb1e6ade0) , QWidget(0x1afb1e694e0) , QCheckBox(0x1afb1e69f60) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E69160), QCheckBox(0x1afb1e69320) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6A0E0), QCheckBox(0x1afb1e69620) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E696A0), QCheckBox(0x1afb1e69e20) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E69520), QHBoxLayout (QHBoxLayout at: 0x000001AFB1EDA900), QLabel(0x1afb1e69960) , QWidget(0x1afb1e69c60) , QPushButton(0x1afb1e692e0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6A0A0), QPushButton(0x1afb1e6a060) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E69CA0), QPushButton(0x1afb1e694a0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E69A60), QPushButton(0x1afb1e69420) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E69220), QHBoxLayout (QHBoxLayout at: 0x000001AFB1EDA540), QLabel(0x1afb1e69260) , QFormLayout (QFormLayout at: 0x000001AFB1EDAA80), QVBoxLayout (QVBoxLayout at: 0x000001AFB1EDA720), QFormLayout (QFormLayout at: 0x000001AFB1EDA150), qMRMLNodeComboBox(0x1afb1e627e0) , qMRMLSortFilterProxyModel (qMRMLSortFilterProxyModel at: 0x000001AFB1E63A60), qMRMLNodeFactory (qMRMLNodeFactory at: 0x000001AFB1E45A20), ctkComboBox(0x1afb1e63a20) , QComboBoxPrivateContainer(0x1afaa382f70) , QComboBoxListView(0x1afb1e632e0) , QItemSelectionModel (QItemSelectionModel at: 0x000001AFB1E45A80), QWidget(0x1afb1dbed00, name="qt_scrollarea_vcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1ED5860), QScrollBar(0x1afb1e63e60) , QWidget(0x1afb1dbf480, name="qt_scrollarea_hcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1ED5590), QScrollBar(0x1afb1e63520) , QWidget(0x1afb1e63fe0, name="qt_scrollarea_viewport") , QBoxLayout (QBoxLayout at: 0x000001AFB1ED60A0), QHBoxLayout (QHBoxLayout at: 0x000001AFB1ED6460), qMRMLSceneModel (qMRMLSceneModel at: 0x000001AFB1E62A60), QLabel(0x1afb1e69aa0) , qMRMLNodeComboBox(0x1afb1e5cda0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6B6E0), qMRMLSortFilterProxyModel (qMRMLSortFilterProxyModel at: 0x000001AFB1E5DC60), qMRMLNodeFactory (qMRMLNodeFactory at: 0x000001AFB1E44360), ctkComboBox(0x1afb1e5cde0) , QComboBoxPrivateContainer(0x1afaa382d90) , QComboBoxListView(0x1afb1e5cba0) , QItemSelectionModel (QItemSelectionModel at: 0x000001AFB1E43DA0), QWidget(0x1afb1dbb6f0, name="qt_scrollarea_vcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1DA1780), QScrollBar(0x1afb1e5dee0) , QWidget(0x1afb1dbabb0, name="qt_scrollarea_hcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1DA09A0), QScrollBar(0x1afb1e5cca0) , QWidget(0x1afb1e5cc20, name="qt_scrollarea_viewport") , QBoxLayout (QBoxLayout at: 0x000001AFB1DA2080), QHBoxLayout (QHBoxLayout at: 0x000001AFB1DA2890), qMRMLSceneModel (qMRMLSceneModel at: 0x000001AFB1E5C2A0), QLabel(0x1afb1e621e0) , qMRMLNodeComboBox(0x1afb1e570e0) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6C060), qMRMLSortFilterProxyModel (qMRMLSortFilterProxyModel at: 0x000001AFB1E56BE0), qMRMLNodeFactory (qMRMLNodeFactory at: 0x000001AFB1E41F60), ctkComboBox(0x1afb1e56220) , QComboBoxPrivateContainer(0x1afaa3827f0) , QComboBoxListView(0x1afb1e56560) , QItemSelectionModel (QItemSelectionModel at: 0x000001AFB1E421E0), QWidget(0x1afb1db7ff0, name="qt_scrollarea_vcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1DAB2C0), QScrollBar(0x1afb1e56620) , QWidget(0x1afb1db7a50, name="qt_scrollarea_hcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1DABBC0), QScrollBar(0x1afb1e569a0) , QWidget(0x1afb1e56960, name="qt_scrollarea_viewport") , QBoxLayout (QBoxLayout at: 0x000001AFB1DAB8C0), QHBoxLayout (QHBoxLayout at: 0x000001AFB1DAB2F0), qMRMLSceneModel (qMRMLSceneModel at: 0x000001AFB1E56D60), QLabel(0x1afb1e5ce60) , qMRMLNodeComboBox(0x1afabfb0b50) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFB1E6BBE0), qMRMLSortFilterProxyModel (qMRMLSortFilterProxyModel at: 0x000001AFA98FFB60), qMRMLNodeFactory (qMRMLNodeFactory at: 0x000001AFB1E40340), ctkComboBox(0x1afabfb4c10) , QComboBoxPrivateContainer(0x1afaa381210) , QComboBoxListView(0x1afabfbb6d0) , QItemSelectionModel (QItemSelectionModel at: 0x000001AFB1E3FF80), QWidget(0x1afb1db2230, name="qt_scrollarea_vcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1DA6340), QScrollBar(0x1afabfa0d10) , QWidget(0x1afb1db2190, name="qt_scrollarea_hcontainer") , QBoxLayout (QBoxLayout at: 0x000001AFB1DA6880), QScrollBar(0x1afabfbb950) , QWidget(0x1afabfbc050, name="qt_scrollarea_viewport") , QBoxLayout (QBoxLayout at: 0x000001AFB1DA65B0), QHBoxLayout (QHBoxLayout at: 0x000001AFB1DA7420), qMRMLSceneModel (qMRMLSceneModel at: 0x000001AFABFB0C50), QLabel(0x1afb1e56260) , QFormLayout (QFormLayout at: 0x000001AFB1DA66A0), QVBoxLayout (QVBoxLayout at: 0x000001AFB1DA5B60), QPushButton(0x1afabfaa110) , PythonQtSignalReceiverBase (PythonQtSignalReceiverBase at: 0x000001AFABFB1150), QVBoxLayout (QVBoxLayout at: 0x000001AFB1DA45A0)]</code></p>
<p>And this one " slicer.util.findChildren(w, name=‘LandmarkRegistration’)   returns empty list []</p>

---

## Post #8 by @jcfr (2020-03-24 20:40 UTC)

<aside class="quote no-group" data-username="Tokai" data-post="7" data-topic="10817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tokai/48/4851_2.png" class="avatar"> Tokai:</div>
<blockquote>
<p>And this one " slicer.util.findChildren(w, name=‘LandmarkRegistration’) returns empty list <span class="chcklst-box fa fa-square-o fa-fw"></span></p>
</blockquote>
</aside>
<p>You need to specify the name of an existing widget.</p>
<p>Looking at the source <a href="https://github.com/Slicer/LandmarkRegistration/blob/master/LandmarkRegistration.py">LandmarkRegistration.py</a>, not all widget are associated with a name.</p>
<p>First find in the source what you would like to hide and if it has no name, you could call <code>findChildren</code> specifying a class name and then retrieving the widget by index.</p>
<p>Just be aware that this approach is very brittle and not sustainable.</p>

---

## Post #9 by @Tokai (2020-03-24 21:01 UTC)

<blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
Looking at the source LandmarkRegistration.py, not all widget are associated with a name.</p>
<p>First find in the source what you would like to hide and if it has no name, you could call findChildren specifying a class name and then retrieving the widget by index.</p>
</blockquote>
<p>Can you give me a dummy example (fairly new at this) ? Did not understand it.<br>
In the <a href="https://github.com/Slicer/LandmarkRegistration/blob/master/LandmarkRegistration.py" rel="noopener nofollow ugc">LandmarkRegistration</a> the class name is also ‘LandmarkRegistration’. And it also returns empty list. And I am trying to hide LocalRefinement, Data probe etc. collapsible frames. <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @jcfr (2020-03-24 21:40 UTC)

<blockquote>
<p>widgets are associated with a name</p>
</blockquote>
<p>Qt provides a function to associate an <code>objectName</code> with any <code>QObject</code> or <code>QWidget</code> instance. See <a href="https://doc.qt.io/qt-5/qobject.html#objectName-prop" class="inline-onebox">QObject Class | Qt Core 5.15.16</a></p>
<p>This means for a given hierarchy of <code>QWidget</code>, it is possible to easily lookup widget given its name.</p>
<p>To illustrate, I will take the Endoscopy module as an example. Looking at the source, we can see that <code>objectName</code> is set:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/67456afd687fea4d3fece919ed0c7e2406875e9c/Modules/Scripted/Endoscopy/Endoscopy.py#L87-L93">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/67456afd687fea4d3fece919ed0c7e2406875e9c/Modules/Scripted/Endoscopy/Endoscopy.py#L87-L93" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/67456afd687fea4d3fece919ed0c7e2406875e9c/Modules/Scripted/Endoscopy/Endoscopy.py#L87-L93" target="_blank" rel="noopener">Slicer/Slicer/blob/67456afd687fea4d3fece919ed0c7e2406875e9c/Modules/Scripted/Endoscopy/Endoscopy.py#L87-L93</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="87" style="counter-reset: li-counter 86 ;">
          <li># Input fiducials node selector</li>
          <li>inputFiducialsNodeSelector = slicer.qMRMLNodeComboBox()</li>
          <li>inputFiducialsNodeSelector.objectName = 'inputFiducialsNodeSelector'</li>
          <li>inputFiducialsNodeSelector.toolTip = "Select a fiducial list to define control points for the path."</li>
          <li>inputFiducialsNodeSelector.nodeTypes = ['vtkMRMLMarkupsFiducialNode', 'vtkMRMLMarkupsCurveNode',</li>
          <li>  'vtkMRMLAnnotationHierarchyNode', 'vtkMRMLFiducialListNode']</li>
          <li>inputFiducialsNodeSelector.noneEnabled = False</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Allowing us to easily retrieve the corresponding widget instance:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; slicer.util.selectModule("Endoscopy")
&gt;&gt;&gt; w = slicer.modules.endoscopy.widgetRepresentation()
&gt;&gt;&gt; slicer.util.findChildren(w, name="inputFiducialsNodeSelector")
[qMRMLNodeComboBox(0x8a8c9f0, name="inputFiducialsNodeSelector") ]
</code></pre>
<p>Now, we could also achieve this without relying on the <code>objectName</code> using something like this:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; slicer.util.findChildren(w, className="qMRMLNodeComboBox")[0]
qMRMLNodeComboBox(0x8a8c9f0, name="inputFiducialsNodeSelector") 
</code></pre>
<blockquote>
<p>hide […] Data probe collapsible frames</p>
</blockquote>
<p>For the dataprobe, this could be achieved simply by doing this:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.setDataProbeVisible(False)
</code></pre>

---

## Post #11 by @Tokai (2020-03-25 08:23 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>The example you gave</p>
<p>`slicer.util.findChildren(w, name=“inputFiducialsNodeSelector”)</p>
<p>Yes, this works for endoscopy module. However, this is inside the ‘path’ collapsible frame which is not a  ‘qMRML…type’ but ctk.ctkCollapsibleButton. So my idea is if I can hide the frame, everything inside should be hidden anyway. However when I try to access like the Fiducial example you gave in landmarkRegistration, it returns empty list.</p>
<pre><code>slicer.util.findChildren(w, className="Local Refinement")
[]</code></pre>

---

## Post #12 by @pieper (2020-03-25 13:28 UTC)

<p>You can use any of the keyword argument search parameters.  Sometimes text is the most useful (but also the most potentially brittle for all the reasons we’ve stated).</p>
<p>In this case here’s a query that works:</p>
<pre><code class="lang-auto">slicer.util.findChildren(text="Local Refinement")[0].hide()
</code></pre>

---

## Post #13 by @Tokai (2020-03-25 13:39 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a><br>
You are life saver! I was doing this and that last 24 hours :))<br>
Thanks a lot .</p>

---
