# Baffle planner input - proposal - frustration

**Topic ID**: 42859
**Date**: 2025-05-10
**URL**: https://discourse.slicer.org/t/baffle-planner-input-proposal-frustration/42859

---

## Post #1 by @Esteban_Barreiro (2025-05-10 05:00 UTC)

<p>Hi there lovely scientific nerdi comunity! Love you all!<br>
Im a teacher, and one of the modules I use to teach for medical institutions such hospitals, clinics and i+d+i+i …<br>
Im writing this post cause I think that, in software development, we must <em><strong>respect the hierarchy “gestural-input-peripherals” over any other “actiones-functions”</strong></em>… I mean, <strong>if you pan-rotate-zoom whith any mouse, button, shortcut… it must not be envolved in any other action</strong>, even if you can “block” some actions just no to modify your work.<br>
I mean: if you do “something” naturally with your mouse just to orbit around… <strong>that input</strong> should NOT be involved in any other actions.<br>
When you design using the Baffle Planner module, if you press the middle mouse button, over your desing, the entire design () is transformed, <em>“spatialy moved”</em>… and using the middle mouse button <strong>must</strong> only be used to orbit around your 3d scene.<br>
I mean, we should <strong>not “overwrite” actiones that get us the wrong output and make the users confuse on how to use the tools.</strong><br>
I hope it make sense.<br>
Love you all,keep up the suuuuuper good work, Im a fan, and if you want to come to Argentina, Ill make you “Asado” hahaha (not kiding, you are welcome, will be an honour)</p>

---

## Post #2 by @lassoan (2025-05-10 12:48 UTC)

<p>I guess you accidentally moved markup points by middle-button-click-and-drag. In the long term, we’ll change markup interactions so that you need to first click to select and then you can drag the selected markup. What you can do now is to enable undo/redo so that you can undo any unintended changes. You can also remap interaction events on a markup by a few lines of python script to disable moving by middle-button-click-and-drag.</p>

---

## Post #3 by @Esteban_Barreiro (2025-05-15 11:47 UTC)

<p>Great, thanks a lot Andras.<br>
Sorry to bother, but I cant find where exactly can I enable undo/redo.<br>
I know I can lock the contour points, and that is really helpful.<br>
Thanks again.</p>

---

## Post #4 by @lassoan (2025-05-18 12:36 UTC)

<p>See how to enable undo here:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/" target="_blank" rel="noopener">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> what do you think about enabling undo/redo by default in Slicer for markups?</p>

---

## Post #5 by @pieper (2025-05-18 12:38 UTC)

<p>Yes, I’ve always wanted undo/redo as a first class feature.  I think if we have solid testing we can catch and fix any of the event issues that have always plagued this feature in the past.</p>

---

## Post #6 by @Esteban_Barreiro (2025-05-18 12:51 UTC)

<p>Thanks a lot Andras!</p>

---

## Post #7 by @Esteban_Barreiro (2025-05-18 12:57 UTC)

<p>I wish I could help, but I think I can’t, cause every month a new batch of students come to my classes to learn segmentation, and, sadly, I can’t use a custom 3dSlicer, cause I explain the basics starting from “absolute zero”, like configuration (like basic design things as orthographic projection vs perspective) and how to download and install extensions…or how to avoid colors and terminology so they can name their segments the way they need (cause we cut and duplicate and things like that)…<br>
But… I don’t know… what can I do to help?</p>

---

## Post #8 by @lassoan (2025-05-18 18:02 UTC)

<aside class="quote no-group" data-username="Esteban_Barreiro" data-post="7" data-topic="42859">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/esteban_barreiro/48/5430_2.png" class="avatar"> Esteban_Barreiro:</div>
<blockquote>
<p>I don’t know… what can I do to help?</p>
</blockquote>
</aside>
<p>Providing feedback and describing your perspective of using Slicer helps a lot.</p>
<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="42859">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>issues that have always plagued this feature in the past</p>
</blockquote>
</aside>
<p>With robust and efficient node copy (deep and shallow) used and thoroughly tested in sequences and scene views (thanks to <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, we can have robust undo/redo. It will surely need some fixes and we will need to introduce it step-by-step (starting with a markups and maybe transforms).</p>
<p>Node serialization to json and fast background saving of bulk data (WIP by <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>) is also a promising avenue to implement continuous scene saving and therefore undo/redo.</p>

---

## Post #9 by @muratmaga (2025-05-18 18:51 UTC)

<aside class="quote no-group" data-username="Esteban_Barreiro" data-post="7" data-topic="42859">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/esteban_barreiro/48/5430_2.png" class="avatar"> Esteban_Barreiro:</div>
<blockquote>
<p>or how to avoid colors and terminology so they can name their segments the way they need (cause we cut and duplicate and things like that)…</p>
</blockquote>
</aside>
<p>with the recent changes, this should not be problem at all. Please review the tutorial here. <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation/colors-and-terms#segment-colors-and-terminology" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/Segmentation/colors-and-terms at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>It is designed exactly to overcome the issues  you describe, particularly with students. You need to use it with a Slicer preview dated after late March…</p>

---

## Post #10 by @Esteban_Barreiro (2025-05-19 01:48 UTC)

<p>Cool! Ill read it.<br>
Thanks!</p>

---

## Post #11 by @Esteban_Barreiro (2025-05-19 02:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="42859">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>fast background saving of bulk data (WIP by <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>) is also a promising avenue to implement continuous scene saving and therefore undo/redo</p>
</blockquote>
</aside>
<p>That could be extremely awesome!</p>
<p>Ill try to help if I can.</p>
<p>Right now, I’m trying to collect errors from DentalSegmentator and TotalSegmentator, cause 2/10 of my students have different issues, I hope someday I’ll be ready to send you “a list” of errors and “solutions”.<br>
i.e. a few weeks ago, one of my students had a special character in her Windows username, and TotalSegmentator couldn’t finish the segmentation properly… weird right? Things like that, and a few combinations of GPU Drivers + CUDA versions + PyTorch versions… (I know I shouldn’t write it here, right now, because I can fail, but I’ll try)…</p>

---

## Post #12 by @Esteban_Barreiro (2025-05-19 04:05 UTC)

<p>I think you sent it to me, can’t remember exactly when… or why…but it doesn’t have much to do with my work, and the work of my students.<br>
Anyway, it is precious information, because someday it will be necessary to work within an institution and its PAKs… Thanks for sharing, hope someday, someone around me, need it.<br>
What I do is just simply cut and duplicate parts of various segments, to make them 3d printable, looking for simulators and practice models for surgeons, biomedical engineers, teachers and researchers, while I teach the basics on how to use 3dSlicer, so then they can, for example, watch the Kitware YouTube channel and understand how to do things with their video tutorials (super fast, for people that already know how to use 3dSlicer)…<br>
I’ve learned a lot from Sonia Pujol’s publications, like ten years ago, but know we work, “almost all the time” whit voxels instead of polygons, and things have changed through time.<br>
My main goal, as a teacher, is to lend a hand to use the Segment Editor (nowadays) the way you need it to be, just to create 3d models from medical imaging and use them for any purpose, like pieces of human parts to create customized implants or physical 3d printed practice models that day by day become increasingly useful here in Latin America.<br>
My students are pretty interesting people, the best of the best, always looking for methods they can use to make the patients happy, resilient, and mitigate their fear or stress. I’m so lucky to teach them the use of this tools, and luckier talking to you directly, you always provide material and resources to make our lives vivid and joyful.<br>
I’m happy to help in anything you need.<br>
Thanks for your time, I mean it.</p>

---
