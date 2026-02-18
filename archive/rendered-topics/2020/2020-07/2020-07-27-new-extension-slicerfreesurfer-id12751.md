# New Extension: SlicerFreeSurfer

**Topic ID**: 12751
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/new-extension-slicerfreesurfer/12751

---

## Post #1 by @Sunderlandkyl (2020-07-27 21:07 UTC)

<p>We have added a new extension called SlicerFreeSurfer to the latest Slicer preview releases (4.11).<br>
This exension takes over handling FreeSurfer models/scalar overlay import from the 3D Slicer core, and adds support for importing FreeSurfer segmentations</p>
<p>FreeSurfer files can be dragged + dropped into Slicer, or users can use the FreeSurfer Importer module can to navigate and import many files from a FreeSurfer subject directory. Models imported from FreeSurfer can now also be transformed into the correct coordinate system by aligning them to a corresponding reference image.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="v0rGbno4h2M" data-video-title="Import FreeSurfer subjects into 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=v0rGbno4h2M" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/v0rGbno4h2M/hqdefault.jpg" title="Import FreeSurfer subjects into 3D Slicer" width="" height="">
  </a>
</div>

<p>Future plans include:</p>
<ul>
<li>Add module for exporting files in FreeSurfer format (<a href="https://github.com/PerkLab/SlicerFreeSurfer/issues/7" class="inline-onebox" rel="noopener nofollow ugc">Add module to handle export of files to FreeSurfer formats · Issue #7 · PerkLab/SlicerFreeSurfer · GitHub</a>)</li>
<li>Streamline user interface (<a href="https://github.com/PerkLab/SlicerFreeSurfer/issues/6" class="inline-onebox" rel="noopener nofollow ugc">FreeSurferImporter: Streamline user interface · Issue #6 · PerkLab/SlicerFreeSurfer · GitHub</a>)</li>
</ul>
<p>Any comments, feedback, suggestions are welcome.</p>
<p>Development was funded in part by NIH grant R01MH112748 and CANARIE’s Research Software Program.</p>

---

## Post #2 by @lassoan (2020-08-27 03:09 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-load-freesurfer-surface-files-in-correct-position-using-python-script/13183">How to load FreeSurfer surface files in correct position using Python script</a></p>

---

## Post #3 by @lassoan (2021-02-11 19:42 UTC)

<p>3 posts were split to a new topic: <a href="/t/parts-of-a-module-user-interface-are-unreadable-in-dark-mode-on-macos/15956">Parts of a module user interface are unreadable in dark mode on macOS</a></p>

---

## Post #4 by @Kae1 (2023-03-08 05:36 UTC)

<p>Hi Kyle,</p>
<p>Can you point me in the direction on information on how to add this SlicerFreeSurfer extension to 3DSlicer? I am new to 3dSlicer use and am not sure how to do this.  I have added other extensions for other software to 3DSlicer through Slicer&gt;edit/Applications &amp; Settings/ Modules/ &gt;add module. However this doesn’t seem to work for the SlicerFreeSurfer extension files I downloaded from Github.</p>
<p>My main issue to getting lh.pial and lh.white files created in FreeSurfer into 3dSlicer. Drag and drop just gives ‘unable to load’ error messages. So, any advice on this would also be great. I’m hoping that the SlicerFreeSurfer extension will help with this.</p>
<p>Thank in advance!</p>

---

## Post #5 by @muratmaga (2023-03-08 05:59 UTC)

<p>Why are you trying to manually install it?</p>
<p>Go to <strong>View-&gt;Extension Manager</strong> (or CTRL/CMD + 4), click <strong>Install Extension</strong> tab, type SlicerFreeSurfer in the search box (or scroll down the list of all available extensions), then click <strong>Install</strong> and restart slicer for changes to take effect?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41c8566f0efac4b392078a53c04e9a29b66991bb.png" data-download-href="/uploads/short-url/9nWfVOGqSw3XrWFGYFwjk4lM17R.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41c8566f0efac4b392078a53c04e9a29b66991bb_2_690x376.png" alt="image" data-base62-sha1="9nWfVOGqSw3XrWFGYFwjk4lM17R" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41c8566f0efac4b392078a53c04e9a29b66991bb_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41c8566f0efac4b392078a53c04e9a29b66991bb_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41c8566f0efac4b392078a53c04e9a29b66991bb.png 2x" data-dominant-color="EBEBF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1312×716 95.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Kae1 (2023-03-08 21:59 UTC)

<p>Thanks,</p>
<p>I wasn’t aware SlicerFreeSurfer was able to be installed in that way. It seems to work fine and I am able to drag and drop pial and white matter files into Slicer.<br>
Much appreicated .</p>
<p>CONFIDENTIALITY NOTICE: This email and any files transmitted with it are confidential and are to be used solely by the individual or entity to whom it is addressed. If you are not the intended recipient and have received this email in error, please be aware that any disclosure, copying or distribution of the information it contains; or taking any action in reliance on the contents of this information, is strictly prohibited and may be unlawful. Please notify us by return email that you have received the email and delete all copies in your system.</p>

---
