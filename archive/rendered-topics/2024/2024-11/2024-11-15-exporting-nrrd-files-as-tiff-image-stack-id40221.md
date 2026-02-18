# Exporting NRRD files as TIFF image stack

**Topic ID**: 40221
**Date**: 2024-11-15
**URL**: https://discourse.slicer.org/t/exporting-nrrd-files-as-tiff-image-stack/40221

---

## Post #1 by @jaimigray (2024-11-15 20:10 UTC)

<p>Is there a way we can convert and export our NRRD files as a TIFF stack without exporting to imageJ/IrfanView afterwards to convert the format from DICOM to a TIFF image series? If not, this seems like something we should have, since the major file format for MorphoSource uploads is a TIFFstack…</p>

---

## Post #2 by @muratmaga (2024-11-15 20:50 UTC)

<p>That’s really a MOrphoSource problem, not a Slicer one.</p>
<p>TIFF (or any other 2D format) is not a good format to retain 3D data, particularly for archival purposes. The lack of standardized metadata to describe image spacing, image coordinate system make those formats problematic. We explained this to MorphoSource team multiple times, and while they seem to appreciate the problem, they don’t seem to be willing to act on it.</p>
<p>At this point there is no interest in the Slicer core team to take a NRRD file and convert into an 2D image sequence, since it will create a whole lot of can of worms and possibly degrade the data quality as well.</p>
<p>Having that, there is nothing to stop someone to  write a short python script that will iterate over the image numpy array and write them as a series of 2D images. It is not difficult, in fact all necessary python functions are probably documented in the Slicer script repository.</p>

---

## Post #3 by @jaimigray (2024-11-15 20:52 UTC)

<p>Thanks for the quick answer Murat. I’m trying to walk a 3D Slicer user through uploading their data to MS, so I’ll direct them to conversion outside of the Slicer environment for now.</p>

---

## Post #4 by @muratmaga (2024-11-15 20:53 UTC)

<p>By the way, if you want to see how unpredictable this can be:</p>
<ol>
<li>Download the MRHead dataset</li>
<li>Click ctrl+S and bring up the save as dialog box and choose the format of TIFF. This will save the file as a multiframe tiff (a single tiff image, with slices)</li>
<li>Load that data into Slicer and see that orientaton and spacing is incorrect.</li>
</ol>

---

## Post #5 by @muratmaga (2024-11-15 20:54 UTC)

<p>I suggested the MorphoSource team to collaborate on data exporter from Slicer for this specific use case. That way it would have been possible to control some of the things, but they don’t seem to be interested in that either.</p>

---

## Post #6 by @Amy_Morton (2024-11-18 19:09 UTC)

<p>At <a href="https://autoscoper.readthedocs.io/en/latest/" rel="noopener nofollow ugc">SlicerAutoscoperM</a>, we also deal with TIFF being necessary input to existing software (Autoscoper)</p>
<p>Jaimi, you may find <a href="https://github.com/BrownBiomechanics/SlicerAutoscoperM/blob/main/AutoscoperM/AutoscoperMLib/IO.py" rel="noopener nofollow ugc">some of our module functions</a> helpful.</p>

---

## Post #7 by @aubricot (2024-11-19 17:11 UTC)

<p>Hi Murat, wouldn’t it be feasible to export an nrrd as a tiff stack with a metadata file in the same folder (similar to metadata files exported during recon from projections to tiff stacks)? I’d imagine the relevant info could be retained and recognized by Slicer during subsequent import of the converted tiff stack, just like it is for importing a reconstructed tiff stack. I quickly wrote a little python script (<a href="https://github.com/aubricot/nrrd2tiff/tree/main" rel="noopener nofollow ugc">GitHub nrrd2tiff</a>) to do the conversion and copy over metadata info both from the original scanner metadata file and from the header of the nrrd. I’d love to develop it a bit further to make sure all the relevant information is retained, if you have any advice.</p>

---

## Post #8 by @muratmaga (2024-11-19 17:25 UTC)

