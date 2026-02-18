# Facial muscle segmentation using MONAI Auto3DSeg

**Topic ID**: 35734
**Date**: 2024-04-24
**URL**: https://discourse.slicer.org/t/facial-muscle-segmentation-using-monai-auto3dseg/35734

---

## Post #1 by @philippepellerin (2024-04-24 15:16 UTC)

<p>Greetings. Much congratulations!<br>
As a professional in the field of medical imaging and segmentation, your work on the thorax, abdomen, and brain is undoubtedly significant. However, I believe that your expertise could also greatly benefit the field of facial segmentation.<br>
A year ago, with the hope of emulating a future “whole head segmentation,” I contacted Jakob Wassertal. I made a proposal to help and, for that purpose, segmented the masticatory muscles in 20 patients (masseter, temporal, medial, and lateral pterygoid muscles). I sent the data to Jakob, but I can’t see anything coming this way.<br>
If you believe that the data I previously shared could be useful for the MONAI Auto3DSeg, I’m more than willing to resend the files for your review and potential use.</p>

---

## Post #2 by @diazandr3s (2024-04-24 16:29 UTC)

<p>Hi <a class="mention" href="/u/philippepellerin">@philippepellerin</a>,</p>
<p>Thanks for your message.<br>
Could you please provide more details of the dataset (resolution, size, etc)? I guess they are CT images, but please confirm. Is it 4 segments (masseter, temporal, medial, and lateral pterygoid muscles)?<br>
Also, do you have a plan as to how to license the dataset?</p>
<p>I could definitely give it a try with Auto3DSeg and make the model available here for you to try.</p>
<p>Please let us know</p>

---

## Post #3 by @philippepellerin (2024-04-24 16:54 UTC)

<p>Hi Andreas, for those 20 folders I have the anonymized .dicom volume, the segments for 6 items ( right and left) .<br>
Just tell me what you need, in which format, all the segmentations were performed with Slicer so I can export in whatever format Slicer is able to.<br>
There is no license for this data set, It would be my very pleasure to share and helping to improve your incredible software.<br>
Best regards.</p>
<p>Envoyé de mon iPhone</p>

---

## Post #4 by @diazandr3s (2024-04-24 18:33 UTC)

<p>Hi <a class="mention" href="/u/philippepellerin">@philippepellerin</a>,</p>
<p>If you could export volumes and segmentations into NRRD format with the same name for each volume/segmentation pair, I can train the Auto3DSeg and see how that goes.</p>
<p>Let me know,</p>

---

## Post #5 by @philippepellerin (2024-04-24 18:39 UTC)

<p>Will do that tomorrow (local time France)<br>
Regards</p>
<p>Envoyé de mon iPhone</p>

---

## Post #6 by @philippepellerin (2024-04-25 08:09 UTC)

<p>Hi Andreas, just to be sure, you need for each case: a file including the CT volume in .NRRD and another file including the segmentation in .NRRD, as well.<br>
Is it important that the names for each segment be in the same order in the slicer segmentation module before exporting the NRRD?<br>
Regards.</p>

---

## Post #7 by @diazandr3s (2024-04-25 08:33 UTC)

<p>Hi <a class="mention" href="/u/philippepellerin">@philippepellerin</a>,</p>
<blockquote>
<p>a file including the CT volume in .NRRD and another file including the segmentation in .NRRD, as well.</p>
</blockquote>
<p>That’s correct.</p>
<blockquote>
<p>Is it important that the names for each segment be in the same order in the slicer segmentation module before exporting the NRRD?</p>
</blockquote>
<p>No, the order is not important. However, please make sure the segment names are the same for all samples - same spelling and avoiding capital letters</p>
<p>Let me know,</p>

---

## Post #8 by @philippepellerin (2024-04-25 08:41 UTC)

<p>Got it. You’ll find a link to download the first case, could you check it and tell me if it is convenient. <a href="https://www.dropbox.com/t/Dns21NN05aEm9l8I" class="inline-onebox" rel="noopener nofollow ugc">Transfer - Dropbox</a></p>

---

## Post #9 by @lassoan (2024-04-25 13:15 UTC)

