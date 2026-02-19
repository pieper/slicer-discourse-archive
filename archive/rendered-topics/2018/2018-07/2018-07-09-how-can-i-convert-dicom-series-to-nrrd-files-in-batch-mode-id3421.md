---
topic_id: 3421
title: "How Can I Convert Dicom Series To Nrrd Files In Batch Mode"
date: 2018-07-09
url: https://discourse.slicer.org/t/3421
---

# How can I convert DICOM series to NRRD files in batch mode?

**Topic ID**: 3421
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/how-can-i-convert-dicom-series-to-nrrd-files-in-batch-mode/3421

---

## Post #1 by @Kyu_Sung_Choi (2018-07-09 11:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7e668a48738a0112b41d4149f6ecc1df9f03ab8.png" data-download-href="/uploads/short-url/uNWiT23JFBKYvZAeXXIOH9KFdhK.png?dl=1" title="capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7e668a48738a0112b41d4149f6ecc1df9f03ab8.png" alt="capture" data-base62-sha1="uNWiT23JFBKYvZAeXXIOH9KFdhK" width="690" height="239" data-dominant-color="111113"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture</span><span class="informations">1428×495 27.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Dear Dr. Fedorov,</p>
<p>I want to convert DICOM series to NRRD files in batch mode in order to feed the NRRD files to make rCBV maps using DSCMRIAnalysis module in batch mode.<br>
However, I can’t figure out how to convert DICOM series to NRRD files in command lines.</p>
<p>You suggested me to see the following site:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor.py#L144">
  <header class="source">

      <a href="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor.py#L144" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor.py#L144" target="_blank" rel="noopener nofollow ugc">SlicerProstate/mpReview/blob/master/mpReviewPreprocessor.py#L144</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="134" style="counter-reset: li-counter 133 ;">
          <li>  if not self.indexer:
</li>
          <li>    self.indexer = ctk.ctkDICOMIndexer()
</li>
          <li>
</li>
          <li>    def updateProgress(progress):
</li>
          <li>      if self.progressCallback:
</li>
          <li>        self.progressCallback(windowTitle='DICOMIndexer', labelText='Processing files', value=progress)
</li>
          <li>    self.indexer.connect("progress(int)", updateProgress)
</li>
          <li>  self.indexer.addDirectory(self.dicomDatabase, inputDir)
</li>
          <li>  logging.debug('Import completed, total %s patients imported' % len(self.patients))
</li>
          <li>
</li>
          <li class="selected">def _processData(self, outputDir, copyDICOM, progressCallback=None):
</li>
          <li>  self.progressCallback = progressCallback
</li>
          <li>
</li>
          <li>  for patient in self.patients:
</li>
          <li>    self.updateProgressBar(windowTitle="Processing patient %s" % patient)
</li>
          <li>    for study in self.dicomDatabase.studiesForPatient(patient):
</li>
          <li>      #print self.dicomDatabase.seriesForStudy(study)
</li>
          <li>      self.updateProgressBar(windowTitle="Processing %s" % study)
</li>
          <li>      series = self.dicomDatabase.seriesForStudy(study)
</li>
          <li>      for seriesIndex, currentSeries in enumerate(series, start=1):
</li>
          <li>        if self.canceled:
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, I do not see any arguments “input file directory” that I should put in some location.</p>
<p>Could you please be more specific? or are there any other ways to convert DSC DICOM series into NRRD multivomes in batch mode?</p>
<p>Thank you in advance!<br>
Kyu Sung</p>

---

## Post #2 by @fedorov (2018-07-09 20:43 UTC)

