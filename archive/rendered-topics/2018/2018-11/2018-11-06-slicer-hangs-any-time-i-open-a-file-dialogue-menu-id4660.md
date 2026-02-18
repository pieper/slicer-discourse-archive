# Slicer hangs any time I open a file dialogue menu

**Topic ID**: 4660
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/slicer-hangs-any-time-i-open-a-file-dialogue-menu/4660

---

## Post #1 by @Justin_Kirby (2018-11-06 18:21 UTC)

<p>On 4.10.0 stable I tried importing data both using “Load Data” and the “Load DICOM Data” buttons.  As soon as I get to the point of trying to change directories to locate my data the interface hangs and the dialogue window says “Not responding”.  I’m on a fairly new Windows 10 computer with a SSD hard disk.  All other apps continue to work properly while Slicer hangs with my Task Manager showing plenty of free CPU/RAM.  Example screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/042ec4d6d600a90892847aa2444a749c217b8a7a.png" data-download-href="/uploads/short-url/B06VJN9S2Vxk08SbzyWz6ffbjY.png?dl=1" title="pastedImage" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/042ec4d6d600a90892847aa2444a749c217b8a7a_2_690x438.png" alt="pastedImage" data-base62-sha1="B06VJN9S2Vxk08SbzyWz6ffbjY" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/042ec4d6d600a90892847aa2444a749c217b8a7a_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/042ec4d6d600a90892847aa2444a749c217b8a7a_2_1035x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/042ec4d6d600a90892847aa2444a749c217b8a7a_2_1380x876.png 2x" data-dominant-color="CDCCCD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pastedImage</span><span class="informations">2729×1735 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-11-06 18:24 UTC)

<p>Most probably you have an unreachable network device (e.g., shared folder on a file server). You need to wait for the network operation to fail (it may take tens of minutes) or remove the unreachable device.</p>
<p>You can also just drag the folder or file what you would like to load and drop to the application window.</p>

---

## Post #3 by @fedorov (2018-11-06 18:25 UTC)

<p>Justin, can you try the following:</p>
<ol>
<li>open DICOM Browser window</li>
<li>click the “&gt;&gt;” button, and set LocalDatabase to some folder under a directory you can access</li>
<li>try “Import” again</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71eaf05637088068d24da9a6b1ddadc2e03e9bd5.png" data-download-href="/uploads/short-url/gfLj6UYZrxAAZ2MsStbJFc2GPoF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71eaf05637088068d24da9a6b1ddadc2e03e9bd5_2_690x62.png" alt="image" data-base62-sha1="gfLj6UYZrxAAZ2MsStbJFc2GPoF" width="690" height="62" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71eaf05637088068d24da9a6b1ddadc2e03e9bd5_2_690x62.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71eaf05637088068d24da9a6b1ddadc2e03e9bd5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71eaf05637088068d24da9a6b1ddadc2e03e9bd5.png 2x" data-dominant-color="DFE1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">901×81 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Justin_Kirby (2018-11-06 18:33 UTC)

<p>When I click the button to select a new folder it hangs as soon as I try to navigate to a new directory.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddcc0a1ed294f2ca715a65b867530d2d7ccc8822.png" data-download-href="/uploads/short-url/vE6FLwaPbw5I1vxdW7ehhrAcP0m.png?dl=1" title="pastedImage" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddcc0a1ed294f2ca715a65b867530d2d7ccc8822_2_690x415.png" alt="pastedImage" data-base62-sha1="vE6FLwaPbw5I1vxdW7ehhrAcP0m" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddcc0a1ed294f2ca715a65b867530d2d7ccc8822_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddcc0a1ed294f2ca715a65b867530d2d7ccc8822_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddcc0a1ed294f2ca715a65b867530d2d7ccc8822_2_1380x830.png 2x" data-dominant-color="FDFDFD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pastedImage</span><span class="informations">2882×1735 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Justin_Kirby (2018-11-06 18:36 UTC)

<p>I’m on a home PC with no network drives mounted/attached.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/416606790d86501deeb946c463c58b358fa784eb.png" data-download-href="/uploads/short-url/9kxCFFvAj6YaHgPfTjGYSkC4WIr.png?dl=1" title="pastedImage" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/416606790d86501deeb946c463c58b358fa784eb_2_586x500.png" alt="pastedImage" data-base62-sha1="9kxCFFvAj6YaHgPfTjGYSkC4WIr" width="586" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/416606790d86501deeb946c463c58b358fa784eb_2_586x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/416606790d86501deeb946c463c58b358fa784eb_2_879x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/416606790d86501deeb946c463c58b358fa784eb_2_1172x1000.png 2x" data-dominant-color="F8F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pastedImage</span><span class="informations">1373×1170 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-11-06 19:24 UTC)

<p>What operating system do you use? Is there a chance you can upgrade to Windows 10?</p>

---

## Post #7 by @fedorov (2018-11-06 19:29 UTC)

<aside class="quote no-group" data-username="Justin_Kirby" data-post="1" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/justin_kirby/48/66502_2.png" class="avatar"> Justin_Kirby:</div>
<blockquote>
<p>I’m on a fairly new Windows 10 computer with a SSD hard disk.</p>
</blockquote>
</aside>
<p>Andras, it is a Windows 10</p>

---

## Post #8 by @fedorov (2018-11-06 19:32 UTC)

<p>Andras, is there a way to get the log file in this situation? Would it contain anything useful? I am not familiar with Windows how to get the log into a file (or even console).</p>

---

## Post #9 by @lassoan (2018-11-06 19:37 UTC)

<p>Interesting. We have been using Slicer on many Windows 10 computers and have not experienced this issue.</p>
<p>Could you try to temporarily disconnect your network and see if you can open the file dialog then?<br>
Maybe also open a command prompt, enter <code>net use</code> and see if anything is printed.</p>
<p>You could also try to wait more (up to 1 hour) to see if the dialog becomes responsive.</p>
<p>Do you have third-party anti-virus software installed?</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>is there a way to get the log file in this situation</p>
</blockquote>
</aside>
<p>Showing a file dialog is a one-line call, so I don’t think we can log anything from Slicer. It is an issue at Qt and operating system level. Probably Qt tries to scans folders to determine what icons to display for them.</p>

---

## Post #10 by @Justin_Kirby (2018-11-06 21:01 UTC)

<p>If I wait long enough (usually 2-3min?) it goes to the next step but then I have to wait again to go to another directory.</p>
<p>Entering “net use” at command prompt results in the response “New connections will be remembered. There are no entries in the list.”</p>

---

## Post #11 by @fedorov (2018-11-06 21:42 UTC)

