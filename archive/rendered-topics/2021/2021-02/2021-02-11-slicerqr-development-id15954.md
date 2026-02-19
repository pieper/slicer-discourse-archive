---
topic_id: 15954
title: "Slicerqr Development"
date: 2021-02-11
url: https://discourse.slicer.org/t/15954
---

# SlicerQR Development

**Topic ID**: 15954
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/slicerqr-development/15954

---

## Post #1 by @spycolyf (2021-02-11 15:59 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/superlib">@superlib</a></p>
<p>Good Morning. I’m starting to think about how to deploy SlicerQR to 25,000 PCs across the Mayo Enterprise. After building the package, it consists of over 7000 files at a total size of over 700MB. It would be seriously frowned-upon to propose deploying it to 25,000 PCs. So, my question is: Would there be any disadvantages to placing the installation in 1 place on a file share and have the users execute SlicerQR from a folder there? Would there be conflicts with sharing? Once the app is loaded into local memory, what are potential problems with a common launch path?</p>

---

## Post #2 by @lassoan (2021-06-08 17:51 UTC)

<p>38 posts were split to a new topic: <a href="/t/slicer-custom-application-deployment-to-many-computers/18019">Slicer custom application deployment to many computers</a></p>

---

## Post #22 by @spycolyf (2021-02-19 17:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a></p>
<p>Question: Do any of you know my friend, Hunter Downs?</p>

---

## Post #41 by @spycolyf (2021-02-24 20:59 UTC)

<p>Question: Do you all do anything with A.I. in imaging?</p>

---

## Post #42 by @lassoan (2021-02-25 06:28 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="38" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"><a href="https://discourse.slicer.org/t/slicer-custom-application-deployment-to-many-computers/18019/38">Slicer custom application deployment to many computers</a></div>
<blockquote>
<p>might I be able to get the size down significantly smaller than 300MB? Sankhesh’s 2018 FourPanesViewer app was has a total size of 60MB and had similar functionality.</p>
</blockquote>
</aside>
<p>The FourPanesViewer is pure VTK. It has no GUI widgets, no proper DICOM parser, no proper widgets, etc. The Slicer core will not be significantly smaller than 300MB just by removing DLLs, but you would need to reengineer the application. Since 300MB is smaller than a typical image that the user downloads by the dozens and you don’t actually need to deploy the 300MB Slicer, only a 10MB launcher, the effort for reengineering (and maintain the ultra-lean Slicer core) is very hard to justify.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="41" data-topic="15954" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Question: Do you all do anything with A.I. in imaging?</p>
</blockquote>
</aside>
<p>Yes, AI is a very trendy topic, so there is lots of activity around it in the Slicer community, too. This is a good example of why creating an ultra-lean Slicer core would not worth the effort: users would keep asking for enabling features and we would end up using the full Slicer core quite quickly.</p>

---

## Post #43 by @spycolyf (2021-02-25 16:40 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I know I’m flooding you with questions here. Here’s more…</p>
<ol>
<li>
<p>What are you using for DICOM parsing. In FourPanesViewer, I am using David Gobbi’s vtkDICOM functions to parse DICOM. I think Gobbi’s objects have been integrated into VTK installations in VTK 9.</p>
</li>
<li>
<p>I’m also using GDCM for JPEG 2000 decompressing. Does Slicer handle JPED 2000 compression? If so, how? I’m still diving into the code, and it helps to know what to look for.</p>
</li>
</ol>
<p>Thanks</p>

---

## Post #44 by @lassoan (2021-02-25 16:44 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="43" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>What are you using for DICOM parsing. In FourPanesViewer, I am using David Gobbi’s vtkDICOM functions to parse DICOM. I think Gobbi’s objects have been integrated into VTK installations in VTK 9</p>
</blockquote>
</aside>
<p>vtkDICOM can handle basic DICOM - 3D Cartesian volumes with uniform spacing. No 2D+t, no 3D+t, no DICOM segmentation objects, no DICOM RT structure sets, etc. It cannot handle some of the technically valid but tricky series (such as overview orthogonal slice embedded in the series; series that contain slices with multiple orientations, …). You cannot rely on this if user may want to be able to open images acquired with a variety of devices, using a variety of imaging protocols.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="43" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I’m also using GDCM for JPEG 2000 decompressing. Does Slicer handle JPED 2000 compression? If so, how?</p>
</blockquote>
</aside>
<p>Yes, Slicer uses GDCM and DCMTK, both can handle compressed DICOM images. Not all compression types are supported (for example, h264 video compression is not), but jpeg is, and I think jpeg2000, too.</p>

---

## Post #45 by @spycolyf (2021-02-25 22:22 UTC)

<p>Wow, that’s great to know about vtkDICOM. I was really going in the wrong direction. Y’all saved my life. Thanks.</p>
<p>I might be mistaking, but I’m under the impression that DCMTK does not handle JPEG 2000 compression. If so, it a recent development. Liqin wrote our QREADS DICOM receiver and is now using GDCM because DCMTK either did not do JPEG 2000, or there were issues with it.</p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #46 by @spycolyf (2021-02-25 22:31 UTC)

<p>Also, I did inform my team that the smallest size we might could possibly achieve is around 300MB. So, we will come up with a deployment scheme that will work. When I suggested the possibility of SlicerQREADS (SQR) staying up in the background once launched, the concern was what if QREADS it terminated and SQR becomes orphaned? Obviously, SQR would need to detect QREADS PID presence at some short interval when SQR is not in focus. The QREADS PID would be passed as an argument to SQR upon launching.</p>

---

## Post #47 by @spycolyf (2021-02-26 00:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> - Question: As you know, building SlicerQREADS can take hours. I know if I make changes to the Python script, I don’t have to rebuild. But do I need to perform the 3 hour rebuild if I make a small modification to the C++ code?</p>

---

## Post #48 by @lassoan (2021-02-26 03:53 UTC)

<p>You only need a full build once. After you make modifications in the C++ source files and build again then only the changed files are compiled and linked, which typically takes about 15-30 seconds.</p>

---

## Post #49 by @lassoan (2021-02-26 04:20 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="45" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I’m under the impression that DCMTK does not handle JPEG 2000</p>
</blockquote>
</aside>
<p>DCMTK tried to make some income from not bundling JPEG2000 codec with the free DCMTK version. Slicer falls back to read with GDCM if DCMTK fails to decode an image.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="46" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>the concern was what if QREADS it terminated and SQR becomes orphaned?</p>
</blockquote>
</aside>
<p>There are many options for solving this, but checking if QR process is running (based on PID) would be an easy way of doing it.</p>

---

## Post #50 by @spycolyf (2021-02-26 15:21 UTC)

<p>OK, great! Can the incremental build be done from the command line as well as in the VS IDE?</p>

---

## Post #51 by @spycolyf (2021-02-26 15:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Could any of you please describe your Slicer development environment to us. Do you use a text editor for Python, or an IDE? PythonQT? I’m sure you use Visual Studio. What is the proper development environment for us here at Mayo. We need to rapidly ramp up to start developing.</p>
<p>Most urgent id to eliminate the Kitware splashes and brightening the colors of the cross reference markers on the images.</p>

---

## Post #52 by @spycolyf (2021-02-26 18:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>OK, I’m finally starting to understand. I know you’ve been trying to tell me many time in the past, it’s mostly about the Python! OK, I’m looking for the python code for the following:</p>
<ol>
<li>To set the colors of the reference markers on my four image panes.</li>
<li>Eliminate the Kitware splashes upon launching</li>
<li>Perform window / level interactively with the left and right mouse button pressed and dragging.</li>
</ol>
<p>Thanks,</p>
<p>Doug Porter</p>

---

## Post #53 by @jamesobutler (2021-02-26 20:01 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="52" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>To set the colors of the reference markers on my four image panes.</p>
</blockquote>
</aside>
<p>Can you provide an image of what you mean here? I’m not sure which object you are talking about.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="52" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Eliminate the Kitware splashes upon launching</p>
</blockquote>
</aside>
<p>Are you using the Slicer Custom App framework? There is an example of such a customized Slicer application at <a href="https://github.com/KitwareMedical/SlicerCAT" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerCAT</a>. Included things is changing the logos used in the application and the splash screen. You would update the images files as are specified at <a href="https://github.com/KitwareMedical/SlicerCAT/tree/master/Applications/SlicerCATApp/Resources/Images" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerCAT/tree/master/Applications/SlicerCATApp/Resources/Images</a>.</p>

---

## Post #54 by @spycolyf (2021-02-26 22:47 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Thank you <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. Pleased to meet you. Yes, I am using the Slicer Custom App framework, here is a picture of what I mean by reference markers. Also, I need to lighten up the background colors of the textboxes containing the slice locations in the upper right corner of each image pane. Or better still, make the text white.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d2bd8763d7f618d09a2d7dc3bb84b39b7417a0.jpeg" data-download-href="/uploads/short-url/oYsLOEKqS38UkdhS56Vgg8bnLW.jpeg?dl=1" title="SlycerQREADS_RefMarkers" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02d2bd8763d7f618d09a2d7dc3bb84b39b7417a0_2_464x500.jpeg" alt="SlycerQREADS_RefMarkers" data-base62-sha1="oYsLOEKqS38UkdhS56Vgg8bnLW" width="464" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02d2bd8763d7f618d09a2d7dc3bb84b39b7417a0_2_464x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d2bd8763d7f618d09a2d7dc3bb84b39b7417a0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d2bd8763d7f618d09a2d7dc3bb84b39b7417a0.jpeg 2x" data-dominant-color="535352"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlycerQREADS_RefMarkers</span><span class="informations">501×539 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My managers are saying that the reference markers are too dark and are sometimes difficult to see. I’m just learning how to program Slicer. Here is the Python code that creates the reference markers…</p>
<p>Here’s some code setting them visible. Is there a reference manual somewhere, or a way to discover available Slicer methods for certain objects? Is there an IDE with intellisense?</p>
<pre><code class="lang-python">  def setReferenceMarkersVisible(visible):
         for sliceLogic in slicer.app.applicationLogic().GetSliceLogics():
              sliceLogic.GetSliceCompositeNode().SetSliceIntersectionVisibility(visible)
              sliceLogic.GetSliceNode().SetWidgetVisible(visible)
</code></pre>

---

## Post #55 by @jamesobutler (2021-02-27 00:08 UTC)

