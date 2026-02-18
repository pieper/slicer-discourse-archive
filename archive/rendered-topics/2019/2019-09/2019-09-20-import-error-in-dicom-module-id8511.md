# import error in DICOM module

**Topic ID**: 8511
**Date**: 2019-09-20
**URL**: https://discourse.slicer.org/t/import-error-in-dicom-module/8511

---

## Post #1 by @rahulba (2019-09-20 17:36 UTC)

<p>Problem report for Slicer 4.10.2 win-amd64: [please describe expected and actual behavior]<br>
Getting<br>
0 New Patients, 0 New Studies<br>
please help…here is my log files<br>
thank you<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f481470e1e8818e3085fe077a52e29eda4d0305.png" data-download-href="/uploads/short-url/dATMYXTnT1DXrWJfppeoLJlKvDn.png?dl=1" title="Screenshot%20(20)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f481470e1e8818e3085fe077a52e29eda4d0305_2_690x388.png" alt="Screenshot%20(20)" data-base62-sha1="dATMYXTnT1DXrWJfppeoLJlKvDn" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f481470e1e8818e3085fe077a52e29eda4d0305_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f481470e1e8818e3085fe077a52e29eda4d0305_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f481470e1e8818e3085fe077a52e29eda4d0305_2_1380x776.png 2x" data-dominant-color="C9DAE7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20(20)</span><span class="informations">1920×1080 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Chris_Rorden (2019-09-20 19:54 UTC)

<p>As a first step, why not see if dcm2niix can handle these images.</p>
<ol>
<li>Choose View/ExtensionManager menu</li>
<li>In “Install Extensions” tab, search for “Dcm2nii” - select the “SlicerDcm2nii” extension and install it.</li>
<li>Now in the main Slicer window you can show “All modules” and select “Dcm2niixGUI”. This will allow you to select the input directory.</li>
</ol>

---

## Post #3 by @rahulba (2019-09-21 10:18 UTC)