<p>Not sure if this helps, but few pointers I found:</p>
<ul>
<li><a href="https://superuser.com/questions/975648/windows-10-often-freezes-when-saving-or-opening-files">https://superuser.com/questions/975648/windows-10-often-freezes-when-saving-or-opening-files</a></li>
<li><a href="https://www.tenforums.com/general-support/77168-save-dialogue-box-freezes.html">https://www.tenforums.com/general-support/77168-save-dialogue-box-freezes.html</a></li>
</ul>
<p><a class="mention" href="/u/justin_kirby">@Justin_Kirby</a> did you experience this problem with any other application?</p>

---

## Post #12 by @jamesobutler (2018-11-06 23:34 UTC)

<p>Although Justin’s issue seems more like a hanging problem and not a crash problem I’ll provide some knowledge I had recently that might be related?</p>
<p>I had a recent experience with a user using Slicer 4.10.0 on Windows 10 where Slicer would consistently crash after the following:</p>
<pre><code class="lang-python">a=qt.QFileDialog()
a.getOpenFileNames()
</code></pre>
<p>The native dialog would open and then after about a second it would crash with a Slicer exit abnormally message and that’s it.  The icon in the Windows Taskbar would flash whenever it crashed so it seem like a Explorer issue. I was unable to replicate this issue on other Windows 10 computers with Slicer 4.10.0.  I tried it again on the problem computer today, and it wasn’t crashing. Maybe something about opening dialogs to specific remembered paths that are invalid or paths with specific icons?</p>

---

## Post #13 by @fedorov (2018-11-08 19:00 UTC)

<p><a class="mention" href="/u/justin_kirby">@Justin_Kirby</a> did you have a chance to try any of the suggestions in the links I referenced?</p>
<p>We talked about this with <a class="mention" href="/u/pieper">@pieper</a>, and one idea was to find another Qt-based application and see if the File open behavior there is the same.</p>

---

## Post #14 by @Justin_Kirby (2018-11-08 19:56 UTC)

<p>I tried the things at those links you sent to no avail.  In terms of trying another Qt-based app, I have VLC on my computer and when I try to navigate to open files with that it works fine.</p>

---

## Post #15 by @fedorov (2018-11-08 20:54 UTC)

<p>That’s too bad. I do not have any other ideas. I am sorry I do not know how to make Slicer work on your computer. This is not a good advertisement in preparations to RSNA for sure …</p>

---

## Post #16 by @lassoan (2018-11-08 21:11 UTC)

<p>Could you try file selectors in a recent version of <a href="https://www.paraview.org/download/">ParaView</a>?</p>
<p>If you keep having problems then contact me in a private message and we can set up a remote desktop sharing session.</p>

---

## Post #17 by @Justin_Kirby (2018-11-08 21:37 UTC)

<p>The latest Paraview lets me move around in the file selectors without any trouble.</p>
<p>I just noticed that I had an old nightly build still installed on my PC.  I uninstalled it using Windows Add/Remove programs just now, but it didn’t fix the issue.  However I’m wondering if there is any chance old files/caches/etc from prior installs could be causing problems.  Are there any hidden locations I can check for appdata to ensure all of the prior installations are totally gone?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97321cbf82f497018bc4407e293946b26642e15c.png" data-download-href="/uploads/short-url/lzxsIj6pdd5ywjS4UMyRxVYYsH2.png?dl=1" title="pastedImage" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97321cbf82f497018bc4407e293946b26642e15c_2_315x500.png" alt="pastedImage" data-base62-sha1="lzxsIj6pdd5ywjS4UMyRxVYYsH2" width="315" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97321cbf82f497018bc4407e293946b26642e15c_2_315x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97321cbf82f497018bc4407e293946b26642e15c_2_472x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97321cbf82f497018bc4407e293946b26642e15c.png 2x" data-dominant-color="DBDFE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pastedImage</span><span class="informations">590×934 25.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @fedorov (2018-11-08 21:46 UTC)

<p>I think it is in <code>C:\Users\&lt;your_user_name&gt;\AppData\Roaming\NA-MIC</code> (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings</a>)</p>

---

## Post #19 by @Justin_Kirby (2018-11-08 22:23 UTC)

<p>I deleted that and also the Cache folder mentioned on that page but no luck.</p>
<p>I just noticed one more detail that could possibly be a clue.  When the window loads the names of the folders show up but there are no icons.  Could Slicer be searching for some kind of icon set that is missing on my computer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c6cbff3cdfb380c198b2a6a14112124f9e781bc.png" data-download-href="/uploads/short-url/mjNtOa99ushwpyENmPbk5Jx0hUU.png?dl=1" title="pastedImage" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c6cbff3cdfb380c198b2a6a14112124f9e781bc.png" alt="pastedImage" data-base62-sha1="mjNtOa99ushwpyENmPbk5Jx0hUU" width="654" height="500" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pastedImage</span><span class="informations">1222×934 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @fedorov (2018-11-08 23:09 UTC)

<p>Are those icons missing with other file open dialogs in other apps?</p>

---

## Post #21 by @cpinter (2018-11-09 14:09 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="18" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I think it is in <code>C:\Users\&lt;your_user_name&gt;\AppData\Roaming\NA-MIC</code> (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings </a>)</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/justin_kirby">@Justin_Kirby</a> Have you tried deleting Slicer.ini in this folder? It helps sometimes.</p>

---

## Post #22 by @Justin_Kirby (2018-11-09 14:35 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>, no I haven’t noticed missing icons in any other applications.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a>, I deleted that entire folder including the .ini file but it didn’t help.</p>

---

## Post #23 by @fedorov (2018-11-09 14:55 UTC)

<p>Here’s another post with more suggested troubleshooting tips: <a href="https://answers.microsoft.com/en-us/windows/forum/windows_7-desktop/icons-missing-on-file-open-dialog/62ec161f-6ac3-4d0f-b65f-1db389e23be2">https://answers.microsoft.com/en-us/windows/forum/windows_7-desktop/icons-missing-on-file-open-dialog/62ec161f-6ac3-4d0f-b65f-1db389e23be2</a></p>
<p>The original issue observed was for Windows 7. I do not know if the tips they suggest are applicable for Windows 10, but at least some of them are simple to try.</p>
<p>Sorry you have to go through this. I don’t recall anything like this before from any user.</p>

---

## Post #24 by @lassoan (2018-11-09 17:05 UTC)

<p>If you keep having problems then contact me in a private message and we can set up a remote desktop sharing session to troubleshoot/fix the issue.</p>

---

## Post #25 by @petemq (2019-03-25 19:57 UTC)

