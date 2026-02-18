# Older Scenes and Specimens Loading Incorrectly

**Topic ID**: 34328
**Date**: 2024-02-14
**URL**: https://discourse.slicer.org/t/older-scenes-and-specimens-loading-incorrectly/34328

---

## Post #1 by @SLDT (2024-02-14 16:17 UTC)

<p>Hello Slicer Community,</p>
<p>I have recently encountered a problem loading some older specimens and project files that I worked on back in 2020 using Slicer 4.10.2. Originally, the scenes would appear like so, with the specimen and the masks overlapping properly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49f75422301fb5df70607b02b7f38e21bcf6b551.png" data-download-href="/uploads/short-url/aykKMoi0hiytY3oZVqS0tSMSNMt.png?dl=1" title="2020-08-17-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49f75422301fb5df70607b02b7f38e21bcf6b551_2_690x473.png" alt="2020-08-17-Scene" data-base62-sha1="aykKMoi0hiytY3oZVqS0tSMSNMt" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49f75422301fb5df70607b02b7f38e21bcf6b551_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49f75422301fb5df70607b02b7f38e21bcf6b551_2_1035x709.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49f75422301fb5df70607b02b7f38e21bcf6b551.png 2x" data-dominant-color="2B2C35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-08-17-Scene</span><span class="informations">1347×924 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I tried to open these files again, in Slicer 4.10.2, and in several other versions of Slicer, including Slicer 4.11.0-2020-09-08, Slicer 4.11.2021-02-26, and Slicer 5.03, the scene appears distorted in various ways.</p>
<p>For example, with the same specimen now opened in Slicer 4.10.2:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f9350ab110c4c11b685607e89557d56eab16003.png" data-download-href="/uploads/short-url/icAg773Ch5FDatQuxamuvsYPIkj.png?dl=1" title="Slicer 4.10.2 Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f9350ab110c4c11b685607e89557d56eab16003_2_690x373.png" alt="Slicer 4.10.2 Error" data-base62-sha1="icAg773Ch5FDatQuxamuvsYPIkj" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f9350ab110c4c11b685607e89557d56eab16003_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f9350ab110c4c11b685607e89557d56eab16003_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f9350ab110c4c11b685607e89557d56eab16003_2_1380x746.png 2x" data-dominant-color="64646A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer 4.10.2 Error</span><span class="informations">1920×1040 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And opened in Slicer 5.0.3:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/782c97dc05682356461038854ed690f09c903641.png" data-download-href="/uploads/short-url/h96PTdLpVkLGj0AZI50hTHIeBix.png?dl=1" title="Slicer 5.0.3 Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782c97dc05682356461038854ed690f09c903641_2_690x373.png" alt="Slicer 5.0.3 Error" data-base62-sha1="h96PTdLpVkLGj0AZI50hTHIeBix" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782c97dc05682356461038854ed690f09c903641_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782c97dc05682356461038854ed690f09c903641_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782c97dc05682356461038854ed690f09c903641_2_1380x746.png 2x" data-dominant-color="686870"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer 5.0.3 Error</span><span class="informations">1920×1040 90.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I opened the segmentation file for one of these specimens in Slicer 5.0.3, I got the following error message:</p>
<pre><code class="lang-auto">- Error: Loading D:/Scans/Phrynosoma Ingroup Scans/Phrynosoma cornutum/Segmentation/2020-08-11-Scene.mrml - ERROR: In D:\D\S\S-0\Libs\MRML\Core\vtkMRMLStorableNode.cxx, line 322

vtkMRMLVolumePropertyNode (000001AAC64937D0): vtkMRMLStorableNode::UpdateScene failed: Failed to read node VolumeProperty (vtkMRMLVolumePropertyNode1) using storage node vtkMRMLVolumePropertyStorageNode1.

- Error: Loading D:/Scans/Phrynosoma Ingroup Scans/Phrynosoma cornutum/Segmentation/2020-08-11-Scene.mrml - ERROR: In D:\D\S\S-0\Libs\MRML\Core\vtkMRMLStorableNode.cxx, line 322

vtkMRMLColorTableNode (000001AAC9F07E40): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Segmentation-label_ColorTable (vtkMRMLColorTableNode1) using storage node vtkMRMLColorTableStorageNode22.

- Loading D:/Scans/Phrynosoma Ingroup Scans/Phrynosoma cornutum/Segmentation/2020-08-11-Scene.mrml - These extensions were installed when the scene was saved but not installed now: . These extensions may be required for successful loading of the scene.
</code></pre>
<p>This is the closest hint I’ve gotten to diagnosing the cause, but I don’t have the technical expertise to know what would be causing these issues and generating this particular error message. This is a fairly distressing situation, though, because I have about 13 specimens that I put a lot of work into preparing that seem to be affected by this issue, and I really need to be able to access the segmentation project files in their original forms in order to make further progress with them. Any suggestions or fixes for this situation would be very much appreciated!</p>

---

## Post #2 by @muratmaga (2024-02-14 16:21 UTC)

<p>Can you share one of your datasets?</p>
<p>it shouldn’t be difficult to fix, but we need to see the where the problem is coming from.</p>

---

## Post #3 by @SLDT (2024-02-14 16:31 UTC)

<p>I attempted to share one of the data sets as a compressed .rar file, but the upload function won’t work since that is not an approved file type. How would I go about sharing it here on the forum?</p>

---

## Post #4 by @muratmaga (2024-02-14 16:32 UTC)

