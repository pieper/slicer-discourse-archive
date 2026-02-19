---
topic_id: 763
title: "Qmrmlsubjecthierarchycombobox Usage"
date: 2017-07-25
url: https://discourse.slicer.org/t/763
---

# qMRMLSubjectHierarchyComboBox usage

**Topic ID**: 763
**Date**: 2017-07-25
**URL**: https://discourse.slicer.org/t/qmrmlsubjecthierarchycombobox-usage/763

---

## Post #1 by @dzenanz (2017-07-25 17:06 UTC)

<p>How to get notified in Python when <code>currentItemChanged</code> fires? I tried this:</p>
<pre><code># myCB1 is qMRMLNodeComboBox
# myCB2 is qMRMLSubjectHierarchyComboBox
myCB1.connect('currentNodeChanged(vtkMRMLNode*)', self.updateMRMLFromGUI)
myCB2.connect('currentItemChanged(int)', self.updateMRMLFromGUI)

def updateMRMLFromGUI(self, **unused):
  # gets called for myCB1, but not for myCB2
</code></pre>
<p>How to make only volumes selectable, and not studies or patients? For <code>qMRMLNodeComboBox</code> this <code>.ui</code> fragment only shows volumes:</p>
<pre><code>   &lt;widget class="qMRMLNodeComboBox" name="myCB1"&gt;
    &lt;property name="nodeTypes"&gt;
     &lt;stringlist&gt;
      &lt;string&gt;vtkMRMLScalarVolumeNode&lt;/string&gt;
     &lt;/stringlist&gt;
    &lt;/property&gt;
</code></pre>
<p>Is there an equivalent or similar thing for <code>qMRMLSubjectHierarchyComboBox</code> either as <code>.ui</code> fragment or Python snippet?</p>

---

## Post #2 by @cpinter (2017-07-25 18:34 UTC)

<p>First question:<br>
<code>self.usPatientItemCombobox.connect('currentItemChanged(vtkIdType)', self.onUSPatientSelectionChanged)</code></p>
<p>Second question:<br>
If you only want to be able to select volumes, then simply use qMRMLNodeComboBox. If you want to see the hierarchy as well, but only have the volumes in the hierarchy show up, then you can easily add a filter similar to the attribute filter in the combobox class<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyComboBox.h#L81" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyComboBox.h#L81" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyComboBox.h#L81</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="71" style="counter-reset: li-counter 70 ;">
<li>Q_INVOKABLE vtkIdType rootItem()const;</li>
<li>
</li>
<li>void setShowRootItem(bool show);</li>
<li>bool showRootItem()const;</li>
<li>
</li>
<li>bool highlightReferencedItems()const;</li>
<li>void setHighlightReferencedItems(bool highlightOn);</li>
<li>
</li>
<li>int maximumNumberOfShownItems()const;</li>
<li>void setMaximumNumberOfShownItems(int maxNumberOfShownItems);</li>
<li class="selected">
</li>
<li>bool alignPopupVertically()const;</li>
<li>void setAlignPopupVertically(bool align);</li>
<li>
</li>
<li>/// Set attribute filter that allows showing only items that have the specified attribute and their parents.</li>
<li>/// \param attributeName Name of the attribute by which the items are filtered</li>
<li>/// \param attributeValue Value of the specified attribute that needs to match this given value in order</li>
<li>///   for it to be shown. If empty, then existence of the attribute is enough to show. Empty by default</li>
<li>Q_INVOKABLE void setAttributeFilter(const QString&amp; attributeName, const QVariant&amp; attributeValue=QVariant());</li>
<li>/// Remove item attribute filtering \sa setAttribute</li>
<li>Q_INVOKABLE void removeAttributeFilter();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @dzenanz (2017-07-25 21:12 UTC)

<p>I have tried <code>myCB2.connect('currentItemChanged(vtkIdType)', self.updateMRMLFromGUI)</code> first, and since that didn’t work I also tried <code>int</code> to which <code>vtkIdType</code> resolves. Does Python have a 64-bit int?</p>
<p>I have seen the method <a href="http://apidocs.slicer.org/master/classqMRMLSubjectHierarchyComboBox.html#aa74541aabd9f1294b6e91a4da00d4924" rel="nofollow noopener">setAttributeFilter</a>, but no example of its usage. Can you provide a few example calls to this method, even if it doesn’t accomplish what I want?</p>

