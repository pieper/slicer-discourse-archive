---
topic_id: 5155
title: "Request For Suggestions For Image Informatics Tools"
date: 2018-12-20
url: https://discourse.slicer.org/t/5155
---

# Request for suggestions for image informatics tools

**Topic ID**: 5155
**Date**: 2018-12-20
**URL**: https://discourse.slicer.org/t/request-for-suggestions-for-image-informatics-tools/5155

---

## Post #1 by @muratmaga (2018-12-20 17:35 UTC)

<p>Hi,</p>
<p>We have various datasets (both clinical and non-clinical) we would like to consolidate into some sort of a image informatics solution that will help us keep them better organized and annotated. I am looking into Xnat as an option but would like know if there are other solutions better integrated with Slicer. Being able to retrieve data from repository into Slicer is a plus.</p>
<p>From clinical data, we might have anonymized DICOM series from a ‘normal’ patient as a nifti/nrrd, a cleaned up version where only cranial bones are retained, segmentations (e.g., mandible and cranium as separate structures), and fiducials and so forth.</p>
<p>There are different projects with different datasets, but in similar vain…</p>
<p>It will be great to hear your suggestions…</p>

---

## Post #2 by @pieper (2018-12-22 00:17 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> -</p>
<p>I guess you saw the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/XNATSlicer" rel="nofollow noopener">XNATSlicer extension</a> which does a lot of the things on your wishlist.  Last I saw it might need some updates for the latest versions of Slicer and I don’t know if it has been used widely (might have limitations/bugs).</p>
<p>Storing the derived data as DICOM (instead of nifti/nrrd) could be a good option.  This has the advantage of keeping all the relationships explicit in the data files instead of storing them in a separate detached database (e.g. the definitive source of information about what images were annotated by whom and when is in the header).  Then you can use different database options to organize the data as needed, like a dicomweb server with an extra database like in <a href="https://github.com/crowds-cure/cancer" rel="nofollow noopener">Crowds Cure Cancer</a>.  Admittedly the Slicer infrastructure for all of this is still a work-in-progress, but the pattern is well defined.</p>

---

## Post #3 by @lassoan (2018-12-22 03:05 UTC)

<p><strong>DICOM file format</strong></p>
<p>It is highly structured and standardized, so it is great for data archival or sharing. However, we usually choose more generic representations (tables in csv files, images as nrrd files, etc.) as internal representation, as they are more flexible, efficient, simpler, and compatible with much more software. <a class="mention" href="/u/fedorov">@fedorov</a> has made nice progress in making DICOM directly usable for certain data analysis tasks, maybe he can add some more comments and give pointers to examples.</p>
<p><strong>XNAT</strong></p>
<p>It is still actively maintained, mostly keeps up with state-of-the art technologies (web APIs, docker, etc) and several groups use it. It is customizable by plugins, but as I’ve heard that it is not easy to create them (this seems to be confirmed by the low number of plugins - less than 30, although the project has been around for more than a decade).</p>
<p><strong>Girder</strong></p>
<p><a href="https://girder.readthedocs.io/en/stable/" rel="nofollow noopener">Girder</a> is Kitware’s fresh take on research data management and analysis (based on their experience with their previous-generation MIDAS data management system). Compared to XNAT, Girder is built on more modern basis and there seem to many more developers on the project. It has nice integration with data analysis and visualization features (<a href="https://resonant.kitware.com/" rel="nofollow noopener">Resonant</a> platform).</p>
<p><strong>Our usual workflow</strong></p>
<p>In the past, we’ve tried to set up XNAT (when it was not yet dockerized) but we did not succeed. We have tried using CouchDB, which worked well for storing small data sets (descriptive data), but was not usable (synchronization was very unreliable) for large files, such as 3D images. We have now a Girder instance set up, but so far we only used it for simply sharing files with external collaborators.</p>
<p>What we usually do is storing Slicer scenes (mrb files) in folders on a shared drive. Mapping from internal IDs to patient information is in a password protected spreadsheet or REDCap database. The saved scene also contains additional annotation (landmarks, manual segmentation, etc.) and may contain computation/analysis results.</p>
<p>For batch processing and analysis we put the selected group of mrb files in a folder and iterate through them using a Python script. In some projects, the data processing is split into a generic data extraction step (done only once, it generates summary csv files, series of aligned/normalized images, meshes, etc.), and a processing/analysis step (which is very specific to the data set and research question).</p>
<p>Nowadays we mostly run Python scripts using <a href="https://github.com/Slicer/SlicerJupyter" rel="nofollow noopener">Jupyter notebooks</a>, as they are easier to run/modify/verify than using a plain command-line interface. Also, notebooks work the same way regardless of operating system and they can also run on high-performance computing clusters (using <a href="https://github.com/jupyterhub/jupyterhub" rel="nofollow noopener">JupyterHub</a>).</p>

---

## Post #4 by @muratmaga (2018-12-22 06:28 UTC)

<p>Thank you both <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>I wish there is some sort of format that will have the metadata capability of DICOM, and the flexibility and ease of use of MRB (so everything travels together).</p>