<p>You need to post it somewhere on the cloud and share the link</p>

---

## Post #5 by @SLDT (2024-02-14 16:47 UTC)

<p>Here’s a Google Drive link:</p>
<p><a href="https://drive.google.com/drive/folders/1N_9q2hocJo9_cNyq1B7DC0kExL02VfKm?usp=drive_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1N_9q2hocJo9_cNyq1B7DC0kExL02VfKm?usp=drive_link</a></p>
<p>Let me know if you have difficulty accessing it.</p>

---

## Post #6 by @hherhold (2024-02-14 17:06 UTC)

<p>The image spacing of the volume in the Z direction looks incorrect: 0.0074 x 0.0074 x 1.000.</p>
<p>I can get it pretty close to looking correct-ish by setting the Z spacing to 0.056 or so, but that’s still not quite right.</p>
<p>I don’t think the missing color table or mis-matched extension setups would cause this. The volume is also saved with this spacing, so I’m not sure how this worked originally. Basically, it looks like the Z spacing of the segmentation and the volume don’t match.</p>

---

## Post #7 by @lassoan (2024-02-14 17:14 UTC)

<p>The problem is that the image was saved in TIFF format. This file format cannot store image orientation and Z spacing in standard tags, therefore the information is lost when it is saved. If you load the image again from the original source (maybe a DICOM files from MorphoSource) and save as .nrrd format then everything should work well. If you don’t have the source files anymore then you may need to experiment with the spacing and alignment.</p>
<p>TIFF format is not a 3D file format and we cannot fix its limitations but Slicer should display a warning when somebody attempts to use this file format for saving a 3D image. I’ve aded an issue to display a warning message:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7588">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7588" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7588" target="_blank" rel="noopener">Display warning when 3D image is saved as TIFF file</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-02-14" data-time="17:13:10" data-timezone="UTC">05:13PM - 14 Feb 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Users may not know that TIFF file cannot store image orientation a<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nd Z spacing and so they lose this information when saving the scene.

See for example this user error report: https://discourse.slicer.org/t/older-scenes-and-specimens-loading-incorrectly/34328

## Steps to reproduce

- Load MRHead example
- Save as TIFF file =&gt; ERROR: no warning is displayed
- Load the TIFF file =&gt; ERROR: the image is distorted

## Environment
- Slicer version: Slicer-5.6.1
- Operating system: Windows11</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @muratmaga (2024-02-14 17:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="34328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>TIFF format is not a 3D file format and we cannot fix its limitations but Slicer should display a warning when somebody attempts to use this file format for saving a 3D image. I’ve aded an issue to display a warning message:</p>
</blockquote>
</aside>
<p>So we have that issue in ImageStacks as well. If someone imports a tiff sequence. and then try to save the imported volume. The default format is shown as TIFF. This is not the case with other formats (PNG/JPG/BMP etc).</p>
<p>It is also the same behavior if one uses Slicer’s regular Add Data menu and import a TIFF sequence. It keeps the format as TIFF. I suggest that behavior needs to changed on the application side. Users are not always knowledgeable about data formats and issues, we should offer to save in the most reliable format (NRRD). If the the user has a specific reason to keep it TIFF, then they can manually override that.</p>

---

## Post #9 by @SLDT (2024-02-14 20:22 UTC)

<p>Thank you for clarifying this issue! I didn’t know that it was because of the data format, though I will definitely know to be cognizant of this in the future. That said, reloading the original TIFF stack via ImageStacks with the correct X, Y, and Z spacing allowed me to realign the specimen data with the original masks that I had prepared. The masking threshold didn’t seem to be saved, though, so for others that may encounter this issue in the future, reloading the image stack with the original spacing and sampling parameters, deleting the original volume, selecting the new volume, and adjusting the masking threshold to approximately match the area covered by the original masks worked to get me to the point where I could start applying edits to the original masks. Hopefully others find this helpful!</p>
<p>That said, when I got to save revised versions of these projects, how would I save the projects as .nrrd format files so that I don’t repeat this issue? Let me know, and thank you again!</p>

---

## Post #10 by @muratmaga (2024-02-14 20:38 UTC)

<p>Yes, when the imported volume is saved as a TIFF file, all the spacing settings you entered during the import is lost. it is always better to save the volumes as NRRD to avoid that issue.</p>
<p>If you want to reconstitute your original scene without having to repear the steps, load each dataset (volume and segmentation) individually (not from the mrml file). Go to the Volumes module, edit the correct spacing of the volume, and things should line up. Then make sure you save the edit volume as a NRRD file.</p>

---

## Post #11 by @lassoan (2024-02-15 12:34 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="34328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I suggest that behavior needs to changed on the application side.</p>
</blockquote>
</aside>
<p>I agree, in addition to the warning we should set the default file format to nrrd for 3D images. I’ve added a comment to the issue.</p>

---

## Post #12 by @kopachini (2024-02-16 08:26 UTC)

<p>I had similar problem but with nrrd files. When I opened segmentation nrrd file, it didn’t overlap the dicom set, yet it was offset on the side.</p>

---

## Post #13 by @pieper (2024-02-16 16:07 UTC)

<p>If you can share data that replicates this issue, with the steps to recreate it based on specific versions of Slicer it could help track down what’s different.  Any changes in Slicer behavior are intended to be backwards compatible with previous scene files.  If you didn’t use scene files then it’s possible that legacy formats like stl load incorrectly because the coordinate systems are not defined by default (and weren’t for files created by older versions of Slicer).</p>

---
