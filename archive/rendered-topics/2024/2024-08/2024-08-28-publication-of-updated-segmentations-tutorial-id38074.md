# Publication of updated segmentations tutorial

**Topic ID**: 38074
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/publication-of-updated-segmentations-tutorial/38074

---

## Post #1 by @cpinter (2024-08-28 08:41 UTC)

<p>Hi all,</p>
<p>After a long time we finally finished an updated version of the Segment Editor tutorial with <a class="mention" href="/u/nagy.attila">@nagy.attila</a> (see for example <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/RefreshAFewSelectedSlicerTrainingMaterialsForAMoreRecentVersionOfSlicer/">Project Description | NA-MIC Project Weeks</a>).</p>
<p>In the ReadTheDocs documentation the tutorials seem to redirect to the old wiki (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#tutorials" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a> → <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a>)</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> Where do you think this tutorial should go? Should we replace the older segmentations tutorial in the wiki, or should we start a new section in ReadTheDocs?</p>
<p>Here’s the tutorial itself in case you want to check it out, comment, or request changes: <a href="https://uszeged-my.sharepoint.com/:p:/g/personal/nagy_attila_o365_u-szeged_hu/EbPF1n4etk5GtJ9kvt3qLaYBVwVTIpzTtkJUHw0oPRcW1Q?e=4m3Fje">3d_printing-Slicer_2023_v.3.2.1_Csaba-A.pptx</a></p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-08-28 12:26 UTC)

<p>Nice work <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>For a start, just updating the wiki with the new link is good.</p>

---

## Post #3 by @lassoan (2024-08-29 00:04 UTC)

<p>Great to see this tutorial updated! Thank you <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/nagy.attila">@nagy.attila</a>.</p>
<p>It is nice that sharepoint renders the pptx file and anonymous comments can be added. However, it is not ideal if we want the community to contribute to the tutorial, as you cannot attribute contributions (unlike in git, it is not easily trackable who contributed which change), only u-szeged people can log in to the sharepoint server, giving edit access to all guests is risky (by default anyone can make any changes), you cannot have version branches, etc. In the long term, we may also want to switch to a markdown-based tutorial engine (to facilitate internationalization, automatic update of screenshots, avoid having large binary assets under revision control, etc.).</p>
<p>So, I think it would be better to create a new github repository for this tutorial and store the tutorial and all supplementary materials in that repository.</p>
<p>i would also link this tutorial directly from the ReadTheDocs page, because the Tutorial page on the wiki is an embarrassment and the whole wiki is in a very bad state (only a handful of people have write access, no new users can be registered, search is broken, file download is broken, etc.).</p>

---

## Post #4 by @cpinter (2024-08-29 08:38 UTC)

<p>Thanks for the feedback!</p>
<p>I will make the repository (I guess I’ll call it simply SlicerTutorials) and upload this file there and link the file using its raw link directly from ReadTheDocs and submit a PR.</p>
<p>I’ll do this tonight or tomorrow unless there are objections.</p>

---

## Post #5 by @cpinter (2024-08-29 15:26 UTC)

<p>Here is the repository and the tutorial:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/EBATINCA/SlicerTutorials/tree/main">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/EBATINCA/SlicerTutorials/tree/main" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/EBATINCA/SlicerTutorials/tree/main" target="_blank" rel="noopener">GitHub - EBATINCA/SlicerTutorials: Collection of tutorials for 3D Slicer</a></h3>

  <p><a href="https://github.com/EBATINCA/SlicerTutorials/tree/main" target="_blank" rel="noopener">main</a></p>

  <p><span class="label1">Collection of tutorials for 3D Slicer. Contribute to EBATINCA/SlicerTutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Let me know if you’d change something.</p>
<p>Here is the Slicer PR: <a href="https://github.com/Slicer/Slicer/pull/7910" class="inline-onebox">DOC: Add link to new tutorials by cpinter · Pull Request #7910 · Slicer/Slicer · GitHub</a></p>

---

## Post #6 by @cpinter (2024-09-04 15:03 UTC)

<p>Some related follow-up discussion: <a href="https://discourse.slicer.org/t/2024-09-03-weekly-meeting/38169/5" class="inline-onebox">2024.09.03 Weekly Meeting - #5 by jcfr</a></p>

---
