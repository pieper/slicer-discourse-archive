---
topic_id: 11895
title: "Nifti To Dicom Conversion"
date: 2020-06-06
url: https://discourse.slicer.org/t/11895
---

# NIfTI to DICOM conversion

**Topic ID**: 11895
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/nifti-to-dicom-conversion/11895

---

## Post #1 by @Chris_Rorden (2020-06-06 11:40 UTC)

<p>This forum seems the correct location for recent questions on <a href="https://neurostars.org/t/convert-nifti-segmentation-mask-to-dicom-rtstruct/7060" rel="nofollow noopener">neurostars</a> and <a href="https://www.nitrc.org/forum/message.php?msg_id=29914" rel="nofollow noopener">nitrc</a> regarding NIfTI to DICOM conversion. Slicer is the tool I would use for these operations. Perhaps members of this forum can provide guidance to these users.</p>
<p>Alex Cohen raises an interesting question of whether the rich meta data of the BIDS JSON headers could be included in the NIfTI to DICOM conversion. This would have several benefits:</p>
<ol>
<li>DICOM images can use a lot of tools that do not support NIfTI.</li>
<li>Complicated 2D classic DICOMs converted to BIDS/NIfTI could be saved as vendor agnostic simple Enhanced DICOM resulting in faster transmission and less disk space.</li>
<li>Vendor specific private tags (e.g. for <a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI" rel="nofollow noopener">diffusion gradients</a> GE uses different frame of reference than Siemens/Philips) could be saved to common public tags (bearing in mind NIfTI uses yet a different frame of reference).</li>
<li>Privacy issues that have plagued DICOM due to buffer-overflow and failure to zero-pad arrays could be addressed. A simple lean converter developed with security in mind could prevent data leakage.</li>
<li>Users could edit the JSON text files to insert crucial data not provided by the vendor and these would then be inserted in DICOM files (e.g. Philips DICOM does not yet report slice timing or phase encoding polarity).</li>
</ol>
<p>I realize there are some challenges to this approach:</p>
<ol>
<li>There are no public tags for some details (slice timing, phase encoding polarity, etc).</li>
<li>Since different vendors have interpreted the DICOM standard differently, many tools use vendor specific heuristics and therefore may not work well (at least initially) with vendor agnostic data.</li>
</ol>
<p><a class="mention" href="/u/fedorov">@fedorov</a> is a leader in Slicer and proponent for DICOM in science (e.g. <a href="https://github.com/QIICR/dcmqi" rel="nofollow noopener">dcmqi</a> and <a href="http://qiicr.org/dicom4miccai/dicom4miccai2017.html" rel="nofollow noopener">PDF</a>) and can provide insight. I recognize the challenges, but also the potential.</p>

---

## Post #2 by @alexlicohen (2020-06-06 11:51 UTC)

<p>Thanks Chris for cross-posting this.</p>
<p>I have also used Slicer for many tasks, but so far only using NifTI files.</p>
<p>Thank you everyone in advance for your help and insight!</p>

---

## Post #3 by @lassoan (2020-06-07 02:27 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="1" data-topic="11895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>Alex Cohen raises an interesting question of whether the rich meta data of the BIDS JSON headers could be included in the NIfTI to DICOM conversion.</p>
</blockquote>
</aside>
<p>DICOM export plugins in Slicer either look up required fields from a cache in the application’s DICOM database or retrieve them from the stored DICOM file. If we want to support alternative DICOM formats (such as nrrd/nifti+json) then either DICOM toolkits (dcmtk, gdcm, and pydicom) or Slicer database and plugins would need to be updated to be able to read these alternative formats. Implementing and maintaining these would require some effort.</p>
<p>A simpler solution would be to implement a tool that can reconstruct a standard binary DICOM file from a nrrd/nifti+json. Then this DICOM file could be processed as usual. (But then it would be even simpler to go back and use the original DICOM file.)</p>
<p>Benefits of text-based DICOM representations are clear and converters are available (e.g., DCMTK’s dcm2xml/xml2dcm), but for some reason I still always get binary files only.  Maybe it will change if the format becomes more compact and user-friendly with the new <a href="https://www.dicomstandard.org/News/current/docs/sups/sup219-slides.pdf">JSON DICOM SR supplement</a>.</p>
<p><a class="mention" href="/u/alexlicohen">@alexlicohen</a> Are you sure you need DICOM RT structure set? That is am old, lossy format with lots of issues. I would recommend to use DICOM segmentation object instead.</p>

---

## Post #4 by @fedorov (2020-06-07 17:40 UTC)

<p>I don’t now about the current status of BIDS, but when I raised the question of the possibility of lossless (in terms of metadata) conversion between BIDS and DICOM, Chris Gorgolewski at the time said that was not possible. At least at that time, it seemed like if one wanted to get to DICOM from BIDS and back to DICOM, required DICOM attributes would be lost in translation.</p>
<p>What we have been exploring together with David Clunie recently is how to take conventional one-slice-per-file DICOM series (aka “2D DICOM” in your nomenclature) and generate legacy enhanced objects, initially just for the simplest use case of 3D volumetric acquisition. That process is very complex, since the input “2D DICOM” data often has errors that need to be fixed first, then a custom logic needs to be implemented to populate some of the attributes of enhanced DICOM, since there is often no 1-to-1 mapping from the original data, and then on top of that there are few tools that write enhanced DICOM and they are in rather early stages of development. We plan to summarize the process and challenges for public review, and will share when ready.</p>
<p>I guess one “advantage” of using BIDS is that it select which attributes can be interpreted and extracted from DICOM, and then discard everything else. Then to write an enhanced DICOM one can come up with “bogus” values for the required attributes that “didn’t make it” to a BIDS representation, and not bother cleaning up the mess in the original data. This approach is not really consistent with the spirit of DICOM, but I can appreciate how it can hugely simplify the process and perhaps meet some needs. Although, it remains to be seen if a meaningful enhanced DICOM object can be produced from the BIDS content.</p>
<p>Regarding “rich meta data of the BIDS JSON headers” - why wouldn’t BIDS community formulate the limitations of the current capabilities of DICOM to directly encode that rich metadata, and bring this to the DICOM community for standardization? I am not familiar with the details and needs of neuroimaging to comment on the limitations. What is that rich metadata that is present in JSON, but not present in DICOM?</p>

---

## Post #5 by @alexlicohen (2020-06-07 23:02 UTC)

<p>Hi Andrey,<br>
It is not that the BIDS-json files have any more data than the DICOMs. In fact, only specific/selected fields are retained. The goal, however, is to take advantage of the universe of software solutions for neuroimaging analysis that require NiFTI files (Many of which are easily applied to BIDS-formatted data (<a href="https://bids-apps.neuroimaging.io/apps/" rel="nofollow noopener">https://bids-apps.neuroimaging.io/apps/</a>), and very few of which can take DICOM data directly as input (and even those immediately convert out of DICOM as their first step)) and then be able to take these results back for clinical utility. Since manual entry and dummy data would have to be created for many of the DICOM header entries to simply get the data back into PACS for a particular subject, it would be ideal to at least fill in the actual data for the fields that we do have in an automated fashion.</p>

---

## Post #6 by @Chris_Rorden (2020-06-08 14:13 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> - the information missing in DICOM varies between vendors and generations. Some of these are listed for <a href="https://github.com/rordenlab/dcm2niix/tree/master/Siemens" rel="nofollow noopener">Siemens</a> (with less metadata in the XA series than the prior VA-VE series), <a href="https://github.com/rordenlab/dcm2niix/tree/master/Philips" rel="nofollow noopener">Phiips</a> and <a href="https://github.com/rordenlab/dcm2niix/tree/master/GE" rel="nofollow noopener">GE</a>. For fMRI and diffusion, information like EPI readout time, phase encoding polarity and slice timing are typically absent or stored in non-standard locations (e.g. Siemens proprietary CSA shadow header). In general, more meta data is missing for GE and Philips, including in plane acceleration, multi band factor, etc. For ASL, there are far more details missing for accurate replication and analyses. You can see the current BIDS specification for ASL to see what I mean. I am able to extract a lot of these parameters from the CSA header for Siemens, but this will not be possible for XA. I have worked closely with my research collaboration manager at Siemens to lobby for the crucial meta data. However, I do not have Philips or GE equipment. My sense is that research users are a small minority of the sales for the manufacturers, so we have a hard time getting the richer meta data into the source DICOM images. From personal communication, I know many users are shy about lobbying their research collaboration managers, as they feel it is important to maintain friendly relations. My own experience is that engineers like getting feedback from users and my own interactions with Siemens have been in the form of constructive criticism that has helped them develop better products.</p>
<p>I agree that a DICOM-&gt;BIDS-&gt;DICOM would not retain all of the meta data of the original DICOM. However, if a converter like dcm2niix is used, it should be enough for a valid DICOM image, and would retain the tags vital for replication and analysis for users in my field.</p>
<p>I think an important value-added component of the BIDS format is the validators, that ensure that the provided data can be handled in an automated data and is well curated. Reading these data back to DICOM would leverage this investment.</p>
<p>For full disclosure, I was a critic of BIDS in its planning stages, arguing that we would end up duplicating the complexity of DICOM. However, the thriving BIDS community reveals it has filled an important niche.</p>
<p>I agree that converting classic 2D DICOM to enhanced DICOM can be very complex. Different vendors have interpreted DICOM very differently. The constrained nature of NIfTI and its popularity in the field mean that there are many robust, well tested tools to handle conversion of classic DICOM to NIfTI, dealing with many of the DICOM edge cases. By using dcm2niix or one of the other <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener">popular alternatives</a> you can leverage the experience provided by having thousands of people use the tool on their own idiosyncratic images. Therefore, by using existing tools the DICOM -&gt; NIfTI -&gt; enhanced DICOM is greatly simplified and in general thoroughly tested. For example, NIfTI enforces that the first 3 dimensions are spatial, does not allow complicated transfer syntaxes, and has a simplicity that is less open to interpretation.</p>

---

## Post #7 by @fedorov (2020-06-08 22:03 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> I completely agree. Tools like dcm2niix are implementing the logic that would be essential to being able to put content of the private tags into the appropriate locations in the enhanced DICOM object, and since they operate on DICOM data, they will also have the attributes that would otherwise be lost once saved into NIfTI/BIDS. I think it would be great if dcm2niix could produce an enhanced DICOM side by side with NIfTI.</p>
<aside class="quote no-group" data-username="alexlicohen" data-post="5" data-topic="11895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alexlicohen/48/7047_2.png" class="avatar"> alexlicohen:</div>
<blockquote>
<p>The goal, however, is to take advantage of the universe of software solutions for neuroimaging analysis that require NiFTI files (Many of which are easily applied to BIDS-formatted data (<a href="https://bids-apps.neuroimaging.io/apps/">https://bids-apps.neuroimaging.io/apps/ </a>), and very few of which can take DICOM data directly as input (and even those immediately convert out of DICOM as their first step)) and then be able to take these results back for clinical utility.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/alexlicohen">@alexlicohen</a> I think that if you really want to take those results back for clinical utility, you need to keep around the original DICOM, or maintain the attributes needed to make sure your results can be saved in a DICOM object that can be part of the study you analyzed.</p>

---

## Post #8 by @alexlicohen (2020-06-09 00:29 UTC)

<p>In most cases, I’m thinking of how would one bring large scale or group level information, or even derived individual-level data (in nifti format) back into register with a single individual’s T1, so that specific individuals’ T1w DICOM would <em>indeed</em> be available.</p>
<p>A tool akin to dcm2niix that could strip/duplicate the appropriate DICOM fields into a json or enhanced DICOM that could then be used as a reference for additional files in the same frame of reference to be brought back to DICOM would be a big step forward.</p>

---

## Post #9 by @lassoan (2020-06-09 02:00 UTC)

<p><a class="mention" href="/u/alexlicohen">@alexlicohen</a> I think the hardest problem is to convince your hospital IT administrators to let any data you generate back into the clinical PACS. Most likely their policy is to only let FDA-approved software add data to the clinical systems. This makes sense, as they don’t have other ways to ensure that your software does not mess up things.</p>
<p>So, you have to develop an FDA-approved software from scratch, which requires a lot of paperwork - much more than implementing any DICOM/research format/DICOM converters.</p>
<p>You may reduce this paperwork if you plug in your software as a third-party application into the a commercial software’s app store. In fact, some of these clinical app stores already contain this kind of DICOM to research format conversion and back. I remember a presentation about Siemens Teamplay doing anonymization/conversion when transferring data between the clinical PACS and third-party applications.</p>

---

## Post #10 by @alexlicohen (2020-06-09 14:35 UTC)

<p>That’s a great point. I’m wondering if an interim goal would simply be to be able to create DICOMs that could be read by standalone clinical software (bypassing the institutional PACS).</p>
<p>This is the crux of the issue, however, as one solution would be that the past decades of software/pipeline development using neuroimaging <em>research</em> tools (e.g., Freesurfer) would have to be recapitulated to handle DICOM data for a continuous provenance chain in a single system (as <a class="mention" href="/u/fedorov">@fedorov</a> is advocating for), or we come up with a way to ‘short-circuit’ the input–&gt;output DICOM information in a controlled/reproducible way (which is the current question, trading absolute fidelity for broader applicability)</p>
<p>I believe this has been avoided in most cases of research-&gt;clinical tool (I’m thinking of DIADEM and NeuroQuant in particular <a href="https://www.nature.com/articles/s41398-020-0798-6" rel="nofollow noopener">https://www.nature.com/articles/s41398-020-0798-6</a>) by doing a complete one-way export from the clinical PACS, with all of the analysis being done using alternative formats, with the report back being a quantitative plus narrative assay, not DICOM formatted images; which has it’s own issues (cannot visually verify registration with clinical data, etc…).</p>

---

## Post #11 by @fedorov (2020-06-09 15:15 UTC)

<aside class="quote no-group" data-username="alexlicohen" data-post="10" data-topic="11895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alexlicohen/48/7047_2.png" class="avatar"> alexlicohen:</div>
<blockquote>
<p>This is the crux of the issue, however, as one solution would be that the past decades of software/pipeline development using neuroimaging <em>research</em> tools (e.g., Freesurfer) would have to be recapitulated to handle DICOM data for a continuous provenance chain in a single system</p>
</blockquote>
</aside>
<p>Relevant effort to harmonize Freesurfer outputs with DICOM: <a href="https://github.com/corticometrics/fs2dicom" class="inline-onebox">GitHub - corticometrics/fs2dicom: Convert FreeSurfer outputs to DICOM</a>.</p>
<p>Switching to DICOM for all purposes is a hard sell. What we’ve been doing instead is cherry-picking use cases and research analysis artifacts that could be suitable for harmonization with DICOM. Paul Wighton from Corticometrics (the link above is the tool he has been developing) has been advocating for using DICOM in neuroimaging analysis. It would be great to see more explorers, if not champions, from the neuroimaging community, who would be willing to give DICOM a chance.</p>
<p><a class="mention" href="/u/alexlicohen">@alexlicohen</a> maybe we should go back to your use case that triggered this conversation, and see what can be done to address your immediate needs, and if there are existing tools you could use?</p>

---

## Post #12 by @alexlicohen (2020-06-09 17:54 UTC)

<p>Thanks <a class="mention" href="/u/fedorov">@fedorov</a>. Will reach out to you off-line.</p>

---