<p>The best is if you select the correct terminology code for all your segments:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fdaeb10fd5e1bbefdb0fc103cd0ca4a34e4c76f.jpeg" data-download-href="/uploads/short-url/fXw1ORlOivTFztcgZEBYNl88b5J.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fdaeb10fd5e1bbefdb0fc103cd0ca4a34e4c76f_2_690x332.jpeg" alt="image" data-base62-sha1="fXw1ORlOivTFztcgZEBYNl88b5J" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fdaeb10fd5e1bbefdb0fc103cd0ca4a34e4c76f_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fdaeb10fd5e1bbefdb0fc103cd0ca4a34e4c76f_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fdaeb10fd5e1bbefdb0fc103cd0ca4a34e4c76f_2_1380x664.jpeg 2x" data-dominant-color="454D53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×924 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This ensures that there are no typos or inconsistent spelling. There might be anatomical structures that you are interested in but not included in the default terminology. In this case, you can keep using just “Tissue” as property type and use the “Name” field consistently to identify the structure - and send the segment name and SNOMED CT terminology code to <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>
<p>How to get the SNOMED CT terminology code:</p>
<ul>
<li>Go to <a href="https://browser.ihtsdotools.org/">SNOMED CT browser</a>, accept the license agreement</li>
<li>Click “Go browsing international edition”</li>
<li>Check the “body structure” checkbox on the left side in “Filter results by Semantic Tag” section</li>
<li>In the search box, type the structure you segment - for example: <code>masseter</code></li>
<li>Click on the relevant item in the list below, for example <code>Left masseter muscle</code>. <em>Tip:</em> ignore the items that start with <code>Entire</code> word (it has a special meaning that it is not used in DICOM), instead select the item that has description starting with <code>Structure of</code> or ends with <code>structure</code>.</li>
<li>The information that you need are the structure name and SCTID values that are displayed on the right side in “Concept details” section, For example, <code>left masseter muscle</code> and <code>1204245006</code>.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32a70263d1381d9114a8a3a56e737935bd99a9b3.jpeg" data-download-href="/uploads/short-url/7e5GJX3OhmeTjXqZ43BE1sdd61R.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32a70263d1381d9114a8a3a56e737935bd99a9b3_2_690x323.jpeg" alt="image" data-base62-sha1="7e5GJX3OhmeTjXqZ43BE1sdd61R" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32a70263d1381d9114a8a3a56e737935bd99a9b3_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32a70263d1381d9114a8a3a56e737935bd99a9b3_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32a70263d1381d9114a8a3a56e737935bd99a9b3_2_1380x646.jpeg 2x" data-dominant-color="E0E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×899 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @diazandr3s (2024-04-25 13:34 UTC)

<p>This is super useful! Thanks, <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
<a class="mention" href="/u/philippepellerin">@philippepellerin</a>, it’d be great if you could do that</p>

---

## Post #11 by @philippepellerin (2024-04-25 13:48 UTC)

<p>Thanks for the tutorial. I will study it since it could be useful for the next batch if this one works fine. In the meantime, I checked my files, fortunately, since there were many typos and majuscules without meaning…I think that it is fine as it is. Let me know if everything is OK.<br>
Best regards. This is a link to download the files: <em>(download link retracted - contact the author of this post to get access)</em></p>

---

## Post #12 by @philippepellerin (2024-04-25 14:48 UTC)

<p>Hi Andras, thanks for your suggestion. How do I get the same terminology window as in your screenIgrab? What I get is this one<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c55bc917a997d6033e1e59fd193f95cb5e467fd1.jpeg" data-download-href="/uploads/short-url/s9UI60Y8Ictk7l1NmCBEngNS7aF.jpeg?dl=1" title="GraphiqueCollé-1.png" rel="noopener nofollow ugc"><img width="636" alt="GraphiqueCollé-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55bc917a997d6033e1e59fd193f95cb5e467fd1_2_636x500.jpeg" data-base62-sha1="s9UI60Y8Ictk7l1NmCBEngNS7aF" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55bc917a997d6033e1e59fd193f95cb5e467fd1_2_636x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55bc917a997d6033e1e59fd193f95cb5e467fd1_2_954x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55bc917a997d6033e1e59fd193f95cb5e467fd1_2_1272x1000.jpeg 2x" data-dominant-color="CBCBD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GraphiqueCollé-1.png</span><span class="informations">1306×1026 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
None of the segments in which I am interested are included in the terminology. I checked the SNOMED CT and found that all the names I used were correct according to the terminology. What should I do now?</p>

