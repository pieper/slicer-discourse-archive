---
topic_id: 39858
title: "Custom File Reader Without Add Data Into Scene Dialog"
date: 2024-10-25
url: https://discourse.slicer.org/t/39858
---

# Custom file reader without 'Add data into scene' dialog

**Topic ID**: 39858
**Date**: 2024-10-25
**URL**: https://discourse.slicer.org/t/custom-file-reader-without-add-data-into-scene-dialog/39858

---

## Post #1 by @koeglfryderyk (2024-10-25 07:38 UTC)

<p>I’m writing a Python Scripted Module and I want to create a custom data loading functionality.</p>
<p>What I want to achieve is to drag a folder into the scene and for Slicer to load the content automatically, according to some logic that I would specify. The folder has some predefined structure of subfolders and files, which is always the same.</p>
<p>I want to do this to save time, so I don’t have to select descriptions in the  ‘Add data into scene’ dialog and then click load.</p>
<p>I tried to use a custom file reader and writer, as shown <a href="https://github.com/Slicer/Slicer/blob/8381ef3e6d73afc9f15ac0db5ddb7de753c90641/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py" rel="noopener nofollow ugc">here</a>, but this didn’t help me. As far as I understood, those two classes only allow you to write custom code to load/save a specific file type - but I want to automatically load files that are dropped into the scene, without opening the dialog.</p>
<p>The holding of ‘shift’ while selecting the description as described <a href="https://discourse.slicer.org/t/applying-the-same-data-description-with-one-click-when-loading-multiple-files/30289">here</a>, doesn’t help me as I have three file types to load - volumes, segmentations and displacement fields.</p>
<p>Is this possible?</p>

---

## Post #2 by @koeglfryderyk (2024-10-25 08:09 UTC)

<p>I figured it out - I created a custom drop widget - when I drop a folder in a specified area, my custom code gets triggered</p>
<p>here’s a simplified extension that does that</p>
<pre data-code-wrap="python"><code class="lang-python">import os
import vtk
import qt
import ctk
import slicer
from slicer.ScriptedLoadableModule import *
import logging


class baselineLoader(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Custom Data Loader"
        self.parent.categories = ["Utilities"]
        self.parent.dependencies = []
        self.parent.contributors = ["Your Name"]
        self.parent.helpText = """
            Module for automatic loading of data from dropped folders.
            """
        self.parent.acknowledgementText = """
            Developed for custom data loading workflow.
            """


class DropWidget(qt.QFrame):
    def __init__(self, parent=None):
        # Get the widget's layout widget as the parent
        if parent is not None:
            parent_widget = parent.parent
        else:
            parent_widget = None
        qt.QFrame.__init__(self, parent_widget)

        self.setAcceptDrops(True)
        self.setStyleSheet(
            "QFrame { border: 2px dashed #999; border-radius: 5px; }")
        self.setMinimumHeight(100)

        # Create layout
        layout = qt.QVBoxLayout(self)
        label = qt.QLabel("Drop folder here")
        label.setAlignment(qt.Qt.AlignCenter)
        layout.addWidget(label)

        # Store reference to parent widget for accessing configuration
        self.moduleWidget = parent

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            self.setStyleSheet(
                "QFrame { border: 2px dashed #44A; border-radius: 5px; background: #EEF; }")
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.setStyleSheet(
            "QFrame { border: 2px dashed #999; border-radius: 5px; }")

    def dropEvent(self, event):
        self.setStyleSheet(
            "QFrame { border: 2px dashed #999; border-radius: 5px; }")
        paths = []
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isdir(path):
                paths.append(path)

        if paths and self.moduleWidget:
            # todo LOAD HERE
            pass


class baselineLoaderWidget(ScriptedLoadableModuleWidget):
    def __init__(self, parent=None):
        ScriptedLoadableModuleWidget.__init__(self, parent)
        self.logic = baselineLoaderLogic()

    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)

        # Add drop zone directly to main layout
        self.dropWidget = DropWidget(self)
        self.layout.addWidget(self.dropWidget)
        self.layout.addStretch(1)
</code></pre>

---

## Post #3 by @bserrano (2024-10-28 08:00 UTC)

<p>Hi,</p>
<p>I am also very interested in a custom load function. I tried running your code by saving it as a .py file and creating a module from it so I could import it, but I didn’t succeed. How can I use your code?</p>
<p>Many thanks.</p>

---

## Post #4 by @koeglfryderyk (2024-10-28 12:45 UTC)

<p>you still have to create an extension first, then you can use the code</p>
<ol>
<li>go to extension wizard</li>
<li>click on ‘Create Extension’ and follow the GUI</li>
<li>click on ‘Add Module to Extension’ - the name of the module has to match the name in the code, so in this case ‘baselineLoader’</li>
<li>now replace the code from &lt;module_name&gt;.py with the code from my previous answer</li>
</ol>

---

