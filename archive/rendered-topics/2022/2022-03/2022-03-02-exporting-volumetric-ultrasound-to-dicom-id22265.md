# Exporting volumetric ultrasound to DICOM

**Topic ID**: 22265
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/exporting-volumetric-ultrasound-to-dicom/22265

---

## Post #1 by @koeglfryderyk (2022-03-02 16:41 UTC)

<p>I want to export 3D ultrasound to DICOM.</p>
<p>When I choose the modality as US during export, and then load the exported DICOMs back it into Slicer, it gets loaded as a lot of separate slices, instead of one volume (like for example with an MR or CT):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfbf25d8d5a15e0dfe74f9ea900155aefb41a90a.jpeg" data-download-href="/uploads/short-url/tDOmRrlf6t2HQyMATpqT3Oqjgfw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbf25d8d5a15e0dfe74f9ea900155aefb41a90a_2_345x188.jpeg" alt="image" data-base62-sha1="tDOmRrlf6t2HQyMATpqT3Oqjgfw" width="345" height="188" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbf25d8d5a15e0dfe74f9ea900155aefb41a90a_2_345x188.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbf25d8d5a15e0dfe74f9ea900155aefb41a90a_2_517x282.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbf25d8d5a15e0dfe74f9ea900155aefb41a90a_2_690x376.jpeg 2x" data-dominant-color="E8E8E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1118×612 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can choose MR or CT as the modality and then it gets loaded as one volume, but that does not seem right.</p>
<p>What should I do?</p>

---

## Post #2 by @errollgarner (2022-03-10 16:09 UTC)

<p>Does exporting it to a different format produce the same outcome?</p>

---

## Post #3 by @koeglfryderyk (2022-03-10 16:15 UTC)

<p>When I export it to .nii and import it back again it gets imported as a volume and not slices</p>

---

## Post #4 by @koeglfryderyk (2022-03-10 16:18 UTC)

<p>I also just noticed that I get the following warning (for each slice) when I load the dicoms:</p>
<blockquote>
<p>Warning in DICOM plugin Image sequence when examining loadable 1: US No series description [107]: Image spacing may need to be calibrated for accurate size measurements.</p>
</blockquote>

---

## Post #6 by @lassoan (2022-04-06 05:44 UTC)

<p>There is no commonly used DICOM standard for storing 3D/4D ultrasound images. What software do you plan to use to read the exported images? What DICOM information objects does that software support?</p>

---

## Post #7 by @koeglfryderyk (2022-04-06 14:20 UTC)

<p>Wouldn’t the <a href="https://www.dicomstandard.org/News-dir/ftsup/docs/sups/sup43.pdf" rel="noopener nofollow ugc">Enhanced Ultrasound Volume Storage (EUVS)</a> be the DICOM standard to be used?</p>
<p>I’m preparing data for a publication on TCIA which wants all the data in DICOM - so I can’t say what kind of software other people would use to read those images.</p>
<p>However, I would ideally want to keep using Slicer and Python (Pydicom).</p>

---

## Post #8 by @lassoan (2022-04-06 14:33 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/david_clunie">@David_Clunie</a> What DICOM information object would you recommend to store 3D ultrasound data on TCIA?</p>

---

## Post #9 by @fedorov (2022-04-06 14:38 UTC)

<p>I would recommend staying as close as possible (ie, keep everything that remains after de-identification following a DICOM profile) to the original representation produced by the US scanner, whatever it is. Exporting from NIFTI to any DICOM object will most likely result in meaningless metadata.</p>

---

## Post #10 by @lassoan (2022-04-06 15:07 UTC)

<p>3D ultrasound images in <a href="https://archive.norstore.no/pages/public/datasetDetail.jsf?id=10.11582/2017.00004">RESECT</a> are created using research software, they are in MINC file format and have never been written to DICOM.</p>
<p>The only 3D ultrasound data in TCIA that I know of is the infamous Eigen Artemis volumes in the <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=68550661">Prostate-MRI-US-Biopsy</a> collection, but I would not want to follow bad practices. <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#eigen-artemis">@David_Clunie’s recommendations a few years ago</a> when the Artemis data set was discussed was:</p>
<blockquote>
<p>It would obviously be far preferable (for us) if the submitter did created an Enhanced US Volume instance, but then probably nobody would be able to display it, so in a clinical product they would have to be able to create both, depending on what the user could cope with. They could stuff the Enhanced US Volume attributes (esp. the spatial macros) in the old SOP Class (as a Standard Extended SOP Class), which would probably be a good compromise.</p>
</blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> do you know about any such data set or tools or examples that can create such Standard Extended SOP Class files? Or we should just use the enhanced format and not care about incompatibility with clinical software?</p>

---

