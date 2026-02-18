# Running TotalSegmentator from Python Console

**Topic ID**: 35461
**Date**: 2024-04-12
**URL**: https://discourse.slicer.org/t/running-totalsegmentator-from-python-console/35461

---

## Post #1 by @evaherbst (2024-04-12 15:49 UTC)

<p>Hello,</p>
<p>I wrote a script to run TotalSegmentator from the python console so I can automatically change some names and run it on several volumes in the scene.</p>
<p>It works, but there is still the prompt whether to run it in slow CPU mode or fast, even though I specified in the code to set fast = FALSE:</p>
<blockquote>
<p>TotalSegmentator.process(inputVolumeNode, outputSegmentation, fast=False, cpu=False, task=“total”, subset=None)</p>
</blockquote>
<p>Does anyone know how to prevent the GUI prompt asking for slow or fast?</p>
<p>Thank you,<br>
Eva</p>

---

## Post #2 by @jamesobutler (2024-04-12 16:53 UTC)

<p>I think it is trying to warn you that you are requesting to use GPU (<code>cpu=False</code>), but you have no CUDA supported GPU so it is falling back on the CPU. Since the warning says it may take an hour for full resolution results on CPU are you actually sure you want to go with that method?</p>
<p>It looks like you would have to modify the following code:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/7aa1ca252261a2b6d026cf58d662286aac904fa3/TotalSegmentator/TotalSegmentator.py#L890-L902">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/7aa1ca252261a2b6d026cf58d662286aac904fa3/TotalSegmentator/TotalSegmentator.py#L890-L902" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/7aa1ca252261a2b6d026cf58d662286aac904fa3/TotalSegmentator/TotalSegmentator.py#L890-L902" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerTotalSegmentator/blob/7aa1ca252261a2b6d026cf58d662286aac904fa3/TotalSegmentator/TotalSegmentator.py#L890-L902</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="890" style="counter-reset: li-counter 889 ;">
          <li>if not fast and not cuda:</li>
          <li></li>
          <li>    import ctk</li>
          <li>    import qt</li>
          <li>    mbox = ctk.ctkMessageBox(slicer.util.mainWindow())</li>
          <li>    mbox.text = "No GPU is detected. Switch to 'fast' mode to get low-resolution result in a few minutes or compute full-resolution result in about an hour?"</li>
          <li>    mbox.addButton("Fast (~2 minutes)", qt.QMessageBox.AcceptRole)</li>
          <li>    mbox.addButton("Full-resolution (~50 minutes)", qt.QMessageBox.RejectRole)</li>
          <li>    # Windows 10 peek feature in taskbar shows all hidden but not destroyed windows</li>
          <li>    # (after creating and closing a messagebox, hovering over the mouse on Slicer icon, moving up the</li>
          <li>    # mouse to the peek thumbnail would show it again).</li>
          <li>    mbox.deleteLater()</li>
          <li>    fast = (mbox.exec_() == qt.QMessageBox.AcceptRole)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @evaherbst (2024-04-14 07:04 UTC)

<p>Thanks James!<br>
The time estimation is hard coded, it takes less than 10 minutes for me.</p>
<p>Also planning to use the code on a cuss enabled computer in the future.</p>
<p>Thanks!<br>
Eva</p>

---

## Post #4 by @hmaguile (2024-04-15 12:07 UTC)

<p>Hi Eva,</p>
<p>Are you creating a script to run the TotalSegmentor on several volumes? Have you been able to do this? If so, I would be very interested in knowing how you have done this.</p>
<p>Best,<br>
Hans Martin</p>

---

## Post #5 by @evaherbst (2024-04-16 08:16 UTC)

<p>Hi Hans,</p>
<p>It is still a work in progress (and not my main focus right now) but yes, I am working on it and will keep you updated.</p>
<p>Best,<br>
eva</p>

---

## Post #6 by @evaherbst (2024-04-19 16:36 UTC)

<p>Hi again <a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
Do you know if there is a way to someone automatically trigger selection of the second GUI button option (slow option) without having to adjust the TotalSegmentator plugin code itself?</p>
<p>Thank you,<br>
Eva</p>

---

## Post #7 by @jamesobutler (2024-04-19 16:56 UTC)

<p>Not that I know of. Your best bet is to modify that SlicerTotalSegmentator code where I linked previously to comment out the pop-up display. Otherwise running on a system with CUDA support would also avoid the pop-up.</p>

---

## Post #8 by @lassoan (2024-04-20 00:55 UTC)

<p>We should modify the logic code to not show any popup (or at least have an option to suppress). By the way, if you run Slicer with <code>--testing</code> argument then I think all popups are bypassed.</p>

---

## Post #9 by @evaherbst (2024-04-22 10:28 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
I modified my local version of the code to commend out everything under “if not fast and not cuda.” and replacing it with a print statement “using slow mode”.</p>
<p>This works well.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Maybe the section can be removed altogether from the TotalSegmentator plugin?</p>
<p>Since for the GUI the user can already designate whether to use Fast mode or not.</p>
<p>I guess the original point of the pop up was to warn users that using fast mode without cuda can take a long time. But the  “~50 minutes” is also a big overestimate in some cases.</p>
<p>So my suggestion would be to just remove this section altogether. Users can then select “fast” mode or not in the GUI or the code arguments and can test themselves whether fast mode is necessary.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #10 by @Matteboo (2024-04-22 11:47 UTC)

