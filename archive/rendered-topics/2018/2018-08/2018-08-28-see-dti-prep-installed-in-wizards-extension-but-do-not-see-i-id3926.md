# See DTI Prep Installed in Wizards Extension but do not see it as an option on 

**Topic ID**: 3926
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/see-dti-prep-installed-in-wizards-extension-but-do-not-see-it-as-an-option-on/3926

---

## Post #1 by @belleauel (2018-08-28 16:01 UTC)

<p>Hello Slicer Experts,</p>
<p>I am using Slicer 4.4.0 on a Mac. I see that I have installed DTIPrep and it appears on my extension wizard but does not show up as a module I can choose from. I would have expected it to show up under “diffusion” module, but it is not there.</p>
<p>Any suggestions?</p>
<p>Thanks!</p>
<p>Emily</p>

---

## Post #2 by @ihnorton (2018-08-28 18:26 UTC)

<p>I added DTIPrep (happened to have Slicer 4.4 installed already) and can see it in the module list under Diffusion. My system is running macOS 10.13. However, there are errors in the log related to library loading for the tools DTIPrep uses, so I doubt it will actually run.</p>
<p>I think DTIPrep is really only supported as a stand-alone tool at the moment.</p>

---

## Post #3 by @belleauel (2018-08-28 18:38 UTC)

<p>Hi Isaiah,</p>
<p>Thanks for responding and checking into this on your own computer!</p>
<p>I actually used it about a year ago on this same mac computer without a problem. I am only using DTI prep to help identify outlier images, so I am shutting off everything else in my protocol (like eddy current correct, etc.). I do those other things using different programs.</p>
<p>Actually, do you by chance happen to have an xml protocol file I could use (the file that contains all the steps you want DTIPrep to run)? What I might try to do is take the xml protocol file and try running DTIPrep through the command line. I had made a batch script to have DTIPrep loop through a bunch of subjects. If you happen to have a protocol file and would be willing to share, you could send to <a href="mailto:belleauel@gmail.com">belleauel@gmail.com</a>.</p>
<p>Thanks so much!</p>
<p>Emily</p>

---

## Post #4 by @ihnorton (2018-08-28 18:58 UTC)

<aside class="quote no-group" data-username="belleauel" data-post="3" data-topic="3926">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/96bed5/48.png" class="avatar"> belleauel:</div>
<blockquote>
<p>I actually used it about a year ago on this same mac computer without a problem.</p>
</blockquote>
</aside>
<p>In that case, you could try cleaning the settings reinstalling extensions specific to Slicer 4.4. Delete (or rename/back-up) the following file and directory:</p>
<ul>
<li><code>~/.config/www.na-mic.org/Slicer-23774.ini</code></li>
<li><code>~/.config/www.na-mic.org/Extensions-23774</code></li>
</ul>
<p>Note: <code>~</code> means “home directory”, usually <code>/Users/USERNAME</code> on mac.</p>
<p>However, If you updated the macOS version since the last time you ran Slicer/DTIPrep, then that might have changed something in the system that DTIPrep requires.</p>
<aside class="quote no-group" data-username="belleauel" data-post="3" data-topic="3926">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/96bed5/48.png" class="avatar"> belleauel:</div>
<blockquote>
<p>Actually, do you by chance happen to have an xml protocol file I could use (the file that contains all the steps you want DTIPrep to run)?</p>
</blockquote>
</aside>
<p>Unfortunately not. You might be able to get sample file(s) if you ask on the DTIPrep forum.</p>

---
