# How to reconstruct 3d heart model from series of short view axis .png files.

**Topic ID**: 9785
**Date**: 2020-01-12
**URL**: https://discourse.slicer.org/t/how-to-reconstruct-3d-heart-model-from-series-of-short-view-axis-png-files/9785

---

## Post #1 by @Jonathan (2020-01-12 17:24 UTC)

<p>Operating system: windows<br>
Slicer version:4.10<br>
Expected behavior: 3d - model using consecutive slices.<br>
Actual behavior: 1d plane - no volume.</p>
<p>I’ve been trying to segment consecutive slices of a porcine heart in short axis view in order to reconstruct a 3d image. I segmented slices in different heights (print screens of several are attached ), yet the outcome was a 1d model.<br>
I also tried to use volume rendering - but I could not managed to use the segmented parts, only the original slices.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb.png" data-download-href="/uploads/short-url/eI79ryW2pOBjm1VSxScu1NMadoD.png?dl=1" title="Screenshot 2020-01-12 at 14.03.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb_2_690x492.png" alt="Screenshot 2020-01-12 at 14.03.50" data-base62-sha1="eI79ryW2pOBjm1VSxScu1NMadoD" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb.png 2x" data-dominant-color="48443B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-01-12 at 14.03.50</span><span class="informations">936×668 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb.png" data-download-href="/uploads/short-url/eI79ryW2pOBjm1VSxScu1NMadoD.png?dl=1" title="Screenshot 2020-01-12 at 14.03.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb_2_690x492.png" alt="Screenshot 2020-01-12 at 14.03.50" data-base62-sha1="eI79ryW2pOBjm1VSxScu1NMadoD" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671b0f033ca0e5e3ebe279127e23542e5233bcfb.png 2x" data-dominant-color="48443B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-01-12 at 14.03.50</span><span class="informations">936×668 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2020-01-12 20:57 UTC)

<p>When you go to Volumes module, and expand the volume information tab for your PNG sequence, what is the volume type reported? If it is vector, Slicer will not render that image and you will need to use the vector2scalar module to change the data type to scalar.</p>
<p>Or you can import your png sequence using the <a class="mention" href="/u/pieper">@pieper</a>’s imagestacks tool:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/pieper/SlicerImageStacks" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/126077?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/pieper/SlicerImageStacks" target="_blank" rel="nofollow noopener">pieper/SlicerImageStacks</a></h3>

<p>Scripted utility to load image stacks (e.g. confocal microscopy) more easily - pieper/SlicerImageStacks</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>which does the conversion automatically.</p>

---

## Post #3 by @Jonathan (2020-01-13 05:59 UTC)

<p>Thanks for the quick reply.<br>
The volume type is a scalar.<br>
I also tried to increase the image spacing, the result was the same.</p>

---

## Post #4 by @muratmaga (2020-01-13 20:53 UTC)

<p>If scalar, you should be able to see 3D rendering of your whole volume with Volume Rendering module. Click the little eye icon on the left-hand side volume name:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2940fa210f9260a0b5038d40953740975f93a6e6.png" data-download-href="/uploads/short-url/5SWMUXJz9lFB3rqeg5bDQoEEKea.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2940fa210f9260a0b5038d40953740975f93a6e6.png" alt="image" data-base62-sha1="5SWMUXJz9lFB3rqeg5bDQoEEKea" width="437" height="499" data-dominant-color="EDEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">542×619 21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-01-13 22:09 UTC)

<p>Where does this data set come from? Can you send a scree shot of the Volume’s module GUI with the information section open and “4-up” view layout showing orthogonal slices?</p>

---

## Post #6 by @Jonathan (2020-01-14 05:15 UTC)

<p>I can see a 3d image. However the slices are on top of one another without any spacing.<br>
Is there a method in 3dslicer by which I can inflate the model, i.e. forcing space inbetween the slices and performing interpolation.<br>
The data itself was taken from an CINE-MRI imaging. The relevant images were selected according to cardiac cycle phase and orientation, and eventually converted to .PNG files.</p>
<p>I can share with you a directory containing the raw data  IMA files as well as the PNG files.</p>
<p>thx<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a091bddbf2ac4c507556bead4519e73b6acab2be.jpeg" data-download-href="/uploads/short-url/mUsE0uDZ4DWEH2ZdK28P0s7udt4.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a091bddbf2ac4c507556bead4519e73b6acab2be_2_690x345.jpeg" alt="Capture" data-base62-sha1="mUsE0uDZ4DWEH2ZdK28P0s7udt4" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a091bddbf2ac4c507556bead4519e73b6acab2be_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a091bddbf2ac4c507556bead4519e73b6acab2be_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a091bddbf2ac4c507556bead4519e73b6acab2be_2_1380x690.jpeg 2x" data-dominant-color="6D6D6E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1949×977 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2020-01-14 05:43 UTC)

