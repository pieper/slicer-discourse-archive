---
topic_id: 781
title: "Recursively Checking If Folder Contains Dicoms"
date: 2017-07-28
url: https://discourse.slicer.org/t/781
---

# Recursively checking if folder contains DICOMs

**Topic ID**: 781
**Date**: 2017-07-28
**URL**: https://discourse.slicer.org/t/recursively-checking-if-folder-contains-dicoms/781

---

## Post #1 by @moselhy (2017-07-28 21:11 UTC)

<p>Hello,</p>
<p>I am developing a segmentation module called “PhantomSegmenter” which would automatically segment phantoms. The user only has to input a volume and press the button. However, I would like to give the user a choice to select a directory containing DICOMs. Here is the issue:</p>
<p>When the user selects a directory, I would like to recursively check whether the selected directory contains any .dcm or .ima files. I would want to check the size of that directory first, to make sure the user did not select the wrong folder (which could potentially contain terabytes of irrelevant files, and recursively checking an enormous directory to see whether each filename ends with the aforementioned two extensions would be too intensive most likely crash the program without saving any data). However, <a href="https://stackoverflow.com/questions/1392413/calculating-a-directory-size-using-python" rel="noopener nofollow ugc">checking the folder size is no more efficient than the recursive check</a>.</p>
<p>Nevertheless, I thought about two potential solutions, and am having a dilemma of which two of the following methods I should take:</p>
<ol>
<li>
<p>Simply enable the “Apply” button, assuming the user inputted a proper directory, and only check when the button is clicked.</p>
</li>
<li>
<p>Recursively check when the user selects a directory, and assume they inputted a proper directory, which could crash the program as I mentioned.</p>
</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f31c8c5ee41562a6e37d512ff8a21fa5715eb11.png" alt="image" data-base62-sha1="i9diFfAGjjN2mFTWKD1yi7SVjvb" width="529" height="326"></p>

---

## Post #2 by @lassoan (2017-07-28 21:44 UTC)

<p>I think it is a reasonable expectations from users to be able to select a directory that contains the relevant data. Parsing gigabytes of data can be completely normal.</p>
<p>Note that the DICOM indexer in Slicer implements recursive checking of a directory tree, analyzing all file contents (DICOM files don’t use any specific file extension, so you cannot assume that all DICOM files have .dcm or .ima extension), load them into a database that is then shown to the user in the DICOM browser.</p>
<p>If you want to improve loading/parsing time and you can be sure that the data comes straight from a scanner (no files has been added or modified) then you can use the DICOMDIR file in the root directory. It contains a catalog of all DICOM files with some metadata. It should be enough to find that single file and show the content to the user. The user can then choose which images he is interested in and you would only examine+load those files. This would reduce file analysis time from several minutes to a few seconds.</p>

---

## Post #3 by @moselhy (2017-07-30 16:14 UTC)

<p>Where can I find this DICOMDIR file? By the root directory, do you mean the user’s home directory?</p>

---

## Post #4 by @lassoan (2017-07-30 18:19 UTC)

<p>DICOMDIR file is usually in the root directory of the DICOM CD or DVD.</p>

---