---

## Post #4 by @lassoan (2017-07-26 01:03 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="3" data-topic="763">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>'currentItemChanged</p>
</blockquote>
</aside>
<p>I agree, it would be great to have some examples in SH Python tests and a few words about this in the class documentation would be useful, too.</p>

---

## Post #5 by @cpinter (2017-07-26 13:00 UTC)

<p>Not sure what you mean by “a few words”, but there is as much in the documentation as there can be for an extremely simple feature like this I think:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L85-L88" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L85-L88" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L85-L88</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="85" style="counter-reset: li-counter 84 ;">
<li>
</li>
<li>/// Get whether multi-selection is enabled</li>
<li>bool multiSelection();</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
and<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyComboBox.h#L77-L80" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyComboBox.h#L77-L80" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyComboBox.h#L77-L80</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="77" style="counter-reset: li-counter 76 ;">
<li>void setHighlightReferencedItems(bool highlightOn);</li>
<li>
</li>
<li>int maximumNumberOfShownItems()const;</li>
<li>void setMaximumNumberOfShownItems(int maxNumberOfShownItems);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Would you add something else?</p>
<p>I’ll add a test about it to the SH generic test. Apparently it started failing last night, so I need to check up on it anyway.</p>

---

## Post #6 by @cpinter (2017-07-26 14:56 UTC)

<p>Example in new test section:<br>
<a href="https://github.com/Slicer/Slicer/commit/e66e3b08e35384526528e6ae678e9ec9f079f286#diff-8cdc75584ed1fbe2b0be1e655a2f22a1R352" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/e66e3b08e35384526528e6ae678e9ec9f079f286#diff-8cdc75584ed1fbe2b0be1e655a2f22a1R352</a></p>

---

## Post #7 by @jcfr (2017-07-26 15:10 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> Where do you think we should link or reference existing documentation and code samples to streamline your developer experience ?</p>

---

## Post #8 by @dzenanz (2017-07-26 18:05 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Thanks, that test is very useful as an example.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> I expected the examples to be either on the <a href="https://www.slicer.org/wiki/Documentation/Labs/SubjectHierarchy" rel="nofollow noopener">labs page</a> or in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy" rel="nofollow noopener">script repository</a>. I will add Csaba’s test as an example in the script repository.</p>
<p>Still, <code>currentItemChanged</code> does not trigger for me. Parts of actual code:</p>
<pre><code>self._get('projectionImage').connect('currentItemChanged(vtkIdType)', self.shChanged) # setting updateMRMLFromGUI directly as slot doesn't work either
self._get('outputImage').connect('currentNodeChanged(vtkMRMLNode*)', self.updateMRMLFromGUI) # gets triggered properly

def shChanged(self, shID):
    self.updateMRMLFromGUI(shID)
    print "Triggered: "+str(shID)
  
def updateMRMLFromGUI(self, **unused):
    # handle the change</code></pre>

---

## Post #9 by @dzenanz (2017-07-26 18:22 UTC)

<p>Link to newly added docs: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Filter_nodes_in_TreeView_or_ComboBox" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Filter_nodes_in_TreeView_or_ComboBox</a></p>

---

## Post #10 by @cpinter (2017-07-26 18:42 UTC)

<p>Thanks! I have two comments:</p>
<ol>
<li>I think the Qt designer plugins are an irrelevant detail for this example</li>
<li>The entities that you show and in this case filter in SH are not nodes, but they are items. It’s important, because for many of the items there is no corresponding MRML node. This may actually confuse people who want to filter in node attribute, when in reality the filter applies on SH item attributes.</li>
</ol>

---

## Post #11 by @cpinter (2017-07-26 18:44 UTC)

<p>I quickly fixed it myself.</p>

---

## Post #12 by @dzenanz (2017-07-26 19:51 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> for docs fix.</p>
<p>Can you provide declaration for <code>onUSPatientSelectionChanged</code>, corresponding to this code fragment?</p>
<pre><code>self.usPatientItemCombobox.connect('currentItemChanged(vtkIdType)', self.onUSPatientSelectionChanged)</code></pre>

---

## Post #13 by @cpinter (2017-07-26 20:55 UTC)

