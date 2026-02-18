# Cancellous bone fill for 3D printing?

**Topic ID**: 8952
**Date**: 2019-10-30
**URL**: https://discourse.slicer.org/t/cancellous-bone-fill-for-3d-printing/8952

---

## Post #1 by @Slim (2019-10-30 02:45 UTC)

<p>Hi everyone!</p>
<p>I’ve been using 3D Slicer for a little while now and I love the program. However, I can’t help but feel that I can be reducing the amount of time I spend creating .STL files for 3D printing. I primarily work with bones, specifically the visualization of complex fractures, and here is my current workflow:</p>
<ol>
<li>Upload the DICOM and crop appropriate ROI</li>
<li>Create a segment for the bone of interest (such as the pelvis and part of the sacrum/lumbar spine)</li>
<li>Change thresholds until almost all of the cortical bone (the perimeter/shell of what I want to be printed) is covered</li>
<li>Go through each individual slice one-by-one, painting and erasing as necessary until the final product is created and a complete model is generated</li>
</ol>
<p>As you can imagine… this is <em>incredibly</em> time consuming. But I’ve had a lot of difficulty following some of the instructions or videos online…</p>
<p>Can anyone outline a “foolproof” methodology that may yield better results? I think the big issue for me is getting all of the cancellous bone (which will ultimately need to be filled for the 3D printing process) after I have my perimeter/shell defined. I recently downloaded the BoneExtension add-on because I saw a photo that shows a “before and after” use of the extension and it seems like what I want (cancellous bone filling) but I have no idea what buttons to check/what operations to perform. Would this method yield better results than seeding? Is there a way to seed the “inside” of what the perimeter I’ve defined so that the inside would essentially fill until it “meets” and touches the perimeter (cortical bone)?</p>
<p>Thanks for taking the time to read this. I’m open to any tips and tricks. Hopefully I can improve my prints and reduce the amount of time spent creating them.</p>

---

## Post #2 by @lassoan (2019-10-30 03:46 UTC)

<p>This is a very common need and there are a couple of approaches that are less time-consuming than manual segmentation on individual slices. You can get some tips here and from similar topics on this forum: <a href="https://discourse.slicer.org/t/after-threshold-based-bone-segmentation-in-ct-structure-filled-with-holes/7983/6" class="inline-onebox">After threshold-based bone segmentation in CT structure filled with holes</a></p>
<p>What exactly is “BoneExtension add-on” that you mentioned?</p>
<p>Probably the most automated bone hole filling method that is available for Slicer right now is in SurfaceWrapSolidify extension (Segment Editor - Wrap Solidify effect; Filter method: Deep hull; Output type: Segmentation). Have you tried it?</p>

---

## Post #3 by @Slim (2019-10-31 01:50 UTC)

<p>Hi Andras,</p>
<p>I will view the post you linked and give the SurfaceWrapSolidify extension a try! Where can I find it? I am looking through the Extensions Manager and GitHub and can’t seem to find it.</p>
<p>The extension is the “BoneTextureExtension” and I have no idea how to run it. I saw photos of its application in the description and it seems like what I needed but I wasn’t able to actually apply it.</p>
<p>I’ll reply soon with my results.</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2019-10-31 02:07 UTC)

<p>SurfaceWrapSolidify is available in extension manager for recent Slicer Preview Releases.</p>

---

## Post #5 by @Slim (2019-10-31 02:53 UTC)

<p>I am trying to load my DICOMs and it seems like, at the given pace, it might take a few hours… as opposed to the few seconds with the 4.10.2 version I have been using. Is this common with the Slicer Preview Release?</p>

---

## Post #6 by @lassoan (2019-10-31 03:02 UTC)

<p>DICOM import in latest Slicer preview release should be several times <em>faster</em> than in 4.10.2, not slower.</p>
<p>What operating system do you use?<br>
Have you created a new database?<br>
Can you upload somewhere the application log (menu: Help / Report a bug) and post the link?  (make sure no patient identifiable information is included in the log)</p>

---

## Post #7 by @Slim (2019-10-31 03:15 UTC)

<p>Usually I just drag and drop the folder containing the DICOMs from my desktop into one of the four views in 4.10.2, it will ask me the directory to load, and then I’m able to access it almost immediately. I’m running Windows 10 Home and downloaded the 64-bit version from the website. I’m not entirely sure if I’ve created a new database. Every time I click the “DCM” button at top left or the “Load DICOM Data” the program crashes/closes out.</p>
<p>As I type this I am on 26% download and the program says (Not Responding) and I am not able to click the Help / Report a bug. In fact, it just closed down… any idea what is going on?</p>
<p>Also, how do you change the contrast in the windows? Before, I would left click and move around to alter the contrast. Now I can’t seem to do it with the left click but can still zoom in and out with right click and pan with the middle mouse button.</p>

---

## Post #8 by @lassoan (2019-10-31 03:31 UTC)

