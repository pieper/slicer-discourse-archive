---
topic_id: 41930
title: "Segmentation In Slicer Extremely Slow When Using The Scissor"
date: 2025-03-02
url: https://discourse.slicer.org/t/41930
---

# Segmentation in Slicer extremely slow when using the Scissors tool in slice view

**Topic ID**: 41930
**Date**: 2025-03-02
**URL**: https://discourse.slicer.org/t/segmentation-in-slicer-extremely-slow-when-using-the-scissors-tool-in-slice-view/41930

---

## Post #1 by @Russell_Engelman (2025-03-02 17:28 UTC)

<p><strong>Operating System</strong> - Windows 10<br>
<strong>Slicer 3D Version</strong> - 5.8.0</p>
<p>I am working with a dataset of a (cleaned, so no flesh) skull with the teeth in occlusion, so I have to separate the upper and lower jaws to get the morphological data I need.</p>
<p>I have done this by thresholding the entire skull and then manually separating the upper and lower jaws using the scissors tool, particularly in areas where the teeth and TMJ are in contact. This is being done in slice view with 3D visualization turned off.</p>
<p>Attempting to draw on a slice to add/remove voxels from a layer often takes 10-20 seconds for Slicer 3D to process each action, compared to near-instant in other CT programs (e.g., Amira/Avizo). The size of voxel area being selected does not matter, timing a selection with a slice cut depth of 0 mm (immediate slice only) as well as one set to “unlimited” both took around 15 seconds.</p>
<p>This has occurred with multiple datasets, one 3.19 gB, one 3.03 gB, and one only about 860 mB, ruling out corruption of the data. The physical RAM on my system is close to or greater than 10x the size of these datasets in all cases. Task Manager reports only 69% of total memory is in use. During an action this increases to ~80%, but the program does not appear to be hitting memory limits.</p>
<p>All other programs such as web browsers were not open at this time. Slicer is also updated to the most recent version. Other colleagues have reported similar observations that Slicer 3D is extremely slow when trying to segment their datasets, though the size and other parameters of these data were not provided.</p>
<p>The thresholding tool works is a relatively timely manner. It also takes about 15 seconds to threshold the entire dataset, despite the amount of data processed being much larger. While thresholding the amount of memory used in Task Manager will hit 95-98% of total available memory space. This suggests the issue may be a glitch with the Scissors tool specifically, rather than a limit of too little RAM.</p>
<p>Checking the forum other users appear to have reported near-identical issues in the past (example: <a href="https://discourse.slicer.org/t/segmentation-tools-very-slow-for-file-above-a-few-hundred-mb/8701" class="inline-onebox">Segmentation tools very slow for file above a few hundred Mb</a>). I have tried several of the solutions seen in these threads (e.g., removing a Wacom tablet), but with no luck. I am passing this on as the issue appears to persist in the most recent stable release of Slicer 3D.</p>

---

## Post #2 by @pieper (2025-03-02 19:28 UTC)

<p><a class="mention" href="/u/russell_engelman">@Russell_Engelman</a> thanks for reporting this.  We want the software to perform well for people, and often there settings or other considerations that may be unique to the way you are using the program.</p>
<p>Would you be able to help solve this by doing the steps I asked for in the issue you linked?</p>
<aside class="quote" data-post="3" data-topic="8701">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-tools-very-slow-for-file-above-a-few-hundred-mb/8701/3">Segmentation tools very slow for file above a few hundred Mb</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Also, if you watch a few of the videos on the tutorial pages you’ll see how slicer works for us, and you can also try some of our SampleData.  If you find scenarios or data that don’t perform well can you share a short screen video to illustrate what you did?
  </blockquote>
</aside>


---

## Post #3 by @Russell_Engelman (2025-03-02 20:12 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<blockquote>
<p>Would you be able to help solve this by doing the steps I asked for in the issue you linked?</p>
</blockquote>
<p>Is there any way I can share a screen video on this site? I recorded one replicating the error but the file itself is 25 mB and when I try to upload it I get an error message the file is too large.</p>

---

## Post #4 by @pieper (2025-03-02 22:54 UTC)

