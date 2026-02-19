---
topic_id: 27661
title: "Is There A Web Based Plug In For Project Management Of Annot"
date: 2023-02-06
url: https://discourse.slicer.org/t/27661
---

# Is there a Web-based plug-in for project management of annotators/labelers?

**Topic ID**: 27661
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/is-there-a-web-based-plug-in-for-project-management-of-annotators-labelers/27661

---

## Post #1 by @Helen_Vu (2023-02-06 14:08 UTC)

<p>We are labeling a large project with multiple labelers but are downloading the images onto Dropbox. Our reviewers then have to open Dropbox to review the images.<br>
Is there a web-based project management platform where completed labeled images can get loaded automatically and reviewers can review and communicate thru the webpage? (like a commercial product like V7)/</p>

---

## Post #2 by @pieper (2023-02-06 16:54 UTC)

<p>There was some progress last week working with <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/Kaapana_overall/">Kaapana</a> for this kind of work.  I’m not sure it’s ready yet but if you are willing to experiment it could be very useful.</p>

---

## Post #3 by @rbumm (2023-02-06 20:16 UTC)

<p>We also saw <a href="https://www.nora-imaging.com/">Nora</a> @ Project Week – a medical imaging platform that was recommended as a tool for image labeling and annotation in the cloud.</p>

---

## Post #4 by @fedorov (2023-02-06 20:19 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="3" data-topic="27661" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>We also saw <a href="https://www.nora-imaging.com/">Nora </a> @ Project Week – a medical imaging platform that was recommended as a tool for image labeling and annotation in the cloud.</p>
</blockquote>
</aside>
<p>It does not look like Nora is open source. Is this correct?</p>

---

## Post #5 by @fedorov (2023-02-06 20:26 UTC)

<aside class="quote no-group" data-username="Helen_Vu" data-post="1" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/helen_vu/48/18195_2.png" class="avatar"> Helen_Vu:</div>
<blockquote>
<p>Is there a web-based project management platform where completed labeled images can get loaded automatically and reviewers can review and communicate thru the webpage? (like a commercial product like V7)/</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a> and I have been working on a Slicer extension (it is not yet in Slicer Extension index, and is not documented -but is in a public repo) that aims to streamline annotation in Slicer. It is not a solution that will look as shiny as commercial solutions, and it is work in progress looking for a “killer app”, but it is free open source and has some nice features already:</p>
<ul>
<li>can talk to a local Slicer database or remote DICOM server via DICOMweb</li>
<li>takes care of data loading and viewer configuration</li>
<li>can be configured with the pre-defined “picklist” of labels that need to be segmented</li>
<li>saves segmentation results as DICOM SEG, which provides a standard way of associating annotation results with the readers</li>
</ul>
<p>We have a “recipe” of deploying Slicer on a cloud VM here <a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop</a>, so you can leverage cloud-based DICOM stores from Google, Slicer application talking to those via authenticated DICOMweb, and access Slicer application via your browser.</p>
<p>If you are looking for a ready-to-go solution, it is not, but if you are looking for something to start with - you may want to consider it. We would be happy to organize a call to demonstrate the existing capabilities if you are interested - just let me know.</p>

---

## Post #6 by @lassoan (2023-02-06 20:41 UTC)

