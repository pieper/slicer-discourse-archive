---
topic_id: 2499
title: "Start Programming In Slicer Transforms Module Elastix"
date: 2018-04-03
url: https://discourse.slicer.org/t/2499
---

# Start programming in Slicer: Transforms module, Elastix

**Topic ID**: 2499
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/start-programming-in-slicer-transforms-module-elastix/2499

---

## Post #1 by @hadasara (2018-04-03 09:57 UTC)

<p>Hi, I’m new in slicer so I have beginners questions:</p>
<p>I’d like to use slicer modules through python programming, which I see in many places that is possible, just not sure how to get started. I don’t want to work through the consol, but rather write scripts etc.</p>
<ol>
<li>How do I do that- where do I write the scripts?</li>
<li>After I’ll figure out 1 - Is the only option is to create an extantion, and that way to operate it?</li>
<li>Can I access into a module script (how?) set a breakpoint and see how it works (as I can do in MATALB functions), like in Transformation module?</li>
</ol>
<p>Question regarding elastix and transformation module:<br>
when I apply elastix transformation on an image using transformation module, I assuem it do resampling+ interpolation.</p>
<ol>
<li>How\Can I control the type of interpolation?</li>
<li>Is the elastix transformation include both rigid+non-linear registration in a vector field? How can I visualize the transformation without applying it on an image?</li>
</ol>
<p>Thanks!</p>

---

## Post #2 by @brhoom (2018-04-03 10:20 UTC)

<p>Welcome to Slicer.</p>
<p>There are 4 simple <a href="https://www.youtube.com/watch?v=sl-00kGpuPk&amp;list=PLJWCUXz3GeAfmYLiFcKus_c0jcsMnVsgb" rel="nofollow noopener">video tutorials</a> that explains the basics Slicer python programming for beginners (note: German audio with English subtitle).</p>
<p>elastix uses parameter text file that controls the registration process. You can modify it to control any registration component you want including interpolation, you can access all these parameter files by clicking on “Advanced” then click on “Show database folder” button.</p>

---

## Post #3 by @hadasara (2018-04-03 10:56 UTC)

<p>Thank you <a class="mention" href="/u/brhoom">@brhoom</a> !<br>
I will look at the videos!<br>
Regarding elastix,<br>
1.I’m asking about the result- the transformation- How can I see it? how can I apply it with contoling the interpolation? is the same interpolation that was used during the registration is used when I apply the transformation resulted from the registration process?<br>
2. Parameters files- how can I know which one is related to which preset Inputs? (they don’t have the same names)</p>

---

## Post #4 by @brhoom (2018-04-03 11:35 UTC)

<p>Slicer plugin is just an interface, to learn more about it, search for Elastix.py. If you want to learn more about elastix, install it and read the <a href="https://github.com/SuperElastix/elastix/releases/download/4.9.0/elastix-4.9.0-manual.pdf" rel="nofollow noopener">elastix manual</a>, it has simple examples for different stuff,  a simple usage is:</p>
<pre><code> elastix -f fixed_image -m moving_image -p parmaeter_file.txt -out output_folder
</code></pre>
<p>To see the results file:<br>
<code>Advanced-&gt;show temp folder.</code><br>
The transformation is saved in TransformParameters.0.txt.</p>
<p>search for ElastixParameterSetDatabase.xml, it explains the parameters files connection to Slicer interface. You can control the interpolation by modifying the used parameters file before the registration, e.g. by modifying the lines (Interpolator “BSplineInterpolator”), (FixedImageBSplineInterpolationOrder 1 ), (BSplineInterpolationOrder 1) .</p>

---

## Post #5 by @pieper (2018-04-03 11:40 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="2" data-topic="2499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>There are 4 simple <a href="https://www.youtube.com/watch?v=sl-00kGpuPk&amp;list=PLJWCUXz3GeAfmYLiFcKus_c0jcsMnVsgb">video tutorials</a> that explains the basics Slicer python programming for beginners (note: German audio with English subtitle).</p>
</blockquote>
</aside>
<p>These videos look great - thanks for the link!</p>

---

## Post #6 by @lassoan (2018-04-04 04:03 UTC)

<p>The official Slicer programming tutorial is quite good, too. It is fully up-to-date for Slicer-4.8: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial</a></p>

---

## Post #7 by @lassoan (2018-04-04 04:06 UTC)

<aside class="quote no-group" data-username="hadasara" data-post="1" data-topic="2499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/c67d28/48.png" class="avatar"> hadasara:</div>
<blockquote>
<p>Can I access into a module script (how?) set a breakpoint and see how it works</p>
</blockquote>
</aside>
<p>Yes, of course. You can choose from a number of integrated development environments with visual debuggers. I mostly use PyCharm but Visual Studio and LiClipse are quite good, too. See detailed instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" class="inline-onebox">Documentation/Nightly/Extensions/DebuggingTools - Slicer Wiki</a></p>

---

## Post #8 by @lassoan (2018-04-04 04:10 UTC)

