---
topic_id: 14530
title: "Orthogonal And Oblique Mpr Slicing And Fusion"
date: 2020-11-10
url: https://discourse.slicer.org/t/14530
---

# Orthogonal and Oblique MPR Slicing and Fusion

**Topic ID**: 14530
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/orthogonal-and-oblique-mpr-slicing-and-fusion/14530

---

## Post #1 by @spycolyf (2020-11-10 21:01 UTC)

<p>Hi, I’m Doug Porter from the Mayo Clinic. We have an application that we developed in-house called QREADS which runs in MS Windows and is used by our clinicians. We are looking to expand it’s capabilities from being a simple 2D medical image viewer, to including some 3D functionality. What would be perfect and productive is a simple open source executable program that we could launch from QREADS to which we could pass the path of CT, MR or NM DICOM files, and allow our physicians to perform orthogonal (sagittal, coronal and axial) and oblique MPR triangulation. ALSO, we need a simple UI for volume slice Fusion; co-registration of CT PET MR and SPECT. I understand that this is a Slicer group. But would anyone know how we could acquire such an app? I’ve been modifying a download of FourPanesViewer to meet out needs, but it’s going to require a lot more work. I suspect there is something in Slicer that can be separated out that could receive a DICOM path and perform MPR triangulations. I’ve been in conversation with David Gobbi and he has been really helpful with using his decompression and using CMake, but CMake is very complicated to say the least. I need help from the VTK/ITK experts like yourselves.</p>
<p>If you have MPR Slicer code that I can isolate as a separate app and pass a DICOM path to and branch to from QREADS, that would save us so many headaches…</p>
<p>Thanks,</p>
<p>Doug Porter<br>
Mayo Clinic Software Developer</p>

---

## Post #2 by @pieper (2020-11-10 22:48 UTC)

<p>Hi Doug -</p>
<p>I can’t promise anything will be simple, but certainly a program like you describe is <em>possible</em> using Slicer as a base.  Most of the complex infrastructure already exists (dicom parsing, MPR display, linear and nonlinear transforms, annotation tools), and everything you need is exposed for python scripting.  It would just be a matter of setting up a startup script that configures the application to meet your needs, no doubt by hiding a lot of unneeded interface elements.  Something similar can be done with C++ if that’s a preference, but python is typically more productive given the choice.</p>
<p>Perhaps others on this forum can give you a sense of how long it takes to get up to speed as a newcomer to Slicer and become productive at adapting it.</p>
<p>-Steve</p>

---

## Post #3 by @spycolyf (2020-11-11 18:12 UTC)

<p>Hi Steve,</p>
<p>Thank you for your response. Sounds like Python is the new love in the industry. So, I need to modify our current Java app called QREADS. To deploy it to 30,000 Mayo Clinic Windows 10 PCs, we simply copy files to the user’s system with no user intervention for installation. In the attached video, I modified a version of FourPanesView and I launch it from QREADS via a dropdown MPR menu item selection, pass it the DICOM file path, and QREADS control returns after the user is done with the UI.</p>
<p>(PLEASE VIEW THE ATTACHED 2 minute VIDEO):</p>
<pre><code>   https://www.dropbox.com/s/okffj0eal4hxn52/QREADS_3D_MPR_Only.mp4?dl=0
</code></pre>
<p>Two questions:</p>
<ol>
<li>Would I still be about to easily deploy to 30,000 workstation?</li>
<li>Would the user experience still be a smooth transition from QREADS to Splicer and back to QREADS?</li>
</ol>

---

## Post #4 by @spycolyf (2020-11-11 18:13 UTC)

<p>          </p><div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/okffj0eal4hxn52/QREADS_3D_MPR_Only.mp4?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/okffj0eal4hxn52/QREADS_3D_MPR_Only.mp4?dl=0" rel="noopener nofollow ugc">https://dl.dropboxusercontent.com/s/okffj0eal4hxn52/QREADS_3D_MPR_Only.mp4?dl=0</a>
            </video>
          </div>


---

## Post #5 by @pieper (2020-11-11 18:25 UTC)