<p>Thanks, that should help.  You can put it on someplace like google drive or dropbox and paste a link here.</p>

---

## Post #5 by @Russell_Engelman (2025-03-03 04:15 UTC)

<p>This should be the link to the video. The slow processing occurs around 1:10 and I show it twice.</p>
<p>“<a href="https://www.dropbox.com/scl/fi/sylq5np0azpcexyn9aab8/3D-Slicer-5.2.2-2025-03-02-15-06-13.mp4?rlkey=ngq56gzgykjkwc30gcw9xzyr4&amp;dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fi/sylq5np0azpcexyn9aab8/3D-Slicer-5.2.2-2025-03-02-15-06-13.mp4?rlkey=ngq56gzgykjkwc30gcw9xzyr4&amp;dl=0</a>”</p>

---

## Post #6 by @muratmaga (2025-03-03 05:08 UTC)

<p>Couple issues,</p>
<ol>
<li>You did not set the correct spacing of your data. I highly doubt the image spacing of this scan is 1x1x1mm. While this will not affect things like segmentation, if you are planning to take measurement, or calculate volumes/areas, they will be wrong.</li>
<li>You dataset is approximately 4GB, which is fairly large. I noticed you are using Scissors tool like a drawing tool (since you set the expansion to 0mm, meaning you are only changing that slice). Is there are reason you are doing that? Draw effect is exactly for what you are doing and may work faster.  I mean I don’t know if people if people ever tested the Scissor’s tools usage like that, most people use it as a 3D tool.</li>
</ol>

---

## Post #7 by @jamesobutler (2025-03-03 06:46 UTC)

<p><a class="mention" href="/u/russell_engelman">@Russell_Engelman</a> Thank you for the initial video. Would you be able to repeat the creation of this video again, but instead use latest Slicer stable 5.8.0? Your original report on this thread details Slicer 5.8.0, but I notice from your video filename that it appears you are using Slicer 5.2.2 which is over 2 years old. There have been quite a few updates to various dependencies that may impact performance and developers want to make sure we are comparing against latest code to make sure this issue hasn’t already been resolved in the past 2 years of development.</p>

---

## Post #8 by @Russell_Engelman (2025-03-07 22:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<ol>
<li>You did not set the correct spacing of your data. I highly doubt the image spacing of this scan is 1x1x1mm. While this will not affect things like segmentation, if you are planning to take measurement, or calculate volumes/areas, they will be wrong.</li>
</ol>
</blockquote>
</aside>
<p>The purpose of this video was merely meant to replicate the issue in question. I have also done this before with the space thickness set to the actual values for the specimen and the loading time was unaffected.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I noticed you are using Scissors tool like a drawing tool (since you set the expansion to 0mm, meaning you are only changing that slice). Is there are reason you are doing that?</p>
</blockquote>
</aside>
<p>I was using the Scissors tool because this is what I had been explicitly told was Slicer 3D’s equivalent to the Lasso tool in other CT software when asked on this forum previously. See attached link. The description I was given of the Draw tool implied it was not suitable for creating a complex segmentation or trimming the results of a thresholding because it was said it would overwrite if a new region was drawn.</p>
<aside class="quote" data-post="2" data-topic="29383">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-there-a-lasso-tool-in-the-segment-editor-module-in-slicer/29383/2">Is there a Lasso tool in the Segment Editor module in Slicer?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can set the slice thickness for Scissors tool (set thickness to 0 to limit it to the current slice). You can also use the Draw tool (if you draw another segment then it will be erased from the current segment). You can use masking settings to limit editing inside a selected segment (so that you only need to pay attention when you draw the contour inside the segment). 
You may save time by segmenting manually on every 5th slice and then fill between using the “Fill between slices” effect.
  </blockquote>
</aside>

<aside class="quote no-group" data-username="jamesobutler" data-post="7" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Would you be able to repeat the creation of this video again, but instead use latest Slicer stable 5.8.0?</p>
</blockquote>
</aside>
<p>I can do this. I had thought I was using Slicer 5.8.0 but I suppose if the filename said otherwise it must be the case. When I had checked the documentation it said 5.8.0, but I wonder if what happened is that I downloaded the newer version but forgot to uninstall the old one, so when I searched for the program documentation it brought the newer file up.</p>

