---
topic_id: 3072
title: "Cannot Find My Installed Extension In Modules"
date: 2018-06-05
url: https://discourse.slicer.org/t/3072
---

# Cannot find my installed extension in modules

**Topic ID**: 3072
**Date**: 2018-06-05
**URL**: https://discourse.slicer.org/t/cannot-find-my-installed-extension-in-modules/3072

---

## Post #1 by @xuec (2018-06-05 03:09 UTC)

<p>Hi,</p>
<p>I have just installed the PETDICOM extension (successfully), as I can view it in the manage your extension in the extension manager, however, it is no where to find in the modules. Does anyone perhaps could give me a hint please? Thank you in advance.</p>
<p>Regards,<br>
Cindy</p>

---

## Post #2 by @xuec (2018-06-05 07:11 UTC)

<p>nevermind, I found a solution already. Thank you.</p>

---

## Post #3 by @cpinter (2018-06-05 13:13 UTC)

<p>It’s great but can you please describe your solution just in case others bump into the same problem? If they find this question and the answer mentioning the solution but without the description they will be disappointed. Thanks!</p>

---

## Post #4 by @jcfr (2018-06-05 15:34 UTC)

<p>5 posts were split to a new topic: <a href="/t/should-we-delete-topics-that-end-up-not-containing-any-useful-information/3079">Should we delete topics that end up not containing any useful information?</a></p>

---

## Post #5 by @fedorov (2018-06-05 18:32 UTC)

<p>To clarify, some of the Slicer modules do not show up in the module list.</p>
<p>Developers can develop modules in such a way that they are invisible in the list, but are still providing the functionality and can be accessed programmatically. The reason this is done is because sometimes the module does not require any user interaction and is applied in batch mode, or because it is integrated as a plugin within another component of Slicer.</p>
<p>In the case of PETDICOM extension, one of the modules it provides is a DICOM plugin that will automatically recognize PET DICOM data, will apply SUV normalization and will allow you to load the result using DICOM Browser. None of the Slicer DICOM plugins are exposed directly in the Slicer module list.</p>
<p><a class="mention" href="/u/xuec">@xuec</a> please let us know if this helps, and whether I correctly understood the source of your confusion from your post.</p>

---

## Post #6 by @xuec (2018-07-20 03:58 UTC)

<p>yes… that’s exactly is the answer. I am sorry it took me quite long to reply. Will reply sooner next time!</p>

---