<p>Do you use the latest Slicer Preview Release (2019-10-29)?</p>
<aside class="quote no-group" data-username="Slim" data-post="7" data-topic="8952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b5e925/48.png" class="avatar"> Slim:</div>
<blockquote>
<p>As I type this I am on 26% download</p>
</blockquote>
</aside>
<p>There should be no download operation at all. What message do you see exactly?</p>
<aside class="quote no-group" data-username="Slim" data-post="7" data-topic="8952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b5e925/48.png" class="avatar"> Slim:</div>
<blockquote>
<p>As I type this I am on 26% download and the program says (Not Responding) and I am not able to click the Help / Report a bug. In fact, it just closed down… any idea what is going on?</p>
</blockquote>
</aside>
<p>In menu: Help/Report a bug, you can choose to see the log of the previous 10 or so sessions. Choose the previous one from the list (the one that was closed during DICOM import or loading).</p>
<p>Restart your computer to make sure you have no remaining Slicer instances in the background and try again.</p>
<aside class="quote no-group" data-username="Slim" data-post="7" data-topic="8952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b5e925/48.png" class="avatar"> Slim:</div>
<blockquote>
<p>Also, how do you change the contrast in the windows?</p>
</blockquote>
</aside>
<p>This is a new feature. First you click on the toolbar to activate window/level mode and then you can click-and-drag to adjust window/level manually; Ctrl + click-and-drag to optimize window/level to the selected region; or double-click to reset window/level.</p>

---

## Post #9 by @Slim (2019-10-31 03:44 UTC)

<p>Yes, I am using “4.11.0-2019-10-29”</p>
<p>I am clicking File &gt; DICOM and the program immediately closes. Instead, I tried to click File &gt; Add Data and when I select the corresponding folder on my desktop several Files populate and the majority of them have the description “Volume” and this is when it takes a very long time. I am assuming this is adding the DICOMs to the directory, no? The preview will often show random slices on different windows and it moves slowly until it’s complete, then it will move a percent up and more images will re-populate and so on. I will restart my computer now.</p>
<p>May I copy log messages to clipboard and private message you to make sure I am not posting any private information publicly?</p>
<p>I have found the window/level mode and I am a big fan! It looks like it will help to prevent accidental changes which I found myself doing quite often.</p>

---

## Post #10 by @lassoan (2019-10-31 03:54 UTC)

<aside class="quote no-group" data-username="Slim" data-post="9" data-topic="8952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b5e925/48.png" class="avatar"> Slim:</div>
<blockquote>
<p>File &gt; Add Data and when I select the corresponding folder on my desktop several Files populate</p>
</blockquote>
</aside>
<p>Add Data should not be used for DICOM files, as its capabilities are very limited, it can only load only images, and only certain types. If you want to try it then you need to select only 1 file of the series (not multiple files or a folder), click “Show options”, and uncheck “Single file” option.</p>
<p>The main issue is that the program closes when you open the DICOM module. We recently completely reworked the DICOM module to make it much faster and more convenient, and nobody has complained so far, but there may be some configuraitons that we haven’t tested. You can send me the log file of the session where Slicer closed in a private message (click on my name and then on the email icon). Restart your computer before you test the DICOM module again to make sure there are no Slicer instances that stuck running in the background.</p>

---

## Post #11 by @Leon (2019-10-31 12:17 UTC)

<p>@ <a href="https://discourse.slicer.org/u/Slim">Slim</a><br>
If your goal is only to print the (fractured) bones, then I would do it like this:</p>
<ul>
<li>Segment only the cortical layer.</li>
<li>Make sure that all openings to ‘the outside world’ are closed. For instance if you have a bone shaft, close the proximal and distal end and make sure that there are no holes left open.</li>
<li>Invert the mask.</li>
<li>Go to Island and select ‘Keep selected island’.</li>
<li>Click on the inverted mask.</li>
<li>Invert the mask back to it’s original.</li>
</ul>

---

## Post #12 by @Slim (2019-11-01 00:58 UTC)

<p>I have uninstalled 4.10.2 and reinstalled the latest Slicer Preview Release (2019-10-30*) with no success. I am still having the same issue where the DCM and Load DICOM Data buttons are closing the application. I am sending you a private message now with the error code.</p>

---

## Post #13 by @lassoan (2019-11-01 04:19 UTC)

<p>We’ve investigated this and found that the crash was caused by invalid DICOM database. Changing the database folder to an empty folder fixed the issue.</p>
<p>We don’t know what corrupted the database, but we’ll keep an eye on it and investigate more if it happens again.</p>
<p>To make it easier to change database folder location without opening the DICOM module, a database folder selector was added to application settings (DICOM section).</p>

---

## Post #14 by @sandress (2019-11-05 09:25 UTC)

<p>This is a very good application for our WrapSolidify filter. If you follow the steps at the bottom of the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#workflow-example" rel="nofollow noopener">github page</a>, you should be able to quite easily remove cancellous structures and speed up printing time (for our acetabular fractured hemipelvices about 70%). It will be more intuitive in the future, too.</p>

---

## Post #15 by @lassoan (2019-11-05 20:44 UTC)

<aside class="quote no-group" data-username="sandress" data-post="14" data-topic="8952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f475e1/48.png" class="avatar"> sandress:</div>
<blockquote>
<p>It will be more intuitive in the future, too.</p>
</blockquote>
</aside>
<p>It would be great if you could make the few <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/issues/2">UI tweaks that we discussed</a>, it would make a huge difference in usability.</p>

---

## Post #16 by @sandress (2019-11-15 20:04 UTC)

<p>We tweaked the UI and made everything a little easier to use (hopefully). Feel free to test it out:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/10871206?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="nofollow noopener">sebastianandress/Slicer-SurfaceWrapSolidify</a></h3>

<p>3D Slicer extension which contains a Segment Editor Effect that extracts the surface of a segmentation - sebastianandress/Slicer-SurfaceWrapSolidify</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