---

## Post #9 by @muratmaga (2025-03-07 23:00 UTC)

<aside class="quote no-group" data-username="Russell_Engelman" data-post="8" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/russell_engelman/48/18425_2.png" class="avatar"> Russell_Engelman:</div>
<blockquote>
<p>The description I was given of the Draw tool implied it was not suitable for creating a complex segmentation or trimming the results of a thresholding because it was said it would overwrite if a new region was drawn.</p>
</blockquote>
</aside>
<p>That is incorrect. Whether a tool draws over a segment, or outputs to a different segment is uniformly controlled from the Masking option that are present for all the segmentation tools.</p>
<p>I highly encourage you to look at official documentation in addition to learning from individuals, which maybe variably informed on such tasks.</p>

---

## Post #10 by @lassoan (2025-03-08 00:48 UTC)

<p><a class="mention" href="/u/russell_engelman">@Russell_Engelman</a> maybe you could join one of the Slicer weekly meetings on Tuesdays at 10am. You could show your workflow and could get advice from Slicer developers and expert users.</p>

---

## Post #11 by @muratmaga (2025-03-08 01:23 UTC)

<p>Also, if you can attend, you might find the upcoming SlicerMorph 101: Introduction to 3D Morphology with Slicer and SlicerMorph short course useful. Here is the application link:</p>
<aside class="onebox googledocs" data-onebox-src="https://docs.google.com/forms/d/e/1FAIpQLSdY-eq8RJw15bC6ArcJFJUwHTBBTq8ce3bBIU4qKgQi8GuPgQ/viewform?usp=dialog">
  <header class="source">

      <a href="https://docs.google.com/forms/d/e/1FAIpQLSdY-eq8RJw15bC6ArcJFJUwHTBBTq8ce3bBIU4qKgQi8GuPgQ/viewform?usp=dialog" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSdY-eq8RJw15bC6ArcJFJUwHTBBTq8ce3bBIU4qKgQi8GuPgQ/viewform?usp=dialog" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-forms-logo"></span></a>

