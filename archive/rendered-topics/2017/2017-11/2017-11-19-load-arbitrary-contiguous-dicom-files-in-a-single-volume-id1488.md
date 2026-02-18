# Load arbitrary contiguous DICOM files in a single volume

**Topic ID**: 1488
**Date**: 2017-11-19
**URL**: https://discourse.slicer.org/t/load-arbitrary-contiguous-dicom-files-in-a-single-volume/1488

---

## Post #1 by @chir.set (2017-11-19 10:40 UTC)

<p>This is a feature request.</p>
<p>Via File/Add data/Choose Files to Add, if an arbitrary number of DICOM files are selected, each file is loaded as a separate volume. Can they be loaded as a single volume ?</p>
<p>Alternatively, can there be a supplementary widget, like a slide bar or spin boxes, to skip some files at the beginning and at the end of the series, while selecting one single file ?</p>
<p>The current workflow is to load the whole volume and then use ‘Crop volume’ module.</p>
<p>Thanks for your opinions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1514adffc61b77dbd03fbfd9486c13d92298ee7.png" data-download-href="/uploads/short-url/piCGcfgENWjbKsR0SzUpqHvriN9.png?dl=1" title="Screenshot_20171119_113010" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1514adffc61b77dbd03fbfd9486c13d92298ee7_2_690x396.png" alt="Screenshot_20171119_113010" data-base62-sha1="piCGcfgENWjbKsR0SzUpqHvriN9" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1514adffc61b77dbd03fbfd9486c13d92298ee7_2_690x396.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1514adffc61b77dbd03fbfd9486c13d92298ee7_2_1035x594.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1514adffc61b77dbd03fbfd9486c13d92298ee7_2_1380x792.png 2x" data-dominant-color="ACC0D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20171119_113010</span><span class="informations">1406×808 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2017-11-19 15:44 UTC)

<p>As a workaround, why not use your OS file explorer and just copy the files of interest into a temp folder and load from there.</p>

---

## Post #3 by @chir.set (2017-11-19 16:20 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="1488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>copy the files</p>
</blockquote>
</aside>
<p>Well it’s just about saving time, when volumes are loaded multiple times a day in short time frames. It would just remove the need to crop down the volume. Now it’s only a request.</p>

---

## Post #4 by @pieper (2017-11-19 16:43 UTC)

<p>Yes, understand that it’s a feature request - I’m just concerned about complicating the user interface for a special case that might be addressed another way (since the user interface is already complex!).</p>
<p>With dicom files is that you have to have special knowledge of the mapping between file names and volume geometry in order for loading subsets of files useful, so I’m concerned that adding custom GUI elements for this purpose could be error prone when used on different datasets.</p>
<p>On the other hand small custom python script (or scripted module) that exploits your knowledge of the file naming could help with the particular kind of data you are loading.</p>

---

## Post #5 by @chir.set (2017-11-19 18:24 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="1488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>could be error prone when used on different datasets</p>
</blockquote>
</aside>
<p>Ah ! File naming scheme varies indeed between CT machines. Sometimes DICOM and JPEG files are mixed in the same directory, and mutiple series may exist in the same directory also.</p>
<p>So it’s a bad idea, let’s drop it. Sorry to have bothered you.</p>

---

## Post #6 by @lassoan (2017-11-19 19:39 UTC)

<p>Crop volume module is better then simply skipping some frames, as often you want to also resample the volume. You can save the cropped &amp; resampled volume to a research file format (metaimage, nrrd,…) or export back to DICOM.</p>

---

## Post #7 by @muratmaga (2017-11-19 23:22 UTC)

<p>While I agree that crop volume it’s very nice tool, I think an import tool has a utility for datasets from highres mCT, where 2000x2000x2000 is not an common dataset. Importing the entire dataset only to crop a portion of is usually a very time consuming process.<br>
Obviously this can be done outside of Slicer, but it can enhance the user experience.<br>
M</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/6f007222d29408f1afc6a3741f6c3b71bda9a9cd.png" width="442" height="3"></p>

---

## Post #8 by @lassoan (2017-11-20 00:59 UTC)

<p>2000^3 images are 50-100x larger than typical clinical images, so I agree that they would deserve special treatment. What is the typical image size after you import, crop, and resample the volume? What operations are you performing most commonly (importing, various visualizations, segmentation, registration, filtering, etc.)? Which ones are the most time-consuming?</p>

---

## Post #9 by @muratmaga (2017-11-20 04:18 UTC)

<p>In our typical uses cases, these large volumes usually contain multiple specimens (e.g., 4-5 mouse fetuses) scanned simultaneously to cut the costs associated with imaging.</p>
<p>I never import them through Slicer, because our slice sequences are output in png format, which slicer reads as a vector volume increasing the memory consumption by 3 times for something that is already 8GB to begin with.</p>
<p>Right here an option to NOT read bmp/png/jpg as a vector, but a scalar would be a useful convenience feature.<br>
A stack limiting feature (to constrain top and bottom) as well as an ROI to constrain within the slice would be good features that will help importing these large sequences (I am assuming same tool feature can be provided for DICOM sequences as well).</p>
<p>We currently do all this outside of Slicer (e.g., Fiji). When cut/crop, our volumes are typically smaller than 1000x1000x1000 range (more around 800-600 cubic voxels), for which most of the functions in Slicer works fairly good. Most of our Slicer work is either 3D visualization, or manual segmentation. If I have to have a 3D representation in segment editor to do my task, I usually down-sample them further, because model creation at those sizes takes quite a bit.</p>
<p>I can provide you a sample large slice sequence, if that helps you to see the challenges.</p>
<p>Again, none of these are real deal breakers for someone who is interested in using extensive imaging tools Slicer provides, but will help novice users (especially ones outside of medical imaging domain) to get their data in faster.</p>

