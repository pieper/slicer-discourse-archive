---
topic_id: 13899
title: "No Images Shown In Slice Viewers In Latest Preview Release S"
date: 2020-10-06
url: https://discourse.slicer.org/t/13899
---

# No images shown in slice viewers in latest preview release (Slicer-4.13.0)

**Topic ID**: 13899
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/no-images-shown-in-slice-viewers-in-latest-preview-release-slicer-4-13-0/13899

---

## Post #1 by @am_49 (2020-10-06 18:18 UTC)

<p>Problem report for Slicer 4.13.0-2020-10-05 win-amd64: [please describe expected and actual behavior]</p>
<p>I am running Windows 10 on ASUS AiO desktop (Intel Core i5, RAM 16 GB, NVIDIA GeForce GTX 1050, updated drivers and application software). The loaded image is there - intensity values are displayed along with mouse cursor coordinates when moved over the viewers. The viewers brightness does not change, remains black when attempting to control it with mouse (left-click-and-drg in slice view).</p>
<p>What am I doing wrong? Please help.<br>
Best,<br>
Andrzej</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e95bbe75569ef78c6934ab03e207603efb03ebf0.png" data-download-href="/uploads/short-url/xinOib6F92oMSg2CQ1bLTIvbkKA.png?dl=1" title="Screen Shot 10-06-20 at 06.59 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e95bbe75569ef78c6934ab03e207603efb03ebf0.png" alt="Screen Shot 10-06-20 at 06.59 PM" data-base62-sha1="xinOib6F92oMSg2CQ1bLTIvbkKA" width="689" height="467" data-dominant-color="7A797E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 10-06-20 at 06.59 PM</span><span class="informations">1181×800 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-10-06 19:15:08<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.13.0-2020-10-05 (revision 29411 / ff8bc2b) win-amd64 - installed release<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16318 MB physical, 18750 MB virtual<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/asus/AppData/Local/NA-MIC/Slicer 4.13.0-2020-10-05/bin<br>
[DEBUG][Qt] 06.10.2020 19:15:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: C:/Users/asus/AppData/Roaming/NA-MIC/Extensions-29411/SlicerRadiomics/lib/Slicer-4.13/cli-modules, C:/Users/asus/AppData/Roaming/NA-MIC/Extensions-29411/SlicerRadiomics/lib/Slicer-4.13/qt-scripted-modules<br>
[DEBUG][Python] 06.10.2020 19:15:09 [Python] (C:\Users\asus\AppData\Local\NA-MIC\Slicer 4.13.0-2020-10-05\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 06.10.2020 19:15:10 [Python] (C:\Users\asus\AppData\Roaming\NA-MIC\Extensions-29411\SlicerRadiomics\Lib\site-packages\pykwalify\compat.py:20) - Using yaml library: C:\Users\asus\AppData\Roaming\NA-MIC\Extensions-29411\SlicerRadiomics\Lib\site-packages\yaml_<em>init</em>_.py<br>
[DEBUG][Python] 06.10.2020 19:15:10 [Python] (C:\Users\asus\AppData\Local\NA-MIC\Slicer 4.13.0-2020-10-05\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 06.10.2020 19:15:11 [Python] (C:\Users\asus\AppData\Local\NA-MIC\Slicer 4.13.0-2020-10-05\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 06.10.2020 19:15:11 [Python] (C:\Users\asus\AppData\Local\NA-MIC\Slicer 4.13.0-2020-10-05\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 06.10.2020 19:15:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Python] 06.10.2020 19:15:15 [Python] (C:/Users/asus/AppData/Local/NA-MIC/Slicer 4.13.0-2020-10-05/bin/…/lib/Slicer-4.13/qt-scripted-modules/SampleData.py:373) - </p><p>Status: <i>Idle</i></p><br>
[DEBUG][Qt] 06.10.2020 19:15:15 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Python] 06.10.2020 19:15:17 [Python] (C:/Users/asus/AppData/Local/NA-MIC/Slicer 4.13.0-2020-10-05/bin/…/lib/Slicer-4.13/qt-scripted-modules/SampleData.py:373) - <b>Verifying checksum</b><br>
[DEBUG][Python] 06.10.2020 19:15:17 [Python] (C:/Users/asus/AppData/Local/NA-MIC/Slicer 4.13.0-2020-10-05/bin/…/lib/Slicer-4.13/qt-scripted-modules/SampleData.py:373) - <b>File already exists and checksum is OK - reusing it.</b><br>
[DEBUG][Python] 06.10.2020 19:15:17 [Python] (C:/Users/asus/AppData/Local/NA-MIC/Slicer 4.13.0-2020-10-05/bin/…/lib/Slicer-4.13/qt-scripted-modules/SampleData.py:373) - <b>Requesting load</b> <i>MRHead</i> from C:/Users/asus/AppData/Local/Temp/Slicer/RemoteIO/MR-head.nrrd …<br>
[DEBUG][Python] 06.10.2020 19:15:17 [Python] (C:/Users/asus/AppData/Local/NA-MIC/Slicer 4.13.0-2020-10-05/bin/…/lib/Slicer-4.13/qt-scripted-modules/SampleData.py:373) - <b>Load finished</b><br>
[INFO][VTK] 06.10.2020 19:15:17 [vtkMRMLVolumeArchetypeStorageNode (00000214C026BE60)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:473) - Loaded volume from file: C:/Users/asus/AppData/Local/Temp/Slicer/RemoteIO/MR-head.nrrd. Dimensions: 256x256x130. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 06.10.2020 19:15:17 [vtkMRMLScene (00000214C23B8940)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 06.10.2020 19:15:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/asus/AppData/Local/Temp/Slicer/RemoteIO/MR-head.nrrd” “[0.11s]”<p></p>

---

## Post #2 by @lassoan (2020-10-06 18:36 UTC)

<p>Sorry for the inconvenience, we know about this issue (<a href="https://github.com/Slicer/Slicer/issues/5220">https://github.com/Slicer/Slicer/issues/5220</a>). You need to use the Stable Release (version 4.11.20200930, revision 29402) for about 1-2 weeks, as we have upgraded Slicer’s rendering library and we need some time to fix all the issues.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could we take down the preview release download links or add big red comments next to them telling that currently they are not usable?</p>

---

## Post #3 by @am_49 (2020-10-06 19:19 UTC)

<p>Thank you very much for quick reply!<br>
Andrzej</p>

---

## Post #4 by @Sam_Horvath (2020-10-07 13:45 UTC)

<p>I’ll look at what I can do with the website.</p>

---

## Post #5 by @Sam_Horvath (2020-10-07 13:54 UTC)

<p>I have opened a PR to mark the preview release as unstable:<br>
</p><aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/mhalle/slicer4-download/pull/19" target="_blank" rel="noopener nofollow ugc">github.com/mhalle/slicer4-download</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/mhalle/slicer4-download/pull/19" target="_blank" rel="noopener nofollow ugc">Mark Preview release as unstable</a>
    </h4>

    <div class="branches">
      <code>mhalle:master</code> ← <code>sjh26:patch-1</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-07" data-time="13:54:28" data-timezone="UTC">01:54PM - 07 Oct 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="noopener nofollow ugc">
          <img alt="sjh26" src="https://avatars2.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/mhalle/slicer4-download/pull/19/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2020-11-03 20:43 UTC)



---

## Post #7 by @lassoan (2020-11-06 17:23 UTC)

<p>There is no working release that contains fixes introduced since Slicer-4.11.20209030. Users that need these fixes cannot do anything else than wait (see <a href="https://discourse.slicer.org/t/no-images-shown-in-slice-viewers-in-latest-preview-release-slicer-4-13-0/13899/4">this example</a>). This also prevents us from getting developments to users in two of our projects.</p>
<p>If fixing of this VTK issue needs more time then we need to do something else that would allow projects to move forward.<br>
<a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could we update the factory builds to use VTK8 for building the preview release? Or should we release a patch release for Slicer-4.11?</p>

---

## Post #8 by @Sam_Horvath (2020-11-06 20:43 UTC)

<p>We can switch the builds to VTK8, I will touch base with JC on this.</p>

---

## Post #9 by @Sam_Horvath (2020-11-06 22:27 UTC)

<p>I am going to switch the builds back to VTK8 now, will take effect for tonight’s preview.</p>

---
