# Flood filling with masking?

**Topic ID**: 7015
**Date**: 2019-06-04
**URL**: https://discourse.slicer.org/t/flood-filling-with-masking/7015

---

## Post #1 by @jarrett-rushmore (2019-06-04 01:40 UTC)

<p>Hi Folks,<br>
I was thinking about perfecting a segment between tissues.  Flood filling does a really nice job throughout a volume, but it isn’t perfect due to slight variations in the intensity - too much and it goes into the tissue I don’t want it in, too little and it doesn’t go far enough.<br>
I was thinking I could use flood filling with masking to limit the extent of the fill so it doesn’t go beyond where I want it.  Alternatively, I was thinking of doing the flood filling, then grow the segment, but use a mask to limit the growth to a value I preselect.  The filling and growing work on their own, but when I select the mask, then nothing happens.</p>
<p>Question 1.  Am I doing something obvious wrong?<br>
Question 2.  Is there a work around?  I’ve tried multiple clicking with the flood filling tool, but more often than not, it included more than I would like.</p>
<p>Thanks for any advice,</p>
<p>Jarrett</p>

---

## Post #2 by @lassoan (2019-06-04 02:25 UTC)

<p>We made available “Flood filling” effect so that it can be evaluated and compared to other effects. Results indicate that this effect performs worse than “Grow from seeds effect”, because flood filling cannot cope well with spatially varying image intensity, segmenting multiple objects at once is cumbersome, hard to make incremental adjustments, etc., so there is not much incentive in trying to improve flood filling effect.</p>
<p>In Slicer-4.10.2 and recent preview releases, “Grow from seeds” effect takes masking into account, therefore probably you can achieve what you need. Let us know how it works for you or if you have any questions.</p>

---

## Post #3 by @chir.set (2019-06-04 09:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="7015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We made available “Flood filling” effect so that it can be evaluated and compared to other effects.</p>
</blockquote>
</aside>
<p>Flood filling is perfect for segmenting arteries on contrast enhanced CT angioscan. It saves a lot of time, really, a lot of time, compared to ‘Grow from seeds’ and any other technique. Please keep in extra effects.</p>

---

## Post #4 by @lassoan (2019-06-04 11:05 UTC)

<p>We should see how you use Flood filling and Grow from seeds effects and why the latter takes more time. Let’s do this at the project week!</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #5 by @pieper (2019-06-04 11:27 UTC)

<p>As an alternative to flood filling with masking, I’d suggest thresholding followed by island effects and paint or scissors to cut of links between the vessels and other structures.  I typically find that to be a much more direct approach.</p>
<p>By the way, if people have example data sets and preferred segmentation techniques please post data and screenshots so we can all try various approaches.</p>

---

## Post #6 by @jarrett-rushmore (2019-06-04 12:05 UTC)

<p>This forum is amazing.<br>
Thanks for your lightening-quick replies.</p>
<p>I’m been noodling around with the grow with seeds, and I think this will work very well.  I still like flood filling, and I think it has a lot of good to do in the world.  For the application I had in mind, the Grow from seeds is more powerful and customizable.  I’ll check out the island effects add on too.</p>
<p>Thanks again for all of the input.</p>

---

## Post #7 by @chir.set (2019-06-04 20:06 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="7015" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We should see how you use Flood filling …</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
</blockquote>
</aside>
<p>If this note is open, here is a <a href="https://yadi.sk/d/cp8rsOes2ssaOQ" rel="noopener nofollow ugc">link</a> showing the result of arterial segmentation using Flood Filling only on contrast enhanced CT scan. For normal arteries, and for pathological aorto-iliac segments, it’s just a few clicks away, using Intensity Tolerance between 100 - 250 and Neighbourhood Size of 2. For pathological arteries below the groin, it takes more clicks and adjustments.</p>
<p>In any case, for such convoluted structures, Grow From Seeds will require much painting of outside structures, not feasible in practice.</p>
<p>This, following the contrast media with mouse clicks. This approach is not suitable for structures without contrast, like veins. Surrounding tissues are much of the same or near intensities. Grow From Seeds might better fit the bill here.</p>

---

## Post #8 by @chir.set (2019-06-04 20:10 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="7015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>By the way, if people have example data sets</p>
</blockquote>
</aside>
<p>Well I’ve got a few hundreds of pathological arterial CT angioscans. If you wish a specific type of dataset, I may probably find one of interest to you.</p>

---

## Post #9 by @pieper (2019-06-04 21:02 UTC)