<p>Of course, the example is from the SegmentRegistration extension:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L283-L290" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L283-L290" target="_blank" rel="nofollow noopener">SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L283-L290</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="283" style="counter-reset: li-counter 282 ;">
<li>  self.usSegmentationNodeCombobox.setCurrentNode(self.logic.usSegmentationNode)</li>
<li>  self.onUSSegmentationNodeSelectionChanged(self.logic.usSegmentationNode)</li>
<li>
</li>
<li>#------------------------------------------------------------------------------</li>
<li>def onUSVolumeNodeSelectionChanged(self, usVolumeNode):</li>
<li>  self.logic.usVolumeNode = usVolumeNode</li>
<li>
</li>
<li>#------------------------------------------------------------------------------</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #14 by @dzenanz (2017-07-27 22:02 UTC)

<p>Filtering does not work, and copy-pasting from SegmentRegistration didn’t help for event triggering:</p>
<pre><code>def __init__(self, parent=None):
  slicer.qMRMLWidget.__init__(self, parent)
  slicer.util.VTKObservationMixin.__init__(self)
  ...
  self._get('projectionImage').connect('currentItemChanged(vtkIdType)', self.shChanged)
  # self._get('projectionImage').setAttributeFilter('DICOM.Modality','NM') #combobox empty if enabled
  self._get('outputImage').connect('currentNodeChanged(vtkMRMLNode*)', self.updateMRMLFromGUI)
  
  # copy-pasted code, combobox is displayed and shows the hierarchy properly
  self.usPatientItemCombobox = slicer.qMRMLSubjectHierarchyComboBox()
  self.usPatientItemCombobox.name = "usPatientItemCombobox"
  self.usPatientItemCombobox.setMRMLScene( slicer.mrmlScene )
  self._get('ioNodes').layout().addRow('US patient', self.usPatientItemCombobox)
  self.usPatientItemCombobox.connect('currentItemChanged(vtkIdType)', self.onUSPatientSelectionChanged)
  ...
  
def onUSPatientSelectionChanged(self, usPatientShItemID):
  print "usPatientShItemID: "+str(usPatientShItemID)
</code></pre>
<p>I will try to create a minimum working example to diagnose what is going on.</p>

---

## Post #15 by @cpinter (2017-07-28 00:13 UTC)

<p>When you say something “doesn’t work”, please tell us how it doesn’t work. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem#Error_report_contents">https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem#Error_report_contents</a></p>

---

## Post #16 by @dzenanz (2017-07-28 14:05 UTC)

<aside class="quote no-group quote-modified" data-username="dzenanz" data-post="14" data-topic="763">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>self._get(‘projectionImage’).setAttributeFilter(‘DICOM.Modality’,‘NM’)</p>
</blockquote>
</aside>
<p>With this line present, the projectionImage <code>qMRMLSubjectHierarchyComboBox</code> doesn’t display any nodes<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85605413ade8ea5f54ca376e7438082b6bb9152a.png" data-download-href="/uploads/short-url/j1TSWOJv3Z44YNQ3dHlgyoRL1s6.png?dl=1" title="36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85605413ade8ea5f54ca376e7438082b6bb9152a.png" alt="36" data-base62-sha1="j1TSWOJv3Z44YNQ3dHlgyoRL1s6" width="690" height="104" data-dominant-color="F1F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">36</span><span class="informations">698×106 1.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
even if there are nodes which have NM modality:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29521d32edf9932644e2128c72d0a552a2d543ab.png" data-download-href="/uploads/short-url/5TxviDcqwTMYqJR7h0JYBUIEk2v.png?dl=1" title="58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29521d32edf9932644e2128c72d0a552a2d543ab_2_301x499.png" alt="58" data-base62-sha1="5TxviDcqwTMYqJR7h0JYBUIEk2v" width="301" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29521d32edf9932644e2128c72d0a552a2d543ab_2_301x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29521d32edf9932644e2128c72d0a552a2d543ab_2_451x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29521d32edf9932644e2128c72d0a552a2d543ab_2_602x998.png 2x" data-dominant-color="EDF1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">58</span><span class="informations">730×1211 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @cpinter (2017-07-28 14:51 UTC)

