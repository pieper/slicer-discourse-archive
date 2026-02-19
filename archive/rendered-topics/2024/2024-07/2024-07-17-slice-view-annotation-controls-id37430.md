---
topic_id: 37430
title: "Slice View Annotation Controls"
date: 2024-07-17
url: https://discourse.slicer.org/t/37430
---

# Slice view annotation controls

**Topic ID**: 37430
**Date**: 2024-07-17
**URL**: https://discourse.slicer.org/t/slice-view-annotation-controls/37430

---

## Post #1 by @cpinter (2024-07-17 12:37 UTC)

<p>Hi all,</p>
<p>I just wanted to turn off slice view annotations in the latest Slicer and I found that it does not work. The main checkbox in the module does not have any effect:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f217a9f146d51d85a0fa822dd2af4048af65283.png" alt="image" data-base62-sha1="29QTcVXtzCE9lg4tckfiHoMWPw7" width="518" height="346"></p>
<p>Steps:</p>
<ul>
<li>Load MRHead (see annotation in all slice views bottom left)</li>
<li>Go to DataProbe module</li>
<li>Uncheck checkbox shown above</li>
</ul>
<p>Similarly, the code here also does not have any effect:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#hide-slice-view-annotations" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#hide-slice-view-annotations</a></p>
<p>Has anything around the topic changed lately?</p>
<p>Update: Same behavior in 5.6.2. Looking at the SliceViewAnnotations code but it’s barely commented and a bit convoluted, so if someone knows it well any advice would be welcome. Thanks!</p>

---

## Post #2 by @cpinter (2024-07-17 12:57 UTC)

<p>It seems to me that the update</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L327">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L327" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L327" target="_blank" rel="noopener">Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L327</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="317" style="counter-reset: li-counter 316 ;">
          <li>        return</li>
          <li></li>
          <li>    # Create corner annotations if have not created already</li>
          <li>    if len(self.sliceViewNames) == 0:</li>
          <li>        self.createCornerAnnotations()</li>
          <li></li>
          <li>    for sliceViewName in self.sliceViewNames:</li>
          <li>        sliceWidget = self.layoutManager.sliceWidget(sliceViewName)</li>
          <li>        if sliceWidget:</li>
          <li>            sl = sliceWidget.sliceLogic()</li>
          <li class="selected">            self.updateCornerAnnotation(sl)</li>
          <li></li>
          <li>def createGlobalVariables(self):</li>
          <li>    self.sliceViewNames = []</li>
          <li>    self.sliceWidgets = {}</li>
          <li>    self.sliceViews = {}</li>
          <li>    self.renderers = {}</li>
          <li></li>
          <li>def createCornerAnnotations(self):</li>
          <li>    self.createGlobalVariables()</li>
          <li>    self.sliceViewNames = list(self.layoutManager.sliceViewNames())</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>is not called due to the early return</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L317">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L317" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L317" target="_blank" rel="noopener">Slicer/Slicer/blob/8c6219abd3f171f938fd5d003cd551db20842c7e/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L317</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="307" style="counter-reset: li-counter 306 ;">
          <li></li>
          <li>    self.cornerTextParametersCollapsibleButton.enabled = enabled</li>
          <li>    self.activateCornersGroupBox.enabled = enabled</li>
          <li>    self.fontPropertiesGroupBox.enabled = enabled</li>
          <li>    self.annotationsAmountGroupBox.enabled = enabled</li>
          <li></li>
          <li>def updateSliceViewFromGUI(self):</li>
          <li>    if not self.sliceViewAnnotationsEnabled:</li>
          <li>        self.removeObservers(method=self.updateViewAnnotations)</li>
          <li>        self.removeObservers(method=self.updateGUIFromMRML)</li>
          <li class="selected">        return</li>
          <li></li>
          <li>    # Create corner annotations if have not created already</li>
          <li>    if len(self.sliceViewNames) == 0:</li>
          <li>        self.createCornerAnnotations()</li>
          <li></li>
          <li>    for sliceViewName in self.sliceViewNames:</li>
          <li>        sliceWidget = self.layoutManager.sliceWidget(sliceViewName)</li>
          <li>        if sliceWidget:</li>
          <li>            sl = sliceWidget.sliceLogic()</li>
          <li>            self.updateCornerAnnotation(sl)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>What I don’t understand</p>
<ul>
<li>Why nobody noticed this in the past several months</li>
<li>Git log on this file shows basically no functional change for years</li>
</ul>
<p>Although there is this commit that touches just what is broken:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/5b0bcad4f3241c63ca455d2b6f5885534d92ea30">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/5b0bcad4f3241c63ca455d2b6f5885534d92ea30" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/5b0bcad4f3241c63ca455d2b6f5885534d92ea30" target="_blank" rel="noopener">ENH: Support restoring SliceViewAnnotations enabled state</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-09-28" data-time="00:08:21" data-timezone="UTC">12:08AM - 28 Sep 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 1 files with 6 additions and 9 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/5b0bcad4f3241c63ca455d2b6f5885534d92ea30" target="_blank" rel="noopener">
          <span class="added">+6</span>
          <span class="removed">-9</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Also simplify setting of checkbox state in SliceViewAnnotations</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I think for now I’ll use the workaround to call <code>updateCornerAnnotation</code> with each slice logic, but it would be good to get to the bottom of this.</p>