---

## Post #5 by @pieper (2018-12-22 20:22 UTC)

<p>DICOM and MRB are really two ends of the spectrum with respect to standardization vs customization.  We can feel free to innovate in MRB but it’s very specific to Slicer while DICOM has compromises but at least the hope of data exchange.  In the end both have their uses.</p>

---

## Post #6 by @muratmaga (2018-12-22 22:44 UTC)

<p>It is a shame that medical imaging doesn’t use a container like hdf5 where dicom tags would contain metadata and you can keep adding image volumes and everything derived from it.</p>

---

## Post #7 by @lassoan (2018-12-22 23:28 UTC)

<p>DICOM specifies a much more sophisticated container than HDF5. The DICOM file container can store any information.</p>
<p>One issue is that the container is probably more complex than it would be necessary. There are many data types that can be stored in many different ways.</p>
<p>Also, DICOM is much more than a file format. <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html" rel="nofollow noopener">Data structure and encoding</a> is just one chapter of the standard. There are <a href="https://www.dicomstandard.org/current/" rel="nofollow noopener">20 other chapters</a> describing various other aspects of data storage. For example, Part 3 contains high-level data structures, defined above the file container level - in more than 1600 pages.</p>
<p>If you used DICOM just as a container, as HDF5, and stores all data in private fields (that you have specified for yourself) then you could make it as simple and efficient as you want. Many imaging device developers follow this approach. However, then you would lose most benefits of DICOM.</p>

---

## Post #8 by @pieper (2018-12-22 23:34 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="5155" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It is a shame that medical imaging doesn’t use a container like hdf5 where dicom tags would contain metadata and you can keep adding image volumes and everything derived from it.</p>
</blockquote>
</aside>
<p>That’s effectively what a DICOM Study is: a place to collect logically related data - you can add additional series and instances that reference or derive from other data.  You can also link across studies.  It’s just mediated by a server, aka PACS, (either over DIMSE or DICOMweb), which typically has a database indexed over the most common query keys.</p>
<p>It’s also possible to put all the DICOM instance data you want into a directory indexed by a DICOMDIR file.  The directory could be encoded as an hdf5 file, although I don’t think I’ve ever seen that done.</p>
<p>And it’s not just that DICOM structures are flexible, it’s that many of the most important fields have well defined representations.  Like human names that can be in different language conventions and quantitive measurements with standardized ways of describing what they measure and what units they are expressed in.  If you don’t use DICOM then you need to re-invent all these things.</p>

---

## Post #9 by @muratmaga (2018-12-23 05:22 UTC)

<p>But hdf would have offered containing everything in a single file, similar to the MRB.</p>
<p>We do have to invent some tags for non-clinical projects (eg., genus, species, strains, genetic variants, collection/accession IDs, specimen numbers, etc…, things DICOM format never probably needed). Ideally, I would like to have them travel with the image data itself, not just sit in a remote server. Currently we seem to stuck in a place where all this information needs to be either part of the filename (when using a research format like NRRD), which makes them unwieldy (e.g., <code>BKS.Cg-Dock7m +/+ Leprdb/J</code>), not to mention error-prone. Or if we go with DICOM (and implement private fields as Andras mentioned), we have to deal with thousands of files per dataset, which makes distribution a bit more challenging.</p>
<p>Or Is it possible to store image volumes in dicom as a single file (like nifti or nrrd) and still maintain compatibility?</p>

---

## Post #10 by @lassoan (2018-12-23 06:01 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="5155">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is it possible to store image volumes in dicom as a single file</p>
</blockquote>
</aside>
<p>Yes. Ability to store an entire image series in a single file was added to DICOM more than a decade ago (enhanced multi-frame IODs). Unfortunately, device manufacturers mostly stayed with the legacy single-frame-per-file format and many software (including Slicer) are less thoroughly tested with those rare multi-frame files.</p>

---

## Post #11 by @pieper (2018-12-23 20:11 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="5155">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>non-clinical projects (eg., genus, species, strains, genetic variants, collection/accession IDs, specimen numbers, etc…, things DICOM format never probably needed).</p>
</blockquote>
</aside>
<p>Actually DICOM has support for a lot of this kind of stuff, some driven by veterinary applications and others by preclinical research.  Could you take look at what is already supported and make a list of what else you would need?</p>
<p><a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.html" class="onebox" target="_blank" rel="noopener">http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.html</a></p>
<p>We can always use non-standard extensions if needed, or we could suggest changes to the standard that would handle more use cases.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="5155">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Ideally, I would like to have them travel with the image data itself, not just sit in a remote server.</p>
</blockquote>
</aside>
<p>Right - that’s what the DICOM approach provides.  Everything is explicit in the data file and a remote server or database is just a convenience for storage or efficient access.</p>
<p>MRB files are very handy.  They are just zip files of nrrd and mrml with a different extension.  We could always make a similar convention for DICOM if that would help us group our DICOM data.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="5155">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Or Is it possible to store image volumes in dicom as a single file (like nifti or nrrd) and still maintain compatibility?</p>
</blockquote>
</aside>
<p>Just as a note, .nhrd files can <a href="http://teem.sourceforge.net/nrrd/format.html#detached">point to other data containers files</a> so even if you kept the ‘canonical’ data in single or multiframe DICOM you could also be compatible with nrrd for interoperability.</p>

