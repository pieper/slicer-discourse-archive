---
topic_id: 42693
title: "Is There A Way To Limit Node Selector Width For Long Node Na"
date: 2025-04-25
url: https://discourse.slicer.org/t/42693
---

# Is there a way to limit node selector width for long node names?

**Topic ID**: 42693
**Date**: 2025-04-25
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-limit-node-selector-width-for-long-node-names/42693

---

## Post #1 by @mikebind (2025-04-25 16:45 UTC)

<p>I’m developing a module where users load a dynamic CT from DICOM as a Sequence.  The automatic names for these nodes are generally very long, and are a pain for users to rename to shorten (just renaming in the subject hierarchy only renames the proxy node which is then replaced when the sequence current frame is changed; to make a persistent change, the user must open the Sequences module, go change tabs, select the sequence, then select rename current sequence).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90dca680383833a5c0ab6855f225cd153a3e7e4c.png" data-download-href="/uploads/short-url/kFvuOAZXNCdxtwd6zBwJ1iMR7dO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90dca680383833a5c0ab6855f225cd153a3e7e4c_2_690x132.png" alt="image" data-base62-sha1="kFvuOAZXNCdxtwd6zBwJ1iMR7dO" width="690" height="132" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90dca680383833a5c0ab6855f225cd153a3e7e4c_2_690x132.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90dca680383833a5c0ab6855f225cd153a3e7e4c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90dca680383833a5c0ab6855f225cd153a3e7e4c.png 2x" data-dominant-color="BBB3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">776×149 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want the user to load the sequence and then be able to select in my module using a node selector as the first input.  However, since the name is so long and the selector widget automatically resizes to show the whole name, the module panel ends up taking up way too much screen real estate (see screenshot).  Is there a way to set a maximum width for the widget to avoid this?  I could rename the sequence once it is selected to be shorter, but since this is the first input, I can’t really rename it before the user selects it, and at that point the module width has already been set too wide.</p>
<p>On other forum questions, I see the suggestion that reducing font size is one way to deal with long node names, but that doesn’t really seem helpful here: the font size would need to be reduced so much that the text would become unreadable, so what would be the point?  A much better solution would be a truncated string that you could see the full length of when selecting from the dropdown. Is that possible using Qt settings somehow?</p>

---

## Post #2 by @muratmaga (2025-04-25 17:08 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="42693">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>However, since the name is so long and the selector widget automatically resizes to show the whole name, the module panel ends up taking up way too much screen real estate (see screenshot). Is there a way to set a maximum width for the widget to avoid this?</p>
</blockquote>
</aside>
<p>I really would like to know the answer to this as well. If possible to stop module pane to auto-adjust.</p>

---

## Post #3 by @pieper (2025-04-25 18:03 UTC)

<p>I don’t believe we have that currently, but Qt has methods to elide text taking into account the current font and layout.  It would be great to add that to the combobox infrastructure.  Probably needs to be in C++ at the CTK level. (see <a href="https://doc.qt.io/qt-6/qfontmetrics.html#elidedText" class="inline-onebox">QFontMetrics Class | Qt GUI | Qt 6.9.0</a>)</p>

---

## Post #4 by @mikebind (2025-04-25 19:24 UTC)

<p>OK thanks, good to know at least that it is not currently possible. I’ll stop trying to figure out how to do it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">  I’m pretty useless in C++, but this also seems pretty simple, so I’ll add this to my “maybe work on if I ever get around to it” pile.  I appreciate the response <a class="mention" href="/u/pieper">@pieper</a>, thanks!</p>

---

## Post #5 by @jcfr (2025-04-25 20:00 UTC)

