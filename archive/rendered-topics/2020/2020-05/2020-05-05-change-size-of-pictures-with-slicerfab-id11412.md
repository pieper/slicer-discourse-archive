---
topic_id: 11412
title: "Change Size Of Pictures With Slicerfab"
date: 2020-05-05
url: https://discourse.slicer.org/t/11412
---

# Change size of pictures with SlicerFab

**Topic ID**: 11412
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/change-size-of-pictures-with-slicerfab/11412

---

## Post #1 by @Mathias (2020-05-05 08:38 UTC)

<p>Hello,</p>
<p>I’m working on a project, I need to add my .stl file and convert this file into an image set with the extension SlicerFab.<br>
But when I “generate bitmaps”, the pictures I obtain are too zoomed, how can I change the pictures size to get a full picture of a slice ?</p>
<p>Thank you for your help,</p>
<p>Mathias.</p>

---

## Post #2 by @pieper (2020-05-05 12:48 UTC)

<p>Hi -</p>
<p>The DPI settings and output scale exposed in the UI should let you control the zoom level.</p>
<p>Currently the size of the bitmap is hard coded to 1k x 1k.  If needed you could edit the code to try different values.  Those parameters could be exposed in the UI with a little coding.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L184-L186" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L184-L186" target="_blank">SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L184-L186</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="184" style="counter-reset: li-counter 183 ;">
<li># Size of each generated layer image in pixels</li>
<li>self.width = 1024</li>
<li>self.height = 1024</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Mathias (2020-05-05 13:00 UTC)

<p>Thanks for helping me, sorry but I’m not used to 3DSlicer, how do I edit the code ?<br>
I’ve tried by pressing CTRL - 3 and just copy past what you gave me but it isn’t working.<br>
And what’s the UI ?</p>

---

## Post #4 by @pieper (2020-05-05 13:23 UTC)

<p>Yes, editing the code is a bit of an advanced topic, but in this case it should be pretty easy and will let you experiment.  First, you should turn on Developer Mode (Edit-&gt;Application Settings-&gt;Developer enable check box) and then restart Slicer.  Then when you enter the module you should have an Edit button that will bring up a text editor with that module’s code.  Find the lines I linked to and change the numbers.  Save the file and click the Reload button in the module.</p>
<p>By UI, I meant the User Interface.  The width and height values are hard coded, but widgets could be added to make them configurable like the other parameters.</p>

---

## Post #5 by @Mathias (2020-05-05 13:33 UTC)

<p>Until now, I’m in the module SlicerFab, I can see the Edit button but when I click on it, nothing happens (I followed your instructions step by step from the begining. I have the Python interactor at the bottom but I think this is not what I need.<br>
Do I need a software to open et edit the source code ?</p>

---

## Post #6 by @pieper (2020-05-05 13:50 UTC)

<p>You only need a text editor to change the python code.  It should pick your default when you click Edit, but it depends on your configuration.  If you look in the error log there’s probably some message about what file it tries to open, and if you can edit that file manually the rest of the steps should work.  Or you can just search for the file named BitmapGenerator.py in your Slicer install and edit it there.</p>

---

## Post #7 by @Mathias (2020-05-05 14:19 UTC)

<p>It works !!!<br>
I have just found the file and change the pixel number.<br>
Thank you so much for your help !</p>

---

## Post #8 by @pieper (2020-05-05 15:34 UTC)

<aside class="quote no-group" data-username="Mathias" data-post="7" data-topic="11412">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bbe5ce/48.png" class="avatar"> Mathias:</div>
<blockquote>
<p>It works !!!<br>
I have just found the file and change the pixel number.</p>
</blockquote>
</aside>
<p>Great!</p>
<p>I’m not sure why we never exposed those fields in the user interface, but in case anyone feels it’s needed, it’s a pretty boilerplate feature to add just by copying and editing the code for the other parameters.</p>

---
