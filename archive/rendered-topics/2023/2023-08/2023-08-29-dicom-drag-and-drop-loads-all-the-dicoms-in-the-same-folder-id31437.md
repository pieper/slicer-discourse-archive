# DICOM drag and drop loads all the dicoms in the same folder instead of just the dragged one

**Topic ID**: 31437
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/dicom-drag-and-drop-loads-all-the-dicoms-in-the-same-folder-instead-of-just-the-dragged-one/31437

---

## Post #1 by @alireza (2023-08-29 19:13 UTC)

<p>Not sure what I have done, or where have I clicked that has changed the behaviour. But, right now if I drag and drop a single DICOM file from a folder that consists other studies/series, slicer would load them all. Instead I expect only the dragged one to be imported.</p>
<p>Can someone let me know how I can fix this?</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7039e4771d55379a09b5ea9a6364274e48c366fd.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7039e4771d55379a09b5ea9a6364274e48c366fd.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7039e4771d55379a09b5ea9a6364274e48c366fd.mp4</a>
    </video>
  </div><p></p>

---

## Post #2 by @alireza (2023-09-01 14:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> any chance you know what is happening here?</p>

---

## Post #3 by @lassoan (2023-09-01 15:09 UTC)

<p>Slicer does not load all the files, it just indexes the folder content, because a DICOM file is rarely acquired in isolation and you can get incomplete or misleading information if you ignore all the other files in the folder. Also, normally DICOM file names are meaningless, so you are not even supposed to know what a specific DICOM file contains.</p>
<p>That said, indeed the default behavior has changed (because we consolidated the two different ways of loading DICOM images - using DICOM module and Add data dialog) and I can imagine research workflows where isolated loading could be useful (e.g., if you copy files from unrelated studies into a folder and rename them to have names that you can recognize).</p>
<p>One solution is to force using the generic image loader for ITK files, by changing “DICOM” to “Volume” in the description column in Add data window.</p>
<p>We could also add a “Single fie” option to DICOM option to force indexing only the drag-and-dropped file. We are reworking the DICOM browser completely, so I would not invest time into adding this option now because maybe with the new visual browser you would not need this option anymore. You can submit a topic in feature request category on this forum or submit a feature request on Github to keep track of this idea.</p>

---

## Post #4 by @alireza (2023-09-05 13:15 UTC)

<p>Thanks for the reply.<br>
My use case is very simple, some one report a DICOM not working in OHIF, I download it, it goes to the Downloads folder. I drag and drop it in the Slicer to see how Slicer renders it, then Slicer loads all the other +100 downloaded DICOMs in my Download folder.</p>
<p>Drag and drop should just care about the dragged content and not the directory, similar to other apps: e.g., in powerpoint, if you drag and drop an image you don’t get all the other images in that folder imported, word, and other apps too</p>

---

## Post #5 by @lassoan (2023-09-05 13:56 UTC)

<aside class="quote no-group" data-username="alireza" data-post="4" data-topic="31437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p>Drag and drop should just care about the dragged content and not the directory, similar to other apps</p>
</blockquote>
</aside>
<p>A DICOM file is not a document, but just one of the data files of a large distributed database, so loading it is not comparable to loading a powerpoint document. That’s why no standard file extension is specified for DICOM files (you are not supposed to “open” a DICOM file by double-clicking on it) and that’s why when you import DICOM files in a DICOM viewer software then you are asked to choose a folder (not a single file).</p>
<p>Processing all the files in the folder is the safer, more foolproof default option, but allowing selectively loading files from a folder would not hurt either. Thank you for submitting the feature request, if there are more upvotes then we get back to it and discuss the details of how exactly offer the option to users.</p>

---

## Post #6 by @pieper (2023-09-05 14:58 UTC)

<p>It’s already possible to load a single dicom file - just change to volume and by default the “Single File” option is selected.</p>
<p>What we don’t have, that I have often wanted, is the ability to add a selection of one or more files to the database as opposed to a directory.  But in practice it’s usually pretty easy just to make a temp directory and copy in the files I want and then import the temp directory.</p>

---
