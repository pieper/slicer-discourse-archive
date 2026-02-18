# Error loading new DICOM

**Topic ID**: 5401
**Date**: 2019-01-17
**URL**: https://discourse.slicer.org/t/error-loading-new-dicom/5401

---

## Post #1 by @Giulia (2019-01-17 16:30 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.10.1<br>
Expected behavior: Add dicom datas from MRI and create a 3D printable model<br>
Actual behavior: Can’t add the datas into DICOM folder, if I import them into the “add data” folder I get each single slice instead of one single study and I canìt create an accurate 3d model</p>
<p>I also tried to use the Embodi3D app Democratiz 3D but this time it failed saying that my " NRRD file originated from an MRI. Currently, we only process NRRDs from CT scans." and “You tried to process individual slices instead of a complete study.”</p>
<p>Thank you for your help, this work is really important to me and I’d love to fix the problem quite soon.<br>
Giulia</p>

---

## Post #2 by @jcfr (2019-01-17 16:32 UTC)

<aside class="quote no-group" data-username="Giulia" data-post="1" data-topic="5401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/d07c76/48.png" class="avatar"> Giulia:</div>
<blockquote>
<p>Can’t add the datas into DICOM folder, if I import them into the “add data” folder I get each single slice instead of one single study and I canìt create an accurate 3d model</p>
</blockquote>
</aside>
<p>DICOM data should be imported using the <code>File -&gt; DICOM</code> instead of <code>File -&gt; Add Data</code></p>
<p>To learn more about the DICOM support in Slicer, read <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM">https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM</a></p>

---

## Post #3 by @Giulia (2019-01-17 16:47 UTC)

<p>Yeah, I’m tryin’ to import DICOM data using the <code>File -&gt; DICOM</code> (instead of <code>File -&gt; Add Data</code>  ) but it doesn’t work, nothing happens, it only says “0 patients added”</p>

---

## Post #4 by @jcfr (2019-01-17 16:48 UTC)

<p>Also, to follow up, even after installing the suggested extensions <code>LongitudinalPETCT</code>, <code>PETDICOMExtension</code> and <code>QuantitativeReporting</code>, I was not able to load the dataset you shared privately with me.</p>
<p>For reference the pop initially reported was:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/830e94745c3078b2f70dec8b96b7eef94974bcf9.png" alt="image" data-base62-sha1="iHnMJ57PiteyfAaIFpC5ajOxjAZ" width="497" height="309"></p>
<p>and the message reported after trying to load the dataset once the extensions are installed:</p>
<pre><code class="lang-auto">Dataset is missing necessary information (patient name, study instance UID, or patient ID)!
Dataset is missing necessary information (patient name, study instance UID, or patient ID)!
[...]
</code></pre>

---

## Post #5 by @Giulia (2019-01-17 16:58 UTC)

<p>Thank you really much for tryin’ to help me, it’s appreciated. I’ll try to figure out something else…<img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"></p>

---