---

## Post #10 by @lassoan (2017-11-20 04:51 UTC)

<p>It’s good that only importing is challenging. It would be very easy to write a Python script (would take 10-20 hours of an experienced Slicer module developer) that would split the large volume into smaller ones and save each as a separate grayscale volume.</p>

---

## Post #11 by @chir.set (2017-11-21 19:46 UTC)

<p>After having discovered the Extension Wizard module, I glued Python code from different sources to come up to a module that suits my workflow.</p>
<p>I am <a href="https://mega.nz/#!BJVggBAC!h94YCmp17ICROsVonKRw8QBOGzFKSV0ypnuKMRB8CHo" rel="nofollow noopener">posting</a> it here in the hope that experienced developers express their views on its technical aspects, if any volunteer can find time for that.</p>
<p>Please note that I am not claiming that this module would be useful to others.</p>
<p>Regards.</p>

---

## Post #12 by @pieper (2017-11-21 21:12 UTC)

<p>I took a quick look - you seem to be getting the idea and I hope it’s seeming productive.  Did you run into any specific questions?  As a hint if you put the code in a github repository it’s possible to have discussion threads about specific lines or blocks of code.</p>

---

## Post #13 by @chir.set (2017-11-21 22:16 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="1488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>if you put the code in a github repository</p>
</blockquote>
</aside>
<p>I’ll give this a try during the week end, thanks.</p>

---

## Post #14 by @chir.set (2017-11-25 19:22 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="1488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>put the code in a github repository</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>Here is an updated <a href="https://github.com/chir-set/TemplateROICrop" rel="noopener nofollow ugc">github repository</a> for this project. I would like to discuss on two subjects if you wish.</p>
<p>Regards.</p>

---

## Post #15 by @pieper (2017-11-30 14:16 UTC)

<p>Thanks for putting the code in the repo <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>
<p>What were the two subjects you wanted to discuss?</p>

---

## Post #16 by @chir.set (2017-11-30 16:59 UTC)

<aside class="quote no-group" data-username="pieper" data-post="15" data-topic="1488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>What were the two subjects you wanted to discuss?</p>
</blockquote>
</aside>
<ol>
<li>
<p>Everytime a ROI is loaded using slicer.util.loadAnnotationROI, an entry is added in ‘Recently loaded’ menu, even though it already exists. Can this be prevented through scripting ? Or can we delete the last inserted entry ? Or should Slicer itself prevent duplicates in the ‘Recently loaded’ menu ?</p>
</li>
<li>
<p>At <a href="http://www.commontk.org/docs/html/index.html" rel="noopener nofollow ugc">www.commontk.org/docs/html/index.html</a> and <a href="http://apidocs.slicer.org/master/index.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: Slicer</a>, we have a complete regular C++ API for Slicer itself and CTK widgets. Does a similar structured API exist for Python scripting? I could not find such an API. Example code is very useful and that’s what I have used. (But perhaps serious scripting requires good knowledge of Slicer’s internals, well on top of my head though… I should not go any further.)</p>
</li>
</ol>
<p>Thanks for your interest.</p>

---

## Post #17 by @pieper (2017-12-05 21:50 UTC)

<p>Regarding the first topic, it makes sense not to have duplicates in the Recently Loaded</p>
<p>Probably we want to avoid adding duplicates here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/qSlicerAppMainWindow.cxx#L1351-L1365" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/qSlicerAppMainWindow.cxx#L1351-L1365" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Applications/SlicerApp/qSlicerAppMainWindow.cxx#L1351-L1365</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1351" style="counter-reset: li-counter 1350 ;">
<li>void qSlicerAppMainWindow::onNewFileLoaded(const qSlicerIO::IOProperties&amp; fileProperties)</li>
<li>{</li>
<li>Q_D(qSlicerAppMainWindow);</li>
<li>
</li>
<li>d-&gt;RecentlyLoadedFileProperties.removeAll(fileProperties);</li>
<li>
</li>
<li>d-&gt;RecentlyLoadedFileProperties.enqueue(fileProperties);</li>
<li>
</li>
<li>d-&gt;filterRecentlyLoadedFileProperties();</li>
<li>
</li>
<li>d-&gt;setupRecentlyLoadedMenu(d-&gt;RecentlyLoadedFileProperties);</li>
<li>
</li>
<li>// Keep the settings up-to-date</li>
<li>qSlicerAppMainWindowPrivate::writeRecentlyLoadedFiles(d-&gt;RecentlyLoadedFileProperties);</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Regarding the python API it’s true that we don’t have good documentation.  <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jcfr">@jcfr</a> have some ideas - definitely we want to start keeping the programming documentation in a repository that is versioned with the code so things stay in sync.</p>

---