<p>It is showing error.Here is the error log…<br>
log</p>
<p>[INFO][Stream] 21.09.2019 15:38:33 [] (unknown:0) - ('running: ‘, [u’C:/Users/abhis/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDcm2nii/lib/Slicer-4.10/qt-scripted-modules\\Resources\\bin\\dcm2niix’, ‘-1’, ‘-d’, ‘0’, ‘-f’, ‘tmpfxalef’, ‘-o’, ‘C:/Users/abhis/AppData/Local/Temp/Slicer/__SlicerTemp__’, ‘-e’, ‘y’, ‘-z’, ‘y’, ‘F:/rahuldce/DCEMRISERIES’])</p>
<p>[CRITICAL][Stream] 21.09.2019 15:38:33 [] (unknown:0) - Command ‘[u’C:/Users/abhis/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDcm2nii/lib/Slicer-4.10/qt-scripted-modules\\Resources\\bin\\dcm2niix’, ‘-1’, ‘-d’, ‘0’, ‘-f’, ‘tmpfxalef’, ‘-o’, ‘C:/Users/abhis/AppData/Local/Temp/Slicer/__SlicerTemp__’, ‘-e’, ‘y’, ‘-z’, ‘y’, ‘F:/rahuldce/DCEMRISERIES’]’ returned non-zero exit status 2</p>

---

## Post #4 by @Chris_Rorden (2019-09-21 11:30 UTC)

<p><a class="mention" href="/u/ljod">@ljod</a> do you have any thoughts on this? Has the SlicerDcm2nii extension been tested on Windows? Just looking at the output it looks like <a class="mention" href="/u/rahulba">@rahulba</a> is using Windows, and the output shows  “\” and “/” where I would expect Windows to use just “”. I am not very familiar with Windows, but I wonder if this is causing issues.</p>
<p><a class="mention" href="/u/rahulba">@rahulba</a> :</p>
<ol>
<li>are you able to share a sample dataset via box, dropbox or google drive?</li>
<li>Do you have access to a MacOS or Linux computer to see if your issue is specific with Windows?</li>
</ol>

---

## Post #5 by @pieper (2019-09-21 13:02 UTC)

<p><a class="mention" href="/u/rahulba">@rahulba</a> did you try the suggestions in the FAQ?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #6 by @lassoan (2019-09-21 14:02 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="4" data-topic="8511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>Has the SlicerDcm2nii extension been tested on Windows?</p>
</blockquote>
</aside>
<p>Yes, it should work well on windows. [quote=“Chris_Rorden, post:4, topic:8511”]<br>
output shows “\” and “/” where I would expect Windows to use just “”<br>
[/quote]</p>
<p>Multi-platform applications usually don’t have problems with mixed path separators.</p>
<p>Is it possible that dcm2niix returns 2 as exit status and does not print any error messages? (I’m just trying to find out if dcm2niix is started successfully or the error occurred before that)</p>

---

## Post #7 by @Chris_Rorden (2019-09-21 14:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> - good catch, Exit code 2 reports that no valid files were found. However, no error is reported as the client asked for zero search depth. In this case, the exit code is explicit that no files are found, and therefore dcm2niix does not see the need to report an error. A quirk of dcm2niix generates a text error to the console when search depth is greater than zero but not when it is zero. The rationale is that with search depth 0 the calling software is explicitly requesting one folder, and might be calling multiple instances of dcm2niix to convert different folders <a href="https://github.com/neurolabusc/dcm2niiXL" rel="nofollow noopener">in parallel and asynchronously</a>. The default behavior of dcm2niix is <code>-d 5</code>, which will search the specified folder and children 5 folders deep. This is useful if the user selects a parent DICOMDIR, or if a single series are spread across multiple child folders (e.g. some vendors limit a folder to 1000 2D DICOM images, so DWI and fMRI series are often stored in multiple folders). I can understand the Slicer developers may prefer to explicitly search only one folder, but they may want to provide some logic for the case where the user is intentionally selecting a root DICOM folder.</p>
<p>The source code is:</p>
<pre><code>if (opts-&gt;dirSearchDepth &gt; 0)
            	printError("Unable to find any DICOM images in %s (or subfolders %d deep)\n", indir, opts-&gt;dirSearchDepth);
            else //keep silent for dirSearchDepth = 0 - presumably searching multiple folders
            	{};
</code></pre>
<p>the dcm2niix error codes are:</p>
<pre><code>EXIT_SUCCESS 0
EXIT_FAILURE 1 (GENERAL TYPE)
EXIT_NO_VALID_FILES_FOUND  2
EXIT_REPORT_VERSION  3
EXIT_CORRUPT_FILE_FOUND  4
</code></pre>
<p>However, it is unclear whether there are in fact no valid files in that folder or whether the folder is not being specified correctly.</p>
<p><a class="mention" href="/u/rahulba">@rahulba</a> can you try running <a href="https://github.com/rordenlab/dcm2niix/releases" rel="nofollow noopener">dcm2niix</a> from the Windows command line: <code>dcm2niix F:/rahuldce/DCEMRISERIES</code> and tell us what error is reported? Are the DICOM files directly in this folder, or does this folder have a DICOMDIR with the actual DICOMs buried in a sub-folder?</p>

---

## Post #8 by @rahulba (2019-09-23 10:42 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="7" data-topic="8511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>dcm2niix F:/rahuldce/DCEMRISERIES</p>
</blockquote>
</aside>
<p>yes i have read that and tried many things from that, nothing helped…thanks</p>

---

## Post #9 by @rahulba (2019-09-23 10:44 UTC)

<p>i will share my data by google drive, please share your email…</p>

---

## Post #10 by @Chris_Rorden (2019-09-23 10:49 UTC)

<p>My last name at sc.edu</p>

---

## Post #11 by @lassoan (2019-09-23 11:38 UTC)

<p>You can also send private messages through discourse (click on the user’s name then in the displayed popup window click the message icon).</p>

---
