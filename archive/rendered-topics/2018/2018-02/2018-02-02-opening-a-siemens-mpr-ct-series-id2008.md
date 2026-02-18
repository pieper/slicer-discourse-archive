# Opening a Siemens MPR CT series

**Topic ID**: 2008
**Date**: 2018-02-02
**URL**: https://discourse.slicer.org/t/opening-a-siemens-mpr-ct-series/2008

---

## Post #1 by @opetne (2018-02-02 08:47 UTC)

<p>Operating system: Windows<br>
Slicer version:18/01/14 nightly<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,</p>
<p>I have a series of animal cardiac CT made on a Siemens Somatom Sensation Cardiac. Since the ECG differs from the humans I made an MPR from 0-100% of the cardiac cycle. If I want to open this series only a small wave like series appears and I can’t select any special timepoint of the cardiac cycle.<br>
Do you now a soultion for that?</p>
<p>Thanks in advance,</p>
<p>Ors</p>

---

## Post #2 by @pieper (2018-02-02 23:50 UTC)

<p>I don’t know if anyone has experience with this.  Since it’s not human data maybe you could share it and maybe someone could have a look?</p>

---

## Post #3 by @opetne (2018-02-03 15:19 UTC)

<p>Dear Steve,</p>
<p>Thank you forthe idea. How can I share the dataset? It says the file format is not authorised. It’s a zipped folder</p>
<p>Ors</p>

---

## Post #5 by @pieper (2018-02-03 16:58 UTC)

<p>Hi Ors - Usually we use google drive, dropbox, or similar service and then post the link here.<br>
-Steve</p>

---

## Post #6 by @opetne (2018-02-05 08:31 UTC)

<p>Dear Steve,</p>
<p>Here is the link. I hope it works.<br>
<a href="https://tinyurl.com/y7zjc23q" class="onebox" target="_blank" rel="nofollow noopener">https://tinyurl.com/y7zjc23q</a></p>
<p>Best,</p>
<p>Ors</p>

---

## Post #7 by @pieper (2018-02-05 14:34 UTC)

<p>Hi Ors -</p>
<p>Interesting data - I can import it via the dicom module but not with the Add Data menu.  As far as I can see there’s just one volume here (1051 slices).  If you export a time series it might load as a multivolume.</p>
<p>The image positions are not in a form Slicer can use, so you get warnings when loading the volume and it uses a default spacing of 1mm.  If I manually change that to .13mm (edit in the Volumes module as shown in the image) I get something that looks better, but perhaps you know the correct value.</p>
<p>HTH,<br>
Steve</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01a0e9ff8ab24f6ff39edb1a146739b53e0194d5.jpeg" data-download-href="/uploads/short-url/epewqZzQwLvTt61rTT7FFt5U2N.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01a0e9ff8ab24f6ff39edb1a146739b53e0194d5_2_690x443.jpg" alt="image" data-base62-sha1="epewqZzQwLvTt61rTT7FFt5U2N" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01a0e9ff8ab24f6ff39edb1a146739b53e0194d5_2_690x443.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01a0e9ff8ab24f6ff39edb1a146739b53e0194d5_2_1035x664.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01a0e9ff8ab24f6ff39edb1a146739b53e0194d5_2_1380x886.jpg 2x" data-dominant-color="919193"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1969×1265 572 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @opetne (2018-02-05 16:16 UTC)

<p>Dear Steve,</p>
<p>The dataset comes from a turkey cardiac CT series and contains the images<br>
of the whole cardiac cycle. The “funny” appearance comes from this<br>
phenomena, I think. Since the ECG and the triggering is adapted for the<br>
human ECG the timepoints saved by the machine doesn’t represent the real<br>
systole or diastole of the turkey. It is very complicated to save the raw<br>
data from the CT directly this is why I saved the cardiac cycle from 0 to<br>
100%.<br>
There is an option if I upload this series to the syngovia software and<br>
reconstruct it at certain cycle phase and save it again. I was wondering if<br>
I could do this with the Slicer without this step. The other question is if<br>
I could make a video out of it with the Slicer?</p>
<p>Ors</p>

