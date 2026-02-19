---
topic_id: 8259
title: "Two Stl File Alignment And Measurement"
date: 2019-09-02
url: https://discourse.slicer.org/t/8259
---

# TWO .stl file alignment and measurement

**Topic ID**: 8259
**Date**: 2019-09-02
**URL**: https://discourse.slicer.org/t/two-stl-file-alignment-and-measurement/8259

---

## Post #1 by @manjula (2019-09-02 13:10 UTC)

<p>Hi, i am researcher in Malmo University.  I am planning to conduct a research on dental implants.  I would be grateful if someone can help me with the problems that i have.</p>
<ol>
<li>Can 3D Slicer be used to to align (superimpose) two .stl files of the same patient ?</li>
</ol>
<p>I will be using the surface scanner (3shape) to scan the patients pre and post operative. (the two stl files pre and post <a href="https://www.transfernow.net/857y81q1ziko" rel="noopener nofollow ugc">https://www.transfernow.net/857y81q1ziko</a> ).</p>
<ol start="2">
<li>If so can 3D Slicer be used to compare and make measurements of the difference in bone height and soft tissue heights ?</li>
</ol>
<p>like in this one <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a84027551bb5df185eba39da3ad8ad11f484774f.jpeg" data-download-href="/uploads/short-url/o0pF8NMzyYk39z6CGLJQwAs5fkz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a84027551bb5df185eba39da3ad8ad11f484774f_2_690x347.jpeg" alt="image" data-base62-sha1="o0pF8NMzyYk39z6CGLJQwAs5fkz" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a84027551bb5df185eba39da3ad8ad11f484774f_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a84027551bb5df185eba39da3ad8ad11f484774f_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a84027551bb5df185eba39da3ad8ad11f484774f.jpeg 2x" data-dominant-color="CEEBCC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1332×670 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> . They have used the Geomagic quantify to do this research.</p>
<ol start="3">
<li>If these can be done can somebody be kind enough to direct me on how to superimpose (Align/register) the two STL files and then make quantitative measurement of the difference of the pre and post scans  ?</li>
</ol>
<p>Kind regards</p>
<p>Manjula</p>

---

## Post #2 by @steffen-o (2019-09-04 14:01 UTC)

<p>Have a look at this thread:</p><aside class="quote quote-modified" data-post="1" data-topic="7818">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/43a26b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/align-2-segment-1-stl-and-1-segment/7818">Align 2 segment 1 stl and 1 segment</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Is there a solution to align 2 objects (1 STL IMPORT and 1 segment )with a lot of acurate 
Maybe an extention. 
thanks a lot for your advice 
jean-marc[align]
  </blockquote>
</aside>


---

## Post #3 by @manjula (2019-09-05 11:06 UTC)

<p>Hi Steffen-o,</p>
<p>Thank you for the direction. It solved my first problem.</p>
<p>And i need to figure out how to do the measurement and the colour map.</p>
<p>Thank you again.</p>

---

## Post #4 by @seanchoi0519 (2021-04-19 10:00 UTC)

<p>Hello Manjula</p>
<p>How do you do. I am a dental student at UQ working on a similar research project for my final year requirement - aligning 2 STL tooth models for endodontic research purposes. I was wondering if you were able to find any methods to do the measurement and the colour map.</p>
<p>Any advice &amp; direction would be appreciated!</p>
<p>Sean</p>

---

## Post #5 by @manjula (2021-04-19 16:27 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="4" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>How do you do. I am a dental student at UQ working on a similar research project for my final year requirement - aligning 2 STL tooth models for endodontic research purposes. I was wondering if you were able to find any methods to do the measurement and the colour map.</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>I have tried virtually all methods available in 3D Slicer for surface registration and found the IGT fiducial registration method, a semi automatic method to be the most useful one.</p>
<p>However, I no longer use any 3D Slicer-based tools for registration as results are subpar and take too much time and uses the ICP registration addon in the Blender which is a fully automatic tool and works wonderfully well.</p>
<p>you can find this add-on in github and install it on Blender. It is very easy to use.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/patmo141/object_alignment">
  <header class="source">

      <a href="https://github.com/patmo141/object_alignment" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/5f9df1835c5fc6797351f474fe4b7766/patmo141/object_alignment" class="thumbnail">

  <h3><a href="https://github.com/patmo141/object_alignment" target="_blank" rel="noopener nofollow ugc">GitHub - patmo141/object_alignment: picked points and ICP alignment addon for Blender</a></h3>

    <p><span class="github-repo-description">picked points and ICP alignment addon for Blender</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can see the discussion I had on this topic, with very useful input from others at,</p>
<aside class="quote quote-modified" data-post="1" data-topic="8364">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/stl-models-alignment-and-volume-measurement/8364">STL models - Alignment and Volume measurement</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hi, 
Our Input - 2 STL surface scan models  (PreOp and Post Op) - from the 3Shape surface scanner. 
We have two problems. 


Need to accurately align the pre and post op surface scans ? (they have fixed landmarks) 


Need to measure the change of volume in the region of interest ? ( the volume of bone resorption) 


So far, we have install CMF registration and, 
as you can see from the pictures the alignment with CMF surface registration is not accurate enough. 
[PreOperative] 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dfd655d9175ff97f94b98986013de29a921c1a6.jpeg" data-download-href="/uploads/short-url/1ZL6xmFVrjiW5xSe8aNpfh8Yrem.jpeg?dl=1" title="SuperImposed" rel="noopener nofollow ugc">[SuperImposed]</a> 
W…
  </blockquote>
</aside>

<p><strong>Colour maps</strong></p>
<p>I use the model to model distance and shape population viewer in the 3D slicer to create the color maps.</p>
<p><strong>measurement</strong></p>
<p>What measurements you need ? If you are going to segment the structures then you can use the segment editor statistics to measure. Also there are lots of other measurement tools available but will depend on what you need to measure and using what type of data.</p>

---

## Post #6 by @muratmaga (2021-04-19 16:44 UTC)

<aside class="quote no-group" data-username="manjula" data-post="5" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I have tried virtually all methods available in 3D Slicer for surface registration and found the IGT fiducial registration method, a semi automatic method to be the most useful one.</p>
</blockquote>
</aside>
<p>Have you tried ALPACA, which is part of SlicerMorph? <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ALPACA" class="inline-onebox">SlicerMorph/Docs/ALPACA at master · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>It is meant to transfer the landmarks via registration. But you can also use to register models. (You will have to create a fiducial node with at least one point in it to initiate the process, once you start, you can ignore it).</p>

---

## Post #7 by @seanchoi0519 (2021-04-20 13:32 UTC)

<p>Manjula, thank you for the pieces of gem you’ve outlined here.<br>
I will have a thorough look at the two softwares you’ve recommended.</p>
<p>Regarding your question of what measurement I need - essentially, I will need to calculate the difference between the 2 STL mesh files in terms of mm (length) once they are aligned. If absolute measurement is not possible, just a relative distance would suffice. Essentially it would give you feedbacks on the quality of your access cavity preparation (whether it’s too wide, deep, etc.). Would you be able to point me in the right direction?</p>
<p>Thanks again,<br>
Sean</p>

---

## Post #8 by @seanchoi0519 (2021-04-20 13:32 UTC)

<p>Hi, thanks for this.<br>
I will have a go at it later today.</p>

---

## Post #9 by @seanchoi0519 (2021-04-20 13:59 UTC)

<p>Hello muratmaga,</p>
<p>I’ve had a look at ALPACA and it seems like it requires a .ply file format &amp; .fcsv landmark file.</p>
<ol>
<li>If possible, I’m looking to work with .stl files. Would there be a way to work around this?</li>
<li>How could I obtain the landmark for a .stl file? Would you mind elaborating on creating a fiducial node  to initiate the process?</li>
</ol>
<p>My apologies, I am not too techy which is why I’m studying dentistry <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>
<p>Sincerely</p>
<p>Sean</p>

---

## Post #10 by @muratmaga (2021-04-20 14:40 UTC)

<p>If you loaded your stl models into slicer, you can save them as ply. We don’t like stl, due to potential issues with physical scale.</p>
<p>As for the fiducial, you only need to create a single point and save it as fcsv.</p>
<p><a class="mention" href="/u/agporto">@agporto</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> should we consider making the interactive mode work with data loaded into the scene as oppose to load from the disk?</p>

---

## Post #11 by @lassoan (2021-04-20 15:48 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We don’t like stl, due to potential issues with physical scale.</p>
</blockquote>
</aside>
<p>I’m not aware of any standard way of specifying coordinate system unit in either STL or PLY. You can include comments in both formats to specify any additional information (we use this for specifying the coordinate system axis directions), but these are not part of the file format but these are conventions that users has to agree on and use consistently.</p>
<p>Nevertheless, PLY is a much more capable format than STL and not much more complicated, so it makes a lot of sense to use PLY.</p>
<aside class="quote no-group" data-username="seanchoi0519" data-post="9" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>I’ve had a look at ALPACA and it seems like it requires a .ply file format &amp; .fcsv landmark file.</p>
</blockquote>
</aside>
<p>It makes sense for Alpaca to require files for its batch mode, but I would consider it as a bug that it requires file input for registering a single pair of models. It would be trivial to replace the file selectors by node selectors.</p>
<p>I believe Alpaca will work better than Blender’s ICP, as Alpaca offers precise control over what is registered by means of landmark points and because it supports non-linear warping transforms as well. Alpaca just have to be made more user-friendly for simple cases (make it work without requiring even a single landmark point, make it easy to add/remove landmark points in the module using markup place widget, etc.).</p>

---

## Post #12 by @muratmaga (2021-04-20 16:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It makes sense for Alpaca to require files for its batch mode, but I would consider it as a bug that it requires file input for registering a single pair of models. It would be trivial to replace the file selectors by node selectors.</p>
</blockquote>
</aside>
<p>We have designed ALPACA with a specific use case in mind, but looks like it can be useful to the people for other things (like alignment). I think few additional changes will also be useful (like actually saving transforms).</p>

---

## Post #13 by @agporto (2021-04-20 16:53 UTC)

<p>One option would be to make the landmark transfer as an optional step in the pipeline. It would be fairly straightforward to do that. I also like the idea of registering models loaded in the scene when using the pairwise tab.</p>

---

## Post #14 by @seanchoi0519 (2021-04-20 17:11 UTC)

<p>Thanks for the feedbacks.<br>
As you guys have mentioned, removing the requirement of landmark point would be great. 3D scanning is still relatively new in the dentistry field and a seamless alignment process would make a huge impact in the implant, prosthodontic, and endodontic field.</p>
<p>Ps. I tried the ALPACA once I converted the files to .ply format &amp; transferring a landmark and the alignment worked fantastically. Thanks a lot.</p>

---

## Post #15 by @seanchoi0519 (2021-04-20 17:14 UTC)

<p>Hello manjula</p>
<p>I was able to align the models using ALPACA successfully as others have advised.<br>
Now moving onto calculating the distance - you have mentioned that you use the model to model distance &amp; shape population viewer.</p>
<p>I have downloaded the model to model distance myself and am not sure where and how I am able to use the extension. How can I access the extension once I’ve downloaded it? Would you be able to provide a guidance? Also is .ply format compatible or is .vtk only compatible?</p>
<p>Thanks a lot</p>

---

## Post #16 by @manjula (2021-04-21 01:36 UTC)

<aside class="quote no-group quote-modified" data-username="seanchoi0519" data-post="15" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>How can I access the extension once I’ve downloaded it? Would you be able to provide guidance? Also is .ply format compatible or is .vtk only compatible?</p>
</blockquote>
</aside>
<p>You can search for the model to model in find module or else it is listed under the quantification category. Also it works with ply format.</p>

---

## Post #17 by @manjula (2021-04-21 14:09 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Have you tried ALPACA, which is part of SlicerMorph? <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ALPACA" rel="noopener nofollow ugc">SlicerMorph/Docs/ALPACA at master · SlicerMorph/SlicerMorph · GitHub </a></p>
</blockquote>
</aside>
<p>I have tried it previously on your suggestions but I could not get it to work the way I wanted to.</p>
<p>I again tried it today, and for me, the results were the same.  I tried adjusting the parameters as well but could not get better results. If you have time please have a look and let me know if there is something i can do to improve the results. For comparison, I have attached the video of the ICP registration in Blender as well. can do the same thing within 20-30 seconds with the default settings.<br>
Please let me know if i am doing it wrong.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="LtwhLBIgIWI" data-video-title="simplescreenrecorder 2021 04 21 19 28 16" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=LtwhLBIgIWI" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/LtwhLBIgIWI/maxresdefault.jpg" title="simplescreenrecorder 2021 04 21 19 28 16" width="" height="">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="4mxlS0zGBbw" data-video-title="simplescreenrecorder 2021 04 21 19 23 50" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=4mxlS0zGBbw" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/4mxlS0zGBbw/maxresdefault.jpg" title="simplescreenrecorder 2021 04 21 19 23 50" width="" height="">
  </a>
</div>

<p>I have attached the sample files if you have time.</p>
<p><a href="https://drive.google.com/file/d/1rEgIvcsPByCH8GBotH919ltpq_tfQELi/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1rEgIvcsPByCH8GBotH919ltpq_tfQELi/view?usp=sharing</a></p>
<p><a href="https://drive.google.com/file/d/1kipMX-7JcqGFuOTa_gZD_CYzVPlv8bDO/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1kipMX-7JcqGFuOTa_gZD_CYzVPlv8bDO/view?usp=sharing</a></p>

---

## Post #18 by @seanchoi0519 (2021-04-21 15:19 UTC)

<p>Thanks for this manjula.<br>
Would you also mind providing a screen recording of you using the Module-to-Module distance &amp; shape population viewer?</p>
<p>There doesn’t seem to be many tutorials online.<br>
It would mean a lot to me!</p>
<p>Sean</p>

---

## Post #19 by @muratmaga (2021-04-21 15:30 UTC)

<aside class="quote no-group" data-username="manjula" data-post="17" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Please let me know if i am doing it wrong.</p>
</blockquote>
</aside>
<p>I don’t think you are doing anything wrong. I will leave the technical comments and more suggestions for improving the alignment to <a class="mention" href="/u/agporto">@agporto</a>, but we haven’t really thought about this use this in ALPACA, in which you have identical shapes with slight modification (a bone cut). We normally deal with geometries much more different.</p>
<p>With basically turning off everything as low as possible, I got this alignment which is not perfect but pretty close.</p>
<p><a class="mention" href="/u/agporto">@agporto</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> any other suggestions?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef0e59e918edddb0c444c46e6a881feb7a4d2ca5.png" data-download-href="/uploads/short-url/y6MRuu7bpOmizIWAQY4iAh4U1Cd.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef0e59e918edddb0c444c46e6a881feb7a4d2ca5_2_617x500.png" alt="image" data-base62-sha1="y6MRuu7bpOmizIWAQY4iAh4U1Cd" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef0e59e918edddb0c444c46e6a881feb7a4d2ca5_2_617x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef0e59e918edddb0c444c46e6a881feb7a4d2ca5_2_925x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef0e59e918edddb0c444c46e6a881feb7a4d2ca5.png 2x" data-dominant-color="D3CAD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×847 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @seanchoi0519 (2021-04-21 15:33 UTC)

<p>Hello</p>
<p>I just had one more question - what is “Run CPD non-rigid registration” for specifically?<br>
To me, “Run rigid alignment” seems to get most of the alignment done.</p>
<p>Thanks for the clarification.</p>

---

## Post #21 by @muratmaga (2021-04-21 15:37 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="18" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Would you also mind providing a screen recording of you using the Module-to-Module distance &amp; shape population viewer?</p>
</blockquote>
</aside>
<p>There is the screen capture of the resultant alignment run through Model to Model distance:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f16975645321b77496cfb6fb73c7ab6805e7a53d.png" data-download-href="/uploads/short-url/yrD0SZo3gFIfw5kIB1mNPtIoy0l.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f16975645321b77496cfb6fb73c7ab6805e7a53d_2_690x432.png" alt="image" data-base62-sha1="yrD0SZo3gFIfw5kIB1mNPtIoy0l" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f16975645321b77496cfb6fb73c7ab6805e7a53d_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f16975645321b77496cfb6fb73c7ab6805e7a53d_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f16975645321b77496cfb6fb73c7ab6805e7a53d.png 2x" data-dominant-color="C2CED5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1252×784 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is no tutorial, since there is not much to the module. You specify the reference model from which the distances will be calculated (fixed in this case) and then the target and choose to create a new model file as output. I slightly modified the visualization so anything within -1 to 1mm range is rendered green.</p>

---

## Post #22 by @muratmaga (2021-04-21 15:39 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="20" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>I just had one more question - what is “Run CPD non-rigid registration” for specifically?<br>
To me, “Run rigid alignment” seems to get most of the alignment done.</p>
</blockquote>
</aside>
<p>Depending on the question, you may skip the deformable registration. Rigid will only rotate and translate the mesh. Whereas deformable will non-linearly deform the mesh to match the others. Whether you need deformable or not depends on what you want to measure.</p>

---

## Post #23 by @manjula (2021-04-21 15:44 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="18" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Would you also mind providing a screen recording of you using the Module-to-Module distance &amp; shape population viewer</p>
</blockquote>
</aside>
<p>I learned via this tutorial,</p>
<div class="youtube-onebox lazy-video-container" data-video-id="Qen8ou5QsAw" data-video-title="5A 3D Craniofacial Quantification of Changes-Compute the Surface Distances using a Color Map" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Qen8ou5QsAw" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Qen8ou5QsAw/maxresdefault.jpg" title="5A 3D Craniofacial Quantification of Changes-Compute the Surface Distances using a Color Map" width="" height="">
  </a>
</div>


---

## Post #24 by @manjula (2021-04-21 15:46 UTC)

<p>thank you for testing. Yes i managed to get the same with your settings.  i was not using the settings properly as I was confused with the tooltips. Many thanks for the help.</p>

---

## Post #25 by @seanchoi0519 (2021-04-21 16:31 UTC)

<p>Thank you. Some great points here.<br>
If you wouldn’t mind, I had a couple follow-up questions.</p>
<ol>
<li>
<p>Is it possible for me to modify the -1 to 1mm threshold? For example I would like to be a little more precise, down to maybe within -0.3 to 0.3mm range.</p>
</li>
<li>
<p>Is it possible for me to see the difference of the “inside” of the model? I’ve tried reducing the opacity however it doesn’t seem to do much. For example, I have 2 tooth models - one of them has a hollow cavity preparation (it has been drilled), while the other has not. The model to model distance allows me to see the outside surface, however, I would like to see the distance INSIDE of the tooth as well if possible. Please see attached for reference.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee82bdc64848c1e38a19c1bb1644f191f892a76.jpeg" data-download-href="/uploads/short-url/y5t3Tdied1iSnSotAst18powrlk.jpeg?dl=1" title="Screen Shot 2021-04-22 at 2.25.57 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_422x500.jpeg" alt="Screen Shot 2021-04-22 at 2.25.57 AM" data-base62-sha1="y5t3Tdied1iSnSotAst18powrlk" width="422" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_422x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_633x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_844x1000.jpeg 2x" data-dominant-color="63917D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-22 at 2.25.57 AM</span><span class="informations">1426×1686 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>

---

## Post #26 by @seanchoi0519 (2021-04-21 16:33 UTC)

<p>Thanks manjula. Everything is fine with model-to-model distance, but somehow when I load the vtk file for shape population viewer, I get a weird result and am thinking I must be doing something wrong. Would you be able to have a look<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6cd5bab6ddd85770ccb82a9ed1945cee6cbba15.jpeg" data-download-href="/uploads/short-url/uEe9GYW50bSYocCo9YWdhRZ8EQJ.jpeg?dl=1" title="Screen Shot 2021-04-22 at 2.27.13 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6cd5bab6ddd85770ccb82a9ed1945cee6cbba15_2_659x500.jpeg" alt="Screen Shot 2021-04-22 at 2.27.13 AM" data-base62-sha1="uEe9GYW50bSYocCo9YWdhRZ8EQJ" width="659" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6cd5bab6ddd85770ccb82a9ed1945cee6cbba15_2_659x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6cd5bab6ddd85770ccb82a9ed1945cee6cbba15_2_988x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6cd5bab6ddd85770ccb82a9ed1945cee6cbba15_2_1318x1000.jpeg 2x" data-dominant-color="342B3C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-22 at 2.27.13 AM</span><span class="informations">3382×2566 558 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee82bdc64848c1e38a19c1bb1644f191f892a76.jpeg" data-download-href="/uploads/short-url/y5t3Tdied1iSnSotAst18powrlk.jpeg?dl=1" title="Screen Shot 2021-04-22 at 2.25.57 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_422x500.jpeg" alt="Screen Shot 2021-04-22 at 2.25.57 AM" data-base62-sha1="y5t3Tdied1iSnSotAst18powrlk" width="422" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_422x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_633x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee82bdc64848c1e38a19c1bb1644f191f892a76_2_844x1000.jpeg 2x" data-dominant-color="63917D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-22 at 2.25.57 AM</span><span class="informations">1426×1686 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #27 by @seanchoi0519 (2021-04-21 16:37 UTC)

<p>Ok I see. Thank you. I should be able to get away with just the rigid function!</p>

---

## Post #28 by @muratmaga (2021-04-21 16:47 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="25" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Is it possible for me to modify the -1 to 1mm threshold? For example I would like to be a little more precise, down to maybe within -0.3 to 0.3mm range.</p>
</blockquote>
</aside>
<p>I am not familiar with population shape viewer module. Instead I used the Models module’s Scalar Tab, after running the Model to Model Distance. There you can modify what values to be displayed by playing around with the Scalar Range Mode, and the Displayed Range settings.</p>

---

## Post #29 by @manjula (2021-04-22 10:01 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="26" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>hape population viewer, I get a weird result and am thinking I must</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/seanchoi0519">@seanchoi0519</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f43ff49fdccecb524feb16412bceabe70a6c300.png" data-download-href="/uploads/short-url/4sAu4bYMWdwrPZm8eP2aiyiCjPG.png?dl=1" title="Screenshot_32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f43ff49fdccecb524feb16412bceabe70a6c300_2_690x388.png" alt="Screenshot_32" data-base62-sha1="4sAu4bYMWdwrPZm8eP2aiyiCjPG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f43ff49fdccecb524feb16412bceabe70a6c300_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f43ff49fdccecb524feb16412bceabe70a6c300_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f43ff49fdccecb524feb16412bceabe70a6c300_2_1380x776.png 2x" data-dominant-color="9A8F9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_32</span><span class="informations">1920×1080 429 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thank you for the help with ALPACA and as you can see  I am now able to get good results.</p>

---

## Post #30 by @seanchoi0519 (2021-04-23 14:38 UTC)

<p>Thanks a lot for all your help</p>

---

## Post #31 by @seanchoi0519 (2021-04-23 14:41 UTC)

<p>Hello Arthur. This would be a great change as it would simplify the alignment process drastically.<br>
Would you guys have any plans to work on this?</p>
<p>I am trying to see if I can create a UI where I can simply drag and drop two .ply models (without the need for landmark transfer) and get the alignment done in a single step.</p>
<p>Any input would be appreciated.</p>

---

## Post #32 by @muratmaga (2021-04-23 15:05 UTC)

<p>Because ALPACA as a module is currently being reviewed in a paper, we are unlikely to make a change like that interim. Most likely that interactive alignment of meshes would be a separate module.</p>

---

## Post #33 by @seanchoi0519 (2021-04-23 15:12 UTC)

<p>I see thank you. I’m so glad I ran into ALPACA, it really works like magic.<br>
In the meanwhile, as my research project is due this coming July, would you guys mind if I attempt to make progress myself?</p>
<p>Any direction &amp; pointers as to how I can achieve it would be appreciated. I’m looking to</p>
<ol>
<li>Replace the file selectors by node selectors (ex. drag &amp; drop 3D models)</li>
<li>Remove the need for .fcsv file</li>
</ol>
<p>I have some basic programming knowledge so I am not sure if I can achieve it, but as Andras has mentioned, it is likely a trivial change so I hope I will be able to make some progress.</p>
<p>Thank you in advance</p>

---

## Post #34 by @muratmaga (2021-04-23 15:13 UTC)

<p>Source code of alpaca is here: <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ALPACA/ALPACA.py" class="inline-onebox">SlicerMorph/ALPACA.py at master · SlicerMorph/SlicerMorph · GitHub</a></p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> and <a class="mention" href="/u/agporto">@agporto</a> can help with your questions.</p>

---

## Post #35 by @seanchoi0519 (2021-04-23 15:30 UTC)

<p>Thank you. I had a read through the code and it seems like I may have to modify</p>
<p>io.read_point_cloud function to another function that will take the node as the input instead of file path. Please correct me if I’m wrong.</p>
<p>Would also love to implement a drag &amp; drop function somehow!</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/agporto">@agporto</a> can’t thank you enough - any advice would be appreciated</p>

---

## Post #36 by @pieper (2021-04-23 16:22 UTC)

<p>This is great <a class="mention" href="/u/seanchoi0519">@seanchoi0519</a>, thanks for jumping in <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Here’s an example of how the drag-and-drop works in python.  If you search through the code for the qt methods it uses you’ll see how this integrates with other ways drops are handled.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Scripted/DICOM/DICOM.py#L504" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Scripted/DICOM/DICOM.py#L504" target="_blank" rel="noopener">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Scripted/DICOM/DICOM.py#L504</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="494" style="counter-reset: li-counter 493 ;">
<li>      if not slicer.util.confirmYesNoDisplay("Import of files that have special (non-ASCII) characters in their names is not supported."</li>
<li>          " It is recommended to move files into a different folder and retry. Try to import from current location anyway?"):</li>
<li>        self.directoriesToAdd = []</li>
<li>        return</li>
<li>
</li>
<li>    slicer.util.selectModule('DICOM')</li>
<li>    slicer.modules.DICOMInstance.browserWidget.dicomBrowser.importDirectories(self.directoriesToAdd)</li>
<li>    self.directoriesToAdd = []</li>
<li>
</li>
<li>
</li>
<li class="selected">class DICOMLoadingByDragAndDropEventFilter(qt.QWidget):</li>
<li>  """This event filter is used for overriding drag-and-drop behavior while</li>
<li>  the DICOM module is active. To simplify DICOM import, while DICOM module is active</li>
<li>  then files or folders that are drag-and-dropped to the application window</li>
<li>  are always interpreted as DICOM data.</li>
<li>  """</li>
<li>
</li>
<li>  def eventFilter(self, object, event):</li>
<li>    """</li>
<li>    Custom event filter for Slicer Main Window.</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #37 by @agporto (2021-04-23 18:12 UTC)

<p>Hi Sean,<br>
A while ago, I started working on a module for pointcloud registration that I didn’t have time to finish. Perhaps that would be a good starting point (and I can help you a bit in updating it).<br>
It can be found at :</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/agporto/PointCloud-Registration/blob/main/PointCloudRegistration.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/agporto/PointCloud-Registration/blob/main/PointCloudRegistration.py" target="_blank" rel="noopener nofollow ugc">agporto/PointCloud-Registration/blob/main/PointCloudRegistration.py</a></h4>
<pre><code class="lang-py">##BASE PYTHON
import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin
import glob
import copy
import multiprocessing
import vtk.util.numpy_support as vtk_np
import numpy as np

#
# PointCloudRegistration
#

class PointCloudRegistration(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
</code></pre>

  This file has been truncated. <a href="https://github.com/agporto/PointCloud-Registration/blob/main/PointCloudRegistration.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
With regard to the io.read_point_cloud function, you can load a model from the scene with something like this:<br>
m = getNode(“Segment_1”)<br>
p = arrayFromModelPoints(m)<br>
cloud = o3d.geometry.PointCloud()<br>
cloud.points = o3d.utility.Vector3dVector(p)<br>
Anyway, if you want to start working on this, I can either give you access to the repo or you can create a branch and I can make some commits to it.</p>

---

## Post #38 by @seanchoi0519 (2021-04-29 15:26 UTC)

<p>Hello,</p>
<p>Thank you all for the feedbacks. I’ve spent some time to digest the code from the scripts this past week - however, I will admit that as a dental student with only basic coding background, it has not been easy creating modifications.</p>
<p>By any chance, would any of you be interested in developing &amp; creating extensions to the ALPACA with some funding? I do have some grants available that I can apply for from my university - and if it means accelerating the timeline of this project &amp; improving the quality of the final product, I am happy to look into this. The funding amount varies from $500-$1000 USD.</p>
<p>Here are some of the functionalities that I’m looking for:</p>
<ol>
<li>Enable drag-and-drop feature (something similar to attached pic)</li>
<li>Upon drag-and-drop and alignment, highlight areas for correction - (for ex. red = needs to be trimmed down, blue = must be added). I think this is possible via shape population viewer already - would be nice to integrate this with ALPACA.</li>
<li>General UI simplification (ex. remove unnecessary toolbar items). I was thinking slicelet could be appropriate for this?</li>
<li>Bonus: provide a score (%) based on total difference. The less, the better.</li>
</ol>
<p>Any feedbacks &amp; interest would be appreciated.<br>
If this project is successful, it is sure to make a difference in the dental field.</p>
<p>Sean</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/agporto">@agporto</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcec81e00efa7919419a7975b075a0af39c94cd7.jpeg" data-download-href="/uploads/short-url/qXitHtonv6L0bZBS5JgJMpC6lRt.jpeg?dl=1" title="Screen Shot 2021-04-30 at 1.13.22 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcec81e00efa7919419a7975b075a0af39c94cd7_2_690x377.jpeg" alt="Screen Shot 2021-04-30 at 1.13.22 AM" data-base62-sha1="qXitHtonv6L0bZBS5JgJMpC6lRt" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcec81e00efa7919419a7975b075a0af39c94cd7_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcec81e00efa7919419a7975b075a0af39c94cd7_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcec81e00efa7919419a7975b075a0af39c94cd7_2_1380x754.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-30 at 1.13.22 AM</span><span class="informations">2458×1344 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #39 by @lassoan (2021-04-30 03:53 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="38" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>If this project is successful, it is sure to make a difference in the dental field.</p>
</blockquote>
</aside>
<p>Can you tell a bit more about this application? How the colored overlay display helps the dentist?<br>
Do you see potential further improvements, additional features that could be useful?</p>
<p>The amount of funding that you mentioned to develop this might be sufficient for a software developer/engineering student looking for a summer project. If you cannot find a suitable student then you could contact one of the <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners">Slicer commercial partners</a> but probably they would ask for about one magnitude more funding to get started on a new project. There seem to be many dental applications of Slicer, so it could also make sense to coordinate with others in the community who are in this field and see if you can find some good common topics to work on and join forces to find funding and developers together.</p>

---

## Post #42 by @seanchoi0519 (2021-06-20 13:45 UTC)

<p>Upon research it looks like it may be beneficial to create a custom slicelet with the drag-and-drop function + ALPACA function. Could someone please confirm?</p>

---

## Post #43 by @seanchoi0519 (2022-04-04 23:21 UTC)

<p>Hello Prof Andras</p>
<p>I hope you’ve been well. I would love to hear your opinion &amp; advice on the direction of our project.</p>
<p>My research team is working on a project where we compare 2 3D scans and essentially compare the % match between the scans. This would be useful for forensic odontology application in identifying victims following a mass disaster event.</p>
<p>The comparison would be between a 3D CBCT scan of the dentition prior to death (from existing dental clinic patient record file) and a 3D CBCT scan of the deceased person.</p>
<p>We are thinking of using the ALPACA’s align functions for this. I would like to ask 2 questions</p>
<ol>
<li>
<p>Is this a feasible idea? I understand that ALPACA’s align functions are near flawless for very similar 3D files, however in this case, some time would’ve passed between the pre-death scan and the post-death scan, meaning some teeth could have drifted, worn away, or had fillings work done, etc. also, keeping in mind only a portion of the dentition may be available for post-death 3D scan (considering there may have been a massive trauma)</p>
</li>
<li>
<p>Our research team has a rather flexible budget, probably ranging anywhere from $5k - $25k. Would the commercial partners be available to hop on board with a budget like this?</p>
</li>
</ol>
<p>Thanks so much for your help</p>

---

## Post #44 by @lassoan (2022-04-15 15:54 UTC)

<p>If meshes are very different then you may need to simplify the problem with manual preprocessing (cut off parts of the mesh that are changed; for example using Dynamic Modeler module’s <a href="https://discourse.slicer.org/t/new-dynamic-modeler-tool-select-by-points/22165">Select by points</a> tool) and manual prealignment (using <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">landmark registration</a>).</p>

---

## Post #45 by @seanchoi0519 (2022-04-20 13:16 UTC)

<p>Thank you Prof Lasso for your insight.</p>
<p>We thought that ALPACA would be a great tool for our project since the whole process seems quick and seamless without the need for manual preprocessing &amp; pre-alignment. Would this still be a mandatory step in our case considering there could be minor/major differences between our samples? Would there be a way to automate this process?</p>
<p>As if a pair is a match, in theory the meshes should be nearly identical.<br>
Your insight is appreciated</p>

---

## Post #46 by @lassoan (2022-04-25 04:26 UTC)

<p>If ALPACA gives good results without any preparation, cleanup, preprocessing of the data then it’s great. If the method struggles to give accurate results reliably, then you can simplify the problem as I described above.</p>
<aside class="quote no-group" data-username="seanchoi0519" data-post="43" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Our research team has a rather flexible budget, probably ranging anywhere from $5k - $25k. Would the commercial partners be available to hop on board with a budget like this?</p>
</blockquote>
</aside>
<p>I think this amount should be sufficient to get help with developing a custom application. I would encourage you to contact Slicer commercial partners.</p>

---

## Post #47 by @youssef_sawas (2024-06-26 11:03 UTC)

<p>i tried install the software but the standard software i can’t find any of the tools which are attached in the comments any help ,<br>
i need to Alline Two ear’s stl files and and export it to one stl file with color map measurement<br>
thanks in advance</p>

---

## Post #48 by @muratmaga (2024-06-26 14:56 UTC)

<aside class="quote no-group" data-username="youssef_sawas" data-post="47" data-topic="8259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/youssef_sawas/48/69460_2.png" class="avatar"> youssef_sawas:</div>
<blockquote>
<p>i need to Alline Two ear’s stl files and and export it to one stl file with color map measurement</p>
</blockquote>
</aside>
<p>3D model registration can be done now with the <code>FastModelAlign</code> module in SlicerMorph (which is based on ALPACA). See the tutorial here:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign" target="_blank" rel="noopener">Tutorials/FastModelAlign at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
