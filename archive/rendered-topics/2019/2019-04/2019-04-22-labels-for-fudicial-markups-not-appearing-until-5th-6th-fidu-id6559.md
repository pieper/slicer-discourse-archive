# Labels for Fudicial Markups Not Appearing Until 5th-6th Fiducial Is Placed 4.11.0

**Topic ID**: 6559
**Date**: 2019-04-22
**URL**: https://discourse.slicer.org/t/labels-for-fudicial-markups-not-appearing-until-5th-6th-fiducial-is-placed-4-11-0/6559

---

## Post #1 by @triple_axel (2019-04-22 19:50 UTC)

<p>Hi,</p>
<p>I’m currently attempting to put fiducial markups on a scan on the nightly 4.11 version, however, the labels for the fiducial markups are not appearing until i put them on the very left of my scan or until I reach the 5th or 6th fiducial. I have attached a small video in the link below.</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/11TLut28TGDFVsTuERgF3bsEqoi4ccobS/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/11TLut28TGDFVsTuERgF3bsEqoi4ccobS/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/11TLut28TGDFVsTuERgF3bsEqoi4ccobS/view?usp=sharing" target="_blank" rel="nofollow noopener">4.11Fiducials.mp4 (video)</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Do you know why this occurs and how do I fix it?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2019-04-22 23:11 UTC)

<p>I’m unable to replicate your issue. I used the same Slicer nightly, loaded a volume, and placed a fiducial similar to your video and the fiducial label appeared immediately. Try going to the Markups module, expanding the “Display” group box and pressing “Reset to Defaults” to reset the settings related to markups. Maybe there is some combination of markup settings causing this issue.</p>
<p>For additional information, could you provide information about what CPU and GPU you were using?</p>

---

## Post #3 by @triple_axel (2019-04-23 13:27 UTC)

<p>Hi, I tried “Reset to Defaults” however the problem is still persistent. Sometimes it appears after 3 fiducials are placed, but sometimes 5-6.</p>
<p>I’m using a Geforce RTX 2070 for the GPU. For CPU I am using an AMD Ryzen 7 2700x Eight-Core Processor (3.70 GHz) and I’m on a Windows 10 Home platform.</p>
<p>Thanks for the help.</p>

---

## Post #4 by @triple_axel (2019-04-24 20:47 UTC)

<p>Hi, sorry I forgot to add this. But I have also attached a file that contains the CT scan of what I am having issues placing fiducials on.<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1QzjkOW1xTW9VL2rX-pYzCfs4ojMBTU_6/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1QzjkOW1xTW9VL2rX-pYzCfs4ojMBTU_6/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1QzjkOW1xTW9VL2rX-pYzCfs4ojMBTU_6/view?usp=sharing" target="_blank" rel="nofollow noopener">CT.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @lassoan (2019-04-24 22:23 UTC)

<p>I was able to reproduce the problem. It seems to be related to the unusual aspect ratio of the view (it is very tall). I’ll work on it soon. You can monitor the status of the issue here: <a href="https://issues.slicer.org/view.php?id=4689" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4689</a></p>

---