<p>Hi Doug -</p>
<p>Thanks for the video, that helps.  Yes, Slicer could be used to implement that (plus more if it were needed).  Slicer works on Windows 10, but also mac and linux if that ever were needed.  It also is just a user install (no admin needed).  The main downside I can think of is that the Slicer installation is pretty big if all you use is the MPR modes.</p>
<p>Not sure about the transition back and forth.  They would be two applications so maybe some work would be needed by the user or you could automate something at the system level.</p>
<p>Perhaps more of a departure from your current implementation but you might also consider using the web-based <a href="https://ohif.org/">OHIF</a> as a platform.  It also supports MPR and slab rendering, and is zero-install (just runs in browser, as long as it’s fairly recent).  You also need to figure out how best to serve the data for that.</p>
<p>Here’s an example you can test.  Click the “2D MPR” tool to experiment with that.</p>
<p><a href="https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.6279.6001.224985459390356936417021464571?seriesInstanceUID=1.2.276.0.7230010.3.1.3.0.57823.1553343864.578877,1.3.6.1.4.1.14519.5.2.1.6279.6001.273525289046256012743471155680" class="onebox" target="_blank" rel="noopener">https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.6279.6001.224985459390356936417021464571?seriesInstanceUID=1.2.276.0.7230010.3.1.3.0.57823.1553343864.578877,1.3.6.1.4.1.14519.5.2.1.6279.6001.273525289046256012743471155680</a></p>
<p>So there are several good options for you to consider.</p>
<p>-Steve</p>

---

## Post #6 by @spycolyf (2020-11-11 18:33 UTC)

<p>Could I use a browser object within my app inside of a window or java composite?</p>

---

## Post #7 by @pieper (2020-11-11 18:36 UTC)

<p>Hmm, maybe.  I don’t know much about current Java.  But you could open a browser tab I guess.</p>

---

## Post #8 by @lassoan (2020-11-11 19:21 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="14530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The main downside I can think of is that the Slicer installation is pretty big if all you use is the MPR modes</p>
</blockquote>
</aside>
<p>If install size is an issue then you can create a minimal build of the application, which only contains components that you need. Its size would be probably about 500-600MB (200-250MB zip file). With some work, we could reduce number of included VTK packages, remove some more dependencies, shaving off potentially an additional 100-200MB.</p>
<p>If you need to pass data between Slicer and your external application then Slicer can open a web server interface, so that you can remote control it and collect data using REST API.</p>
<p>What is the role of QREADS? Does it just connect to PACS and query/retrieves data? Or has other specialized functions?</p>

---

## Post #9 by @spycolyf (2020-11-11 20:56 UTC)

<p>Oh Hi Andras! We can communicate here. QREADS was first  written back in the 90’s when DICOM implementation was fairly new. It is client server based and very scalable. The server does al of the the work and maintains short term image storage on file servers while archiving into long term using DICOM communication to store and retrieve. The QREADS server is very scalable and can handle Mayo on the enterprise level for all of the sites around the country. The QREADS server streams images down to a folder on the local QREADS client viewer workstation of which there are around 30,000 in quantity. It’s surprisingly fast for the load it has to handle and other vendors are much too expensive to replace this infrastructure. The major complaint about QREADS is that MPR and Fusion are not supported and that’s my quest. The demo is my prototype to the docs but it was a pretty tedious endeavor. I am 66 years old and this is my last hurrah before retirement which is becoming more and more tempting. Needless to say, I don’t want to spend the next 5 years reinventing the wheel <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #10 by @spycolyf (2020-11-11 21:03 UTC)

<p>Hey Steve, could the browser code be downloaded and executed locally to access a local folder? Or does it implement DICOM query/retrieves? How did you load the data in the Browser?</p>

---

## Post #11 by @lassoan (2020-11-11 21:40 UTC)

<p>Nowadays, basic viewing features (including MPR and fusion) are expected to be available in the web browser (and they are available, for free, for example in OHIF viewer). For more advanced annotation/segmentation/analysis you would launch another web application or a local application (such as 3D Slicer) from the web browser.</p>
<p>If QREADS already uses DICOM PACS servers for storage and retrieval with standard DIMSE or DICOMweb interface then OHIF and Slicer should be able to connect directly to them already, query what is available on the server, show patient/study/series list, retrieve and display what the user needs, and even edit/annotate data, and push it back to the DICOM server. Probably some enhancements are needed to reach full feature parity with your existing solution (e.g., provide advanced query options, make sure performance is good even if you have tens of millions of studies, configure user authentication/access control, …), but this would not be a tremendously big effort and there would be synergies with various projects, so you would not need to do it all by yourself.</p>

---

## Post #12 by @spycolyf (2020-11-13 18:53 UTC)

<p>Ok, of all of the 30,000 standard Mayo PCs my development one had somehow been down graded to OpenGL 1.0. I didn’t suspect this because it worked 2 weeks ago. Anyway, sorry for the waste of time and stress. Slicer is good now. Now I can try some of your suggestions. Thank you so much.</p>

