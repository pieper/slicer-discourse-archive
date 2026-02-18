# Customizing Python after extension wizard

**Topic ID**: 26751
**Date**: 2022-12-15
**URL**: https://discourse.slicer.org/t/customizing-python-after-extension-wizard/26751

---

## Post #1 by @Lee_Newberg (2022-12-15 16:39 UTC)

<p>I used the Slicer Extension Wizard to create two modules for my custom Slicer application.  Instead of the <code>inputSelector (qMRMLNodeComboBox)</code>, <code>outputSelector (qMRMLNodeComboBox)</code>, <code>imageThresholdSliderWidget (ctkSliderWidget)</code>, <code>invertOutputCheckBox (QCheckBox)</code>, and <code>invertedOutputSelector (qMRMLNodeComboBox)</code>. which are supplied as examples, I will have <code>DataDirectory (ctkPathLineEdit)</code> and <code>PatientPrefix (QLineEdit)</code>.</p>
<p>I have some pretty good ideas on how to modify the <code>MyNewModule.ui</code> file accordingly.  However, I am having trouble with the <code>MyNewModule.py</code> file.  For example, what should the <code> self.ui.DataDirectory.connect(...)</code> call look like?  (I am not that clear on what this does which likely is a big part of my problem.)  Likewise what should the arguments for <code>self.ui.PatientPrefix.connect(...)</code> be?  Thanks!</p>

---

## Post #2 by @jamesobutler (2022-12-15 17:14 UTC)

<p>Have a read of this old post of mine seen below. I generally prefer the new style Qt signal/slot method of <strong>{object}.{signal_name}.connect({slot_name})</strong></p>
<aside class="quote quote-modified" data-post="2" data-topic="14013">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-use-signals-and-slots-in-slicer-3d/14013/2">How to use signals and slots in Slicer 3d?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A previous post of mine mentioned some about basics of using Qt signals and slots with python. 

Essentially the syntax is something like {object}.{signal_name}.connect({slot_name}). 
So something that is based on QProgressBar will have <a href="https://doc.qt.io/qt-5/qprogressbar.html#signals" rel="noopener nofollow ugc">these signals</a> such as valueChanged. Therefore 
def printMyNewValue(value):
  print("The progress bar value is now: {}".format(value))

import qt
progress_bar = qt.QProgressBar()
progress_bar.setMaximum(10)
progress_bar.valueChanged.connect(printMyNewValue)
progre…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2022-12-15 20:04 UTC)

<aside class="quote no-group" data-username="Lee_Newberg" data-post="1" data-topic="26751">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p>For example, what should the <code> self.ui.DataDirectory.connect(...)</code> call look like?</p>
</blockquote>
</aside>
<p>It creates a connection between a Qt signal and a Python method. When the Qt object emits the signal then it calls the connected Python method. You can find the specification of signals in the header files or the generated documentation. Unfortunately, <a href="https://github.com/commontk/CTK/issues/919">CTK documentation site is down</a>, so you need to look up the signal parameters in source code:</p>
<ul>
<li>google for ctkPathLineEdit, click on the <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkPathLineEdit.h">first hit</a></li>
<li>search for <code>signals</code></li>
<li>probably you are interested in this signal:</li>
</ul>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/1abb81ed5cf0d91827518c55f73047d8fcc870f2/Libs/Widgets/ctkPathLineEdit.h#L250">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/1abb81ed5cf0d91827518c55f73047d8fcc870f2/Libs/Widgets/ctkPathLineEdit.h#L250" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/1abb81ed5cf0d91827518c55f73047d8fcc870f2/Libs/Widgets/ctkPathLineEdit.h#L250" target="_blank" rel="noopener">commontk/CTK/blob/1abb81ed5cf0d91827518c55f73047d8fcc870f2/Libs/Widgets/ctkPathLineEdit.h#L250</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="240" style="counter-reset: li-counter 239 ;">
          <li></li>
          <li>  /// The width returned, in pixels, is the entire length of the current path</li>
          <li>  /// if any. Otherwise, it's enough for 15 to 20 characters.</li>
          <li>  virtual QSize sizeHint()const;</li>
          <li></li>
          <li>Q_SIGNALS:</li>
          <li>  /** the signal is emit when the state of hasValidInput changed</li>
          <li>  */</li>
          <li>  void validInputChanged(bool);</li>
          <li></li>
          <li class="selected">  void currentPathChanged(const QString&amp; path);</li>
          <li></li>
          <li>public Q_SLOTS:</li>
          <li>  void setCurrentPath(const QString&amp; path);</li>
          <li></li>
          <li>  /// Open a QFileDialog to select a file or directory and set current text to it.</li>
          <li>  /// Type of dialog (file open, file save, select directory) is controlled by options flags</li>
          <li>  /// Files (chooses between file and directory dialog) and Writable (chooses between open and save).</li>
          <li>  /// You would probably connect a browse push button like this:</li>
          <li>  /// connect(myPushButton,SIGNAL(clicked()),myPathLineEdit,SLOT(browse()))</li>
          <li>  /// As a conveniency, such button is provided by default via the browseButton</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<ul>
