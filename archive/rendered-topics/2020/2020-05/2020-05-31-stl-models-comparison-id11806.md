---
topic_id: 11806
title: "Stl Models Comparison"
date: 2020-05-31
url: https://discourse.slicer.org/t/11806
---

# STL models comparison

**Topic ID**: 11806
**Date**: 2020-05-31
**URL**: https://discourse.slicer.org/t/stl-models-comparison/11806

---

## Post #1 by @danila (2020-05-31 15:03 UTC)

<p>Operating system: macOS Catalina v10.15<br>
Slicer version: 4.10.2<br>
Expected behavior: How to compare and analyse two STL models of the same patients at T1 and T2.<br>
Actual behavior: I have done a CBCT superimposition using a voxel based registration.</p>

---

## Post #2 by @cpinter (2020-06-01 09:29 UTC)

<p>First of all, I recommend using a recent preview version, because 4.10.2 is very old, and we’re approaching 5.0 so the previews are quite stable, and contain many improvements since 4.10.2.</p>
<p>I think to compare models, especially if you have the corresponding volumetric images (the T1 and T2 MRIs), the best is if you convert the models to segmentations, and use the Segment Comparison module. This is a generic answer to a generic question, so if you describe your needs in more detail, then we can help you better.</p>
<p>A few things that would help a lot:</p>
<ul>
<li>Where do these STLs coming from? If they are segmentations, then you could do the segmentations in Slicer where we have great tools now for that, so you don’t need to convert-export-import-convert (resulting in data loss)</li>
<li>Are the data spatially registered? Do you need to register them after importing in Slicer?</li>
</ul>

---

## Post #3 by @danila (2020-06-01 10:15 UTC)

<p>Thank you for your answer.</p>
<ol>
<li>I converted two cone beam CTs from DICOM files to GIPL with ITK SNAP</li>
<li>I performed segmentation of the anterior skull base with ITK SNAP of scans T1 and T2</li>
<li>I loaded on 3D slicer: T1 scan, t2 scan, segmentation of the skull base of T1, segmentation of the skull base on T2. I then used the CMF Registration module and chose the Voxel (non growing registration) function. I set the options and applied by obtaining an Output Registered Seg and an Output Registered Scan.</li>
</ol>
<p>At this point I would like to quantify through a colormap the changes obtained at the level of the maxillary bones. Do I have to proceed by segmenting my Output Registered Scan and then converting the segmentations into 3D surface models?</p>
<p>Also how can I spatially record stl files after importing them into slicer? Is there a tutorial?</p>
<p>Kind regards</p>
<blockquote>
<p>First of all, I recommend using a recent preview version, because 4.10.2 is very old, and we’re approaching 5.0 so the previews are quite stable, and contain many improvements since 4.10.2.</p>
<p>I think to compare models, especially if you have the corresponding volumetric images (the T1 and T2 MRIs), the best is if you convert the models to segmentations, and use the Segment Comparison module. This is a generic answer to a generic question, so if you describe your needs in more detail, then we can help you better.</p>
<p>A few things that would help a lot:</p>
<ul>
<li>Where do these STLs coming from? If they are segmentations, then you could do the segmentations in Slicer where we have great tools now for that, so you don’t need to convert-export-import-convert (resulting in data loss)</li>
<li>Are the data spatially registered? Do you need to register them after importing in Slicer?</li>
</ul>
<p>–<br>
<em>Previous Replies</em><br>
Operating system: macOS Catalina v10.15<br>
Slicer version: 4.10.2<br>
Expected behavior: How to compare and analyse two STL models of the same patients at T1 and T2.<br>
Actual behavior: I have done a CBCT superimposition using a voxel based registration.</p>
<hr>
<p><a href="https://discourse.slicer.org/t/stl-models-comparison/11806/2">Visit Topic</a> or reply to this email to respond.<br>
To stop receiving emails about this topic, category, or all discussions, <a href="https://discourse.slicer.org/email/unsubscribe/bfe6c64fbbd640aad0c0343588de34de86ff74c83768d146b559ef1e4337cbeb">click here to unsubscribe</a>.</p>
</blockquote>
<p><em><strong>PRIVACY:</strong> In ottemperanza con il nuovo Regolamento Europeo GDPR n. 679/2016, le informazioni</em><br>
<em>contenute in questo messaggio sono riservate. Il loro utilizzo è consentito esclusivamente al</em><br>
<em>destinatario del messaggio, per le finalità indicate nel messaggio stesso. Qualora Lei non fosse la</em><br>
<em>persona a cui il presente messaggio è destinato, La invitiamo ad eliminarlo dal Suo Sistema ed a</em><br>
<em>distruggere le varie copie o stampe, dandocene gentilmente immediata comunicazione anche</em><br>
<em>inviando un messaggio di ritorno all’indirizzo e-mail del mittente. Ogni utilizzo improprio è</em><br>
<em>contrario ai principi del nuovo Regolamento Europeo GDPR n. 679/2016.</em><br>
<em>Si avvisa che il presente messaggio ed eventuali risposte potrebbero essere letti da soggetti</em><br>
<em>appartenenti all’Amministrazione differente dal mittente.</em><br>
<em>L’Università degli Studi Magna Graecia di Catanzaro opera in conformità al nuovo Regolamento</em><br>
<em>Europeo GDPR n. 679/2016. Per qualsiasi informazione a riguardo si prega di contattare l’indirizzo</em><br>
<em>e-mail: <a href="mailto:dirgen@unicz.it">dirgen@unicz.it</a></em></p>