<aside class="quote no-group" data-username="hadasara" data-post="1" data-topic="2499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/c67d28/48.png" class="avatar"> hadasara:</div>
<blockquote>
<p>Is the elastix transformation include both rigid+non-linear registration in a vector field? How can I visualize the transformation without applying it on an image?</p>
</blockquote>
</aside>
<p>Yes, Elastix provides the entire transformation as a displacement field. This is somewhat inconvenient for linear and bspline transforms where it would be more efficient to be able to work with matrices and coefficients instead. We plan to have this option implemented soon.</p>
<p>You can visualize a transform using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_display_options">Transforms module’s Display section</a>.</p>

---

## Post #10 by @hadasara (2018-04-16 08:12 UTC)

<p>I scucedde using the instructions here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools</a><br>
to set a breakpoint.<br>
but when I want to stop and go back to slicer, slicer is getting “not responding” , and I have to close it and open again. Is this a normal behaviour?</p>

---

## Post #11 by @lassoan (2018-04-17 03:42 UTC)

<aside class="quote no-group" data-username="hadasara" data-post="10" data-topic="2499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/c67d28/48.png" class="avatar"> hadasara:</div>
<blockquote>
<p>when I want to stop and go back to slicer, slicer is getting “not responding” , and I have to close it and open again. Is this a normal behaviour?</p>
</blockquote>
</aside>
<p>Yes, when a breakpoint is hit, execution is stopped. No need to close and open anything, just use <em>Resume program</em> to continue.</p>

---

## Post #12 by @hadasara (2018-05-07 12:22 UTC)

<p>Hi <a class="mention" href="/u/brhoom">@brhoom</a><br>
I tried to change the ResampleInterpolator to:<br>
(ResampleInterpolator “NearestNeighborResampleInterpolator”)<br>
and removed (FinalBSplineInterpolationOrder 1)<br>
In order to change the final interpolation that is applied on the image.<br>
But I get an error:</p>
<pre><code>Traceback (most recent call last):
</code></pre>
<p>File “C:/Users/user/AppData/Roaming/NA-MIC/Extensions-26813/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Elastix.py”, line 327, in onApplyButton<br>
movingVolumeMaskNode = self.movingVolumeMaskSelector.currentNode())<br>
File “C:/Users/user/AppData/Roaming/NA-MIC/Extensions-26813/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Elastix.py”, line 575, in registerVolumes<br>
self.logProcessOutput(ep)<br>
File “C:/Users/user/AppData/Roaming/NA-MIC/Extensions-26813/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Elastix.py”, line 515, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
CalledProcessError: Command ‘elastix’ returned non-zero exit status 1</p>
<p>when I tried to keep</p>
<p>(ResampleInterpolator “BSplineInterpolator”)<br>
(FinalBSplineInterpolationOrder 0)</p>
<p>it runs, but the result seems like it didn’t do anything…</p>
<p>could you please help me understand what do I do wrong?<br>
thanks!</p>

---

## Post #13 by @brhoom (2018-05-07 12:41 UTC)

<p>Please don’t address members in your question as this will encourage other members to answer. Try to isolate the problem, is it elastix problem or slicer problem? check elastix log, run elastix using the same images and parameters and check the result.</p>

---

## Post #15 by @hadasara (2018-05-07 14:08 UTC)

<blockquote>
<p>check elastix log</p>
</blockquote>
<p>This was a wonderfull advice! I’ve realized I didn’t use the parameter files I though I’m using.</p>
<blockquote>
<p>run elastix using the same images and parameters and check the result</p>
</blockquote>
<p>What do you mean?<br>
Thank you!</p>

---

## Post #16 by @brhoom (2018-05-07 17:11 UTC)

<p>I meant using the terminal without slicer e.g.</p>
<p><code>elastix -f fixed_image -m moving_image -p parameter.txt -o output_folder</code></p>

---

## Post #17 by @hadasara (2018-05-10 09:31 UTC)

<p>I’m sorry, but I have a realy begginer question, hope it’s ok to ask.<br>
Where can I run terminal commands? the command line of windows doesn’t recognize elastix.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b006aeeba063988b6690329e1d31df5c8dcb3aca.png" alt="image" data-base62-sha1="p7clVuDRoTZYxytsKgUmHY7JmFY" width="521" height="73"></p>
<p>should I first install elastix seperatly, and then do it?</p>

---

## Post #18 by @brhoom (2018-05-10 21:30 UTC)

<p>I am not a windows user so I don’t know the path of elastix in windows, simply search for “elastix” in your system then provide the full path to run e.g. elastix_Path\elastix.exe -f …</p>
<p>You can also download elastix binaries for windows from <a href="http://elastix.isi.uu.nl/" rel="nofollow noopener">elastix official website</a> and read the elastix manual to learn how to use it.</p>

---

## Post #19 by @lassoan (2018-05-14 02:57 UTC)

<p>On Windows, Elastix is bundled with the SlicerElastix extension. Elastix path and complete list of command-line arguments that are passed to Elastix are all shown if you enable “Show detailed log during registration” in Advanced section.</p>

---