<p>I have the same problem, tried reinstalling the latest stable version (4.10), deleting all cache files, creating a new empty dicom directory. All unsuccessfull so far.</p>
<p>However, the module seems to work in some way. After clearing the directory and reimporting, Slicer started hanging again right away, but after cancelling the operation a few minutes later, there were a few files correctly imported.</p>
<p>If it’s just a time factor, that would still be odd. On the longest try, I had Slicer run for 2 hours to import a 4GB directory. My PC is fairly new (Surface Book 2) and never used more than 25% CPU/2GB RAM. It runs on Win10 pro.</p>
<p>HHope you can help,<br>
Peter</p>

---

## Post #26 by @pieper (2019-03-25 20:17 UTC)

<p>Is this something you are able to reproduce using public data or is it something specific to your data?</p>

---

## Post #27 by @fedorov (2019-03-25 20:20 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>: I believe <a class="mention" href="/u/justin_kirby">@Justin_Kirby</a> who originally reported this issue could reproduce it with any dataset. Justin, were you able to resolve that issue, or gave up? I recall you were going to have a screen share with Andras to debug this, but there is no update on the thread whether you could resolve this.</p>

---

## Post #28 by @petemq (2019-03-25 20:34 UTC)

<p>Unfortunately, yes. I tried loading a different dataset with just 3 Patients. Again, Slicer went offline for &gt;15 mins, but when I restarted, the patients were in the directory.</p>
<p>It is just weird that for a study of ~800 patients with 1 series each the loading time should exceed 1 hour (especially as the same dataset on the old Imac next to me loaded in 10 min, but with a<br>
nice progress bar and without hanging issues).</p>

---

## Post #29 by @jamesobutler (2019-03-25 23:16 UTC)

<aside class="quote quote-modified" data-post="12" data-topic="4660">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-hangs-any-time-i-open-a-file-dialogue-menu/4660/12">Slicer hangs any time I open a file dialogue menu</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Although Justin’s issue seems more like a hanging problem and not a crash problem I’ll provide some knowledge I had recently that might be related? 
I had a recent experience with a user using Slicer 4.10.0 on Windows 10 where Slicer would consistently crash after the following: 
a=qt.QFileDialog()
a.getOpenFileNames()

The native dialog would open and then after about a second it would crash with a Slicer exit abnormally message and that’s it.  The icon in the Windows Taskbar would flash whenev…
  </blockquote>
</aside>

<p>To follow-up on my post earlier in this thread, I found a solution after reading <a href="https://bugreports.qt.io/browse/QTBUG-41416?page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel&amp;showAll=true" rel="noopener nofollow ugc">QTBUG-41416</a>. The problem was TortoiseSVN and after uninstalling the problem was resolved.</p>

---

## Post #30 by @lassoan (2019-03-25 23:59 UTC)

<p>I’m not sure if everyone talks about the same issue.</p>
<p>Opening the file dialog may hang due to faulty shell extensions (such as TortoiseGit) and/or problematic network resources. The issue is usually that shell extensions try to access a resources in the file tree to determine appropriate icon. On Windows, I never use folder selector but always drag-and-drop a folder to the Slicer application window to import it into the DICOM browser.</p>
<p>Slow DICOM import and/or loading is an entirely different issue. Slicer-4.10 and later should be reasonably fast on all operating systems. If import is slower than 100 files per minute then please share the application log so that we can have a quick look. If there is nothing obvious there then try it on a few different computers with the same operating system and exact same Slicer version. If you don’t have access to other comouters then see if you can reproduce the slow loading with a publicly available data set (e.g., from TCIA website) and send us the data set name so that we can test it, too.</p>

---

## Post #31 by @Justin_Kirby (2019-03-26 13:27 UTC)

<p>I agree with Andrey, this sounds a bit different than the experience I was having.  I never did get it resolved, but it was on my home computer so it’s not too important for me to have it working there.</p>

---

## Post #32 by @petemq (2019-03-26 14:54 UTC)

<p>Update:</p>
<ul>
<li>I tried importing the QIN lung database from TCIA. That worked just fine (~2 min for the whole database) and showed the progress bar I am used to</li>
<li>I tried running the import overnight with no other processes running. Again, slicer went into unresponsive mode. When I looked at my screen this morning, it showed a progress bar (for the first time!) at 30%, but still didn’t respond.</li>
<li>I can’t really share an error log, as I have to forcibly shut down slicer</li>
<li>It doesn’t matter if I try the import via the dicom dialogue or drag+drop</li>
<li>It doesn’t matter whether I choose “link” or “copy”</li>
<li>The database works just fine on the IMAC with the same version (but different OS). Will try it on a Windows machine.</li>
</ul>

---

## Post #33 by @pieper (2019-03-26 15:08 UTC)

<aside class="quote no-group" data-username="petemq" data-post="32" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f4b2a3/48.png" class="avatar"> petemq:</div>
<blockquote>
<ul>
<li>I tried importing the QIN lung database from TCIA. That worked just fine (~2 min for the whole database) and showed the progress bar I am used to</li>
<li>I tried running the import overnight with no other processes running. Again, slicer went into unresponsive mode. When I looked at my screen this morning, it showed a progress bar (for the first time!) at 30%, but still didn’t respond.</li>
</ul>
</blockquote>
</aside>
<p>Just to be sure I understand, you are saying that on the windows machine for your data the loading is slow, but for the TCIA data it is normal?  And they are loaded from the same disk?</p>

---

## Post #34 by @cpinter (2019-03-26 15:10 UTC)

<aside class="quote no-group" data-username="petemq" data-post="32" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f4b2a3/48.png" class="avatar"> petemq:</div>
<blockquote>
<p>I can’t really share an error log, as I have to forcibly shut down slicer</p>
</blockquote>
</aside>
<p>If you start Slicer then you can access the past logs in About / Report a bug / Recent log files.</p>

---

## Post #35 by @petemq (2019-03-26 15:14 UTC)

<p>Exactly. All files are on my local SSD</p>

---

## Post #36 by @petemq (2019-03-26 15:15 UTC)