---

## Post #9 by @pieper (2018-02-05 16:37 UTC)

<p>Hi Ors -</p>
<p>Ah, yes, that explains a little more about the why it loaded the way it did and looks “funny”.</p>
<p>You may be able to use the MultiVolumeImporter module if you know the dicom tags that differentiate the frames of the cine sequence.  (See the Advanced section, I know the default ones don’t recognize this as a time series).  If you find a tag that works of this data it might make sense to add it as another default.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/MultiVolumeImporter" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/MultiVolumeImporter</a></p>
<p>You can also look at the Sequences extension:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences</a></p>
<p>Once you have the data loaded you can make a movie with ScreenCapture.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/ScreenCapture" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/ScreenCapture</a></p>
<p>HTH,<br>
Steve</p>

---

## Post #10 by @opetne (2018-02-05 18:29 UTC)

<p>Dear Steve,</p>
<p>Sorry for being a bad padavan but I couldn’t open it with anything you<br>
suggested. The multivolume importer doesn’t do anything. I checked the<br>
metadata of the image series but there were not such data the module<br>
requires (this is a CT series, so no echo and repetition time and flip<br>
angle).<br>
It would be realy nice to be able to open the series somehow and make a<br>
video out of it to check the best timepoint for diastole and systole.</p>
<p>Best,</p>
<p>Ors</p>

---

## Post #11 by @pieper (2018-02-05 19:04 UTC)

<p>Hi Ors -</p>
<p>Right - the MultiVolumeImporter only sees a single frame here (see the error log after clicking import), I hope <a class="mention" href="/u/fedorov">@fedorov</a> can advise on this.</p>
<p>With the data imported and selected in the Slicer dicom database you can bring up the metadata as shown below and see which tags are changing and ImageComments seems like it would work to delineate the frames, but it’s not clear how to make this work for the MultiVolumeImporter.</p>
<p>-Steve</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/058497285bf5e4a9a4978d052b29e0c82a553051.png" data-download-href="/uploads/short-url/MOsAtsE1BohCj8Zbgd6cIOmrJf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/058497285bf5e4a9a4978d052b29e0c82a553051_2_472x500.png" alt="image" data-base62-sha1="MOsAtsE1BohCj8Zbgd6cIOmrJf" width="472" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/058497285bf5e4a9a4978d052b29e0c82a553051_2_472x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/058497285bf5e4a9a4978d052b29e0c82a553051_2_708x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/058497285bf5e4a9a4978d052b29e0c82a553051_2_944x1000.png 2x" data-dominant-color="F3F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1371×1450 82.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @fedorov (2018-02-06 17:00 UTC)