---

## Post #13 by @lassoan (2024-04-25 15:06 UTC)

<p>You can see the terminology category selector if you click the small left-arrow button on the left side. You won’t find the <code>masseter</code> in the default terminologies that are bundled with Slicer, so you’ll have to add a code for it. If you want to be able use new terms in Slicer, you can do the following:</p>
<ol>
<li>Create a small Segmentation Category/Type/Modifier terminology file, you can call it <code>SegmentationCategoryTypeModifier-Head.term.json</code> and set this content:</li>
</ol>
<pre data-code-wrap="json"><code class="lang-json">{
  "SegmentationCategoryTypeContextName": "Segmentation category and type - Head",
  "@schema": "https://raw.githubusercontent.com/qiicr/dcmqi/master/doc/segment-context-schema.json#",
  "SegmentationCodes": {
    "Category": [
      {
        "CodingSchemeDesignator": "SCT", "CodeValue": "123037004", "CodeMeaning": "Anatomical Structure",
        "showAnatomy": false,
        "Type": [
          { "CodingSchemeDesignator": "SCT", "CodeValue": "1204245006", "CodeMeaning": "Left masseter muscle", "recommendedDisplayRGBValue": [180, 80, 60] },
          { "CodingSchemeDesignator": "SCT", "CodeValue": "1204246007", "CodeMeaning": "Right masseter muscle", "recommendedDisplayRGBValue": [190, 80, 60] }
        ]
      }
    ]
  }
}
</code></pre>
<ol start="2">
<li>Drag-and-drop this file into the Slicer application window</li>
<li>Double-click the colored rectangle to open the terminology selector, click the left-arrow button to show the terminology context selector, and select your terminology: <code>Segmentation category and type - Head</code></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13398474f808181879da07bb94c95dbe51b3c399.png" data-download-href="/uploads/short-url/2K4iKvjUWvQ5mAFTNqgNwggCOTL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13398474f808181879da07bb94c95dbe51b3c399_2_690x257.png" alt="image" data-base62-sha1="2K4iKvjUWvQ5mAFTNqgNwggCOTL" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13398474f808181879da07bb94c95dbe51b3c399_2_690x257.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13398474f808181879da07bb94c95dbe51b3c399_2_1035x385.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13398474f808181879da07bb94c95dbe51b3c399_2_1380x514.png 2x" data-dominant-color="363A3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2445×913 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @philippepellerin (2024-04-25 16:00 UTC)

<p>Thanks, I will try, but it will be the first time in my life that I write a line of code…I attempted in 1978 to write some basic, but it went so badly that I never tried working again with a computer for 10 years!<br>
I am a final user without any basic skills in computational language</p>

---

## Post #15 by @lassoan (2024-04-25 16:05 UTC)

<p>It might seem complicated, but this is not software code, just a text file that lists the medical terminology codes that you want to see in the application. You just need to add one line for each structure (under the <code>Type</code> section).</p>
<p>Let us know if you run into any issues, we would like to learn what things are causing difficulties for users.</p>

---

## Post #16 by @philippepellerin (2024-04-26 14:31 UTC)

