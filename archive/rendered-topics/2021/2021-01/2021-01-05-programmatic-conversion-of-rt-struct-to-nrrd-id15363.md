---
topic_id: 15363
title: "Programmatic Conversion Of Rt Struct To Nrrd"
date: 2021-01-05
url: https://discourse.slicer.org/t/15363
---

# Programmatic Conversion of RT Struct to nrrd

**Topic ID**: 15363
**Date**: 2021-01-05
**URL**: https://discourse.slicer.org/t/programmatic-conversion-of-rt-struct-to-nrrd/15363

---

## Post #1 by @PhilippG (2021-01-05 22:01 UTC)

<p>Hi, I first want to say how impressed I am with the persistent and comprehensive support provided by the slicer team on these forums!</p>
<p>Now for the boring part…</p>
<p>I’m looking to programmatically convert an RTstruct file to a nrrd binary mask via python using the slicer python interpreter for a particular contour. I have attempted running the batch processing module in RTslicer via command line but it a) did not operate as intended and b) purports to convert all of the potential segmentations. For these reasons I would prefer to code the iterative conversion myself. Unfortunately, I’m a little lost with respect to which functions to use in order to achieve this goal. I was having similar troubles with converting a dicom series to nrrd until I found <a class="mention" href="/u/lassoan">@lassoan</a> had made an excellent post describing a <a href="https://discourse.slicer.org/t/fastest-way-to-load-dicom/9317/2">procedure</a> that helped me a lot. Something similar to the linked post would be ideal, but any guidance would be much appreciated!</p>
<p>Thanks again</p>

---

## Post #2 by @cpinter (2021-01-05 23:54 UTC)

<aside class="quote no-group" data-username="PhilippG" data-post="1" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3ab097/48.png" class="avatar"> PhilippG:</div>
<blockquote>
<p>a) did not operate as intended and b) purports to convert all of the potential segmentations. For these reasons I would prefer to code the iterative conversion myself.</p>
</blockquote>
</aside>
<p>It is always better both for you and the community to fix something existing instead of implementing it again from scratch, especially if the purpose of the tool you decide not to use is exactly what you need. Please describe why the BatchProcessing module in SlicerRT does not work for you. We are happy to help you adapt it.</p>

---

## Post #4 by @PhilippG (2021-01-06 19:34 UTC)

<p>I suppose you’re correct. Let’s get into it then, I’m working with (as a start) the MAASTRO Lung1 dataset available on TCIA that you may be familiar with. I downloaded it via the NBIA retriever. Within the dataset each patient has a corresponding folder containing 3 folders: one for the dicom series, one for the RTstruct and one for the segmentation.</p>
<p>My understanding was that running the script included in the “readme” in the command line was meant to convert all of the RT structs (each segmentation within) present in the entire dataset (containing all of the patient folders) into binary mask nrrds that would be stored in the output folder. In short I used the following as guidance(from the readme):</p>
<blockquote>
<p>Usage:<br>
[path/]Slicer.exe --no-main-window --python-script [path/]BatchStructureSetConversion.py --input-folder input/folder/path --output-folder output/folder/path<br>
(Optionally use -i and -o instead of the long argument names)<br>
Additional arguments:<br>
–ref-dicom-folder (-r): Folder containing reference anatomy DICOM image series, if stored outside the input study<br>
–use-ref-image (-u): Use anatomy image as reference when converting structure set to labelmap<br>
–exist-db (-x): Process an existing database instead of importing data in a new one (in this case --input-folder is a database and not a folder containing DICOM data)<br>
–export-images (-m): Export all image data alongside the labelmaps to NRRD</p>
</blockquote>
<p>Because the folder housing all the patient folders contains both the structs and dicom series I did not use a dicom reference folder or reference image. I did use -m because I figured it may be more convenient for future implementation if it worked.</p>
<p>Upon running the script I found that only the segmentations from (what appears to be) the first patient appeared “LUNG-001” in the output folder, rather than nrrds for the RT struct of every patient. It’s possible that there was an error but I found it difficult to troubleshoot without error messages. I will say that upon examining the generated output for this singular patient, I was very happy with the quality of conversion!</p>
<p>Beyond the error, the file names produced by the script do not lend themselves to facile interpretation and <em><strong>every</strong></em> contour from the RT struct is saved as a separate file whereas I’m seeking to only extract the gross tumour volume (GTV). Granted, this is a very minor issue as I could filter out the unnecessary files out afterwards and computation efforts are not a significant for me in this case.</p>
<p>Let me know what further information I can provide or if I’ve misinterpreted the use-case of the script that I employed as I am somewhat of a neophyte when it comes to this stuff.</p>
<p>Thanks!</p>
<p>Other information:<br>
System: Windows 10 pro<br>
Slicer version: 4.11.20200930</p>

