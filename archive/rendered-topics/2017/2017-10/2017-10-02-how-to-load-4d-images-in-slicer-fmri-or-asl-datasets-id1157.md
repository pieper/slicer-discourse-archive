# How to load 4D images in Slicer - fMRI or ASL datasets

**Topic ID**: 1157
**Date**: 2017-10-02
**URL**: https://discourse.slicer.org/t/how-to-load-4d-images-in-slicer-fmri-or-asl-datasets/1157

---

## Post #1 by @acsenrafilho (2017-10-02 17:47 UTC)

<p>Hello, slicers!</p>
<p>Firstly, I am sorry if this is a naive question, but I’ve tried to find something on the web and until now I could not fix my problem.</p>
<p>I have a small dataset with ASL and fMRI (both as 4D nii files) which I want to use Slicer to process it. However, I cannot load it simply by the Load volume module (apparently only the first volume is loaded).<br>
I’ve checked <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWIConverter" rel="nofollow noopener">DWIConverter</a> module since this module has a flag (–fMRI) that may help me on this occasion. Nevertheless, I did not have success.</p>
<p>I wondering if there is a simple way to load 4D images in Slicer and then process it with a specific image processing module. Is there already a module to do that? If not, is it interesting to be implemented to the community? (I’m asking this because I can invest some time to figure it out to a simple CLI module if this is an interesting to several people)</p>
<p>Thank you again for the comprehension!</p>
<p>Best wishes</p>

---

## Post #2 by @ihnorton (2017-10-02 18:04 UTC)