---

## Post #4 by @cpinter (2020-06-01 12:34 UTC)

<p>Thanks for the detailed explanation!</p>
<p>Your workflow seems to be more complicated than necessary, and in the process data may be lost. Conversion of DICOM to non-DICOM data incurs loss in data, most importantly (based on what I found about the format you use) the spatial information that is key. Also, the Segment Editor module offers more advanced tools and can provide higher accuracy than ITK-SNAP (we have put in immense efforts into this in the past few years), and can be used as an integrated workflow as it’s in Slicer. What I’d recommend instead:</p>
<ol>
<li>Load your DICOM data in Slicer</li>
<li>Do the registration first. I recommend the SlicerElastix extension</li>
<li>Segment both images using Segment Editor</li>
<li>Evaluate the segmentations</li>
</ol>
<p>There is no need to handle any STL file, nor do conversions. The segmentations infrastructure in Slicer will take care of this.<br>
I didn’t understand some of your questions, so let us know when you are at the last step and tell us how you want to do the comparison.</p>

---

## Post #6 by @danila (2020-06-02 09:11 UTC)

<p>I was probably not clear on explaining my problems.</p>
<p>My goal is to measure the linear and volumetric change of a jaw before and after an orthognathic surgery (therefore comparing the pre and post CBCT).</p>
<p>Following the tutorial I found on the DCBIA team website, I made the segmentation of the anterior skull base at t0 and t1 with the ITK-SNAP software.</p>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=97051730c2&amp;attid=0.1&amp;permmsgid=msg-a:r-3726477025870366709&amp;th=17273d9276a2d85e&amp;view=fimg&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ8mTLURwpSBWdiuMxFDLjrB1l2vBSOTfASeLkykjL3NjDgTNq6QI_OeoYM6_4h2HWfvWcJBFF1gdaNug2lUxhChC3y1P15QqJI9GBQiXW7I5GIkg_QFMoRN23U&amp;disp=emb&amp;realattid=ii_kaxkc3wo0" alt="Screenshot 2020-06-01 at 10.17.19.png" width="510" height="319"></p>
<p>Then I do the landmarks approximation about the two scans with Slicer and subsequently the recording performed on voxel relating to the skull base (using: basaline scan - T1; basaline segmentation - segmentation of anterior skull base at T1; follow-up scan - T2landmarks; follow-up segmentation - segmentation of skull base at T2landmarks).</p>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=97051730c2&amp;attid=0.2&amp;permmsgid=msg-a:r-3726477025870366709&amp;th=17273d9276a2d85e&amp;view=fimg&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ8XF6a3BGNi5j40A-FtMHtOS6yh6bj6qc4MqmoxoAKP0OFUGABdMAyRYRWMEsTWEGU1LNMkPOnogxAumc_eiDgIi-H_6eoVn8UWULBWaxKKftniFedYYHPYzOk&amp;disp=emb&amp;realattid=ii_kaxkgl061" alt="Screenshot 2020-06-01 at 15.17.41.png" width="510" height="319"></p>
<p>After the registration I have segmented the first mandible on the t1 scan and the second mandible on the t2 scan obtained from the voxel recording.  Then I transformed the segmentations of the two mandible into 3D surface models.  I uploaded the two models on Slicer and I apply the module “model to model distance”.</p>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=97051730c2&amp;attid=0.3&amp;permmsgid=msg-a:r-3726477025870366709&amp;th=17273d9276a2d85e&amp;view=fimg&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ-COlouSwMjG-gfoj_bJ1IP9zrzhJmtc5XoOylZU_Es4qrU1kA5pFrI8qJ9L8uBSs0vhAojUusWDpJFbLDODZsKDlUHpkYqlfGdAyFyHaC0EVx8vwrefQLvCn0&amp;disp=emb&amp;realattid=ii_kaxkkufu2" alt="Screenshot 2020-06-01 at 15.54.00.png" width="510" height="319"></p>
<p>I use the module “Shape Analysis Viewer” to obtain a color map.</p>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=97051730c2&amp;attid=0.4&amp;permmsgid=msg-a:r-3726477025870366709&amp;th=17273d9276a2d85e&amp;view=fimg&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ9Nw4ZiRLYVjWcLBdmw899g-puwpaPwJ8-7mE8OOIjA9W-nFMyK1GzqW8oL44J9Mk65wfY8cQVUHByHXwS5QRMudGcIVGrIuZlHyx8L8C8XNFJaF1k5s81R7Fg&amp;disp=emb&amp;realattid=ii_kaxkmhef3" alt="Screenshot.png" width="510" height="283"></p>
<p>Now I would like to take a statistic analysis about this, but I don’t know how I can do. Can you help me?</p>
<p>The flow that I have use is correct?</p>