---

## Post #13 by @lassoan (2020-11-13 18:53 UTC)

<p>Do you have an NVidia GPU in your developer computer?</p>

---

## Post #14 by @spycolyf (2020-11-13 19:09 UTC)

<p>No it’s an Intel card, but it works now. So, I’m good. I tried the script you suggested. See below…</p>
<p>“C:\ProgramData\NA-MIC\Slicer 4.11.20200930\Slicer.exe” --no-splash --python-code “setToolbarsVisible(False); setMenuBarsVisible(False); slicer.app.processEvents(); mainWindow().findChildren(‘QDockWidget’,‘PanelDockWidget’)[0].hide(); slicer.app.processEvents(); loadVolume(r’H:\VTKTest\Images4VTK\CTChestThinSlice’)”</p>
<p>Slicer comes up fine. I’m specifying a folder to the loadVolume function, not a file. Also the images are compressed DICOM. No images load though. What am I doing wrong?</p>
<p>Thanks,</p>
<p>Doug</p>

---

## Post #15 by @lassoan (2020-11-13 19:38 UTC)

<p>There are a couple of ways to load DICOM data into Slicer. The method that I described requires a filename as inputs and that all data in the series are stored in that same folder. How to launch Slicer from command line to view a DICOM data set is a slightly different from the scope of this discussion, so it would be great if you could post it as a new topic.</p>

---

## Post #16 by @spycolyf (2020-11-13 20:47 UTC)

<p>OK Thanks! I’ll try that single file thing now.</p>

---

## Post #17 by @spycolyf (2020-11-16 19:09 UTC)

<p>OK, I obviously lack the knowledge and experience with Slicer that I need in order to solve my problems without being spoon-fed by y’all experts. How do I catch up? Are there good beginner tutorials out there that would teach me how to do what I need to do? Thanks.</p>

---

## Post #18 by @pieper (2020-11-16 19:21 UTC)

<p>Yes, it can be hard to learn.</p>
<p>Did you find the developer resources here?  Were they helpful?</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" target="_blank" rel="noopener">Documentation/4.10/Training - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #19 by @lassoan (2020-11-16 19:21 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">PerkLab’s Slicer bootcamp training material</a> is a good start, especially the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">Scripting and module development tutorial</a>. You can also check out <a href="https://github.com/SlicerMorph/SlicerMorph#3d-morphometrics-and-image-analysis-short-course-materials">SlicerMorph tutorials</a>.</p>
<p>It is not a problem if you ask here anything - next time someone will have the same question will find it on Google, so it is a good investment of our time.</p>

---

## Post #20 by @spycolyf (2020-11-16 19:45 UTC)

<p>Thanks Steve, I’ll go there to read.</p>
<p>OK, I’ll consider this as a slicer-documenting forum.</p>
<p>So where were we? So here is what I get when I issue the following command. Just one frame not orthogonal slices generated and I can’t scroll through the axials.</p>
<p>“C:\ProgramData\NA-MIC\Slicer 4.11.20200930\Slicer.exe” --no-splash --python-code “setToolbarsVisible(False); setMenuBarsVisible(False); slicer.app.processEvents(); mainWindow().findChildren(‘QDockWidget’,‘PanelDockWidget’)[0].hide(); slicer.app.processEvents(); loadVolume(r’H:\VTKTest\Images4VTK\CTChestThinSlice’)”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed8022078a8e8b7e3ef7aafb178dee40b19d1fe5.jpeg" data-download-href="/uploads/short-url/xT1GpoWtksOTVNARjkE8bEUXCkd.jpeg?dl=1" title="SlicerCommandResult" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed8022078a8e8b7e3ef7aafb178dee40b19d1fe5_2_539x500.jpeg" alt="SlicerCommandResult" data-base62-sha1="xT1GpoWtksOTVNARjkE8bEUXCkd" width="539" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed8022078a8e8b7e3ef7aafb178dee40b19d1fe5_2_539x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed8022078a8e8b7e3ef7aafb178dee40b19d1fe5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed8022078a8e8b7e3ef7aafb178dee40b19d1fe5.jpeg 2x" data-dominant-color="605F6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerCommandResult</span><span class="informations">635×589 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #21 by @lassoan (2020-11-16 23:39 UTC)

<p>Is only a single slice loaded? Do you see image in the other views if you click the “Reset field of view” button (rectangle button next to the slice slider)?</p>

---

## Post #22 by @spycolyf (2020-11-17 15:54 UTC)

