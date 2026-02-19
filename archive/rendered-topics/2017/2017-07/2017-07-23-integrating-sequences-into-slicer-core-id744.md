---
topic_id: 744
title: "Integrating Sequences Into Slicer Core"
date: 2017-07-23
url: https://discourse.slicer.org/t/744
---

# Integrating Sequences into Slicer core

**Topic ID**: 744
**Date**: 2017-07-23
**URL**: https://discourse.slicer.org/t/integrating-sequences-into-slicer-core/744

---

## Post #1 by @moselhy (2017-07-23 11:51 UTC)

<p>Seeing as that Sequences are going to be the new era of browsing through multiple volumes, transforms, etc… I think it would be appropriate to integrate sequences into the core of Slicer without being an optional extension.</p>
<p>To do this, I think the following should be done, please let me know if I am missing something:</p>
<ol>
<li>qSlicerSequencesReader to work with the Core IO manager</li>
<li>A sample sequence to be included in the SampleData module (one is already uploaded <a href="http://slicer.kitware.com/midas3/item/299877" rel="nofollow noopener">here</a> by <a class="mention" href="/u/lassoan">@lassoan</a>)</li>
<li>slicer.util to have a loadSequence method</li>
<li>SampleData module to have a method to load a sample sequence</li>
</ol>
<p>I think I achieved the last two <a href="https://github.com/moselhy/Slicer/commit/c663e1f6b8fdcd73f540752b7eaf1a52eef3e843" rel="nofollow noopener">here</a>, but the first one requires C++ and I am only proficient with C programming as of yet, so I need some help on this.</p>

---

## Post #2 by @lassoan (2017-07-23 13:09 UTC)

<p>While all these can be added to Slicer without any changes to the core due to plugin interfaces (you can register IO plugins, sample data etc. in extensions and they appear the same way as if they had been implemented in Slicer core). However, I agree that it is probably time to make Sequences extension included in the Slicer download package. If there will be no argument about it, I’ll do it by the end of the week.</p>

---

## Post #3 by @adamrankin (2017-07-23 13:21 UTC)

<p>I will second the vote that it would be valuable as part of the downloaded package.</p>

---

## Post #4 by @adamrankin (2017-07-23 13:36 UTC)

<p>Related to Ben Wilk’s little workaround script for DICOM-&gt;Sequences, I am going to add the OnNodeLoaded callback from the DICOMDetailsPopup widget.</p>
<p>Then, I’ll investigate a proper solution.</p>
<p>Edit: This has already been accomplished. Simply use the ioManager Qt connect mechanism to catch the nodeLoaded signal</p>

---

## Post #5 by @moselhy (2017-07-30 22:40 UTC)

<blockquote>
<p>Simply use the ioManager Qt connect mechanism to catch the nodeLoaded signal</p>
</blockquote>
<p>Could you please point me to docs where I can find how to do this?</p>

---

## Post #6 by @adamrankin (2017-07-30 23:14 UTC)

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/adamrankin/SlicerTAVI/blob/master/ValvePlanning/ValvePlanning.py#L702" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/adamrankin/SlicerTAVI/blob/master/ValvePlanning/ValvePlanning.py#L702" target="_blank" rel="nofollow noopener">adamrankin/SlicerTAVI/blob/master/ValvePlanning/ValvePlanning.py#L702</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="692" style="counter-reset: li-counter 691 ;">
<li>
</li>
<li>#-------------------------------------------------------------------------------</li>
<li>def onDicomButtonClicked(self):</li>
<li>  logging.debug('ValvePlanningSlicelet.onDicomButtonClicked')</li>
<li>  dicomDialog = DICOMLib.DICOMDetailsPopup()</li>
<li>  dicomDialog.open()</li>
<li>
</li>
<li>#-------------------------------------------------------------------------------</li>
<li>def onDataButtonClicked(self):</li>
<li>  logging.debug('ValvePlanningSlicelet.onDataButtonClicked')</li>
<li class="selected">  slicer.app.ioManager().connect('newFileLoaded(qSlicerIO::IOProperties)', self.onNewAnatomyVolumeLoaded)</li>
<li>  slicer.app.ioManager().openAddVolumesDialog()</li>
<li>
</li>
<li>#-------------------------------------------------------------------------------</li>
<li>def onNewAnatomyVolumeLoaded(self, params):</li>
<li>  logging.debug('ValvePlanningSlicelet.onNewAnatomyVolumeLoaded')</li>
<li>  slicer.app.ioManager().disconnect('newFileLoaded(qSlicerIO::IOProperties)', self.onNewAnatomyVolumeLoaded)</li>
<li>  if len(params['nodeIDs']) != 1:</li>
<li>    slicer.util.warningDisplay("Multiple volumes selected. Using only the first selected.")</li>
<li>  self.anatomyVolumeNode = slicer.mrmlScene.GetNodeByID(params['nodeIDs'][0])</li>
<li>  self.logic.getParameterNode().SetParameter('anatomyVolumeNodeID', params['nodeIDs'][0])</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @moselhy (2017-07-31 06:33 UTC)

<p>Thanks. So which file am I supposed to edit to add a SequenceImporterPlugin?</p>

---

## Post #8 by @adamrankin (2017-07-31 12:49 UTC)

<p>Oh!! The proper fix.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> will have to help with that. You could look for multi volume in DICOM and adapt to handle sequences as well.</p>

---

## Post #9 by @jcfr (2017-10-19 08:02 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="744">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>probably time to make Sequences extension included in the Slicer download package […] I’ll do it by the end of the week.</p>
</blockquote>
</aside>
<p>What is the status ? Now we started working toward Slicer 5.x, do you think it is ready for inclusion ?</p>

---

## Post #10 by @lassoan (2017-10-19 13:04 UTC)

<p>The main reason I did not follow through with the integration is that for a nice integration some backward-incompatible changes would be needed in the Slicer core. We can do those for Slicer5!</p>
<p>I added a labs page: <a href="https://www.slicer.org/wiki/Documentation/Labs/Sequences">https://www.slicer.org/wiki/Documentation/Labs/Sequences</a></p>

---

## Post #11 by @lassoan (2017-10-19 14:47 UTC)

<p>By the way, 4D volumes can be loaded directly into Sequences nodes if Sequences extension is installed. You can set in Application settings to load into Sequence nodes by default (instead of multivolume nodes).</p>

---