---

## Post #7 by @cpinter (2020-06-02 10:01 UTC)

<p>I cannot see any images, only their empty frames. Is it only me?</p>

---

## Post #8 by @pieper (2020-06-02 11:19 UTC)

<p>Right - I see just frames too.</p>

---

## Post #9 by @danila (2020-06-02 12:15 UTC)

<p>Sorry for the mistake, below I written the whole tesxt with the imagines again.</p>
<p>My goal is to measure the linear and volumetric change of a jaw before and after an orthognathic surgery (therefore comparing the pre and post CBCT).</p>
<p>Following the tutorial I found on the DCBIA team website, I made the segmentation of the anterior skull base at t0 and t1 with the ITK-SNAP software.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aad3db73a45cd7102c0a680cc2a28f92a356af2.png" data-download-href="/uploads/short-url/8n4Rm4L7IFrSOsU1Qh4u5X6BfHQ.png?dl=1" title="immagine 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_690x431.png" alt="immagine 1" data-base62-sha1="8n4Rm4L7IFrSOsU1Qh4u5X6BfHQ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_1380x862.png 2x" data-dominant-color="2D382D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 1</span><span class="informations">2880×1800 577 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I do the landmarks approximation about the two scans with Slicer and subsequently the recording performed on voxel relating to the skull base (using: basaline scan - T1; basaline segmentation - segmentation of anterior skull base at T1; follow-up scan - T2landmarks; follow-up segmentation - segmentation of skull base at T2landmarks).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f.jpeg" data-download-href="/uploads/short-url/wWvSfhqMX0e4WAmcHe59ouhgZGL.jpeg?dl=1" title="immagine 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_690x431.jpeg" alt="immagine 2" data-base62-sha1="wWvSfhqMX0e4WAmcHe59ouhgZGL" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_1380x862.jpeg 2x" data-dominant-color="9A9AA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 2</span><span class="informations">2880×1800 733 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After the registration I have segmented the first mandible on the t1 scan and the second mandible on the t2 scan obtained from the voxel recording.  Then I transformed the segmentations of the two mandible into 3D surface models.  I uploaded the two models on Slicer and I apply the module “model to model distance”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e208f1dc2dd32060dd82b6f403f47ca380431cc.png" data-download-href="/uploads/short-url/dqGDER1gMdaTyHRcCtOyoKy9l9O.png?dl=1" title="immagine 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_690x431.png" alt="immagine 4" data-base62-sha1="dqGDER1gMdaTyHRcCtOyoKy9l9O" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_1380x862.png 2x" data-dominant-color="B6BAD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 4</span><span class="informations">2880×1800 784 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I use the module “Shape Analysis Viewer” to obtain a color map.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de.png" data-download-href="/uploads/short-url/1l9LFRA5Msnincwqen12E3gjC9g.png?dl=1" title="immagine 5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_690x382.png" alt="immagine 5" data-base62-sha1="1l9LFRA5Msnincwqen12E3gjC9g" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_1380x764.png 2x" data-dominant-color="6B6286"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 5</span><span class="informations">2880×1598 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I would like to take a statistic analysis about this, but I don’t know how I can do. Can you help me?</p>
<p>The flow that I have use is correct?</p>
<p>Thanks again for the support. Hoping that now you can view the images.</p>