<aside class="quote no-group" data-username="aubricot" data-post="7" data-topic="40221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aubricot/48/67544_2.png" class="avatar"> aubricot:</div>
<blockquote>
<p>wouldn’t it be feasible to export an nrrd as a tiff stack with a metadata file in the same folder (similar to metadata files exported during recon from projections to tiff stacks)?</p>
</blockquote>
</aside>
<p>No, not really. That’s poor data management. There are many issues: What is the convention of that file, what fields there would be, what are the units, what format (csv, tab, json, xml?), which reader is going to read all that? Most programs will see a tiff file and completely ignore that file. There is already a well documented, open formats that covers all of that situation, why re-invent the wheel.</p>
<aside class="quote no-group" data-username="aubricot" data-post="7" data-topic="40221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aubricot/48/67544_2.png" class="avatar"> aubricot:</div>
<blockquote>
<p>quickly wrote a little python script (<a href="https://github.com/aubricot/nrrd2tiff/tree/main" rel="noopener nofollow ugc">GitHub nrrd2tiff</a>) to do the conversion and copy over metadata info both from the original scanner metadata file and from the header of the nrrd.</p>
</blockquote>
</aside>
<p>As I said, all the necessary functionality to do that exists, we just don’t want to have it as a core feature of Slicer.</p>
<aside class="quote no-group" data-username="aubricot" data-post="7" data-topic="40221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aubricot/48/67544_2.png" class="avatar"> aubricot:</div>
<blockquote>
<p>d. I’d love to develop it a bit further to make sure all the relevant information is retained, if you have any advice.</p>
</blockquote>
</aside>
<p>Looks good to me. I would suggest reloading your new tiff sequence back into Slicer and double checking that it is indeed complete and consistent with the original data.</p>

---

## Post #9 by @aubricot (2024-11-19 17:33 UTC)

<p>Thanks for the quick response. So far, the datasets I’ve tried seem consistent upon reimport to Slicer, but I will keep verifying before I apply it to all ~130 of the datasets I still need to upload to MorphoSource. Completely understood that converting Nrrd’s to Tiff’s is not an ideal solution for data management best practices, but for those of us that want to use 3D Slicer and upload our datasets to MorphoSource, I don’t see an alternative.</p>

---

## Post #10 by @muratmaga (2024-11-19 17:40 UTC)

<aside class="quote no-group" data-username="aubricot" data-post="9" data-topic="40221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aubricot/48/67544_2.png" class="avatar"> aubricot:</div>
<blockquote>
<p>but for those of us that want to use 3D Slicer and upload our datasets to MorphoSource, I don’t see an alternative.</p>
</blockquote>
</aside>
<p>I understand that, it is a MorphoSource requirement. But what we don’t want to encourage is to use of those formats as primary mean to keep the image data. If you want test, do this:</p>
<p>Crop your original NRRD file and/or put it under a transform. Save it as a new NRRD file, then export your NRRD file your script as your TIFF sequence. Then reload both of them into the Slicer. I suspect your tiff file no longer will have the correct orientation and the origin of the modified NRRD.</p>
<p>That’s what we want to avoid.</p>

---

## Post #11 by @aubricot (2024-11-19 18:19 UTC)

<p>Indeed, the orientation and origin are different for the cropped Nrrd and original. If you all were willing to add a feature to simplify the process for those of us wanting to upload to MorphoSource, it seems like optional form fields in the ImageStacks module for origin, pixel size, height/width/no images would correct for this loss of information. Totally understood that you all don’t want to open this can of worms, though. Thanks for the info, it’s been helpful and interesting.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fb4878d60a02a21b312a66e78d32ca53c22ceaa.jpeg" data-download-href="/uploads/short-url/2eVWzxkdwLzmsCxQmVUDoGPLAxA.jpeg?dl=1" title="Screen Shot 2024-11-19 at 13.14.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fb4878d60a02a21b312a66e78d32ca53c22ceaa_2_690x379.jpeg" alt="Screen Shot 2024-11-19 at 13.14.10" data-base62-sha1="2eVWzxkdwLzmsCxQmVUDoGPLAxA" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fb4878d60a02a21b312a66e78d32ca53c22ceaa_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fb4878d60a02a21b312a66e78d32ca53c22ceaa_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fb4878d60a02a21b312a66e78d32ca53c22ceaa_2_1380x758.jpeg 2x" data-dominant-color="111113"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2024-11-19 at 13.14.10</span><span class="informations">1920×1056 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
