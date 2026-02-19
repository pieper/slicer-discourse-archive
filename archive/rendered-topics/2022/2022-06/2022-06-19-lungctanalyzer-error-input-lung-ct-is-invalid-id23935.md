---
topic_id: 23935
title: "Lungctanalyzer Error Input Lung Ct Is Invalid"
date: 2022-06-19
url: https://discourse.slicer.org/t/23935
---

# LungCTAnalyzer error: Input lung CT is invalid

**Topic ID**: 23935
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/lungctanalyzer-error-input-lung-ct-is-invalid/23935

---

## Post #1 by @ashipde (2022-06-19 04:11 UTC)

<p>Hello, I am a novice user of 3D Slicer and trying to use version 5.0.2 of the software in macOS 10.12.</p>
<p>For a CT that I am looking at, I could get segmentation done, but at the next step, Analyzer shows error message: <em>Failed to compute results: Input lung CT is invalid.</em> When I click the OK button on the message, I see a message <em>Starting processing - 0%</em> but nothing happens. What may be the reason? I see the same error with <em>Load Covid-19 demo</em> data.</p>
<p><img src="https://user-images.githubusercontent.com/16885020/174464404-0efd3495-1af0-4885-a8fe-7f256aba6e1e.jpg" alt="error" width="690" height="471"></p>
<p>(sorry for double posting here and <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/issues/32" rel="noopener nofollow ugc">GitHub</a>; I noticed later that the GitHub project page suggests using this community)</p>

---

## Post #2 by @ashipde (2022-06-19 07:01 UTC)

<p>Sorry, it is macOS 12.2 and not 10.12.</p>

---

## Post #3 by @rbumm (2022-06-19 07:18 UTC)

<p>Hello,<br>
I just tested again on a Windows 11 PC with Slicer 5.0.2 and Lung CT Analyzer V 2.49</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/802077cdf0faf5abb673292ef4827c9fa6fd99aa.png" data-download-href="/uploads/short-url/ihsG4n8whlxlWBrwuaxDlN9BvSi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802077cdf0faf5abb673292ef4827c9fa6fd99aa_2_690x289.png" alt="image" data-base62-sha1="ihsG4n8whlxlWBrwuaxDlN9BvSi" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802077cdf0faf5abb673292ef4827c9fa6fd99aa_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802077cdf0faf5abb673292ef4827c9fa6fd99aa_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802077cdf0faf5abb673292ef4827c9fa6fd99aa_2_1380x578.png 2x" data-dominant-color="AAAAAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1905×800 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There are no such error messages.<br>
The one thing that comes to my mind: I do not see the Lung CT Analyzer version number on your screenshot.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41e43fca125c14350dd3e013552ac6c7bb931e39.png" alt="image" data-base62-sha1="9oU3xOYWRQLirntQec7fyuUjPy9" width="163" height="113"></p>
<p>Are you maybe using an outdated version of the extension?</p>

---

## Post #4 by @ashipde (2022-06-19 07:34 UTC)

<p>Thanks for the quick response. I also noticed the missing version identifier. I used the extension manager within 5.0.2 to install Chest Imaging Platform (CIP) and Lung CT Analyzer a couple of days ago, and for the analysis I used CIP &gt; Lung CT Analyzer. I will try updating the extensions.</p>

---

## Post #5 by @rbumm (2022-06-19 07:36 UTC)

<p>Maybe something has gone wrong with that install on the mac.<br>
You could remove the Lung CT Analyzer extension and restart Slicer. Check that it is gone.</p>
<p>Then, clone the Lung CT Analyzer Github version by</p>
<pre><code class="lang-auto">git clone https://github.com/rbumm/SlicerLungCTAnalyzer.git
</code></pre>
<p>into a directory of your choice.</p>
<p>Then go to Slicers “Application settings”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6da8f156afc8cbb9329e874b5979d8e3043e8b8.png" data-download-href="/uploads/short-url/wWe4RS8jLKOKbXr8n3UOzw0Vudy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6da8f156afc8cbb9329e874b5979d8e3043e8b8.png" alt="image" data-base62-sha1="wWe4RS8jLKOKbXr8n3UOzw0Vudy" width="542" height="499" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×619 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and manually add two folders here:</p>
<p>LungCTSegmenter<br>
LungCTAnalyzer</p>
<p>Restart Slicer. This should give you the most recent version of the extension.</p>

---

## Post #6 by @ashipde (2022-06-19 07:37 UTC)

<p>Thanks. Will do and report within a day.</p>

---

## Post #7 by @lassoan (2022-06-19 13:59 UTC)

<p>I’ve tried 5.0.2 on macOS using the <code>DemoChestCT</code> sample data set and everything worked perfectly. The version string (V 2.49) appears for me.</p>
<p>I don’t think we need to experiment with manual download of the repository and adding them as additional module paths, because it may lead to more complications (there are a lot of possibilities for user errors in manual installation).</p>
<p>Instead, I would recommend to check the application log for any errors. Also, try if segmentation and analysis work with the <code>DemoChestCT</code> sample data set.</p>

---

## Post #8 by @rbumm (2022-06-19 19:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="23935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t think we need to experiment with manual download</p>
</blockquote>
</aside>
<p>Agree - this was just to show how it could be troubleshot. Generally, it would be better to use the extension manager.</p>

---

## Post #9 by @ashipde (2022-06-19 20:52 UTC)

<p>Unfortunately I am still seeing the same issues – <em>invalid input CT</em>, and no version number – with both my and the Covid-19 demo CTs under <strong>four different installation settings</strong>:</p>
<ol>
<li>
<p>Removing the extension and reinstalling from GitHub as <a href="https://discourse.slicer.org/t/lungctanalyzer-error-input-lung-ct-is-invalid/23935/5">suggested</a> in Dr. Bumm.</p>
</li>
<li>
<p>Completely removing the Slicer app (with App Cleaner to remove any ancillary file), reinstalling Slicer 5.0.2 using the macOS installer DMG from Slicer download site, and installing just the Lung Segmenter and Analyzer as in <span class="hashtag">#1</span>.</p>
</li>
<li>
<p>As <span class="hashtag">#2</span> but using Homebrew  to install Slicer 5.0.2.</p>
</li>
<li>
<p>As <span class="hashtag">#2</span> but using Extension Manager to install LungCTAnalyzer.</p>
</li>
</ol>
<p>The Slicer app’s  <strong>error log</strong> (for <span class="hashtag">#4</span> setting with Covid-19 demo CT):</p>
<pre><code class="lang-auto">This will clear all data in the scene. Do you want to continue?
Clearing the scene
Registering the sample data
Downloading COVID Chest CT dataset
&lt;b&gt;Verifying checksum&lt;/b&gt;
&lt;b&gt;File already exists and checksum is OK - reusing it.&lt;/b&gt;
&lt;b&gt;Requesting load&lt;/b&gt; &lt;i&gt;DemoChestCT&lt;/i&gt; from /Users/ashipde/Library/Caches/NA-MIC/Slicer/SlicerIO/DemoChestCT.nrrd ...
Clearing the scene
Registering the sample data
Downloading COVID Chest CT dataset
Loaded volume from file: /Users/ashipde/Library/Caches/NA-MIC/Slicer/SlicerIO/DemoChestCT.nrrd. Dimensions: 490x490x361. Number of components: 1. Pixel type: short.


"Volume" Reader has successfully read the file "/Users/ashipde/Library/Caches/NA-MIC/Slicer/SlicerIO/DemoChestCT.nrrd" "[0.99s]"
&lt;b&gt;Load finished&lt;/b&gt;
Downloading COVID Lung Mask segmentation
&lt;b&gt;Verifying checksum&lt;/b&gt;
&lt;b&gt;File already exists and checksum is OK - reusing it.&lt;/b&gt;
&lt;b&gt;Requesting load&lt;/b&gt; &lt;i&gt;DemoLungMasks&lt;/i&gt; from /Users/ashipde/Library/Caches/NA-MIC/Slicer/SlicerIO/DemoLungMasks.seg.nrrd ...
Downloading COVID Lung Mask segmentation
"Segmentation" Reader has successfully read the file "/Users/ashipde/Library/Caches/NA-MIC/Slicer/SlicerIO/DemoLungMasks.seg.nrrd" "[1.62s]"
&lt;b&gt;Load finished&lt;/b&gt;
Centering.
Normal end of loading procedure.
Centering.
Normal end of loading procedure.
Apply
Processing started.
Apply
Processing started.
Failed to compute results: Input lung CT is invalid
Failed to compute results: Input lung CT is invalid
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 853, in onApplyButton
    self.logic.process()
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 2135, in process
    raise ValueError("Input lung CT is invalid")
ValueError: Input lung CT is invalid
</code></pre>
<p>My <strong>system</strong>: macOS 12.2.1 with XCode 13.4.1, Intel Core i9 3.6 GHz 8-core, 48 GB DDR4, Radeon Pro 580X 8 GB; Slicer app has full data access privilege in macOS Preferences.</p>

---

## Post #10 by @rbumm (2022-06-20 14:33 UTC)

<p>Thank you <a class="mention" href="/u/ashipde">@ashipde</a>. Could you restart Slicer and enable the Python interactor for a test, then run Lung CT Analyzer?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a8989c0c17e61a1bfec4aa9ff95e436c2f5174c.png" alt="image" data-base62-sha1="cUVE4AxXt2NL02ykD0Ne3VP2nBW" width="358" height="230"></p>
<p>Do you see any exceptions/error messages in the interactor?</p>

---

## Post #11 by @ashipde (2022-06-20 23:00 UTC)

<p>Thank you Dr. Bumm. Using the <em>Interactor</em> as you suggested helps us identify a possible cause: a file permission issue.</p>
<p>My computer is at an institution and managed by IT, though I have admin rights. The Slicer installer (dmg) had installed Slicer.app with <em>drwxr-xr-x</em> permission.</p>
<p>To possibly solve the issue, I set permissions to 777 for /Applications/Slicer.app, /Applications/Slicer.app/Contents, ~/Documents/SlicerDICOMDatabase, and ~/Documents/LungCTAnalyzerReports.</p>
<p>But the problem remains.</p>
<p>Below is message log from Python interactor from one session. I have annotated it with my actions.</p>
<pre><code class="lang-auto">/////// Start

Python 3.9.10 (main, May  6 2022, 02:57:10) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
&gt;&gt;&gt; 

/////// Load – my CT DICOM

Loading with imageIOName: GDCM

/////// Switch module selector in top menu to Lung CT Segmenter &gt; Start &gt; Apply

StartSegmentation completed in 1.09 seconds
self.extentGrowthRatio = 0.5
masterImageExtent = (0, 174, 0, 174, 0, 142)
labelsEffectiveExtent = (34, 148, 56, 132, 62, 133)
labelsExpandedExtent = [0, 174, 18, 170, 27, 142]
Grow-cut operation on volume of 175x153x116 voxels was completed in 0.5 seconds.
Saving markups in temp directory ...
ApplySegmentation completed in 8.02 seconds

/////// Switch module selector in top menu to Lung CT Analyzer &gt; (Input volume/segmentation already selected) &gt; Computer results

Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 211, in setup
    with open('LCTA.INI', 'w') as configfile:    # save
OSError: [Errno 30] Read-only file system: 'LCTA.INI'
Directory changed
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 895, in onReportDirectoryChanged
    with open('LCTA.INI', 'w') as configfile:    # save
OSError: [Errno 30] Read-only file system: 'LCTA.INI'
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 337, in enter
    self.initializeParameterNode()
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 375, in initializeParameterNode
    self.setParameterNode(self.logic.getParameterNode())
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 415, in setParameterNode
    self.updateGUIFromParameterNode()
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 462, in updateGUIFromParameterNode
    self.ui.checkForUpdatesCheckBox.checked = self.checkForUpdates
AttributeError: 'LungCTAnalyzerWidget' object has no attribute 'checkForUpdates'

//////// Download and examine demo CT – Within Lung CT Analyzer module window &gt; Load Demo Covid-19 data &gt;  Compute results

This will clear all data in the scene. Do you want to continue?
Clearing the scene
Registering the sample data
Downloading COVID Chest CT dataset
Downloading COVID Lung Mask segmentation
Centering.
Normal end of loading procedure.
Apply
Processing started.
Failed to compute results: Input lung CT is invalid
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 853, in onApplyButton
    self.logic.process()
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 2135, in process
    raise ValueError("Input lung CT is invalid")
ValueError: Input lung CT is invalid

//////// Again download demo CT (but not analyze) – Within Lung CT Analyzer module window &gt; Load Demo Covid-19 data

This will clear all data in the scene. Do you want to continue?
Clearing the scene
Registering the sample data
Downloading COVID Chest CT dataset
Downloading COVID Lung Mask segmentation
Centering.
Normal end of loading procedure.

//////// Try other module commands – Within Lung CT Analyzer module window &gt; Report directory &gt; Change report directory

Open Directory
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 880, in onOpenReportDirectoryButton
    subprocess.Popen(f'explorer {os.path.realpath(self.reportFolder)}')
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/subprocess.py", line 1821, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'explorer /Users/ashipde/Documents/LungCTAnalyzerReports'

/// Folder '/Users/ashipde/Documents/LungCTAnalyzerReports' exists

//////// Try other module commands – Within Lung CT Analyzer module window &gt; Report directory &gt; Open report directory

Directory changed
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py", line 895, in onReportDirectoryChanged
    with open('LCTA.INI', 'w') as configfile:    # save
OSError: [Errno 30] Read-only file system: 'LCTA.INI'

</code></pre>

---

## Post #12 by @pieper (2022-06-20 23:30 UTC)

<aside class="quote no-group" data-username="ashipde" data-post="11" data-topic="23935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ashipde/48/15695_2.png" class="avatar"> ashipde:</div>
<blockquote>
<p><code>OSError: [Errno 30] Read-only file system</code></p>
</blockquote>
</aside>
<p>Yes, the mac now has several safety features that can make things difficult, like read-only volumes.  Try moving the Slicer.app folder to your home directory.  It should run fine out of there and be able to store files.</p>

---

## Post #13 by @lassoan (2022-06-21 01:48 UTC)

<aside class="quote no-group quote-modified" data-username="ashipde" data-post="11" data-topic="23935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ashipde/48/15695_2.png" class="avatar"> ashipde:</div>
<blockquote>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-30822/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTAnalyzer.py”, line 211, in setup<br>
with open(‘LCTA.INI’, ‘w’) as configfile:    # save<br>
OSError: [Errno 30] Read-only file system: ‘LCTA.INI’<br>
Directory changed</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/rbumm">@rbumm</a> I would recommend not to try to create files in such locations (where code is stored). Instead, use the folders provided by the application or the scene:</p>
<ul>
<li><code>slicer.app.temporaryPath</code>: for data that will not be preserved after restarting Slicer, suitable for large data (images, etc.)</li>
<li><code>slicer.app.cachePath</code>: for data that will be preserved after restarting Slicer, but will be removed when more recent data is added to the cache and the cache size limit is reached, suitable for large data (images, etc.)</li>
<li><code>slicer.app.slicerUserSettingsFilePath</code>: folder of this file is good for storing data that needs to be persistently stored; suitable for small data, such as configuration information, but not for bulk data (images, etc.)</li>
<li><code>slicer.app.defaultScenePath</code>: default location for exported data or reports; the best is to only use this as default and let the user specify a different folder</li>
<li><code>slicer.mrmlScene.GetRootDirectory()</code>: current scene file location, for exported data or reports</li>
</ul>
<p>Also, I would not recommend to create a separate ini file (<code>LCTA.INI</code>) for your module but instead use all your settings in <code>Slicer.ini</code> (via <code>slicer.app.userSettings()</code> object). Slicer settings would become very difficult to manage if each module maintained its settings in a separate ini file.</p>

---

## Post #14 by @ashipde (2022-06-21 01:56 UTC)

<p><span class="mention">@piper</span> The issue <em>also</em> occurs with Slicer app in my user directory. Note that the Lung CT Segmenter part of the LungCTAnalyzer extension works but the Lung CT Analyzer part fails. Another extension, DensityLungSegmentation, that I tried works fine with my and the demo Covid-19 data.</p>
<p>The LungCTAnalyzer extension works well with my CTs  in Windows 10, so the issue is macOS-specific. I also updated macOS from 12.2 to 12.4 but it didn’t help.</p>

---

## Post #15 by @lassoan (2022-06-21 02:00 UTC)

<p><a class="mention" href="/u/ashipde">@ashipde</a> as a workaround, you can probably simply comment out the offending lines. For example, it won’t cause much trouble if your settings are not saved in the private .ini file.</p>

---

## Post #16 by @ashipde (2022-06-21 02:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you for the suggestion. I commented out the <em>LCTA.INI</em> calls in <em>LungCTAnalyzer.py</em> (8 lines) and I was able to get LungCTAnalyzer to perform the analysis.</p>

---

## Post #17 by @ashipde (2022-06-21 06:20 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Dr. Bumm, I am actually planning to use the LungCTAnalyzer to quantify ILD progression over a period of two years. There are 9 CT scans, from different CT imagers and of varying slice thickness, but same position, supine, and respiratory phase, inspiratory. Will my use of the software be appropriate?</p>

---

## Post #18 by @rbumm (2022-06-21 08:47 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for the recommendations.</p>
<p>Will put LCTA.ini into slicer.app.slicerUserSettingsFilePath in an update folloing today and use Slicer.ini as soon as I figure that out.</p>

---

## Post #19 by @rbumm (2022-06-21 08:52 UTC)

<p>Yes, the Lung CT Analyzer should be sufficient in ILD if you select the appropriate thresholds.<br>
I have mainly used LCTA for COVID-19 data until now but would be very interested to see how this works in ILD.<br>
BTW Thanks you for doing all those tests on your MAC !</p>

---

## Post #20 by @lassoan (2022-06-21 17:05 UTC)

<aside class="quote no-group" data-username="ashipde" data-post="17" data-topic="23935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ashipde/48/15695_2.png" class="avatar"> ashipde:</div>
<blockquote>
<p>from different CT imagers and of varying slice thickness, but same position, supine, and respiratory phase, inspiratory. Will my use of the software be appropriate?</p>
</blockquote>
</aside>
<p>Different CT scanner should not make any difference. Different slice thickness may make small differences, but probably not more than a few percent.</p>
<p>If you want to estimate the possible effects of different slice thickness, you can resample a volume at different resolutions (for example, using “Crop volume” module) and see how much difference it makes in the analysis results.</p>

---

## Post #21 by @rbumm (2022-06-21 19:09 UTC)

<p>Hi <a class="mention" href="/u/ashipde">@ashipde</a>,<br>
it would be great if you could do another test with an update to Lung CT Analyzer I pushed to Github today. It should be automatically available as an update in the extension manager tomorrow or the day after and should hopefully fix the issue with LTCA.ini you experienced. No hurry, just to be sure that the permission error has been solved. It should show V 2.50</p>
<p>Concerning your ILD study I will be glad to help, even may be able to provide a few ILD cases if you are interested.</p>
<p>Thank you</p>

---

## Post #22 by @ashipde (2022-06-21 20:03 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Dr. Bumm, the updated extension on GitHub works well. The version number for Analyzer also gets displayed now (as 2.49). I will test the in-app extension once it gets available (new version not yet there, at 8 pm UTC).</p>
<p>I thank you and Dr. Lasso for the suggestions and offer of help for the ILD analysis, and I may request advice/help.</p>

---

## Post #23 by @ashipde (2022-06-27 02:58 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Dr. Bumm, two questions:</p>
<p>(1) Can LungCTAnalyzer be used on multiple CT series of same subject sequentially, or does one have to delete some nodes in between different CTs, or restart the app altogether? I am asking because, in my system, some nodes like results and masked volume that are created after examination of a series get put directly under subject and not the CT series in the node hierarchy.</p>
<p>(2) Is rescaling of any sort is needed before using LungCTAnalyzer, and if I were to leave default module thresholds, will my results be to inaccurate or just off by a minor fraction?</p>

---

## Post #24 by @rbumm (2022-06-27 07:25 UTC)

<p>(1) You can analyze a series of CT data (f.e. within a directory) and save the result to a CSV file line by line automatically. However, you would need to segment the lung masks for each volume beforehand. Please have a look at <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/tree/master/PythonScripts" class="inline-onebox">SlicerLungCTAnalyzer/PythonScripts at master · rbumm/SlicerLungCTAnalyzer · GitHub</a>.</p>
<p>(2) this depends on your data. If it is all from one CT machine I would leave the thresholds as they are.</p>

---

## Post #25 by @ashipde (2022-06-27 22:53 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Thank you Dr. Bumm for the suggestions. Regarding thresholding, is it then an ‘art’ that one learns by experience, or are there some sound principles that one can use? I am asking this because I am trying to use multiple CTs from different machines to attempt to track ILD progression. Thank you.</p>

---

## Post #26 by @rbumm (2022-06-28 09:09 UTC)

<p>Not exactly an “art” … I would suggest defining the range of the sliders in Lung CT Analyzer in a way that the preview covers the interstitial abnormalities as best as possible with the ranges of “Infiltrated” and “Collapsed”. Find a compromise here, and maybe discuss it with your radiologist. Then run the analysis with unchanged sliders over all datasets and evaluate the difference between the initial and follow-up data (% change) for each individual patient. Would be really cool if you could quantify a progression that way.<br>
Hope that helps …</p>

---

## Post #27 by @ashipde (2022-06-29 06:33 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Dr. Bumm, will contrast affect LungCTAnalyzer analysis. If so, which aspect - infiltrate, consolidation, etc. - is likely to get exaggerated? Please also comment on the effect of depth of inspiration.</p>

---