<p>Yes, only one slice. Nothing in the other panes. The folder contains 2,271 images.</p>
<p>Correction to the command:</p>
<p>, I did specify a single file in that command, not just a folder. So the correction is here…</p>
<p>“C:\ProgramData\NA-MIC\Slicer 4.11.20200930\Slicer.exe” --no-splash --python-code “setToolbarsVisible(False); setMenuBarsVisible(False); slicer.app.processEvents(); mainWindow().findChildren(‘QDockWidget’,‘PanelDockWidget’)[0].hide(); slicer.app.processEvents(); loadVolume(r’H:\VTKTest\Images4VTK\CTChestThinSlice\Slice_1.dcm’)”</p>

---

## Post #23 by @lassoan (2020-11-17 21:08 UTC)

<p>Does the folder contain multiple series? If yes, then it is better to index the folder and load using DICOM module.</p>
<p>An example for loading all series from a folder is available here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder</a></p>
<p>Performance can be improved if you have an idea what kind of data set you want to load (by default all possible interpretations of an image set will be evaluated and the best fit will be loaded, but going through all these interpretations take some time).</p>

---

## Post #24 by @spycolyf (2020-11-18 15:09 UTC)

<p>No, it’s just one thin slice CT series and I’m specifying only 1 frame of that single frame series. It is rather huge. Maybe I should try a smaller series. But it should handle large series.</p>

---

## Post #25 by @spycolyf (2020-11-19 15:51 UTC)

<p>Andras, I just viewed the document in the link you sent. Thanks. I’ll study that for a bit. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #26 by @spycolyf (2020-11-19 16:08 UTC)

<p>A question about oblique slicing: Is there a way to show orientation labels on each of the 3 orthogonal views as we rotate the slice cursors?</p>

---

## Post #27 by @spycolyf (2020-11-19 16:39 UTC)

<p>That’s not a slicer question, it’s a VTK programming question. Thanks.</p>

---

## Post #28 by @spycolyf (2020-12-01 20:15 UTC)

