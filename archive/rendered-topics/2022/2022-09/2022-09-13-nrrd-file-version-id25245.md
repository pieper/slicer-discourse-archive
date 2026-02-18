# NRRD File Version

**Topic ID**: 25245
**Date**: 2022-09-13
**URL**: https://discourse.slicer.org/t/nrrd-file-version/25245

---

## Post #1 by @Michael_French (2022-09-13 21:48 UTC)

<p>With the recent Slicer patch, nrrd files we are exporting are now being exported as NRRD0004, whereas previously they were being exported as NRRD0005. This is causing issues as our application supports NRRD0005 only. Is there a way to switch the version of the nrrd file being exported in Slicer?</p>

---

## Post #2 by @lassoan (2022-09-13 23:01 UTC)

<p>The only <a href="http://teem.sourceforge.net/nrrd/format.html#general.1">difference between NRRD 4 and 5</a> is that an optional <code>measurement frame</code> was added. Therefore, if a reader can load NRRD 5 files then it can load NRRD 4 files, too; there is no reason to reject NRRD0004 files. Writers should write the lowest necessary file version for maximum compatibility, which is usually NRRD 4.</p>
<p>Slicer mostly writes NRRD 4 files, but it writes NRRD 5 when writing tensor volumes, as they require storage of measurement frame. Volume and transform sequences (.seq.nrrd) are saved with the same writer as tensor volumes and so they happen to be unnecessarily written in NRRD 5 format (while NRRD 4 would suffice). We could change this to use NRRD 5 only when it is strictly necessary, but as I understand it would not help you, because you would like to always see NRRD 5.</p>
<p>What kind of images you have experienced a different behavior in different Slicer versions (scalar volumes, vector volumes, tensor volumes, segmentations, volume sequences, …)?<br>
Which Slicer versions?<br>
What is the software that refuses to load NRRD0004 files?</p>

---

## Post #3 by @Michael_French (2022-09-14 13:11 UTC)

<p>We had previously used slicer 4.x.x and older which would export .seg.nrrd files as NRRD0005, but we are now using slicer 5.0.2 which exports .seg.nrrd files as NRRD0004.</p>
<p>The software that’s breaking is our own personal software that we built. We decided to change our software to support NRRD0004, but were wondering if there were any settings or fixes in the slicer application that we could use to temporarily fix the issue.</p>
<p>The images that are having issues in our software when the data is exported from 5.0.2 are segmentations.</p>

---

## Post #4 by @lassoan (2022-09-14 15:39 UTC)

<p>Writing NRRD0005 (and the identity measurement frame) was unnecessary for segmentation files. Using the lowest necessary version would normally make the file compatible with more software, so we don’t plan to change this.</p>
<p>Changing your software to accept both NRRD0005 and NRRD0004 should be sufficient. You can accept earlier versions as well, because all the changes between NRRD versions have been backward compatible so far.</p>
<p>If you want to isolate yourself from such details and don’t want to spend time with redeveloping and maintaining a nrrd parser then you can use (and even contribute to) existing free, open-source nrrd libraries. For reading Slicer .seg.nrrd files, you can use <a href="https://pypi.org/project/slicerio/">slicerio Python package</a> (if anything is missing or inconvenient then contributions are very welcome!). In general, for NRRD reading/writing there is <a href="https://pypi.org/project/pynrrd/">pynrrd</a> for Python, <a href="https://itk.org/">ITK</a> for C++, <a href="https://scif.io/">scifio</a> for Java, <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">nrrdread/nrrdwrite</a> for Matlab, etc.</p>

---

## Post #5 by @Michael_French (2022-09-14 17:42 UTC)

<p>Okay thank you for your help! I have a better understanding of the versioning now, and will work on updating our software accordingly.</p>

---