---

## Post #5 by @cpinter (2021-01-07 13:59 UTC)

<aside class="quote no-group" data-username="PhilippG" data-post="4" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3ab097/48.png" class="avatar"> PhilippG:</div>
<blockquote>
<p>was meant to convert all of the RT structs (each segmentation within) present in the entire dataset (containing all of the patient folders) into binary mask nrrds that would be stored in the output folder. In short I used the following as guidance(from the readme</p>
</blockquote>
</aside>
<p>Correct.</p>
<aside class="quote no-group" data-username="PhilippG" data-post="4" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3ab097/48.png" class="avatar"> PhilippG:</div>
<blockquote>
<p>folder housing all the patient folders contains both the structs and dicom series I did not use a dicom reference folder or reference image</p>
</blockquote>
</aside>
<p>Are you sure the image and the RT struct are in the same DICOM study? You can check it if you import the folder to Slicer’s DICOM database and see if selecting one study (middle table) you’ll see both series on the bottom.</p>
<aside class="quote no-group" data-username="PhilippG" data-post="4" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3ab097/48.png" class="avatar"> PhilippG:</div>
<blockquote>
<p>I found that only the segmentations from (what appears to be) the first patient appeared “LUNG-001” in the output folder</p>
</blockquote>
</aside>
<p>I’m not sure I understand this. What do you mean by segmentation here? The RT struct is a segmentation. You wrote above that there is a third object in the folders, which is a segmentation. Are you talking about that? If so, what format is it?</p>
<aside class="quote no-group" data-username="PhilippG" data-post="4" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3ab097/48.png" class="avatar"> PhilippG:</div>
<blockquote>
<p>whereas I’m seeking to only extract the gross tumour volume (GTV)</p>
</blockquote>
</aside>
<p>This is a feature that could be added potentially.</p>

---

## Post #6 by @PhilippG (2021-01-08 16:20 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Correct</p>
</blockquote>
</aside>
<p>That’s reassuring</p>
<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Are you sure the image and the RT struct are in the same DICOM study? You can check it if you import the folder to Slicer’s DICOM database and see if selecting one study (middle table) you’ll see both series on the bottom.</p>
</blockquote>
</aside>
<p>The RT struct and dicom series for each patient are attributed to the same study, and I believe that they are mapping onto each other as the results for the first patient are great. I’ve attached an image from slicer for your reference in case I’m missing something. Note that there appears to be no study ID/description (this is the case for all patients), I’m not sure if that may be causing the issue in loading the subsequent patients? Although, it’s strange that this didn’t present to be an issue for the first patient if that’s the case.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97384de85ccc1e65c6ce3f818497ebacb9b1dfb2.png" data-download-href="/uploads/short-url/lzKJecFPAzoPldxBLpJqS4ublbI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97384de85ccc1e65c6ce3f818497ebacb9b1dfb2.png" alt="image" data-base62-sha1="lzKJecFPAzoPldxBLpJqS4ublbI" width="690" height="190" data-dominant-color="D1E2EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1264×349 13.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I’m not sure I understand this. What do you mean by segmentation here? The RT struct is a segmentation. You wrote above that there is a third object in the folders, which is a segmentation. Are you talking about that? If so, what format is it?</p>
</blockquote>
</aside>
<p>Apologies for inconsistent terminology. To clarify, my issue is that upon running the script I only found nrrd masks corresponding to the RT struct segmentations (and corresponding volume nrrd with command ‘-m’) for the first patient, rather than all patients.<br>
The third object in the folders I was referring as a segmentation was a .dcm segmentation object, you’re welcome to disregard this detail as I have since removed those files from my database and ran the script again to the same result (conversion of RT struct and dicom series to nrrds files for the first patient only).</p>
<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>This is a feature that could be added potentially.</p>
</blockquote>
</aside>
<p>Excellent</p>

---

## Post #7 by @cpinter (2021-01-08 16:42 UTC)

<p>Perfect, thank you for the detailed descriptions!</p>
<p>A simple question first in case it indicates something: is there any error or suspicious entry in the output on stdout or the log file?</p>

---

## Post #8 by @PhilippG (2021-01-08 17:43 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="15363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>A simple question first in case it indicates something: is there any error or suspicious entry in the output on stdout or the log file?</p>
</blockquote>
</aside>
<p>There appears to be no error or suspicious entry.</p>

---

## Post #9 by @cpinter (2021-01-11 08:55 UTC)

<p>OK then can you please share at least two of the patients (you said only the first patient is converted so I guess two will do it)? If not then please try to reproduce it with two freely accessible patients (for example from TCIA). And also your command line command. Thanks!</p>

---

## Post #10 by @PhilippG (2021-01-13 00:02 UTC)

<p>Hi, the dataset I’m working with actually is from TCIA! It’s the lung1 dataset from the MAASTRO clinic <a href="https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics" rel="noopener nofollow ugc">see here</a>. So in this case the patient labelled lung-001 is the only one that gets converted.</p>
<p>The command line is as follows:</p>
<pre><code>C:\&gt;"C:/Users/guevorgp/AppData/Local/NA-MIC/Slicer 4.11.20200930/Slicer.exe" --no-main-window --python-script "C:/Users/guevorgp/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/BatchStructureSetConversion.py" --input-folder "E:/NSCLC-2Patients" --output-folder "P:/ForPyradiomics/SlicerOutput2" -m    
</code></pre>
<p>Let me know if there’s any additional information that you might find useful.</p>

---

## Post #11 by @cpinter (2021-01-18 16:37 UTC)

<p>The link you posted gives a 404 error with a message that the server is under maintenance, and I cannot find a dataset with MAASTRO in its name in the TCIA browser. Is it this one?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea68369061ad7a0086de72ccc71bb6e52598db6.png" data-download-href="/uploads/short-url/fMRh2H9LWsmLcpZYETJOOIqARyC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea68369061ad7a0086de72ccc71bb6e52598db6.png" alt="image" data-base62-sha1="fMRh2H9LWsmLcpZYETJOOIqARyC" width="660" height="500" data-dominant-color="F2F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1018×771 34.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @cpinter (2021-01-19 11:34 UTC)

<p>Still getting the 404 error…</p>

---

## Post #13 by @PhilippG (2021-01-20 23:44 UTC)

<p>Very unfortunate timing but it appears to be back up now:</p>
<p><a href="https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics" class="onebox" target="_blank" rel="noopener nofollow ugc">https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics</a></p>

---

## Post #14 by @cpinter (2021-01-21 08:59 UTC)

<p>Thanks! I’ll look at it when I have a free hour again.</p>

---

## Post #15 by @PhilippG (2021-02-02 01:17 UTC)

<p>Hey,</p>
<p>Just wondering if you’ve had a chance to look at this and whether you think a fix would be straightforward to implement. Otherwise, I would appreciate a reference to some functions in the slicer API that would suit my application in the meantime.</p>
<p>Thanks!</p>

---

## Post #16 by @cpinter (2021-02-03 10:17 UTC)

<p>I took a look at it and ran the script on a folder containing four of the patients in the large 33GB dataset you referenced.</p>
<p>Based on the console output and the code, it seems that the current version of the script only supports processing the first patient if you do not use an existing database (<code>--exist-db (-x)</code> argument). I don’t see any reason for this limitation and actually it seems easy to fix.</p>

---

## Post #17 by @cpinter (2021-02-03 11:08 UTC)

<p>I implemented the improvement, see <a href="https://github.com/SlicerRt/SlicerRT/commit/c77aaf51abb0f13b431102d4d8e5143e7e748c69" class="inline-onebox">ENH: Allow BatchStructureSetConversion to convert multiple patients · SlicerRt/SlicerRT@c77aaf5 · GitHub</a></p>
<p>Your command line should work, and instead of only processing the first patient it will process all patients, and will put the output of each patient in its own folder named the patient database ID (i.e. incremental numbers). You can try it in tomorrow’s preview version.</p>

---

## Post #18 by @PhilippG (2021-02-03 17:33 UTC)

<p>This is very exciting, I will report back shortly with confirmation!</p>

---

## Post #19 by @PhilippG (2021-02-04 22:40 UTC)

<p>I can confirm that it now works great! Thanks a lot Csaba, if you’re ever around Western University I will get you a coffee or a mineral water.</p>

---