<p>If you are using  <code>qMRMLNodeComboBox</code>, I would expect the text to be elided because the property <code>Qt::ElideMiddle</code> is already set <sup class="footnote-ref"><a href="#footnote-124626-1" id="footnote-ref-124626-1">[1]</a></sup>. This is made possible because <code>qMRMLNodeComboBox</code> itself instantiate <code>ctkComboBox</code>  providing  the function <code>setElideMode</code>.</p>
<p>If using <code>qMRMLSubjectHierarchyComboBox</code>, calling the function <code>setElideMode</code> should also be possible  as it derives from <code>ctkComboBox</code></p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-124626-1" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/cf620694f5a7addb540fdd656c8c0474f4fea08c/Libs/MRML/Widgets/qMRMLNodeComboBox.cxx#L101" class="inline-onebox">Slicer/Libs/MRML/Widgets/qMRMLNodeComboBox.cxx at cf620694f5a7addb540fdd656c8c0474f4fea08c · Slicer/Slicer · GitHub</a> <a href="#footnote-ref-124626-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #6 by @mikebind (2025-04-25 20:06 UTC)

<p>It is indeed a qMRMLNodeComboBox, but it is definitely not eliding the middle by default.  Is there another setting I can change, either in Slicer or in Qt Designer?</p>

---

## Post #7 by @mikebind (2025-04-25 20:35 UTC)

<p>Sorry, I was partially wrong!  If I manually resize the module panel, it will let me shrink it slightly and the middle of the node name <strong>does</strong> begin to elide (just a few characters before something stops it).  Additionally, I just tried setting maximum widths on the combo boxes, and that also appears to be working, with the text being elided in the middle. I’m not sure what is preventing me from making the module panel even thinner, but I think I can work with pre-set maximum widths and this middle elide mode option.</p>

---

## Post #8 by @lassoan (2025-04-26 12:47 UTC)

<p>You can choose how to set the size of a Qt combobox using <a href="https://doc.qt.io/qt-5/qcombobox.html#sizeAdjustPolicy-prop">sizeAdjustPolicy property</a>. For some reason, the default in Qt is to set the size based on the first item length on first show.</p>
<p>Could you try if setting it to <a href="https://doc.qt.io/qt-5/qcombobox.html#SizeAdjustPolicy-enum">QComboBox::AdjustToMinimumContentsLengthWithIcon</a> fixes your issue? The property is currently not exposed in Qt Designer but you can call <code>self.ui.myComboBox.setSizeAdjustPolicy(qt.QComboBox.AdjustToMinimumContentsLengthWithIcon)</code> in your widget setup method.</p>

---

## Post #9 by @mikebind (2025-04-28 23:30 UTC)

<p>Thanks for the suggestion <a class="mention" href="/u/lassoan">@lassoan</a>. However, I am running into problems while trying it.</p>
<pre><code class="lang-auto"># Gather all node selector combo boxes in module ui
comboBoxes = [
            val
            for key, val in ui.__dict__.items()
            if type(val) == slicer.qMRMLNodeComboBox
        ]
# Set the SizeAdjustPolicy for each
for comboBox in comboBoxes:
    comboBox.setSizeAdjustPolicy(
        qt.QComboBox.AdjustToMinimumContentsLengthWithIcon
    )
</code></pre>
<p>Yields <code>AttributeError: qMRMLNodeComboBox has no attribute named 'setSizeAdjustPolicy'</code>.  I tried a few variations like<br>
<code>comboBox.sizeAdjustPolicy = qt.QComboBox.AdjustToMinimumContentsLengthWithIcon </code>, but that yields <code>AttributeError: Property 'sizeAdjustPolicy' of type 'QComboBox::SizeAdjustPolicy' does not accept an object of type SizeAdjustPolicy (3)</code></p>
<p>Also, do I need to unset the maximum widths I was using in order to try this if we do manage to set the policy?  I’m not clear on how this will help.  Is the idea that the comboBox size will be set to a small size before being populated with list items? And that will help to trigger the eliding behavior? If so, do I need to do this in the module setup() method before <code>uiWidget.setMRMLScene(slicer.mrmlScene)</code>, which is what I think will populate the comboBox lists of nodes?</p>

---

## Post #10 by @lassoan (2025-04-28 23:41 UTC)

