---
topic_id: 1951
title: "Machine Learning Project Questions About Integrating Slicer"
date: 2018-01-26
url: https://discourse.slicer.org/t/1951
---

# Machine Learning Project - Questions about integrating Slicer into workflow

**Topic ID**: 1951
**Date**: 2018-01-26
**URL**: https://discourse.slicer.org/t/machine-learning-project-questions-about-integrating-slicer-into-workflow/1951

---

## Post #1 by @djqazi (2018-01-26 21:16 UTC)

<p>Hi everyone,</p>
<p>I am a medical student from Connecticut with a (relatively) recent change of heart regarding medicine. That being said, for the past 7 months I have been studying math (linear algebra, prob/stats, calculus), programming (Python and Matlab), machine learning, natural language processing, and the nature of digital imaging. I am working on a project involving knee MRIs. To keep things short, our team is trying to automate the interpretation of anterior cruciate ligament injury (ACL) in MR images, as well as automatically generate a text report from the viusal interpretation much like a radiologist would. I am working on the imaging side of this project, but since I am new to this and working in semi-isolation, I have a lot of questions that have been accumulating over the past few months. I stumbled onto Slicer via a recommendation last month and was amazed by the software. I believe it is an essential component for this project.</p>
<p>First, I want to outline the project <em>very briefly</em>. Like I said, our data is MR images/volumes of the knee. We have secured an IRB to gain access to ~15,000 studies (retrospective). The data is formatted according to DICOM standards. We plan on seperating the studies into “ACL torn” and “ACL intact”. Then using supervised methods (we are still looking into this but will be some variation of CNN/RNN), we plan on training an algorithm to classify the MR volumes accordingly. Along the way, I personally would like to come up with a way to automatically segment the ACL as well, a difficult task for those who know the MR images of the knee joint.</p>
<p>Here are my questions:</p>
<ol>
<li>
<p>Data format: As a team we have been discussing the appropriate data format. It is between NIFTI and DICOM. I have spent some time reading up on DICOM, including some of the papers published by indiviudals involved with Slicer development (also I just started reading a book by O. Pianykh), and it seems to me that DICOM should be the choice. Assuming all of the studies truly follow DICOM standards, is there any advantage in using NIFTI over DICOM with Slicer?</p>
</li>
<li>
<p>MR images: Many of you probably know that MRI is a complicated imaging modality that allows you to choose several parameters (TR, TE, etc) that determine the image contrast (PD, T1, T2…), spatial resolution, etc. Thus, for a given study, you obtain several series. Each series is a distinct volume of the same object, however the image histograms are very different, and the dimensions of the volumes can be different. From my understanding, one thing that is important when using supervised machine learning methods is that the input vector (each voxel in the volume is feature) should be the same size for every training sample. Consequently, that should mean that <em>any and all volumes</em> we want to use for training have to be the same size and shape. I have a sample of 30 studies, with ~7-8 series in each study (PD FS in all 3 planes, T2 FS in coronal and sagittal, T1 in sagittal, STIR in coronal and sagittal). I know this is not a question directly related to Slicer, but if anybody could advise whether it is a good idea to use all of the series from each patient/study, or simply focus on one or two (see next question for more detail).</p>
</li>
</ol>
<p>3.) Resampling and Registration: Given the nature of the differences within and among the different knees i.e. intra-patient and inter-patient, I think I will need to resample and register this sample dataset to a common volume. I did a bunch of reading and found the Elastix module, read (to the best of my ability) the manual and it seemed pretty good because it resamples for you! However…after some thought, I realized this may not work so well. I think there is too much variation in contrast and spatial resolution to produce anything worthwhile. Perhaps I need to pick a single series e.g. PD FS? In any case, I will probably end up using Elastix. Could someone explain or point me to how I can use python to script batch registration and. The sample data I have is organized into a directory tree on my drive, so I will probably need to loop through folders…or can I simply load the DICOM data into Slicer and loop that way? I vaguely (very vaguely) understand that Slicer represents things as “nodes” but not very clear about this.</p>
<ul>
<li>P.S. I was also wondering about the utility of super-resolution reconstruction i.e. since I have PD FS in all 3 planes I was wondering if there was any Slicer modules that supported this type of reconstruction. This would really benefit segmentation, image recognition, etc.</li>
</ul>
<p>4.) Segmentation: All supervised methods rely on labeled data and so I know that we will have probably have to manually segment the ACL on many, many volumes. I found the knee atlas for surgical planning made by the folks in Boston, really amazing stuff. I’m trying to figure out the best workflow here as well. After the images are registered, is the Segment Editor the best tool for this task? Also, is it feasible to segment say, 100 ACLs, then use noise models (perhaps that’s not the right terminology), to generate novel volumes for use in our neural network. I know several authors have used this technique e.g. prostate to avoid having to label thousands of images. I am just not sure about how to go about doing this with Slicer (if it is possible).</p>
<p>I have more questions, but this is already too long of a post. I apologize for rambling. Also, I wasn’t sure if this was the right forum for this post, but I have been struggling trying to understand this stuff on my own and the community here seems very supportive.Thank you for any and all help!!!</p>
<p>Sincerely,</p>
<p>Dan</p>

---

## Post #2 by @ihnorton (2018-01-27 12:55 UTC)

