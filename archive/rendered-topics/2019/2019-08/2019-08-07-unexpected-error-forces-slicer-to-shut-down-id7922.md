# Unexpected error forces Slicer to shut-down

**Topic ID**: 7922
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/unexpected-error-forces-slicer-to-shut-down/7922

---

## Post #1 by @dfafalis (2019-08-07 17:15 UTC)

<p>I keep getting the error shown in the attached pic.<br>
Slicer will stop working and eventually will shut down.<br>
What could be causing this behavior?</p>

---

## Post #2 by @lassoan (2019-08-07 17:21 UTC)

<p>It seems that the attachment did not come through. Could you please try to upload the image again?</p>
<p>Applications typically crash when you run out of memory. How much RAM do you have in your computer and how large is the image that you are working with?</p>

---

## Post #3 by @dfafalis (2019-08-07 17:38 UTC)

<p>Hello.</p>
<p>Here is the attachment.</p>
<p>The project I am working on has a size of 3GB. The installed RAM is 56GB.</p>
<p>I have also increased the cache size to 100GB.</p>
<p>The program was working properly for a long time. It started crashing during my last operations.</p>
<p>Thanks for your help. Regards</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ce97fe17d00c850a2e96857cffd91b2a7bd6ae.jpeg" data-download-href="/uploads/short-url/4XURfZYrthjUc0YMyPXngkNqEbA.jpeg?dl=1" title="Slicer_Error.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ce97fe17d00c850a2e96857cffd91b2a7bd6ae_2_690x431.jpeg" alt="Slicer_Error.png" data-base62-sha1="4XURfZYrthjUc0YMyPXngkNqEbA" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ce97fe17d00c850a2e96857cffd91b2a7bd6ae_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ce97fe17d00c850a2e96857cffd91b2a7bd6ae_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ce97fe17d00c850a2e96857cffd91b2a7bd6ae_2_1380x862.jpeg 2x" data-dominant-color="BCBFC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Error.png</span><span class="informations">1679×1049 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-08-07 17:51 UTC)

<p>What effects did you use? Could you attach the application log of the session where the crash occurred? (menu: Help/Report a bug)</p>

---

## Post #5 by @dfafalis (2019-08-07 18:41 UTC)

<p>Hi Andras,</p>
<p>I was using the “Paint” effect with a radius of “1%”. You can see from the attached screenshot.</p>
<p>Here is the application log:</p>

---

## Post #6 by @muratmaga (2019-08-07 19:10 UTC)

<p>Log is not attached.</p>

---

## Post #7 by @dfafalis (2019-08-07 19:58 UTC)

<p>I am sorry about that.</p>
<p>I tried once more to repeat the operations and I had the same problem.</p>
<p>Here is the log file</p>
<p>(Attachment Slicer_28257_20190807_155407.log is missing)</p>

---

## Post #8 by @dfafalis (2019-08-07 20:00 UTC)

<p>Hi there,</p>
<p>I receive an error that some attachments are not sent.</p>
<p>I resent the log file as a txt file</p>
<p>(Attachment Slicer_28257_20190807_155407.txt is missing)</p>

---

## Post #9 by @dfafalis (2019-08-07 20:02 UTC)