<p>Yes, thank you for sharing those examples <a class="mention" href="/u/chir.set">@chir.set</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">  They are very good examples of challenging segmentation tasks.  In addition to the artifact from the hip replacements, some parts are so stenotic that there’s barely any contrast in some of the vessels.  I’m curious what your goal is for segmenting these.  Are you trying to quantify something about the vasculature?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82b8baa5ee8f72c3d57ce1ffe2d29e5efe48ce9a.jpeg" alt="image" data-base62-sha1="iEpQMQIfFZKYVpR3LnzeWaamCIG" width="427" height="454"></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> you should have a look at those examples if you haven’t already.</p>
<p>Also I should mention that with 4.10.1 when I load the aorto_iliac mrml scene and then switch to the Segment Editor I get a crash with the stack trace below.  It doesn’t happen if I have Segment Editor open when I load the scene.</p>
<pre><code class="lang-auto">Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libvtkCommon-8.2.1.dylib      	0x00000001221d2564 vtkImageData::GetNumberOfScalarComponents() + 4
1   libqSlicerSegmentationsModuleWidgets.dylib	0x000000012dc4009b qMRMLSegmentEditorWidgetPrivate::updateAlignedMasterVolume() + 651
2   libqSlicerSegmentationsModuleWidgets.dylib	0x000000012dc4bf0d qMRMLSegmentEditorWidget::updateVolume(void*, bool&amp;) + 189
3   org.qt-project.QtCore         	0x000000011e78d139 QMetaObject::activate(QObject*, int, int, void**) + 3113
4   libqSlicerSegmentationsEditorEffects.dylib	0x000000012dde9f64 qSlicerSegmentEditorAbstractEffectPrivate::updateVolumeSignal(void*, bool&amp;) + 68
5   libqSlicerSegmentationsEditorEffects.dylib	0x000000012ddcd0ce qSlicerSegmentEditorAbstractEffect::masterVolumeImageData() + 30
6   libqSlicerSegmentationsEditorEffects.dylib	0x000000012dde81a2 qSlicerSegmentEditorAbstractEffect::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 1682
7   libqSlicerSegmentationsEditorEffects.dylib	0x000000012dde955c qSlicerSegmentEditorAbstractEffect::qt_metacall(QMetaObject::Call, int, void**) + 140
8   libqSlicerSegmentationsEditorEffects.dylib	0x000000012ddeac48 qSlicerSegmentEditorScriptedEffect::qt_metacall(QMetaObject::Call, int, void**) + 24
9   libPythonQt.dylib             	0x00000001167eb79b PythonQtCallSlot(PythonQtClassInfo*, QObject*, _object*, bool, PythonQtSlotInfo*, void*, _object**, void**, PythonQtPassThisOwnershipType*) + 1051
10  libPythonQt.dylib             	0x00000001167edbd3 PythonQtSlotFunction_CallImpl(PythonQtClassInfo*, QObject*, PythonQtSlotInfo*, _object*, _object*, void*, void**, PythonQtPassThisOwnershipType*) + 1091
11  libPythonQt.dylib             	0x00000001167ec599 PythonQtMemberFunction_Call(PythonQtSlotInfo*, _object*, _object*, _object*) + 185
12  libpython2.7.dylib            	0x000000011cf6d784 PyObject_Call + 100
13  libpython2.7.dylib            	0x000000011cffa71d PyEval_EvalFrameEx + 29149
14  libpython2.7.dylib            	0x000000011cff31ad PyEval_EvalCodeEx + 1997
15  libpython2.7.dylib            	0x000000011cf9641b function_call + 363
16  libpython2.7.dylib            	0x000000011cf6d784 PyObject_Call + 100
17  libpython2.7.dylib            	0x000000011cf799d5 instancemethod_call + 325
18  libpython2.7.dylib            	0x000000011cf6d784 PyObject_Call + 100
19  libpython2.7.dylib            	0x000000011cfff435 PyEval_CallObjectWithKeywords + 165
20  libqSlicerBaseQTCore.dylib    	0x000000010f014244 qSlicerPythonCppAPI::callMethod(int, _object*) + 196
21  libqSlicerSegmentationsModuleWidgets.dylib	0x000000012dc3f06f qMRMLSegmentEditorWidgetPrivate::notifyEffectsOfMasterVolumeNodeChange() + 175
22  org.qt-project.QtCore         	0x000000011e78d139 QMetaObject::activate(QObject*, int, int, void**) + 3113
23  libqMRMLWidgets.dylib         	0x000000010e9e8d8d qMRMLNodeComboBox::currentNodeChanged(vtkMRMLNode*) + 61
24  libqMRMLWidgets.dylib         	0x000000010e9605b0 qMRMLNodeComboBox::emitCurrentNodeChanged() + 64
25  org.qt-project.QtCore         	0x000000011e78d139 QMetaObject::activate(QObject*, int, int, void**) + 3113
26  org.qt-project.QtWidgets      	0x000000011db9d05b 0x11da79000 + 1196123
</code></pre>

---

## Post #10 by @lassoan (2019-06-04 21:30 UTC)

<p>Masking in Grow from seeds is a game changer. Using that,  marking “other” region is much simpler (and may not be even necessary).</p>
<p>Anyway, if use cases come up that make Flood filling work better than Grow from seeds then we can invest some more time in it. The underlying VTK filter can take a mask, so we could make Flood filling support masking, too. We just have to prioritize developments, because there are a number of other low-hanging fruits in various other effects, too.</p>
<p>I’ve fixed the crash in r28289. It happened because the master volume could not be loaded from the scene (they were DICOM files that were not included in the zip file).</p>

---

## Post #11 by @chir.set (2019-06-05 06:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="7015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m curious what your goal is for segmenting these.</p>
</blockquote>
</aside>
<p>Here it’s only for demonstrative purposes, showing that Flood Filling is an efficient tool of interest.</p>
<p>I do not perform such extensive segmentation on a daily basis. I need it to isolate the blood flow that is not readily analyzable behind heavily calcified walls in Volume Rendering for instance. It’s helpful also for non-vertical arteries, like the iliac, aortic branches or carotid bifurcation.</p>
<p>You are right to show a Volume Rendering image that is a good summary of the flow status, and indeed, that’s my daily tool for surgical planning.</p>

---

## Post #12 by @Amine (2019-06-07 15:01 UTC)

<p>hi, you could use your mask to create a segment then use logical operation&gt;intersect with your flood filled segment to crop everything out of the mask, is that what you’re trying to achieve?</p>

---