<p>Indeed, the screenshot shows that the item does have that attribute. What happens if you set the same filter on the SH tree view? You can get it like this:<br>
dmw=slicer.modules.data.widgetRepresentation()<br>
sht=slicer.util.findChildren(dmw,className=‘qMRMLSubjectHierarchyTreeView’)[0]</p>
<p>If I create a combobox like this (I had a CT in the scene), it works with the latest version:<br>
c=slicer.qMRMLSubjectHierarchyComboBox()<br>
c.setMRMLScene(slicer.mrmlScene)<br>
c.show()<br>
c.setAttributeFilter(‘DICOM.Modality’,‘CT’)</p>
<p>Basic question but are you sure you set the scene to the combobox?</p>

---

## Post #18 by @lassoan (2017-07-28 16:52 UTC)

<p>Another thing to check: Try if it works if you set the attribute before you create the widget (the order should not matter but maybe there is a bug and the tree is not re-filtered when an attribute is changed).</p>

---

## Post #19 by @dzenanz (2017-08-01 22:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Even if data is loaded (and hence attributes are set) before my widget is created/accessed, I did not notice any change.</p>
<p>I created the minimum working example in this <a href="https://github.com/dzenanz/Slicer/commit/76f880c2661267aff7cf674d5b08aa203262f959" rel="nofollow noopener">commit</a>. The <a href="https://github.com/dzenanz/Slicer/blob/76f880c2661267aff7cf674d5b08aa203262f959/Modules/Scripted/ScriptedMWE/ScriptedMWEWidgets/ScriptedMWEWidget.py#L16-L19" rel="nofollow noopener">problematic</a> lines are 16-19.</p>

---

## Post #20 by @dzenanz (2017-08-04 17:19 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Have you tried my <a href="https://github.com/dzenanz/Slicer/blob/76f880c2661267aff7cf674d5b08aa203262f959/Modules/Scripted/ScriptedMWE/ScriptedMWEWidgets/ScriptedMWEWidget.py#L16-L19" rel="nofollow noopener">MWE</a>?</p>

---

## Post #21 by @cpinter (2017-08-04 20:35 UTC)

<p>Is adding a module to the Slicer source code itself the way to go for examples like this? I could imagine a variety of ways that are simpler than building a whole Slicer from scratch.</p>

---

## Post #22 by @dzenanz (2017-08-07 16:41 UTC)

<p>I don’t know why my code isn’t working, so keeping its build system might be important. Also rewriting it into a copy-paste script would have required a lot of effort. I know that building Slicer is slow, but it does not require much effort. A faster way to test this is to copy-paste added files (and the modified CMakeLists) into existing Slicer instance and rebuilding it.</p>

---

## Post #23 by @cpinter (2017-08-07 21:24 UTC)

<p>I built your branch, and did the following:</p>
<ul>
<li>Uncomment line 18</li>
<li>Start Slicer</li>
<li>Load MRHead (so that there is one node that has no attributes)</li>
<li>Load a CT and an RTDOSE from DICOM</li>
<li>Switch to your module</li>
</ul>
<p>The combobox was not empty and I only saw the CT, which is the expected behaviour. Did I do something in a different order than the way you could reproduce it?</p>

---

## Post #24 by @jcfr (2017-08-07 22:46 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> Let’s work together and offline to address the issue. We can then report back our findings.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> Thanks for looking into the problem.</p>

---

## Post #25 by @cpinter (2017-08-07 23:04 UTC)

