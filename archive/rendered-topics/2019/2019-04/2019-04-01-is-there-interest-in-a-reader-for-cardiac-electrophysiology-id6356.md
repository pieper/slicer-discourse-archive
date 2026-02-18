# Is there interest in a reader for cardiac electrophysiology electronanatomic maps?

**Topic ID**: 6356
**Date**: 2019-04-01
**URL**: https://discourse.slicer.org/t/is-there-interest-in-a-reader-for-cardiac-electrophysiology-electronanatomic-maps/6356

---

## Post #1 by @stephan (2019-04-01 17:48 UTC)

<p>Hi,<br>
for a research project I developed a python scripted module that reads data exported from cardiac electroanatomic mapping systems (Ensite Velocity, CARTO 3, and Rhythmia) and creates models in Slicer from it (with the electric data as a scalar overlay).<br>
The code was good enough for what I needed it for, but it is still quite experimental and not ready to be released as it is (e.g. it is not packed/built into an extension but it is rather the raw python file as generated from the Extension Wizard, and no self-test is implemented).<br>
I was wondering if there are other cardiac electrophysiologists out there who would like to use this functionality in Slicer. If so, I would try to get it to a more release-ready shape as soon as I can find some time to spare. Otherwise it will probably end up further down on the to-do list…</p>

---

## Post #2 by @pieper (2019-04-02 12:29 UTC)

<p>Hi <a class="mention" href="/u/stephan">@stephan</a> - I’m not currently doing anything with cardiac ep, but I can imagine the code you described being very interesting to people in the field even if it’s not completely packaged up.  As far as I know there’s no real standard file format, so having file reader code for the various vendor systems could be handing.  Maybe you could just publish a github repository with a clear WIP warning in the readme?</p>
<p>-Steve</p>

---

## Post #3 by @stephan (2019-04-02 14:28 UTC)

<p>Sounds good. I will do that (probably within the next two weeks) and post updates here.</p>

---

## Post #4 by @lassoan (2019-04-06 04:23 UTC)

<p>I fully agree with <a class="mention" href="/u/pieper">@pieper</a>’s suggestion. Just make the extension public, even if it is not polished yet, to give others a chance to try it, give feedback, etc.</p>
<p>We have collaborators who use Slicer for EP procedures, with CARTO, they would be probably interested.</p>

---

## Post #5 by @stephan (2019-04-10 17:30 UTC)

<p>It is out there now: <a href="https://github.com/stephan1312/SlicerEAMapReader" rel="nofollow noopener">https://github.com/stephan1312/SlicerEAMapReader</a></p>

---

## Post #6 by @pieper (2019-04-10 18:21 UTC)

<p>This looks great <a class="mention" href="/u/stephan">@stephan</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Just a thought, but if you happen to have any sample data sets to post somewhere that would be great too.</p>

---

## Post #7 by @jcfr (2019-04-10 18:34 UTC)

<p>Ditto</p>
<p><a class="mention" href="/u/stephan">@stephan</a> When you have a chance, could you associate the <code>3d-slicer-extension</code> GitHub topic so that it is listed here: <a href="https://github.com/topics/3d-slicer-extension" rel="nofollow noopener">https://github.com/topics/3d-slicer-extension</a></p>

---

## Post #8 by @stephan (2019-04-10 20:00 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="6356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>could you associate the <code>3d-slicer-extension</code> GitHub topic so that it is listed here</p>
</blockquote>
</aside>
<p>done</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="6356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>if you happen to have any sample data sets to post somewhere that would be great too</p>
</blockquote>
</aside>
<p>I’ll work on it.</p>

---

## Post #9 by @mattjolley (2019-04-10 20:58 UTC)

<p>Yes.  As noted above we are working in this space as well, but putting images into CARTO.</p>
<p>Being able to get them from CARTO to Slicer would be very helpful.</p>

---

## Post #10 by @stephan (2019-04-10 21:03 UTC)

<p>Feel free to test it. We worked mostly with Rhythmia, so CARTO and Velocity testing has been more limited. I am looking forward to any feedback and improvements. Let me know if you have any questions.</p>

---

## Post #11 by @stephan (2019-11-21 20:06 UTC)

<p>Update: Unfortunately, CARTO import is broken. The extension was developed (and limited testing was done) using sample files exported from a CARTO3 v<strong>4</strong> system.<br>
In the current version (CARTO3 v<strong>6</strong>) export from the work station has been changed and the interesting data (the triangulated mesh of the map) is no longer being exported.<br>
It is unclear whether this change is intentional (might not be, since the files which are now missing from the exported data set are still referred to in other parts of the exported data).<br>
However, preliminary feedback from the manufacturer indicates that they will probably leave it that way.</p>

---

## Post #12 by @tomasz (2020-02-16 14:47 UTC)

<p>Hi Stephan,<br>
My name is Tom. I am an electrophysiology fellow at the International Clinical Research Center (Brno, Czech Republic) and Medical University of Silesia (Katowice, Poland).<br>
Thank you for your contribution and development of the reader for cardiac EP maps.</p>
<p>We are planning to initiate the radiosurgery clinical study designed for patients with VT. Thus, I am looking for a solution to merge EP maps with CT scans for procedure planning. Thus, I would like to ask if your reader can be used to integrate Ensite Velocity maps with CT.</p>
<p>I will be grateful for the information.</p>
<p>Kind regards,<br>
Tom</p>