<p><span class="mention">@Andras</span> I tried it: I copied your text, pasted it in a new text edit, named it "SegmentationCategoryTypeModifier-Head.term.json”.<br>
I drop it on the application which recognised the file but thereafter got an error message here after a screen grab of the log<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1027f9505bd64279aaecf23e661e63d38750feb.png" data-download-href="/uploads/short-url/w6wMA4PeMO7ZlPMhhxbojis2BBN.png?dl=1" title="GraphiqueCollé-1.png" rel="noopener nofollow ugc"><img width="690" alt="GraphiqueCollé-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1027f9505bd64279aaecf23e661e63d38750feb_2_690x65.png" data-base62-sha1="w6wMA4PeMO7ZlPMhhxbojis2BBN" height="65" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1027f9505bd64279aaecf23e661e63d38750feb_2_690x65.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1027f9505bd64279aaecf23e661e63d38750feb_2_1035x97.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1027f9505bd64279aaecf23e661e63d38750feb_2_1380x130.png 2x" data-dominant-color="EBECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GraphiqueCollé-1.png</span><span class="informations">2162×206 35.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @diazandr3s (2024-04-26 18:32 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/philippepellerin">@philippepellerin</a>,</p>
<p>Here is my update after training the Auto3DSeg on this dataset (20 samples):</p>
<ul>
<li>A sort of preprocessing step before training the model has to be done to the annotations. Specifically, we need to make sure the label indices are consistent in the dataset. We can kind of automate this, but this has to be considered.</li>
<li>Images are of great quality and resolution. This means, more computing resources are needed to train and run inference within a reasonable amount of time.</li>
</ul>
<p>image_size_mm_median: <strong>[257.0, 233.0, 231.0]</strong><br>
image_size_mm_90: <strong>[354, 281, 250]</strong><br>
image_size: <strong>[704, 575, 471]</strong></p>
<p>Spacing: <strong>[0.50, 0.49, 0.53]</strong></p>
<ul>
<li>
<p>More annotated volumes are needed to get better performance. We could also consider adding more segments so we help the model by “telling” what are the True Negative regions (i.e. skull, brain temporal lobes, frontal lobe, etc)</p>
</li>
<li>
<p>Here is the video showing the inference: <a href="https://drive.google.com/file/d/11FGCoqgQHntl5LjyLQ_vJuu8dTsRhgWT/view?usp=sharing" rel="noopener nofollow ugc">masticatorymuscles_video.mp4 - Google Drive</a></p>
</li>
<li>
<p>We also need to get the standard DICOM label names as Andras suggested here: <a href="https://discourse.slicer.org/t/facial-muscle-segmentation-using-monai-auto3dseg/35734/9">Facial muscle segmentation using MONAI Auto3DSeg - #9 by lassoan</a></p>
</li>
</ul>

---

## Post #18 by @lassoan (2024-04-26 19:06 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="16" data-topic="35734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>I copied your text, pasted it in a new text edit, named it "SegmentationCategoryTypeModifier-Head.term.json”.<br>
I drop it on the application which recognised the file but thereafter got an error message here after a screen grab of the log</p>
</blockquote>
</aside>
<p>It works well for me. Probably you have not copied the complete content. Unfortunately, I could not see the actual error message in the screenshot (just the first line). If you have a look at the complete message then it may give you a hint of what was wrong.</p>
<p>You can download the file from <a href="https://github.com/lassoan/PublicTestingData/releases/download/data/SegmentationCategoryTypeModifier-Head.term.json">here</a>.</p>

---

## Post #19 by @philippepellerin (2024-04-27 08:47 UTC)

<p>Well it is not so bad, and I could use it. The result is good for the masseters and the pterygoid muscles. The part of the temporal muscle on the squamosal part of the temporal bone is poor, but it is the most difficult to segment.<br>
I made an attempt to load the SegmentationCategoryTypeModifier-Head.term.json file provided by laossan onto the slicer window. Although it was recognized and uploaded, it does not appear after restarting the slicer. I apologize for my lack of expertise in this area.<br>
-Again, I’m sorry, but processing more cases is very time-consuming. For the first 20 cases, it took me a day, full time, per case, and I do not have time left for more.<br>
A colleague engaged in a PhD on the topic came in touch. He may be willing to complete the job. I am writing to suggest that if so, he come in touch with you. I believe that one could run the MONAI Auto3DSeg with the Masticatory Muscles v1.0.0. That will have the benefit of naming all the segments identically and refining the segmentation manually.<br>
Last point: I am retired(75), and I am short on CT scans since they came from the library that I collected during my activity.<br>
-About the raised concern for anonymity, I find it paranoid.<br>
It has been a pleasure working with you, and I hope that soon, a v1.0.1 will happen, and more…</p>

