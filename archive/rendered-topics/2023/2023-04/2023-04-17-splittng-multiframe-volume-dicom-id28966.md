# Splittng multiframe/volume DICOM

**Topic ID**: 28966
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/splittng-multiframe-volume-dicom/28966

---

## Post #1 by @William (2023-04-17 14:04 UTC)

<p>Let me start by saying I am a novice in the use of DICOM files when it comes to anything more than viewing/interpreting the final products in PACS, so please excuse me for the use of any incorrect nomenclature, I will do my best to explain this in a way that will help you help me.</p>
<p>I am currently in the process of performing spectral analysis on DECT images. For this I require the iodine(-water) and water(-iodine) maps. Both these maps are produced in a single series, so if there are 450 slices, the series will contain 900 images, for each position one iodine-water and one water-iodine map. In PACS (Sectra IDS7) when one opens the series it allows you to scroll through 450 images of the first set (iodine-water) after which it “loops around” and one can scroll through the 450 images of the second set (water-iodine), in doing so it stays within the same series (making this presumably a multivolume/multiframe series). So far so good.</p>
<p>However when I load the images into 3D slicer using the DICOM loader it jumbles the sets. Individually each set is still in the right order, but the two sets are merged with (random) break points (i.e. it will be in the order of A1-A2-A3 B1-B2-B3-B4 A4-A5 B4-B5 … A448 B449 B500 A449 A500, with A and B being the two sets). This makes it rather hard to interpret, but more importantly not very useful when it comes to segmentation prior to analysis.</p>
<p>I tried using the advanced DICOM viewer and followed the instructions found here <a href="https://discourse.slicer.org/t/switch-between-multiple-images-type-in-one-series/6542/3" class="inline-onebox">Switch between multiple images type in one series - #3 by n2018</a>, but so far to no avail. The problem, in so far as I can tell, is that the tags that differ between the one set and the other are not included in the grouptags of MultiVolumeImporterPlugin. Though from what I gather from several other posts (e.g.: <a href="https://discourse.slicer.org/t/split-scalar-volume-into-multiple-frames/13490" class="inline-onebox">Split Scalar Volume into Multiple Frames</a>) this plugin is not the advised way to be tackling this problem anyway.</p>
<p>When exploring the DICOM file metadata, the tags that differentiate between the two sets are:</p>
<p><strong>(0008,103e) SeriesDescription</strong> with one being named XXX_iodine-water and the other XXX_water-iodine (no real surprise there I suppose).<br>
<strong>(0029,0010) PrivateCreator</strong> with water-iodine NOT containing this tag, and iodine-water having it set to “SECTRA_ImageInfo_01”.<br>
<strong>(0029,1005) Unknown Tag &amp; Data</strong> with water-iodine again not having this tag, and iodine-water being set to “-2048”.</p>
<p>I assume from this that Sectra PACS is using these last two tags to differentiate between one set and the other.</p>
<p>Is there a way to split these two set within 3D-slicer? If not, what would you suggest would be the best way to solve this problem? (which at face value seems like it should be relatively easy to solve, but it is giving me a headache nonetheless).<br>
If any additional information is required please let me know.</p>
<p>Thank you in advance for your time!</p>

---

## Post #2 by @lassoan (2023-04-17 14:53 UTC)

<p>Unfortunately, this is a very typical situation with DICOM. Each vendor implement 4D image support differently (using different grouping tags). We need to add a vendor-specific logic to split the series.</p>
<p>You can modify the MultiVolumeImporterPlugin.py file locally (in your Slicer installation folder) or if you provide an anonymized sample data set then we can make the changes.</p>
<p>Based on what you described, splitting based on <code>SeriesDescription</code> would be the most meaningful, but I would have a look at the tags again to see if there is really nothing else.</p>
<p><code>(0029,0010) PrivateCreator</code> just specifies the group for the private tag “SECTRA_ImageInfo_01 (0029, xx05)”. This tag is added by the Sectra PACS (<a href="https://sectraprodstorage01.blob.core.windows.net/medical-uploads/2020/04/conformance-statement-22.1.pdf">https://sectraprodstorage01.blob.core.windows.net/medical-uploads/2020/04/conformance-statement-22.1.pdf</a>) and it specifies <code>Original pixel padding value</code>, which is just a coincidence that happens to be different in the subseries, so I would not use that.</p>
<p>I would expect to see difference in the KVP value in the sub-series and/or differences in some private tags. Maybe some relevant DICOM tags disappeared during anonymization? Try to have a look at tags of non-anonymized images or try to get images directly from the CT console (maybe there are some automatic processing/validation rules in the CT that alter DICOM tags).</p>

---

## Post #3 by @William (2023-04-17 16:05 UTC)

<p>Thank you for the speedy reply!</p>
<p>Indeed, in the process of of anonymization it seems to have scrubbed the files of most identifying tags (such as KVP values, and pretty much all private tags other than the ones mentioned in my previous post).<br>
I am currently not in the position to post the data set, but later this week this should be possible (should it haven’t been solved by then).</p>
<p>I implemented your suggested solution in MultiVolumeImporterPlugin.py, but I believe I have done it too naively. I simply added <code>self.multiVolumeTags['seriesDescription'] = "0008,103E"</code> and <code>self.multiVolumeTagsUnits['SeriesDescription'] = "name"</code><br>
to the <code># tags used to identify multivolumes</code> block of code. Then I ran the MultiVolumeImporter module with <code>Frame identifying DICOM tag (if known):</code> set to “0008,103E” and <code>Frame identifying units:</code> set to “name” (corresponding with the changes I made in the script).<br>
This then results in a a single output node of 900 frames that are still in the same wrong order as previously.</p>
<p>On a side note, I have since tried using the dcm2niix plugin you mentioned in another thread, which <em>almost</em> gives the desired results. It gives me the volume of the first set (iodine-water).</p>

---

## Post #4 by @William (2023-04-17 17:03 UTC)

<p>Solved! I was rather stupidly editing the MultiVolumeImporter<strong>Plugin</strong>.py and then <em>using</em> the module. I then remembered your post from the other thread in which you explicitly state not to use the ‘MultiVolumeImporter’ module and instead to use the DICOM importer module with the right <strong>plugin</strong> selected. Furthermore I noticed that the seriesDescription tag was not working for differentiation purposes (I believe this may have something to do with the name, which in its unabbreviated form is rather long and has special characters in it). I instead took your advise to look for a more suitable tag, and found that the WindowLevel and WindowCenter tags were unique for each of the two sets (and have simpler numerical values attached to them). Performing an examine with these changes then allowed me to load in 2 separate multivolumes, one for each of the iodine-water/water-iodine maps.</p>
<p>Thank you very much for your help!</p>
<p>(Tomorrow I will do some more testing and see if I can find out why exactly the seriesDescription tag did not perform the way I expected it to)</p>

---

## Post #5 by @lassoan (2023-04-17 17:58 UTC)

<p>Thanks for the update, these sound very promising.</p>
<p>Window Level/Center tags are not ideal for splitting, because they may vary within the subseries or they may happen to be set for the same values in both subseries.</p>
<p>A much more robust solution would be to adjust anonymization settings to preserve very basic image acquisition information, including KVP. Then split based on KVP.</p>

---

## Post #6 by @William (2023-04-18 10:10 UTC)

<p>Indeed, for this study population I checked and it happens to be part of the protocol to have it split this way on the windowcenter//level, but it is by no means robust. As you say a less  aggressive anonymization would be most ideal. Again, thank you for the valuable help.</p>

---