<p>If the files is a sequence of 2D files in time then it should not be “inflated to 3D” but should be stored as a sequence of single-slice volumes. You can create such a sequence manually as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes</a>. If you have many data sets to process then you can write a short Python script that does this automatically.</p>
<p>We can already import 3D+t (time sequence of 3D volumes) cine-MRI, CT, and ultrasound images from DICOM. However, if we detect that it is a 2D+t (time sequence of 2D image slices) then we don’t offer to load it as a sequence. Not because it would be hard to implement, but simply because it has not been requested by any funded project or contributed by volunteers so far. Implementation would probably take a few days for an experienced Slicer developer and a few weeks for someone who is completely new to Slicer.</p>

---

## Post #8 by @Jonathan (2020-01-14 07:55 UTC)

<p>Thanks for the quick reply.<br>
I stored the 2d files as a sequence of single-slice volumes as you suggested.<br>
The result was rather the same. screenshots are attached. (The process was performe<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc68f12cd429d38a013ab59a11cab517de23080c.jpeg" data-download-href="/uploads/short-url/qSKBjslFU3PA2OmiDYjLaxymZZ2.jpeg?dl=1" title="3d_sequence" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc68f12cd429d38a013ab59a11cab517de23080c_2_690x324.jpeg" alt="3d_sequence" data-base62-sha1="qSKBjslFU3PA2OmiDYjLaxymZZ2" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc68f12cd429d38a013ab59a11cab517de23080c_2_690x324.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc68f12cd429d38a013ab59a11cab517de23080c_2_1035x486.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc68f12cd429d38a013ab59a11cab517de23080c_2_1380x648.jpeg 2x" data-dominant-color="717178"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_sequence</span><span class="informations">1971×926 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d47bcfa656ed7e62410ce89db8abd99307a74d7.jpeg" alt="3d_sequence_2" data-base62-sha1="b1EsK4SXm3qS8QU3D10Dz8Lvvpl" width="408" height="335"> d before cropping.)</p>

---

## Post #9 by @lassoan (2020-01-14 22:45 UTC)

<p>This does not look like a single-slice volume but as if it has some thickness. After the import into sequence is completed, delete the original slices to make sure they don’t obscure the view.</p>
<p>After you create a segmentation sequence for the volume sequence, what do you plan to use it for?</p>

---

## Post #10 by @Jonathan (2020-01-15 05:33 UTC)

<p>The input files are serial  short axis cross section of the whole heart.<br>
The model which was created, may have some thickness. However, the geometry does not resemble a 3d Heart shape (or even a portion of it). Perhaps the distance inbetween slices is too small.</p>
<p>3d- reconstruction is the ultimate goal.</p>

---

## Post #11 by @lassoan (2020-01-15 13:04 UTC)

<p>It is hard to guess what’s happening. Can you share the data set so that we can have a closer look?</p>

---

## Post #12 by @Jonathan (2020-01-16 06:44 UTC)

<p>of course.<br>
<a href="https://drive.google.com/drive/folders/1b1TPDlqwDu6pZEeGzx4UADFofAIhv_7T?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/1b1TPDlqwDu6pZEeGzx4UADFofAIhv_7T?usp=sharing</a></p>

---

## Post #13 by @lassoan (2020-01-16 16:02 UTC)

