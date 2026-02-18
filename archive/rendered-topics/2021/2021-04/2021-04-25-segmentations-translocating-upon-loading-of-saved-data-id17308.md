# Segmentations translocating upon loading of saved data

**Topic ID**: 17308
**Date**: 2021-04-25
**URL**: https://discourse.slicer.org/t/segmentations-translocating-upon-loading-of-saved-data/17308

---

## Post #1 by @Isaac.Annal (2021-04-25 13:02 UTC)

<p>Hi all!</p>
<p>I’ve been trying to really get going with 3D slicer for a while now and I can’t seem to figure out a resolution to this issue. I am currently working on the segmentation of skink skulls. When I load saved data, what is supposed to be located at the back of the skull is found at the front. I have toyed around with changing the way I save things, but I can’t seem to figure out how to properly save the data for it to be correctly loaded the next time I work on it. Has anyone seen this issue/know of a resolution?</p>
<p>Thank you!<br>
Isaac</p>

---

## Post #2 by @lassoan (2021-04-25 13:23 UTC)

<p>What format your original input files are loaded from? DICOM, nrrd, nii, stl, obj, ply,…?</p>
<p>What file format the segmentation is saved into?</p>
<p>After saving, do you load the saved scene (.mrml or .mrb file) or select a few data files and load just those?</p>
<p>What Slicer version do you use?</p>
<p>Can you share the application logs of both saving the segmentation and loading the segmentation? (application logs are available in menu: Help / Report a bug)</p>

---

## Post #3 by @Isaac.Annal (2021-04-26 05:29 UTC)

<p>Thank you for the response! I am importing .tif files. I saved the segmentation as a .nrrd file. I load in the scene as a .mrml file and I also load in the segmentation and .tif files that were found in the saved data. I am currently using 3D Slicer 4.11.20210226.</p>
<p>This is the application log after saving</p>
<aside class="onebox googledocs">
  <header class="source">
      <a href="https://docs.google.com/document/d/1tcBW0wgdumMU8bd6BUFYef0ocLU0lWHG46T1oQsbkZ4/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>
  <article class="onebox-body">
    <a href="https://docs.google.com/document/d/1tcBW0wgdumMU8bd6BUFYef0ocLU0lWHG46T1oQsbkZ4/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-docs-logo"></span></a>

<h3><a href="https://docs.google.com/document/d/1tcBW0wgdumMU8bd6BUFYef0ocLU0lWHG46T1oQsbkZ4/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">after save</a></h3>

<p>[DEBUG][Qt] 25.04.2021 19:42:37 [] (unknown:0) - Session start time .......: 2021-04-25 19:42:37 [DEBUG][Qt] 25.04.2021 19:42:37 [] (unknown:0) - Slicer version ...........: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This is the application log after loading</p>
<aside class="onebox googledocs">
  <header class="source">
      <a href="https://docs.google.com/document/d/1QCQ6g69Q-sB-o6ItT-4A_mFw5j92FVRjAWsSipLfbuc/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>
  <article class="onebox-body">
    <a href="https://docs.google.com/document/d/1QCQ6g69Q-sB-o6ItT-4A_mFw5j92FVRjAWsSipLfbuc/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-docs-logo"></span></a>

<h3><a href="https://docs.google.com/document/d/1QCQ6g69Q-sB-o6ItT-4A_mFw5j92FVRjAWsSipLfbuc/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">after loading</a></h3>

<p>[DEBUG][Qt] 26.04.2021 01:06:46 [] (unknown:0) - Session start time .......: 2021-04-26 01:06:46 [DEBUG][Qt] 26.04.2021 01:06:46 [] (unknown:0) - Slicer version ...........: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @muratmaga (2021-04-26 05:49 UTC)

<aside class="quote no-group" data-username="Isaac.Annal" data-post="3" data-topic="17308">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e8c25b/48.png" class="avatar"> Isaac.Annal:</div>
<blockquote>
<p>Thank you for the response! I am importing .tif files. I saved the segmentation as a .nrrd file. I load in the scene as a .mrml file and I also load in the segmentation and .tif files that were found in the saved data. I am currently using 3D Slicer 4.11.20210226.</p>
</blockquote>
</aside>
<p>Looks like your image is coming in as a tiff stack. You will probably find it easier if you use the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks"><code>ImageStacks</code> module of SlicerMorph extension</a>.</p>
<p>If the specimen is reversed to what you are expecting to find, you can click the reverse option, and reimport the stack.</p>
<p>Once you successfully import your stack (with correct orientation and image spacing) before segmenting it, you really need to save it as NRRD volume, so that next time you don’t have to repeat the import process. You can do CTRL + S to open the Save As dialog box, or if you installed the SlicerMorph, right click on the imported volume in the <code>Data</code> module and choose Export As and save it as NRRD.</p>

---

## Post #5 by @Isaac.Annal (2021-04-29 00:18 UTC)

<p>Thank you! I will try this and reply with how it worked for me.</p>

---
