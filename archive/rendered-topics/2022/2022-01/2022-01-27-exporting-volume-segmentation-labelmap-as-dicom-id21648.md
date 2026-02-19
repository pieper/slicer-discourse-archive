---
topic_id: 21648
title: "Exporting Volume Segmentation Labelmap As Dicom"
date: 2022-01-27
url: https://discourse.slicer.org/t/21648
---

# Exporting Volume + Segmentation LabelMap as DICOM

**Topic ID**: 21648
**Date**: 2022-01-27
**URL**: https://discourse.slicer.org/t/exporting-volume-segmentation-labelmap-as-dicom/21648

---

## Post #1 by @Fluvio_Lobo (2022-01-27 03:14 UTC)

<p>Hello,</p>
<p>I am trying to export a Scalar Volume, which combines the original CT and the binary Label-Maps of the segmentation, as DICOM. Below is a coronal section of the volume and three labels, one of which is a cranioplasty implant. The purpose is to share the volume using a viewer like OHIF and get feedback through annotations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa294d480788b63e09358a448010b1039647cd64.jpeg" data-download-href="/uploads/short-url/zH1R6jP9McwFxJjZNA2SzLOIdHC.jpeg?dl=1" title="combined_volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa294d480788b63e09358a448010b1039647cd64_2_345x233.jpeg" alt="combined_volume" data-base62-sha1="zH1R6jP9McwFxJjZNA2SzLOIdHC" width="345" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa294d480788b63e09358a448010b1039647cd64_2_345x233.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa294d480788b63e09358a448010b1039647cd64_2_517x349.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa294d480788b63e09358a448010b1039647cd64_2_690x466.jpeg 2x" data-dominant-color="292927"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">combined_volume</span><span class="informations">1263×855 70.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I created the volume using the <strong>Mask Volume</strong> seg. editor effect, which only allows me to assign a greyscale intensity value per mask. So;</p>
<ol>
<li>
<p>Is it possible to assign a color as in the Label-Map?</p>
</li>
<li>
<p>Do DICOM volumes even support color? i.e. would I even be able to export as DICOM…</p>
</li>
<li>
<p>Is there a more efficient approach at generating these Volumes with Label-Maps</p>
</li>
</ol>

---

## Post #2 by @lassoan (2022-01-27 03:59 UTC)

<p>OHIF can display DICOM segmentation object overlaid on the volume. To create a DICOM segmentation object, you can convert the labelmap to segmentation and follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">these instructions</a>. I’ve also created a detailed video tutorial that demonstrates a full segmentation object roundtrip between OHIF-&gt;Slicer-&gt;OHIF:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="60_hzSlptWY" data-video-title="Using 3D Slicer with cloud DICOMweb databases" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=60_hzSlptWY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/60_hzSlptWY/maxresdefault.jpg" title="Using 3D Slicer with cloud DICOMweb databases" width="" height="">
  </a>
</div>


---

## Post #3 by @Fluvio_Lobo (2022-01-27 05:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>When exporting the segmentation as DICOM, the DICOMSegmentation option does not appear as shown on the video. This is what shows for me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54e8f7f0891629c29d60e6e5a30dfa87e1dc70c8.png" data-download-href="/uploads/short-url/c79eTxYYdXsfsF2uICxRWzXnYKs.png?dl=1" title="windows" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54e8f7f0891629c29d60e6e5a30dfa87e1dc70c8.png" alt="windows" data-base62-sha1="c79eTxYYdXsfsF2uICxRWzXnYKs" width="527" height="500" data-dominant-color="393B3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">windows</span><span class="informations">662×628 33.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-01-27 05:09 UTC)

<p>See the instructions that I linked above, You need to install Quantitative Reporting extension to have Segmentation Object export.</p>

---

## Post #5 by @Fluvio_Lobo (2022-01-27 15:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>This is working so far. One thing I noticed is that I had to use the <strong>DICOM Patcher</strong> for some of the original datasets. Otherwise, sending to the KHEOPS server kept throwing <strong>Error 409</strong></p>

---

## Post #6 by @Fluvio_Lobo (2022-01-27 19:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Following-up on this.<br>
How to you export a modified base or reference volume?<br>
I tend to clone and modify the cloned volume node to preserve the original. For instance, applying a filter and maybe even a transformation.<br>
When I export to DICOM, the segmentation is the only node that actually gets exported.<br>
If I use the scalar volume exporter, the process generates an additional study.</p>

---

## Post #7 by @lassoan (2022-01-27 19:51 UTC)

<p>The behavior might have been different in earlier Slicer versions, but in the current version (recent Slicer Preview Releases) if you export an image by right-clicking on it in the Data module then:</p>
<ul>
<li>if you leave <code>StudyInstanceUID</code> empty then it will be set based on where you have the image in the Subject Hierarchy tree (first tab in Data module)</li>
<li>if you set the <code>StudyInstanceUID</code>, <code>FrameOfReferenceInstaceUID</code> to match another study (and preferably copy all the other patient and study field values, too) and generate a new <code>SeriesInstanceUID</code> value then the image will appear under that other patient/study</li>
</ul>
<p>If you use this via the GUI then the first option is definitely easier. If you process the images automatically then the second may be a bit simpler and more explicit. Although if you do batch processing then it may be simpler to use DICOM Patcher module, which does not disassemble the image and puts it back together, but just changes individual DICOM tags. You can even add custom rules by a couple of lines of Python script to address specific non-conformities that you encounter and not fixed by default.</p>

---