## Post #11 by @koeglfryderyk (2022-04-06 15:20 UTC)

<p>I just gave the RESECT file as an example as I’m not allowed to share my data yet. Bu this is how I gather all my data:</p>
<ol>
<li>Ultrasound is recorded during surgery with Brainlab Curve</li>
<li>The data is sent from the Brainlab Curve with OpenIGTLink to a PC with Slicer on it</li>
<li>The files arrive as .nrrd and are saved<br>
(4. In order to publish them I’m supposed to convert them to DICOM)</li>
</ol>

---

## Post #12 by @lassoan (2022-04-06 15:28 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="11" data-topic="22265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<ul>
<li>The data is sent from the Brainlab Curve with OpenIGTLink to a PC with Slicer on it</li>
<li>The files arrive as .nrrd and are saved</li>
</ul>
</blockquote>
</aside>
<p>OK, this is essentially the same as the case with RESECT, i.e., research software creates a 3D ultrasound volume, so the 3D ultrasound DICOM files must be created from scratch.</p>

---

## Post #13 by @fedorov (2022-04-06 15:53 UTC)

<p>Thank you for the clarification, I didn’t know those details.</p>
<p>First and foremost, even if you end up doing the conversion to DICOM, I would recommend including the original data as collected by the acquisition equipment in the final package you will be sharing via TCIA.</p>
<p>If you decide to explore conversion to DICOM, I am not aware of any tools or examples that you could leverage. Reading the recommendation from <span class="mention">@dclunie</span>, it sounds like the recommended approach is not something that anyone implemented before. Quite likely, it will take significant effort to create those standard representations (it is not even clear to me if that compromise suggested would pass David’s validator - and if it is expected that validation will not be passed, it will be challenging to distinguish expected errors from the real errors).</p>
<p>My recommendation would be to proceed with sharing of the data in NRRD format to make them available expediently, and in parallel evaluate the effort that would be required to follow recommendations from David.</p>

---

## Post #14 by @lassoan (2022-04-06 16:02 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="13" data-topic="22265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>My recommendation would be to proceed with sharing of the data in NRRD format to make them available expediently, and in parallel evaluate the effort that would be required to follow recommendations from David.</p>
</blockquote>
</aside>
<p>Sounds good to me. <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> I can offer my help with implementing 3D ultrasound DICOM import/export plugin for Slicer if you can provide a Python script that creates a valid DICOM file (e.g., using <a href="https://pydicom.github.io/">pydicom</a>). I can also help with advice/review your Python script and participate in a few meetings with <a class="mention" href="/u/david_clunie">@David_Clunie</a> and TCIA folks to agree in an acceptable file format.</p>

---

## Post #15 by @fedorov (2022-04-06 16:10 UTC)

<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> if you decide to work on such a converter, I can also advice/participate in a few meetings. I do not anticipate TCIA will have any guidance on the details of DICOM encoding. As long as the result passes David’s validator, or has David’s approval, I am sure it will be fine, so we can save the time. I am not sure David is monitoring this forum, so I will add this topic to my agenda for the weekly meeting with David on Friday, and can update this thread after that. For me the key question is how useful the resulting converter would be for the community beyond your specific use case, and whether the investment of effort is justified.</p>

---

## Post #16 by @koeglfryderyk (2022-04-06 16:25 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> ok, thank you for your advice. I’ll share it as NRRD then, this will save me a lot of time.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you for your offer of help. I think I’ll first try to determine, as <a class="mention" href="/u/fedorov">@fedorov</a> mentioned, whether anyone else would use this and if the investment would make sense.</p>

---

## Post #17 by @koeglfryderyk (2022-04-06 16:28 UTC)

<p>However, I have one last question:</p>
<p>When I load the exported US DICOM, next to the slices there is also a Scalar volume loaded, which contains all the data in one volume, however, the pixel spacing is incorrect (as I describe <a href="https://github.com/Slicer/Slicer/issues/6303" rel="noopener nofollow ugc">here</a>).</p>
<p>So it seems to me like the exporting and loading of 3D US in Slicer kind of works, only that it also loads slices and has wrong pixel spacing</p>

---

## Post #18 by @fedorov (2022-04-08 14:05 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="16" data-topic="22265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> ok, thank you for your advice. I’ll share it as NRRD then, this will save me a lot of time.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> I discussed this with David Clunie today. There is a NRRD to DICOM converter that he has: <a href="https://www.dclunie.com/pixelmed/software/javadoc/com/pixelmed/convert/NRRDToDicom.html" class="inline-onebox">NRRDToDicom</a>, but it currently does not have the features needed to produce DICOM US. David thinks it may not be a very complex task to improve that converter to generate DICOM US, he is willing to spend time on this, and we can justify this work within the scope of the IDC project. BUT in order to start David would need a sample of your data. I understand you are not able to share that yet, but as soon as you can, it would be great if you could update this thread, or email me, so we can start this work.</p>
<p>The converter will likely be useful to others, and you won’t find a better expert to work on this than David Clunie, so let’s make sure we use this opportunity!</p>