<p>It sounds like an interesting project; hopefully others will chime in after the weekend, but to touch on one point here:</p>
<aside class="quote no-group quote-modified" data-username="djqazi" data-post="1" data-topic="1951">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/74df32/48.png" class="avatar"> djqazi:</div>
<blockquote>
<p>Data format: As a team we have been discussing the appropriate data format. It is between NIFTI and DICOM.  […] is there any advantage in using NIFTI over DICOM with Slicer?</p>
</blockquote>
</aside>
<p>If you plan to have a Slicer-centric workflow, your best bet is to work in Slicer’s native “NRRD” format. There is very little advantage – and some disadvantage – to using Nifti with Slicer instead of NRRD unless you have to work with other software that only supports Nifti (but Elastix will work fine with NRRD, for example). Basically using Nifti will add another conversion step in various places, and there are occasional interpretation mismatches with other software.</p>
<p>Keep in mind that most Nifti-related software is focused on neuroimaging (of course there is some applicability cross-over for tools like registration).</p>
<p>As for DICOM: Slicer has robust support for interacting with DICOM at the beginning (import) and end (export) of studies, but I don’t think it is really recommended to try a DICOM-native workflow yet. Various tools using the CLI interface won’t work without without conversion to NRRD anyway (as far as I know – maybe this has changed or been automated recently).</p>

---

## Post #3 by @pieper (2018-01-27 18:15 UTC)

<p>I agree with Isaiah - your project sounds very interesting.  It sounds like you are on the right track on many topics and I think you understand that there’s a lot of work involved in making these things work but there are a lot of tools for you to try out, and this forum will be a good place to post specific questions (or examples of where you have gotten things to work).</p>
<p>A couple of things that would really help you make use of this community would be open data and open development.  If you are able, for example, to post deidentified datasets and start a public github repository with your code so that people can try things themselves and give you very specific advice and feedback.  Of course you’ll need to careful to get permission from your institution and colleagues for anything you share publicly.</p>
<p>In terms of getting stared, you could have a look at the new <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">CaseIterator</a> as one tool that could help you.</p>
<p>Regarding the data formats, if you plan to work with 15,000 studies you will need to be super careful organizing things and automate as much as you can.</p>

---

## Post #4 by @lassoan (2018-01-27 19:25 UTC)

<p>Very interesting project, indeed.</p>
<p>You’ve raised many good questions, which cannot be efficiently discussed in a single forum topic. So, I would suggest to post each question as separate topic. For example, you can start a topic on data format and organization.</p>

---

## Post #5 by @JoostJM (2018-01-29 09:16 UTC)

<p>Very interesting project!</p>
<p>ad 1) I agree with the others that using the NRRD format would be easiest, especially if you want to use some form of 3D network (DICOM is mainly 2D). As you have a quite large dataset, a batch converter from DICOM to NRRD (or NIFTII) might help you a lot. Check out <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/" rel="nofollow noopener">this project</a> (by <a class="mention" href="/u/fedorov">@fedorov</a>) on DICOM volume reconstruction tools. Alternatively, I built a python script which uses PyDicom and SimpleITK to read a bunch of DICOM series and convert them to NRRD. It only works for 3D, but it does also check if slices are equidistant (sanity check). <a href="https://github.com/JoostJM/nrrdify" rel="nofollow noopener">This</a> is the repository.</p>
<p>ad 2)/3) Regardless of resampling etc., you can use multiple sequences as input for your network, but not interchangeably. Therefore, you should only use sequences you have for all cases. We published <a href="https://www.nature.com/articles/s41598-017-05728-9" rel="nofollow noopener">this</a> paper using MR with multiple sequences to train a network to segment rectal tumors, but a similar approach can be used to segment your knees and also answer your classification question.</p>
<p>Finally, if your interested in deep learning etc. the stanford notes are always a good place to start. They can be found <a href="http://cs231n.github.io/" rel="nofollow noopener">here</a>.</p>

---

## Post #6 by @djqazi (2018-01-31 19:09 UTC)

<p>Thanks for all of the advice, I really appreciate it! A few things:</p>
<p>1.) It seems like NRRD is the way to go at this time, so I converted (simply saved) my imported DICOM files as NRRD via Slicer. However I have some questions about this (see below).</p>
<p>2.) It took a little working, but I got permission to post my sample of 30 patients on Git. The DICOM data is already anonymized, but my university wants some additional scrubbing before I post the data. I would imagine the conversion to NRRD addresses this (but I’m not sure, forgive my ignorance, I am very new to computer science). But I’d like to be able to post the DICOM data as well because one of the imortant issues is <em>workflow</em>. I will take lassoan’s advice and compartmentalize my queries. Thus, I will create a new thread about data where I will detail my specifics.</p>

---

## Post #7 by @djqazi (2018-01-31 19:10 UTC)

<p>Thanks for the advice! I took a look at CaseIterator and have some questions. I will post in the new thread I am creating specifically about data.</p>

---

## Post #8 by @djqazi (2018-01-31 19:16 UTC)

<p>Wow, thanks for the tools, references and guidance! Will take a look at this stuff and see where it leads.</p>

---

## Post #9 by @mebner (2018-02-01 12:11 UTC)

<p>Hi Daniel,</p>
<p>It definitely sounds like an interesting project. Regarding Super-Resolution, it might be worth having a look at NiftyMIC (<a href="https://github.com/gift-surg/NiftyMIC" rel="nofollow noopener">https://github.com/gift-surg/NiftyMIC</a>) which I have been developing within my PhD work on fetal MRI reconstruction. It is mainly developed for T2 single-shot sequences, but I have tried it on some other contrasts as well obtaining decent results there too (not on PD yet though). I appreciate that this is not Slicer related but, perhaps, this might be of help to you and I would be happy to support you with this.</p>
<p>Best wishes,<br>
Michael</p>

---