<p>It seems that the <code>sizeAdjustPolicy</code> property is not exposed on the public API of <code>qMRMLNodeComboBox</code>. Do you have a C++ build of Slicer? It should be easy to add it (just a few lines of code that calls <code>sizeAdjustPolicy</code> of the embedded <code>QComboBox</code> widget). If you don’t have a C++ build then I can add it in the next few days.</p>

---

## Post #11 by @mikebind (2025-04-29 02:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="42693">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you have a C++ build of Slicer?</p>
</blockquote>
</aside>
<p>Unfortunately no.</p>
<p>I’ve moved on, using enforced maximum widths to prevent the module panel from getting too wide,  but am willing to continue to test options if that would be helpful.</p>

---

## Post #12 by @cpinter (2025-04-30 09:23 UTC)

<p>I wanted to quickly add it, but it seems to me that it is already exposed:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L93">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L93" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L93" target="_blank" rel="noopener">Libs/MRML/Widgets/qMRMLNodeComboBox.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L93" rel="noopener"><code>3b2948fb0</code></a>
</div>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="83" style="counter-reset: li-counter 82 ;">
          <li>  /// but node editing is not requested via interaction node.</li>
          <li>  /// \sa nodeAboutToBeEdited</li>
          <li>  Q_PROPERTY(QString interactionNodeSingletonTag READ interactionNodeSingletonTag WRITE setInteractionNodeSingletonTag)</li>
          <li></li>
          <li>  Q_PROPERTY(bool selectNodeUponCreation READ selectNodeUponCreation WRITE setSelectNodeUponCreation)</li>
          <li>  /// This property controls the name that is displayed for the None item.</li>
          <li>  /// "None" by default.</li>
          <li>  /// \sa noneEnabled</li>
          <li>  Q_PROPERTY(QString noneDisplay READ noneDisplay WRITE setNoneDisplay)</li>
          <li></li>
          <li class="selected">  Q_PROPERTY(QComboBox::SizeAdjustPolicy sizeAdjustPolicy READ sizeAdjustPolicy WRITE setSizeAdjustPolicy)</li>
          <li></li>
          <li>public:</li>
          <li>  typedef QWidget Superclass;</li>
          <li></li>
          <li>  /// Construct an empty qMRMLNodeComboBox with a null scene,</li>
          <li>  /// no nodeType, where the hidden nodes are not forced on display.</li>
          <li>  explicit qMRMLNodeComboBox(QWidget* parent = nullptr);</li>
          <li>  ~qMRMLNodeComboBox() override;</li>
          <li></li>
          <li>  /// Get MRML scene that has been set by setMRMLScene(), there is no scene</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I tried using it on a node combobox and when getting the property it returns null, and when setting I get the same type of error <a class="mention" href="/u/mikebind">@mikebind</a> mentions (“does not accept an object of type…”).</p>
<p>Taking a quick look at the implementation I don’t see anything potentially wrong. I don’t have more time now to continue, but wanted to report these findings.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.cxx#L1301-L1312">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.cxx#L1301-L1312" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.cxx#L1301-L1312" target="_blank" rel="noopener">Libs/MRML/Widgets/qMRMLNodeComboBox.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Widgets/qMRMLNodeComboBox.cxx#L1301-L1312" rel="noopener"><code>3b2948fb0</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1301" style="counter-reset: li-counter 1300 ;">
          <li>QComboBox::SizeAdjustPolicy qMRMLNodeComboBox::sizeAdjustPolicy()const</li>
          <li>{</li>
          <li>  Q_D(const qMRMLNodeComboBox);</li>
          <li>  return d-&gt;ComboBox-&gt;sizeAdjustPolicy();</li>
          <li>}</li>
          <li></li>
          <li>//--------------------------------------------------------------------------</li>
          <li>void qMRMLNodeComboBox::setSizeAdjustPolicy(QComboBox::SizeAdjustPolicy policy)</li>
          <li>{</li>
          <li>  Q_D(qMRMLNodeComboBox);</li>
          <li>  d-&gt;ComboBox-&gt;setSizeAdjustPolicy(policy);</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