<p>In case you want to do some debugging, a breakpoint here should help revealing the problem:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.cxx#L335" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.cxx#L335" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSortFilterSubjectHierarchyProxyModel.cxx#L335</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="325" style="counter-reset: li-counter 324 ;">
<li>      // If level was requested but different, then only show if any of its children are shown</li>
<li>      onlyAcceptIfAnyChildIsAccepted = true;</li>
<li>      }</li>
<li>    else</li>
<li>      {</li>
<li>      return false;</li>
<li>      }</li>
<li>    }</li>
<li>  }</li>
<li>
</li>
<li class="selected">// Filter by item attribute</li>
<li>if (!d-&gt;AttributeNameFilter.isEmpty())</li>
<li>  {</li>
<li>  std::string attributeNameFilterStr(d-&gt;AttributeNameFilter.toLatin1().constData());</li>
<li>  if (!shNode-&gt;HasItemAttribute(itemID, attributeNameFilterStr))</li>
<li>    {</li>
<li>    if (canAcceptIfAnyChildIsAccepted)</li>
<li>      {</li>
<li>      // If attribute was requested but missing, then only show if any of its children are shown</li>
<li>      onlyAcceptIfAnyChildIsAccepted = true;</li>
<li>      }</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #26 by @dzenanz (2017-08-08 14:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> You were right about order of widget creation and data loading. Loading data first, and then accessing the widget works (but not the other way around). But I think I tested that - I guess not carefully enough.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> Do you have some suggestion for <code>currentItemChanged</code> not firing?</p>

---

## Post #27 by @dzenanz (2017-08-08 14:49 UTC)

<p>I am taking rest of the day off, so I could debug this tomorrow (unless you beat me to it). But it is probably due to some scene change event not being observed, and not in the logic here.</p>

---

## Post #28 by @cpinter (2017-08-08 16:33 UTC)

<p>You probably use currentItemChanged wrong. It works in this example. Please look at the differences. As a last resort you can just copy-paste the related code<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L72" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L72" target="_blank" rel="nofollow noopener">SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L72</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="62" style="counter-reset: li-counter 61 ;">
<li>self.showDicomBrowserButton.name = "showDicomBrowserButton"</li>
<li>self.registrationCollapsibleButtonLayout.addRow(self.showDicomBrowserButton)</li>
<li>self.showDicomBrowserButton.connect('clicked()', self.onDicomLoad)</li>
<li>
</li>
<li># US patient item combobox</li>
<li>self.usPatientItemCombobox = slicer.qMRMLSubjectHierarchyComboBox()</li>
<li>self.usPatientItemCombobox.setLevelFilter(slicer.vtkMRMLSubjectHierarchyConstants.GetDICOMLevelPatient())</li>
<li>self.usPatientItemCombobox.setMRMLScene( slicer.mrmlScene )</li>
<li>self.usPatientItemCombobox.setToolTip( "Select US patient" )</li>
<li>self.usPatientItemCombobox.name = "usPatientItemCombobox"</li>
<li class="selected">self.registrationCollapsibleButtonLayout.addRow('US patient: ', self.usPatientItemCombobox)</li>
<li>self.usPatientItemCombobox.connect('currentItemChanged(vtkIdType)', self.onUSPatientSelectionChanged)</li>
<li>
</li>
<li># US volume node combobox</li>
<li>self.usVolumeNodeCombobox = slicer.qMRMLNodeComboBox()</li>
<li>self.usVolumeNodeCombobox.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )</li>
<li>self.usVolumeNodeCombobox.showChildNodeTypes = False</li>
<li>self.usVolumeNodeCombobox.noneEnabled = True</li>
<li>self.usVolumeNodeCombobox.noneDisplay = 'Automatic search failed - please select'</li>
<li>self.usVolumeNodeCombobox.setMRMLScene( slicer.mrmlScene )</li>
<li>self.usVolumeNodeCombobox.setToolTip( "Select US image" )</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #29 by @dzenanz (2017-08-09 15:56 UTC)

<p>I tried that. Now I added that to MWE. The event is still not triggered.<br>
<a href="https://github.com/dzenanz/Slicer/commit/7335435f49a8946badba9dbfa90dbb7d9bca6871" class="onebox" target="_blank" rel="nofollow noopener">https://github.com/dzenanz/Slicer/commit/7335435f49a8946badba9dbfa90dbb7d9bca6871</a></p>

---

## Post #30 by @cpinter (2017-08-09 16:26 UTC)

<p>I don’t know what to add. I provided a working example, which still works. Please try to find the difference that makes yours inoperational.</p>

---

## Post #31 by @dzenanz (2017-08-09 17:25 UTC)

<p>The only big difference is that in <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L72" rel="nofollow noopener">ProstateMRIUSContourPropagation</a> UI is generated programatically, whereas in my MWE it is loaded from a <code>.ui</code> file using <code>QUiLoader</code>.</p>

---

## Post #32 by @cpinter (2017-08-09 17:40 UTC)

<p>If that is the only difference then is it possible that the widget is not completely set up by the time you try to connect?</p>

---

## Post #33 by @dzenanz (2017-08-09 18:05 UTC)

<p>That <a href="https://github.com/dzenanz/Slicer/commit/3670a645d64ef94a37548643224936a185c4b15f" rel="nofollow noopener">does not</a> seem to matter. Even if if the only thing left to do are connections, connecting <code>currentItemChanged</code> has no effect.</p>

---

## Post #34 by @dzenanz (2017-08-17 17:38 UTC)

<p>In an attempt to get a working MWE, I tried starting from the existing module. However the event does not fire in it either!</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/dzenanz/Slicer/blob/915dcd08afa3dcdee5e78a322b83850833ffac12/Modules/Scripted/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L236" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/dzenanz/Slicer/blob/915dcd08afa3dcdee5e78a322b83850833ffac12/Modules/Scripted/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L236" target="_blank" rel="nofollow noopener">dzenanz/Slicer/blob/915dcd08afa3dcdee5e78a322b83850833ffac12/Modules/Scripted/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L236</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="226" style="counter-reset: li-counter 225 ;">
<li>  # Add vertical spacer</li>
<li>  self.layout.addStretch(4)</li>
<li>
</li>
<li>#------------------------------------------------------------------------------</li>
<li>def onDicomLoad(self):</li>
<li>  slicer.modules.dicom.widgetRepresentation()</li>
<li>  slicer.modules.DICOMWidget.enter()</li>
<li>
</li>
<li>#------------------------------------------------------------------------------</li>
<li>def onUSPatientSelectionChanged(self, usPatientShItemID):</li>
<li class="selected">  logging.info("onUSPatientSelectionChanged, usPatientShItemID: "+usPatientShItemID)</li>
<li>  print("onUSPatientSelectionChanged, usPatientShItemID: "+usPatientShItemID)</li>
<li>  self.logic.usPatientShItemID = usPatientShItemID</li>
<li>  self.logic.parseUSPatient()</li>
<li>  # Select parsed nodes in the comboboxes</li>
<li>  self.usVolumeNodeCombobox.setCurrentNode(self.logic.usVolumeNode)</li>
<li>  self.onUSVolumeNodeSelectionChanged(self.logic.usVolumeNode)</li>
<li>  self.usSegmentationNodeCombobox.setCurrentNode(self.logic.usSegmentationNode)</li>
<li>  self.onUSSegmentationNodeSelectionChanged(self.logic.usSegmentationNode)</li>
<li>
</li>
<li>#------------------------------------------------------------------------------</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #35 by @cpinter (2017-08-17 17:50 UTC)

<p>Thanks, <a class="mention" href="/u/dzenanz">@dzenanz</a>! This is strange indeed, I’ll investigate at once, as it’s very easy for me to reproduce now.</p>

---

## Post #36 by @cpinter (2017-08-22 19:24 UTC)

<p>Hi <a class="mention" href="/u/dzenanz">@dzenanz</a>, sorry for the wait! The cause of the problem was very banal: the signal was not propagated to the combobox (aggregation vs inheritance…). I committed a fix in Slicer. Please let me know how it works.<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/b9acab728f0a44841cfc2c039a7fd2a419025eed" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    
<h4>
  <a href="https://github.com/Slicer/Slicer/commit/b9acab728f0a44841cfc2c039a7fd2a419025eed" target="_blank" rel="nofollow noopener">BUG: Propagate current item changed signal in SH combobox</a>
</h4>

  <pre class="message" style="white-space: pre-wrap;">Related to discussion https://discourse.slicer.org/t/qmrmlsubjecthierarchycombobox-usage/763

git-svn-id: http://svn.slicer.org/Slicer4/trunk@26298 3bd1e089-480b-0410-8dfb-8563597acbee</pre>

<div class="date">
  by <a href=""></a>
  on <a href="https://github.com/Slicer/Slicer/commit/b9acab728f0a44841cfc2c039a7fd2a419025eed" target="_blank" rel="nofollow noopener">07:22PM - 22 Aug 17</a>
</div>

<div class="github-commit-stats">
  changed <strong>1 files</strong>
  with <strong>2 additions</strong>
  and <strong>0 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #37 by @dzenanz (2017-08-22 23:15 UTC)

<p>Thanks Csaba, that seems to have fixed it!</p>

---

## Post #38 by @cpinter (2017-08-23 13:05 UTC)

<p>Excellent! Sorry for giving you a hard time, I was fully in the knowledge that the function in MRI-US worked.</p>

---
