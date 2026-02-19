---
topic_id: 1243
title: "Slicer Extension Spacing Out Points Along Curve From Curve M"
date: 2017-10-18
url: https://discourse.slicer.org/t/1243
---

# Slicer Extension: Spacing out points along curve from Curve Maker

**Topic ID**: 1243
**Date**: 2017-10-18
**URL**: https://discourse.slicer.org/t/slicer-extension-spacing-out-points-along-curve-from-curve-maker/1243

---

## Post #1 by @Gordon (2017-10-18 18:16 UTC)

<p>My collaborator is using Curve Maker to fit a curve to feature in an MRI image. They would like to be able to space a certain number of points along that curve. Is there already a way to do this? If not, how difficult would this be to do? I use python, but I am a researcher not a trained programmer.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2017-10-18 18:58 UTC)

<p>You might find the code below helpful  - this is set up to calculate equally spaced steps along a piecewise spline.  It would be possible to do this once and add up the path length of the curve and then divide it out by the desired number of steps to get a set of equally spaced points.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/944c364a6dd95f1e57dca9ee6b5e1878951de184/Modules/Scripted/Endoscopy/Endoscopy.py#L389-L445" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/944c364a6dd95f1e57dca9ee6b5e1878951de184/Modules/Scripted/Endoscopy/Endoscopy.py#L389-L445" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/944c364a6dd95f1e57dca9ee6b5e1878951de184/Modules/Scripted/Endoscopy/Endoscopy.py#L389-L445</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="389" style="counter-reset: li-counter 388 ;">
<li>def calculatePath(self):</li>
<li>  """ Generate a flight path for of steps of length dl """</li>
<li>  #</li>
<li>  # calculate the actual path</li>
<li>  # - take steps of self.dl in world space</li>
<li>  # -- if dl steps into next segment, take a step of size "remainder" in the new segment</li>
<li>  # - put resulting points into self.path</li>
<li>  #</li>
<li>  n = self.n</li>
<li>  segment = 0 # which first point of current segment</li>
<li>  t = 0 # parametric current parametric increment</li>
<li>  remainder = 0 # how much of dl isn't included in current step</li>
<li>  while segment &lt; n-1:</li>
<li>    t, p, remainder = self.step(segment, t, self.dl)</li>
<li>    if remainder != 0 or t == 1.:</li>
<li>      segment += 1</li>
<li>      t = 0</li>
<li>      if segment &lt; n-1:</li>
<li>        t, p, remainder = self.step(segment, t, remainder)</li>
<li>    self.path.append(p)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/944c364a6dd95f1e57dca9ee6b5e1878951de184/Modules/Scripted/Endoscopy/Endoscopy.py#L389-L445" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @tavaughan (2017-10-20 14:35 UTC)

<p>I’m working on an extension called Slicer Markups to Model, which has similar functionality to Curve Maker. I’m curious to hear more about what you (and your collaborator) are trying to do. Just to clarify: are you trying to resample the curve (output a new set of markup fiducials)? Or maybe you’re trying to get a smoother curve for visualization?</p>

---

## Post #4 by @HarishRRao (2017-10-25 21:47 UTC)

<p>Hey Thomas!</p>
<p>Greetings!</p>
<p>I am Harish, a Master’s student at the University of Waterloo. Firstly, I want to thank you for your extension ‘MarkupsToModel’. I am really excited to discover the capabilities of the extension, which I will be doing soon.</p>
<p>I had a few questions for you though, if you don’t mind. Before I ask them, here is a brief of what I am going to use the extension for: For my research I am trying to morph an existing mesh of a knee model to generate patient-specific models having CT/MRI as inputs. In 3D Slicer I was trying to generate points along the boundaries of distinct regions (such as bone, cartilage, ligament etc.) and I want to then export the co ordinates of these points to Hypermesh and try to morph my existing knee model to the new co-ordinates so I can obtain a new patient-specific model.</p>
<p>I wanted to know if there exists a tutorial with examples as to how MarkupsToModel could be used? And also will I be able to export the generated points as co-ordinates into a file or something?</p>
<p>Thanks again!<br>
Regards,<br>
Harish R Rao</p>

---

## Post #5 by @tavaughan (2017-10-30 19:25 UTC)

<p>Hi Harish! It sounds to me like you want to resample points along the curve, then. I can’t think of any script-free ways to do this at the moment.</p>
<p>In the next 2-3 weeks I plan to add a way to resample points along the curve and export those point coordinates to Markups. Hypothetically you could then save those Markups as .fcsv (which should be comma-delimited text containing the coordinates).</p>
<p>In the meantime, there is some documentation for the existing features in the module here (scroll below the file browser): <a href="https://github.com/tavaughan/SlicerMarkupsToModel" rel="nofollow noopener">https://github.com/tavaughan/SlicerMarkupsToModel</a></p>
<p>Feel free to let me know if you have any trouble with the documentation!</p>

---

## Post #6 by @HarishRRao (2017-11-01 17:19 UTC)

<p>Hey Thomas,</p>
<p>Thanks a lot for your reply!</p>
<p>I will definitely try to explore the features of Markups. I will also get in touch with you if I face an obstacles on the way.</p>

---