<p><a class="mention" href="/u/opetne">@opetne</a> indeed, the dataset, as is, cannot be parsed as a multivolume node, but looking at the dataset - this is expected.</p>
<p>Multivolume DICOM plugin makes certain assumptions about the dataset  to be able to parse it:</p>
<ol>
<li>
<p>The dataset has a fourth dimension, and the frames in the dataset can be sorted into groups by that fourth dimension. The result of this sorting should be such that each group have the same number of frames, and that group of frames should be possible to reconstruct into a valid 3-d volume.</p>
</li>
<li>
<p>The heuristics of how frames should be sorted into groups is defined by the DICOM tags that will be examined for sorting as defining the 4th dimension. The current list of tags that will be examined are here: <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporterPlugin.py#L35-L53" class="inline-onebox">MultiVolumeImporter/MultiVolumeImporterPlugin.py at master · fedorov/MultiVolumeImporter · GitHub</a></p>
</li>
</ol>
<p>Looking at your dataset, the multivolume frames are identified by “ImageComments”, but also “ScanOptions”. And conveniently, cardiac cycle is already parsed out of the first item in the “ScanOptions” tag (<a href="https://github.com/fedorov/MultiVolumeImporter/commit/8b6cff76ee7cae048c91619ba2668381e80c85fb">contributed</a> by <a class="mention" href="/u/lassoan">@lassoan</a>!).</p>
<p>However, your dataset does not satisfy the first assumption. After I sorted the files in your dataset by “ImageComments”, I see that the number of frames is not identical for every unique value of “ImageComments” (compare 0% and 10%, for example)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef66d781a84fd96c35c5645a7c555d5fdd5d960c.png" data-download-href="/uploads/short-url/y9Qs5qzvCFRAfupAElAWfMvjG9u.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef66d781a84fd96c35c5645a7c555d5fdd5d960c_2_690x213.png" alt="image" data-base62-sha1="y9Qs5qzvCFRAfupAElAWfMvjG9u" width="690" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef66d781a84fd96c35c5645a7c555d5fdd5d960c_2_690x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef66d781a84fd96c35c5645a7c555d5fdd5d960c_2_1035x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef66d781a84fd96c35c5645a7c555d5fdd5d960c_2_1380x426.png 2x" data-dominant-color="1A1B1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2290×710 92.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To fix this, I did the following:</p>
<ol>
<li>ran <a href="https://github.com/fedorov/DICOMScripts/blob/master/separateByTagValue.py">this script</a> to sort by “ImageComments”</li>
<li>removed the folder that corresponds to 0%, as it was the only one with the inconsistent number of frames (of course, a better way is to find the specific offending frame, and remove that one file, but I didn’t have a handy tools to do this quickly)</li>
<li>used “DICOM Patcher” module of Slicer to normalize the file path, since “ImageComments” has special characters and import was failing.</li>
<li>Imported the “clean” dataset from the output folder produced by DICOM Patcher.</li>
</ol>
<p>Once this is done, I am able to load the dataset (minus 0% frame) into Slicer as a multivolume - see a demo here: <a href="https://www.screencast.com/t/ggcHB3Z1">https://www.screencast.com/t/ggcHB3Z1</a></p>

---

## Post #13 by @opetne (2018-02-06 21:00 UTC)

<p>Dear Andrey,</p>
<p>I am totaly impressed, thank you! That is a very promising result.</p>
<p>Thanks,</p>
<p>Ors</p>

---

## Post #14 by @opetne (2018-02-07 11:36 UTC)

<p>Dear Andrey,</p>
<p>Thank you for your help. I don’t have such developed skills in script<br>
running, so I asked onee of my colleagues. He modified the script a bit,<br>
like the output path and we experineced that the 0% folder conatins always<br>
1 more image than the others. I could open the series successfuly.<br>
One more question of course, if you have time to anser it. At some of the<br>
animals I’m not sure wether the systole or diastole was saved at the<br>
correct timepoint. As stepping through the frames, I can see exactly what<br>
the real systole or diastole is. Is there a chance to see what cardiac<br>
cycle they belong? I mean which phase (%) between 0 and 100%? On the graph<br>
there is only the signal intensity showed.</p>
<p>Best,</p>
<p>Ors</p>

---

## Post #15 by @fedorov (2018-02-07 14:56 UTC)

<p>In the MultiVolumeExplorer there is a slider for selecting the frame to be shown, and the frame number. Knowing that your frames are in 5% increments, you can calculate the phase %.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/577877d43b35a89871243c5fde06f14814818a4f.png" data-download-href="/uploads/short-url/ctNDMkmI0fhS703yGusVZAp7kCP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/577877d43b35a89871243c5fde06f14814818a4f_2_690x470.png" alt="image" data-base62-sha1="ctNDMkmI0fhS703yGusVZAp7kCP" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/577877d43b35a89871243c5fde06f14814818a4f_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/577877d43b35a89871243c5fde06f14814818a4f_2_1035x705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/577877d43b35a89871243c5fde06f14814818a4f.png 2x" data-dominant-color="C4C4C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×733 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @opetne (2018-02-07 20:12 UTC)

<p>Thank you! I was not sure that there is a direct link between the frame<br>
number and the cardiac cycle.</p>
<p>Ors</p>
<p>Andrey Fedorov <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> (időpont: 2018. febr. 7., Sze,<br>
16:07) ezt írta:</p>

---
