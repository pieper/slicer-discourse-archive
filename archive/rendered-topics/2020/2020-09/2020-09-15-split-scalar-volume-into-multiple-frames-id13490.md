# Split Scalar Volume into Multiple Frames

**Topic ID**: 13490
**Date**: 2020-09-15
**URL**: https://discourse.slicer.org/t/split-scalar-volume-into-multiple-frames/13490

---

## Post #1 by @Fluvio_Lobo (2020-09-15 13:49 UTC)

<p>Hello,</p>
<p>I am trying to split scalar-DICOM volume, with multiple frames, so that I can create multiple volumes.<br>
I am trying to do this because the multi-volume exporter does not seem to recognize the input volume as a multi-volume.</p>
<p><strong>UPDATE:</strong> <em>Just checked, these DICOMs I am having issues with lack the “trigger time” tag on the metadata/headers. I compared them to some that do import as multi-volumes</em></p>
<p>Thoughts?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f20479c42cbf153a4b50298a4d23ebab4528faf.png" data-download-href="/uploads/short-url/90reRa9KVBOWnFPg8x1S4szzXpt.png?dl=1" title="issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f20479c42cbf153a4b50298a4d23ebab4528faf.png" alt="issue" data-base62-sha1="90reRa9KVBOWnFPg8x1S4szzXpt" width="690" height="74" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">issue</span><span class="informations">1433×154 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-09-15 17:36 UTC)

<p>These are the fields that we currently recognize as fields that may be used to split a volume:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/fedorov/MultiVolumeImporter/blob/8a81b4395e9093875b0f90a3a1b479b0832f8c36/MultiVolumeImporterPlugin.py#L37-L57" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/fedorov/MultiVolumeImporter/blob/8a81b4395e9093875b0f90a3a1b479b0832f8c36/MultiVolumeImporterPlugin.py#L37-L57" target="_blank" rel="noopener">fedorov/MultiVolumeImporter/blob/8a81b4395e9093875b0f90a3a1b479b0832f8c36/MultiVolumeImporterPlugin.py#L37-L57</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="37" style="counter-reset: li-counter 36 ;">
<li>self.multiVolumeTags['TriggerTime'] = "0018,1060"</li>
<li>self.multiVolumeTags['EchoTime'] = "0018,0081"</li>
<li>self.multiVolumeTags['FlipAngle'] = "0018,1314"</li>
<li>self.multiVolumeTags['RepetitionTime'] = "0018,0080"</li>
<li>self.multiVolumeTags['AcquisitionTime'] = "0008,0032"</li>
<li>self.multiVolumeTags['SeriesTime'] = "0008,0031"</li>
<li>self.multiVolumeTags['ContentTime'] = "0008,0033"</li>
<li># Siemens Somatom Cardiac CT 'ScanOptions' tag contains info on cardiac cycle</li>
<li>self.multiVolumeTags['CardiacCycle'] = "0018,0022"</li>
<li># GE Revolution CT uses 'NominalPercentageOfCardiacPhase' tag to identify cardiac cycle</li>
<li>self.multiVolumeTags['NominalPercentageOfCardiacPhase'] = "0020,9241"</li>
<li># this one is GE-specific using the private tag</li>
<li>self.multiVolumeTags['Siemens.B-value'] = "0019,100c"</li>
<li>self.multiVolumeTags['GE.B-value'] = "0043,1039"</li>
<li># used on some GE systems, with 2D acquisitions</li>
<li>self.multiVolumeTags['TemporalPositionIdentifier'] = "0020,0100"</li>
<li># Philips DWI</li>
<li>self.multiVolumeTags['Philips.B-value'] = "2001,1003"</li>
<li>self.multiVolumeTags['Standard.B-value'] = "0018,9087"</li>
<li># GE Revolution CT Kinematics protocol</li>
<li>self.multiVolumeTags['DeltaStartTime'] = "0043,101e"</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>We are making adjustments, add more tags as we encounter valid data sets that are not recognized.<br>
Could you try if latest Slicer Preview Release can recognize it as a time sequence?</p>
<p>If the latest version does not recognize your data but you believe that your data set is correct and complete (e.g., DICOM tags were removed by too aggressive anonymization) then we can see if we can add one more tag to split by.</p>

---

## Post #3 by @Fluvio_Lobo (2020-09-15 18:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you for the response!</p>
<p>First, let me clarify that I must have done something weird before when reading the metadata. If I import the dataset alone, I do read “trigger time” in the metadata</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1ee5656d23b030f2b337b72ab18c92ded158231.png" data-download-href="/uploads/short-url/ywdHKm3FiThVXmt7B3E9VMNGSVb.png?dl=1" title="trigger_value" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1ee5656d23b030f2b337b72ab18c92ded158231_2_690x100.png" alt="trigger_value" data-base62-sha1="ywdHKm3FiThVXmt7B3E9VMNGSVb" width="690" height="100" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1ee5656d23b030f2b337b72ab18c92ded158231_2_690x100.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1ee5656d23b030f2b337b72ab18c92ded158231_2_1035x150.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1ee5656d23b030f2b337b72ab18c92ded158231_2_1380x200.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">trigger_value</span><span class="informations">1559×227 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As expected (I believe), there are about 9 values for trigger time. I am estimating about 9 frames per slice. The values are [0,  61443, 122886, 184328, 245771, 307213.99, 368657.01, and 430099]</p>
<p>If I use the <strong>MultiVolumeImporter</strong>, I get a “multivolume” named “664 frames MultiVolume.” I then use the <strong>MultiVolumeExplorer</strong> to copy a specific frame, the it seems to only get a single frame and not the entire sequence!</p>

---

## Post #4 by @lassoan (2020-09-15 18:35 UTC)

<p>Do not use MultiVolumeImporter module for this. You should be able to simply load the data set using DICOM module.</p>
<p>Can you share the data set? (make sure it is anonymized, animal, or phantom)</p>

---

## Post #5 by @Fluvio_Lobo (2020-09-15 18:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I am adding the data <a href="https://app.box.com/s/p3vm4eztkb78s4sfbi7sza4ukpwp3rme" rel="noopener nofollow ugc">here</a><br>
The data is from <a href="https://www.cancerimagingarchive.net/" rel="noopener nofollow ugc">The Cancer Image Archive</a><br>
As far as I know, it has been properly anonymized</p>

---

## Post #6 by @lassoan (2020-09-15 20:54 UTC)

<p>Multi-volumes can only be imported if the volumes form hypercubes (all timepoints have the same geometry). In this data set, 84 slices are found for TriggerTime=[0.0], 82 slices are found for TriggerTime=[61443.0], and 83 slices are found for TriggerTime=[122886.0, 184328.0, 245771.0, 307213.99, 368657.01, 430099.0].</p>
<p>There may be an issue with the data set and so it may be safer to reject it.</p>

---

## Post #7 by @Fluvio_Lobo (2020-09-15 21:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Wow, that is very random. I think this could very well be an issue with the dataset. I have been going through other datasets and found nothing similar, everything is importing fine.</p>
<p>I have to go through about 10 more, so I will be sure to follow-up and tell you if the error occurred again.</p>
<p>Thank you!</p>

---

## Post #8 by @Fluvio_Lobo (2020-09-17 13:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I can confirm that it was some download error from the TCIA database. I re-downloaded the two datasets that had this issue and Slicer properly recognized them as multivolumes.</p>

---

## Post #9 by @lassoan (2020-09-17 13:42 UTC)

<p>Thank you, this is very useful feedback. It indicates that (at least in some cases) it makes sense to be strict and reject suspicious data sets instead of being more tolerant for errors.</p>

---