<p>Ok I see. The slice controller area of the slice views. Have you registered a custom layout in that image there (as in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout" rel="noopener nofollow ugc">customize view layout</a>)? That’s how a custom layout can be created which allows you to specify different colors for the slice viewers. I’m not aware of a a specific layout view that looks like that in the latest versions of Slicer.</p>
<p>As it relates to python autocomplete you can see the state of things from this older thread. Note that I really haven’t tried it any further. As it relates to figuring what methods are supported by various objects I often use the python interactor in slicer and just use tab completion to look into the available methods. So like volume_node.[PRESS TAB].</p><aside class="quote quote-modified" data-post="12" data-topic="9496">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496/12">Developing Slicer modules in Visual Studio / Visual Studio Code?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I was able to get auto completion within Visual Studio Code on Windows following these settings: 
“C:\Users\JamesButler\AppData\Roaming\Code\User\settings.json” 
{
    "python.pythonPath": "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\bin\\SlicerPython",
    "python.autoComplete.extraPaths": [
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\",
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\lib\\Python",
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\lib\\QtPlugins",
        "…
  </blockquote>
</aside>

<p>Some further python debugging content can be found linked from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html?highlight=python%20interactor#debugging-python-scripts" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html?highlight=python%20interactor#debugging-python-scripts</a>.</p>

---

## Post #56 by @jcfr (2021-02-27 00:21 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="55" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Ok I see. The slice controller area of the slice views. Have you registered a custom layout in that image there […]?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>  custom layout is indeed registered</p>
<p><a class="mention" href="/u/spycolyf">@spycolyf</a> The color are consistent with the original design you shared with me. Which colors should be used instead ? Providing the hexadecimal code for each colors would be ideal.</p>

---

## Post #57 by @spycolyf (2021-03-01 15:29 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thanks everyone for your extremely helpful responses. I’ll responding in more detail when I return from my tax appointment in about an hour. But here’s my immediate answer to <a class="mention" href="/u/jcfr">@jcfr</a> 's question. Same colors, but lighter. I will send the hex shortly. Question though: can the reference marker line colors be adjusted independently of the image background colors? Id like the background colors to remain the same, but the ref line colors to be brighter which corresponds to the 3D graphics boundary lines in the lower right quadrant. If not independent I will pick the best overall color. Thanks.</p>

---

## Post #58 by @spycolyf (2021-03-01 15:35 UTC)

<p>… also, in case you’re wondering how to pronounce “spycolyf,” it’s “spice o’ life,” and it’s the business name of my music production company." I don’t remember how the use of that name happened, but that’s the way it turned out somehow. Thanks.</p>

---

## Post #59 by @spycolyf (2021-03-01 18:42 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="56" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>The color are consistent with the original design you shared with me. Which colors should be used instead ? Providing the hexadecimal code for each colors would be ideal.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>What are your current 3 color hex values? I want to try 990000, 009900 and 000099. Just brighter colors than current. Image background colors are fine. I’ll update the tasks on GitHub. Here is how the current Red and Green lines appear zoomed up in Photo Shop. I wonder how it’s being interpolated. Maybe a little exclusive or’ing going on? When I samle the pixel colors, it’s mostly dark gray.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d48ffbdf1683772af78f698f2b02a81d58ec8bcc.jpeg" alt="Current lines on the image" data-base62-sha1="ukpHSD12lqubS3dIey4YhqxHBes" width="132" height="92"></p>

---

## Post #60 by @jcfr (2021-03-01 18:45 UTC)

<p>For reference, here are the comment I directly shared by email few days ago:</p>
<blockquote>
<blockquote>
<ol>
<li>To set the colors of the reference markers on my four image panes.</li>
</ol>
</blockquote>
</blockquote>
<blockquote>
<p>To follow up on this thread <a href="https://discourse.slicer.org/t/slicerqr-development/15954/54" class="inline-onebox">SlicerQR Development - #54 by spycolyf</a></p>
<p>These are currently set here:</p>
<p><a href="https://github.com/KitwareMedical/SlicerQReads/blob/52e84ddc4c6d637f72b350c7061aad693f430f28/Modules/Scripted/QReads/QReads.py#L336-L344" class="inline-onebox">SlicerQReads/Modules/Scripted/QReads/QReads.py at 52e84ddc4c6d637f72b350c7061aad693f430f28 · KitwareMedical/SlicerQReads · GitHub</a></p>
<p>Note that the string “Red”, “Yellow” and “Green” are used to identify each viewer and do not define the<br>
colors. The colors are defined using the hexadecimal code.</p>
<p>Which color should we use ?</p>
</blockquote>

---

## Post #61 by @spycolyf (2021-03-01 19:12 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="60" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>These are currently set here:</p>
<p><a href="https://github.com/KitwareMedical/SlicerQReads/blob/52e84ddc4c6d637f72b350c7061aad693f430f28/Modules/Scripted/QReads/QReads.py#L336-L344" rel="noopener nofollow ugc">SlicerQReads/QReads.py at 52e84ddc4c6d637f72b350c7061aad693f430f28 · KitwareMedical/SlicerQReads · GitHub</a></p>
</blockquote>
</aside>
<p>OK, then it seems the reference line colors are the same as the background colors. I’ll try this in practice, Is there an easy way to set the slice loc text colors to white?</p>

---

## Post #62 by @jcfr (2021-03-01 19:21 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="61" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>it seems the reference line colors are the same as the background colors</p>
</blockquote>
</aside>
<p>Reference lines and background color can be set independently.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="61" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>slice loc text colors to white?</p>
</blockquote>
</aside>
<p>Yes, every aspect can be customized. It should be possible to set this updating the Qt stylesheet.</p>

---

## Post #63 by @spycolyf (2021-03-01 19:39 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> - OK, Style sheet I can do. I tried changing the 3 lines you referenced in QREADS.py, but that’s for slice view background. I liked the original for those because dark is less distracting from the images. So, how do I change the line colors independently?</p>
<pre><code class="lang-python">  SLICEVIEW_BACKGROUND_COLORS = {
    "Red": "#990000",
    "Yellow": "#009900",
    "Green": "#000099"
  }
</code></pre>

---

## Post #64 by @spycolyf (2021-03-01 19:42 UTC)

<p>… also, at the moment, we don’t want the “save scene” prompt on close. Physicians here seem to hate prompts and prefer as little as possible.</p>
<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #65 by @spycolyf (2021-03-01 20:19 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> - Hello JC, Liqin did the new build and it seems SlicerQREADS is still looking for the splash screen. And crashes.  How do we fix this?</p>

---

## Post #66 by @lassoan (2021-03-01 23:46 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="64" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>… also, at the moment, we don’t want the “save scene” prompt on close. Physicians here seem to hate prompts and prefer as little as possible.</p>
</blockquote>
</aside>
<p>See how to customize exit confirmation in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Override_application_close_behavior">script repository</a>.</p>

---

## Post #67 by @spycolyf (2021-03-02 16:56 UTC)

<p>Hello, I’ve been testing launching SlicerQREADS from QREADS and I think it has an acceptable launch speed which will improve a lot after we get rid of the splash screens.</p>
<p>However, it does not seem to be able to handle our image folder paths. For example, “C:\Abcdef\Ghijkl\Mnopqrstu\Vwxyz_12345\1.3.12.2.1107.5.8.15.101834.30000020080812425097400002372\27”. Why is this a problem? It was not a problem with FourPanesViewer.</p>
<p>When I move the data to a folder such as c:\TextImages, it works fine.</p>

---

## Post #68 by @spycolyf (2021-03-02 17:43 UTC)

<p>Found a case where the orientation is incorrect. Here are the test images: <a href="https://www.dropbox.com/s/tun2gklwoiqkbrs/BadOrientation.zip?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - BadOrientation.zip - Simplify your life</a></p>
<p>The coronals are upside down and the superior orientation is still pointing up. Any Ideas?</p>

---

## Post #69 by @pieper (2021-03-02 18:13 UTC)

<p>I had a quick look and that is DICOM Secondary Capture format (screen dump) so geometry is often not well preserved.</p>
<p>In this case it loads correctly via the DICOM module but incorrectly with the regular Add Data.  We always recommend the DICOM module for data that is known to be in DICOM format.</p>

---

## Post #70 by @spycolyf (2021-03-02 18:24 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="67" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>However, it does not seem to be able to handle our image folder paths. For example, “C:\Abcdef\Ghijkl\Mnopqrstu\Vwxyz_12345\1.3.12.2.1107.5.8.15.101834.300000200808124250974000</p>
</blockquote>
</aside>
<p>OK, I found the problem here. Folders cannot begin with a number</p>

---

## Post #71 by @pieper (2021-03-02 18:27 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="68" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Here are the test images: <a href="https://www.dropbox.com/s/tun2gklwoiqkbrs/BadOrientation.zip?dl=0">Dropbox - BadOrientation.zip</a></p>
</blockquote>
</aside>
<p>By the way for anyone else that looks, <a class="mention" href="/u/spycolyf">@spycolyf</a> confirms that this is a test patient, not PHI.</p>

---

## Post #72 by @spycolyf (2021-03-02 18:28 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="68" data-topic="15954" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Found a case where the orientation is incorrect. Here are the test images: <a href="https://www.dropbox.com/s/tun2gklwoiqkbrs/BadOrientation.zip?dl=0" rel="noopener nofollow ugc">Dropbox - BadOrientation.zip - Simplify your life</a></p>
<p>The coronals are upside down and the superior orientation is still pointing up. Any Ideas?</p>
</blockquote>
</aside>
<p>Not to worry, no PHI here, it’s a test patient from our QREADS test server.</p>

---

## Post #73 by @spycolyf (2021-03-02 21:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="69" data-topic="15954" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I had a quick look and that is DICOM Secondary Capture format (screen dump) so geometry is often not well preserved.</p>
<p>In this case it loads correctly via the DICOM module but incorrectly with the regular Add Data. We always recommend the DICOM module for data that is known to be in DICOM format.</p>
</blockquote>
</aside>
<p>Oh that’s great Steve. So the data orientation is not properly reflected in the direction cosines and other orientation header values?</p>
<p>But, I loaded the data in another DICOM viewer called Weasis and the orientation is correct.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b8bdd83387d75ee1c028643d575b56d4f1a00b6.jpeg" data-download-href="/uploads/short-url/hCWo6KARRRmX6FaY8wZwTgPVjpQ.jpeg?dl=1" title="SlicerQROrientationWrong" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b8bdd83387d75ee1c028643d575b56d4f1a00b6_2_634x500.jpeg" alt="SlicerQROrientationWrong" data-base62-sha1="hCWo6KARRRmX6FaY8wZwTgPVjpQ" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b8bdd83387d75ee1c028643d575b56d4f1a00b6_2_634x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b8bdd83387d75ee1c028643d575b56d4f1a00b6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b8bdd83387d75ee1c028643d575b56d4f1a00b6.jpeg 2x" data-dominant-color="676665"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerQROrientationWrong</span><span class="informations">873×688 96.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68df47c9abf7c6b17156b68603fae7e6a6fa0b78.jpeg" data-download-href="/uploads/short-url/eXK22WbiKzod4pyFasEzmxHsyKs.jpeg?dl=1" title="Weasis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68df47c9abf7c6b17156b68603fae7e6a6fa0b78_2_515x500.jpeg" alt="Weasis" data-base62-sha1="eXK22WbiKzod4pyFasEzmxHsyKs" width="515" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68df47c9abf7c6b17156b68603fae7e6a6fa0b78_2_515x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68df47c9abf7c6b17156b68603fae7e6a6fa0b78_2_772x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68df47c9abf7c6b17156b68603fae7e6a6fa0b78.jpeg 2x" data-dominant-color="383734"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Weasis</span><span class="informations">870×844 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #74 by @pieper (2021-03-02 21:48 UTC)

<p>There is position and orientation info available per-slice, and Slicer’s DICOMScalarVolumePlugin is parsing it correctly to form the same view as you see in Weasis.  If you go through the Add Data module then the data is sent down to ITK for loading.  It could be that because this particular data is a Secondary Capture, where orientation and spacing are optional, that ITK ignores the fields and use some other ordering logic.  It might make sense to debug this with native ITK to see if this interpretation is correct.</p>
<p>In any case this particular dataset is probably not representative of real clinical datasets.  But it does illustrate that testing with real data is important. By default Slicer defaults to ‘best efforts’ at loading data that is not well defined (e.g. is not fully conformant with the standard), but you may or may not want to that tighten up, depending on your data and the user expectations.</p>

---

## Post #75 by @spycolyf (2021-03-03 16:18 UTC)

<p>Thanks Steve,</p>
<p>I will relay this to my team.</p>

---

## Post #76 by @spycolyf (2021-03-03 16:24 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>As you can see in the picture the reference lines are much more visible as compared to pictures I sent earlier in this thread. But, I need the background to stay dark. How can I set the reference lines colors separate from the image background colors?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b048ab7b87dc54d3d67ceb5dfb7a0ab683c2103.jpeg" data-download-href="/uploads/short-url/1zsYWWVKsJcOM94tO9888YgKpeH.jpeg?dl=1" title="SlicerQRBrighterReferenceMarkers" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b048ab7b87dc54d3d67ceb5dfb7a0ab683c2103_2_452x500.jpeg" alt="SlicerQRBrighterReferenceMarkers" data-base62-sha1="1zsYWWVKsJcOM94tO9888YgKpeH" width="452" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b048ab7b87dc54d3d67ceb5dfb7a0ab683c2103_2_452x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b048ab7b87dc54d3d67ceb5dfb7a0ab683c2103.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b048ab7b87dc54d3d67ceb5dfb7a0ab683c2103.jpeg 2x" data-dominant-color="2D302F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerQRBrighterReferenceMarkers</span><span class="informations">614×678 68.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #77 by @spycolyf (2021-03-05 01:36 UTC)

<aside class="quote no-group" data-username="pieper" data-post="74" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It could be that because this particular data is a Secondary Capture, where orientation and spacing are optional, that ITK ignores the fields and use some other ordering logic. It might make sense to debug this with native ITK to see if this interpretation is correct.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Hello <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Could you share with me why you determined this to be secondary capture data?  I’m afraid that most of our volumes except for the Head/Neck process where to sagittals and coronals get vertically flipped  as if the axial slices are read (or stored) in reverse order. That makes this wonderful product unusable. I really hate to see this happen. Is this a known issue and could fixing it help others?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffc54888c767618a5f8b08ce96ad0defa0b0d242.jpeg" data-download-href="/uploads/short-url/AuEqOMjlYlwxx5ageYSqQmUUng6.jpeg?dl=1" title="SlicerQROrientationWrong" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffc54888c767618a5f8b08ce96ad0defa0b0d242_2_480x500.jpeg" alt="SlicerQROrientationWrong" data-base62-sha1="AuEqOMjlYlwxx5ageYSqQmUUng6" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffc54888c767618a5f8b08ce96ad0defa0b0d242_2_480x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffc54888c767618a5f8b08ce96ad0defa0b0d242.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffc54888c767618a5f8b08ce96ad0defa0b0d242.jpeg 2x" data-dominant-color="1C1D16"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerQROrientationWrong</span><span class="informations">696×725 37.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, are you referring to any of these DICOM elements being wrong?</p>
<p>(0018,5100) - Patient Position : FFS<br>
(0020,0032) - Image Position (Patient) : -249.5-369.5-80.7<br>
(0020,0037) - Image Orientation (Patient) : 1\0\0\0\1\0</p>
<p>I’m just curious, how are you calculating the Z direction. I vaguely remember when I developed Mayo Image Studio, I think I calculated single frame spacing between slices by the difference between consecutive slices’ Image Position (patient) vectors, or the difference between consecutive slices’ slice locations and the sign of the differences gave me a positive of negative z direction. I don’t remember exactly. I never trusted the Patient Position element. Seemed to work fine I think.</p>
<p>But clearly the slices are ordered head-first in SlicerQREADS. I’m probably wrong though.</p>
<p>Please lets nail this down. Luckily I demoed only Head-Neck and the orientation was correct.</p>
<p>Thanks.</p>

---

## Post #78 by @lassoan (2021-03-05 02:53 UTC)

<p>The DICOM module must be used for loading DICOM images. It works well. It does not have this inage flipping issue.</p>
<p>We have not explicitly disabled ITK’s DICOM reader, but we know that it does not work well and it must not be used clinically. ITK’s DICOM reader works better when it assembles the file list by itself (instead of getting it from Slicer), but we don’t plan to investigate this much further, because the DICOM module is a much more feature-complete and robust solution anyway.</p>

---

## Post #79 by @spycolyf (2021-03-05 15:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Ok, you’ve stated the problem, but I’m still not clear on the solution. I’m just getting started with knowing the Python. I have a little experience with ITK about 16 years ago when I was creating Mayo Image Studio, but I emphasize “little.”</p>
<p>This is urgent because, the reason I switched to Slicer was because of the orientation issues of vtkSlicerImageViewer; that’s also the reason I gave my Mayo colleagues for switching to this awesome Slicer tool kit that gets the orientations correct so I don’t have to worry about it. So, this would be a show stopper in more that one way. The 2nd way is since this is my last hoorah before retirement, if I cannot get this done, I’ll probably retire sooner. This is very important to me. I will either leave my career a hero, or and failure. Just being truthful here. Please forgive me for being so drastic and dramatic. I lost sleep over this and I’m just venting</p>
<p>So, what do we do in very practical cookbook steps? Remove ITK? Do we need it? Do we send the images unsorted to ITK and let it do the ordering? And what is the code for doing this? Maybe I could reorder the slices in QREADS before I send them to Slicer, but which DICOM header elements would give me the hint that these series would be a problem and need header changes or reordering.</p>
<p>Again, my apologies for expressing this urgency. This is probably unusual for your amazing team and I’m sure you’ll help come up with the right solution.</p>

---

## Post #80 by @jcfr (2021-03-05 16:31 UTC)

<blockquote>
<p>I’m still not clear on the solution</p>
</blockquote>
<p><a class="mention" href="/u/spycolyf">@spycolyf</a> Since data are properly handled using the Slicer DICOM module (instead of directly loading the series using ITK based reader), all building blocks are available.</p>
<p>Mentioning this to your team is sensible I think.</p>
<p>Considering that the demo dataset initially shared was properly oriented using the <code>Add Data...</code> approach, in the interest of time the SlicerQReads prototype was built using this.</p>
<p>Now that we identified datasets that are incorrectly loaded using this approach, it makes sense to leverage the <code>Slicer DICOM</code> module.</p>
<p>I will submit a pull request with a draft implementation.</p>
<p>That said, more work will be needed to:</p>
<ul>
<li>report error in the context of your custom application</li>
<li>decide if exposing the DICOM browser is relevant or not</li>
<li>come with a cleanup strategy for the local DICOM database</li>
</ul>
<p>This is why graduating <code>SlicerQReads</code> from a prototype created in less than a week to an application associated with a maintenance plan will be critical.</p>
<p>The <code>Add Data ...</code> approach corresponds to the one labeled as " Non-DICOM data" in the documentation. As a shortcut and to avoid integrating with the Slicer DICOM database, we decided to use this approach. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="inline-onebox">Data Loading and Saving — 3D Slicer documentation</a></p>

---

## Post #81 by @spycolyf (2021-03-05 17:04 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>OK, I will explain to tell my colleagues that this is a bug that will be fixed.</p>

---

## Post #82 by @lassoan (2021-03-05 17:11 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="80" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>come with a cleanup strategy for the local DICOM database</p>
</blockquote>
</aside>
<p>Certain DICOM objects (e.g., structured reports, segmentation objects, RT structure sets) only make sense when associated series are in the database as well. So, I would recommend to clean the database when review of a new patient is started.</p>
<p>The fastest and most complete cleanup is creation of a new database folder (and removal of the previous one).</p>
<p>If reading of 4D (3D+t) data sets are not needed then the MultiVolume plugin can be disabled, to make Examine faster.</p>

---

## Post #83 by @spycolyf (2021-03-05 18:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>I forgot to mention that I have until the end of March to finish the implementation / coding phase and then testing starts. Is this accomplishable? I will update the tasks in GitHub. Thanks.</p>

---

## Post #84 by @pieper (2021-03-05 19:15 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="77" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Could you share with me why you determined this to be secondary capture data?</p>
</blockquote>
</aside>
<p>You can right-click on the study in the DICOM module to see the headers and confirm this is a secondary capture of some kind, not an image right off the scanner.  I’m not completely clear on what QREADS is meant to support, but in my experience it’s much more common for CT scans to be reviewed from the original axials, not from a secondary capture.  Is it correct that these secondary captures are merely testing data or do the represent the actual use case for QREADS?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7833329b1285625c29a8722b5d99f26ffe61f6.png" data-download-href="/uploads/short-url/mBSXZxQGAQphUnEmsgDPg69rEwu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e7833329b1285625c29a8722b5d99f26ffe61f6_2_687x500.png" alt="image" data-base62-sha1="mBSXZxQGAQphUnEmsgDPg69rEwu" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e7833329b1285625c29a8722b5d99f26ffe61f6_2_687x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7833329b1285625c29a8722b5d99f26ffe61f6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7833329b1285625c29a8722b5d99f26ffe61f6.png 2x" data-dominant-color="EAEBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">978×711 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In any case, it seems Andras, Jc, and I all agree that you should be routing the data through the dicom database so that Slicer can detect and hopefully fix any anomalies.</p>
<p>I’ll reiterate that the app should be heavily tested against the real expected data before deployment.</p>

---

## Post #85 by @spycolyf (2021-03-08 16:28 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<p>Yes, I was going to get around to studying the header. But I did notice that it was not reflected in the SOPClassUID. And it is an 8 bit secondary capture, i.e. pixels per sample = 1.</p>

---

## Post #86 by @spycolyf (2021-03-08 16:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Do you think this is something that can be corrected this week? The Med school needs to use this in new student orientation on March 30th, and there is a lot of implementation and testing work that I need to do with SlicerQREADS deployment. I plan on implementing a quick and dirty on-demand SlicerQREADS extension deployment for the students in the March 30th orientation. But it is critical that the orientation is not worse than the Sankhesh’s FourPaneViewer used for the past 2 years.</p>

---

## Post #87 by @spycolyf (2021-03-08 16:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Question: Management is asking if multiple SlicerQREADS instances can be launched for comparing 2 different series.</p>
<p>Thanks</p>

---

## Post #88 by @pieper (2021-03-08 16:44 UTC)

<p>If you load your data like this it should work for this data:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder</a></p>
<p>(But I also still maintain this data is very odd and not representative of real clinical data - maybe it’s just teaching data).</p>
<aside class="quote no-group" data-username="spycolyf" data-post="87" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Question: Management is asking if multiple SlicerQREADS instances can be launched for comparing 2 different series.</p>
</blockquote>
</aside>
<p>Yes, that’s not a problem.  Be sure to use the OS level command that starts a new process and doesn’t just switch you to a currently running instance.</p>
<p>Or you can consider using Slicer’s CompareVolumes module.</p>

---

## Post #89 by @spycolyf (2021-03-08 17:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="88" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>(But I also still maintain this data is very odd and not representative of real clinical data - maybe it’s just teaching data).</p>
</blockquote>
</aside>
<p>Yes it is cadaver teaching data, but then I discovered some data that not teaching data with the same issues. I’ll study this data for that same condition. Maybe I will make it a requirement that bastardized non-DICOM compliant data is not guaranteed to work, but then the question becomes, why does the data load correctly in the other vended systems.</p>
<p>Question: I would expect that the database method increases the image load time, correct? Is it a significant increase?</p>
<p>Thanks</p>

---

## Post #90 by @spycolyf (2021-03-08 17:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="88" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, that’s not a problem. Be sure to use the OS level command that starts a new process and doesn’t just switch you to a currently running instance.</p>
<p>Or you can consider using Slicer’s CompareVolumes module.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Oh wow! That’s cool! Most of the systems installed at Mayo have 8GB memory. Would you say this is too little memory? Or should we recommend at least 16GB to all users who want to use SlicerQREADS?.</p>

---

## Post #91 by @spycolyf (2021-03-08 17:48 UTC)

<p>Please forgive me for all of these Monday morning question dumps! I appreciate your responses. So far they’ve been extremely stress-relieving <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:">.</p>
<p>Anyway, one requirement is that we place patient name and number, and study and series info in the title bar. Especially important if multiple instances will be implemented and to visually detect any patient context violation issues. Is this information available when SlicerQREADS is first displayed and in time to display it in the title bar? If not, will using the database method described allow for header info access.</p>
<p>Another thought is that I can pass in any DICOM info via args from the DOS launch command. Would that help this as well as the orientation issue? I could pass in direction cosines and spacing between slices for orientation.</p>
<p>Thanks</p>

---

## Post #92 by @spycolyf (2021-03-08 17:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="88" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Or you can consider using Slicer’s CompareVolumes module.</p>
</blockquote>
</aside>
<p>The CompareVolumes module could be an  important advance for using Slicer as a development platform. Any documentation or demos?</p>

---

## Post #93 by @pieper (2021-03-08 18:01 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="91" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Please forgive me for all of these Monday morning question dumps! I appreciate your responses. So far they’ve been extremely stress-relieving <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">.</p>
</blockquote>
</aside>
<p>No worries.  As you can tell, responding on this forum is something of a hobby for some of us <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="spycolyf" data-post="89" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Question: I would expect that the database method increases the image load time, correct? Is it a significant increase?</p>
</blockquote>
</aside>
<p>Maybe just a tiny bit, but I doubt it would be noticeable if you only enable ScalarVolume support (which would make sense if that’s all you expect to be able to display, that is if you don’t expect to support timeseries volumes or something).</p>
<aside class="quote no-group" data-username="spycolyf" data-post="90" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Or should we recommend at least 16GB to all users who want to use SlicerQREADS?.</p>
</blockquote>
</aside>
<p>More memory could certainly help, but 8GB is not bad for reasonable volume sizes.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="91" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>is that we place patient name and number, and study and series info in the title bar</p>
</blockquote>
</aside>
<p>That should be no problem - just a little python code.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="91" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Another thought is that I can pass in any DICOM info via args from the DOS launch command. Would that help this as well as the orientation issue? I could pass in direction cosines and spacing between slices for orientation.</p>
</blockquote>
</aside>
<p>I don’t think this is needed, just routing through the DICOM module should be enough.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="92" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>The CompareVolumes module could be an important advance for using Slicer as a development platform. Any documentation or demos?</p>
</blockquote>
</aside>
<p>It’s a bit out of date and needs to be migrated to readthedocs, but here’s a start:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/CompareVolumes" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/CompareVolumes</a></p>

---

## Post #94 by @spycolyf (2021-03-08 21:21 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="88" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If you load your data like this it should work for this data:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Hey <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>I’ve been hesitant but, I’m going to try including this code in my qreads.py file and see what happens.  We’ll see how it goes.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #95 by @jcfr (2021-03-08 22:34 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="94" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I’ve been hesitant but, I’m going to try including this code in my qreads.py file and see what happens.</p>
</blockquote>
</aside>
<p>See <a href="https://github.com/KitwareMedical/SlicerQReads/pull/51" class="inline-onebox">BUG: Ensure proper handling of orientation using Slicer DICOM module by jcfr · Pull Request #51 · KitwareMedical/SlicerQReads · GitHub</a></p>

---

## Post #96 by @spycolyf (2021-03-10 18:15 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Question:  I have a version of the SlicerQREADS extension already built. Now <a class="mention" href="/u/jcfr">@jcfr</a> has a new version ready. How shall I build the new version? Should I follow the build.md instructions again using the same target folders? Should I empty those folders first? Or should I leave the old files in tact and gitbash and build over them and maybe the build will be incremental and faster?</p>
<p>Thanks</p>

---

## Post #97 by @lassoan (2021-03-10 19:23 UTC)

<p>Pull the latest source code using git then run <code>make</code> in your build folder should do it. Only the necessary parts of the application will be rebuilt, so it should not take more than a few minutes.</p>

---

## Post #98 by @spycolyf (2021-03-12 01:39 UTC)

<p><a href="https://github.com/jcfr" rel="noopener nofollow ugc">@jcfr</a>, I’ve resized the QREADS toolbar and created new icons. I tried replacing the icons in the latest release that I downloaded from GitHub rebuilding it. I received errors. Don’t know what I did wrong.</p>
<p><a href="https://github.com/jcfr" rel="noopener nofollow ugc">@jcfr</a>, the icons and Toolbar are uploaded and here are the links. Could you have a look? Thanks.</p>
<p><a href="https://github.com/KitwareMedical/SlicerQReads/files/6126828/QReads.zip" rel="noopener nofollow ugc">QReads.zip</a><br>
<a href="https://github.com/KitwareMedical/SlicerQReads/files/6126843/QReads.UI.zip" rel="noopener nofollow ugc">QReads.UI.zip</a></p>

---

## Post #99 by @spycolyf (2021-03-15 14:57 UTC)

<p>Good Morning <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,<br>
We’re almost ready for prime time with just a couple of tasks left that will make a difference in acceptability and aesthetics.</p>
<ul>
<li>How do I set the color of the image panels background colors to black without changing the reference markers line colors to black? Currently, whenever I change the background colors, the corresponding reference markers take on the same colors</li>
<li>How do I set the initial main window size</li>
<li>I need to make the QREADS toolbar thinner and a fixed size, I changed the size in QT Creator and it displays like this. How do I eliminate the white space between the toolbar and the images</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08aae34a8cdf618181fdfb9b9eeacd233d7b7e9b.jpeg" data-download-href="/uploads/short-url/1eFWBLa9UfA96ju75dCwa3RjZ3l.jpeg?dl=1" title="NewQREADSToolBar" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08aae34a8cdf618181fdfb9b9eeacd233d7b7e9b_2_653x500.jpeg" alt="NewQREADSToolBar" data-base62-sha1="1eFWBLa9UfA96ju75dCwa3RjZ3l" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08aae34a8cdf618181fdfb9b9eeacd233d7b7e9b_2_653x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08aae34a8cdf618181fdfb9b9eeacd233d7b7e9b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08aae34a8cdf618181fdfb9b9eeacd233d7b7e9b.jpeg 2x" data-dominant-color="868886"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NewQREADSToolBar</span><span class="informations">854×653 53.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #100 by @spycolyf (2021-04-07 19:41 UTC)

<p>JC did a great job replacing my icons. I’m happy with them.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520d04b45629b2ad502b511432110f1c4193de11.png" data-download-href="/uploads/short-url/bHR2KmLIiYK52yUgxFlt9PgEc7f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520d04b45629b2ad502b511432110f1c4193de11_2_203x500.png" alt="image" data-base62-sha1="bHR2KmLIiYK52yUgxFlt9PgEc7f" width="203" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520d04b45629b2ad502b511432110f1c4193de11_2_203x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520d04b45629b2ad502b511432110f1c4193de11.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520d04b45629b2ad502b511432110f1c4193de11.png 2x" data-dominant-color="BEC2BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">223×548 24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #101 by @spycolyf (2021-04-07 19:45 UTC)

<p>Hello Slicer team,</p>
<p>How can I replace the icon and the text in the title bar with DICOM header info? Here’s what I need…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c21c2769f978adcf408abb9e4908988580fab725.png" data-download-href="/uploads/short-url/rHaWPnvhluOzl4XHEfrzrXV4sPb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c21c2769f978adcf408abb9e4908988580fab725_2_345x107.png" alt="image" data-base62-sha1="rHaWPnvhluOzl4XHEfrzrXV4sPb" width="345" height="107" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c21c2769f978adcf408abb9e4908988580fab725_2_345x107.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c21c2769f978adcf408abb9e4908988580fab725_2_517x160.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c21c2769f978adcf408abb9e4908988580fab725_2_690x214.png 2x" data-dominant-color="7E8285"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">831×260 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the Python code we tried that’s not working.</p>
<pre><code>def _update():
  slicer.app.processEvents()
  slicer.app.layoutManager().resetThreeDViews()
  QReadsLogic.setZoom(self._parameterNode.GetParameter("Zoom"))

  tags = {
    "0010,0010": "PatientName",
    "0010,0020": "PatientID",
    "0008,1030": "StudyDescription",
    "0008,103e": "SeriesDescription"
  }
  # Dictionary of name and values
  values = {tags[tag]: value for tag, value in QReadsLogic.dicomTagValues(node, slicer.dicomDatabase, tags).items()}
  # Update window title
  slicer.util.mainWindow().windowTitle = "%s - %s" % (
    slicer.util.mainWindow().windowTitle,
    "CMRN: {PatientID}     Patient Name: {PatientName}     Study: {StudyDescription}     Series: {SeriesDescription}".format(**values))

# Delay update to ensure images are rendered
qt.QTimer.singleShot(750, _update)
</code></pre>
<p>No matter what I try, This title comes up…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6a3ed954159f65df17ea8dea62b8b7319284ebf.png" alt="image" data-base62-sha1="uCNomokOLayIkxusi4mKphG3uDJ" width="331" height="86"></p>

---

## Post #102 by @jcfr (2021-04-07 19:57 UTC)

<p>To provide additional context, this is tracked by issue <a href="https://github.com/KitwareMedical/SlicerQReads/issues/59">SlicerQReads#59</a>, initial set of changes have already been integrated in <a href="https://github.com/KitwareMedical/SlicerQReads/pull/56">PR SlicerQReads#56</a></p>
<p>Answering questions posted in <a href="https://github.com/KitwareMedical/SlicerQReads/issues/59#issuecomment-815175400">this comment</a> (also copied below for context) should help you move forward.</p>
<blockquote>
<p>Two things to check:</p>
<ol>
<li>Are the relevant changes also in the file contain in the build tree (for detailed see <a href="https://github.com/KitwareMedical/SlicerQReads/issues/59#issuecomment-813537198">#59 (comment)</a>)?</li>
<li>Are there any errors reported in the python interactor (Menu → View → Python Interactor) ?</li>
</ol>
</blockquote>

---

## Post #103 by @spycolyf (2021-04-07 20:16 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Yes, the QREADS.py file in the Package contains those changes. My Package folder name is “C:\SlicerQREADS-Build_4-5-2021\lib\SlicerQReads-4.13\qt-scripted-module. the qreads.py” file is dated 4/3/2021 3:02 PM. Also, the git log -n1 command shows the result expected. Is there anything else to check?</p>
<p>I tried changing the wait time to 10000 and that did not work.</p>
<p>qt.QTimer.singleShot(10000, _update)</p>

---

## Post #104 by @jcfr (2021-04-07 20:24 UTC)

<p>I am copying your answer into issue <a href="https://github.com/KitwareMedical/SlicerQReads/issues/59">SlicerQReads#59</a> and will provide further guidance there.</p>

---

## Post #105 by @spycolyf (2021-04-07 20:31 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>ok, I actually commented there as well. Thanks</p>

---

## Post #106 by @jcfr (2021-04-07 20:36 UTC)

<p>For reference, see suggestions <a href="https://github.com/KitwareMedical/SlicerQReads/issues/59#issuecomment-815240732">here</a></p>

---

## Post #107 by @jcfr (2021-04-07 21:26 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-set-initial-size-of-the-main-window/16991">How to set initial size of the main window?</a></p>

---

## Post #108 by @spycolyf (2021-04-07 21:15 UTC)

<p><a class="mention" href="/u/superlib">@superlib</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Important, please see your email!</p>
<p>Thanks</p>

---

## Post #109 by @jcfr (2021-04-08 00:48 UTC)

<p>4 posts were merged into an existing topic: <a href="/t/how-to-set-initial-size-of-the-main-window/16991/5">How to set initial size of the main window?</a></p>

---

## Post #110 by @jcfr (2021-04-08 01:02 UTC)

<p>A post was merged into an existing topic: <a href="/t/how-to-set-initial-size-of-the-main-window/16991/10">How to set initial size of the main window?</a></p>

---

## Post #111 by @jcfr (2021-04-08 01:01 UTC)

<p>A post was merged into an existing topic: <a href="/t/how-to-set-initial-size-of-the-main-window/16991/9">How to set initial size of the main window?</a></p>

---

## Post #112 by @jcfr (2021-04-15 21:59 UTC)

<p>6 posts were split to a new topic: <a href="/t/how-to-display-web-page-in-a-dialog-using-python/17112">How to display web page in a dialog using Python?</a></p>

---

## Post #115 by @spycolyf (2021-04-12 18:03 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I’m finally getting into the tutorials after 14 hour days of urgent changes to QREADS. We finished testing on Friday and now preparing for a big release tomorrow. I’m learning all about HelloPython and the Python Interactor. Hopefully, more intelligent question in the future. Thanks everyone for your patience.</p>

---

## Post #116 by @spycolyf (2021-04-13 15:25 UTC)

<p>Hey <a class="mention" href="/u/pieper">@pieper</a>! You’ve done a great job with the SlicerWelcome tutorial. Thanks.</p>

---

## Post #117 by @spycolyf (2021-04-14 15:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I’ve installed Visual Studio Code and the Python Extension, the Slicer Python Debugger Extension, set up remote debugger connection to Slicer and they are connected. In Slicer, I then loaded the SlicerQREADS module and I see no way to load the a volume as in the HelloPython example. No menu bar is visible at the top to Add Data&gt; <a class="mention" href="/u/jcfr">@jcfr</a>, how do I load the data so that I may then debug the Title bar demographics issue?</p>

---

## Post #118 by @spycolyf (2021-04-14 15:56 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> … also, I have a change for which I need to submit a pull request. Do I have the privileges in GitHub to do that? Can’t figure out how to create a branch in GitHub in order to do a pull request and merge the change into main after approval.</p>

---

## Post #119 by @lassoan (2021-04-14 16:29 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="118" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>also, I have a change for which I need to submit a pull request. Do I have the privileges in GitHub to do that?</p>
</blockquote>
</aside>
<p>Yes, this is the beauty of distributed version control. You always have right to everything - in your own fork. You make all changes that you want, and then send a pull request to the official repository.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="118" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Can’t figure out how to create a branch in GitHub in order to do a pull request and merge the change into main after approval.</p>
</blockquote>
</aside>
<p>I use TortoiseGit git client on Windows and it makes everything very simple, as I don’t need to memorize any commands but all operations are offered in the right-click menu in File explorer.</p>

---

## Post #120 by @spycolyf (2021-04-14 17:55 UTC)

<p>Yes, I  installed TortoiseGit and it is really nice. I’ll tell my team about it for managing GIT for QREADS. Thanks for sharing that <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #121 by @jcfr (2021-04-15 22:03 UTC)

<p>2 posts were split to a new topic: <a href="/t/is-there-a-way-to-load-images-using-the-python-interactor-in-slicer/17113">Is there a way to load images using the Python Interactor in Slicer?</a></p>

---

## Post #123 by @spycolyf (2021-04-15 00:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>Is it possible to position the image scroll slider at the bottom of the images rather than the top?</p>

---

## Post #124 by @spycolyf (2021-04-15 00:55 UTC)

<p>I’m proud of myself. Thanks to <a class="mention" href="/u/lassoan">@lassoan</a> helping me today, with TortoiseGit, I was able create a branch, make minor changes, commit, push, and then create a pull request. Lots more to learn, but it’s a start.</p>

---

## Post #125 by @spycolyf (2021-04-15 01:28 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Can the mouse button event assignment be done in Python? For example, with the Python script, can I assign zoom to the mouse wheel down and drag, and pan to the left button, and W/L to simultaneous left and right buttons?</p>
<p>Maybe the SetEventTranslationClickAndDrag function?</p>

---

## Post #128 by @spycolyf (2021-04-15 21:21 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I built the latest code and the title information still does not work. I tried the following and nothing printed in Python interactor. Does this mean that the code never gets executed?. Here’s where I placed the print statements in the code…</p>
<pre><code>def _update():
  slicer.app.processEvents()
  slicer.app.layoutManager().resetThreeDViews()
  QReadsLogic.setZoom(self._parameterNode.GetParameter("Zoom"))
  # Dictionary of name and values
  values = {QReadsLogic.DICOM_TAGS[tag]: value for tag, value in QReadsLogic.dicomTagValues(node).items()}

  print("*" * 40)
  print(values)
  print("*" * 40)

  # Update window title
  slicer.util.mainWindow().windowTitle = "CMRN: {PatientID}    Patient Name: {PatientName}     Study: {StudyDescription}     Series: {SeriesDescription}".format(**values)</code></pre>

---

## Post #129 by @jcfr (2021-04-15 21:29 UTC)

<p>To help others understand the context:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/7fcd4749c80ead46cbbe60829126c7a1814ae6b1/Modules/Scripted/QReads/QReads.py#L210-L232" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/7fcd4749c80ead46cbbe60829126c7a1814ae6b1/Modules/Scripted/QReads/QReads.py#L210-L232" target="_blank" rel="noopener">KitwareMedical/SlicerQReads/blob/7fcd4749c80ead46cbbe60829126c7a1814ae6b1/Modules/Scripted/QReads/QReads.py#L210-L232</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="210" style="counter-reset: li-counter 209 ;">
<li>@vtk.calldata_type(vtk.VTK_OBJECT)</li>
<li>def onNodeAdded(self, caller, event, calldata):</li>
<li>  if slicer.mrmlScene.IsBatchProcessing():</li>
<li>    return</li>
<li>  node = calldata</li>
<li>  if not isinstance(node, slicer.vtkMRMLScalarVolumeNode):</li>
<li>    return</li>
<li>  self.updateParameterNodeFromVolumeNode(node)</li>
<li>
<li>  def _update():</li>
<li>    slicer.app.processEvents()</li>
<li>    slicer.app.layoutManager().resetThreeDViews()</li>
<li>    QReadsLogic.setZoom(self._parameterNode.GetParameter("Zoom"))</li>
<li>
<li>    # Dictionary of name and values</li>
<li>    values = {QReadsLogic.DICOM_TAGS[tag]: value for tag, value in QReadsLogic.dicomTagValues(node).items()}</li>
<li>
<li>    # Update window title</li>
<li>    slicer.util.mainWindow().windowTitle = \</li>
<li>      "CMRN: {PatientID}    Patient Name: {PatientName}     Study: {StudyDescription}     Series: {SeriesDescription}".format(**values)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/KitwareMedical/SlicerQReads/blob/7fcd4749c80ead46cbbe60829126c7a1814ae6b1/Modules/Scripted/QReads/QReads.py#L210-L232" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This code is called after a node is created, failing to see the information reported in the log file or python interactor probably means there are other errors happen beforehand during the loading of the data.</p>

---

## Post #130 by @spycolyf (2021-04-16 17:13 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>How do I show and un-show the ruler at the bottom of the image?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10dbce06eff44c2beeb86231dd7d55702c6a2976.png" alt="image" data-base62-sha1="2p8zhIqSvtKnHYU9mL9jjNUNFA2" width="240" height="64"></p>
<p>I can’t find it in the Script Repository.</p>
<p>Thanks</p>

---

## Post #131 by @mau_igna_06 (2021-04-16 17:30 UTC)

<p>This is how I do it:</p>
<pre><code class="lang-auto">#For the 3D view
ThreeDViewNode = slicer.mrmlScene.GetSingletonNode("1", "vtkMRMLViewNode")
ThreeDViewNode.SetRulerType(1)# Change 1 by 0, 2 to get no ruler or thick
ThreeDViewNode.SetRulerColor(0)# Change 0 to 1, 2 to get other colors

#For red slice
redSliceNode = slicer.mrmlScene.GetSingletonNode("Red", "vtkMRMLSliceNode")
redSliceNode.SetRulerType(1)
redSliceNode.SetRulerColor(2)
</code></pre>

---

## Post #132 by @spycolyf (2021-04-16 17:40 UTC)

<p>Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>,</p>
<p>Do you also implement an interactive measuring tool? One where the user can draw a line on the image and a measurement is given?</p>

---

## Post #133 by @mau_igna_06 (2021-04-16 18:08 UTC)

<p>I think you can implement it yourself using a vtkMRMLMarkupsLineNode, some event listeners and GUI buttons. But the experts may guide you further</p>

---

## Post #134 by @spycolyf (2021-04-16 18:29 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="133" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>vtkMRMLMarkupsLineNode</p>
</blockquote>
</aside>
<p>Some info is here I believe. In case you want to know.</p><aside class="quote" data-post="4" data-topic="13454">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/help-with-orientation-marker-and-ruler/13454/4">Help with orientation marker and ruler</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello again, 
I spoke to the people who will be the end users of my Slicer module and they really do want something more precise than the built-in ruler tool I referred to in the first post in this thread. 
If you have any links to share that could help me figure out the syntax for adding a ruler tool to my module (using qSlicerSimpleMarkupsWidget?) that would be greatly appreciated.
  </blockquote>
</aside>


---

## Post #135 by @spycolyf (2021-05-04 16:08 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>My module works perfectly except if I push the “Set Thickness” button first. Then hardly anything works. If I push other buttons first, everything works perfectly.  We beta test next Monday, so HELP!!!</p>
<p>This issue is listed in tracker here: <a>https://github.com/KitwareMedical/SlicerQReads/issues/103</a></p>
<p>Here’s the deal. After I push the “Set Threshold” button I get this error…</p>
<pre><code>Traceback (most recent call last):
  File "/home/jcfr/Projects/SlicerQReads-Release/Slicer-build/lib/SlicerQReads-4.13/qt-scripted-modules/QReads.py", line 389, in updateGUIFromParameterNode
    QReadsLogic.slabThicknessInMmToNumberOfSlices(volumeNode, slabThicknessInMm))
  File "/home/jcfr/Projects/SlicerQReads-Release/Slicer-build/lib/SlicerQReads-4.13/qt-scripted-modules/QReads.py", line 612, in slabThicknessInMmToNumberOfSlices
    assert tichknessInMm &gt; 0
AssertionError
</code></pre>
<p>Here’s the code segments at 389 and 612</p>
<blockquote>
<pre><code> def updateGUIFromParameterNode(self, caller=None, event=None):
      QReadsLogic.setSlab(       (line 389)
          QReadsLogic.slabModeFromString(slabModeStr),
          QReadsLogic.slabThicknessInMmToNumberOfSlices(volumeNode, slabThicknessInMm))
</code></pre>
</blockquote>
<pre><code>@staticmethod
  def slabThicknessInMmToNumberOfSlices(volumeNode, tichknessInMm):
     if volumeNode is None:
      return 1
    assert tichknessInMm &gt; 0  (line 612)
    return int(tichknessInMm / max(volumeNode.GetSpacing()))
</code></pre>
<p>… and no jokes anout</p>

---

## Post #136 by @lassoan (2021-05-04 16:52 UTC)

<p>Can you upload an Windows installation package and send the link so that we can test it?</p>
<p>You can also check it yourself by attaching a Python debugger and check where the 0 slice thickness value comes from.</p>

---

## Post #137 by @jcfr (2021-05-04 16:53 UTC)

<p>To ensure messages posted on the forum benefit the community, we suggest to provide minimally reproducible example.</p>
<p>In that particular case, it turns out I started to look at this and it is a simple logic issue.</p>

---

## Post #138 by @spycolyf (2021-05-04 17:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Yes, I would have done that if I could get my debugger to work. I’ve successfully attached the Python Debugger fro VS Code, and tried to set break points, but get this error…</p>
<pre><code>pydev debugger: warning: trying to add breakpoint to file that does not exist: c:\programdata\na-mic\slicer 4.13.0-2021-04-22\qreads.py (will have no effect)
Traceback (most recent call last):
  File "C:/SlicerQReads-0.1.0-2021-04-27-win-amd64/lib/SlicerQReads-4.13/qt-scripted-modules/QReads.py", line 55, in eventFilter
    slicer.util.mainWindow().writeSettings()
AttributeError: qSlicerAppMainWindow has no attribute named 'writeSettings'
</code></pre>
<p>Although my SlicerQREADS module folder was set to “C:/SlicerQReads-0.1.0-2021-04-27-win-amd64/lib/SlicerQReads-4.13/qt-scripted-modules/QReads.py”, why is it trying to set break points in “c:\programdata\na-mic\slicer 4.13.0-2021-04-22\qreads.py?”</p>
<p>Thanks</p>

---

## Post #139 by @jcfr (2021-05-04 17:28 UTC)

<blockquote>
<p>started to look at this and it is a simple logic issue.</p>
</blockquote>
<p>This has been fixed in <a href="https://github.com/KitwareMedical/SlicerQReads/pull/105" class="inline-onebox">BUG: Fix toggling of SlabThickness mode by jcfr · Pull Request #105 · KitwareMedical/SlicerQReads · GitHub</a></p>
<blockquote>
<p><code>qSlicerAppMainWindow has no attribute named 'writeSettings'</code></p>
</blockquote>
<p>Consider rebuilding the application, the error reported indicate you didn’t rebuilt. Changes have been integrated.</p>
<p>See <a href="https://github.com/KitwareMedical/SlicerQReads/commit/215006327069cb90633487a409adb710b8c472fe" class="inline-onebox">BUG: Ensure window geometry and position is restored · KitwareMedical/SlicerQReads@2150063 · GitHub</a></p>

---

## Post #140 by @spycolyf (2021-05-04 17:29 UTC)

<p>Sorry <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I’ll try to speak more in the context of addressing the Slicer community rather than the experts. Got it.</p>
<p>And thanks so much for the fix, I was losing a little sleep over this one. You just added a couple more days to my life I think.</p>
<p>Thanks</p>

---

## Post #141 by @lassoan (2021-05-04 18:13 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="138" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Although my SlicerQREADS module folder was set to “C:/SlicerQReads-0.1.0-2021-04-27-win-amd64/lib/SlicerQReads-4.13/qt-scripted-modules/QReads.py”, why is it trying to set break points in “c:\programdata\na-mic\slicer 4.13.0-2021-04-22\qreads.py?”</p>
</blockquote>
</aside>
<p>This is a recent regression in Visual Studio Code’s Python debugger. On Windows, you need to remove <code>pathMappings</code> section from the default debugger configuration - see instruction <a href="https://github.com/SlicerRt/SlicerDebuggingTools#one-time-setup-1">here</a>.</p>

---

## Post #142 by @spycolyf (2021-05-04 19:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Wow! That fixed it. Thanks</p>

---

## Post #143 by @spycolyf (2021-05-06 20:41 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Hello, have you tried running Slicer on a VDI? Does it work?.</p>

---

## Post #144 by @lassoan (2021-05-07 13:36 UTC)

<p>We have successfully used Slicer in several virtual environments (VirtualBox, VMWare, Hyper-V) and it works well in docker containers, Windows subsystem for Linux, etc. There was only one exception, Parallels on macOS, which only supported an embarrassingly old OpenGL version (this was about 1-2 years ago, the situation may have improved since then).</p>

---

## Post #145 by @pieper (2021-05-07 13:56 UTC)

<p>There might also be some issues with versions of microsoft’s remote desktop protocol and the version of opengl they support.  But other remote desktop solutions like VNC, nomachine, google remote desktop, teamviewer, etc all work well.</p>

---

## Post #147 by @spycolyf (2021-05-13 16:03 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I was asked by a radiologist if there’s a way to present other types of 3D renderings in the 3D view of SlicerQREADS. I’m thinking this would be fairly easy with this amazing development environment. How could I implement some kind of toggle that would show a MIP and other 3D rendering in that 3d view in addition to the current intersecting planes?</p>
<p>Thanks!</p>

---

## Post #148 by @pieper (2021-05-13 16:07 UTC)

<p>Yes, that would be very straightforward.  The full volume rendering API is scriptable and can be triggered of events or UI actions.  See:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded</a></p>

---

## Post #149 by @lassoan (2021-05-13 16:43 UTC)

<p><a class="mention" href="/u/spycolyf">@spycolyf</a> We can give more specific advice if you attach a few screenshots of the kind of renderings that you would like to see.</p>

---

## Post #150 by @spycolyf (2021-05-13 17:25 UTC)

<aside class="quote no-group" data-username="pieper" data-post="148" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, that would be very straightforward. The full volume rendering API is scriptable and can be triggered of events or UI actions. See:</p>
</blockquote>
</aside>
<p>Wow! Thanks! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>OK now that I’m in the beta testing phase of the app, I’m starting to get feedback from physicians about certain features of SlicerQREADS (SQR) they need changed. We are currently making matrices for prioritizing the issues. Therefore, I want to warn you that I will be asking many questions on how to implement certain changes. I think it will be very impressive to the physicians when they see how quickly the changes can be made and my team will be impressing when they se how easily they can be made. So, thank you ahead of time, and forgive me in advanced for many future questions.</p>
<p>Thanks</p>

---

## Post #151 by @spycolyf (2021-05-13 17:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="149" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We can give more specific advice if you attach a few screenshots of the kind of renderings that you would like to see.</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. I will <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #152 by @spycolyf (2021-05-13 17:30 UTC)

<p><span class="mention">@lasson</span>, <a class="mention" href="/u/pieper">@pieper</a></p>
<ul>
<li>A Maximum intensity projection would be most useful.</li>
<li>And one more type of rendering with opacities would be great. Got any impressive suggestions?</li>
</ul>
<p>I’ll look and get more specific, and a link to observe different rendering would save time if you have any. Thanks.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:"></p>

---

## Post #153 by @spycolyf (2021-05-13 18:30 UTC)

<p>Great! I’ll look into those in a little while, but just to be more specific, I need…</p>
<ul>
<li>a MIP</li>
<li>at least CT 3D surface renderings skin, bone, lung and brain.</li>
</ul>
<p>I think other more sophisticated renderings will involve segmentation like with the picture below. Correct? Or could this be done automatically?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6602012cf13f5beba45264255b7f01d0bc4f14f2.jpeg" data-download-href="/uploads/short-url/eyoZNIoBizGceUJ1qbkORd1aNIC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6602012cf13f5beba45264255b7f01d0bc4f14f2_2_612x500.jpeg" alt="image" data-base62-sha1="eyoZNIoBizGceUJ1qbkORd1aNIC" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6602012cf13f5beba45264255b7f01d0bc4f14f2_2_612x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6602012cf13f5beba45264255b7f01d0bc4f14f2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6602012cf13f5beba45264255b7f01d0bc4f14f2.jpeg 2x" data-dominant-color="656374"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">754×616 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #154 by @lassoan (2021-05-13 19:22 UTC)

<p>I’ve added two code snippets that you can use to set up these renderings.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="152" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>A Maximum intensity projection would be most useful.</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-using-maximum-intensity-projection">this script</a>.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f429a5b8d16b9bd4b9c73400ce1d115bc13b3a05.mp4">
  </div><p></p>
<aside class="quote no-group" data-username="spycolyf" data-post="152" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>And one more type of rendering with opacities would be great.</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-making-soft-tissues-transparent">this script</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0b66ce8e52357eddae7d578a613305988b6c6a3.jpeg" data-download-href="/uploads/short-url/w3TNtJO8TFMj0swJrLj0nNfVp1V.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0b66ce8e52357eddae7d578a613305988b6c6a3_2_518x500.jpeg" alt="image" data-base62-sha1="w3TNtJO8TFMj0swJrLj0nNfVp1V" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0b66ce8e52357eddae7d578a613305988b6c6a3_2_518x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0b66ce8e52357eddae7d578a613305988b6c6a3_2_777x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0b66ce8e52357eddae7d578a613305988b6c6a3_2_1036x1000.jpeg 2x" data-dominant-color="896F87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1212×1169 336 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #155 by @spycolyf (2021-05-18 18:45 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I’ve gotten things to work somewhat. I’m trying to implement it in such a way that the user has a choice between MIP, Surface Rendering and Intersecting planes. How can I get back to the Intersecting Planes view after having switched the other views? Also how do I programmatically toggle slice visibility in 3D view (as can be done with the “v” key). Thanks.</p>

---

## Post #156 by @lassoan (2021-05-18 19:17 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="155" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>How can I get back to the Intersecting Planes view after having switched the other views?</p>
</blockquote>
</aside>
<p>I’m not sure what you mean by “intersection planes view”. You can show/hide slice planes and change volume rendering settings.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="155" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Also how do I programmatically toggle slice visibility in 3D view (as can be done with the “v” key).</p>
</blockquote>
</aside>
<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures">add keyboard shortcut at Qt level</a> or add an observer to the keypress event to each 3D viewer’s interactor (you can search for <code>vtk.vtkCommand.KeyPressEvent</code> for examples; or use a scripted displayable manager to capture keyboard events).</p>

---

## Post #157 by @spycolyf (2021-05-18 19:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Oh, ok. Then I should ask, how do I show/hide the slice planes with Python commands.</p>
<p>Then how do I set the renderings to nothing.</p>
<p>Thanks</p>

---

## Post #158 by @jamesobutler (2021-05-18 21:20 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="157" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Then I should ask, how do I show/hide the slice planes with Python commands</p>
</blockquote>
</aside>
<p>I think you are looking for the following: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-slice-views-in-3d-window" rel="noopener nofollow ugc">Show slice views in 3D window</a></p>

---

## Post #159 by @spycolyf (2021-05-18 23:24 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a></p>
<aside class="quote no-group" data-username="jamesobutler" data-post="158" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I think you are looking for the following: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-slice-views-in-3d-window" rel="noopener nofollow ugc">Show slice views in 3D window</a></p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p>That works. I appreciate that. Now I can display the renderings without the slice planes. Great!</p>

---

## Post #160 by @spycolyf (2021-05-18 23:29 UTC)

<p>How do I clear out the renderings to switch to another rendering? I can switch from the opacity rendering to the MIP, but not from the MIP to any other rendering. I think if I can reset or clear the MIP first, it might work. How do I clear out the rendering?</p>
<p>Thanks</p>

---

## Post #161 by @lassoan (2021-05-19 01:27 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">choose a different rendering preset</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-using-maximum-intensity-projection">set rendering technique to <code>slicer.vtkMRMLViewNode.Composite</code></a>.</p>

---

## Post #162 by @spycolyf (2021-05-20 18:08 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Hello JC, I’m seeing that I can’t set the 3D view to display MIPS or 3D rendering with the SlicerQREADS build. But when I run the SlicerQREADS module inside of the Slicer app, I can perform the 3D render with my Python changes. Did you remove this capability from SlicerQREADS?</p>
<p>Thanks</p>

---

## Post #163 by @jcfr (2021-05-20 20:52 UTC)

<blockquote>
<p>Did you remove this capability from SlicerQREADS?</p>
</blockquote>
<p>Since MIP was not part of the requirements, the VolumeRendering module providing the functionality has been disabled:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L123-L134">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L123-L134" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L123-L134" target="_blank" rel="noopener">KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L123-L134</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="123" style="counter-reset: li-counter 122 ;">
          <li>set(Slicer_QTLOADABLEMODULES_DISABLED</li>
          <li>  CropVolume</li>
          <li>  Plots</li>
          <li>  SceneViews</li>
          <li>  Sequences</li>
          <li>  Segmentations</li>
          <li>  SlicerWelcome</li>
          <li>  Tables</li>
          <li>  Texts</li>
          <li>  ViewControllers</li>
          <li>  VolumeRendering</li>
          <li>  )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #164 by @spycolyf (2021-05-21 19:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="161" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded" rel="noopener nofollow ugc">choose a different rendering preset </a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-using-maximum-intensity-projection" rel="noopener nofollow ugc">set rendering technique to <code>slicer.vtkMRMLViewNode.Composite</code> </a></p>
</blockquote>
</aside>
<p><span class="mention">@lasson</span>, thanks you so much that worked! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #165 by @spycolyf (2021-05-26 17:31 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Hello JC, I’m looking to remove slice planes rendering in the 3D view because I want to replace it with a surface render. How can I clear that out?</p>
<p>Thanks.</p>

---

## Post #166 by @jamesobutler (2021-05-26 17:42 UTC)

<p><a class="mention" href="/u/spycolyf">@spycolyf</a> I believe you are looking for the following example in the Slicer Script repository titled <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-slice-views-in-3d-window" rel="noopener nofollow ugc">Show slice views in 3D window</a>. You had posted previously an image (seen below) which was detailing volume rendering being shown at the same time as Slice views showing in the 3D View.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05886d8642bbae3a5fb60581ba64a1eee0e6ff47.png" alt="image" data-base62-sha1="MWGk1MMP6zYaDvJIa66MvOYP4z" width="266" height="247">.</p>

---

## Post #167 by @spycolyf (2021-06-08 17:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Could you extract from 1/159 to 43/159 of this topic to a new topic, “Slicer Module Local Installation Footprint” (for want of a much better name)?</p>
<p>Thanks.</p>

---

## Post #168 by @lassoan (2021-06-08 17:52 UTC)

<p>Done. The new topic is here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="18019">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-custom-application-deployment-to-many-computers/18019">Slicer custom application deployment to many computers</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/superlib">@superlib</a> 
Good Morning. I’m starting to think about how to deploy SlicerQR to 25,000 PCs across the Mayo Enterprise. After building the package, it consists of over 7000 files at a total size of over 700MB. It would be seriously frowned-upon to propose deploying it to 25,000 PCs. So, my question is: Would there be any disadvantages to placing the installation in 1 place on a file share and have the users execute SlicerQR from a folder there? Would there be conflicts with …
  </blockquote>
</aside>


---

## Post #169 by @spycolyf (2021-06-23 20:05 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Hello JC,</p>
<p>Whenever the user zooms and pans, and then pushes the EnableWLButton to window/level, the zoom and pan resets forcing the user to zoom and pan all over again. The code that causes this is…</p>
<p><code>self._parameterNode.SetParameter("WindowLevelEnabled", "true" if self.ui.EnableWLButton.checked else "false")</code></p>
<p>How do I use the WL widget without resetting the zoom and pan?</p>
<p>Thanks</p>

---

## Post #170 by @pieper (2021-06-23 20:20 UTC)

<p>This doesn’t happen in regular slicer so it must be something to do with your customizations not handling the end of the pan/zoom interactions.</p>

---

## Post #171 by @spycolyf (2021-06-23 20:35 UTC)

<p>Yes, that;s true. Slicer does not have this issue. However <a class="mention" href="/u/jcfr">@jcfr</a> implements many if the UI actions using the self._parameterNode.SetParameter function and each of them reset my views, Here are all of those features that use the self._parameterNode.SetParameter function, each resetting my views…</p>
<pre><code class="lang-auto">    self._parameterNode.SetParameter("ReferenceMarkersVisible", "true" if self.ui.ShowReferenceMarkersButton.checked else "false")
    self._parameterNode.SetParameter("SlabEnabled", "true" if slabEnabled else "false")
    self._parameterNode.SetParameter("SlabMode", QReadsLogic.slabModeToString(self.slabModeButtonGroup.checkedId()))
    self._parameterNode.SetParameter("SlabThicknessInMm", str(self.ui.SlabThicknessSliderWidget.value))
    self._parameterNode.SetParameter("InverseGray", "true" if self.ui.InverseGrayButton.checked else "false")
    self._parameterNode.SetParameter("Zoom", self.ui.ZoomComboBox.currentText)
    self._parameterNode.SetParameter("OrientationMarkerType",
      str(slicer.util.getNodesByClass('vtkMRMLAbstractViewNode')[0].GetOrientationMarkerType()))
    self._parameterNode.SetParameter("RulerVisible", "true" if self.ui.RulerVisibleButton.checked else "false")
    self._parameterNode.SetParameter("OrientationMarkerType", str(nextOrientationMarkerType))

</code></pre>

---

## Post #172 by @spycolyf (2021-06-23 21:04 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="171" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p><code>SetParameter</code></p>
</blockquote>
</aside>
<p>OK, might have something to do with this…</p>
<pre><code class="lang-auto">def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """
    if inputParameterNode:
      self.logic.setDefaultParameters(inputParameterNode)

    # Unobserve previously selected parameter node and add an observer to the newly selected.
    # Changes of parameter node are observed so that whenever parameters are changed by a script or any other module
    # those are reflected immediately in the GUI.
    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
    self._parameterNode = inputParameterNode
    if self._parameterNode is not None:
      self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

    # Initial GUI update
    self.updateGUIFromParameterNode()
</code></pre>

---

## Post #173 by @spycolyf (2021-06-23 21:10 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, is there a way to, for instance, enable he window/level widget without resetting the views?</p>
<p>Thanks</p>

---

## Post #174 by @mau_igna_06 (2021-06-23 21:46 UTC)

<p>Hi Doug, I looked at the code here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py</a></h4>


    <pre><code class="lang-py">import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import NodeModify, toBool, VTKObservationMixin

from Resources import QReadsResources
#
# QReads
#

class QReads(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "QReads"  # TODO: make this more human readable by adding spaces
</code></pre>


  This file has been truncated. <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This two functions or calls may have something to do with the causes of view-reset you are looking for:</p>
<pre><code class="lang-auto">centerSlice
sliceLogic.FitSliceToAll()
</code></pre>
<p>I started looking for keywords in code as reset and found that. I also looked for ‘sliceLogic’ mentions as it may be related to the cause of your problem.</p>
<p>Hope this helps</p>

---

## Post #175 by @spycolyf (2021-06-24 01:13 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="172" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p><code>self._parameterNode</code></p>
</blockquote>
</aside>
<p>OK, thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>, I’ll have a look at that. But since only self._parameterNode.SetParameter calls cause this slice view reset behavior, I’m suspecting  it’s the setParameterNode function causing it.</p>
<p>Have a look…</p>
<p>Each of the following calls reset the views…</p>
<pre><code class="lang-auto">    self._parameterNode.SetParameter("ReferenceMarkersVisible", "true" if self.ui.ShowReferenceMarkersButton.checked else "false")
    self._parameterNode.SetParameter("SlabEnabled", "true" if slabEnabled else "false")
    self._parameterNode.SetParameter("SlabMode", QReadsLogic.slabModeToString(self.slabModeButtonGroup.checkedId()))
    self._parameterNode.SetParameter("SlabThicknessInMm", str(self.ui.SlabThicknessSliderWidget.value))
    self._parameterNode.SetParameter("InverseGray", "true" if self.ui.InverseGrayButton.checked else "false")
    self._parameterNode.SetParameter("Zoom", self.ui.ZoomComboBox.currentText)
    self._parameterNode.SetParameter("OrientationMarkerType",
      str(slicer.util.getNodesByClass('vtkMRMLAbstractViewNode')[0].GetOrientationMarkerType()))
    self._parameterNode.SetParameter("RulerVisible", "true" if self.ui.RulerVisibleButton.checked else "false")
    self._parameterNode.SetParameter("OrientationMarkerType", str(nextOrientationMarkerType))
</code></pre>
<p>Do you think the following function is the culprit? It does a removeObserver followed by an add observer</p>
<pre><code class="lang-auto">def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """
    if inputParameterNode:
      self.logic.setDefaultParameters(inputParameterNode)

    # Unobserve previously selected parameter node and add an observer to the newly selected.
    # Changes of parameter node are observed so that whenever parameters are changed by a script or any other module
    # those are reflected immediately in the GUI.
    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
    self._parameterNode = inputParameterNode
    if self._parameterNode is not None:
      self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

    # Initial GUI update
    self.updateGUIFromParameterNode()
</code></pre>

---

## Post #176 by @spycolyf (2021-07-12 17:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a> , <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Good afternoon everyone,</p>
<p>All of this time I’ve been focused on optimizing everything for CT.  Now that that’s all prefect, MR and PET images have issues. For both PET and MR, the initial W/L’s are messed up and I can’t adjust it manually. They both look like this…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc6c90836fc69040c07038689c3771530bfa1581.jpeg" data-download-href="/uploads/short-url/A12V64gisU5PNWXBEzgxyeXp39v.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc6c90836fc69040c07038689c3771530bfa1581_2_669x500.jpeg" alt="image" data-base62-sha1="A12V64gisU5PNWXBEzgxyeXp39v" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc6c90836fc69040c07038689c3771530bfa1581_2_669x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc6c90836fc69040c07038689c3771530bfa1581_2_1003x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc6c90836fc69040c07038689c3771530bfa1581_2_1338x1000.jpeg 2x" data-dominant-color="232222"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1609×1202 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This looks like overflow or underflow of some sort. I was expecting the W/L to be initially read from the header.</p>
<p>Any hint as I begin to investigate the Python code?</p>
<p>Thanks</p>

---

## Post #177 by @lassoan (2021-07-12 18:01 UTC)

<p>In fact, the window/level is from the DICOM header - from the first slice. However, for whole-body images the first slice is often almost empty, so it could be better to use the center slice instead - see:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5140">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5140" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5140" target="_blank" rel="noopener">Use more representative slice's window/level when loading DICOM image</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-08-26" data-time="22:58:54" data-timezone="UTC">10:58PM - 26 Aug 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When loading a DICOM series, default window/level is taken from the first slice.<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> In some cases, window/level is different for each slice, and since first slice usually does not contain typical anatomy, its window/level may not be ideal for the object of interest. Instead, it could be better to use the center slice's window/level values.

See more information here: https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284/9

Slicer version: Slicer-4.11.0-2020-08-26</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The transparency for low values is a feature of the colormap. You should be able to change the colormap and/or adjust the window/level. If you show multiple series (e.g., PET and CT) then left-click-and-drag may adjust the other volume that you expect.</p>
<p>We have improved PET/CT default colormap selection - see <a href="https://github.com/Slicer/Slicer/search?q=PET&amp;type=commits">these commits</a>. I would recommend to try PET/CT loading in recent Slicer Preview Release and if you like the changes then update your custom application to use a recent master version of Slicer and use the DICOM module for load DICOM data.</p>

---

## Post #178 by @pieper (2021-07-12 18:20 UTC)

<p>You should also have a look at the PET related extensions (just type PET in the extension search box) and in particular the dicom plugin:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/QIICR/Slicer-PETDICOMExtension">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/0330fb24343b17b26478365b5b059c04a985296dd5bda69568e4688b90eb116d/QIICR/Slicer-PETDICOMExtension" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/QIICR/Slicer-PETDICOMExtension" target="_blank" rel="noopener">QIICR/Slicer-PETDICOMExtension</a></h3>

  <p>3D Slicer extension containing tools for importing DICOM PET series - QIICR/Slicer-PETDICOMExtension</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PET-IndiC" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PET-IndiC</a></p>

---

## Post #179 by @jcfr (2021-07-12 19:13 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="176" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I was expecting the W/L to be initially read from the header.</p>
<p>Any hint as I begin to investigate the Python code?</p>
</blockquote>
</aside>
<p>By default, the windows level is automatically adjusted:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L371-L372">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L371-L372" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L371-L372" target="_blank" rel="noopener">KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L371-L372</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="371" style="counter-reset: li-counter 370 ;">
          <li>interactionMode = slicer.vtkMRMLInteractionNode.AdjustWindowLevel if windowLevel else slicer.vtkMRMLInteractionNode.ViewTransform</li>
          <li>slicer.app.applicationLogic().GetInteractionNode().SetCurrentInteractionMode(interactionMode)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Otherwise, here is the relevant function called when brightness/contract are updated or is one of the preset is selected:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L579-L593">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L579-L593" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L579-L593" target="_blank" rel="noopener">KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L579-L593</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="579" style="counter-reset: li-counter 578 ;">
          <li>def updateWindowLevel(windowStep=None, levelStep=None):</li>
          <li>  for volumeNode in slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode"):</li>
          <li>    volumeDisplayNode = volumeNode.GetDisplayNode()</li>
          <li>    with NodeModify(volumeDisplayNode):</li>
          <li></li>
          <li>      window = volumeDisplayNode.GetWindow()</li>
          <li>      if windowStep is not None:</li>
          <li>        window = window + windowStep</li>
          <li></li>
          <li>      level = volumeDisplayNode.GetLevel()</li>
          <li>      if levelStep is not None:</li>
          <li>        level = level + levelStep</li>
          <li></li>
          <li>      volumeDisplayNode.SetAutoWindowLevel(0)</li>
          <li>      volumeDisplayNode.SetWindowLevel(window, level)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Here are the window level presets:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L457-L463">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L457-L463" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L457-L463" target="_blank" rel="noopener">KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L457-L463</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="457" style="counter-reset: li-counter 456 ;">
          <li>WINDOW_LEVEL_PRESETS = {</li>
          <li>  'CT-BodySoftTissue': (400, 40),</li>
          <li>  'CT-Bone': (2500, 300),</li>
          <li>  'CT-Head': (100, 40),</li>
          <li>  'CT-Lung': (1600, -600)</li>
          <li>}</li>
          <li>"""Windows level presets specified as (windows, level)"""</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #180 by @jcfr (2021-07-12 19:17 UTC)

<p>To ensure the community can help you, you may also consider updating the code base <a href="https://github.com/KitwareMedical/SlicerQReads">KitwareMedical/SlicerQReads</a> to include your recent updates (e.g Volume Cropper, …) or sharing a link  to the relevant fork including the changes.</p>

---

## Post #181 by @spycolyf (2021-07-12 19:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> - FYI: I’m on Slicer version 4.13. Also, for those particular images the first W/L setting is center=8438.388323078, width=16876.776646156 which is comparable to the middle slices.</p>
<p>So it does appear that it’s reading it from the header.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> - 1) It does the same thing with MR series, Is the PET extension necessary for getting the PET W/L fixed?</p>

---

## Post #182 by @spycolyf (2021-07-12 19:34 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="180" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To ensure the community can help you, you may also consider updating the code base <a href="https://github.com/KitwareMedical/SlicerQReads" rel="noopener nofollow ugc">KitwareMedical/SlicerQReads</a> to include your recent updates (e.g Volume Cropper, …) or sharing a link to the relevant fork including the changes.</p>
</blockquote>
</aside>
<p>JC, yes I wish I could, I’ll have to clear that with management. I’ll try to get up the courage to ask. They do not have the appetite to hear about more issues as this “should have been released a long time ago.” But I hear you loud and clear because I could definitely use the help from the slicer community and this may happen after I get this used and loved by the physician users. Without this help, it’s a real struggle. But, these (w/l) are the kinds of issues that will turn them off and frustrate them completely on first use.</p>
<p>But, to reiterate, I’d love to do what you say, so we are in the same boat. I’ll keep trying to encourage management.</p>
<p>Thanks</p>

---

## Post #183 by @lassoan (2021-07-12 19:43 UTC)

<p>Probably the only issue is that you use a color table that maps very bright voxels to be transparent. There several beautiful PET color tables (those that are specified in the DICOM standard and a few others). Is there a particular reason you don’t use those? Which color table do you use?</p>

---

## Post #184 by @pieper (2021-07-12 20:19 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="182" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I’ll have to clear that with management.</p>
</blockquote>
</aside>
<p>I guess you know this Doug, but make sure you management knows that we are willing to help people here for free because we think this open discussion and troubleshooting helps make the code better and it creates an educational resource for the community.  If your project is not open then we just have to say sorry we can’t really help and they really need to hire consultants to work on closed projects.</p>

---

## Post #185 by @spycolyf (2021-07-12 20:25 UTC)

<p>OK, that’s a great point that I was not clear on. Thanks for making this really clear. I’ll let them know.<br>
Also, I sincerely apologize for not fully understanding this previously.</p>

---

## Post #186 by @spycolyf (2021-07-12 21:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>FYI: Slicer displays this PET series the same as my module…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9295f680e80263570163f8fe306a2c462e1cccb.png" data-download-href="/uploads/short-url/sHyBWZIQPt45bn1JYBqkX7UiLGj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9295f680e80263570163f8fe306a2c462e1cccb_2_690x406.png" alt="image" data-base62-sha1="sHyBWZIQPt45bn1JYBqkX7UiLGj" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9295f680e80263570163f8fe306a2c462e1cccb_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9295f680e80263570163f8fe306a2c462e1cccb_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9295f680e80263570163f8fe306a2c462e1cccb.png 2x" data-dominant-color="AFAFBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1087×640 96.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What do I need to do to display it here? Is there a fix in your latest slicer nightly build?</p>
<p>Thanks.</p>

---

## Post #187 by @lassoan (2021-07-12 21:23 UTC)

<p>The release that you tried is almost a year old! Please try the latest Slicer Preview Release. Default color table selection for PET/CT studies has been improved recently.</p>

---

## Post #188 by @spycolyf (2021-07-12 21:52 UTC)

<p>Yes, this is version 4.11. But the same is happening in 4.13</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c1017f3319190f5ae6cfe8d069164f568b12409.png" data-download-href="/uploads/short-url/40fQFiJAu1HGiVM5LqUD2JSso7n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c1017f3319190f5ae6cfe8d069164f568b12409_2_690x409.png" alt="image" data-base62-sha1="40fQFiJAu1HGiVM5LqUD2JSso7n" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c1017f3319190f5ae6cfe8d069164f568b12409_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c1017f3319190f5ae6cfe8d069164f568b12409_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c1017f3319190f5ae6cfe8d069164f568b12409.png 2x" data-dominant-color="B0AEBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1079×641 91.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Here’s an MRI…</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb56b0f928951171ba611d54ca209024fe14862.png" data-download-href="/uploads/short-url/fNncVkN5IwSezXj4ukQ4cnRPKjU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6eb56b0f928951171ba611d54ca209024fe14862_2_690x409.png" alt="image" data-base62-sha1="fNncVkN5IwSezXj4ukQ4cnRPKjU" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6eb56b0f928951171ba611d54ca209024fe14862_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6eb56b0f928951171ba611d54ca209024fe14862_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb56b0f928951171ba611d54ca209024fe14862.png 2x" data-dominant-color="B8B8C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1089×647 93.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are we the only organization having these issues? Is this something that you would be interested in investigating, Or are we stuck with SlicerQREADS working only with CT? If you’re interested, I can send you the DICOM files.</p>
<p>Thanks</p>

---

## Post #189 by @pieper (2021-07-12 22:08 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="188" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Are we the only organization having these issues?</p>
</blockquote>
</aside>
<p>This is the first I’ve seen this, and I’ve seen a whole lot of dicom files in Slicer.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="188" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>If you’re interested, I can send you the DICOM files.</p>
</blockquote>
</aside>
<p>Yes, if you can share these for testing that would help.  Can they be made part of a public testing data set?  This could help ensure the problem doesn’t crop up again in the future.</p>

---

## Post #190 by @spycolyf (2021-07-13 00:21 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<p>Ok, I’ll ask or anonymize. If folks want this fixed, we need to know the cause. This seems to be happening for all of our non-CT data (MR and PET); a major blow for me. This is our test data, but I’ll make extra sure it’s public sharable. I should have them for you by tomorrow on Drop Box.</p>
<p>Thanks</p>

---

## Post #191 by @lassoan (2021-07-13 01:53 UTC)

<p>This is very interesting, I don’t recall ever seeing this issue either (and there have been no user complaints about it). It should be trivial to fix it if we get a sample image that reproduces it.</p>

---

## Post #192 by @spycolyf (2021-07-13 14:07 UTC)

<p>GREAT!!! Looks like some kind of overflow where the pixel values go high they set the sign bit and go negative. I don’t know, but I’ll get it to you. Thanks.</p>

---

## Post #193 by @spycolyf (2021-07-13 15:17 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> : Interesting hint: It displays fine in QREADS and another DICOM apps. But Photoshop displays just like Slicer.</p>
<p>I am working on getting you the data now.</p>
<p>Thanks</p>

---

## Post #197 by @spycolyf (2021-10-07 17:00 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a></p>
<p>QREADS 3D MPR (SlicerQREADS) has been deployed for about a month, and thanks to you, it is rock solid. I think the timing is right for me to ask the powers that be if I can open source it. I will start asking and hopefully I can get it done. Thank you guys so so much for all of the great help; I am so grateful to you. I will be retiring on December 24th, so I’ll be out of here. I’ll keep you informed of how the politics play out with open-sourcing SlicerQREADS. I’ll try my best.</p>
<p>Thanks</p>

---

## Post #198 by @pieper (2021-10-07 17:03 UTC)

<p>That’s great to hear, congrats <a class="mention" href="/u/spycolyf">@spycolyf</a> on getting this accomplished and on your upcoming retirement - hope you have fun!</p>

---

## Post #199 by @jcfr (2021-10-07 17:06 UTC)

<p>Ditto. And thanks for your patience and willingness to consider an alternative approach <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>the timing is right for me to ask the powers that be if I can open source it.</p>
</blockquote>
<p>Sounds great. When it makes sense, consider reaching out so that we consolidate with the version hosted at <a href="https://github.com/KitwareMedical/SlicerQReads">https://github.com/KitwareMedical/SlicerQReads</a></p>

---

## Post #200 by @mau_igna_06 (2021-10-07 17:24 UTC)

<p>Very happy to hear that SlicerQReads project is going well.</p>
<p>Have a good time in your future retirement.</p>

---

## Post #201 by @lassoan (2021-10-07 18:03 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="197" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>has been deployed for about a month, and thanks to you, it is rock solid</p>
</blockquote>
</aside>
<p>This is awesome news! …and it may be a perfect time to add a few sentences to the <a href="https://discourse.slicer.org/c/community/success-stories/29">Success stories</a> category.</p>
<p>Congratulations for your retirement and please don’t forget to introduce us to you successor(s).</p>

---

## Post #202 by @spycolyf (2021-10-13 14:17 UTC)

<p>OK <a class="mention" href="/u/lassoan">@lassoan</a> , I will add to the Success Stories. Thanks for reminding me. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #203 by @spycolyf (2021-11-23 20:20 UTC)

<p>Hello all,</p>
<p>I’m experiencing sometimes the SlicerQREADS module does not display the images. I think it might be the DCM files folder path length. Also, the log files indicate that it could not find the folder. Could you tell me what the maximum length is? Thanks.</p>

---

## Post #204 by @jcfr (2021-11-23 20:33 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="203" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>files folder path length</p>
</blockquote>
</aside>
<p>By default, that would be 256 characters. See <a href="https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=cmd" class="inline-onebox">Maximum Path Length Limitation - Win32 apps | Microsoft Learn</a></p>

---

## Post #205 by @spycolyf (2021-11-23 21:28 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="204" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>By default, that would be 256 characters. See <a href="https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=cmd" rel="noopener nofollow ugc">Maximum Path Length Limitation - Win32 apps | Microsoft Docs</a></p>
</blockquote>
</aside>
<p>Does this also apply to Slicer’s DICOM database? Does it have it’s own path length restrictions? I know the Slicer installation has issues with path lengths. So I was wondering about other Slicer functions as well.</p>
<p>Thanks</p>

---

## Post #206 by @spycolyf (2021-11-23 21:33 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>By the way, I asked my Unit Head for permission to put 3D MPR back out in Slicer open source. He is looking into it. He’s going to ask the legal folks. I’m trying to get it done before I retire in December.</p>
<p>Thanks,</p>

---

## Post #207 by @pieper (2021-11-23 22:15 UTC)

<p>Yes, these windows path length limitations are pretty much global.  I believe <a class="mention" href="/u/lassoan">@lassoan</a> maybe said there’s a way to enable a longer path mode?  I don’t use windows much.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="206" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>By the way, I asked my Unit Head for permission to put 3D MPR back out in Slicer open source. He is looking into it. He’s going to ask the legal folks. I’m trying to get it done before I retire in December.</p>
</blockquote>
</aside>
<p>That would be great - let us know if speaking to one of us could help answer any questions they have.  I and others have worked with many institutions about their use of and contributions to Slicer.</p>

---

## Post #208 by @lassoan (2021-11-24 04:15 UTC)

<p>Paths to DICOM files can easily get extremely long when they are named automatically based on long DICOM tags (UIDs, series description, etc.).</p>
<p>About 1-2 years ago we implemented automatic filename generation from cryptographic hash of UIDs for filenames that are copied into Slicer’s DICOM database. Therefore, copying DICOM files into the database is very unlikely to fail due to path length limitations.</p>
<p>However, if the input files already have longer paths than MAX_PATH_LIMIT (about 260 characters), created using UNC paths or application with long path support then Slicer most likely cannot read those files. I’ve added some details about how long file support could be added to <a href="https://github.com/Slicer/Slicer/issues/6037">this issue</a>, but in the short term we need to keep avoiding paths longer than 260 characters on Windows.</p>

---