---

## Post #13 by @stephan (2020-02-17 19:00 UTC)

<p>Hi Tom,<br>
thank you for your note and for your interest in the EA map reader. The plug-in is being overhauled right now (since some python-related changes in Slicer 4.11 stopped from working properly), so please bear with me for a couple more weeks. In general, Ensite Velocity maps can be read (although testing has been limited so far)<br>
I’ll let you know when the plug-in is working again. Thank you for your patience.</p>
<p>Stephan</p>

---

## Post #14 by @tomasz (2020-02-17 19:17 UTC)

<p>Thank you Stephan. I am looking forward to hearing from you.<br>
Yours,<br>
Tomasz</p>

---

## Post #15 by @lassoan (2020-02-18 00:59 UTC)

<aside class="quote no-group" data-username="stephan" data-post="13" data-topic="6356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>The plug-in is being overhauled right now (since some python-related changes in Slicer 4.11 stopped from working properly), so please bear with me for a couple more weeks</p>
</blockquote>
</aside>
<p>Let us know if we can help with anything. If you send the repository URL and a test data set then we may be able to fix Python2/3 API differences.</p>

---

## Post #16 by @Sergio_Laranjo (2020-05-15 11:33 UTC)

<p>Dear Stephan,</p>
<p>Would very much appreciated to have access to the EA map reader, in particular for NavX maps.</p>
<p>Are you planning to share it again?</p>

---

## Post #17 by @stephan (2020-06-15 08:49 UTC)

<p><a class="mention" href="/u/sergio_laranjo">@Sergio_Laranjo</a> <a class="mention" href="/u/tomasz">@tomasz</a></p>
<p>We debugged the reader to make it work with Slicer 4.11 / Python 3.<br>
Also, an accompanying publication has been submitted and is currently under review.<br>
The extension can be found at<br>
</p><aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/stephan1312/SlicerEAMapreader/" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/33878842?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/stephan1312/SlicerEAMapreader/" target="_blank" rel="nofollow noopener">stephan1312/SlicerEAMapReader</a></h3>

<p>Read cardiac electrophysiology maps from various electroanatomic mapping systems into 3D Slicer - stephan1312/SlicerEAMapReader</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Just download the <a href="https://github.com/stephan1312/SlicerEAMapReader/raw/master/EAMapReader-Slicer-4.11.zip" rel="nofollow noopener">EAMapReader-Slicer-4.11.zip</a> file and install the extension from file.
<p>Also, see the <a href="https://github.com/stephan1312/SlicerEAMapReader/blob/master/README.txt" rel="nofollow noopener">Readme file</a></p>

---

## Post #18 by @lassoan (2020-06-16 05:13 UTC)

<p>Thank you for sharing this. Would you consider polishing up this module a bit and submitting to the extension manager? We could also distribute this module as part of SlicerHeart extension, thereby saving some administration and maintenance efforts.</p>

---

## Post #19 by @Predrag_Stojadinovic (2020-10-19 21:33 UTC)

<p>Hi. This extension is not working. At least not on my Mac.<br>
This is a notification.</p>
<p>Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX</p>
<p>Do you have any sugestion.</p>
<p>Thank you, very much.</p>

---

## Post #20 by @lassoan (2020-10-20 00:25 UTC)

<p>It seems that you missed the installation step of dragging the Slicer application to your Applications folder. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#mac">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#mac</a>.</p>

---

## Post #21 by @mk.kassai (2021-08-20 15:11 UTC)

<p>Dear Stephan,<br>
First of all, thank you for your efforts in making this module!</p>
<p>I’d like to import some CARTO electroanatomic maps to Slicer on a Mac.<br>
The module gives a message, that it has imported, extracted the archive (to a hidden folder), cleans up temporary files, and then Done.<br>
However I can’t find any files in said folder, even when looking for hidden files.<br>
I guess this is the problem you wrote, with carto.<br>
Do you have any news on solving this issue?</p>
<p>Thanks again for your help!<br>
Miklos</p>

---

## Post #22 by @mayaambar (2024-05-30 08:38 UTC)

<p>HI Stephan<br>
First of all, thank you so much for sharing this.<br>
I looked at the link to the GitHub that you posted and I am in the installation phase (at the README)<br>
I installed the EAMapReader.zip file and I have the 3D Slicer 5.6 but when I try to select “Install from file” and open this file it is empty and its not opening any extension .<br>
do you maybe have any idea of what am I doing wrong?<br>
I would really appreciated help of any kind !<br>
thank you so much<br>
Maya</p>

---

## Post #23 by @lassoan (2024-05-30 15:07 UTC)

<p>I’ve added EA Map Reader module to SlicerHeart extension. It will be available from tomorrow in both the latest Slicer Stable Release (Slicer-5.6) and the latest Slicer Preview Release (Slicer-5.7 downloaded June 1, 2024 or later).</p>

---

## Post #24 by @mayaambar (2024-06-04 07:25 UTC)

<p>wow, that is amazing. thank you<br>
where can I find it?</p>

---

## Post #25 by @lassoan (2024-06-04 16:03 UTC)

<p>It is in SlicerHeart extension. Install the very latest Slicer Preview Release and then install SlicerHeart extension to make <code>EA Map Reader</code> module available.</p>

---