<details>
<summary>
Recent logfiles</summary>
<p>[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - Session start time …: 2019-03-26 11:13:38<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - Slicer version …: 4.10.1 (revision 27931) win-amd64 - installed release<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - Memory …: 16309 MB physical, 20794 MB virtual<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 26.03.2019 11:13:38 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 26.03.2019 11:13:44 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 26.03.2019 11:13:45 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 26.03.2019 11:13:45 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 26.03.2019 11:13:46 [] (unknown:0) - Switch to module:  “Welcome”</p>
</details>

---

## Post #37 by @petemq (2019-03-26 15:16 UTC)

<p>To me it looks like the relevant information is not included in that log… <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=9" title=":confused:" class="emoji" alt=":confused:"></p>

---

## Post #38 by @lassoan (2019-03-26 15:26 UTC)

<p>There is a listbox where you can choose previous sessions. Find the one where you did the DICOM import and paste that log here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5041e1c4856152844fe2515126cf62bf1d51907c.png" data-download-href="/uploads/short-url/brZlDqqo6GKeVWgw2KDJRApbPdi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5041e1c4856152844fe2515126cf62bf1d51907c_2_690x443.png" alt="image" data-base62-sha1="brZlDqqo6GKeVWgw2KDJRApbPdi" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5041e1c4856152844fe2515126cf62bf1d51907c_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5041e1c4856152844fe2515126cf62bf1d51907c_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5041e1c4856152844fe2515126cf62bf1d51907c_2_1380x886.png 2x" data-dominant-color="DEDFE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1456×936 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #39 by @petemq (2019-03-26 16:04 UTC)

<details>
<summary>
Logfile from loading QIN lung study</summary>
<pre>
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - Session start time .......: 2019-03-25 22:03:02
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - Slicer version ...........: 4.10.1 (revision 27931) win-amd64 - installed release
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - Memory ...................: 16309 MB physical, 20894 MB virtual
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 25.03.2019 22:03:02 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 25.03.2019 22:03:04 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 25.03.2019 22:03:05 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 25.03.2019 22:03:05 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 25.03.2019 22:03:05 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Switch to module:  "DICOM"
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - New patient inserted: 35
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - New patient inserted as :  35
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.203059346048546067166621241946"
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.26655.1427919632.692116"
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.26680.1427919659.772120"
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.26703.1427919686.825713"
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.10926.1415313934.845816"
[DEBUG][Qt] 25.03.2019 22:03:19 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.10953.1415313952.202264"
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.10975.1415313969.658041"
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.10998.1415313986.834357"
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11020.1415314004.305238"
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11044.1415314021.713578"
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.113686129632252779806152571225"
[DEBUG][Qt] 25.03.2019 22:03:20 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:22 [] (unknown:0) - New patient inserted: 36
[DEBUG][Qt] 25.03.2019 22:03:22 [] (unknown:0) - New patient inserted as :  36
[DEBUG][Qt] 25.03.2019 22:03:22 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.131280137047230504248620024434"
[DEBUG][Qt] 25.03.2019 22:03:22 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:22 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11068.1415314060.494984"
[DEBUG][Qt] 25.03.2019 22:03:22 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11090.1415314090.247233"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11113.1415314108.629954"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11136.1415314127.447979"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11163.1415314146.771753"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11185.1415314165.811769"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11207.1415314184.314874"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11229.1415314213.682100"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11250.1415314232.286719"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.105160215333178506680008445454"
[DEBUG][Qt] 25.03.2019 22:03:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - New patient inserted: 37
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - New patient inserted as :  37
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.125721920632162119492941634336"
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11273.1415314264.119823"
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11303.1415314280.413802"
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11324.1415314296.790216"
[DEBUG][Qt] 25.03.2019 22:03:26 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11345.1415314313.310193"
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11367.1415314329.586022"
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11389.1415314346.112759"
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11411.1415314362.739985"
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11436.1415314392.362533"
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11461.1415314408.590393"
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.226952804465088850041383585906"
[DEBUG][Qt] 25.03.2019 22:03:27 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - New patient inserted: 38
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - New patient inserted as :  38
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.905893527127370577828717624475"
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11533.1415314442.128968"
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11557.1415314473.956189"
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11579.1415314490.398530"
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11605.1415314519.781969"
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11628.1415314548.266682"
[DEBUG][Qt] 25.03.2019 22:03:29 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11649.1415314564.809184"
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11674.1415314594.379340"
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11697.1415314611.138311"
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11719.1415314640.377971"
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.175436775971528801344124816822"
[DEBUG][Qt] 25.03.2019 22:03:30 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - New patient inserted: 39
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - New patient inserted as :  39
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.179196140853257709306370614304"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11740.1415314673.825314"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11764.1415314703.391937"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11785.1415314732.536466"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11811.1415314761.964741"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11832.1415314778.533651"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11854.1415314803.558985"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11880.1415314821.506006"
[DEBUG][Qt] 25.03.2019 22:03:32 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:33 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11902.1415314838.390805"
[DEBUG][Qt] 25.03.2019 22:03:33 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:33 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11924.1415314858.460"
[DEBUG][Qt] 25.03.2019 22:03:33 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:33 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.488217962349550158953121757047"
[DEBUG][Qt] 25.03.2019 22:03:33 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - New patient inserted: 40
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - New patient inserted as :  40
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.162154920966479062956783486597"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11948.1415314892.417932"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11970.1415314923.676592"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.11993.1415314941.526737"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12016.1415314960.375346"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12038.1415314989.918016"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12061.1415315019.930016"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12089.1415315049.748635"
[DEBUG][Qt] 25.03.2019 22:03:35 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:36 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12113.1415315067.282722"
[DEBUG][Qt] 25.03.2019 22:03:36 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:36 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12135.1415315084.763860"
[DEBUG][Qt] 25.03.2019 22:03:36 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:36 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.290396844417547229927401577621"
[DEBUG][Qt] 25.03.2019 22:03:36 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - New patient inserted: 41
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - New patient inserted as :  41
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.528630355329208477591397393556"
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12158.1415315114.303388"
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12186.1415315139.757904"
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12212.1415315156.136151"
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12235.1415315172.997841"
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12256.1415315189.280575"
[DEBUG][Qt] 25.03.2019 22:03:38 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12278.1415315207.840712"
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12301.1415315228.953072"
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12325.1415315244.987161"
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12346.1415315273.655167"
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.151808167652515688166637630421"
[DEBUG][Qt] 25.03.2019 22:03:39 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - New patient inserted: 42
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - New patient inserted as :  42
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.129972703814280056799490443458"
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12369.1415315298.868004"
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12392.1415315318.39702"
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12416.1415315344.221771"
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12445.1415315372.871258"
[DEBUG][Qt] 25.03.2019 22:03:44 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12469.1415315390.427772"
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12492.1415315409.240468"
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12515.1415315437.767778"
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12538.1415315454.420669"
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12566.1415315470.906815"
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7007.279704545205332033572331095200"
[DEBUG][Qt] 25.03.2019 22:03:45 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - New patient inserted: 43
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - New patient inserted as :  43
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7006.272642986942028254801481747252"
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12591.1415315505.148370"
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12615.1415315535.10496"
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12637.1415315552.666511"
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12708.1415315577.451018"
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12734.1415315600.691274"
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12757.1415315629.547878"
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:47 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12780.1415315653.762106"
[DEBUG][Qt] 25.03.2019 22:03:48 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:48 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12802.1415315670.640491"
[DEBUG][Qt] 25.03.2019 22:03:48 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:48 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12824.1415315699.661550"
[DEBUG][Qt] 25.03.2019 22:03:48 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:48 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7006.707460157128929865794170952055"
[DEBUG][Qt] 25.03.2019 22:03:48 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - New patient inserted: 44
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - New patient inserted as :  44
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7006.560604575027641500480263397602"
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12872.1415315749.26145"
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12895.1415315765.668432"
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12921.1415315782.521178"
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.27634.1427924773.535713"
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.27655.1427924794.376624"
[DEBUG][Qt] 25.03.2019 22:03:50 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.27681.1427924838.899306"
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12944.1415315798.955926"
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12966.1415315828.225166"
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Need to insert new series:  "1.2.276.0.7230010.3.1.3.0.12988.1415315844.619273"
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7006.223754665617431091646793304801"
[DEBUG][Qt] 25.03.2019 22:03:51 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:53 [] (unknown:0) - New patient inserted: 45
[DEBUG][Qt] 25.03.2019 22:03:53 [] (unknown:0) - New patient inserted as :  45
[DEBUG][Qt] 25.03.2019 22:03:53 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.248552508121514040263344871813"
[DEBUG][Qt] 25.03.2019 22:03:53 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:53 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.966354075876482042295761929295"
[DEBUG][Qt] 25.03.2019 22:03:53 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:54 [] (unknown:0) - New patient inserted: 46
[DEBUG][Qt] 25.03.2019 22:03:54 [] (unknown:0) - New patient inserted as :  46
[DEBUG][Qt] 25.03.2019 22:03:54 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.858893877330075891307460974850"
[DEBUG][Qt] 25.03.2019 22:03:54 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:54 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.108377250346249631601443486053"
[DEBUG][Qt] 25.03.2019 22:03:54 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:56 [] (unknown:0) - New patient inserted: 47
[DEBUG][Qt] 25.03.2019 22:03:56 [] (unknown:0) - New patient inserted as :  47
[DEBUG][Qt] 25.03.2019 22:03:56 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.928600880221753310061248736893"
[DEBUG][Qt] 25.03.2019 22:03:56 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:56 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.181100751603684262521895320396"
[DEBUG][Qt] 25.03.2019 22:03:56 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:57 [] (unknown:0) - New patient inserted: 48
[DEBUG][Qt] 25.03.2019 22:03:57 [] (unknown:0) - New patient inserted as :  48
[DEBUG][Qt] 25.03.2019 22:03:57 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.247213804717656850252490925334"
[DEBUG][Qt] 25.03.2019 22:03:57 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:57 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.257694099169946365430398843583"
[DEBUG][Qt] 25.03.2019 22:03:57 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:58 [] (unknown:0) - New patient inserted: 49
[DEBUG][Qt] 25.03.2019 22:03:58 [] (unknown:0) - New patient inserted as :  49
[DEBUG][Qt] 25.03.2019 22:03:58 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.188933890086471043002203871046"
[DEBUG][Qt] 25.03.2019 22:03:58 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:58 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.858665305863061871764636291385"
[DEBUG][Qt] 25.03.2019 22:03:58 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:03:59 [] (unknown:0) - New patient inserted: 50
[DEBUG][Qt] 25.03.2019 22:03:59 [] (unknown:0) - New patient inserted as :  50
[DEBUG][Qt] 25.03.2019 22:03:59 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.219900495822852419986671497215"
[DEBUG][Qt] 25.03.2019 22:03:59 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:03:59 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.177447273293879900929015869634"
[DEBUG][Qt] 25.03.2019 22:03:59 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:01 [] (unknown:0) - New patient inserted: 51
[DEBUG][Qt] 25.03.2019 22:04:01 [] (unknown:0) - New patient inserted as :  51
[DEBUG][Qt] 25.03.2019 22:04:01 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.851061538959703807827542270653"
[DEBUG][Qt] 25.03.2019 22:04:01 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:01 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.194126952887269510493034552293"
[DEBUG][Qt] 25.03.2019 22:04:01 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:02 [] (unknown:0) - New patient inserted: 52
[DEBUG][Qt] 25.03.2019 22:04:02 [] (unknown:0) - New patient inserted as :  52
[DEBUG][Qt] 25.03.2019 22:04:02 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.108892307565047668935473558485"
[DEBUG][Qt] 25.03.2019 22:04:02 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:02 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.326346544715454182651074735799"
[DEBUG][Qt] 25.03.2019 22:04:02 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:04 [] (unknown:0) - New patient inserted: 53
[DEBUG][Qt] 25.03.2019 22:04:04 [] (unknown:0) - New patient inserted as :  53
[DEBUG][Qt] 25.03.2019 22:04:04 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.192223804861576056024369880508"
[DEBUG][Qt] 25.03.2019 22:04:04 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:04 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.357245235701670723101804413792"
[DEBUG][Qt] 25.03.2019 22:04:04 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:06 [] (unknown:0) - New patient inserted: 54
[DEBUG][Qt] 25.03.2019 22:04:06 [] (unknown:0) - New patient inserted as :  54
[DEBUG][Qt] 25.03.2019 22:04:06 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.223114647221486834339942810753"
[DEBUG][Qt] 25.03.2019 22:04:06 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:06 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.256644935344040683824919640017"
[DEBUG][Qt] 25.03.2019 22:04:06 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:07 [] (unknown:0) - New patient inserted: 55
[DEBUG][Qt] 25.03.2019 22:04:07 [] (unknown:0) - New patient inserted as :  55
[DEBUG][Qt] 25.03.2019 22:04:07 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.233872568071694592857630274388"
[DEBUG][Qt] 25.03.2019 22:04:07 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:07 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.546493509930628296274751118533"
[DEBUG][Qt] 25.03.2019 22:04:07 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:08 [] (unknown:0) - New patient inserted: 56
[DEBUG][Qt] 25.03.2019 22:04:08 [] (unknown:0) - New patient inserted as :  56
[DEBUG][Qt] 25.03.2019 22:04:08 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.224592101182434229311031186058"
[DEBUG][Qt] 25.03.2019 22:04:08 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:08 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.326776744705831132952530466898"
[DEBUG][Qt] 25.03.2019 22:04:08 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:10 [] (unknown:0) - New patient inserted: 57
[DEBUG][Qt] 25.03.2019 22:04:10 [] (unknown:0) - New patient inserted as :  57
[DEBUG][Qt] 25.03.2019 22:04:10 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.280234577145640976141947438241"
[DEBUG][Qt] 25.03.2019 22:04:10 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:10 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.300937475543792074693364445656"
[DEBUG][Qt] 25.03.2019 22:04:10 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:11 [] (unknown:0) - New patient inserted: 58
[DEBUG][Qt] 25.03.2019 22:04:11 [] (unknown:0) - New patient inserted as :  58
[DEBUG][Qt] 25.03.2019 22:04:11 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.194806069120358144549293949080"
[DEBUG][Qt] 25.03.2019 22:04:11 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:11 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.607116685535995843554823064088"
[DEBUG][Qt] 25.03.2019 22:04:11 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:12 [] (unknown:0) - New patient inserted: 59
[DEBUG][Qt] 25.03.2019 22:04:12 [] (unknown:0) - New patient inserted as :  59
[DEBUG][Qt] 25.03.2019 22:04:12 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.316241214174868905194751342644"
[DEBUG][Qt] 25.03.2019 22:04:12 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:12 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.262962273919574275687811368173"
[DEBUG][Qt] 25.03.2019 22:04:12 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:14 [] (unknown:0) - New patient inserted: 60
[DEBUG][Qt] 25.03.2019 22:04:14 [] (unknown:0) - New patient inserted as :  60
[DEBUG][Qt] 25.03.2019 22:04:14 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.378450399989714541022204301518"
[DEBUG][Qt] 25.03.2019 22:04:14 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:14 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.729243044254570583133005972993"
[DEBUG][Qt] 25.03.2019 22:04:14 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:16 [] (unknown:0) - New patient inserted: 61
[DEBUG][Qt] 25.03.2019 22:04:16 [] (unknown:0) - New patient inserted as :  61
[DEBUG][Qt] 25.03.2019 22:04:16 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.311635966572418715302622159361"
[DEBUG][Qt] 25.03.2019 22:04:16 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:16 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.218975768694320541488737374474"
[DEBUG][Qt] 25.03.2019 22:04:16 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:17 [] (unknown:0) - New patient inserted: 62
[DEBUG][Qt] 25.03.2019 22:04:17 [] (unknown:0) - New patient inserted as :  62
[DEBUG][Qt] 25.03.2019 22:04:17 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.258791025467107717549952052215"
[DEBUG][Qt] 25.03.2019 22:04:17 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:17 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.249790265424420499532684148743"
[DEBUG][Qt] 25.03.2019 22:04:17 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:19 [] (unknown:0) - New patient inserted: 63
[DEBUG][Qt] 25.03.2019 22:04:19 [] (unknown:0) - New patient inserted as :  63
[DEBUG][Qt] 25.03.2019 22:04:19 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.174752416535028436038836053946"
[DEBUG][Qt] 25.03.2019 22:04:19 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:19 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.332367356450026445862610984105"
[DEBUG][Qt] 25.03.2019 22:04:19 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:20 [] (unknown:0) - New patient inserted: 64
[DEBUG][Qt] 25.03.2019 22:04:20 [] (unknown:0) - New patient inserted as :  64
[DEBUG][Qt] 25.03.2019 22:04:20 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.286202242964262414175811821515"
[DEBUG][Qt] 25.03.2019 22:04:20 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:20 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.157350444067781191153251322487"
[DEBUG][Qt] 25.03.2019 22:04:20 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:22 [] (unknown:0) - New patient inserted: 65
[DEBUG][Qt] 25.03.2019 22:04:22 [] (unknown:0) - New patient inserted as :  65
[DEBUG][Qt] 25.03.2019 22:04:22 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.803397998355063686023109438391"
[DEBUG][Qt] 25.03.2019 22:04:22 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:22 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.325851233802697617990000642816"
[DEBUG][Qt] 25.03.2019 22:04:22 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:23 [] (unknown:0) - New patient inserted: 66
[DEBUG][Qt] 25.03.2019 22:04:23 [] (unknown:0) - New patient inserted as :  66
[DEBUG][Qt] 25.03.2019 22:04:23 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.138525986909732252421346117470"
[DEBUG][Qt] 25.03.2019 22:04:23 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:23 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.184331161898265797536679037106"
[DEBUG][Qt] 25.03.2019 22:04:23 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:25 [] (unknown:0) - New patient inserted: 67
[DEBUG][Qt] 25.03.2019 22:04:25 [] (unknown:0) - New patient inserted as :  67
[DEBUG][Qt] 25.03.2019 22:04:25 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.253056126926926164849057283847"
[DEBUG][Qt] 25.03.2019 22:04:25 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:25 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.388928335629903864121985226150"
[DEBUG][Qt] 25.03.2019 22:04:25 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:26 [] (unknown:0) - New patient inserted: 68
[DEBUG][Qt] 25.03.2019 22:04:26 [] (unknown:0) - New patient inserted as :  68
[DEBUG][Qt] 25.03.2019 22:04:26 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.320460374301563573628329637280"
[DEBUG][Qt] 25.03.2019 22:04:26 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:26 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.227287063806269076002068979333"
[DEBUG][Qt] 25.03.2019 22:04:26 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:28 [] (unknown:0) - New patient inserted: 69
[DEBUG][Qt] 25.03.2019 22:04:28 [] (unknown:0) - New patient inserted as :  69
[DEBUG][Qt] 25.03.2019 22:04:28 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.281350061153986532104891148002"
[DEBUG][Qt] 25.03.2019 22:04:28 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:28 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.222717809741020436235558472790"
[DEBUG][Qt] 25.03.2019 22:04:28 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:30 [] (unknown:0) - New patient inserted: 70
[DEBUG][Qt] 25.03.2019 22:04:30 [] (unknown:0) - New patient inserted as :  70
[DEBUG][Qt] 25.03.2019 22:04:30 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.135924640766121071722315644650"
[DEBUG][Qt] 25.03.2019 22:04:30 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:30 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.885953737796154243790528823078"
[DEBUG][Qt] 25.03.2019 22:04:30 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:31 [] (unknown:0) - New patient inserted: 71
[DEBUG][Qt] 25.03.2019 22:04:31 [] (unknown:0) - New patient inserted as :  71
[DEBUG][Qt] 25.03.2019 22:04:31 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.240191044353389722771211299721"
[DEBUG][Qt] 25.03.2019 22:04:31 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:31 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.480687834929077561103132587918"
[DEBUG][Qt] 25.03.2019 22:04:31 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:33 [] (unknown:0) - New patient inserted: 72
[DEBUG][Qt] 25.03.2019 22:04:33 [] (unknown:0) - New patient inserted as :  72
[DEBUG][Qt] 25.03.2019 22:04:33 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.204472883229145857680771972310"
[DEBUG][Qt] 25.03.2019 22:04:33 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:33 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.620040738965321821094509795118"
[DEBUG][Qt] 25.03.2019 22:04:33 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:34 [] (unknown:0) - New patient inserted: 73
[DEBUG][Qt] 25.03.2019 22:04:34 [] (unknown:0) - New patient inserted as :  73
[DEBUG][Qt] 25.03.2019 22:04:34 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.243097352990517043299166705830"
[DEBUG][Qt] 25.03.2019 22:04:34 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:34 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.124429021744741770821343524565"
[DEBUG][Qt] 25.03.2019 22:04:34 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:36 [] (unknown:0) - New patient inserted: 74
[DEBUG][Qt] 25.03.2019 22:04:36 [] (unknown:0) - New patient inserted as :  74
[DEBUG][Qt] 25.03.2019 22:04:36 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.235421247181116496076807967411"
[DEBUG][Qt] 25.03.2019 22:04:36 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:36 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.335061130682811200494806372259"
[DEBUG][Qt] 25.03.2019 22:04:36 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:38 [] (unknown:0) - New patient inserted: 75
[DEBUG][Qt] 25.03.2019 22:04:38 [] (unknown:0) - New patient inserted as :  75
[DEBUG][Qt] 25.03.2019 22:04:38 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.171212440157430459418132315336"
[DEBUG][Qt] 25.03.2019 22:04:38 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:38 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.210474902742206786896646008982"
[DEBUG][Qt] 25.03.2019 22:04:38 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:42 [] (unknown:0) - New patient inserted: 76
[DEBUG][Qt] 25.03.2019 22:04:42 [] (unknown:0) - New patient inserted as :  76
[DEBUG][Qt] 25.03.2019 22:04:42 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.322467995907076448427396699530"
[DEBUG][Qt] 25.03.2019 22:04:42 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:42 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.757906135929300183785285252738"
[DEBUG][Qt] 25.03.2019 22:04:42 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:43 [] (unknown:0) - New patient inserted: 77
[DEBUG][Qt] 25.03.2019 22:04:43 [] (unknown:0) - New patient inserted as :  77
[DEBUG][Qt] 25.03.2019 22:04:43 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.118971343230482216615654322951"
[DEBUG][Qt] 25.03.2019 22:04:43 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:43 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.411911859032422710586149276741"
[DEBUG][Qt] 25.03.2019 22:04:43 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:44 [] (unknown:0) - New patient inserted: 78
[DEBUG][Qt] 25.03.2019 22:04:44 [] (unknown:0) - New patient inserted as :  78
[DEBUG][Qt] 25.03.2019 22:04:44 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.400035228893251034032961747040"
[DEBUG][Qt] 25.03.2019 22:04:44 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:44 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.817039488118322614736494063645"
[DEBUG][Qt] 25.03.2019 22:04:44 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:46 [] (unknown:0) - New patient inserted: 79
[DEBUG][Qt] 25.03.2019 22:04:46 [] (unknown:0) - New patient inserted as :  79
[DEBUG][Qt] 25.03.2019 22:04:46 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.294146073179367570423565184119"
[DEBUG][Qt] 25.03.2019 22:04:46 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:46 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.289029811259950700918044216155"
[DEBUG][Qt] 25.03.2019 22:04:46 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:47 [] (unknown:0) - New patient inserted: 80
[DEBUG][Qt] 25.03.2019 22:04:47 [] (unknown:0) - New patient inserted as :  80
[DEBUG][Qt] 25.03.2019 22:04:47 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.275763013774423666595125337398"
[DEBUG][Qt] 25.03.2019 22:04:47 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:47 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.310786298605125936123363770421"
[DEBUG][Qt] 25.03.2019 22:04:47 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:48 [] (unknown:0) - New patient inserted: 81
[DEBUG][Qt] 25.03.2019 22:04:48 [] (unknown:0) - New patient inserted as :  81
[DEBUG][Qt] 25.03.2019 22:04:48 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.443635061226959308567626629836"
[DEBUG][Qt] 25.03.2019 22:04:48 [] (unknown:0) - Study Added
[DEBUG][Qt] 25.03.2019 22:04:48 [] (unknown:0) - Need to insert new series:  "1.3.6.1.4.1.14519.5.2.1.4320.7015.324614335142762859716329057359"
[DEBUG][Qt] 25.03.2019 22:04:48 [] (unknown:0) - Series Added
[DEBUG][Qt] 25.03.2019 22:04:50 [] (unknown:0) - "DICOM indexer has successfully processed 4044 files [90.95s]"
[INFO][Python] 25.03.2019 22:04:55 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:471) - Imported a DICOM directory, checking for extensions
[INFO][Python] 25.03.2019 22:04:59 [Python] (C:\Program Files\Slicer 4.10.1\bin\Python\slicer\util.py:1097) - The following data type is in your database:

  Segmentation Objects