<p>A way to do it could be to put the checkbox ask before the call to <em>process</em> in the function <em>onApplyButton</em> . That way for the user nothing changes but we can call the process function without the need for human intervention</p>
<p>I tried to make a pull request on the github with the above changes</p>

---

## Post #11 by @evaherbst (2024-04-22 12:58 UTC)

<p><a class="mention" href="/u/matteboo">@Matteboo</a> that is a nice idea.</p>
<p>I also suggest changing “Full-resolution (~50 minutes)” to "“Full-resolution (up to ~50 minutes)” since on my computer it runs in a few minutes.</p>

---

## Post #12 by @evaherbst (2024-04-22 13:45 UTC)

<p>I also noticed I never replied to the cpu=false point (good question).</p>
<p>I want to set cpu=false because otherwise it forces cpu use.<br>
As far as I understand, if I set cpu=false, it should then work with gpu if cuda is enabled, and if not, still resort to cpu.</p>

---

## Post #13 by @lassoan (2024-04-22 16:38 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="9" data-topic="35461">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>Maybe the section can be removed altogether from the TotalSegmentator plugin?</p>
</blockquote>
</aside>
<p>The current code is the result of lots of feedback and troubleshooting on computers on thousands of users. All those checks and warnings are guardrails for users to prevent them from reporting that “Slicer crashed” (it actually just hangs for a long time, while the computation is in progress). So, simply removing these checks is not the best solution.</p>
<p>Adding a <code>silent</code> option (enabled by default, disabled when the module widget calls it) to skip any GUI interaction and just do what is specified in the input arguments would be a very simple change. It would be great if you could implement this, test that it works for you, and send a pull request.</p>
<p>Current location of checking the parameters and displaying of the popups is incorrect: all GUI interactions belong to the module widget and not to the logic. If you can implement this change so that it all works for you but the current behavior via the GUI does not change then that would be even better. maybe instead of a popup, a warning icon should appear next to the “Apply” button when runtime is likely to be excessive.</p>
<p>If you have any suggestion for changing wording of messages then please send a pull request. I also experienced that that full-resolution segmentation on CPU can run on a 20-core workstation with 64GB RAM within a few minutes, but on an i7 laptop with 16GB RAM typical runtime is around 40 minutes. Maybe some of this information could be added to popup messages and documentation.</p>
<p>Also note that we are releasing a new extension tomorrow: MONAIAuto3DSeg. It has similar models (low-res/high-res with similar hardware requirements) like TotalSegmentator, but better in many sense: does not contain only a few models, but over 30; not just healthy anatomy, but various abnormalities; not just CT, but also MRI (and some private models successfully used on ultrasound, too); it can accept not just a single input image but multiple images; it can run in the background and segmentation can be interrupted anytime; has less Python package dependencies and installs more cleanly and can be trained faster than nn-UNet, etc. I would recommend to check it out.</p>

---

## Post #14 by @evaherbst (2024-04-22 16:54 UTC)

<p>Thank you Andras for the quick reply.</p>
<p>I am currently running on i7 laptop with 16GB RAM but I just realized that maybe it is running much faster because I have small crop volumes of the shoulder joint instead of a whole body.</p>
<p>I will try what you suggested.</p>
<blockquote>
<p>If you can implement this change so that it all works for you but the current behavior via the GUI does not change then that would be even better. maybe instead of a popup, a warning icon should appear next to the “Apply” button when runtime is likely to be excessive.</p>
</blockquote>
<p>I was also thinking this could be a good solution to keep the warning.<br>
I will try to make the adjustments you proposed.</p>
<p>Also note that we are releasing a new extension tomorrow: MONAIAuto3DSeg<br>
This is great, thank you! Excited to try it.</p>
<p>Best,<br>
Eva</p>

---

## Post #15 by @evaherbst (2024-04-22 17:36 UTC)

<p>I am looking into the code and have an idea how to do this.</p>
<p>I see the widget checks if buttons are clicked/boxes are selected in lines 104-116 of  def setup, and then runs some functions if they are (e.g. for</p>
<p>I want to add a line that checks if the Fast box is toggled and then run a function called onSetSlow that incorporated the GUI warnings that we discussed.</p>
<p>I see that I can use:<br>
self.ui.fastCheckBox.connect(‘toggled(bool)’,self.myFunction) to run a function <strong>if the Fast box is toggled</strong></p>
<p>What syntax would I need to check if the box is NOT toggled?<br>
To run the warning if fast mode is not selected?</p>
<p>Thank you!<br>
Eva</p>

---

## Post #16 by @lassoan (2024-04-24 01:30 UTC)

<p>I would recommend to add one more argument to the <code>process</code> method:  <code>interactive</code> (set to False by default). If <code>interactive=True</code> then the method works the same way as now (the widget will call the method this way). If <code>interactive=False</code> then no popups are displayed but the method does what the <code>fast</code> and <code>cpu</code> flags dictate (you will call the mwthod this way when doing batch processing).</p>

---

## Post #17 by @evaherbst (2024-04-24 09:03 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>Thank you for the suggestion.</p>
<p>I implemented it and it works for me (tested with GUI which gave popup warning, and via command line which did not give popup warning).</p>
<p>If you could also confirm it works for you that would be great.</p>
<p>I also adjusted the time estimate in the pop up warning about slow mode.</p>
<p>Thank you,<br>
Eva</p>

---
