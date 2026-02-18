# Generate a "Viewer" for CT scans

**Topic ID**: 10157
**Date**: 2020-02-07
**URL**: https://discourse.slicer.org/t/generate-a-viewer-for-ct-scans/10157

---

## Post #1 by @JoeCrozier (2020-02-07 15:05 UTC)

<p>Odd question for you:<br>
We’re doing a study here at my hospital that will require a surgeon to look through about 100 ct scans and write down his diagnosis.  The scans will be anonymized and in an effort to not take up the surgeons workday when he could be operating, I’d like to deliver them to him in a way where he could do this at home.  A portable hard drive or live feed or something is what I had in mind.</p>
<p>Obviously if I were that surgeon I’d probably just download slicer and use that to import the scans/etc…   but I get the feeling that’ll not go over well, or I’d have to get on his computer and do that for him.</p>
<p>So my question is:  sometimes when you get a cd with ct scans on it, it’ll come with a “viewer” icon that you can click, that opens up the scans and allows you to scroll through, etc…<br>
Can 3DSlicer generate something like that?  It doesn’t need to have any of the typical slicer functionality besides being able to “see” the scans and scroll through them.  Any ideas?</p>
<p>And/or if not, any ideas of a different method that would work?  Sorry if this is too open ended.</p>

---

## Post #2 by @lassoan (2020-02-07 16:31 UTC)

<p>I see two main approaches.</p>
<ol>
<li>Classic DICOM CD viewer</li>
</ol>
<p>Since Slicer is a portable application (you don’t need to install it but it can run directly from anywhere), so it can be already used like a DICOM viewer running from a CD or USB stick. Application settings is read from Slicer.ini file from the user’s folder, but you can set your can update your database folder path by editing your SlicerLauncherSettings.ini file: in Application section, set <code>arguments</code> to:</p>
<pre><code>arguments=--python-code "slicer.util.selectModule('DICOM');slicer.dicomDatabaseDirectorySettingsKey='LocalDicomDatabase';slicer.modules.DICOMWidget.browserWidget.dicomBrowser.databaseDirectory=slicer.app.slicerHome+'/data'"
</code></pre>
<p>The only problem is that the DICOM database stores absolute paths for the indexed files, so that would need to be changed to relative paths (at least for files that are copied into the database). I’ve submitted an issue to track this: <a href="https://issues.slicer.org/view.php?id=4722">https://issues.slicer.org/view.php?id=4722</a></p>
<ol start="2">
<li>Web-based solution</li>
</ol>
<p>You can use a DICOMWeb database with a frontend like <a href="https://kheops.online/">Kheops</a> and launch Slicer from there. Slicer downloads the data from the web server and shows it to the user. See more detils <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/OHIFSlicerBridge/">here</a>. This already works but with some limitations: there is no progress display of the download operation (so for large studies Slicer be non-responsive for a few minutes) and uploading of analysis results is not yet implemented. We’ll work on improving this in the coming months.</p>

---

## Post #3 by @JoeCrozier (2020-02-07 16:59 UTC)

<p>I think I understand and that sounds great.  So if I’m understanding correctly, if I:</p>
<ul>
<li>
<p>Have all the images on a portable harddrive</p>
</li>
<li>
<p>Have slicer on that hard drive</p>
</li>
<li>
<p>Have updated the database folder path to a location on that hard drive</p>
</li>
</ul>
<p>Then someone should be able to click the slicer icon on that portable hard drive and slicer will open with the images already in the dicom database?  Correct?</p>

---

## Post #4 by @pieper (2020-02-07 17:14 UTC)

<p>Yes, that sounds like a reasonable solution.  Andras’s point about the absolute path names was that the paths have to match between the two computers, so if you mount the hard drive as D:\ on one machine it has to be mounted as D:\ on the other as well (if it’s Windows; for mac/linux you could use a symbolic link).</p>

---
