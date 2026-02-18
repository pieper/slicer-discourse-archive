# Bundle file creation

**Topic ID**: 573
**Date**: 2017-06-26
**URL**: https://discourse.slicer.org/t/bundle-file-creation/573

---

## Post #1 by @Felix_Navarro_Guirad (2017-06-26 16:53 UTC)

<p>Dear Slicer users,</p>
<p>I use Slicer CLI modules as pilar of a pipeline executed in a Ubuntu server from a web page located in an Apache Tomcat hosted by that server.</p>
<p>I would like to create a mrb file containing the scene to be used but when I invoke Slicer for this purpose I’m having a "SlicerApp-real: cannot connect to X server " message.</p>
<p>Is it possible to do this task without opening the GUI?</p>
<p>Thanks in advance.</p>
<p>PS: This is the sentence that I use:<br>
Slicer --no-splash --python-script <a href="http://composeScene.py" rel="nofollow noopener">composeScene.py</a>  -i file1.nii … -i fileN.nii  -o output.mrb &gt;&gt; scriptPython.log. The script just loads all the input files and  set a few details about the window location which are not essential.</p>

---

## Post #2 by @lassoan (2017-06-26 17:07 UTC)

<p>Try with adding --no-main-window parameter. You can also configure a dummy x server.</p>

---

## Post #3 by @Felix_Navarro_Guirad (2017-06-26 17:14 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your fast reply.</p>
<p>–no-main-window returns the same message. I’ll try to learn how to set up that dummy x server.</p>
<p>Thank you again, I’ll keep you informed about the result.</p>

---

## Post #4 by @ihnorton (2017-06-26 17:31 UTC)

<p>See</p>
<aside class="quote quote-modified" data-post="1" data-topic="138">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/65b543/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/saving-images-from-slicer-views-in-headless-compute-node/138">Saving images from slicer views in headless compute node</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi Slicer community, 
I am trying to perform what I thought would be a straightforward task of loading a study into slicer and saving a few images from each of the viewing panes (red, yellow, green) into PNG or jpg files. My script is based off example code here: 
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_a_series_of_images_from_a_Slice_View" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_a_series_of_images_from_a_Slice_View</a> 
The script works when I call it from the Python Interactor window of an already launched Slicer application (in windows) usin…
  </blockquote>
</aside>


---

## Post #5 by @pieper (2017-06-26 17:35 UTC)

<p>This is a good place to start:</p>
<p><a href="https://xpra.org/trac/wiki/Xdummy" class="onebox" target="_blank">https://xpra.org/trac/wiki/Xdummy</a></p>
<p>Here’s a docker container that sets it up the server as an example:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/pieper/SlicerDockers/tree/master/x11" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/126077?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/pieper/SlicerDockers/tree/master/x11" target="_blank">pieper/SlicerDockers</a></h3>

<p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Felix_Navarro_Guirad (2017-06-27 16:47 UTC)

<p>Thank you <a class="mention" href="/u/ihnorton">@ihnorton</a> and <a class="mention" href="/u/pieper">@pieper</a> for your kind replies.</p>
<p>I solved the problem installing xvfb package. I just need to run Slicer this way:<br>
xvfb-run -s “-screen 0 1024x768x24” Slicer …</p>
<p>xvfb-run sets the dummy X server, redirects the graphical output to it and closes it when slicer is close.</p>
<p>Thanks for your support.</p>

---

## Post #7 by @Mohammed_Abdelaziz (2020-04-10 13:30 UTC)

<p>Hi Felix</p>
<p>i have the same pb with google clooud<br>
did you just intall xvfb<br>
whats the whole command used to run slicer<br>
xvfb-run -s “-screen 0 1024x768x24” Slicer</p>

---