The following extension is not installed, but may help you work with this data:

  QuantitativeReporting

You can install extensions using the Extension Manager option from the View menu.
[INFO][Stream] 25.03.2019 22:04:55 [] (unknown:0) - Imported a DICOM directory, checking for extensions
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) - The following data type is in your database:
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) -
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) -   Segmentation Objects
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) -
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) - The following extension is not installed, but may help you work with this data:
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) -
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) -   QuantitativeReporting
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) -
[INFO][Stream] 25.03.2019 22:04:59 [] (unknown:0) - You can install extensions using the Extension Manager option from the View menu.
[DEBUG][Qt] 25.03.2019 22:06:17 [] (unknown:0) - Switch to module:  ""
</pre>
</details>
<details>
<summary>
Logfile from my data</summary>
<pre>
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - Session start time .......: 2019-03-26 10:22:01
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - Slicer version ...........: 4.10.1 (revision 27931) win-amd64 - installed release
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - Memory ...................: 16309 MB physical, 20794 MB virtual
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 26.03.2019 10:22:01 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 26.03.2019 10:22:10 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 26.03.2019 10:22:11 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 26.03.2019 10:22:11 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 26.03.2019 10:22:11 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 26.03.2019 10:22:21 [] (unknown:0) - Switch to module:  "DICOM"
[CRITICAL][Stream] 26.03.2019 10:22:23 [] (unknown:0) - W: DcmItem: Invalid Element (0005,0005) found in data set
[CRITICAL][Stream] 26.03.2019 10:22:23 [] (unknown:0) - W: DcmItem: Invalid Element (0005,0006) found in data set
[CRITICAL][Stream] 26.03.2019 10:22:23 [] (unknown:0) - W: DcmItem: Invalid Element (0005,000b) found in data set
[DEBUG][Python] 26.03.2019 10:22:48 [Python] (C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 26.03.2019 10:22:48 [Python] (C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 2 multivolumes!
[DEBUG][Python] 26.03.2019 10:22:49 [Python] (C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 26.03.2019 10:22:49 [Python] (C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 1 multivolumes!
[INFO][Python] 26.03.2019 10:22:50 [Python] (C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM
[INFO][Stream] 26.03.2019 10:22:50 [] (unknown:0) - Loading with imageIOName: GDCM
[DEBUG][Qt] 26.03.2019 10:23:43 [] (unknown:0) - Switch to module:  "Volumes"
[DEBUG][Qt] 26.03.2019 10:24:21 [] (unknown:0) - Switch to module:  ""
</pre>
</details>

---

## Post #41 by @lassoan (2019-03-27 12:48 UTC)

<p>To see a DICOM image in Slicer, you need to first <em>import</em> the data set to the DICOM database, then select one or more series and <em>load</em> them.</p>
<p>The first log that you provided show <em>import</em> of QIN data set - it all looks good.</p>
<p>The second log contain <em>loading</em> of some data set. As I understand, you have problems with your data in the <em>import</em> step, so proably the log you attached is not the correct one. Please try again: choose a new location for your DICOM data to make sure you start from a clear database, restart Slicer, take note of the current time (so that you can later verify that you select the correct log file), drag-and-drop the folder that contains DICOM data to Slicer application window, choose DICOM import option, wait up to 15 minutes for the import to finish, if it is not completed, restart your computer (to make sure the log file is not locked by a running instance of Slicer), start Slicer, look up the log file that matches the time that you noted before (it should be the previous entry in the log file list), and copy the contents of that.</p>

---

## Post #42 by @petemq (2019-03-29 19:23 UTC)

<p>To finish up:</p>
<p>I have taken the right log. Somehow the import command (which would have been the last action in the log) did not start until Slicer crashed and is apparently also not represented in the log. In the QIN lung database it worked slow, but fine (as the log shows).</p>
<p>I tried importing the files into microDicom, which worked fine and took about 4 minutes for the whole 850 images. Then I exported them into a new DICOM database and tried importing that into Slicer. That worked, but microDicom disfigured the headers, so the data was unusable.</p>
<p>After that I tried splitting the database into small packages of about 50 images each, and that finally did the trick. Slicer still becomes irresponsive for the time of importing and is incredibly slow (cumulated time ~7h for ~800 images, link only), but at least it works.</p>

---

## Post #43 by @fedorov (2019-03-29 19:36 UTC)

<aside class="quote no-group" data-username="petemq" data-post="42" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f4b2a3/48.png" class="avatar"> petemq:</div>
<blockquote>
<p>Slicer still becomes irresponsive for the time of importing and is incredibly slow (cumulated time ~7h for ~800 images, link only), but at least it works.</p>
</blockquote>
</aside>
<p>I would argue this is opposite from “it works” … At the same time, if a user considers Slicer is that valuable that it is worth the wait of 7 hours to import images - it speaks volumes about Slicer importance!</p>
<p>I would suggest a screenshare to debug this, but I don’t think I know enough about Windows to be of much help.</p>

---

## Post #44 by @lassoan (2019-03-29 19:44 UTC)

<aside class="quote no-group" data-username="petemq" data-post="42" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f4b2a3/48.png" class="avatar"> petemq:</div>
<blockquote>
<p>After that I tried splitting the database into small packages of about 50 images each, and that finally did the trick.</p>
</blockquote>
</aside>
<p>Can you send the log of one of these sessions? My experience is that Slicer can import a few hundred slices per minute. You seem to have magnitudes slower speed than that which should be possible to fix. My suspicion is that some fields might be malformed and a lot of warning/error messages are printed, which slows down the process. Getting the log file could confirm this or indicate what other problems might be with this data set.</p>

---

## Post #45 by @pieper (2019-03-29 20:00 UTC)

<p>Yes, it would be good to know if this can be replicated.</p>
<p>It would be interesting to know if it’s the QFileIterator or the actual addListOfFiles that is slow.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMIndexer.cpp#L102-L168" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMIndexer.cpp#L102-L168" target="_blank" rel="nofollow noopener">commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMIndexer.cpp#L102-L168</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="102" style="counter-reset: li-counter 101 ;">
<li>//------------------------------------------------------------------------------</li>
<li>void ctkDICOMIndexer::addDirectory(ctkDICOMDatabase&amp; database,</li>
<li>                                   const QString&amp; directoryName,</li>
<li>                                   const QString&amp; destinationDirectoryName,</li>
<li>                                   bool includeHidden/*=true*/)</li>
<li>{</li>
<li>  ctkDICOMIndexer::ScopedIndexing indexingBatch(*this, database);</li>
<li>  QStringList listOfFiles;</li>
<li>  QDir directory(directoryName);</li>
<li>
</li>
<li>  if(directory.exists("DICOMDIR"))</li>
<li>  {</li>
<li>    addDicomdir(database,directoryName,destinationDirectoryName);</li>
<li>  }</li>
<li>  else</li>
<li>  {</li>
<li>    QDir::Filters filters = QDir::Files;</li>
<li>    if (includeHidden)</li>
<li>    {</li>
<li>      filters |= QDir::Hidden;</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMIndexer.cpp#L102-L168" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #46 by @petemq (2019-03-29 20:08 UTC)

<p>Not just important, essential<br>
<img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20">.</p>
<p>In a way, apart from the slow import it does everything is supposed to, and I don’t need to import images that often. So, yes, worth the tradeoff.</p>
<p>I don’t know if a screenshare will be possible. We work with identified patient data, and I would probably need to delete the database before I can make sure there’s no privacy concerns. You can<br>
probably see why I’m reluctant to do that. If somebody is willing and able to help, I can discuss it with my supervisor. Or maybe we can find a workaround for that.</p>
<p>As for the log files, The successful import logs are no longer in the “recent logs” list; is there a way to access older logs or are they deleted? If so, I’ll make sure to grab a log the next time<br>
I import data.</p>
<p>We recognised that the problem persisted when we tried to import the dataset into slicer on another windows pc, but worked fine on our old Imac. So I too assume that the dataset itself is a source<br>
of error. We exported the DICOM database through Osirix on our Imac using default options. I know that expertise on two platforms and programs is a lot to ask for, but maybe there is an option we need to check/uncheck?</p>
<p>Thank you so much for helping!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/9/934f3c8dbe3f04a74d14dab937e5097d12933d1d.jpeg" width="35" height="35"></p>

---

## Post #47 by @lassoan (2019-03-29 20:21 UTC)

<aside class="quote no-group" data-username="petemq" data-post="46" data-topic="4660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f4b2a3/48.png" class="avatar"> petemq:</div>
<blockquote>
<p>As for the log files, The successful import logs are no longer in the “recent logs” list; is there a way to access older logs or are they deleted? If so, I’ll make sure to grab a log the next time<br>
I import data.</p>
</blockquote>
</aside>
<p>Only the last 10 or so log files are preserved, so you need to re-import to generate the logs again (unless you can find the deleted files in your recycling bin).</p>

---
