---
topic_id: 29229
title: "Na Mic Project Week Project Week 39 Preparation Meetings Sta"
date: 2023-05-01
url: https://discourse.slicer.org/t/29229
---

# [Na-mic-project-week] Project Week 39 preparation meetings start this Tuesday (May 2nd)

**Topic ID**: 29229
**Date**: 2023-05-01
**URL**: https://discourse.slicer.org/t/na-mic-project-week-project-week-39-preparation-meetings-start-this-tuesday-may-2nd/29229

---

## Post #1 by @Sam_Horvath (2023-05-01 14:16 UTC)

<p>Dear Project Week community,</p>
<p>We are happy to announce the beginning of preparation meetings for the next project week (June 12-16, 2023). Weekly meetings will start this Tuesday, May 2nd, 2023 (10 am Boston time, EDT) on Zoom. You can join using the following link which will remain the same for all preparation meetings:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09">
  <header class="source">
      <img src="https://etsmtl.zoom.us/zoom.ico" class="site-icon" width="32" height="32">

      <a href="https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09" target="_blank" rel="noopener">Zoom Video</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09" target="_blank" rel="noopener">Join our Cloud HD Video Meeting</a></h3>

  <p>Zoom is the leader in modern enterprise video communications, with an easy, reliable cloud platform for video and audio conferencing, chat, and webinars across mobile, desktop, and room systems. Zoom Rooms is the original software-based conference...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Looking forward to see you all!</p>
<p>Cheers.</p>
<p>The PW organizing committee</p>
<p>(Tina Kapur, Simon Drouin, Rafael Palomar, Sam Horvath, Theodore Aptekarev)</p>
<hr>
<p>Project Week#39 will be held June 12-16, 2023, at École de Technologie Supérieur (ETS) in Montreal, Canada. The meeting will have a hybrid format to make it possible to participate remotely. Please look here for additional details: <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/" class="inline-onebox">NA-MIC Project Weeks | Website for NA-MIC Project Weeks</a></p>
<p><em>Preparation</em> : To prepare, we will be holding weekly meetings at 10am on Tuesdays, starting <strong>May</strong> <strong>2nd, 2023</strong> and ending on June 6th. Please join at <a href="https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09">this link</a> if you have a project that you would like to present or work on during project week.</p>
<p><em>Background</em> : The Project Week is a week-long hackathon of hands on activity in which medical image computing researchers create solutions using the open source image computing platform, 3D Slicer, and VTK, ITK, CMake, and CDash libraries as well as OHIF, Cornerstone, dcmjs, vtkjs, itkjs, DICOMweb, Girder and related web technologies. Participants work collaboratively on solutions that lie at the interfaces of the fields of computer science, mechanical engineering, biomedical engineering, and medicine. In contrast to conferences and workshops where the primary focus is to report results, the objective of the ProjectWeek is to provide a venue for creators of medical image computing open-source software creators to collaboratively work.</p>
<hr>
<p>Na-mic-project-week mailing list<br>
<a href="mailto:Na-mic-project-week@public.kitware.com">Na-mic-project-week@public.kitware.com</a><br>
<a href="https://public.kitware.com/cgi-bin/mailman/listinfo/na-mic-project-week" class="onebox" target="_blank" rel="noopener">https://public.kitware.com/cgi-bin/mailman/listinfo/na-mic-project-week</a></p>

---

## Post #2 by @muratmaga (2023-05-02 16:20 UTC)

<p>I am not planning to attend the PW in person, but I am wondering whether it makes sense to form a planning project about revamping Volume Rendering module and what it would it take from funding and resources point of view.</p>
<p>To me it seems it is one of the oldest modules of Slicer serious in need of redesign from usability and integration with the other modules (specifically segment editor, lighting, cameras, screenshots, movies, AR/VR) point of view. It also seems it is a big undertake.</p>
<p>We discussed this in a few threads in forum, but I thought maybe a dedicated session with more structure might be useful for moving this forward. We can then see if it makes sense to implement it in a usual manner, where parts of it gets written into relevant grants, or is it more meaningful to seek funding dedicated to this.</p>

---

## Post #3 by @pieper (2023-05-02 19:11 UTC)

<p>I’d also be interested in discussing volume rendering improvements, either in person or virtually.  I do plan to be in Montreal in person.</p>

---

## Post #4 by @drouin-simon (2023-05-03 09:46 UTC)

<p>I’m also very interested in this topic. We should have a project about it. For me, it is not clear where the effort should go first. The VTK framework for volume rendering is even more outdated than the Slicer module using it and redesigning the module without addressing VTK issues might not yield a lot of improvement. With <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>, we discussed the idea of creating an “experimental rendering” module where we could more freely play with different architecture, overwrite vtk classes functionality and figure out what new design may work well for the main volume rendering module.</p>

---

## Post #5 by @pieper (2023-05-03 12:39 UTC)

<p><a class="mention" href="/u/drouin-simon">@drouin-simon</a> <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> I really like the idea of experimentally integrating some different rendering options to see what we really like.  I’ve got some prototypes myself to support <a href="https://youtu.be/8dputUoKBTA?t=95">nonlinear transforms and compositing</a>, but also I’ve always liked what <a href="https://www.nitrc.org/project/list_screenshots.php?group_id=889&amp;screenshot_id=1284">MicroGL</a> can do in terms of image quality.  The move to WebGPU could help us share code more easily across.</p>

---

## Post #6 by @muratmaga (2023-05-06 01:06 UTC)

<p>So, do we have a consensus to discuss this in the next PW call?</p>

---

## Post #7 by @pieper (2023-05-06 14:44 UTC)

<p>I’ll miss the next call, but would be happy to discuss volume rendering the following week.</p>

---

## Post #8 by @drouin-simon (2023-05-08 15:47 UTC)

<p>This week’s call will be dedicated mostly to segmentation, but the following could focus on rendering. We can gather the list of people interested and follow up with a more focused meeting with just those interested.</p>

---