---

## Post #20 by @muratmaga (2024-04-27 17:06 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="19" data-topic="35734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>About the raised concern for anonymity, I find it paranoid.</p>
</blockquote>
</aside>
<p>It is not simply a paranoia. It is a liability issue for slicer community. If the data is not properly consented for this use, there can be serious repercussion. And perhaps more importantly these are facial scans, making anonymity almost impossible…</p>

---

## Post #21 by @lassoan (2024-04-27 19:19 UTC)

<p>I agree that it is paranoia in the sense that the risk of data abuse is negligible. However, I would rather not spend time with arguing about this, as it would just distract us from working on things that matter.</p>
<p>So, I’ll remove the public download link above and if anyone would like to get access to the data then he can contact <a class="mention" href="/u/philippepellerin">@philippepellerin</a> .</p>

---

## Post #22 by @philippepellerin (2024-04-28 07:58 UTC)

<p>Sorry, when I sent the link for the data, I believed I was only in touch with Andres Diaz and did not know that it was going public, I am not used with the “social networks” may be I am too old for that stuff.<br>
If it comes to that in the future, I will shortcut the community to contact only one person at a time.<br>
Best</p>

---

## Post #23 by @philippepellerin (2024-04-28 08:00 UTC)

<p>At the same time I canceled the link for the data…</p>

---

## Post #24 by @Camila (2024-05-13 22:07 UTC)

<p>Hello, how are you Philippellerin? I’ve been following the conversation and would love to have access to the data you used to segment the masticatory muscles in 3D Slicer. Could you send me your email address so I can contact you? Thank you!</p>

---

## Post #25 by @philippepellerin (2024-05-14 06:50 UTC)

<p>Hi what is your purpose ?</p>

---

## Post #26 by @philippepellerin (2024-05-15 09:48 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="12" data-topic="35734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>SNOMED CT</p>
</blockquote>
</aside>
<p>For people interested in craniofacial segmentation, I add the extrinsic eye muscles and major salivary glands at the head terminology. You can load the jason.file here.<a href="https://www.dropbox.com/t/p9Xanatb4ohb6EUs" class="inline-onebox" rel="noopener nofollow ugc">Transfer - Dropbox</a></p>

---

## Post #27 by @iPsych (2024-11-15 04:09 UTC)

<p><a class="mention" href="/u/philippepellerin">@philippepellerin</a> Hello, I am also following-up your threads. Do you have any progress with major facial muscles segmentation like Orbicularis oculli?</p>

---

## Post #28 by @philippepellerin (2024-11-15 09:54 UTC)

<p>Hi, I sent some segmented oculomotor muscles to “whole body” and “Monai labe”,l but up to now, I do not have any feedback. I do not plan to segment the superficial muscles since the density gradient with the surroundings is too low. We can’t expect to reach a level of precision up to obtaining reliable measurement, and if your interest is in a coarse general shape of the muscles you get a nice one with 3D volume rendering with those settings: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb0fff4cdfd18bb550de06459d8f2a1ca9a74bd1.jpeg" data-download-href="/uploads/short-url/qGPyMksshr9QHvHaNjOkQEti5ep.jpeg?dl=1" title="Screenshot 2024-11-15 at 10.48.46.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb0fff4cdfd18bb550de06459d8f2a1ca9a74bd1_2_572x500.jpeg" data-base62-sha1="qGPyMksshr9QHvHaNjOkQEti5ep" width="572" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb0fff4cdfd18bb550de06459d8f2a1ca9a74bd1_2_572x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb0fff4cdfd18bb550de06459d8f2a1ca9a74bd1_2_858x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb0fff4cdfd18bb550de06459d8f2a1ca9a74bd1.jpeg 2x" data-dominant-color="BBA396"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-15 at 10.48.46.jpg</span><span class="informations">1100×960 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I do not consider segmenting the orbicularis oris, since its external part is composed of fibres originating from all the surrounding muscles, and there is no way to distinguish which belongs to whom from the CT scan data, it is almost impossible, even from the segmentation of the hight resolution pictures from the Korean visible project…</p>

---
