---
topic_id: 7631
title: "Tractography Interactive Seeding In Cli Module"
date: 2019-07-17
url: https://discourse.slicer.org/t/7631
---

# Tractography interactive seeding in CLI module

**Topic ID**: 7631
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/tractography-interactive-seeding-in-cli-module/7631

---

## Post #1 by @fpsiddiqui91 (2019-07-17 15:03 UTC)

<p>Hello Developers,</p>
<p>First of all Thank you for the support. I made some progress in my current task. I have implemented UKF tractography and add some modifications on it which I needed.</p>
<p>Now I want to implement interactive seeding tractography module as CLI. I am trying to implement it like this:</p>
<pre><code>  def dti2fibers(self,markup,b):

if not hasattr(self, 'tractography_node'):
  self.tractography_node = slicer.vtkMRMLFiberBundleNode()
  slicer.mrmlScene.AddNode(self.tractography_node)

parameters = {
  'InputVolume': self.DTISelector.currentNode(),
  'OutputFibers': self.fiberBundleSelector.currentNode(),
  'InputFiducialList':self.markupSelector.currentNode() # THIS IS THE POINT OF ERROR
}

self.seeding_parameter_node = slicer.cli.run(
slicer.modules.tractographyinteractiveseeding, None,
parameters,wait_for_completion=False)
</code></pre>
<p>I am not sure about the input parameters?  how can I give my markup node as an input to the module.<br>
I saw the docuemntetion: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/TractographyInteractiveSeeding" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/TractographyInteractiveSeeding</a></p>
<p>But the inputs are not mentioned as clear as in ROI module : <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/TractographyLabelMapSeeding" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/TractographyLabelMapSeeding</a></p>
<p>Can you please let me know how can I give markup node as an input to my interactive seeding module.</p>
<p>Thank you so much</p>

---

## Post #2 by @pieper (2019-07-17 15:17 UTC)

<aside class="quote no-group" data-username="fpsiddiqui91" data-post="1" data-topic="7631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/53a042/48.png" class="avatar"> fpsiddiqui91:</div>
<blockquote>
<p>First of all Thank you for the support.</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji only-emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>To help people help you, could you include the specific error message?  Also if you can point to a github repository of the full code it’s better than just including a snippet (so people can see where variables are defined, etc).</p>

---

## Post #3 by @fpsiddiqui91 (2019-07-17 15:23 UTC)

<p>Hello Thank you fro your response. This snippet is general implementation from my source code. I am actually asking about the CLI parameters for tractographyinteractiveseeding module.</p>
<p>For ROI module it is clearly mentioned in documentation with the names:</p>
<blockquote>
<p>Input DTI Volume**  (InputVolume): DTI volume in which to seed (generate) tractography.<br>
Input Label Map**  (InputROI): Label map defining region for seeding tractography.<br>
Output Fiber Bundle**  (OutputFibers): Tractography result</p>
</blockquote>
<p>But for Interative seeding module there is no such thing mentioned in the documentation.</p>
<p>I hope I am clear with my question. Sorry for the confusion.</p>

---

## Post #4 by @ljod (2019-07-17 15:24 UTC)

<p>What is your goal? Have you looked at the interactive UKF module?</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/pnlbwh/ukftractography/tree/master/InteractiveUKF" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/3407942?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/pnlbwh/ukftractography/tree/master/InteractiveUKF" target="_blank" rel="nofollow noopener">pnlbwh/ukftractography</a></h3>

<p>Contribute to pnlbwh/ukftractography development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @fpsiddiqui91 (2019-07-17 15:51 UTC)

<p>I actually want to make a simple interactive tractography with simple mouse clicking which I have already implemented with ukf tractography.<br>
Now I want to implement the same thing with interactive seeding module as ukf is computationally expensive.</p>
<p>I want to learn how to use interactive seeding module in CLI. I have tried to make a function but I dont know the CLI parameters it needs.</p>

---

## Post #6 by @ljod (2019-07-17 16:06 UTC)

<p>But does the Interactive UKF module already work for your needs?</p>
<p>Also, all CLIs should be able to print their help information when run on the command line with -h. This should help understand inputs.</p>

---

## Post #7 by @fpsiddiqui91 (2019-07-17 16:11 UTC)

<p>It worked but it might be computationally expensive,</p>
<p>Also, I want to run tractography module on background. I could not figure out a way to run the whole UKF tracktography on background,</p>
<p>Typically on any CLI module we can this flag: set wait_for_completion=False</p>
<p>Thank you for your response.</p>

---

## Post #8 by @pieper (2019-07-17 16:39 UTC)

<p>Did you try the autorun options for the CLI?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2b96a837ff90431e75f383b69966d34b495716e.png" data-download-href="/uploads/short-url/wlH9WDVxpjjeR6nVJdbonmvi8Vw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2b96a837ff90431e75f383b69966d34b495716e_2_690x241.png" alt="image" data-base62-sha1="wlH9WDVxpjjeR6nVJdbonmvi8Vw" width="690" height="241" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2b96a837ff90431e75f383b69966d34b495716e_2_690x241.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2b96a837ff90431e75f383b69966d34b495716e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2b96a837ff90431e75f383b69966d34b495716e.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1030×360 46.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @fpsiddiqui91 (2019-07-17 16:45 UTC)

<p>Thank you for your response, I have implemented UKF on my own application. I will try to activate it pragmatically. Thank you</p>

---