<p>YES! THIS WORKED!</p>
<p>Slicer.exe --python-code “slicer.util.loadVolume(‘C:/DICOMImages//CTSlice.dcm’, <em>{‘singleFile’: False}</em>)”</p>
<p>singleFIle=false</p>

---

## Post #29 by @lassoan (2020-12-01 21:09 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="26" data-topic="14530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Is there a way to show orientation labels on each of the 3 orthogonal views as we rotate the slice cursors?</p>
</blockquote>
</aside>
<p>You can enable orientation marker in views using slice/3D view controllers or using this code snippet: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_orientation_marker_in_all_views" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #30 by @spycolyf (2020-12-02 20:15 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a>, are you familiar with the code that was used to generate the QtVTKRenderWindows? A guy named Sankhesh Jhaveri developed it. do you know him?</p>
<p>Thanks</p>

---

## Post #31 by @lassoan (2020-12-03 02:53 UTC)

<p>Yes, we collaborate with Sankhesh and other Kitware engineers on QVTKOpenGLNativeWidget/QVTKOpenGLWidget/QVTKWidget to have VTK rendering working in Slicer and ParaView. Right now, he is working on bugs in VTK9 that we discovered when trying to upgrade Slicer to use VTK9.</p>

---

## Post #32 by @spycolyf (2020-12-04 15:55 UTC)

<p>Great! I’m happy to know that you’re working on bugs in VTK9 and that he is still involved. Thanks!</p>

---

## Post #33 by @spycolyf (2020-12-11 17:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Does slicer have a Fusion UI?</p>

---

## Post #34 by @lassoan (2020-12-11 17:12 UTC)

<p>Yes. In slice views you can fuse two volumes, a labelmap volume, and any number of segmentation, models, and markup layers. In 3D views, you can superimpose any kind and number of data objects.</p>

---

## Post #35 by @spycolyf (2020-12-11 18:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> is the code written in such a way that I can extract the fusion function from Slicer to make a stand alone app?</p>

---

## Post #36 by @lassoan (2020-12-11 19:16 UTC)

<p>The blending pipeline is implemented here: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx">https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx</a></p>
<p>What was the reason not to go with Slicer? Large install package? Startup time?</p>

---

## Post #37 by @spycolyf (2020-12-11 20:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> - I think I just don’t know how to do it. I tried different things and can’t get it to work. Would you be patient enough to see me through to getting it to work? I know you’re really busy.</p>

---

## Post #38 by @spycolyf (2020-12-11 20:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> ow thanks for that code. Looks interesting. So, I’m assuming the I would write all of the GUI and when ready to blend between volumes or images, I would call this function to create the output blended image. Correct?</p>

---

## Post #39 by @spycolyf (2020-12-11 20:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  I appeared before the Mayo Applications committee yesterday and proposed my QREADS 3D MPR and Fusion expansion or plugin ideas to them. One of their big requests was to have the UI look and feel match that of our QREADS application as much as possible. This may be another reason to try isolating the code to create a stand alone app that I can have full control of the look and feel as well as loading faster than a full Splicer would. It would also need to read DICOM files directly from disk.</p>

---

## Post #40 by @pieper (2020-12-11 20:46 UTC)

<p><a class="mention" href="/u/spycolyf">@spycolyf</a> - if the QTREADS 3D UI is probably feasible to implement in Qt.  Then you could just use the Slicer logic classes underneath.</p>

---

## Post #41 by @spycolyf (2020-12-11 20:46 UTC)

<p>If I could do this I could give some recognition to the Slicer team to Mayo.</p>

---

## Post #42 by @spycolyf (2020-12-11 20:51 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<p>OK, I’ll give that some thought. Has anyone else done something similar?</p>

---

## Post #43 by @jcfr (2020-12-11 20:59 UTC)

<blockquote>
<p>One of their big requests was to have the UI look and feel match that of our QREADS application as much as possible.</p>
</blockquote>
<p><a class="mention" href="/u/spycolyf">@spycolyf</a>  This make sense. I just sent you a direct message with some suggestions to move forward with this by collaborating with Kitware.</p>

---

## Post #44 by @spycolyf (2020-12-11 21:34 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> OK, I’ll take a look.</p>

---

## Post #45 by @pieper (2020-12-11 21:45 UTC)

<p>There are several examples in the Slicer tests that could serve as inspiration.  Or if you can get help from experts, as <a class="mention" href="/u/jcfr">@jcfr</a> suggests that could really help get you over the initial hurdles and customize from there.</p>

---

## Post #46 by @spycolyf (2020-12-11 22:00 UTC)

<p>The first hurdle for me is to have a successful process for downloading source code and get it running successfully. I’ll try to get Slicer working in debug mode inside of Visual Studio 2017. Is that doable with some ease?</p>

---

## Post #47 by @pieper (2020-12-11 22:11 UTC)

<p>I haven’t used 2017 in a while, but I have used VS 2019 with no problems lately.  Building Slicer can be a challenge when you try to improvise, but if you follow the instructions exactly you should have no problems.</p>

---

## Post #48 by @spycolyf (2020-12-11 23:17 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> - Oh. Did I miss some thing? Where are those instructions. I 'll look on the website. Thanks.</p>

---

## Post #49 by @lassoan (2020-12-11 23:21 UTC)

<p>Build instructions are here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html</a></p>
<p>You cam start with this to ensure you have set up everything correctly, and then <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">create a custom application</a>, where you can customize everything in C++.</p>

---

## Post #50 by @spycolyf (2020-12-11 23:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Cool! I’ll keep you posted. You are so good and generous with your time. Thank you and have a great weekend and stay safe.</p>

---

## Post #51 by @spycolyf (2021-01-18 18:27 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a></p>
<p>I’ve been off learning QT Creator and I built Slicer Release and debug. Wow! QT is powerful and Slicer is huge! I’m looking at the Slicer code in VS 2019. It’s overwhelming.</p>
<p>QT is the best and most flexible visual IDE WYSIWYG that I’ve used in my career. Here’s what I did with it so far. I designed the QREADS Toolbar…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68e181ad7713ad8027d8e2fe663221c94ccd2117.jpeg" data-download-href="/uploads/short-url/eXONKLtUvnAoPwCqmJLEJTgmqZV.jpeg?dl=1" title="QTQREADSToolBar" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68e181ad7713ad8027d8e2fe663221c94ccd2117_2_149x500.jpeg" alt="QTQREADSToolBar" data-base62-sha1="eXONKLtUvnAoPwCqmJLEJTgmqZV" width="149" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68e181ad7713ad8027d8e2fe663221c94ccd2117_2_149x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68e181ad7713ad8027d8e2fe663221c94ccd2117_2_223x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68e181ad7713ad8027d8e2fe663221c94ccd2117_2_298x1000.jpeg 2x" data-dominant-color="988A86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">QTQREADSToolBar</span><span class="informations">312×1046 51.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After I create all of my widgets, if I want to use the resulting .ui file in Visual Studio, do I need to write any C++ code in QT? Or is all of the coding done in VS? Or a combination? If the coding is only done in VS, then I guess I’m done with using QT Creator, correct?</p>
<p>Thanks.</p>

---

## Post #52 by @spycolyf (2021-01-18 18:53 UTC)

<p>Hello Hello <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a>,</p>
<p>I would like to introduce Liqin Wang (<a class="mention" href="/u/liqin">@Liqin</a>), who is my teammate on this project. She is also a Mayo IT employee and she will be joining in at some point after she’s done with her current priority project working on our specialized DICOM receiver, processor and short term storage. She has some ITK experience.</p>
<p>Thanks</p>

---

## Post #53 by @lassoan (2021-01-18 18:54 UTC)

<p>Thanks for the introduction.</p>
<p><a class="mention" href="/u/liqin">@Liqin</a> welcome to the Slicer community! Let us know if we can help with anything.</p>

---

## Post #54 by @spycolyf (2021-01-25 15:53 UTC)

<p><a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a>, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I’ve spent a couple of days trying to get a my QPushButton to fire and signal and recognizing a slot. The strange thing is I’ve gotten gotten other button to work perfectly, and I set up this button the same exact way as the ones that work. But when the connect statement is executed on this one I get …</p>
<pre><code class="lang-auto">QObject::connect: No such slot QtVTKApp::setWidgetsEnabled()
</code></pre>
<p>I read something in StackOverflow that referenced the “moc_classname.cpp” file. Should that file be recreated every time I build? And if so, what do I do to fix it if it’s not recreating? Please let me know if you need clarification. Thanks.</p>

---

## Post #56 by @spycolyf (2021-01-25 18:10 UTC)

<p><a href="https://discourse.slicer.org/u/spycolyf"><img src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/90.png" alt="" width="45" height="45"></a></p>
<p><a href="https://discourse.slicer.org/u/spycolyf">spycolyf</a><a href="https://discourse.slicer.org/u/spycolyf">Doug Porter</a></p>
<p><a href="https://discourse.slicer.org/t/orthogonal-and-oblique-mpr-slicing-and-fusion/14530/55">2h</a></p>
<p>Here is the statement that generates the “No such slot” message…</p>
<pre><code class="lang-auto">connect(this-&gt;ui-&gt;setWidgetsEnabledToggle, SIGNAL(pressed()), this, SLOT(setWidgetsEnabled()));

virtual void setWidgetsEnabled();
</code></pre>
<p>the clickable property is set to true to make it a toggle.</p>

---

## Post #57 by @lassoan (2021-01-25 19:22 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="54" data-topic="14530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>QObject::connect: No such slot QtVTKApp::setWidgetsEnabled()</p>
</blockquote>
</aside>
<p>I don’t know what is a QtVTKApp, probably it is an alternative to a Slicer-based application. We can help with debugging issues that you can reproduce in Slicer.</p>

---

## Post #58 by @spycolyf (2021-01-25 20:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I just solve my problem. FYI: QtVTKApp is just a generic name I made up just to use as an example for this post.</p>
<p>I found my problem. Lesson learned: You can’t just make a copy of a VS C++ QT project and try to work from that copy without changing a bunch of paths in a few project files (my ignorance for not knowing CMake.)</p>
<p>The Meta-Object Compiler (MOC) is what makes signals and slots work and it’s automatically launched whenever you build a QT project in Visual Studio C++; and because I was working from a copy of the original project, the MOC AutogenInfo.json contained paths to the wrong mocs_compilation.cpp and other files. As a result, I was seeing no change when adding new events, and the new slots were not recognized. So I had to modify the AutogenInfo.json file to point to the current project and it worked fine afterwards.</p>
<p>I hope this can help others, but knowing CMake would help the most.</p>
<p>Thanks.</p>

---

## Post #59 by @lassoan (2021-01-25 20:46 UTC)

<p>I see, it makes sense. It’s good that you could figure it out. We’ll try to be more helpful next time.</p>

---

## Post #60 by @spycolyf (2021-01-26 16:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="59" data-topic="14530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We’ll try to be more helpful next time.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>No no, I don’t expect you to have solutions to all of my dumb mistakes. My apologies for taking up so much of your time. I’m just happy that I can contribute my issues and solutions to the forum to help others.</p>

---

## Post #61 by @spycolyf (2021-01-26 21:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a></p>
<p>Hi, I’m trying to dynamically change the window level of images after I push button to change the W/L.</p>
<pre><code class="lang-auto"> vtkSmartPointer&lt; vtkResliceImageViewer &gt; riw;
</code></pre>
<p>… read in and displayed images.</p>
<pre><code class="lang-auto">riw-&gt;GetWindowLevel()-&gt;SetWindow(400);
riw-&gt;GetWindowLevel()-&gt;SetLevel(40);|
riw-&gt;Render();
</code></pre>
<p>This does not display the new W/L immediately but does so when I use the mouse interactively. I.e., after the code is executed there is no change; then when I press the left button down and move the mouse, the new W/L shows.</p>
<p>What is the correct way to accomplish this?</p>

---

## Post #62 by @lassoan (2021-01-26 22:13 UTC)

<p>Where does this vtkResliceImageViewer come from? Do you place custom VTK actors in renderers in Slicer?</p>

---

## Post #63 by @spycolyf (2021-01-26 22:23 UTC)

<p>OK, I think I should be posting this is a general VTK forum. I’m not doing this in Slicer. Sorry. <img src="https://emoji.discourse-cdn.com/twitter/neutral_face.png?v=9" title=":neutral_face:" class="emoji" alt=":neutral_face:"></p>

---

## Post #64 by @lassoan (2021-01-27 02:49 UTC)

<p>I just asked this because we have a mechanism to manage rendering requests in Slicer, but there is no such thing in VTK. So, the answer is different in a plain VTK render window than a render window in Slicer.</p>
<p>For quick prototyping it might make sense try a vtkResliceImageViewer, but the current image reslice widgets are not too far from what vtkResliceImageViewer can do, so that may be a good option, too (slightly more work, but has long-term benefits). <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is currently working on adding ROI markup widget and in scope of this activity he may move draggable handles out from markups so that other components (such as slice intersection widgets) could utilize it. With some coordination of this effort, it might be not too much development work to make slice intersections and slice view boundaries draggable.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> what do you think? How difficult would be to add markups plane widget-like features to slice and 3D views (translate, rotate, change slice thickness of slices) without redeveloping handles from scratch?</p>

---

## Post #65 by @spycolyf (2021-01-27 15:24 UTC)

<p>To be clear, you’re saying that currently, Slicer does not have draggable handles for translating, rotating, and changing slice thickness of slice intersection widgets, correct? I could live without having handles for changing thickness; it’s probably easier and more intuitive to set thickness with a slider and/or entering a value in a text box. But for oblique slicing, using translation and rotation handles are most intuitive.</p>

---

## Post #66 by @jcfr (2021-01-27 15:30 UTC)

<blockquote>
<p>for oblique slicing, using translation and rotation handles are most intuitive.</p>
</blockquote>
<p>The existing support is available through the “Reformat” widget, it can enabled using this icon:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82de918a5c782eccfe58304ecbd7a4e136cdd938.png" alt="image" data-base62-sha1="iFIVachPVvVpgsqoWO1u06qRpna" width="47" height="46"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/961238bce03bcd0625e7f374835ba5a15714d425.png" alt="image" data-base62-sha1="lpAEVWe2S49dHZx0A1Ne2Fm1lS5" width="311" height="45"></p>
<p>Once enabled, this widget is available in the 3d viewer:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22a75180de13ba0e403be7f108edb48b84d7ae8d.png" alt="image" data-base62-sha1="4WyI8KSOLijUKJKzxqkgPCeFi6V" width="480" height="390"></p>

---

## Post #67 by @Sunderlandkyl (2021-01-27 16:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I don’t think it should be too much work to move the interaction handle pipeline to a more general location. I’ll start looking into it</p>

---

## Post #68 by @lassoan (2021-01-27 16:15 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="65" data-topic="14530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Slicer does not have draggable handles for translating, rotating, and changing slice thickness of slice intersection widgets, correct?</p>
</blockquote>
</aside>
<p>The widgets are draggable in 3D view as <a class="mention" href="/u/jcfr">@jcfr</a> showed above. In slice views, you can move slice intersection by holding down Shift key and rotate slice intersections by Ctrl-Alt + left-click-and-drag. These mouse&amp;keyboard gestures are very effective and keep the image viewers clean, but not easily discoverable for newcomers, so it may be useful to allow dragging the intersections using visible handles.</p>

---

## Post #69 by @spycolyf (2021-01-27 18:03 UTC)

<p>This all sounds great. I look forward to seeing it all come together. Thanks.</p>

---

## Post #70 by @spycolyf (2021-01-27 19:10 UTC)

<p>By the way, the answer to my window/level issue earlier was to use vtkResliceImageViewer’s base class, vtkImageViewer2 methods, SetColorWindow and SetColorLevel.</p>
<pre><code>        vtkSmartPointer&lt; vtkResliceImageViewer &gt; riw;
        riw-&gt;SetColorWindow(400);
        riw-&gt;SetColorLevel(40);
</code></pre>
<p>Using these set the W/Ls immediately <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #71 by @spycolyf (2021-01-28 19:06 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Does a VTK reference manual exist that contains examples of how to use functions like vtkImageSlabReslice-&gt;SetSlabThickness(thickness); How do I set the thickness and show the change in the thickness reference lines on the image. Here my code and nothing happens …</p>
<p>void QtVTKRenderWindows::SetSlabThickness(double thickness)<br>
{<br>
if (debug_mode) std::cout &lt;&lt; "SetSlabThickness = " &lt;&lt; thickness &lt;&lt; std::endl;<br>
for (int i = 0; i &lt; 3; i++)<br>
{<br>
vtkImageSlabReslice* thickSlabReslice = vtkImageSlabReslice::SafeDownCast(<br>
vtkResliceCursorThickLineRepresentation::SafeDownCast(<br>
riw[i]-&gt;GetResliceCursorWidget()-&gt;GetRepresentation())-&gt;GetReslice());<br>
thickSlabReslice-&gt;SetSlabThickness(thickness);<br>
riw[i]-&gt;GetRenderer()-&gt;ResetCamera();<br>
riw[i]-&gt;Render();<br>
}<br>
}</p>

---

## Post #72 by @lassoan (2021-01-28 19:31 UTC)

<p>Setting the slab thickness is tricky. I remember that I had trouble figuring out how exactly it has to be specified (I think it is not set in mm but in image space or something like that). Have look at the documentation, if that does not clarify it then fall back to the source code, and if all these fail then ask David Gobbi on the VTK forum.</p>

---

## Post #73 by @spycolyf (2021-01-28 20:05 UTC)

<p>Hmm… GetSlabThickness returns the thickness in mm, it just seems SetSlabThickness would allow you to change the thickness in the same units. OK. I’ll ask in the VTK forum because this is still a vtkResliceImageViewer quetion.</p>

---

## Post #74 by @jcfr (2021-01-28 22:06 UTC)

<p>A post was split to a new topic: <a href="/t/web-application-based-on-vtk-js/15725">Web application based on vtk.js</a></p>

---

## Post #75 by @spycolyf (2021-02-11 15:37 UTC)

<p>Hello <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/superlib">@superlib</a></p>
<p>I’m very grateful for the amazing help you’ve given us here ay Mayo. No other way would I have gotten through my issues. Your service to the 3D imaging development community is extremely valuable and in the end, helps the patient, and the patient’s wellbeing is always our top priority. We all contribute to saving lives. Thanks you!</p>

---

## Post #76 by @lassoan (2021-02-11 21:30 UTC)

<p>Thank you! Could you write this (maybe copy, maybe add one sentence for some context) as a topic in this category?</p>
<aside class="onebox category-onebox" style="box-shadow: -5px 0px #92278F;">
  <article class="onebox-body category-onebox-body">
    <h3>
      <a class="badge-wrapper bullet" href="/c/community/success-stories/29">
          <span class="badge-category-bg" style="background-color: #92278F"></span>
        <span class="clear-badge"><span>Success stories</span></span>
      </a>
    </h3>
      <div>
        <span class="description">
          <p>This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos.</p>
        </span>
      </div>
  </article>
  <div class="clearfix"></div>
</aside>

<p>Maybe it is too early to say it is “Success story” yet, so it is up to you, you can post it later, when you managed to actually deploy it. Anyway, happy to see that you are happy.</p>

---

## Post #77 by @spycolyf (2021-02-12 17:01 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/superlib">@superlib</a></p>
<p>Question: Do any of you know Dan Blezek, Brad Erickson or Bill Ryan here at mayo? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>They definitely know <a class="mention" href="/u/pieper">@pieper</a> from way back.</p>

---

## Post #78 by @pieper (2021-02-12 17:22 UTC)

<p>Oh yes indeed.  Say hello to them all!</p>

---

## Post #79 by @spycolyf (2021-02-19 21:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="76" data-topic="14530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe it is too early to say it is “Success story” yet, so it is up to you, you can post it later, when you managed to actually deploy it. Anyway, happy to see that you are happy.</p>
</blockquote>
</aside>
<p>Oh OK, yes you’re correct. I’ll remove it for now.</p>

---
