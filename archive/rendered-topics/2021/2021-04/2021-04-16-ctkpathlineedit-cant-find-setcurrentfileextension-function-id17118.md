---
topic_id: 17118
title: "Ctkpathlineedit Cant Find Setcurrentfileextension Function"
date: 2021-04-16
url: https://discourse.slicer.org/t/17118
---

# ctkPathLineEdit can't find setCurrentFileExtension function?

**Topic ID**: 17118
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/ctkpathlineedit-cant-find-setcurrentfileextension-function/17118

---

## Post #1 by @Teresa_Gadda (2021-04-16 02:15 UTC)

<p>I’m trying to set up my own slicer extension and one of the things I want to do is to be able to load a file but restrict the allowed extensions (or at least make it easier to select the correct one).  Other posts here helpfully pointed me to the ctkPathLineEdit() widget and I’m trying to implement the extension limitations but running into a strange problem.  I believe the function I want is “setCurrentFileExtension” (shown <a href="http://www.commontk.org/docs/html/classctkPathLineEdit.html#a01d413dfb401752b2022821c3c551f61" rel="noopener nofollow ugc">here</a> ) however the slicer python interactor (and my python extension) do not acknowledge this function.  See this minimal example from the python interactor:</p>
<p>&gt;&gt;&gt; c = ctk.ctkPathLineEdit()<br>
&gt;&gt;&gt; c.setCurrentFileExtension(“jpg”)<br>
Traceback (most recent call last):<br>
File “&lt;console&gt;”, line 1, in &lt;module&gt;<br>
AttributeError: ctkPathLineEdit has no attribute named ‘setCurrentFileExtension’</p>
<p>I get the same error when running from my (otherwise functioning) custom extension.  Any ideas what might be going on here?  Or have recommendations for a workaround or alternative?</p>

---

## Post #2 by @pieper (2021-04-16 13:57 UTC)

<p>Yes, it looks like that method is not exposed for python.  That class has a lot of methods that are C++ only, meaning it probably hasn’t been used much from python an nobody went through to make the public api available.</p>
<p>The declaration is here and probably it’s enough to add <code>Q_INVOKABLE</code> to the line:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkPathLineEdit.h#L206" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkPathLineEdit.h#L206" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/Widgets/ctkPathLineEdit.h#L206</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="196" style="counter-reset: li-counter 195 ;">
<li>#ifdef USE_QFILEDIALOG_OPTIONS</li>
<li>  void setOptions(const QFileDialog::Options&amp; options);</li>
<li>  const QFileDialog::Options&amp; options()const;</li>
<li>#else</li>
<li>  void setOptions(const Options&amp; options);</li>
<li>  const Options&amp; options()const;</li>
<li>#endif</li>
<li>
<li>  /// Change the current extension of the edit line.</li>
<li>  ///  If there is no extension yet, set it</li>
<li class="selected">  void setCurrentFileExtension(const QString&amp; extension);</li>
<li>
<li>  QString settingKey()const;</li>
<li>  void setSettingKey(const QString&amp; key);</li>
<li>
<li>  bool showBrowseButton()const;</li>
<li>  void setShowBrowseButton(bool visible);</li>
<li>
<li>  bool showHistoryButton()const;</li>
<li>  void setShowHistoryButton(bool visible);</li>
<li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you have your own build you can test it.</p>
<p>But it would be better to go through the class and add <code>Q_PROPERTY</code> or <code>Q_INVOKABLE</code> for any feature someone might want to use from python.  Or make them <code>Q_SLOTS</code>.</p>
<p>Here’s an example of a class that is pretty completely exposed:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkColorDialog.h" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkColorDialog.h" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/Widgets/ctkColorDialog.h</a></h4>
<pre><code class="lang-h">/*=========================================================================

  Library:   CTK

  Copyright (c) Kitware Inc.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0.txt

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

=========================================================================*/

</code></pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkColorDialog.h" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Teresa_Gadda (2021-04-16 16:43 UTC)

<p>Thanks for the help!  I’ll give that a try.</p>

---
