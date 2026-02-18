# Can't export segmentation as Dicom RTStruct in Python Script

**Topic ID**: 16981
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/cant-export-segmentation-as-dicom-rtstruct-in-python-script/16981

---

## Post #1 by @Namng1210 (2021-04-07 14:19 UTC)

<p>Operating system: Python Script<br>
Slicer version: 4.11.20210226<br>
Dear authors,<br>
Everything seems to be really good when i exported it by hand and I’ve followed your instructions video of exporting RT-STRUCT file by right click at Study and choose Export to DICOM then click in RT struct and got the result as i want.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8aef4f677deed6518d2d7989ae69e898651ec8bd.png" data-download-href="/uploads/short-url/jP4BR9K3bbiGENMt3zZyPKnoRdj.png?dl=1" title="ui" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8aef4f677deed6518d2d7989ae69e898651ec8bd_2_617x500.png" alt="ui" data-base62-sha1="jP4BR9K3bbiGENMt3zZyPKnoRdj" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8aef4f677deed6518d2d7989ae69e898651ec8bd_2_617x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8aef4f677deed6518d2d7989ae69e898651ec8bd_2_925x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8aef4f677deed6518d2d7989ae69e898651ec8bd_2_1234x1000.png 2x" data-dominant-color="F0F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ui</span><span class="informations">1320×1069 46.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But when i was doing it in python script by the following code, after passing the studyID as parameter, i got the result return ‘Exportable list contains no exportables’. Then, i have also tried to pass the segmentationID, but got another warning : ‘Must export the primary anatomical (CT/MR) image’. How can i fix this problem ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb83aa576b142a19d4794464c4211c4bced962e6.png" data-download-href="/uploads/short-url/xBsir4IzWGCefsuSFXhFaUfscQe.png?dl=1" title="export" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb83aa576b142a19d4794464c4211c4bced962e6.png" alt="export" data-base62-sha1="xBsir4IzWGCefsuSFXhFaUfscQe" width="690" height="342" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">export</span><span class="informations">1343×667 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hope you reply me soon. Thank you so much.</p>

---

## Post #2 by @cpinter (2021-04-07 14:28 UTC)

<p>This is a duplicate of this issue:</p><aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/issues/184#issuecomment-814931832" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/issues/184#issuecomment-814931832" target="_blank" rel="noopener">Can't export segmentation as Dicom RTStruct</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-04-07" data-time="09:15:16" data-timezone="UTC">09:15AM - 07 Apr 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/Namng1210" target="_blank" rel="noopener">
          <img alt="Namng1210" src="https://avatars.githubusercontent.com/u/69883752?v=4" class="onebox-avatar-inline" width="20" height="20">
          Namng1210
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Dear authors,
Everything seems to be really good when i exported it by hand and I've followed your instructions video of exporting...</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/namng1210">@Namng1210</a> Please do not duplicate threads especially without mentioning the other one as the community members helping you will duplicate work that others did in other threads.</p>
<p>Also I just see an email about your comment to that GitHub issue that it worked, but then you seem to have removed that comment. Then you post the original question here without any of the suggestions, and there is no trace about any information why that solution that seemed to work, finally (apparently) didn’t.</p>
<p>Now that we have a thread about this on GitHub let’s keep the discussion there, and a good start would be to react to the last suggestion. Thank you</p>

---

## Post #3 by @Namng1210 (2021-04-07 14:51 UTC)

<p>Dear author,<br>
This question was actually posted at the same time as my post on github.I’m so sorry because at that time, i really wanted to solve the problem and this is the first time that I joined this community.<br>
Thanks a lot for your help and i’ll learn from my mistakes next time.<br>
Best regards,<br>
Nguyen Phuong Nam</p>

---

## Post #4 by @rodger (2021-12-01 16:22 UTC)

<p>Hello,<br>
I am kinda new with python. Can you explain to me how you manage to solve this issue? (the github post is closed so I am asking here sorry…).</p>
<p>I tried to run the ExamineForExport function on the volume and the segmentations, then past them in a list for the export function, but it did not worked:</p>
<p>exporter = DicomRtImportExportPlugin.DicomRtImportExportPluginClass()<br>
exportable1 = exporter.examineForExport(segmentationShItem)<br>
exportable2 = exporter.examineForExport(referenceVolumeShItem)</p>
<p>for exp in exportable1:<br>
exp.directory=outputFolder<br>
for exp in exportable2:<br>
exp.directory=outputFolder</p>
<p>exportables = [exportable1,exportable2]</p>
<blockquote>
<blockquote>
<blockquote>
<p>exporter.export(exportables)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/tmp/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DicomRtImportExportPlugin.py”, line 122, in export<br>
exportable.copyToVtkExportable(vtkExportable)<br>
AttributeError: ‘list’ object has no attribute ‘copyToVtkExportable’</p>
</blockquote>
</blockquote>
</blockquote>
<p>thanks !</p>

---