<p>I had a look and found that this data set consists of 14 independent 2D cine-MRI series, each contains only 1 time point, and each one is acquired at a different position. This of course does not make sense at all, because if you only acquire a single time point then you don’t need to use a cine-MRI protocol, and if you want to acquire a 3D volume then you would acquire all the slices in one series.</p>
<p>You can hack the metadata in the files to make them appear as a single series (I did that, the result is available <a href="https://www.dropbox.com/sh/gng5sbttr1pwil8/AAAKVUbqVDKuTHLym_e6cxgwa?dl=0">here</a>), but it would be much better to acquire images properly in the first place.</p>
<p>The png files should not be used at all, because their bit depth is just 8 instead of the original 11, so subtle contrast changes in the image are discarded. (The image spacing information is lost during png conversion, too, but you can recover that by typing the correct spacing values in the volumes module, so this information loss is not critical.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22eed3c047fd828a77f9261c87ca0b5876ab8e8a.jpeg" data-download-href="/uploads/short-url/4Z1UXUb6u6rYk2gNJIuCDWp2zx0.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22eed3c047fd828a77f9261c87ca0b5876ab8e8a_2_690x305.jpeg" alt="image" data-base62-sha1="4Z1UXUb6u6rYk2gNJIuCDWp2zx0" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22eed3c047fd828a77f9261c87ca0b5876ab8e8a_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22eed3c047fd828a77f9261c87ca0b5876ab8e8a_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22eed3c047fd828a77f9261c87ca0b5876ab8e8a.jpeg 2x" data-dominant-color="2A2A2A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1296×573 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @Jonathan (2020-01-17 11:52 UTC)

<p>Thanks for the detailed answer.<br>
I have the entire cine-MRI data. It serves for deferent purposes.<br>
My goal is to reconstruct a 3D heart model at a single time point (end diastolic phase for example).</p>
<p>When I tried to reconstruct the model by using the IMA files the picture orientation was oblique and I failed to segment the components, hence I chose a specific time point and tried to convert the files to png format.The volume data was lost during the conversion, as you said and the correction of the spacing values was also  unsuccessful.</p>
<p>I will gladly share the entire MRI files. it might be an overkill though…</p>
<p>Thanks again for your help</p>

---

## Post #15 by @lassoan (2020-01-17 13:33 UTC)

<p>Yes, the complete study is needed to be able to load it correctly (as a volume sequence). After loading the 4D data set, you can then still decide to segment only one or all time points. If you do not succeed in loading the complete study then please send the complete study and I can investigate.</p>
<p>Oblique orientation is no problem - you can either snap to closest acquisition plane by a single click or segment on oblique slices. See details here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---

## Post #16 by @Jonathan (2020-01-18 17:34 UTC)

<p>Thanks again for the guidance. I tried uploading the entire study via the DICOM uploader and also via the simple file uploader. I am still trying to fix the orientation and to crop the slices for a better visualisation.<br>
so far I was able to progress.</p>
<p>A link of the complete study:<br>
<a href="https://drive.google.com/file/d/1VQsZj6LelMqkHiqBvaCvpL4g4BNiS1kY/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/1VQsZj6LelMqkHiqBvaCvpL4g4BNiS1kY/view?usp=sharing</a></p>

---

## Post #17 by @lassoan (2020-01-19 21:19 UTC)

<p>Thank you, I’ve checked and the study has lots of time sequence series and they seem to load fine.</p>
<p>To segment a single timepoint only, you can load an image time series as MultiVolume node and in “MultiVolume explorer” module check “Enable copying while sliding” to make the volume appear as a regular scalar volume.</p>
<p>To create a segmentation sequence, you can use Sequences extension instead (install Sequences extension, in menu: Edit/Application settings/DICOM/Preferred multi-volume import format select “volume sequence”, then load the selected series). To create a segmentation time series, you can create a segmentation node and create a sequence from it using Sequence Browser module. The GUI is not very intuitive, so if you have any questions then let us know.</p>

---

## Post #18 by @Jonathan (2020-01-20 12:44 UTC)

<p>I encounter several issues:</p>
<ol>
<li>The image is not aligned. I rotated it (Rotate to volume plane) for one axis. when I tried the other two axes I got the same image.</li>
</ol>
<p>2.I have been trying to use the Sequence extension, by creaing a sequence of all short axis slides (see pic). I went to “Sequence browser” module to replay the sequence. Yet nothing was played. Finally, the sequence I created was not on the list of volumes under the section of “Volume Rendring”.</p>

---

## Post #19 by @lassoan (2020-01-20 12:50 UTC)

<aside class="quote no-group" data-username="Jonathan" data-post="18" data-topic="9785">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jonathan/48/5635_2.png" class="avatar"> Jonathan:</div>
<blockquote>
<p>The image is not aligned. I rotated it (Rotate to volume plane) for one axis. when I tried the other two axes I got the same image.</p>
</blockquote>
</aside>
<p>Single-slice volumes are always rotated to the image plane. Maybe you have loaded a single-slice volume (sequence).</p>
<p>Anyway, if you align slice views to volume axes by clicking on the “warning” icon in Segment Editor module then you should see 3 orthogonal slices.</p>
<aside class="quote no-group" data-username="Jonathan" data-post="18" data-topic="9785">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jonathan/48/5635_2.png" class="avatar"> Jonathan:</div>
<blockquote>
<p>I have been trying to use the Sequence extension, by creaing a sequence of all short axis slides (see pic). I went to “Sequence browser” module to replay the sequence. Yet nothing was played.</p>
</blockquote>
</aside>
<p>Make sure you replay the sequence that you see in the slice view.</p>
<aside class="quote no-group" data-username="Jonathan" data-post="18" data-topic="9785">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jonathan/48/5635_2.png" class="avatar"> Jonathan:</div>
<blockquote>
<p>Finally, the sequence I created was not on the list of volumes under the section of “Volume Rendring”.</p>
</blockquote>
</aside>
<p>If you use Volume Sequences module then this does not happen. If you use MultiVolume then in “MultiVolume explorer” module check “Enable copying while sliding” to make the volume appear in the scene as a regular scalar volume.</p>

---

## Post #20 by @Jonathan (2020-02-11 18:12 UTC)

<p>Sorry for the late reply.<br>
I tried recording a sequence by using the horizontal scroll bars (red yellow and green). However , the image is constant/frozen once the alignment of the axis is performed. (cannot skip between the snapshots), which makes it impossible to record;  yet when I uploaded the png images instead of the DICOM files (all have already been sorted to a specific timeframe), I was able to use the side scroll bars to record and segment the axial view slices.</p>
<p>perhaps my loading process itself is wrong? should I use the DICOM uploader or to upload by “Add Data” (tried both). Should I check the “Single File” option?</p>

---

## Post #21 by @lassoan (2020-02-11 20:06 UTC)

<p>I’ve uploaded a screen capture video that shows how to import, load, and view your data: <a href="https://1drv.ms/v/s!Arm_AFxB9yqHuqZm30QtZX1dENaceQ?e=tmwBBr">https://1drv.ms/v/s!Arm_AFxB9yqHuqZm30QtZX1dENaceQ?e=tmwBBr</a></p>

---