---

## Post #10 by @cpinter (2020-06-02 12:53 UTC)

<p>Thanks! At this point this is a question on how to get a histogram for a shape analysis, but I don’t have experience with that specific extension.</p>
<p>My recommendation, however, about using Slicer for segmentation still stands, because your fragmented workflow leaves more than necessary room for inaccuracies.</p>

---

## Post #11 by @danila (2020-06-02 14:22 UTC)

<p>Thanks for the information.<br>
I have another questions, what kind of informations Can I obtain from the color map and how can I get them?</p>

---

## Post #12 by @muratmaga (2020-06-02 14:57 UTC)

<p>In broad terms, the workflow appears correct. But the devil is always in the detail. I also second that trying to do everything Slicer.</p>
<p>You can’t run statistics on a single specimen with two time points. If your goal is to show that after the surgery mandible is more ‘normal’ looking, you at least need a sample of normal mandibles to calculate that statistic.</p>
<p>With a single sample and two time points, the simplest is to highlight the differences as color maps, and interpret them in light of the surgery conducted.</p>

---

## Post #13 by @danila (2020-06-02 16:26 UTC)

<p>Thanks for the answer.<br>
I have a single sample and two time points available, so I would like to obtain distance measurements in millimeter terms through the color map. How can I get them? could you explain to me how to set the correct range?</p>
<p>Thanks a lot</p>

---

## Post #14 by @smrolfe (2020-06-02 16:40 UTC)

<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" rel="nofollow noopener">ModelToModelDistance</a> extension will compute a point by point Hausdorff distance between two models. The distance array can be visualized as a heat map on the output model.</p>

---

## Post #15 by @danila (2020-06-02 17:58 UTC)

<p>I used modeltomodel, but what is the error that i do?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="mjA7bDvBU3s" data-video-title="Modeltomodel" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=mjA7bDvBU3s" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/mjA7bDvBU3s/hqdefault.jpg" title="Modeltomodel" width="" height="">
  </a>
</div>


---
