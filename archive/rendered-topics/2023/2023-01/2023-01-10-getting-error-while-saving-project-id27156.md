# Getting error while saving project

**Topic ID**: 27156
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/getting-error-while-saving-project/27156

---

## Post #1 by @Dwij_Mistry (2023-01-10 09:24 UTC)

<p>Dear sir,<br>
I was working on one case, in which my area of interest is<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae1c47f36c33ad8a225bde2d6d07756f9deb0df4.png" data-download-href="/uploads/short-url/oQfFEbNdBxdUlI2f10WG69iSccc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae1c47f36c33ad8a225bde2d6d07756f9deb0df4_2_690x315.png" alt="image" data-base62-sha1="oQfFEbNdBxdUlI2f10WG69iSccc" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae1c47f36c33ad8a225bde2d6d07756f9deb0df4_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae1c47f36c33ad8a225bde2d6d07756f9deb0df4_2_1035x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae1c47f36c33ad8a225bde2d6d07756f9deb0df4_2_1380x630.png 2x" data-dominant-color="33353A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1910×873 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Dataset: <a href="https://jajalmedicals.sharepoint.com/:u:/s/CodePandas/EWQU_S52NABMoyWmxn-9ydYBdjddvCFeBgo2NkaeNVvkrA?e=Za2EKY" rel="noopener nofollow ugc">Anonymize.zip</a></p>
<p>while saving I am getting this error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/832e7d4f3301324d58726e28a041700f71f2f86e.png" data-download-href="/uploads/short-url/iIu9pUjpLL1HVDK158TuY2giPD0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832e7d4f3301324d58726e28a041700f71f2f86e_2_690x440.png" alt="image" data-base62-sha1="iIu9pUjpLL1HVDK158TuY2giPD0" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832e7d4f3301324d58726e28a041700f71f2f86e_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832e7d4f3301324d58726e28a041700f71f2f86e_2_1035x660.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832e7d4f3301324d58726e28a041700f71f2f86e_2_1380x880.png 2x" data-dominant-color="2F2B2C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1482×946 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">[Qt] class QList&lt;class qSlicerFileWriter *&gt; __cdecl qSlicerCoreIOManagerPrivate::writers(const class QString &amp;,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLScene *) const warning: Unable to find node with ID "" in the given scene.
[VTK] vtkMRMLVolumeArchetypeStorageNode::UpdateFileList: Failed to write 'C:/Users/Team B/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleSaveTemp-2023-01-10_144146_115/2023-01-10-Scene/Data/TempWrite3 /3 .625 PLAIN.nrrd'.
[VTK] vtkMRMLScene::WriteToMRB: Failed to save C:/Users/Team B/Desktop/2023-01-10-Scene.mrb: Failed to save scene to data bundle directory
[Qt] bool __cdecl qSlicerCoreIOManager::saveNodes(class QString,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLMessageCollection *,class vtkMRMLScene *) error: Saving failed with all writers found for file "C:/Users/Team B/Desktop/2023-01-10-Scene.mrb" of type "SceneFile"
[Qt] void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save error: "- Error: 3: .625 PLAIN (vtkMRMLScalarVolumeNode1): Failed to write 'C:/Users/Team B/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleSaveTemp-2023-01-10_144146_115/2023-01-10-Scene/Data/TempWrite3 /3 .625 PLAIN.nrrd'.\n- Error: Failed to save C:/Users/Team B/Desktop/2023-01-10-Scene.mrb: Failed to save scene to data bundle directory\n- Error: Failed to save scene as C:/Users/Team B/Desktop/2023-01-10-Scene.mrb\n- Error: Saving failed with all writers found for file 'C:/Users/Team B/Desktop/2023-01-10-Scene.mrb' of type 'SceneFile'.\n"

</code></pre>
<p>I am unable to save the case.<br>
Thank you</p>

---

## Post #2 by @pieper (2023-01-10 18:28 UTC)

<p>Do you only get the error for this particular series?</p>

---

## Post #3 by @Dwij_Mistry (2023-01-11 06:44 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
Getting error in those series who is starting with <strong>“.625”</strong> series description<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/129ccadffe48b1cc474d299c2ab9d074075618f7.png" data-download-href="/uploads/short-url/2EEwhZ7T3jsuFuKEuAs17k8cagf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/129ccadffe48b1cc474d299c2ab9d074075618f7_2_690x391.png" alt="image" data-base62-sha1="2EEwhZ7T3jsuFuKEuAs17k8cagf" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/129ccadffe48b1cc474d299c2ab9d074075618f7_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/129ccadffe48b1cc474d299c2ab9d074075618f7_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/129ccadffe48b1cc474d299c2ab9d074075618f7_2_1380x782.png 2x" data-dominant-color="31414F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×818 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have tries on Mimics software in that I am able to save all cases without error.</p>

---

## Post #4 by @cpinter (2023-01-11 13:57 UTC)

<p>Can you try saving it in a directory that does not have spaces in the path (<code>"Team B"</code>)? Just a thought.</p>

---

## Post #5 by @pieper (2023-01-11 17:11 UTC)

<aside class="quote no-group" data-username="Dwij_Mistry" data-post="1" data-topic="27156">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dwij_mistry/48/15265_2.png" class="avatar"> Dwij_Mistry:</div>
<blockquote>
<p>Dataset: <a href="https://jajalmedicals.sharepoint.com/:u:/s/CodePandas/EWQU_S52NABMoyWmxn-9ydYBdjddvCFeBgo2NkaeNVvkrA?e=Za2EKY">Anonymize.zip</a></p>
</blockquote>
</aside>
<p>This link didn’t work for me.  Can you try opening up the permissions?</p>

---

## Post #6 by @Dwij_Mistry (2023-01-12 04:23 UTC)

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1dfcyK1lZozlhsBy7xoS2nkRq9JigwOkf/view?usp=share_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1dfcyK1lZozlhsBy7xoS2nkRq9JigwOkf/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1dfcyK1lZozlhsBy7xoS2nkRq9JigwOkf/view?usp=share_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1dfcyK1lZozlhsBy7xoS2nkRq9JigwOkf/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">Anonymize.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/pieper">@pieper</a> here is the updated link</p>

---

## Post #7 by @pieper (2023-01-13 23:50 UTC)

<p>Thanks for sharing the anonymized data.</p>
<p>I was able to import the dicom data, save a series that included the “.625” string to a file, and then correctly reload.  I tested this on a mac.  Maybe someone can test on windows?</p>

---
