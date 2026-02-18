# Crash reporting?

**Topic ID**: 26390
**Date**: 2022-11-22
**URL**: https://discourse.slicer.org/t/crash-reporting/26390

---

## Post #1 by @Lohi (2022-11-22 21:51 UTC)

<p>Hello all;<br>
being new to this program, I’m not sure where to send crash information, and what to send.<br>
I have saved the main part of the ‘Send to Apple’ crash report, in a text file, if that is useful, and, of course, can save the whole ball of wax, if desirable?</p>

---

## Post #2 by @pieper (2022-11-23 00:49 UTC)

<p>We take crash reports seriously.  The most important thing is to know is how to replicate the issue with public data, so please try to do that and file a bug report with all the details.  If the crash is hard to reproduce, then yes, the crash info can help.  Mostly it’s just the first chunk of 20-30 lines of the stack trace that’s important, but that may be hard to judge so posting it all can’t hurt (put it in a google drive or similar and link here if it’s really big).</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#get-help" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#get-help</a></p>

---

## Post #3 by @Lohi (2022-11-23 21:11 UTC)

<p>The crash file is just 231 K, so I’ll attach it here… I had an ROI-limited 3D of head and C-spine up, from a CTA with 0.5 mm slices.<br>
I was doing a ‘trim’ with scissors tool… hopefully not doing something dumb, but something dumb should tell me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
The images are my own scans (what a mess… sigh…)<br>
anyway, I attach the crash file in ,txt<br>
If you wish to suggest other information, let me know… if the image files are needed, it would be nice to keep them kind of confidential <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>(Attachment DOING SCISSORS EDIT IN 3D Panel copy.txt is missing)</p>

---

## Post #4 by @Lohi (2022-11-23 21:13 UTC)

<p>The system rejected the text file, it’s hard to make it an MP4 <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><br>
Do you use Wetransfer, for example?</p>

---

## Post #5 by @pieper (2022-11-23 21:21 UTC)

<p>Yes, any file transfer service is fine, like dropbox, google drive, onedrive, etc.</p>
<p>Are you using an M series mac by any chance?  We’ve seen issues with random crashes there probably due to the on-the-fly translation so clicking the report to Apple option might help.  I’ve been able to replicate this issue with the SampleData and in this case there doesn’t appear to be much we can do in Slicer since it appears to be an OS / chip level issue.</p>

---

## Post #6 by @Lohi (2022-11-23 22:58 UTC)

<p>OK… I’m using an old MacMini with Mojave 10.14.6</p>
<p>I’ll try wetransfer to<br>
<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a></p>
<p>you should have a notification and link coming to you</p>

---

## Post #7 by @pieper (2022-11-24 01:31 UTC)

<p>I’m not sure you can send to the discourse mail like that with wetransfer (I don’t think anyone gets that email).  If you can make a public download link that will be better.</p>

---

## Post #8 by @Lohi (2022-11-24 08:00 UTC)

<p>let’s see if this works</p>
<p><a href="https://www.dropbox.com/s/hhkq4btt90mlzjr/DOING%20SCISSORS%20EDIT%20IN%203D%20Panel%20copy.txt?dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/s/hhkq4btt90mlzjr/DOING%20SCISSORS%20EDIT%20IN%203D%20Panel%20copy.txt?dl=0</a></p>

---

## Post #9 by @pieper (2022-11-24 09:05 UTC)

<p>Yes, that worked.  This is the key information indicating that something has gone wrong internal to the scissors implementation.</p>
<p>The other key information that’s needed is how to reproduce the crash so it can be debugged and fixed.  Does this happen consistently for you and if so, what steps lead up to it?</p>
<pre><code class="lang-auto">0   libvtkCommon-9.1.1.dylib      	0x000000011c721fdb vtkCellLinks::BuildLinks(vtkDataSet*) + 891
1   libvtkCommon-9.1.1.dylib      	0x000000011c8b2670 vtkPolyData::BuildLinks(int) + 160
2   libvtkFilters-9.1.1.dylib     	0x000000011bd78dce vtkPolyDataNormals::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1614
3   libvtkCommon-9.1.1.dylib      	0x000000011c694015 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*) + 69
4   libvtkCommon-9.1.1.dylib      	0x000000011c68ed5d vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 61
5   libvtkCommon-9.1.1.dylib      	0x000000011c689198 vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 104
6   libvtkCommon-9.1.1.dylib      	0x000000011c68e51d vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1437
7   libvtkCommon-9.1.1.dylib      	0x000000011c6d2990 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 848
8   libvtkCommon-9.1.1.dylib      	0x000000011c68a439 vtkCompositeDataPipeline::ForwardUpstream(vtkInformation*) + 297
9   libvtkCommon-9.1.1.dylib      	0x000000011c68e33d vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 957
10  libvtkCommon-9.1.1.dylib      	0x000000011c6d2990 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 848
11  libvtkCommon-9.1.1.dylib      	0x000000011c6d2f8b vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*) + 283
12  libqSlicerSegmentationsEditorEffects.dylib	0x000000013855eadb qSlicerSegmentEditorScissorsEffectPrivate::updateBrushStencil(qMRMLWidget*) + 203
13  libqSlicerSegmentationsEditorEffects.dylib	0x000000013855ee39 qSlicerSegmentEditorScissorsEffectPrivate::paintApply(qMRMLWidget*) + 137
14  libqSlicerSegmentationsEditorEffects.dylib	0x0000000138562bb0 qSlicerSegmentEditorScissorsEffect::processInteractionEvents(vtkRenderWindowInteractor*, unsigned long, qMRMLWidget*) + 448
15  libqSlicerSegmentationsModuleWidgets.dylib	0x000000013841b75b qMRMLSegmentEditorWidget::processEvents(vtkObject*, unsigned long, void*, void*) + 619
16  libvtkCommon-9.1.1.dylib      	0x000000011ce6dff1 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
17
</code></pre>

