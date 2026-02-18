# Issue using Dcm2niixPlugin for 4D DTI Dicom data

**Topic ID**: 18402
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/issue-using-dcm2niixplugin-for-4d-dti-dicom-data/18402

---

## Post #1 by @andieku (2021-06-29 16:49 UTC)

<p>Hi, I have been using <a href="https://github.com/SlicerDMRI/SlicerDcm2nii/blob/master/Dcm2niixPlugin/Dcm2niixPlugin.py" rel="noopener nofollow ugc">Dcm2niixPlugin</a> to convert 4D DTI Dicom files to a 4D NIFTI file (.nii).</p>
<p>However, when I checked the output from the plugin’s <code>load(self,loadable)</code> function, it returned a 3D volume node while it’s supposed to return a 4D volume (or a series of 3D volumes).</p>
<p>I tried tracing the issue and noticed that <code>load(self,loadable)</code> function has a call to <code>slicer.util.loadVolume()</code> at <a href="https://github.com/SlicerDMRI/SlicerDcm2nii/blob/4f09c628c72aee04a410431c3a08168601a2cc76/Dcm2niixPlugin/Dcm2niixPlugin.py#L175" rel="noopener nofollow ugc">line 175</a>.</p>
<p>While <code>dcm2niix</code> command correctly produced a 4D NIFTI file, it appears that a call to the <code>loadVolume()</code> has converted it to a 3D volume. According to <a href="https://discourse.slicer.org/t/how-can-i-import-nifti-files-to-dscmrianalysis-module/3645">this related post</a> and my testing, I believe 4D NIFTI file can’t be properly loaded using <code>slicer.util.loadVolume()</code>. (Please correct me if I am wrong.)</p>
<p>So I was wondering why we are using <code>slicer.util.loadVolume()</code> instead of  <a href="https://github.com/fedorov/MultiVolumeImporter" rel="noopener nofollow ugc">MultiVolumeImporter</a> as mentioned in <a href="https://discourse.slicer.org/t/how-can-i-import-nifti-files-to-dscmrianalysis-module/3645/2">this post</a>.</p>
<p>Any explanation would be greatly appreciated. Thank you in advance for your help!</p>

---

## Post #2 by @pieper (2021-06-29 21:07 UTC)

<p>If the plugin isn’t working for your data I’d suggest running dcm2niix independently from Slicer to confirm that your data is compatible.</p>
<p>There’s a nrrd export option for dcm2niix that should make the results directly compatible with SlicerDMRI.  If it turns out your data isn’t compatible, the dcm2niix developer may be able to help.</p>

---

## Post #3 by @andieku (2021-06-29 23:32 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> for your reply.</p>
<p>I tried running dcm2niix independently and checked that my data is compatible. It produced a 4D .nii file.</p>
<p>The part that I still don’t understand from the plugin is that call to <code>slicer.util.loadVolume()</code> at <a href="https://github.com/SlicerDMRI/SlicerDcm2nii/blob/4f09c628c72aee04a410431c3a08168601a2cc76/Dcm2niixPlugin/Dcm2niixPlugin.py#L175" rel="noopener nofollow ugc">line 175</a>. By any chance, do you know why it’s calling <code>loadVolume()</code> instead of <code>MultiVolumeImporter.read4DNIfTI()</code>? Is that a mistake or was the plugin designed to support only 3D Dicoms and not 4D dicoms?</p>
<p>Thank you for your help!</p>

---

## Post #4 by @lassoan (2021-06-30 01:53 UTC)

<p>I think dcm2niix can create nrrd files. If you generate a 4D nrrd file then Slicer should be able to read it (just choose “Volume Sequence” in the “Description” column in “Add data” window).</p>

---

## Post #5 by @pieper (2021-06-30 12:45 UTC)

<p>If the scan is a compatible dwi scan (depends on both the scanner model and acquisition protocol) then dcm2niix can convert it to a valid nrrd file.  <code>slicer.util.loadVolume</code> automatically detects and loads nrrd files as scalar, vector, tensor, or dwi automatically based on the content.</p>

---

## Post #6 by @andieku (2021-06-30 21:15 UTC)

<p>Thank you for your prompt replies <a class="mention" href="/u/lassoan">@lassoan</a> &amp; <a class="mention" href="/u/pieper">@pieper</a>!</p>
<p>I followed your suggestion and changed the dcm2niixPlugin to convert it to a 4D <code>.nrrd</code> file and now the <code>slicer.util.loadVolume()</code> works well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b2d23e32fd379e4aa7ae22ec47a7c1a6d5ca0e.png" data-download-href="/uploads/short-url/pMx4bleyanHwWjCNf9bfn6jg9vU.png?dl=1" title="Screen Shot 2021-06-30 at 2.10.08 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4b2d23e32fd379e4aa7ae22ec47a7c1a6d5ca0e_2_690x278.png" alt="Screen Shot 2021-06-30 at 2.10.08 PM" data-base62-sha1="pMx4bleyanHwWjCNf9bfn6jg9vU" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4b2d23e32fd379e4aa7ae22ec47a7c1a6d5ca0e_2_690x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b2d23e32fd379e4aa7ae22ec47a7c1a6d5ca0e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b2d23e32fd379e4aa7ae22ec47a7c1a6d5ca0e.png 2x" data-dominant-color="333332"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-30 at 2.10.08 PM</span><span class="informations">928×374 435 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And now I would like to save the loaded 4D nrrd volume to 4D NIFTI file but <code>slicer.util.saveNode()</code> doesn’t seem to allow me to do that. Is there a way I can save a 4D nrrd to a 4D NIFTI?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce99adb1763543047d18780d457c533aa2f6921f.png" data-download-href="/uploads/short-url/ttFC2vMT3r6dyKFyYeXGjD2g6ar.png?dl=1" title="Screen Shot 2021-06-30 at 2.08.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce99adb1763543047d18780d457c533aa2f6921f.png" alt="Screen Shot 2021-06-30 at 2.08.29 PM" data-base62-sha1="ttFC2vMT3r6dyKFyYeXGjD2g6ar" width="690" height="105" data-dominant-color="232B34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-30 at 2.08.29 PM</span><span class="informations">916×140 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pieper (2021-06-30 22:52 UTC)

<aside class="quote no-group" data-username="andieku" data-post="6" data-topic="18402">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andieku/48/8934_2.png" class="avatar"> andieku:</div>
<blockquote>
<p>Is there a way I can save a 4D nrrd to a 4D NIFTI?</p>
</blockquote>
</aside>
<p>Not directly in Slicer but you can use this code:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pnlbwh/conversion">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/a8a20a27493020cee89dee7ce7d832aa5a8eba367e279bf95bd5fbcf61ecb0a7/pnlbwh/conversion" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">GitHub - pnlbwh/conversion: Various mri conversion/modification scripts</a></h3>

  <p>Various mri conversion/modification scripts. Contribute to pnlbwh/conversion development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @andieku (2021-07-05 17:39 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a>! I will try using the conversion package.</p>

---