---

## Post #3 by @lassoan (2024-07-18 04:29 UTC)

<p>Disabling corner annotation has never worked for me. I always force update manually add you described.</p>
<p>The current implementation of this feature is so low quality (fragile, complicated, very limited functionality, poor visual appearance) that I would rewrite it from scratch. See details here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7184">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7184" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7184" target="_blank" rel="noopener">Refactor Slice View Annotations infrastructure</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-08-22" data-time="02:38:43" data-timezone="UTC">02:38AM - 22 Aug 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

Since its i<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nception started in 2014, the support for rendering slice annotations has been very useful.

It is ultimately done in the `SliceAnnotations`[^1] class instantiated based on the workflow described below.

Once the `SliceAnnotations` is instantiated, it is then responsible to add observation on slice logics (see `addSliceViewObserver()`[^6]) by systematically checking if new slice viewer have been instantiated within the function `updateViewAnnotations()`[^7] it self called when any of the slice logic is modified.

**Problem:** As outlined below by @lassoan, the current design is not extensible &amp; flexible as it requires to hard-code module specific behavior into a single script. It for example, prevent extension from registering new annotation that should take precedence.

[^6]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L346-L357
[^7]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L363-L380

## Describe the solution you'd like

* Re-implemented in C++
* Organize the content to display in `vtkMRMLTextNode` nodes with associated displayable manager
* Allow customization of displayed fields
* Support displaying
  * Slice position
  * Anatomical direction codes
  * Image display parameters (window, level, slice thickness, etc)
  * Patient/study/series metadata

## Describe alternatives you've considered

NA

## Additional context

### Related posts &amp; issues

* https://discourse.slicer.org/t/how-to-show-orientation-marker-label-left-right-anterior-posterior/20231
* https://github.com/Slicer/Slicer/issues/4854

### Excerpt copied from the prior comments and emails

_Originally shared by @lassoan over email on August 19th, 2023_

&gt; We want to display a lot of things around image sides and corners:
&gt; - Patient/study/series metadata (with much more flexibility than now) 
&gt; - Anatomical direction codes (L, R, A, P, LA, LPI,... similarly to slice offset sliders) 
&gt; - Image display parameters (window, level, slice thickness, etc)
&gt; - Slice position, maybe some data probe content
&gt; - Any text node content (that would allow a flexible way for modules to display custom content; which corner, color, etc. could be specified in display node)
&gt; 
&gt; The current design is very limited, inflexible, non-extensible in any way. The implementation is also very fragile, low quality.
&gt; 
&gt; The best would be to reimplement it in C++, using MRML nodes to store data, displayable manager to render, etc.
&gt; 
&gt; Maybe all the corner text could be specified using HTML-like description using placeholders, for example:
&gt; 
&gt; ```html
&gt; &lt;b&gt;&lt;PatientName/&gt; &lt;PatientAge/&gt; &lt;PatientSex format="short" /&gt;&lt;/b&gt;&lt;br&gt;
&gt; &lt;StudyDate/&gt;&lt;br&gt;
&gt; &lt;WindowWidthLevel/&gt;&lt;br&gt;
&gt; &lt;TextNode id="vtkMRMLTextNode1" color="red" /&gt;
&gt; ```

_Originally posted by @lassoan in https://github.com/Slicer/Slicer/issues/7176#issuecomment-1684865471_

&gt; Slice view annotations is a mess. It was a quick prototype that got integrated to have this important feature in Slicer, but the design is really fragile and limited. We would need to rebuild it from scratch, using proper MRML-based design and flexibility and extensibility in mind, as overlay on image corners is very important space for displaying information.

_Originally posted by @pieper in https://github.com/Slicer/Slicer/issues/7176#issuecomment-1685033306_

&gt; Many viewers also use these as UI controls/widgets too (e.g. control reslice rotation or window/level tools by clicking on the corresponding corner annotation can be logical and 

### Workflow: Instantiation of `DataProbeLib.SliceAnnotations`

1. `DataProbe` module constructor, `slicer.app.startupCompleted()` is connected to `DataProbe.DataProbe.addView()`[^2]
3. `DataProbe.DataProbe.addView()` instantiates[^3] `DataProbeInfoWidget.DataProbeInfoWidget`[^4] class 
4. In `DataProbeInfoWidget` constructor, the function `DataProbeInfoWidget._createSmall()` which intern instantiates `DataProbeLib.SliceAnnotations()`[^5]

[^1]: https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py
[^2]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L40-L41
[^3]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L59-L60
[^4]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L68-L106
[^5]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L401-L406</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @cpinter (2024-07-19 11:15 UTC)

<p>Agreed, thanks. If this is not a recent regression then let’s leave any improvement or fix for the complete revamp.</p>

---