---

## Post #10 by @Lohi (2022-11-24 10:53 UTC)

<p>hello…good to know that it’s pointing to something … I’m not in very good shape today (CSF leak(s)) but I’ll try to light up the slicer, and reproduce the problem.<br>
the files are my scans, but i can also try with a sample set.</p>

---

## Post #11 by @pieper (2022-11-27 07:19 UTC)

<aside class="quote no-group" data-username="Lohi" data-post="6" data-topic="26390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b782af/48.png" class="avatar"> Lohi:</div>
<blockquote>
<p>OK… I’m using an old MacMini with Mojave 10.14.6</p>
</blockquote>
</aside>
<p>Can you confirm that your mac mini has an intel chip?  I.e. is it before <a href="https://en.wikipedia.org/wiki/Mac_Mini#Fifth_generation_(Apple_silicon)">the M1</a> versions were introduced?  I ask because I’ve only seen this particular crash on Apple silicon and not with intel.</p>

---

## Post #12 by @Lohi (2022-11-27 09:28 UTC)

<p>yes, Steve, it’s an i5 2.3 GHz.<br>
late 2012, Mojave 10.14.6</p>
<p>I’m having trouble getting to approximately the same 'state’s, being as lost as I am in the application. : -(</p>
<p>i can’t seem to get to a point where scissors work on the 3d image, or <em>anywhere</em>, for that matter… it’s frustrating, that a tool that is so obviously powerful, and graphically ‘pleasing’, is so driven by some “other appreciation” of User Experience (user experience is something that i have real-world experience with, in both 'consumer’s and ‘engineering’ fields, with <em>extremely</em> complex instruments )… i really can’t spend months to accomplish even seemingly-simple tasks, in the midst of attempting to get to some understanding of a combination of CSF leak, apparent VBI of unknown aetiology, but both apparently connected to Cervical spine (truly a mess on MR and CT!)<br>
I’ll keep plugging away at it…</p>
<p>btw, is there any simple way to ‘translate’ the 3d object? there are ‘buttons’ to rock it, or spin it, but no readily-apparent mouse mode to move the object in the viewport’s x/y? Surely it’s just one more ‘beginner missing something obvious’!<br>
the entire 'segmentation thing’s is also killing me…sorry, folks…</p>
<p>it’s a beautiful Sunday morning, first day of Advent, Christmas markets open … maybe time for Glühwein instead of C-spine!</p>
<p>freundlichen Grüßen</p>

---

## Post #13 by @pieper (2022-11-27 10:46 UTC)

<p>Thanks for reporting back <a class="mention" href="/u/lohi">@Lohi</a> - the fact that you get the same stack trace on an intel mac as I see on the M2 mac, but isn’t seen on windows/linux, indicates perhaps it’s something to do with the Apple compilers or something else to be determined.  Hopefully with more debugging we’ll get to the bottom of it. Please try <a href="https://discourse.slicer.org/t/slicer-program-crash-suddenly-in-macbook/26453/2">these instructions</a> for capturing the program state so you can share it if a crash occurs.</p>
<p>And yes, Slicer is a UI/UX minefield.  Just so you know, we have limited developer resources so we draw an arbitrary line and say that any hardware over 5 years old should be considered unsupported, so your 10 year old mac mini is way out of spec for current Slicer.  Still, we’d like it to work anyway and it’s helpful for debugging, but it may never be usable with the latest releases.  A newer computer might save you some frustration.</p>
<p>Regarding translating the object (or for Slicer, the camera) on a mac with a trackpad you press shift and then use the trackpad click-and-drag motion.  A three-button mouse is highly recommended if you are doing a lot of interactive visualization and segmentation.</p>

---

## Post #14 by @Lohi (2022-11-27 12:12 UTC)

<p>thanks, Steve;</p>
<p>i do understand about “resource limitations”…</p>
<p>I’ve not ‘updated’ my Mac mini, because later versions had more restrictions on expansion, and it seems that Apple has made the newest ones kind of 'what you buy is. what you’really stuck witch’s, as far as RAM, although i guess drives can be changed. I’m thinking seriously about going to Linux, at some point, but my ‘newer’ i7 Mac still has enough performance for most of what zip do.<br>
i thought that i had tried every combination of keys to get translation, but ‘shift’, maybe not.<br>
i noticed some kind of debug thing in preferences, turned it on.</p>
<p>thanks!</p>

---