---

## Post #12 by @muratmaga (2018-12-23 21:14 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
I forgot about veterinary use cases! Yes, those do contain quite a bit of the stuff we would need  or things that might be reworked. I will take a more careful look.</p>
<p>I like NHRD format. Problem is, I don’t know how to force to keep data in that format. For example, we make a NHDR that points out to a dicom for a metadata, but then when the user saves it is a nrrd from slicer, what happens? Perhaps you can argue that it is in the end users’ responsibility to be careful, but it is easy to make these kinds of mistakes.</p>
<p>Anyways, these discussions had been very useful for me and I do appreciate you guys taking the time for input.</p>

---

## Post #13 by @fedorov (2018-12-23 22:12 UTC)

<p>I didn’t respond since I didn’t have enough time, and there is no easy answer. I think the short answer is that there is no easy solution, and it all depends what exactly you need. I think XNAT is the best “ready to go” platform, if you want to limit development or just explore the existing capabilities. I do not know though how well it is integrated with Slicer. Long time ago I saw some demos, but I never tried to use XNAT-Slicer integration for anything beyond a demo. Also, the last time I heard from the XNAT team about the Slicer plugin, in response to a report that it does not work <a href="https://groups.google.com/d/msg/xnat_discussion/iPDAXWZ0jms/XCGGOF2pCQAJ" rel="nofollow noopener">they said (back in June)</a>: “The XNAT team doesn’t currently have anyone assigned for development on the XNATSlicer plugin. We intend to continue supporting the extension, but when we may have an update depends heavily on when we can find someone to actually do the update!” Not very encouraging.</p>
<p>5+ years ago I set up an XNAT instance integrated with CTP for de-identification, and we used it for something like 1000 DICOM studies here in the lab. But basic (in my view, anyway) things that I wanted to see supported - more flexible and customizable search, easy extension with processing plugins, better integration with image viewing and annotation tools - were either very difficult or not possible. I don’t know whether this changed fundamentally since then. I am actually thinking to take another look at XNAT during the project week.</p>
<p>I do think DICOM is the right foundation for organizing imaging data. But I also think that it will require a lot of effort to cover gaps in the standard itself and in its implementation. Over the past years we did a lot of work on those gaps for clinical imaging analysis results. Maybe this most recent paper and pointers therein can give you an idea of the overall approach: <a href="https://www.nature.com/articles/sdata2018281" rel="nofollow noopener">https://www.nature.com/articles/sdata2018281</a>. But we did not do anything on the data management side, which is a huge gap (we are actively looking for opportunities and resources to work on that aspect as well). I feel if we as a community all made a commitment to use and improve DICOM, it would be very feasible to solve many problems using DICOM, but it is not the case, and the amount of work is overwhelming.</p>
<p>If you are interested in pre-clinical application, on top of all the issues related to dealing with the derived data, you will also be in a much worse situation with the vendors compliance on the acquisition side. Also I imagine the derived data is a lot more heterogeneous, the data analysis approaches are a lot more dynamic, and I don’t know if there are any existing implementations supporting the DICOM pre-clinical stuff to start from.</p>
<p>I would be very interested to learn from your experience using whatever approach you selected to support your work. If you are planning to be at the project week (this January or in the Summer), would be great to chat about this topic!</p>

---

## Post #14 by @Douglas_Boyer (2018-12-24 02:03 UTC)

<p>For what its worth, my team at MorphoSource (<a href="https://www.morphosource.org/" rel="nofollow noopener">https://www.morphosource.org/</a>) is developing a three.js volume viewer normalized to single file dicom volumes and nrrd for the “universal viewer” (<a href="https://universalviewer.io/" rel="nofollow noopener">https://universalviewer.io/</a>), which is designed for interoperabilitty with iiif (<a href="https://iiif.io/" rel="nofollow noopener">https://iiif.io/</a>) image servers.  This could be a good standard to rally around since it will undubitably be the solution of choice for the library preservation community (assuming it works!) and more generic preservation repositories.  Initially we will build some basic measurement tools, but more functionality could be added down the road.</p>

---

## Post #15 by @muratmaga (2018-12-24 04:54 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Unfortunately, I won’t be able to make it the upcoming winter PW, but hoping to attend the summer one, if it is in Boston as usual. DICOM, especially multi-frame one, seems like a good overall solution, but surprisingly few programs seem to support it well.</p>
<p>Currently I am leaning towards a solution that looks like Andras’ current workflow; ie., one that uses MRBs to store both the original image data and all derivative datasets associated with a single patient/specimen and a redcap (or likes) DB for access to the meta and PHI data for IRB approved folks. Same approach can be used for pre-clinical as well I think.  I guess we will start one way and learn from out mistakes.</p>

---