<p>MONAILabel can be used for this, too. There was some prototype (MONAILabelReview) that allowed identification of users, user roles, etc. but I’m not sure if all those features have made it into MONAILabel.</p>
<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>It does not look like Nora is open source. Is this correct?</p>
</blockquote>
</aside>
<p>Correct, source code of Nora is not publicly available. Nora might have a chance either as a product or as an open-source viewer/segmentation tool, but right now it seems to be just an internal tool that is only used by the developers and some of their collaborators.</p>
<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a> and I have been working on a Slicer extension (it is not yet in Slicer Extension index</p>
</blockquote>
</aside>
<p>This sounds great, it would be nice to learn more about this.</p>
<p>It could use the <a href="https://phabricator.mitk.org/T29160">Kaapana tasklist file format</a> that MITK uses already and I plan to add support for in Slicer.</p>

---

## Post #7 by @fedorov (2023-02-06 20:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It could use the <a href="https://phabricator.mitk.org/T29160">Kaapana tasklist file format </a> that MITK uses already and I plan to add support for in Slicer.</p>
</blockquote>
</aside>
<p>Interesting. I have not heard about this before. We should consider this discussion thread in that context: <a href="https://discourse.canceridc.dev/t/storing-definitions-of-data-collections-as-dicom-entities/286" class="inline-onebox">Storing definitions of data collections as DICOM entities - Developers - Imaging Data Commons</a>.</p>
<p>From my perspective (and I think from Kaapana perspective as well), it will be rather important that the definition of task representation is developed with the understanding of requirements and implications of using DICOM for input and output of the segmentation process.</p>
<p><a class="mention" href="/u/nolden">@nolden</a> <a class="mention" href="/u/hmeine">@hmeine</a> might be interested to monitor this discussion.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This sounds great, it would be nice to learn more about this.</p>
</blockquote>
</aside>
<p>Those interested, please add your voice, and we can organize a demo/discussion. We had such demos earlier for <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/rbumm">@rbumm</a> and <a class="mention" href="/u/lassoan">@lassoan</a> I believe, but we can meet again and revisit where we are, and whether there is motivation and interest to go further.</p>

---

## Post #8 by @lassoan (2023-02-06 21:20 UTC)

<p>Kaapana takes care of collecting data from and uploading the end result to DICOMweb or other storage. But I agree that it could be useful to allow the client (Slicer, MITK, etc) use a DICOMweb or other storage directly.</p>
<p>It could be just a matter of adding a property that specifies storage type (local file, DICOMweb, DICOM DIMSE networking, S3, etc.) and an object that specifies storage properties (server URL, API key, …).</p>
<p>Of course we are talking about redefining/reimplementing features that have been around in DICOM for decades. It would make sense to look at how DICOM modality worklist/performed procedure step data structures would be suitable for this. I guess it is just too tempting to start from scratch with something really simple.</p>

---

## Post #9 by @kislinsk (2023-02-07 13:03 UTC)

<p>Hi all! <a class="mention" href="/u/nolden">@nolden</a> made me aware of this thread. I’m Stefan, one of the MITK core developers. If you have any questions regarding the MITK Segmentation Task List and its file format, please do not hesitate to ask.</p>
<p>We originally created the file format / feature primarily for another internal project but it already sparked quite some interest in (and is used by) other projects like Kaapana. Hence, we are planning to make the format public with the upcoming MITK v2023.04 release:</p>
<ul>
<li>File format specification and feature documentation will be part of MITK’s documentation and help system</li>
<li>The plugin/GUI on top of the MITK Segmentation Task Lists will be available in our official MITK Workbench application (currently only available in the less known, “build yourself” MITK FlowBench application).</li>
</ul>
<p>We are happy to get any feedback and ideas for extensions in particular regarding any DICOM topics.</p>

---

## Post #10 by @lassoan (2023-02-07 14:13 UTC)

<p>Thanks for the information <a class="mention" href="/u/kislinsk">@kislinsk</a>. Have you considered adding support for alternative storage types, such as DICOMweb?</p>
<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>From my perspective (and I think from Kaapana perspective as well), it will be rather important that the definition of task representation is developed with the understanding of requirements and implications of using DICOM for input and output of the segmentation process.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Do you have any specific requirement in mind? Do you think DICOM worklist could/should be  used for prescribing and tracking completion of manual segmentation tasks?</p>

---

## Post #11 by @fedorov (2023-02-07 14:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Do you have any specific requirement in mind? Do you think DICOM worklist could/should be used for prescribing and tracking completion of manual segmentation tasks?</p>
</blockquote>
</aside>
<p>Andras, I don’t have specific requirements in mind right away. I would need to spend time evaluating the alternatives and functionality available in DICOM, I have never looked into those before.</p>
<p><a class="mention" href="/u/kislinsk">@kislinsk</a> have you looked into the related capabilities in DICOM, such as DICOM worklist and inventory IOD while developing that format proposal?</p>
<p><a class="mention" href="/u/david_clunie">@David_Clunie</a> do you have any thoughts on contrasting Kaapana tasklist format and existing DICOM capabilities?</p>

---

## Post #12 by @kislinsk (2023-02-09 08:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/kislinsk">@kislinsk</a>. Have you considered adding support for alternative storage types, such as DICOMweb?</p>
</blockquote>
</aside>
<p>We focused on local file paths so far indeed, driven by our requirements and Kaapana’s way of providing general resource access through local files. URIs are not off the table, though, as long as complexity lies within in the intentional KISS spirit of the file format.</p>
<aside class="quote no-group" data-username="fedorov" data-post="11" data-topic="27661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/kislinsk">@kislinsk</a> have you looked into the related capabilities in DICOM, such as DICOM worklist and inventory IOD while developing that format proposal?</p>
</blockquote>
</aside>
<p>We had a look at these alternatives in the beginning but eventually decided to come up with our own, more simple, tailored approach for what we actually need. One of the main goals was to keep it as simple as possible and therefore easily approachable for people in our research environment compared to having a fully fledged solution for clinical routine.</p>
<p>That said, we see DICOM compatibility more from the perspective of I/O mapping instead of having a fully integrated DICOM workflow. For example, we have (experimental) support of DICOM SEG and try to pipe or derive important/necessary DICOM tags through from corresponding input.</p>

---
