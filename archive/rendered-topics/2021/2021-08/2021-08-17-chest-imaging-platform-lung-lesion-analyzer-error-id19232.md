---
topic_id: 19232
title: "Chest Imaging Platform Lung Lesion Analyzer Error"
date: 2021-08-17
url: https://discourse.slicer.org/t/19232
---

# Chest Imaging Platform - Lung Lesion Analyzer error

**Topic ID**: 19232
**Date**: 2021-08-17
**URL**: https://discourse.slicer.org/t/chest-imaging-platform-lung-lesion-analyzer-error/19232

---

## Post #1 by @matt-warkentin (2021-08-17 15:33 UTC)

<p>Hi all,</p>
<p>I have run into an issue trying to the <code>Lung Lesion Analyzer</code> submodule from the <code>Chest Imaging Platform</code> extension. For context, this error arises on the current stable build of Slicer on MacOS (version <code>4.11.20210226</code>), but the issue does not occur on some previous versions (I can confirm it works on <code>4.8.1</code>).</p>
<p>When trying to add a <code>New Nodule</code> the following error is produced in the python REPL:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-29738/Chest_Imaging_Platform/lib/Slicer-4.11/qt-scripted-modules/CIP_LesionModel.py", line 1352, in __onAddNoduleButtonClicked__
    self.addNewNodule()
  File "/Applications/Slicer.app/Contents/Extensions-29738/Chest_Imaging_Platform/lib/Slicer-4.11/qt-scripted-modules/CIP_LesionModel.py", line 720, in addNewNodule
    fiducialsNode.AddObserver(fiducialsNode.MarkupAddedEvent, self.__onAddedSeed__)
AttributeError: 'vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsFid' object has no attribute 'MarkupAddedEvent'
</code></pre>
<p>I am not sure whether something has changed on the Slicer side of things that might throw this error, or if this is strictly a <code>CIP</code> extension issue. Has the <code>MarkupEventAdded</code> attributed been dropped in recent versions?</p>
<p>In any case, in the past I have tried seeking help with bugs by posting issues on their GitHub to no response, so I am turning here for advice.</p>

---

## Post #2 by @pieper (2021-08-17 20:13 UTC)

<p>Yes, the markups have improved a lot in Slicer since 4.8.1, so if CIP hasn’t been updated then you will probably still need to use the old version.  Probably you can move data back and forth easily if you also need to use features of new versions of Slicer.</p>

---

## Post #3 by @matt-warkentin (2021-08-18 14:38 UTC)

<p>Thanks for the response, <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>Does Slicer have any protection against having extensions available in the extension manager for a given version if those extensions haven’t been tested against/updated to that version?</p>

---

## Post #4 by @pieper (2021-08-18 14:49 UTC)

<p>Extensions are closely tied to the version of Slicer so generally this works well.  Often C++ extensions will fail to build if they aren’t compatible with the version of Slicer, so that will make them unavailable, but with python scripts they may fail at runtime with errors like you saw.  We don’t really want to prevent people from installing an extension where some parts may be useful and even if other parts are broken.  Often extension developers don’t have resources to maintain and update all the code so they rely on motivated community members to help identify and fix issues.</p>

---

## Post #5 by @matt-warkentin (2021-08-18 14:55 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="19232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>We don’t really want to prevent people from installing an extension where some parts may be useful and even if other parts are broken. Often extension developers don’t have resources to maintain and update all the code so they rely on motivated community members to help identify and fix issues.</p>
</blockquote>
</aside>
<p>Totally understandable on both points. I may make an attempt at trying to fix this bug and if so I will submit the PR to the maintainers. Thanks!</p>

---

## Post #6 by @pieper (2021-08-18 14:56 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="5" data-topic="19232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>I may make an attempt at trying to fix this bug and if so I will submit the PR to the maintainers.</p>
</blockquote>
</aside>
<p>That would be much appreciated!</p>

---

## Post #7 by @Eserval (2022-12-08 14:19 UTC)

<p>Hello everyone !</p>
<p>Did we have some sucess in update the Lung Lesion Analyzer tool ?</p>
<p>Best</p>

---

## Post #8 by @matt-warkentin (2022-12-08 17:44 UTC)

<p><a class="mention" href="/u/eserval">@Eserval</a> Sorry, I never ended up getting around to working on a fix.</p>

---

## Post #9 by @rbumm (2022-12-08 18:04 UTC)

<p>Thanks <a class="mention" href="/u/matt-warkentin">@matt-warkentin</a> - is there a demo somewhere of what the lung lesion analyzer actually did? Is it something like MINT lesion functionality?</p>

---

## Post #10 by @matt-warkentin (2022-12-08 18:07 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> This slide deck walks through its basic functionality: <a href="https://chestimagingplatform.org/files/chestimagingplatform/files/lung_lesion_analyzer.pdf" rel="noopener nofollow ugc">https://chestimagingplatform.org/files/chestimagingplatform/files/lung_lesion_analyzer.pdf</a></p>
<p>From the following website: <a href="https://chestimagingplatform.org/documentation" class="inline-onebox" rel="noopener nofollow ugc">Documentation | Chest Imaging Platform (CIP)</a></p>

---
