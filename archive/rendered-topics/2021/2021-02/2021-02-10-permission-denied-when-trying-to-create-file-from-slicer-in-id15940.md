---
topic_id: 15940
title: "Permission Denied When Trying To Create File From Slicer In"
date: 2021-02-10
url: https://discourse.slicer.org/t/15940
---

# Permission denied when trying to create file from Slicer in most recent Nightly

**Topic ID**: 15940
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/permission-denied-when-trying-to-create-file-from-slicer-in-most-recent-nightly/15940

---

## Post #1 by @mikebind (2021-02-10 22:26 UTC)

<p>I’m a little mystified why I can’t seem to save screenshots or other files on a recent nightly on Windows (4.13.0-2021-02-04). I wonder if this Slicer version has been put into some kind of sandbox, but I’m not sure how to test that.  After some experimentation, I have found that a minimal example which demonstrates the problem on my machine is to put the following at the python interactor prompt</p>
<pre><code>f = open('c:/Users/mikeb/Documents/test.txt','w')
</code></pre>
<p>This works fine for me in 4.11.20200930, but fails with a “PermissionError [Errno 13]” on 4.13.0-2021-02-04.  I think this demonstrates that the problem is not a permission setting on the folder itself (because then the stable Slicer release also wouldn’t have permission to write there).</p>
<p>Oddly, if I go further up the file hierarchy, both Slicer versions can create a file in “c:/tempslicer”, so it is also not the case that 4.13.0-2021-02-04 can’t create files anywhere.</p>
<p>I would appreciate any help, suggestions, or insight anyone can provide.  This feels like a weird error and I’m not sure how to troubleshoot it.</p>

---

## Post #2 by @lassoan (2021-02-11 00:10 UTC)

<p>I have no idea what can cause this, but very interesting.</p>
<ul>
<li>Do you get the same error for any filenames in the Documents folder (test1.txt, test2.txt, …)?</li>
<li>Can you reproduce the issue in a subfolder (“c:/Users/mikeb/Documents/something/test.txt”)?</li>
<li>Do you run any antivirus software?</li>
<li>Does it make any difference if you set a different encoding (<code>f = open('c:/Users/mikeb/Documents/test111.txt','w', encoding="latin1"</code>)?</li>
<li>You can trace all file access operations using <a href="https://docs.microsoft.com/en-us/sysinternals/downloads/procmon">Process Monitor</a> to see if Slicer even gets to a system call and if any other software manipulates files in that folder.</li>
<li>Does it work if you install a new Slicer (e.g., latest Slicer Preview Release)?</li>
</ul>

---

## Post #3 by @mikebind (2021-02-11 01:59 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="15940" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I have no idea what can cause this, but very interesting.</p>
<ul>
<li>Do you get the same error for any filenames in the Documents folder (test1.txt, test2.txt, …)?</li>
</ul>
<p>Yes.</p>
<ul>
<li>Can you reproduce the issue in a subfolder (“c:/Users/mikeb/Documents/something/test.txt”)?</li>
</ul>
<p>Yes, initially I was trying to save to a subfolder of Documents and was running into the same issue.</p>
<ul>
<li>Do you run any antivirus software?</li>
</ul>
<p>Yes, Avast antivirus</p>
<ul>
<li>Does it make any difference if you set a different encoding (<code>f = open('c:/Users/mikeb/Documents/test111.txt','w', encoding="latin1"</code>)?</li>
</ul>
<p>No, same error.</p>
<ul>
<li>You can trace all file access operations using <a href="https://docs.microsoft.com/en-us/sysinternals/downloads/procmon">Process Monitor</a> to see if Slicer even gets to a system call and if any other software manipulates files in that folder.</li>
</ul>
<p>See below the quote for results…</p>
<ul>
<li>Does it work if you install a new Slicer (e.g., latest Slicer Preview Release)?</li>
</ul>
<p>I can try with the newest from today if you think it might help, but I just downloaded this preview release a few days ago…</p>
</blockquote>
</aside>
<p>This is the “Event Properties” of the Access Denied event pasted from ProcessMonitor (process is C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-02-04\bin\SlicerApp-real.exe):</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>High Resolution Date &amp; Time:</th>
<th>2/10/2021 5:35:34.7648711 PM</th>
</tr>
</thead>
<tbody>
<tr>
<td>Event Class:</td>
<td>File System</td>
</tr>
<tr>
<td>Operation:</td>
<td>CreateFile</td>
</tr>
<tr>
<td>Result:</td>
<td>ACCESS DENIED</td>
</tr>
<tr>
<td>Path:</td>
<td>C:\Users\mikeb\Documents\test111.txt</td>
</tr>
<tr>
<td>TID:</td>
<td>9448</td>
</tr>
<tr>
<td>Duration:</td>
<td>0.0000197</td>
</tr>
<tr>
<td>Desired Access:</td>
<td>Generic Write, Read Attributes</td>
</tr>
<tr>
<td>Disposition:</td>
<td>OverwriteIf</td>
</tr>
<tr>
<td>Options:</td>
<td>Synchronous IO Non-Alert, Non-Directory File</td>
</tr>
<tr>
<td>Attributes:</td>
<td>N</td>
</tr>
<tr>
<td>ShareMode:</td>
<td>Read, Write</td>
</tr>
<tr>
<td>AllocationSize:</td>
<td>0</td>
</tr>
</tbody>
</table>
</div><p>I do not see anything obvious around this time in ProcessMonitor, but I’m also not sure what I’m looking for.  There are a tremendous number of events recorded (100s of thousands in a few seconds).  Searching for test111 finds only the single event.</p>

---

## Post #4 by @lassoan (2021-02-11 02:48 UTC)

<p>The ProcessMonitor event shows that the Slicer properly requests opening the file but the system rejects the request. Since Windows typically does not block file applications like this (prevent a specific application from creating a file in a folder that is meant to be modified by the user), it is more likely that Avast sandboxes Slicer. It may be because Slicer Preview Releases are not signed (we only sign Slicer Stable Releases). You can try to uninstall Avast or disable real-time protection/sandbox/etc. features and see if it helps.</p>
<p>I don’t think you need antivirus on Windows 10 as the chances that a third-party software can stop something that slips through built-in protections are quite slim; but it is very likely that the antivirus will interfere with normal operation of your computer (slows it down and causes random failures).</p>
<p>Using ProcessMonitor is indeed enlightening. It shows you just how busy your computer is with millions of things even when you don’t do anything.</p>

---

## Post #5 by @mikebind (2021-02-11 19:10 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>.  It does appear to have been due to Avast.  In the past, I have typically had Avast pop up a warning alert the first time I open a newly installed nightly version of Slicer, but I have always clicked been able to say “Run Anyway” and I think this has created an exception which allowed normal Slicer operation.  I honestly don’t remember whether something like that warning came up this time, but if so, it appears that the same exception was not created this time.  I could open and use Slicer normally, but it seems like it was sandboxed in some way to prevent creation of files in my Documents directory or below.  When I turned off Avast temporarily and restarted the Slicer version that had not been able to save, the problem disappeared.  I added the SlicerApp-real.exe exception for the new version to the list manually, and the problem has not recurred.</p>
<p>Thanks for your help.</p>

---