<h3><a href="https://docs.google.com/forms/d/e/1FAIpQLSdY-eq8RJw15bC6ArcJFJUwHTBBTq8ce3bBIU4qKgQi8GuPgQ/viewform?usp=dialog" target="_blank" rel="noopener nofollow ugc">SlicerMorph 101 - Short Course on 3D Digital Morphology (March 31st-April 3rd,...</a></h3>

<p>This is an introductory course for 3D digital morphology using 3D Slicer and its SlicerMorph extension. Some of the topics we will cover include:
Importing data (imagestacks)
Visualization (volume rendering)
Segmentation and...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @Russell_Engelman (2025-03-14 17:10 UTC)

<p>Okay, I did what <a class="mention" href="/u/jamesobutler">@jamesobutler</a> asked and repeated the same thing in the newest stable release of 3D Slicer (Slicer 5.8.1). The problem persisted. The same dataset was loaded in (a skull of <em>Vormela peregusna</em>, hereafter <em>Vormela</em>, total dataset size 3.19 gB) and a section of the thresholded dataset in one slice was moved from one layer to another using the “Scissors” tool with slice width set to 0. The time to complete the action was slightly faster than in Slicer 5.2.2 (~16-18 seconds versus 20+), but there was still a significant delay. 3D view was turned off the entire time. As mentioned before the amount of RAM on my device (32 gB) is about 10x that of the <em>Vormela</em> scan.</p>
<p>Following advice I was given I tried using the Draw tool to see if that produced a faster result. This was not the case, processing time was still 16+ seconds when the Draw tool was used.</p>
<p>Here is a link to a video documenting this for both the Draw and Scissors tool.</p>
<p>(<a href="https://www.dropbox.com/scl/fi/yubsuw0y278h7g6j0s814/3D-Slicer-5.8.1-2025-03-14-12-34-44.mp4?rlkey=ywfjpb53gz7c4m1h7bjcd2hf8&amp;st=ehdwymo2&amp;dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fi/yubsuw0y278h7g6j0s814/3D-Slicer-5.8.1-2025-03-14-12-34-44.mp4?rlkey=ywfjpb53gz7c4m1h7bjcd2hf8&amp;st=ehdwymo2&amp;dl=0</a>)</p>
<p>I tried changing the viewport to just the green window to see if limiting visualization to one axis sped up processing time. Processing still took about 16 seconds for both.</p>
<p>I also tried reading in a much smaller DICOM scan of <em>Carcharhinus dussumieri</em> that was only 770 mB in size to see how much scan size affected this. Processing time was 4 seconds for both the Scissors and the Draw tool, much faster than the <em>Vormela</em> scan but still a noticeable lag for a scan that was significantly smaller than my system’s RAM.</p>
<p>I read the <em>Vormela</em> specimen into Avizo 7 and performed the same action (thresholding, then moving data from the same region into a distinct layer using the Lasso tool) as a point of comparison. This action took only 3-4 seconds to perform.</p>
<p>(<a href="https://www.dropbox.com/scl/fi/1hklgcm5zanlbkfnv6lvv/Avizo-Standard-Edition-Untitled-2025-03-14-12-57-40.mp4?rlkey=jgsygfck1qs2g4k4rojyu0rhc&amp;st=t399axwn&amp;dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fi/1hklgcm5zanlbkfnv6lvv/Avizo-Standard-Edition-Untitled-2025-03-14-12-57-40.mp4?rlkey=jgsygfck1qs2g4k4rojyu0rhc&amp;st=t399axwn&amp;dl=0</a>)</p>
<p>Because my copy of Avizo 7 is on a different, older machine than my main working computer I downloaded Slicer 5.8.1 on that machine and performed the same function to make sure the difference in performance was not due to differences in operating system, version, or available RAM. The delay on this machine was approximately 28 seconds per action.</p>
<p>(<a href="https://www.dropbox.com/scl/fi/zwn1vaq52scre8vis2dw6/3D-Slicer-5.8.1-2025-03-14-12-56-15.mp4?rlkey=jnzbpmftv75iiyev379m4t3vp&amp;st=ias8drhs&amp;dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fi/zwn1vaq52scre8vis2dw6/3D-Slicer-5.8.1-2025-03-14-12-56-15.mp4?rlkey=jnzbpmftv75iiyev379m4t3vp&amp;st=ias8drhs&amp;dl=0</a>)</p>

---

## Post #13 by @muratmaga (2025-03-14 17:34 UTC)

<p>Is it possible to share your data?</p>
<p>I did an experiment on my macbook with 32GB of RAM, and blow up a dataset approximately the size of yours (~4GB), and did the steps you have done. Cutting sections into new segments via draw and scissors tool with the way you are doing took about 5-10 seconds, depending on the size of the contour I made, which seemed reasonable on my laptop.</p>
<p>What are the specs of your computer beyond RAM (like the CPU/GPU on them)?</p>

---

## Post #14 by @Russell_Engelman (2025-03-15 03:42 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="41930" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is it possible to share your data?</p>
</blockquote>
</aside>
<p>Yes. The <em>Vormela</em> scan is openly available online and can be found at the following link…</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://deepblue.lib.umich.edu/data/concern/data_sets/4b29b6830">
  <header class="source">

      <a href="https://deepblue.lib.umich.edu/data/concern/data_sets/4b29b6830" target="_blank" rel="noopener nofollow ugc">Deep Blue Data</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="http://deepblue.lib.umich.edu/downloads/z890rv240" class="thumbnail">

<h3><a href="https://deepblue.lib.umich.edu/data/concern/data_sets/4b29b6830" target="_blank" rel="noopener nofollow ugc">Computed tomography voxel dataset for ummz:mammals:57841-Vormela peregusna...</a></h3>

  <p>Scan of specimen ummz:mammals:57841 (Vormela peregusna peregusna) - Skull. Raw Dataset includes 1601 TIF images (each 1036 x 1784 x 1 voxel at 0.03049953 mm resolution, derived from 1601 scan proje...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>That said, the problem is not unique to this scan but I have had it with multiple CT datasets downloaded from MorphoSource. I had similar issues with <a href="https://www.morphosource.org/concern/biological_specimens/000569301?locale=en" rel="noopener nofollow ugc">this scan</a> of <em>Mungotictis decimlineata</em>, for example. Indeed, this has been a problem with almost every dataset I have loaded into 3D Slicer except for very small ones.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="41930" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>What are the specs of your computer beyond RAM (like the CPU/GPU on them)?</p>
</blockquote>
</aside>
<p>For the first computer it is…</p>
<p><strong>Computer</strong> - Dell Precision 5820 Tower<br>
<strong>Software OS</strong> - Windows 10<br>
<strong>Total RAM</strong> - 32 gB<br>
<strong>CPU</strong> - Intel(R) Xeon(R) W-2225 CPU @ 4.10 gHz<br>
<strong>GPU</strong> - NVIDIA RTX A4500<br>
64 bit operating system, 4 cores</p>
<p>For the second (the one with Avizo 7 and the one where Slicer took 28 seconds to work per action) it is…</p>
<p><strong>Computer</strong> - Dell Precision 7710<br>
<strong>Software OS</strong> - Windows 10 Pro<br>
<strong>Total RAM</strong> - 64 gB<br>
<strong>CPU</strong> - Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80 gHz<br>
<strong>GPU</strong> - NVIDIA Quadro M3000M</p>

---

## Post #15 by @muratmaga (2025-03-15 18:33 UTC)

<aside class="quote no-group" data-username="Russell_Engelman" data-post="14" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/russell_engelman/48/18425_2.png" class="avatar"> Russell_Engelman:</div>
<blockquote>
<p>For the second (the one with Avizo 7 and the one where Slicer took 28 seconds to work per action) it is…</p>
</blockquote>
</aside>
<p>So your computer specs are fairly old and low. The type of things you are trying to do will benefit having more cores on your computer.</p>
<p>As for taking things being slow on Slicer compared to the Avizo the same computer, are you sure you are doing exactly the same thing?</p>
<p>For example, if I don’t do the  masking option (i.e., I created a thresholded segment, then I use scissors or draw tool to transfer the contents of that from Segment_1 to Segment_2) things are also instantaneous for me.  Is that how you are segmenting in Avizo (i.e did you create fully thresholded segment, and then you are subtracting things from it)?</p>
<p>If your goal is to do slice-by-slice segmentation, you can achieve the same thing without doing what you are doing by setting your threshold range for masking to the global threshold, and using the draw tool to outline the mandible at every slice. That operaiton should be instantaneous or near instantaneous.</p>

---

## Post #16 by @Russell_Engelman (2025-03-16 14:49 UTC)

<blockquote>
<p>So your computer specs are fairly old and low. The type of things you are trying to do will benefit having more cores on your computer.</p>
</blockquote>
<p>Is the Dell 5820 really that old? The 7710 is definitely an older computer, but the 5820 is a one that was bought new from the dealer within the last year to (in part) replace it. On the 5820 it still took 18-20 seconds per action.</p>
<blockquote>
<p>For example, if I don’t do the masking option (i.e., I created a thresholded segment, then I use scissors or draw tool to transfer the contents of that from Segment_1 to Segment_2) things are also instantaneous for me. Is that how you are segmenting in Avizo (i.e did you create fully thresholded segment, and then you are subtracting things from it)?</p>
</blockquote>
<p>I don’t understand. I am pretty sure I am doing the same thing. If I don’t do the masking option there doesn’t seem to be a way to transfer the contents of Segment 1 to Segment 2. When I try doing it via the Draw or Scissors tool it instead takes the entire circled area instead of just the material in Segment 1.</p>
<p>That is definitely how I am segmenting things in Avizo, at least.</p>
<blockquote>
<p>If your goal is to do slice-by-slice segmentation, you can achieve the same thing without doing what you are doing by setting your threshold range for masking to the global threshold, and using the draw tool to outline the mandible at every slice. That operaiton should be instantaneous or near instantaneous.</p>
</blockquote>
<p>Again, I am unclear how to do this and in what way it differs from the previous workflow. I checked the Draw tool and there doesn’t seem to be any option to set a masking threshhold. I checked the Threshold tool and there is an option to use a local histogram for masking, but that sends me to the Paint tool.</p>
<p>So…and I <em>think</em> this is what you meant, I set the local histogram to match the values of the specimen for masking in the Threshold tool, and then it gave me an option to use it for masking in the Draw tool. When I did this it did select the correct outline for the specimen, but still took about 16-18 seconds to complete per action on the Dell Precision 5820.</p>

---

## Post #17 by @pieper (2025-03-16 15:57 UTC)

<aside class="quote no-group" data-username="Russell_Engelman" data-post="16" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/russell_engelman/48/18425_2.png" class="avatar"> Russell_Engelman:</div>
<blockquote>
<p>Draw tool and there doesn’t seem to be any option to set a masking threshhold.</p>
</blockquote>
</aside>
<p>Did you try using the “Enable intensity range” in the Draw tool?  This is what gets enabled when you click “Use for masking” in the threshold tool.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b023d75bcf691df82b0ab973ce3c4b23e374ff0.png" data-download-href="/uploads/short-url/3QVGQnLBZsE9vLWEri1X7dAUMta.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b023d75bcf691df82b0ab973ce3c4b23e374ff0.png" alt="image" data-base62-sha1="3QVGQnLBZsE9vLWEri1X7dAUMta" width="425" height="147"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">425×147 8.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @muratmaga (2025-03-17 03:46 UTC)

<aside class="quote no-group" data-username="Russell_Engelman" data-post="16" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/russell_engelman/48/18425_2.png" class="avatar"> Russell_Engelman:</div>
<blockquote>
<p>Is the Dell 5820 really that old? The 7710 is definitely an older computer, but the 5820 is a one that was bought new from the dealer within the last year to (in part) replace it. On the 5820 it still took 18-20 seconds per action.</p>
</blockquote>
</aside>
<p>It is not so much being old, but it is the CPU having very few cores (only 4). Most operations in Slicer are multi-threaded so they benefit from having more cores. Having more cores are useful when working with large datasets.</p>
<aside class="quote no-group" data-username="Russell_Engelman" data-post="16" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/russell_engelman/48/18425_2.png" class="avatar"> Russell_Engelman:</div>
<blockquote>
<p>I don’t understand. I am pretty sure I am doing the same thing. If I don’t do the masking option there doesn’t seem to be a way to transfer the contents of Segment 1 to Segment 2.</p>
</blockquote>
</aside>
<p>The difference is this: With this approach you already created a  segment with a global threshold (Segment_1). Then you are asking it to find in this 3D volume and then extract from it and move to a new segment. This is a very costly operation, since it is looking at the entire 3D segmented volume to find which voxels are in it extracted. There are places to use this approach, but not for this slice-by-slice option, where there are much faster alternatives.</p>
<p>So start from the scratch, create your segment_1, then go to the threshold tool, set your threshold range, and instead of hitting APPLY, hit USE for MASKING.  Then switch to the Draw tool, and make the same contour. It should only select the voxels within the contour and also within the selected threshold range.</p>
<p>This should be really fast, and probably is closer to what you are doing in Aviso.</p>

---

## Post #19 by @Russell_Engelman (2025-03-26 03:25 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="18" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It is not so much being old, but it is the CPU having very few cores (only 4). Most operations in Slicer are multi-threaded so they benefit from having more cores. Having more cores are useful when working with large datasets.</p>
</blockquote>
</aside>
<p>That makes more sense.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="18" data-topic="41930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So start from the scratch, create your segment_1, then go to the threshold tool, set your threshold range, and instead of hitting APPLY, hit USE for MASKING. Then switch to the Draw tool, and make the same contour. It should only select the voxels within the contour and also within the selected threshold range.</p>
<p>This should be really fast, and probably is closer to what you are doing in Aviso.</p>
</blockquote>
</aside>
<p>I can try this, and see if it works.</p>

---
