# Is there a way to wait until certain condition are met before continuing and deleting nodes in using a python script

**Topic ID**: 6396
**Date**: 2019-04-04
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-wait-until-certain-condition-are-met-before-continuing-and-deleting-nodes-in-using-a-python-script/6396

---

## Post #1 by @Kevin.Kn (2019-04-04 17:14 UTC)

<p>I am currently going through directories, grabbing fcsv and image pairs, and then loading them into slicer using a python script.</p>
<pre><code class="lang-auto"># Image/fcsv loading
[success, markupNode] = slicer.util.loadMarkupsFiducialList(fcsv, returnNode=True)
[success, imageNode] = slicer.util.loadVolume(image, returnNode=True)

#want to wait here until some condition is met

# Node deletion
slicer.mrmlScene.RemoveNode(markupNode)
slicer.mrmlScene.RemoveNode(imageNode)
</code></pre>
<p>My goal is to be able to somehow wait inbetween the reading and the removing of the node, so I can check the fcsv files for accuracy and edit them if possible.</p>
<p>Is there a way to do this?</p>
<p>I tried using a simple input() command to wait for an enter keypress , but I get an ‘EOFError: EOF when reading a line’ when trying to do this</p>

---

## Post #2 by @jcfr (2019-04-04 18:44 UTC)

<p>It looks like you want to continuous the processing once the user had an opportunity to validate the content of the files by inspecting the loaded image and markups.</p>
<p>To achieve this, you could look at what is done <a href="https://github.com/JoostJM/SlicerCaseIterator" rel="nofollow noopener">https://github.com/JoostJM/SlicerCaseIterator</a></p>

---

## Post #3 by @Kevin.Kn (2019-04-04 19:15 UTC)

<p>Thanks, Ill take a look at this.</p>
<p>I found a workaround using raw_input() that waits for an enter press command, but the embedded python in 3d slicer requires you to enter 3 characters before the input is interpreted as a string/keypress.</p>
<p>otherwise it gives you an EOFError, which im thinking is because it places the start of the user input before the ‘&gt;&gt;&gt;’ that ive seen used by python in other places</p>

---

## Post #4 by @bserrano (2023-10-30 10:56 UTC)

<p>Hi,</p>
<p>I’m facing the same problem. I have an script that helps the user through various steps. For example:</p>
<pre><code class="lang-auto">def functionName():
  # step1:
  _Ask the user to segment
  
  # step2:
  _Save segmentation
  
  # step3:
  _Ask the user to place tow fiducials
  
  # step4:
  _Use those fiducials to generate a centerline
  
  # step5:
  _Save results

</code></pre>
<p>I need my code to wait between step1 and step2 and between step3 and step4, since I need the user to manually segment or place the control points. Now I’m using (ex) <code>input("Place fiducial points and press key to continue...")</code> but I don’t want the user to come back to the python interactor each time. Instead I want a key shortcut “continue”.</p>
<p>I know I can implement this using:</p>
<pre><code class="lang-auto">shortcutNext = qt.QShortcut(slicer.util.mainWindow())
shortcutNext.setKey(qt.QKeySequence('C'))

shortcutNext.connect('activated()', someFunction)
</code></pre>
<p>But then I guess I need to rewrite the code in <code>functionName()</code> and replace it with different funcions like <code>step1()</code>, <code>step2()</code>… and call them in order depending the number of times the user has pressed “C”. Am I right? Is there another posibility similar to <code>input()</code> that can be in the same place in the code?</p>
<p>I’m thinking about something like:</p>
<pre><code class="lang-auto">while(not continue):
   wait
</code></pre>
<p>but slicer gets blocked.</p>

---

## Post #5 by @pieper (2023-10-30 13:42 UTC)

<p>Your code could be event driven, in the sense that you should be observing the scene for nodes being added or modified and then you can move through from step to step.  Since Slicer operates asynchronously you can implement these state changes either base on events from the scene or from users pressing buttons to move from step to step and you can validate if the step change is allowed based on what data is in the scene.</p>

---

## Post #6 by @mikebind (2023-10-30 23:27 UTC)

<p>Another solution would be to develop a python module that would allow you to carry out the steps via GUI.  You would still need to break up the function logic to the various steps, but you would gain making it easy to have others carry out your process.  There is definitely a bit of a learning curve getting started, but the working example module code provided by the Extension Wizard module is a great starting point if you want to try heading in this direction.</p>
<p>Another alternative is to have the user do the segmentation and place the fiducials first, and run your code at that point, with the segmentation and fiducials is inputs.  That way there aren’t any steps your code has to wait for.  It can save the segmentation to a file, use the fiducials to generate a centerline (I presume using the segmentation), and save the results.</p>

---

## Post #7 by @bserrano (2023-10-31 08:47 UTC)

<p>Thanks. Where I can find an example of this kind of implementation?</p>

---

## Post #8 by @bserrano (2023-10-31 08:51 UTC)

<p>I’ll take a look at the Extension Wizard Module, if you know where to find documentation or examples, it would be great <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @pieper (2023-10-31 13:26 UTC)

<p>Basically all modules work this way.  For example if you look at the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py">Endoscopy code</a> you can see that  some of the buttons aren’t enabled until some of the prerequisite combo boxes have valid values selected.  So in a similar way, your module could have a combo box to select a segmentation and a button that when clicked creates a segmentation and shows the segment editor widget.  The use would then need to perform the segmentation and then push a button to create the fiducials.  You just don’t enable the next steps until the input data is available.</p>

---

## Post #10 by @lassoan (2023-10-31 19:53 UTC)

<p>The PerkLab programming tutorial is a good way to get started with Python scripting in Slicer. You can find the link from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">Slicer developer training page</a>.</p>

---
