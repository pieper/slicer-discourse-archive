# Is there a way to build a macro/script out of segment editor steps?

**Topic ID**: 4170
**Date**: 2018-09-22
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-build-a-macro-script-out-of-segment-editor-steps/4170

---

## Post #1 by @muratmaga (2018-09-22 15:56 UTC)

<p>Hello,</p>
<p>Let say, I want to apply a series of effects in segment editor to multiple datasets. Is there a way to record a ‘macro’ or build a script by interactively doing the steps in editor one time, and using that as a script? If not, this would be a good feature to introduce us, (aka non-programmer types) to python scripting in Slicer.</p>

---

## Post #2 by @pieper (2018-09-22 20:13 UTC)

<p>That sounds like a neat idea - I’m not sure how it exactly it would work in practice since each dataset may require different parameters or interactive input at various steps.</p>
<p>Do you know of any other software that provides a feature like this?</p>

---

## Post #3 by @lassoan (2018-09-23 02:26 UTC)

<p><strong>How can sequences be processed now</strong></p>
<ol>
<li>Process a sequence manually</li>
</ol>
<ul>
<li>set up processing (make sure “Save changes” is enabled for the output node in Sequence Browser module), set up processing parameters</li>
<li>apply processing to current frame (typically by a mouse click)</li>
<li>go to next frame (click Ctrl + Shift + right-arrow)</li>
<li>repeat the last two steps (mouse click then Ctrl + Shift + right arrow) until all frames are processed</li>
</ul>
<p>Up to maybe 10 frames and short processing time, manual workflow may be acceptable, but clearly not ideal.</p>
<ol start="2">
<li>Add custom modules for processing that is commonly needed for sequences. One example is Sequence Registration module.</li>
</ol>
<p>Although this requires only very small amount of software development and allows simple, optimized user interface, it would not be feasible to use this approach for all available operations in Slicer.</p>
<p><strong>What could be done?</strong></p>
<ol>
<li>Add sequence processor for operations implemented in CLI modules</li>
</ol>
<p>To automate processing, we could add Sequence processing module, where you could select a CLI module parameter node and a sequence browser node. The module could then use the sequence browser node to iterate through a sequence of nodes and process each of them using the chosen CLI module. This would probably work well, but it could only be used for CLI modules.</p>
<ol start="2">
<li>Record macro for one frame and apply it to all frame as recommended by <a class="mention" href="/u/muratmaga">@muratmaga</a>. This method could complement method 1 (which is only applicable to CLI modules). There is already macro recording and replay capability in Slicer (enable QtTesting in Application settings and then Record macro / Play macro options will appear in Edit menu. It would not be too difficult to create a module, which would apply a recorded macro to each frame in a sequence. Since so far Macro recorder has been mainly used by developers only, for generating test scripts, it may need some work to make it robust and polished enough for regular users. I’ve been also thinking about slightly changing the macro recorder to be able to create Python scripts as well, which would be easier to edit by developers or users with minimal programming knowledge.</li>
</ol>
<p>If anybody would like to explore these options I would be happy to help.</p>

---

## Post #4 by @muratmaga (2018-09-23 05:16 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
Yes, I agree at some point usually segmentation require user input/intervention and unlikely to be fully automated. One of my use cases is parameter sweeps on large volumes (1024x1024x1024 or bigger), which are typically simple, but time consuming tasks (e.g., running connected components with a number of different threshold values).</p>
<p>But more importantly, making the move from interactive to scripted tasks is a big time investment on users end, especially if one is not already familiar with python. I thought guiding them with some sort of a editable template customized to their needs would be a good way to entice them to make the investment.</p>
<p>I am not aware of any software that does this.</p>

---

## Post #5 by @pieper (2018-09-24 20:53 UTC)

<p>Maybe we can come up with some simple example use cases and see what a solution would look like.  I realize writing code can be a big step for some people, but it can be really efficient and flexible for things that would be really hard to express in a GUI (just as the opposite can sometimes be true).</p>
<p>I’m thinking we could have a much more entry-level python scripting tutorial with some handy recipes for automating common operations.  Perhaps using the new Jupyter infrastructure.</p>

---

## Post #6 by @brhoom (2018-11-14 18:17 UTC)

<p>This is already done in other software e.g. ImageJ  and it would be very useful to have in Slicer for automating simple tasks and also answering a lot of future python scripting questions.</p>

---

## Post #7 by @pieper (2018-11-15 16:35 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="6" data-topic="4170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>already done in other software e.g. ImageJ</p>
</blockquote>
</aside>
<p>Could you provide links to examples that you think are particularly useful?</p>

---

## Post #8 by @brhoom (2018-11-15 17:07 UTC)

<p>I am not sure what do you mean by examples, in Slicer or in ImageJ?</p>
<p>I used imageJ years ago  and I don’t work with it anymore but here is a  <a href="https://www.youtube.com/watch?v=icG87vuiVp8" rel="nofollow noopener">youtube video</a> explains the use in FIJI (a variant of imageJ).</p>
<p>A Slicer example: a user did some operations manually and wanted to have them in a python script to apply the same thing in a future or to to put this in a loop to process many images. If Slicer provides macros recording, the user can get the python code directly from the recorded macro. It is helpful, especially for beginners users in Slicer.</p>

---

## Post #9 by @lassoan (2018-11-15 20:27 UTC)

<p>It would be certainly useful if we could generate Python code directly from observing events.</p>
<p>There are things that would be very easy to automate, such as CLI execution (basically what is shown in the ImageJ youtube video), but most interactive features would be hard to capture at a meaningful level.</p>
<p>Probably recording MRML node changes would capture most of the interactions, but that would require some infrastructure development in MRML, which would allow observing node property changes. We’ve already started some work along these lines: node property macros are used at many places for node property read/write/print/copy; but there are no commonly used macros for get/set of node properties yet.</p>

---

## Post #10 by @brhoom (2018-11-16 08:29 UTC)

<p>An idea is to provide a logical variable for each interactive user event to print an equivalent script line(s) e.g. in the python interactor. When a user clicks on a “record macro”  or “stop recording” button this variable change its value.</p>
<p>Probably this needs a lot of work but the macros recording a good feature to have in the future.</p>

---

## Post #11 by @pieper (2018-11-19 16:57 UTC)

<p>We actually already have this feature:</p>
<ol>
<li>enable Qt Testing in the Developer page of the Application settings menu</li>
<li>restart Slcier</li>
<li>select Record Macro from the Edit menu</li>
<li>start recording</li>
<li>do actions</li>
<li>stop recording and save file</li>
<li>select Play Macro from the Edit menu</li>
<li>click Play to replay steps</li>
</ol>
<p><strong>Note</strong> that this can be a fragile operation and may not work across slicer versions (and may be there are other issues).</p>

---

## Post #12 by @brhoom (2018-11-19 18:06 UTC)

<p>Thanks for the info. I just checked it. Personally, I found the imageJ way is much simpler and easier to use for the purposes I mentioned. Here are some examples (not sure if it is already possible with Slicer macro):</p>
<ul>
<li>Getting a python code e.g. I loaded a model by drag and drop but I could not get a code that I can use in a python script to do the same thing.</li>
<li>Using the same macro with a new input model.</li>
<li>Using the same macro in a loop to process a number of input models.</li>
</ul>

---

## Post #13 by @pieper (2018-11-19 19:01 UTC)

<p>Yeah, the Qt Testing recorder isn’t ideal, but maybe it’s a part of solution.</p>
<p>Also for reference Blender has a <a href="https://blender.stackexchange.com/questions/6409/possible-to-replay-repetitive-tasks-using-python">some python script recording options</a> too.  I also remember seeing that blender included the python commands in the tooltips.</p>

---