---

## Post #19 by @koeglfryderyk (2022-04-15 17:34 UTC)

<p>Would you need a 3D US DICOM or NRRD?</p>

---

## Post #20 by @fedorov (2022-04-15 17:43 UTC)

<p>I thought NRRD is the only thing that you have, no?</p>

---

## Post #21 by @koeglfryderyk (2022-04-15 17:46 UTC)

<p>For most cases we have only NRRDs, but we have DICOMs for a few specific ones. We are still working on getting everything in DICOM, but this depends on on Brainlab fixing some things and not on us.</p>

---

## Post #22 by @fedorov (2022-06-10 20:38 UTC)

<p>To follow up on this, <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> shared a sample phantom scan (can that be shared publicly here in this thread, Fryderyk?), which <a class="mention" href="/u/david_clunie">@David_Clunie</a>  reviewed and provided instructions, sample and conversion tool from Pixelmed toolkit. Can you please let us know Fryderyk if this issue can be resolved? It would be great if we could link the public phantom dataset and David’s instructions here for the benefit of the community.</p>

---

## Post #23 by @gordon-n-stevenson (2022-11-16 05:36 UTC)

<p>Hi all, just picked up this thread while looking into Dicom US options.</p>
<p>I would be interested to know if there was any followup on the use of Pixelmed for this particular use case</p>

---

## Post #24 by @koeglfryderyk (2023-02-03 11:08 UTC)

<p>I think this can be resolved, but I’ll write another comment with an explanation of how to do it. Could you just tell me what is the best way of sharing files? (the NRRD has 30MB, the DICOM 100MB)</p>

---

## Post #25 by @koeglfryderyk (2023-02-03 11:18 UTC)

<p>Volumetric ultrasound can be exported to DICOM using David Clunie’s tool <code>com.pixelmed.convert.NRRDToDicom </code>.</p>
<p>The documentation is <a href="http://www.dclunie.com/pixelmed/software/javadoc/com/pixelmed/convert/NRRDToDicom.html" rel="noopener nofollow ugc">here</a></p>
<p>To use it follow those steps:</p>
<ol>
<li>Make sure you have java installed, if not, install it from <a href="https://www.oracle.com/java/technologies/downloads/#jdk19-mac" rel="noopener nofollow ugc">here</a>
</li>
<li>Download <a href="http://www.dclunie.com/pixelmed/software/20221004_current/index.html" rel="noopener nofollow ugc">pixelmed.jar</a>
</li>
<li>run the following command in your terminal:</li>
</ol>
<pre><code class="lang-auto">java -cp "path_to_pixelmed.jar" -Djava.awt.headless=true \
	com.pixelmed.convert.NRRDToDicom \
	"path_to_the_input.nrrd" \
	"path_to_the_output.dcm \
	"Patient Name" "Patient ID" "Study ID" "Series Number" "Instance Number"
</code></pre>
<p><br>
A US phantom can be found <a href="https://www.dropbox.com/sh/e8s6yj6bcpamfpg/AAABEXQO6xzncmkWKM80DT5Da?dl=0" rel="noopener nofollow ugc">here</a> (in NRRD and exported to DICOM).</p>

---

## Post #26 by @fedorov (2023-02-03 11:29 UTC)

<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> I’ve just shared a dropbox folder with your gmail email - we can use that for sharing the files. Thank you for getting back to this discussion and answering the questions!</p>

---

## Post #27 by @koeglfryderyk (2023-02-03 11:35 UTC)

<p>I still have to figure out how to change the modality from OT to US after the export (David mentioned another one of his <a href="http://www.dclunie.com/pixelmed/software/javadoc/com/pixelmed/apps/SetCharacteristicsFromSummary.html" rel="noopener nofollow ugc">tools</a> to do that, but I haven’t yet figured out how to do that. I’ll update the comment with the solution once I know how to do that</p>

---

## Post #28 by @juanmaverde (2023-02-03 11:58 UTC)

<p>hello all, and really nice to see people investing efforts on this.</p>
<p>We’re working on the space of 3D/4DUS as well, and will be very interesting to have such a converter.</p>
<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> , are you not keeping .mha sequence files?</p>

---

## Post #29 by @koeglfryderyk (2023-02-03 12:45 UTC)

<p>we don’t have .mha files. We’re working with the Brainlab Curve neuronavigation system which only gives us the reconstructed 3D US volume</p>

---
