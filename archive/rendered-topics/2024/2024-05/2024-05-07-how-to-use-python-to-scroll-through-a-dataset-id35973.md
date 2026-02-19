---
topic_id: 35973
title: "How To Use Python To Scroll Through A Dataset"
date: 2024-05-07
url: https://discourse.slicer.org/t/35973
---

# How to use python to scroll through a dataset

**Topic ID**: 35973
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/how-to-use-python-to-scroll-through-a-dataset/35973

---

## Post #1 by @Tobias (2024-05-07 21:55 UTC)

<p>Hi<br>
I use slicer alot in education but am very new to programing. I would like to make a python script that scrolls through a dataset from the first to the last image in z.<br>
So ideally it should be able to get the min and max for the active slice and the scroll through it one by one.</p>
<p>Can anyone give me some advice as how i should get started. For instance what is the easiest way to find the commands needed?</p>
<p>Any help in  the right directions is very appreciated.</p>

---

## Post #2 by @jamesobutler (2024-05-07 23:08 UTC)

<p>If it is auto-scrolling that you desire, I would suggest to first look into the “AutoScroll” extension available to install through the Slicer Extensions Manager.</p>
<p>The associated code for AutoScroll can be reviewed at the following:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerAutoscroll">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerAutoscroll" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/e6b2a5fcbe67e596d6b52ffddac74e7f884d032b11040b498e71132b90738cf3/lassoan/SlicerAutoscroll" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerAutoscroll" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerAutoscroll</a></h3>

  <p>Contribute to lassoan/SlicerAutoscroll development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Tobias (2024-05-08 07:07 UTC)

<p>Thank you this is a very useful start<br>
Basically what i would like to do is scroll through the image as fast as possible and check the time. So use it as a kind of benchmark tool. I think some small modifications on this one should make that work very well.</p>

---