<p>Same error,</p>
<p>I enclose the log file within my email:</p>
<p>[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - Session start time …: 2019-08-07 15:54:08<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - Operating system …: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - Memory …: 57296 MB physical, 114607 MB virtual<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 07.08.2019 15:54:08 [] (unknown:0) - Additional module paths …: C:/Users/DF/AppData/Roaming/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules, C:/Users/DF/AppData/Roaming/NA-MIC/Extensions-28257/MarkupsToModel/lib/Slicer-4.10/qt-loadable-modules<br>
[DEBUG][Python] 07.08.2019 15:54:34 [Python] (E:\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 07.08.2019 15:54:36 [Python] (E:\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 07.08.2019 15:54:36 [Python] (E:\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 07.08.2019 15:54:37 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #10 by @lassoan (2019-08-07 20:17 UTC)

<p>This is the log of the current session. Please choose the log of the session where the crash occurred (in the “Report a bug…” dialog there is a listbox to select the session).</p>

---

## Post #11 by @dfafalis (2019-08-07 20:31 UTC)

<p>Hi Andras,</p>
<p>I think it is this one:</p>
<p>[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Session start time …: 2019-08-07 12:01:12<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Slicer version …: 4.11.0-2019-07-01 (revision 28354) win-amd64 - installed release<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Operating system …: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Memory …: 57296 MB physical, 114607 MB virtual<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 07.08.2019 12:01:12 [] (unknown:0) - Additional module paths …: C:/Users/DF/AppData/Roaming/NA-MIC/Extensions-28354/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, C:/Users/DF/AppData/Roaming/NA-MIC/Extensions-28354/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/DF/AppData/Roaming/NA-MIC/Extensions-28354/SegmentMesher/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 07.08.2019 12:01:14 [Python] (C:\Users\DF\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-01\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 07.08.2019 12:01:14 [Python] (C:\Users\DF\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-01\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 07.08.2019 12:01:14 [Python] (C:\Users\DF\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-01\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 07.08.2019 12:01:15 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 07.08.2019 12:02:20 [vtkMRMLVolumeArchetypeStorageNode (00000000144FD280)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:464) - Loaded volume from file: E:/0-Hiro_Archive/GP_2016/GP_CUT_BULLA_100%_IKI_2.7um_Al/3D_Slicer_GP_CUT_BULLA_100%_IKI_2.7um_Al_REC_d2c3_working/GP_CUT_BULLA_100%_IKI_2.7um_Al_REC_d2c3.nrrd. Dimensions: 1286x1240x1872. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][VTK] 07.08.2019 12:04:46 [vtkMRMLVolumeArchetypeStorageNode (00000000144FD460)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:464) - Loaded volume from file: E:/0-Hiro_Archive/GP_2016/GP_CUT_BULLA_100%_IKI_2.7um_Al/3D_Slicer_GP_CUT_BULLA_100%_IKI_2.7um_Al_REC_d2c3_working/Segmentation-label.nrrd. Dimensions: 1286x1240x1872. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 07.08.2019 12:04:49 [] (unknown:0) - “MRML Scene” Reader has successfully read the file “E:/0-Hiro_Archive/GP_2016/GP_CUT_BULLA_100%_IKI_2.7um_Al/3D_Slicer_GP_CUT_BULLA_100%_IKI_2.7um_Al_REC_d2c3_working/2019-07-26-Scene.mrml” “[178.57s]”<br>
[DEBUG][Qt] 07.08.2019 12:10:42 [] (unknown:0) - Switch to module:  “”</p>

---

## Post #12 by @lassoan (2019-08-08 01:16 UTC)

<p>It doesn’t seem to be the correct log either. “Switch to module:” lines indicate that you did not switch to Segment editor module in this session.</p>

---

## Post #13 by @Raid (2019-08-08 05:40 UTC)

<p>Hi,<br>
Slicer used to crash with me as well when using the scissors tool after applying the threshold,<br>
the file size I’m working on was around 5 GB, and I’m working on a really good computer…</p>
<p>I overcame this issue by:</p>
<ul>
<li>reducing the size of the data by using Image J (5 Gb to ~200000 KB) by reducing the pixels to one third.</li>
<li>cropping the exact area I wanted to segment with safety margins using (crop volume) in 3d Slicer.</li>
</ul>
<p>Finally, try to turn off the (show 3d) option when your segmenting.</p>
<p>Regards,<br>
Raid</p>

---

## Post #14 by @justdcinaus (2019-08-08 07:05 UTC)

<p>Hi<br>
Another option is that Slicer has not finished a write operation.<br>
For some of my files it was crashing as soon as I attempted to do anything after changing a volume (crop module).  I got around the error by manually saving and opening a file explorer window to the save folder.   If I attemtped to do anything in the Segment Editor module before the file write was complete I’d get a crash.</p>
<p>It may not solve your problem, but it is worth trying.</p>
<p>David</p>

---

## Post #15 by @muratmaga (2019-08-08 17:30 UTC)

<p><a class="mention" href="/u/dfafalis">@dfafalis</a> <a class="mention" href="/u/raid">@Raid</a> <a class="mention" href="/u/justdcinaus">@justdcinaus</a> I would be nice to replicate and find the specific cause of the crash, especially if it is not related to the lack memory resources on the computer.</p>
<p>For example, we had a similar crashing issue with large segmentation, and turned out to be a variable type that needs to be changed (<a href="https://discourse.slicer.org/t/segmentation-effects-crashing-slicer/7474/4" class="inline-onebox">Segmentation effects crashing Slicer</a>), and is now fixed in preview version.</p>
<p>It would be great if you can provide datasets and the exact steps that replicate the issue.</p>

---

## Post #16 by @dfafalis (2019-08-08 19:06 UTC)

<p>Hi Murat,</p>
<p>Thank you for your reply.</p>
<p>I will try to get it for you.</p>
<p>Best</p>
<p>Dimitrios</p>

---

## Post #17 by @dfafalis (2019-08-13 19:45 UTC)

<p>Hello Murat and Andras,</p>
<p>I summarize here some problems I have been encountering while using 3D Slicer.</p>
<p>I hope they will give you an insight of what may be going wrong.</p>
<p>The<br>
problems I describe happen quite often, repeatedly, and it is frustrating to see that at the end the work I had done is not saved.</p>
<p>For the problems I describe in the sequence, I used a PC (windows 10 Enterprise), 3D Slicer version 4.10.2 (the latest stable).</p>
<p>The PC I am using has 32 GB RAM, Intel(R) Xeon(R) W-2133 CPU @ 3.60Hz 3.60Hz</p>
<p>Available space on SSD hard drive: 261GB</p>
<p>A. Screenshots Slicer_Error_3ab :</p>
<p>Here, <strong>screenshot a</strong>, I tried to use the Paint effect in the regions shown by yellow arrows. Slicer returned the error message shown in screenshot <strong>screenshot b</strong>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/880cd8768ef38950c7704622a01c731f22e3be11.jpeg" data-download-href="/uploads/short-url/jpysmuA2MGuFN5Rj8RyBXnOJuTL.jpeg?dl=1" title="Slicer_Error_3ab.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/880cd8768ef38950c7704622a01c731f22e3be11_2_690x218.jpeg" alt="Slicer_Error_3ab.jpg" data-base62-sha1="jpysmuA2MGuFN5Rj8RyBXnOJuTL" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/880cd8768ef38950c7704622a01c731f22e3be11_2_690x218.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/880cd8768ef38950c7704622a01c731f22e3be11_2_1035x327.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/880cd8768ef38950c7704622a01c731f22e3be11_2_1380x436.jpeg 2x" data-dominant-color="626668"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Error_3ab.jpg</span><span class="informations">3342×1060 1.04 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>B. Screenshots Slicer_Error_3cd:</p>
<p>I Continued working on the same region as in previous screenshot:</p>
<p>After<br>
the Paint effect failed, I tried the Draw effect, <strong>screenshot c</strong> . The first time, after<br>
waiting for a while for Slicer to complete its process, the effect showed nothing. So I tried for a second time and then it worked as shown<br>
in screenshot <strong>screenshot d</strong>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55137f111a0d046e795efc27ad72ff73344812c5.jpeg" data-download-href="/uploads/short-url/c8Cm3rITtLYRF9Y3vyNwTFkF9cx.jpeg?dl=1" title="Slicer_Error_3cd.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55137f111a0d046e795efc27ad72ff73344812c5_2_690x216.jpeg" alt="Slicer_Error_3cd.png" data-base62-sha1="c8Cm3rITtLYRF9Y3vyNwTFkF9cx" width="690" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55137f111a0d046e795efc27ad72ff73344812c5_2_690x216.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55137f111a0d046e795efc27ad72ff73344812c5_2_1035x324.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55137f111a0d046e795efc27ad72ff73344812c5_2_1380x432.jpeg 2x" data-dominant-color="5D6162"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Error_3cd.png</span><span class="informations">3346×1050 824 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>C. Screenshot Slicer_Error_3e:</p>
<p>Many times, I observe this strange random positioning of circles when I want to use the Paint effect.</p>
<p>When this happens I have to either “Esc” and use another effect, or if I need to use the Paint effect, then I just let it do whatever and then I “Undo” and repeat the process.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88670f13917b6a3e354a37242fe23b47a751f920.jpeg" data-download-href="/uploads/short-url/jsFJNkuxVxrN1wuqoyKRU07eYjm.jpeg?dl=1" title="Slicer_Error_3e.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88670f13917b6a3e354a37242fe23b47a751f920_2_690x429.jpeg" alt="Slicer_Error_3e.jpg" data-base62-sha1="jsFJNkuxVxrN1wuqoyKRU07eYjm" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88670f13917b6a3e354a37242fe23b47a751f920_2_690x429.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88670f13917b6a3e354a37242fe23b47a751f920_2_1035x643.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88670f13917b6a3e354a37242fe23b47a751f920_2_1380x858.jpeg 2x" data-dominant-color="5C5E60"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Error_3e.jpg</span><span class="informations">1671×1039 600 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @jamesobutler (2019-08-13 20:48 UTC)

<p><a class="mention" href="/u/dfafalis">@dfafalis</a> This appears to be a similar issue that was discussed in the following thread:</p>
<aside class="quote quote-modified" data-post="1" data-topic="7474">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-effects-crashing-slicer/7474">Segmentation effects crashing Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
I’m using the preview version of Slicer to do a segmentation on a 2.6 GB micro-CT scan saved as a TIF. I can do a simple segmentation, but when I try to apply the mask or split volume effect, the Slicer application crashes. I’ve checked the error logs and there were no errors generated. I’m using a Windows machine with 32GB RAM and ~500GB free disk space. 
I also generated the following warnings when trying to use the islands effect: 

Slicer has caught an internal error. 
You may be abl…
  </blockquote>
</aside>

<p>This was solved by a recent fix to one of Slicer’s dependencies as detailed in the linked thread. If you are working with a large data set, please try a Slicer preview release (<a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>) to see if this solves your problem.</p>

---

## Post #19 by @muratmaga (2019-08-13 21:32 UTC)

<p><a class="mention" href="/u/dfafalis">@dfafalis</a><br>
Yes, please try the same steps with the latest preview (after installing segmenteditorextraeffects) and see whether you still get the same error. Bad allocation error message in your first window means it is running out of memory.</p>

---

## Post #20 by @dfafalis (2019-08-16 14:23 UTC)

<p>Hello everyone,</p>
<p>Thank you for your advice.</p>
<p>I downloaded the preview edition and working on it.</p>
<p>However, I encountered these errors, attached screenshots, while actually doing nothing, just viewing the segmentations.</p>
<p>Best</p>
<p>Dimitrios</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3b6c48d92223c02d809bb8d642cab284520638.png" data-download-href="/uploads/short-url/frsSyBvsFrdGtnSQoQFOARkg0ti.png?dl=1" title="Slicer_Error_4.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c3b6c48d92223c02d809bb8d642cab284520638_2_690x215.png" alt="Slicer_Error_4.png" data-base62-sha1="frsSyBvsFrdGtnSQoQFOARkg0ti" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c3b6c48d92223c02d809bb8d642cab284520638_2_690x215.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3b6c48d92223c02d809bb8d642cab284520638.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3b6c48d92223c02d809bb8d642cab284520638.png 2x" data-dominant-color="F0EFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Error_4.png</span><span class="informations">781×244 65.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @jamesobutler (2019-08-16 14:34 UTC)

<p>Those errors likely showed up when you closed Slicer. That just indicates there are some memory leaks somewhere in the code that developers will work on fixing. You can proceed to ignore these messages.</p>
<p>What is surprising is that these are showing for preview builds downloaded from the Slicer website. Maybe this is only on Windows 7?</p>

---

## Post #22 by @dfafalis (2019-08-16 15:01 UTC)

<p>Hello James,</p>
<p>Yes, these errors show when I close Slicer, and I am using a Windows 7 PC</p>

---
