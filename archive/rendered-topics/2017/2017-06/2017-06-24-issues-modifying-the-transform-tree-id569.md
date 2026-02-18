# Issues Modifying the Transform Tree

**Topic ID**: 569
**Date**: 2017-06-24
**URL**: https://discourse.slicer.org/t/issues-modifying-the-transform-tree/569

---

## Post #1 by @j-f (2017-06-24 20:03 UTC)

<p>Hi all,</p>
<p>my team is currently developing a Slicer/Python module for a internal research project.<br>
At the moment I am still waiting for the permission to publish parts of the source code here, so I cannot provide you with the entire plugin code so far (which hopefully will change soon <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">).</p>
<p>What the plugin is essentially loading multiple volumns and performs some registrations (via BRAINS).<br>
This finally gives me the following (linear) transform tree:<br>
volumeT2h → volumeT2 → volumeT1 → volumeCiss<br>
where “-&gt;” is the registration transform.</p>
<p>So I want to put volumeT1 into the “global” world coordinate system. To do so, I copy the transform from volumeT1 to volumeCISS, invert the linear matrix and perform the following commands:</p>
<blockquote>
<blockquote>
<p>volCiss.SetAndObserveTransformNodeID(tfCissToT1.GetID())  &lt;— tfCissToT1 is the inverted transform<br>
volT1.SetAndObserveTransformNodeID(None)<br>
volT1.Modified()   &lt;— may not required</p>
</blockquote>
</blockquote>
<p>The registration steps as well as the transform handling and the three lines above are executed by a procedure inside my module.</p>
<p>And here is the weird behavior: After the procedure has finished, the transform tree remains unchanged (only) for volT1, which still “observes” the tfT1toCiss, whereas volT1 should actually be in world space.</p>
<p>So I tried to debug this issue with the debugger (PyCharm) and right after these three lines the evaluation of the volT1 node tells me that there is no transform node assigned to volT1. But again, after the procedure has finished, the SAME evaluation (done on the internal Slicer/Python console) tells me, that volT1 is assigned to tfT1toCiss.</p>
<p>In addition to that, if I then execute the three lines (above) manually inside the Slicer/Python console, the commands work “correctly” and I finally get the expected result.</p>
<p>I finally modified the procedure to the following scheme:</p>
<blockquote>
<p>def my_procedure():<br>
…do_some_preprocessing_and_registrations()<br>
…my_three_lines_from_above()<br>
…[At this point, my debugger tells me that volT1 has no transform assigned anymore]<br>
…try:<br>
…import code<br>
…code.interact(local=locals())<br>
…except SystemExit:<br>
…pass<br>
…[At this point, volT1 has the unwanted transform assigned, again]<br>
…my_three_lines_from_above() [again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> ]<br>
…[At this point, volT1 has the no transform assigned. Yeah!]</p>
</blockquote>
<p>(Dots indicate whitespaces.)</p>
<p>At the call code.interact(), an interactive interpreter is accessable inside the Slicer/Python console, in which I always type in “exit()”. Now, aside that console-exit()-workaround-thing, the procedure works as desired.</p>
<p>This behavior is waaaaay unexpected to me and, unfortunately, out of my knowledge scope <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>May some of you folks have an idea, why Slicer currently behaves like this.</p>
<p>Again, I’m going to talk to my team in order to get the permission to publish the entire source ASAP.</p>
<p>Cheers,<br>
Johann</p>

---

## Post #2 by @lassoan (2017-06-24 20:51 UTC)

<p>We cannot reproduce the problem based on the information you provided and without that we cannot investigate or fix anything. Please post a complete python snippet that reproduces the problem. You can start by loading some images using SampleData volume, assigning parent transforms, setting transformation matrices in them, etc.</p>

---

## Post #3 by @lassoan (2017-06-24 20:56 UTC)

<aside class="quote no-group quote-modified" data-username="j-f" data-post="1" data-topic="569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/d26b3c/48.png" class="avatar"> j-f:</div>
<blockquote>
<p>SetAndObserveTransformationNodeID</p>
</blockquote>
</aside>
<p>Do you actually have this in your code? There is no such method in Slicer.</p>

---

## Post #4 by @lassoan (2017-06-24 21:05 UTC)

<p>One more thing: when a registration CLI module completes the registration successfully, it sets the computed transform as a parent of the moving volume (so that you can actually see the registration result). You may swap fixed/moving volumes you don’t like this or just set the desired parent transforms after the registration is completed. Note that CLI modules run in the background by default and they set the parent transform when the registration is completed (it can happen anytime). If it confuses your module then either wait for completion of the registration or add an observer to the CLI module node and reorganize the tree when the registration is finished.</p>

---

## Post #5 by @j-f (2017-06-24 23:39 UTC)

<p>Wow! Thank you for your fast response!</p>
<p>Yes indeed, the method I am referring to is <em>SetAndObserveTransformNodeID</em>.</p>
<p>Sorry, I forgot to mention that I am using a recent nightly build of Slicer. But the described behavior is equal to Slicer 4.5.</p>
<p>I’m going to try to get the permission next week. Then I will report back to you.</p>
<p>Cheers,<br>
Johann</p>

---

## Post #6 by @j-f (2017-06-27 15:54 UTC)

<p>I have uploaded a slightly debloated version of the widget with an example dataset integrated.<br>
You can find it here:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/zrug9kyd9wxkujt/TestWidget.zip?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:214/200;"><img src="https://cfl.dropboxstatic.com/static/images/logo_catalog/glyph_m1%402x.png" class="thumbnail" width="214" height="200"></div>

<h3><a href="https://www.dropbox.com/s/zrug9kyd9wxkujt/TestWidget.zip?dl=0" target="_blank" rel="nofollow noopener">Dropbox - Link not found</a></h3>

<p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Short instruction to trigger the strange behavior:<br>
-Right after you start the widget, click at the “Load data and init” button.<br>
-Set RotationIS to -180.0<br>
-Set LR to 180.0, PA and IS to 0.0!<br>
-Switch back to the test widget.<br>
-Click at “Run global registrations”.</p>
<p>After a few seconds the Python prompt will show up in interactive mode. At line 359 in the widget source ([1]), I applied the transform modification, which seems to be without effect. (volT1 is not in global world space…)<br>
To continue the execution, type “exit()” in the prompt.<br>
The code after line 377 ([3]) applies again the transform modification. But this time it is successful. (volT1 is now in global world space!)</p>
<p>Without the try/catch code ([2]) in between, both [1] and [3] fail to apply the transform modification. And I cannot figure out, why… <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>Cheers,<br>
Johann</p>

---

## Post #7 by @lassoan (2017-06-27 20:13 UTC)

<p>Calling <code>slicer.app.processEvents()</code> at the end of <code>runBRAINSRegistration</code> method will solve your problem.</p>
<p>Explanation: When a registration CLI module completes the registration successfully, it sets the computed transform as a parent of the moving volume (so that you can actually see the registration result). This parent transform setting does not happen immediately but when the the application becomes idle or slicer.app.processEvents() is called. So, you have to make sure you set the parent transform after the CLI module’s parent transform setting is completed.</p>

---

## Post #8 by @j-f (2017-06-27 21:12 UTC)

<p>Sir, you hit the nail right on its head!<br>
That function call finally fixes my issue.</p>
<p>Thank you for your support and for the explanation.</p>

---

## Post #9 by @j-f (2017-06-30 11:22 UTC)

<p>Sorry to ask you again.</p>
<p>We tried to call this slicer.app.processEvents() method and it worked fine on Windows and Linux. Unfortunately, it did not work on MacOS.<br>
Any ideas?</p>
<p>Cheers,<br>
Johann</p>

---

## Post #10 by @lassoan (2017-06-30 12:42 UTC)

<p>This should work the same way on all OS. Are you sure you use <em>exactly</em> the same Slicer and module versions?</p>

---

## Post #11 by @j-f (2017-06-30 17:00 UTC)

<p>I have prepared a slightly modified version of the first TestWidget example script (but needs volumes from TestWidget.zip):<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/vvruykrh4u6g5ca/dsgzValCissReg.py?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:214/200;"><img src="https://cfl.dropboxstatic.com/static/images/logo_catalog/glyph_m1%402x.png" class="thumbnail" width="214" height="200"></div>

<h3><a href="https://www.dropbox.com/s/vvruykrh4u6g5ca/dsgzValCissReg.py?dl=0" target="_blank" rel="nofollow noopener">Dropbox - Link not found</a></h3>

<p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I was able to verify the issue on my own Hackintosh setup on Slicer 4.6.</p>
<p>I just added the processEvents() to the BRAINS registration method.<br>
-Linux, Slicer 4.6+4.7(nightly) -&gt; works!<br>
-Windows Slicer 4.6 -&gt; works!<br>
-MacOS Slicer 4.6+4.7(nightly) -&gt; does not work!</p>
<p>The tested Slicer versions slightly differ. However, I guess this issue is not sensitive to the specific Slicer versions but to the used OS.<br>
Maybe it is a Qt/MacOS bug and Slicer-independent.</p>

---

## Post #12 by @lassoan (2017-06-30 21:47 UTC)

<p>Is the problem the same as before (moving volume’s parent transform is overwritten after the CLI execution is completed)?</p>
<p>Just for testing, you may add some delay and see if it changes things:</p>
<pre><code>slicer.app.processEvents()
time.delay(5)
slicer.app.processEvents()</code></pre>

---

## Post #13 by @j-f (2017-07-01 14:18 UTC)

<p>Yes, the problem is the same as before on MacOS.</p>
<p>I guess you mean time.sleep(5) as time.delay does not exist.<br>
Unfortunately, no changes using these three lines. (using time.sleep)</p>

---

## Post #14 by @lassoan (2017-07-04 16:09 UTC)

<p>I’m working on eliminating the need for processEvents() to make the results more deterministic. It may fix your problem on Mac. It’ll be available in a couple of days.</p>

---

## Post #15 by @j-f (2017-07-05 19:47 UTC)

<p>Thank you, sir!<br>
I’ll try it out as soon as the new version is available!</p>

---

## Post #16 by @lassoan (2017-07-06 16:08 UTC)

<p>I’ve made the mechanism more robust for setting parent transforms at the end of CLI module execution. Please test the nightly build that you can download tomorrow or later.</p>

---

## Post #17 by @j-f (2017-07-14 16:34 UTC)

<p>I finally managed to test the latest nightly build at all our MacOS setups and it seems to be fixed! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thank you for all your support!</p>

---