<p>Here is how you can do the conversion in batch mode.</p>
<p>First, install mpReview extension. This will add two new modules: <code>mpReview</code> and <code>mpReviewPreprocessor</code>.</p>
<p><code>mpReviewPreprocessor</code> can be used to volume-reconstruct any collection of DICOM files in batch mode using Slicer DICOM plugins. It can be accessed from the Slicer GUI, but you can also run the script as from the command line follows (you will need to update the path to the preprocessor to the on your system after installing the script, or you can just download the script from the GitHub repository <a href="https://github.com/SlicerProstate/mpReview">here</a>):</p>
<pre data-code-wrap="bash"><code class="lang-bash">Slicer --no-main-window --no-splash --python-script \
/Applications/Slicer.app/Contents/Extensions-27269/mpReview/lib/Slicer-4.9/qt-scripted-modules/mpReviewPreprocessor.py \
-- -i DSC-DICOM -o DSC-mpReview
</code></pre>
<p><code>-i</code> takes a directory with DICOM files (it can have any hierarchy of subordinate content, will be scanned recursively</p>
<p><code>-o</code> is the output directory.</p>
<p>After script is completed, it will have a hierarchy of directories similar to what is shown below (the example I show is for the dataset you shared earlier) -</p>
<p><code>&lt;PatientID&gt; \ RESOURCES \ &lt;SeriesNumber&gt; \ Reconstructions \ &lt;SeriesNumber&gt;.nrrd</code></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16d0059dd3b5f5f68cbf7176ab5b5f8311f2e664.png" alt="image" data-base62-sha1="3fObJFr89jpiK4d4WVumMP9HktS" width="381" height="169"></p>
<p>The NRRD file will be the one that corresponds to the default loadable when the corresponding DICOM series is loaded using DICOM Browser. If you need to customize this behavior, you would need to look into the script, but the default behavior might be sufficient for you.</p>
<p>Note that to correctly parse your specific DSC MRI dataset <a href="https://github.com/Slicer/Slicer/pull/982">patch that I introduced last week</a> will be needed, otherwise the resulting volume will not have the timing information. The patch was integrated today, and, if things go well, you should be able to access the updated nightly tomorrow.</p>
<p>Let us know if this answers your question.</p>

---

## Post #3 by @Kyu_Sung_Choi (2018-07-11 00:42 UTC)

<p><strong>Thank you so much, and it worked perfect for DSC MRI dataset that I’ve got.</strong></p>
<p>Since you said the patch was integrated for the specific DSC MRI dataset that I have sent you before, <strong>I re-installed DSCMRIAnalysis now, which still did not work for the specific dataset.</strong></p>
<p>Do I have to re-install the Slicer with nightly build version? or DSCMRIAnalysis module using extension manager?</p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #4 by @fedorov (2018-07-11 13:57 UTC)

<p>Yes, you will have to re-install Slicer, and then re-install the extensions that you need for your work.</p>

---

## Post #5 by @Kyu_Sung_Choi (2018-07-12 02:09 UTC)

<p>Dear Dr.Fedorov,</p>
<p>I am so sorry that updated (Extensions-27273) mpReviewPreprocess module did not work for the specific dataset I sent to you, which I was confused.<br>
When I preprocess the specific DICOM dataset with mpReviewPreprocess module on GUI, and then put it into DSCMRIAnalysis module on GUI, then I’ve got error msg attached below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d020f6a6536bb26573e24112a18ad298bebfdde8.png" data-download-href="/uploads/short-url/tHbW8NKLxTYmkRdItmbI8Of7BfW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d020f6a6536bb26573e24112a18ad298bebfdde8_2_690x392.png" alt="image" data-base62-sha1="tHbW8NKLxTYmkRdItmbI8Of7BfW" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d020f6a6536bb26573e24112a18ad298bebfdde8_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d020f6a6536bb26573e24112a18ad298bebfdde8_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d020f6a6536bb26573e24112a18ad298bebfdde8_2_1380x784.png 2x" data-dominant-color="88888F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1847×1050 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Same error msg in the command line.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6f869a3a97812a7b4e4449509286105b45552ec.png" data-download-href="/uploads/short-url/zeNG7yJ2niNeJkA1irdzlDx8qAs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6f869a3a97812a7b4e4449509286105b45552ec.png" alt="image" data-base62-sha1="zeNG7yJ2niNeJkA1irdzlDx8qAs" width="690" height="457" data-dominant-color="3C1E32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">738×489 79.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I do not get error msg when I preprocess the specific DICOM dataset with DICOM module on GUI, and then put it into DSCMRIAnalysis module on GUI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15345029c90c76d54ab6e21a98cd0e834595e0d2.jpeg" data-download-href="/uploads/short-url/31A6Ej14EBqrnNlaHcoEb793yJc.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15345029c90c76d54ab6e21a98cd0e834595e0d2_2_690x392.jpg" alt="image" data-base62-sha1="31A6Ej14EBqrnNlaHcoEb793yJc" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15345029c90c76d54ab6e21a98cd0e834595e0d2_2_690x392.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15345029c90c76d54ab6e21a98cd0e834595e0d2_2_1035x588.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15345029c90c76d54ab6e21a98cd0e834595e0d2_2_1380x784.jpg 2x" data-dominant-color="83848B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1851×1053 420 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Could you please let me know how to use DICOM module on command line? or could you please fix mpReviewPreprocess module?</strong><br>
Sorry to bother you again.</p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #6 by @fedorov (2018-07-12 16:27 UTC)

<p>Indeed, there was a bug in the mpReviewPreprocessor script. The loadables that were produced by the multivolume plugin were not sorted by confidence by the script. It is now fixed, and should work as expected (consistent with how multivolume is loaded using Slicer DICOM Browser) in the next nightly (as before, you would need to re-install Slicer, and install mpReview extension).</p>
<p>Alternatively, if you want to try the update earlier, you can locate the <code>mpReviewPreprocessor.py</code> script, and add one line to the source code as shown here: <a href="https://github.com/SlicerProstate/mpReview/commit/ab6a388eb1d42b3b477386ca99264c46e7808765">https://github.com/SlicerProstate/mpReview/commit/ab6a388eb1d42b3b477386ca99264c46e7808765</a>.</p>
<p>Sorry for the trouble, and thank you for your patience. Your feedback is very helpful in improving the tool.</p>

---

## Post #7 by @Kyu_Sung_Choi (2018-07-23 07:17 UTC)

<p>Dear Dr.Fedorov,</p>
<p>I re-installed Slicer-4.9.0 with 2018-07-22 nightly build version, and tried to re-install the extension DSCMRIAnalysis.<br>
However, it says, “No extensions found for linux:64-bit, revision: ‘27291’. Please try a different combination”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaf0d40ebaf106e742f660a81d5e3cdf0a5bd503.png" data-download-href="/uploads/short-url/xwnHqvBTv5gyYcmsCYajFjJA9fJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaf0d40ebaf106e742f660a81d5e3cdf0a5bd503_2_690x88.png" alt="image" data-base62-sha1="xwnHqvBTv5gyYcmsCYajFjJA9fJ" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaf0d40ebaf106e742f660a81d5e3cdf0a5bd503_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaf0d40ebaf106e742f660a81d5e3cdf0a5bd503_2_1035x132.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaf0d40ebaf106e742f660a81d5e3cdf0a5bd503_2_1380x176.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1847×238 24.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think it could be a problem regarding the version of the extension.<br>
Could you please tell me how I can re-install DSCMRIAnalysis?<br>
Please let me test what you fixed.</p>
<p>All the best,<br>
Kyu Sung Choi</p>

---

## Post #8 by @fedorov (2018-07-23 14:28 UTC)

<p>It could be that the extensions were not yet built/packaged at the time you tried. Looking at the dashboard <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">here</a>, the package of DSCAnalysis extension is now ready, so you should try again.</p>

---

## Post #9 by @Kyu_Sung_Choi (2018-07-24 01:38 UTC)

<p>Dear Dr.Fedorov,</p>
<p>I re-installed Slicer-4.9.0 with 2018-07-22 nightly build version, and re-installed the extension DSCMRIAnalysis (27291).<br>
However, same as the last time, it worked with DICOM module to make dicom files of DSC into nrrd files, but mpReview Preprocessor won’t work in GUI as well as in command lines.<br>
I think I correctly entered the directory path of mpReviewPreprocessor.py.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ab6bb4b6f4c47c253749c3414460a971fde51a9.png" data-download-href="/uploads/short-url/3OjUIXpv1KTrP2Lvrb4FBqTSzR7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ab6bb4b6f4c47c253749c3414460a971fde51a9.png" alt="image" data-base62-sha1="3OjUIXpv1KTrP2Lvrb4FBqTSzR7" width="690" height="460" data-dominant-color="422639"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×486 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<strong>Could you please fix it ? or please let me know how to use DICOM modules in command line.</strong></p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #10 by @lassoan (2018-07-24 02:08 UTC)

<p>It seems that there are special characters in the path. Please try again by installing Slicer in a folder that only has ASCII characters in the path and store all data in folders that only contain ASCII characters.</p>

---

## Post #11 by @Kyu_Sung_Choi (2018-07-24 02:23 UTC)

<p>I changed the path of data folder in English.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6c9cbde6a1d7603eb7fc87229328b9ae7599d7.png" data-download-href="/uploads/short-url/oT1MoxR3WyuVnyBCk0X6UKm4mFh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae6c9cbde6a1d7603eb7fc87229328b9ae7599d7_2_690x87.png" alt="image" data-base62-sha1="oT1MoxR3WyuVnyBCk0X6UKm4mFh" width="690" height="87" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae6c9cbde6a1d7603eb7fc87229328b9ae7599d7_2_690x87.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6c9cbde6a1d7603eb7fc87229328b9ae7599d7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6c9cbde6a1d7603eb7fc87229328b9ae7599d7.png 2x" data-dominant-color="381C30"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">734×93 17.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Slicer was already installed in the path which contains only ASCII characters: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b7ede8f57ca1bb81c285ff5c909f748cc70f8e5.png" alt="image" data-base62-sha1="6cMlydsbGxIkQ0IU0fUNkVmanS5" width="584" height="35"><br>
However, it made the same error msg.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d270a83c8d9978716c9e3d7cb0b701dc4ef94c2.png" data-download-href="/uploads/short-url/fzBGK1CQC2VTGs8gNRXBgwRRPMK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d270a83c8d9978716c9e3d7cb0b701dc4ef94c2.png" alt="image" data-base62-sha1="fzBGK1CQC2VTGs8gNRXBgwRRPMK" width="690" height="171" data-dominant-color="422439"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×183 43.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, I tried it on my Windows desktop and Ubuntu workstation.<br>
I was able to run mpReview GUI on my Windows desktop, however it doesn’t work on Ubuntu workstation.<br>
Could you please tell me how to use DICOM modules in command lines?</p>

---

## Post #12 by @Kyu_Sung_Choi (2018-07-24 05:46 UTC)

<p>I reboot my workstation, and I don’t know why but it works!<br>
Thank you for your comments.<br>
I really appreciate it.</p>

---