<li>the connection code will look like this:</li>
</ul>
<pre data-code-wrap="python"><code class="lang-python">self.ui.DataDirectory.connect('currentPathChanged(QString)', self.someFunction)
</code></pre>
<p>Since Slicer is open-source and there are about 200 open-source extensions, mostly developed in Python, hosted on github, an alternative approach is to learn from working examples. You can find example for most API calls, for example you can <a href="https://github.com/search?l=Python&amp;q=ctkPathLineEdit+currentPathChanged&amp;type=Code">search for <code>ctkPathLineEdit currentPathChanged</code> in Python code in entire github</a>. One of the hits show how to create the connection:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerImageStacks/blob/76e40cf61a68cdab5cc7802e61cc3e0ee9b5acca/ImageStacks/ImageStacks.py#L170">
  <header class="source">

      <a href="https://github.com/pieper/SlicerImageStacks/blob/76e40cf61a68cdab5cc7802e61cc3e0ee9b5acca/ImageStacks/ImageStacks.py#L170" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerImageStacks/blob/76e40cf61a68cdab5cc7802e61cc3e0ee9b5acca/ImageStacks/ImageStacks.py#L170" target="_blank" rel="noopener">pieper/SlicerImageStacks/blob/76e40cf61a68cdab5cc7802e61cc3e0ee9b5acca/ImageStacks/ImageStacks.py#L170</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="160" style="counter-reset: li-counter 159 ;">
          <li>addByNameFormLayout.addRow("Index range", self.indexRange)</li>
          <li></li>
          <li>self.generateNamesButton = qt.QPushButton("Apply")</li>
          <li>self.generateNamesButton.toolTip = "Run the algorithm."</li>
          <li>self.generateNamesButton.enabled = False</li>
          <li>addByNameFormLayout.addRow(self.generateNamesButton)</li>
          <li></li>
          <li># connections</li>
          <li>self.addByBrowsingButton.connect('clicked()', self.addByBrowsing)</li>
          <li>self.clearFilesButton.connect('clicked()', self.onClearFiles)</li>
          <li class="selected">self.archetypePathEdit.connect('currentPathChanged(QString)', self.validateInput)</li>
          <li>self.archetypePathEdit.connect('currentPathChanged(QString)', self.updateGUIFromArchetype)</li>
          <li>self.archetypeFormat.connect('textChanged(QString)', self.validateInput)</li>
          <li>self.generateNamesButton.connect('clicked()', self.onGenerateNames)</li>
          <li># self.outputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.validateInput) # TODO - this is missing</li>
          <li>self.loadButton.connect('clicked()', self.onLoadButton)</li>
          <li></li>
          <li># refill last selection</li>
          <li>self.archetypePathEdit.currentPath = slicer.util.settingsValue("ImageStacks/lastArchetypePath", "")</li>
          <li></li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2022-12-15 20:32 UTC)

<p>I’ve added the information from <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and my post to the Python FAQ:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6737">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6737" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6737" target="_blank" rel="noopener">DOC: Add Qt connection documentation to Python FAQ</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Slicer:lassoan-patch-doc-qt-connection</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-15" data-time="20:30:21" data-timezone="UTC">08:30PM - 15 Dec 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 21 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6737/files" target="_blank" rel="noopener">
            <span class="added">+21</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This should help with questions like this: https://discourse.slicer.org/t/custom<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6737" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">izing-python-after-extension-wizard/26751/3</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please have a look and suggest improvements that would help other developers.</p>

---