## Post #5 by @bserrano (2024-10-28 13:41 UTC)

<p>Many thanks, it works but if I restart slicer and then try to open the module again, then<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b49a95ad4cb767a6d5de9285c463d9ed7e2d4a41_2_690x50.png" alt="imagen" data-base62-sha1="pLH8JjxREiMQ3hCXYaMDtq1IpMd" width="690" height="50" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b49a95ad4cb767a6d5de9285c463d9ed7e2d4a41_2_690x50.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b49a95ad4cb767a6d5de9285c463d9ed7e2d4a41_2_1035x75.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b49a95ad4cb767a6d5de9285c463d9ed7e2d4a41.png 2x" data-dominant-color="100420"><br>
Do you know why this happens?</p>

---

## Post #6 by @koeglfryderyk (2024-10-28 16:26 UTC)

<p>I made an error. you have to delete this line</p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="2" data-topic="39858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<pre><code class="lang-auto">        self.logic = baselineLoaderLogic()
</code></pre>
</blockquote>
</aside>

---

## Post #7 by @lassoan (2024-10-29 16:25 UTC)

<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> Adding a dropwidget is a neat idea if you want to directly load and select a file in a particular widget. I’m just wondering what was the issue with the Add Data dialog. Was the problem that you had to confirm loading in the add data window (single mouse click or hitting Enter key)? Or the problem was that you had to change what description was selected by default?</p>
<p>In recent Slicer versions, you can make sure that always the correct description is selected by adding a custom file reader that provides high confidence value.</p>

---

## Post #8 by @cpinter (2024-10-29 20:21 UTC)

<p>I think it’s about hanging protocols and simplification of data organized in a standard way.</p>
<p>Btw I’ll need to override drag&amp;drop very soon on the main window in one of the applications as well, in this particular case because the app loads a huge stack of TIFFs and the default loader does not support progress reporting, which is a must (may be 200+GB).</p>

---

## Post #9 by @muratmaga (2024-10-30 04:35 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="8" data-topic="39858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Btw I’ll need to override drag&amp;drop very soon on the main window in one of the applications as well, in this particular case because the app loads a huge stack of TIFFs and the default loader does not support progress reporting, which is a must (may be 200+GB).</p>
</blockquote>
</aside>
<p>If you are working with TIFF, and particularly that large, be aware of this potential problem, which hopefully will be fixed soon.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7994">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7994" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7994" target="_blank" rel="noopener nofollow ugc">Tiff errors slowing down the Slicer performance. </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-10-14" data-time="17:07:01" data-timezone="UTC">05:07PM - 14 Oct 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary
Please see for detail discussion and solution:

https://github.com<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">/SlicerMorph/SlicerMorph/issues/320#issuecomment-2411678264

This issue is added to make sure that ITK changes to fix the slowness issue are incorporated before the 5.8 stable is released.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @koeglfryderyk (2024-10-30 07:57 UTC)

<p>it was actually both the description and the click/enter. I just needed a fast way to load data organized in a standard way.</p>
<p>and to return a confidence value, do I just have to add this function to my reader?</p>
<pre><code class="lang-auto">def canLoadFileConfidence(self, filePath)
</code></pre>
<p>Could I just return ‘1’? the few example that I saw always returned something smaller than 1</p>

---

## Post #11 by @lassoan (2024-10-30 21:06 UTC)

<p>See a complete example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/6b9765ac0e4094b033a899573ad9647af456d13c/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py#L45-L60">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/6b9765ac0e4094b033a899573ad9647af456d13c/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py#L45-L60" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6b9765ac0e4094b033a899573ad9647af456d13c/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py#L45-L60" target="_blank" rel="noopener">Slicer/Slicer/blob/6b9765ac0e4094b033a899573ad9647af456d13c/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py#L45-L60</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="45" style="counter-reset: li-counter 44 ;">
          <li>def canLoadFileConfidence(self, filePath):</li>
          <li>    # Only enable this reader in testing mode</li>
          <li>    if not slicer.app.testingEnabled():</li>
          <li>        return 0.0</li>
          <li></li>
          <li>    # Check first if loadable based on file extension</li>
          <li>    if not self.parent.supportedNameFilters(filePath):</li>
          <li>        return 0.0</li>
          <li></li>
          <li>    firstLine = ""</li>
          <li>    with open(filePath) as f:</li>
          <li>        firstLine = f.readline()</li>
          <li>    fileLooksValid = "magic" in firstLine</li>
          <li>    # Default confidence is 0.5 + 0.01 * fileExtensionLength = 0.53,</li>
          <li>    # we return a higher value if we recognize this file</li>
          <li>    return 0.8 if fileLooksValid else 0.3</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Confidence value can be any positive number. Default readers use values around 0.5. Slicer core and uses confidence values &lt;= 1 and I would recommend this for all publicly distributed extensions (so that custom applications can be sure that when they use a &gt; 1 value then that is higher than all other values).</p>

---