<p>Please give an example of the files or look at the error log ( X in bottom right corner) and post any errors.</p>
<p>There is a Sequences module and a Multi-Volume module, but I don’t think either one has support for nifti specifically (for the latter: <a href="https://issues.slicer.org/view.php?id=2972">https://issues.slicer.org/view.php?id=2972</a>). A CLI would be the simplest way to add support for your specific nifti flavor. Be aware that there is a difference in ITK between a vector image and a 4D image. This causes some complication in the i/o code, and may be a reason why Slicer’s readers don’t work for your data. Nifti 3d multivolume, 3d+t, and 3d+1 (no-op dimension) are all common, so any code may need user assistance to disambiguate.</p>

---

## Post #3 by @lassoan (2017-10-02 18:54 UTC)

<p>You can create a NIFTI importer for Sequences similarly how it is done for a different format (sequence metafile format) - see here <a href="https://github.com/SlicerRt/Sequences/tree/master/MetafileImporter">https://github.com/SlicerRt/Sequences/tree/master/MetafileImporter</a>. If you are not sure how to get started or stuck at any point then let me know.</p>

---

## Post #4 by @acsenrafilho (2017-10-03 12:40 UTC)

<p>Hi Norton,</p>
<p>In fact, the Slicer error log does not show any type of error when I tried<br>
to load my data, however, only the first volume is shown. My data is<br>
actually a series of 3D volumes concatenated through time (3D+t), as<br>
usually applied in fMRI datasets. A similar behaviour is found when I try<br>
to load a raw DTI data (1 b0 volume and N gradients in FSL format, i.e. one<br>
nifti file, one .bval and one .bvec text files). If I load only the nifti<br>
file from the 4D DWI, only the first volume appears in the scene and no<br>
errors are shown.</p>
<p>Fortunately, in DWI-DTI cases, there is the SlicerDMRI module that deal<br>
with the conversion from FSL data to Nrrd files. That’s fine. However, I<br>
have not seen anything similar to fMRI-like dataset conversion, i.e. only a<br>
series of 3D volumes through time.</p>
<p>I’ve also checked out the modules that you commented before, but it seems<br>
that is not exactly what I am looking for here. Maybe they only work on<br>
DICOM conversion. Am I right?</p>
<p>I hope that I am not creating more confusing with my question! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thank you again for the quick response and suggestions!</p>
<p>Cheers<br>
Antonio</p>

---

## Post #5 by @acsenrafilho (2017-10-03 12:42 UTC)

<p>Sorry, Andras! I have not seen your message! I will try it and get back as<br>
soon as possible.<br>
Thank you!</p>

---

## Post #6 by @lassoan (2017-10-03 13:10 UTC)

<p>Importing of 3D+t volumes are implemented by MultiVolumeImporter plugin. Once you loaded the image, you can browse between the frames using MultiVolumeExplorer module.</p>

---

## Post #7 by @acsenrafilho (2017-10-03 13:44 UTC)

<p>Great! MutliVolumeImporter solved the problem!</p>
<p>Thanks</p>

---

## Post #8 by @djrowland (2018-03-14 17:31 UTC)

<p>I am interested in this topic. I have some Bruker cardiac data that I would like to look at in Slicer. I use a plugin in FIJI to convert the data from Bruker format to either Analyze or Nifti format. I looked at the MultiVolumeImporter and it seems to import nifti but the frames of the images are stacked in a single volume such that I cannot explore the multi-volumes. The advanced settings don’t make complete sense. Any pointers on this would be appreciated. Thanks<br>
Doug</p>

---

## Post #9 by @djrowland (2018-03-14 17:32 UTC)

<p>And I am actually quite surprised that Slicer does not have a generalized multi-volume/frame importer. It would be great to have to import framed PET data as well. If you know of resources showing how to do this, it would be appreciated as well.</p>

---

## Post #10 by @lassoan (2018-03-14 18:22 UTC)

<p>There are not one but several ways of importing volume sequences.</p>
<p>If you have your volume as individual volume files in a folder then you have two main options:</p>
<p><strong>Option A:</strong> If all volumes have the same geometry (origin, spacing, axis directions, extent)and they are all scalar volumes</p>
<p>Use MultiVolumeImporter module.</p>
<p>This module creates a Multivolume node. If you prefer volume sequence nodes (because you want to browse it along with other node types, have arbitrary number of time points extracted, etc.) then you can save the node as a nrrd file and when you load it into Slicer again, selecting <code>Volume sequence</code> in the <code>Description</code> column in <code>Add data</code> dialog.</p>
<p><strong>Option B:</strong> In all other cases, for example volumes have different geometry or you want to import different data types (surface or volumetric meshes, point sets, tables, segmentations, etc)</p>
<ul>
<li>Install <code>Sequences</code> extension.</li>
<li>Load your data set: drag-and-drop the folder to the Slicer application window, choose <code>Any data</code>, click OK, click OK.</li>
<li>Go to <code>Sequences</code> module.</li>
<li>Create a new Sequence node.</li>
<li>In <code>Add/remove data nodes</code> section, click on your first node of the sequence, click the green <code>left arrow</code> button.</li>
<li>Click the <code>left arrow</code> button until all nodes are added.</li>
</ul>
<p>If you want to show the sequence playing in viewers:</p>
<ul>
<li>Go to Sequence browser module</li>
<li>Select your sequence in the node selector at the top of <code>Synchronized nodes</code> section</li>
<li>Click the green <code>+</code> icon</li>
<li>You can click <code>Rename</code> checkbox to include index value in the proxy node name (that represents the selected sequence item in the scene)</li>
<li>Select the proxy node to be shown in slice viewer or volume renderer to see the volume</li>
</ul>

---

## Post #11 by @pieper (2018-03-14 20:02 UTC)

<aside class="quote no-group" data-username="djrowland" data-post="8" data-topic="1157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/8edcca/48.png" class="avatar"> djrowland:</div>
<blockquote>
<p>Nifti format. I looked at the MultiVolumeImporter and it seems to import nifti but the frames of the images are stacked</p>
</blockquote>
</aside>
<p>The latest version of the MultiVolumeImporter (as of just the last few days) will try to load 4D nifti data (xyzt) if it finds it as the only file in the import directory.  This is new and we don’t have a lot of example data but it works for 4D data from the <a href="https://nifti.nimh.nih.gov/nifti-1/data">nifti site</a>.  The mac and linux nightly downloads are both broken today but it should work on windows or a local mac or linux build.</p>

---

## Post #12 by @djrowland (2018-03-14 21:53 UTC)

<p>Thanks for the responses. I am still confused by this. The data I have are on the same grid as it was acquired with Intragate which retrospectively reconstructs phases of the heart cycle for a given acquisition. So technically, I should be using option A. The multivolumeImporter does identify the NIFTI format. But the image looks strange and it is such that I cannot cycle the heart phases. See attachment.</p>
<p>Thanks</p>
<p>Doug</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/971c9775b0c7143915d3e3d01a6f9cf8b62570aa.png" data-download-href="/uploads/short-url/lyNm1WcrsdXCQZmR3tIPxVHzB3A.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/971c9775b0c7143915d3e3d01a6f9cf8b62570aa_2_690x377.png" alt="image" data-base62-sha1="lyNm1WcrsdXCQZmR3tIPxVHzB3A" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/971c9775b0c7143915d3e3d01a6f9cf8b62570aa_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/971c9775b0c7143915d3e3d01a6f9cf8b62570aa_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/971c9775b0c7143915d3e3d01a6f9cf8b62570aa_2_1380x754.png 2x" data-dominant-color="96969D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1888×1033 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @djrowland (2018-03-14 22:00 UTC)

<p>I do have some additional suggestions, based on working in the preclinical area. Most datasets, dynamic framing or multivolume Cardiac data, comes in a single file. From a preclinical perspective, I like not having them as separate files for storage and retrieval. It would be cumbersome to have single files in individual directories. Most of the time a single directory has multiple nifti, raw or analyze files that are multi volume. Being able to select individual files would be a great thing to have.</p>
<p>Also having raw and analyze file imports would be great. Most image of the other image analysis software I use allows this flexibility and is intuitive (PMOD, Amira, FIJI, etc.). It is a bit surprising that this flexibility and intuitive import isn’t yet built into Slicer. This is what initially kept me from using Slicer.</p>
<p>Doug</p>

---

## Post #14 by @fedorov (2018-03-15 13:23 UTC)

<aside class="quote no-group" data-username="djrowland" data-post="12" data-topic="1157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/8edcca/48.png" class="avatar"> djrowland:</div>
<blockquote>
<p>The multivolumeImporter does identify the NIFTI format. But the image looks strange and it is such that I cannot cycle the heart phases.</p>
</blockquote>
</aside>
<p>Can you share the dataset to reproduce the problem?</p>

---

## Post #15 by @djrowland (2018-03-15 17:34 UTC)

<p>I am willing to send a dataset. The first message bounced back as the attachment was to large. I am trying it through the forum website.The attachment is a screen shot of the .nii properties from FIJI.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad7e526f6fbe99cc85f4e25dfc8d09f97e92db90.jpeg" alt="Capture" data-base62-sha1="oKNffP6uCYR96KaSTmO7YvC7tKM" width="207" height="409"></p>
<p>The forum doesn’t allow upload of .nii files. Only jpg, jpeg, png and gif. How can I get you the data?</p>
<p>Doug</p>

---

## Post #16 by @fedorov (2018-03-15 18:07 UTC)

<p>You can put it on Dropbox, Box, MS Drive, Google Drive, etc and share a link</p>

---

## Post #17 by @djrowland (2018-03-15 18:24 UTC)

<p>Thanks.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/qvjyx5mohti6tv5/MI1%20T2w.nii?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/qvjyx5mohti6tv5/MI1%20T2w.nii?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/qvjyx5mohti6tv5/MI1%20T2w.nii?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - File Deleted</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope this works.<br>
Doug</p>

---

## Post #18 by @pieper (2018-03-15 20:35 UTC)

<p>Hi Doug -</p>
<p>Yes, this loaded for me as a 10 frame multivolume using a build of the current slicer source code (current nightly build for mac or windows should work, linux built from source would also work).  So you can at play the frames and plot the pixel values.</p>
<p>HTH,<br>
-Steve</p>

---

## Post #19 by @fedorov (2018-03-15 22:01 UTC)

<p><a class="mention" href="/u/djrowland">@djrowland</a> make sure you use the latest nightly</p>
            <video title="2018-03-15_17-59-31.mp4" width="695" height="492" style="max-width:100%" controls="">
              <source src="https://content.screencast.com/users/andrey.fedorov/folders/Snagit/media/4d2d0494-28b6-47f6-aec7-a0b88c30d0f6/2018-03-15_17-59-31.mp4"></source>
            </video>


---

## Post #20 by @djrowland (2018-03-15 22:20 UTC)

<p>Thanks for checking it out. Does it work with the current stable release 4.8.1 for you? I have had issues with the nightly builds in the past and have kept to the stable release. It does not seem as though all the extensions are available in the nightly build, so it isn’t as useful to me.</p>
<p>I downloaded the nightly release and as you said it does work. Is there anyway to get the stable release to have this module working? The stable release in general is much more useful unless I am missing something with the extensions. But in general I don’t think I want to be using a nightly build or have to update on a daily or weekly basis by installing a nightly build.</p>
<p>Since the nightly build works, I tested having two nifti files in the same directory. It does not work well as it imports what looks to be the first frame of each multivolume and create it as a 2 frame multivolume. The project I am working on, we have already generated 40 separate images. I don’t want to have to create 40 separate directories for single nifti files. Will there be individual file support or will it remain as directory import?</p>

---

## Post #21 by @pieper (2018-03-15 22:40 UTC)

<p>Hi Doug -</p>
<p>This is a new feature, just added to the Nightly.  There is a release planned in the next few weeks.  It might be possible to use the newer code with the older release, I didn’t check.</p>
<p>Is there any chance you are a python programmer?  Neither Andrey nor I have a particular use case for 4D nifti files but we added minimal support without planning to take on all possible uses.  if you wanted to customize the interface to suit what’s most convenient that would be great.</p>
<p>Right now the code only tries to read a 4D nifti when there’s one file in the selected folder, but this could obviously be generalized to loop through and load all the files, but also some logic would be needed to tell when it’s a directory of 3D that should be one multivolume vs. a folder with more than one 4D volume.  Perhaps the easiest would be just to add a file browser in addition to the directory browser, perhaps with a radio button to select which to use.  None of this is especially hard to do, but it would be some work to implement, document, test, etc.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L190-L192" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L190-L192" target="_blank" rel="nofollow noopener">fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L190-L192</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="190" style="counter-reset: li-counter 189 ;">
<li>if len(niftiFiles) == 1:</li>
<li> self.read4DNIfTI(mvNode, niftiFiles[0])</li>
<li> return</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #22 by @djrowland (2018-03-15 23:17 UTC)

<p>Again, thanks for all the help. Unfortunately, I am not a python programmer. I have had programming experience (Fortran for computations many years ago), but probably would take me a while to get to know the language and Slicer code. I could ask around here if someone is up to it.</p>
<p>I do like slicer now that I understand it a bit more. It was very helpful with some DTI reconstructions. I have been recommending it to our customers and I am trying to get it running for the group looking at the cardiac data. I think it will be very useful for them.<br>
Doug</p>

---

## Post #23 by @pieper (2018-03-16 00:09 UTC)

<p>We hope you find it useful - I think everyone recognizes that Slicer is a bit of a beast and certainly not for everything.</p>
<p>Best,<br>
Steve</p>

---

## Post #24 by @lassoan (2018-03-16 00:14 UTC)

<aside class="quote no-group" data-username="djrowland" data-post="22" data-topic="1157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/8edcca/48.png" class="avatar"> djrowland:</div>
<blockquote>
<p>I am trying to get it running for the group looking at the cardiac data</p>
</blockquote>
</aside>
<p>4D cardiac DICOM import in Slicer is quite good. Probably one of the best among all open-source applications. If you find any problems with importing cardiac DICOM data then let us know.</p>

---