## Post #8 by @Fluvio_Lobo (2022-01-27 20:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I am running <strong>4.13.0-2022-01-16</strong>, do I need to grab the latest latest?</p>
<p>This is what happens when I go through the GUI;</p>
<ul>
<li>On my data module, I clone the volume and name it differently. Then I create a segmentation with a single segment (not shown)</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d2b79deecb67b17f474d29b706d3abdf3a1967b.jpeg" alt="data_module" data-base62-sha1="fzLbRmUB1KSY1HtZbtRr7bWIw7F" width="598" height="234"></p>
<ul>
<li>Right-click and pull the “exporter”. I leave everything blank and export the volume using the scalar volume exporter.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9eec4969d12edb84e1b850bd0ec6a99eea95d57c.jpeg" data-download-href="/uploads/short-url/mFTGj9HnaFr845pO40c5W5DvqSE.jpeg?dl=1" title="export_gui" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9eec4969d12edb84e1b850bd0ec6a99eea95d57c_2_527x500.jpeg" alt="export_gui" data-base62-sha1="mFTGj9HnaFr845pO40c5W5DvqSE" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9eec4969d12edb84e1b850bd0ec6a99eea95d57c_2_527x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9eec4969d12edb84e1b850bd0ec6a99eea95d57c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9eec4969d12edb84e1b850bd0ec6a99eea95d57c.jpeg 2x" data-dominant-color="353637"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">export_gui</span><span class="informations">662×628 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>A different study is generated after a successful export.</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e7e4045d8f8954373ce4cf8dc2a0a4862673d4.jpeg" alt="separate_output" data-base62-sha1="wEZGzYo4F41a8WnqctM5UUNpK5u" width="545" height="108"></p>

---

## Post #9 by @lassoan (2022-01-27 20:48 UTC)

<p>Thank you, you are right, I could reproduce the behavior. It seems that you need to set the 3 IDs manually for now. You can get the ID values by right-clicking on the original series in the DICOM database and choose “View DICOM metadata” and then “Copy metadata”. I’ll see if we can automate this process to make it easier to export data to the same study as the original.</p>

---

## Post #10 by @Fluvio_Lobo (2022-01-28 14:51 UTC)

<p>I thought of looking into the volume attributes to confirm that these IDs had copied through, and they did…</p>
<p>Here are the IDs on the cloned volume,</p>
<pre><code class="lang-auto">&gt;&gt;&gt; instUids = vol2.GetAttribute("DICOM.instanceUIDs").split()
&gt;&gt;&gt; filename = slicer.dicomDatabase.fileForInstance(instUids[0])
&gt;&gt;&gt; print(slicer.dicomDatabase.fileValue(filename, "0020,0052"))
1.3.12.2.1107.5.1.4.73059.30000022011009555884900000009
&gt;&gt;&gt; print(slicer.dicomDatabase.fileValue(filename, "0020,000d"))
2.16.840.1.114151.2557845743209115757346250429223761125620220110
&gt;&gt;&gt; print(slicer.dicomDatabase.fileValue(filename, "0020,000e"))
1.3.12.2.1107.5.1.4.73059.30000022011009505325400001687
</code></pre>
<p>Here are the IDs for the original volume;</p>
<pre><code class="lang-auto">&gt;&gt;&gt; instUids = vol1.GetAttribute("DICOM.instanceUIDs").split()
&gt;&gt;&gt; filename = slicer.dicomDatabase.fileForInstance(instUids[0])
&gt;&gt;&gt; print(slicer.dicomDatabase.fileValue(filename, "0020,0052"))
1.3.12.2.1107.5.1.4.73059.30000022011009555884900000009
&gt;&gt;&gt; print(slicer.dicomDatabase.fileValue(filename, "0020,000d"))
2.16.840.1.114151.2557845743209115757346250429223761125620220110
&gt;&gt;&gt; print(slicer.dicomDatabase.fileValue(filename, "0020,000e"))
1.3.12.2.1107.5.1.4.73059.30000022011009505325400001687
</code></pre>
<p>Then I started copying them manually into the GUI and realized that the <code>SeriesInstanceUID</code> needs to be different in order for this to work!</p>
<p>In other words, I think copying the volume node does preserve the <code>SeriesInstanceUID</code> instead of changing it. Is there a way to programmatically change this DICOM attribute?</p>

---

## Post #11 by @lassoan (2022-01-28 23:16 UTC)

<p>I’ve made the DICOM export more convenient. In Slicer Preview Release that you download tomorrow or later images that show up under the same study in the subject hierarchy tree will be exported by default into the same study (the study instance UID is now populated automatically).</p>
<p>You can copy the frame of reference UID from the original image to the modified image if you want fused image display in external software.</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="10" data-topic="21648">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>I think copying the volume node does preserve the <code>SeriesInstanceUID</code> instead of changing it. Is there a way to programmatically change this DICOM attribute?</p>
</blockquote>
</aside>
<p>A DICOM series is not allowed to be changed, ever, without generating new Series instance UID. If a file must be corrected then you send a “delete” request to the PACS (this hides the old instance); then push a new version of the image (that references the old hidden version). The same UID keeps referring to the same content.</p>
<p>Therefore, since the same series instance UID cannot be reused in another image, I would recommend to leave the series instance UID empty, which will generate a new UID automatically.</p>
<p>I’ve added some more information to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">DICOM export section in the documentation</a>.</p>
<p>Again, this new behavior is implemented in the Slicer Preview Release that you download tomorrow or later.</p>

---
