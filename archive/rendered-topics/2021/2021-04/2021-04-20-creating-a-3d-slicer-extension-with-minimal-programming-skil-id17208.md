# Creating a 3D Slicer extension with minimal programming skills

**Topic ID**: 17208
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/creating-a-3d-slicer-extension-with-minimal-programming-skills/17208

---

## Post #1 by @Vincebisca (2021-04-20 13:34 UTC)

<p>Operating system: Win64<br>
Slicer version: 4.11</p>
<p>Hello,</p>
<p>I am an Engineering Student, with a background in CAD Softwares and Product Design. Recently, for an internship project, I started to use 3D Slicer to perform segmentation on CT scans and MRI DICOMs. For this project, I want to create a little extension to optimize my workflow, using only existing features of the software (or extensions like SegmentEditorExtraEffect). My goal is mainly to recreate a custom GUI where I have only the features I use, in the sequence I need to have something intuitive.</p>
<p>My problem is that I have a really REALLY low knowledge in programming, and since I don’t really want to add any function nor do I need to automatize existing features, I wonder if there is any way to create a GUI that uses existing tools without having to code that much… What do you think?</p>
<p>Thank you in advance for your help !</p>

---

## Post #2 by @pieper (2021-04-20 20:00 UTC)

<p>Maybe somebody else here can chime in if they have been through this process recently.  I suspect it’s a challenge for a new developer to be learning python and slicer (vtk, qt, etc) all at the same time.  But if you are just creating buttons and rearranging widgets it’s certainly doable.</p>
<p>You can start with one of these tutorials and see how it fees:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a></p>

---

## Post #3 by @Vincebisca (2021-04-20 20:55 UTC)

<p>Thank you for your answer ! Effectively, I already saw this page and tried some tutorials. The hard thing for me is to understand what I’m doing… Because on some tutorials, it’s just a matter of copy pasting without much thinking, so I manage through the tutorial but can’t say that I learn that much. Other tutorials I don"t really understand because there are huge differences between the screenshots provided and what I actually see in the code. Maybe because things changed a bit (especially around the module extension wizard’s generated code).</p>
<p>That’s why I am a bit struggling (of course I will try other tutorials and do my best to learn as much as I can). I think that I still didn’t do a few tutorials on this page so I will do that, and I wanted to know if there’s maybe somewhere, even out of Slicer, where I can learn the basics to manage to understand the Slicer’s python code and modify a few things myself?</p>
<p>I appreciate any help and will keep the hard work to finally understand what I’m doing !</p>

---

## Post #4 by @mikebind (2021-04-20 20:56 UTC)

<p>Creating simple modules which basically just use existing Slicer capabilities but organize them into a sensible workflow for a particular task is a lot of what I do in Slicer. In my experience, I think this would be a challenge without some basic programming knowledge.  Designing your module GUI using QtDesigner is very intuitive and requires essentially no programming knowledge, but connecting the GUI to the functionality on the back end requires basic Python plus some familiarity with how Slicer does things (MRML nodes and things like that). You definitely do NOT need to be an expert programmer to do what you want, but you do need basic skills and a willingness to look through Slicer code examples and find how to do what you want.</p>
<p>This forum has lots of very helpful and responsive people on it and can be a great resource for when you inevitably get stuck on something.</p>

---

## Post #5 by @Vincebisca (2021-04-20 20:59 UTC)

<p>Yes that’s exactly what I want to do : for example understanding how to do a threshold button, or a watershed button, etc… I looked already a bit through QtDesigner and it’s indeed within my grasp. As for the code, I am really willing to dive in the code. The issue for now is that I don’t have a real “starting point” on which to start building some experience, and thus I’m a bit lost. If you have any particular place where I can learn the basics I will look through as much tutorials as I can !</p>

---

## Post #6 by @mikebind (2021-04-20 22:49 UTC)

<p>One of the best single places to look for how to do things using Python in Slicer is the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a>.  There are many examples there of how to accomplish a wide variety of tasks. For example, modifying a volume by thresholding is shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume" rel="noopener nofollow ugc">here</a> (note that this is not the same as creating a segment by thresholding; an example of that can be found in the links from <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Use_Segment_editor_effects_from_script_(qMRMLSegmentEditorWidget)" rel="noopener nofollow ugc">here</a>).  Also, I think the extension wizard’s auto-generated code still has a complete example of having a threshold button, and connecting it to a callback, so examining that carefully will show you how to connect a button click to an action.</p>
<p>One other suggestion as you’re getting started: in the extension wizard auto-generated example code, there is a fair amount of code which manages a “parameter node”.  This parameter node is primarily useful so that your module can save and restore its state with the scene, so that you could be partway through your workflow, save the scene, close Slicer, and at some point later, open Slicer, load the saved scene, and pick up exactly where you left off.  If that functionality is not important to you, you don’t really need to understand the parameter node yet, and you can mostly just ignore it and comment out any line which gives you an error when trying to read or modify the parameter node. (When you remove stuff you don’t need from the auto-generated UI, whenever the existing code refers to those deleted UI elements to store stuff in the parameter node, there will be errors).</p>
<p>Good luck, and feel free to post questions when you get stuck.</p>

---

## Post #7 by @lassoan (2021-04-20 23:06 UTC)

<p>I think there are two main approaches that you may try:</p>
<ul>
<li>A. Try to develop a module in Slicer and learn everything at once along the way.</li>
<li>B. First learn most important technologies that Slicer is built on and once you are familiar with those then learn how to use them in Slicer.</li>
</ul>
<p>It is up to you which works better for you.</p>
<p>If you choose option A, then you’ll get lost but you can ask specific questions here from time to time when you cannot figure out something yourself. The advantage of this method is that you don’t spend your time with working on some toy examples, but you are starting to go towards reaching your goal on day 1.</p>
<p>For option B, I could recommend materials listed in this post:</p>
<aside class="quote quote-modified" data-post="10" data-topic="2584">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/a-free-biomedical-image-analysis-and-visualization-2-day-course/2584/10">A free biomedical image analysis and visualization 2-day course</a> <a class="badge-category__wrapper " href="/c/announcements/events/27"><span data-category-id="27" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #ED207B;" data-parent-category-id="7" data-drop-close="true" class="badge-category --has-parent"><span class="badge-category__name">Events</span></span></a>
  </div>
  <blockquote>
    Participating at a 2-day course in person is a great learning opportunity. However, if you cannot make it, then there is online training material already available that should keep you busy for about a year: 

Read the <a href="https://www.vtk.org/vtk-textbook/">VTK textbook</a>, cover to cover, 2-3 times (I’m serious, read all of it; and read it several times, as in the first pass you’ll not have deep enough understanding to get all details); this is essential, don’t do anything else before you read the book completely at least once
Skim thr…
  </blockquote>
</aside>

<p>We’ll have our yearly 3-day bootcamp event where we teach our new students about basics of using and programming 3D Slicer. This year it will be a virtual event and the application is open to anyone (but we may need to prioritize applications if we get too many). If you are interested you can find the link to apply <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/README.md#perklab-bootcamp">here</a>.</p>

---

## Post #8 by @pieper (2021-04-21 00:16 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="6" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>This parameter node is primarily useful so that your module can save and restore its state with the scene, so that you could be partway through your workflow, save the scene, close Slicer, and at some point later, open Slicer, load the saved scene, and pick up exactly where you left off. If that functionality is not important to you, you don’t really need to understand the parameter node yet, and you can mostly just ignore it and comment out any line which gives you an error when trying to read or modify the parameter node.</p>
</blockquote>
</aside>
<p>This is great advice and I have also done that when trying to quickly develop a proof of concept.  I did one time get bitten by a bug where somehow something I’d deleted made Slicer crash at startup for reasons I never figured out so I had to start fresh.  It could be good for us to add some more templates that don’t aspire to be full working modules since they would be easier to understand.</p>

---

## Post #9 by @Vincebisca (2021-04-21 07:34 UTC)

<p>Alright, I will take a look at all the links send here and try my best to figure out at least the amount I need. Indeed, I tried to have a dive in the generated code to understand the buttons connexion. I did the LineIntensityProfile tutorial, but for example, the buttons on the tutorial were built though coding, not QtDesigner, so I found myself with something a lot different that I couldn’t really understand through the tutorial. I guess I’ll just need time to figure things out through analysis.<br>
Anyway I will try what you suggested !</p>

---

## Post #10 by @Vincebisca (2021-04-21 07:36 UTC)

<p>Yes I agree very much on these 2 options. I would prefer to chose Option A but I know that at some point some Option B will be needed so I’ll try to combine both and get there aas fast as I can improving the little knowledge I have !</p>
<p>I will also check out the course ! It seems really interesting !</p>

---

## Post #11 by @cpinter (2021-04-21 08:05 UTC)

<p>Great discussion!</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="3" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>on some tutorials, it’s just a matter of copy pasting without much thinking</p>
</blockquote>
</aside>
<p>Although the tutorials are made easy by providing the snippets you need to copy-paste, the goal of the tutorials are not to create simple useless modules, but to show how to make certain things possible. So a (maybe obvious) suggestion would be to think about what these copy-pasted snippets do exactly. If you cannot figure some of those out, please report back here in this thread, and I’ll update the tutorial with more comments. Many of the people here answering questions are seasoned programmers, so it’s quite hard to get into the skin of someone new to these things, so this kind of feedback would be actually useful to us.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="3" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>there are huge differences between the screenshots provided and what I actually see in the code</p>
</blockquote>
</aside>
<p>If you could please point to these instances we’ll update those resources that have diverted a lot and are hard to apply. Typically Slicer documentation is created by the members of the community in their free time, so we know some of it is out of date. However it takes extra time to go through them and find if something needs updating, so again, once you already found some, please help us by letting us know.</p>
<p>We (at some of the <a href="https://www.slicer.org/commercial-use.html">commercial partners</a>) are also thinking about Slicer programming training, but it will take time setting it up. We’ll make an announcement once we have a first event planned out. Until then another tutorial you could do (if you haven’t) is the PerkLab bootcamp one <a class="mention" href="/u/lassoan">@lassoan</a> mentioned: <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">here</a> is the programming tutorial. If at the end of your journey you have some suggestions please let us know.</p>

---

## Post #12 by @Vincebisca (2021-04-21 09:14 UTC)

<p>Yes I totally agree with the first part ! I try to understand everytime but it’s a bit harder to understand “why” it works sometimes, and why it doesn’t the rest of the time. For example when I try to modify some code, it doesn’t work and I don’t know why because I do not fully understand yet the structure. I tried this tutorial for example : <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g1363d5232e_0_153" class="inline-onebox" rel="noopener nofollow ugc">Developing extension in 3D Slicer - Google Slides</a><br>
I manage to create the QtDesigner interface, and then I tried to connect the button based on the one already existing and doing the same thing (Input Volume Selection) and just mimicking the code of the first one doesn’t seem to work.</p>
<p>On the tutorial, there is this instructions for the creation :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d345a40721ad9ef1d7bb38e077795e6935649f.png" alt="image" data-base62-sha1="5oCjvwpq9jyp2JLndiCGBu7qHbF" width="629" height="454"></p>
<p>But it doesn’t appear to be the same anymore in the generated code, I suspect that this part was replaced by QtDesigner’s GUI creation, which is great ! But as a consequence I find it hard to use this tutorial because I can’t adapt to the changes… I don’t know if I’m missing something obvious on the tutorial, but when I try to add the Second Volume Selector, I am not managing to have an actually functionnal ComboBox (the ComboBox remains grey, no selection possible). Since the code seem to have changed from when the tutorial was created, I can’t really refer to it so I tried the mimicking stuff I mentionned, without success yet</p>

---

## Post #13 by @cpinter (2021-04-21 09:37 UTC)

<p>This particular tutorial is more out of date than usual I’d say - it is 7 years old now. The Annotations infrastructure is deprecated, and we do not use the type of scripted modules where the UI was created from code.</p>
<p>Can you please try the PerkLab bootcamp tutorial I linked in my previous post? It is updated each year.</p>
<p>Just to answer the specific issue, I think your combobox is greyed out because the scene connection is not made. In Designer, you go to events mode (F4) and drag&amp;drop from the very edge of the widget to the combobox and select the signal/slot:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c23b99340c71ecfaa9c84494ddd6a6595ed57bb.png" alt="image" data-base62-sha1="d96sZchp3ErgwDvif89i2qQtDez" width="587" height="393"></p>
<p>From code you need to call <code>setMRMLScene(slicer.mrmlScene)</code> as you can also see in the screenshot you provided.</p>

---

## Post #14 by @Vincebisca (2021-04-21 09:41 UTC)

<p>Okay so that’s what I thought. i’ll stop using this one.</p>
<p>Yes I will anyway go through every link provided in this discussion, might take me several days (weeks? ^^) to do it but I will and let you know. Currently I am studying the first link sent by <a class="mention" href="/u/pieper">@pieper</a> but I will go on others soon enough too.</p>
<p>Okay thank you for this specific answer, I will try it out !</p>

---

## Post #15 by @Vincebisca (2021-04-21 13:09 UTC)

<p>Your advice worked on my selector problem, thanks ! I managed to do the first tutorial fairly entirely (not the sphere thing), except that I am not getting a functionnal auto update. I have been trying several things and I’m not getting what’s the problem. I would like to manage it since auto update is an interesting feature !</p>
<p>My function is as follows :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0443c6fa0fe6534b1e77a0ede1a88de82d24b971.png" data-download-href="/uploads/short-url/BJ7ySwn55GUkSFVveTLu7H3zWx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0443c6fa0fe6534b1e77a0ede1a88de82d24b971.png" alt="image" data-base62-sha1="BJ7ySwn55GUkSFVveTLu7H3zWx" width="690" height="286" data-dominant-color="444443"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">850×353 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I don’t really get how the part I marked really works, like I tried to see self.ui.inputSelector.currentNode and it’s not a boolean so I don’t get how it can work as an “if” condition. Tryed commenting it, didn’t change anything, so I’m a bit blocked</p>

---

## Post #16 by @mikebind (2021-04-21 16:45 UTC)

<p>First, you want to have the parentheses on the end of the <code>self.ui.inputSelector.currentNode()</code> in the <code>if</code> line as well.  In Python, if you use the name of a function with parentheses, then you call that function, but if you use the name without parentheses, you just get a reference to the function (and the function is not actually called).  Second, in an <code>if</code> statement, python treats almost anything as <code>True</code>, unless it is empty, <code>None</code>, zero, or explicitlly <code>False</code> (<a href="https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/" rel="noopener nofollow ugc">here’s a link</a> that gives you the real details).  The currentNode() function of node selectors returns the selected node (if one is selected) or <code>None</code> if there is no selected node.  Since <code>None</code> counts as <code>False</code> and a node would count as <code>True</code>, it works to include this in the <code>if</code>.</p>
<p>The first line after the <code>if</code> stores the currently selected node in <code>self.observedMarkupNode</code>, so that it can be accessed later in other parts of the code (like in the previous <code>if</code> where the observer we’re about to create is removed).  The next line creates an “observer” such that whenever the observed markups node is modified (by the user or by other code), another function (<code>self.onMarkupsUpdated</code>) is called.  Since <code>onMarkupsUpdated()</code> just calls <code>onApplyButton()</code>, the ultimate effect is that anytime the user makes changes to the markups, it is like they followed that by clicking the Apply button as well.</p>

---

## Post #17 by @Vincebisca (2021-04-22 07:48 UTC)

<p>Hello Mike, thank you for the answer, indeed the lack of parenthesis was weird. Fixed now. But it still isn’t working : when I move or add a markup, nothing happens, the displayed Center Of Mass doesn’t change. Can it be that since my “CenterOfMassValueLabel” is above the ApplyButton on the GUI, it doesn’t work because of that?<br>
Also in QtDesigner I linked the CheckBox with the scene through a “toggle”, should I change for click?</p>

---

## Post #18 by @Vincebisca (2021-04-22 09:32 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> you said that a lot of what you do on Slicer is rearranging the GUI to create new workflows so I have a few questions :</p>
<p>I want to create some kind of workflow interface as follows :</p>
<ol>
<li>File loading manually (drag and drop would be cool)</li>
<li>Selecting a segmentation scenario according to the type of image and anatomical parts to be treated</li>
<li>Segmentation using a limited set of methods (I want to display only the needed methods for this particular scenario, not everything that is available)</li>
<li>Exportation of the segments as STL files</li>
</ol>
<p>So my questions are :</p>
<ol>
<li>I would like to not overcrowd the interface, so I am thinking of doing something like several interfaces that are displayed in the order of the phases and linked with a “previous/next” button, is it feasible? Do I need to have several QtDesigner files with the specific interface on each or is it one file with different pages?</li>
<li>For the segmentation part especially, is there a way to fully reuse what is done in the segment editor but with just a limitation of the available effects? Or do I have to recreate the whole thing manually?</li>
<li>I’ve seen in QtDesigner that there is a SegmentEditorWidget that basically displays the whole thing at once but I have not been able yet to understand how the connexion is done. It seems a bit different from simple buttons. And can I edit this widget? Because I haven’t found a way to access the internal features of the Widget…</li>
</ol>
<p>Sorry for the amount of questions, I really appreciate any help !</p>

---

## Post #19 by @mikebind (2021-04-22 16:55 UTC)

<p>I haven’t been through that tutorial or ever done auto-updating in response to markups changes, and the full code isn’t shown, so I’m not sure I can help debug that much further.  You might take a look at <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_markup_point_position_is_modified" rel="noopener nofollow ugc">this code</a> from the script repository and see if that works for you and if you can adapt it to your purposes.</p>

---

## Post #20 by @mikebind (2021-04-22 17:41 UTC)

<aside class="quote no-group" data-username="Vincebisca" data-post="18" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>I want to create some kind of workflow interface as follows :</p>
<ol>
<li>File loading manually (drag and drop would be cool)</li>
</ol>
</blockquote>
</aside>
<p>I don’t know how to do this, but I believe it is possible. Loading via the Add Data method has never seemed cumbersome enough to me to pursue it.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="18" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<ol start="2">
<li>Selecting a segmentation scenario according to the type of image and anatomical parts to be treated</li>
</ol>
</blockquote>
</aside>
<p>Automatically? Then you need to come up with the decision algorithm and implement it. Manually? Then just pick your favorite UI method (buttons, radio buttons, etc.)</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="18" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<ol start="3">
<li>Segmentation using a limited set of methods (I want to display only the needed methods for this particular scenario, not everything that is available)</li>
</ol>
</blockquote>
</aside>
<p>I have used segment editor effects from my modules, but have not tried to put a limited set of interactive effects to be available to the user. However, it looks like <a href="https://discourse.slicer.org/t/how-to-remove-some-segment-editor-effects/16162">this discussion</a> has exactly what you want.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="18" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<ol start="4">
<li>Exportation of the segments as STL files</li>
</ol>
</blockquote>
</aside>
<p>This is straightforward. You can use <code>slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles()</code> to export to STL or OBJ files.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="18" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>So my questions are :</p>
<ol>
<li>I would like to not overcrowd the interface, so I am thinking of doing something like several interfaces that are displayed in the order of the phases and linked with a “previous/next” button, is it feasible? Do I need to have several QtDesigner files with the specific interface on each or is it one file with different pages?</li>
</ol>
</blockquote>
</aside>
<p>The simple method used in many Slicer modules is to have sections with collapsible buttons.  This allows areas which are not in current use to be collapsed and take up less room, allowing more screen space for the active area.  You can set up your code to automatically collapse and expand sections at the proper times. For example, if I have a section in a collapsible button which is <code>self.ui.CTRegistrationAreaCB</code> I can collapse it with <code>self.ui.CTRegistrationAreaCB.collapsed = True</code>.  For another approach, I believe Qt also allows tabbed layouts, but I’ve never tried that or looked into it so I can’t really help with that. Another possible approach would be to have multiple modules that you switch between (see <a href="https://discourse.slicer.org/t/create-a-workflow-between-modules/8510">this discussion</a>).  Also, I would highly recommend taking a look at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">Slicelets</a>.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="18" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<ol start="2">
<li>For the segmentation part especially, is there a way to fully reuse what is done in the segment editor but with just a limitation of the available effects? Or do I have to recreate the whole thing manually?</li>
<li>I’ve seen in QtDesigner that there is a SegmentEditorWidget that basically displays the whole thing at once but I have not been able yet to understand how the connexion is done. It seems a bit different from simple buttons. And can I edit this widget? Because I haven’t found a way to access the internal features of the Widget…</li>
</ol>
</blockquote>
</aside>
<p><a href="https://discourse.slicer.org/t/how-to-remove-some-segment-editor-effects/16162">This discussion</a> looks like it answers your question directly.</p>
<p>If you want to see an example of a working module which uses specific segment editor effects (but not the same way as they appear in the Segment Editor module) you could take a look at <a href="https://github.com/mikebind/Heartbeat4D/blob/main/PropagateSegToOtherPhases.py" class="inline-onebox">Heartbeat4D/PropagateSegToOtherPhases.py at main · mikebind/Heartbeat4D · GitHub</a> The code there is old, written before Qt Designer became the default way of creating the UI, but it still works fine.  It makes use of thresholding, grow from seeds, erode, close holes, masking, creating empty segments, and copying from one segmentation to another.</p>

---

## Post #21 by @lassoan (2021-04-23 03:44 UTC)

<p>I’ve created a small example project of a slicelet (3D Slicer running with a simplified GUI) that you might find useful. It is only for loading an image, segmenting it, and saving the result. See more details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="inline-onebox">Documentation/Nightly/Developers/Slicelets - Slicer Wiki</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9a7064828bdb466549d82fcbf2407be4c9ea9f6.jpeg" data-download-href="/uploads/short-url/ocOxxkCeZEUf4tBfyji28mf88Zw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9a7064828bdb466549d82fcbf2407be4c9ea9f6_2_690x496.jpeg" alt="image" data-base62-sha1="ocOxxkCeZEUf4tBfyji28mf88Zw" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9a7064828bdb466549d82fcbf2407be4c9ea9f6_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9a7064828bdb466549d82fcbf2407be4c9ea9f6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9a7064828bdb466549d82fcbf2407be4c9ea9f6.jpeg 2x" data-dominant-color="9F9F9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×602 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can easily customize everything and can switch between simplified/full Slicer GUI by adding a keyboard shortcut.</p>

---

## Post #22 by @Vincebisca (2021-04-23 08:17 UTC)

<p>Wow that’s a lot of information from everyone, thanks !</p>
<aside class="quote no-group" data-username="mikebind" data-post="20" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I have used segment editor effects from my modules, but have not tried to put a limited set of interactive effects to be available to the user. However, it looks like <a href="https://discourse.slicer.org/t/how-to-remove-some-segment-editor-effects/16162">this discussion</a> has exactly what you want.</p>
</blockquote>
</aside>
<p>This is quite exactly what I need indeed ! And I managed to adapt it to the Qt created Widget in Andras’ Slicelet example ! That is so great !</p>
<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve created a small example project of a slicelet (3D Slicer running with a simplified GUI) that you might find useful. It is only for loading an image, segmenting it, and saving the result. See more details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Slicelets - Slicer Wiki</a></p>
</blockquote>
</aside>
<p>Yes I saw it before but I didn’t have the knowledge to understand it, now I do understand a lot more! This is very useful and very close to what I want to achieve, thank you!</p>
<p>I am testing it and there are a few things I notice :</p>
<ul>
<li>My Slicer seems to run a bit slower when using the module, is it to be expected?</li>
<li>When I run it, and then I load or select a DICOM file in the Database, I don’t find a way to come back to the module page. Is there any way for me to add the icon of the module in the toolbars? So that the user can come back to it? I have tried to edit the code in the showSingleModule section (adding lines in keeptoolbars, commenting others underneath,…) but didn’t succeed.</li>
<li>the same way, I would like to show the ToolBars to control the views and the 3D (switching between views, navigating through the Slices, etc…) but commenting the slicer.util.setViewControllersVisible(not singleModule) line doesn’t seem to work</li>
</ul>
<p>I think the Slicelet example is a great base for me to learn and do trials to achieve what I want ! thank you !</p>

---

## Post #23 by @lassoan (2021-04-23 15:26 UTC)

<aside class="quote no-group" data-username="Vincebisca" data-post="22" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>My Slicer seems to run a bit slower when using the module, is it to be expected?</p>
</blockquote>
</aside>
<p>It is exactly the same Slicer (just some widgets are hidden), so it should not be any slower. If it is indeed slower then maybe there are some error/warning messages flooding the application log - you will see it when you check the logs.</p>
<p>All the other things that you describe should work, probably there are just some trivial errors. You can find them easily by attaching a Python debugger (PyCharm, Visual Studio Code, …) and step through your code line by line.</p>

---

## Post #24 by @Vincebisca (2021-04-23 15:39 UTC)

<p>Okay I see, then it was also maybe my computer struggling a bit!</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="22" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<ul>
<li>When I run it, and then I load or select a DICOM file in the Database, I don’t find a way to come back to the module page. Is there any way for me to add the icon of the module in the toolbars? So that the user can come back to it? I have tried to edit the code in the showSingleModule section (adding lines in keeptoolbars, commenting others underneath,…) but didn’t succeed.</li>
<li>the same way, I would like to show the ToolBars to control the views and the 3D (switching between views, navigating through the Slices, etc…) but commenting the slicer.util.setViewControllersVisible(not singleModule) line doesn’t seem to work</li>
</ul>
</blockquote>
</aside>
<p>Since then, I managed to handle a lot better the interface changes and I’m starting to build a fairly satisfying interface for my use. But I still didn’t find the way to add an icon to get back to the module on the toolbar (to come back from the DICOM database), neither a way to display the navigating tool for the axis and 3D view displays (usually there is a slider with also a pin to show various options to switch between files, etc…) Is it possible to get these two things back on the interface by modifying the ToolBar section in the code?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f0f226cf602c1127a8c317f23ede2e9890ecc9b.png" data-download-href="/uploads/short-url/kpyHDandgdI2deBTFZaePe9lxWz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f0f226cf602c1127a8c317f23ede2e9890ecc9b_2_576x500.png" alt="image" data-base62-sha1="kpyHDandgdI2deBTFZaePe9lxWz" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f0f226cf602c1127a8c317f23ede2e9890ecc9b_2_576x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f0f226cf602c1127a8c317f23ede2e9890ecc9b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f0f226cf602c1127a8c317f23ede2e9890ecc9b.png 2x" data-dominant-color="313131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">727×630 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Around there I guess? Did various tries without success…</p>

---

## Post #25 by @lassoan (2021-04-23 15:47 UTC)

<aside class="quote no-group" data-username="Vincebisca" data-post="24" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>But I still didn’t find the way to add an icon to get back to the module on the toolbar (to come back from the DICOM database)</p>
</blockquote>
</aside>
<p>You can add a button that switches the active module and/or changes the view layout (that shows slice and 3D views instead of the DICOM browser). You can find examples in the script repository.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="24" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>display the navigating tool for the axis and 3D view displays (usually there is a slider with also a pin to show various options to switch between files, etc…)</p>
</blockquote>
</aside>
<p>You can show/hide view controllers by calling <code>setViewControllersVisible</code>.</p>

---

## Post #26 by @Vincebisca (2021-04-26 07:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can show/hide view controllers by calling <code>setViewControllersVisible</code> .</p>
</blockquote>
</aside>
<p>Thanks ! It worked and I understand a lot better how the hide/show works.</p>

---

## Post #27 by @Vincebisca (2021-04-26 09:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can add a button that switches the active module and/or changes the view layout (that shows slice and 3D views instead of the DICOM browser). You can find examples in the script repository.</p>
</blockquote>
</aside>
<p>I have searched the repository but I don’t think that what I want is adding a view layout. To be precise, what I am trying to do is displaying the “Favorite Modules” toolbar, and if possible edit it to display only my module or at least adding my module to the list through Python. I don’t know if I can do that. I have been trying to do the same hide/show manipulation as for the other toolbars but I don’t find the right way to call it and I wasn’t able to find any documentation on that.</p>
<p>I am getting really close to what I want so thanks for the patience ! Helps a lot</p>

---

## Post #28 by @lassoan (2021-04-26 13:30 UTC)

<p>DICOM browser is shown in the view layout that’s why changing the view layout may be useful (you can be in the DICOM module and show the browser or show slice&amp;3D viewers).</p>
<p>You may show the favorites toolbar (using standard Qt functions or convenience methods in slicer.util) but if you know exactly which modules you want to use then you can have a simpler, more compact GUI by placing a few buttons for <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#switch-to-a-different-module">switching between modules</a>.</p>

---

## Post #29 by @Vincebisca (2021-04-26 13:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="28" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>DICOM browser is shown in the view layout that’s why changing the view layout may be useful (you can be in the DICOM module and show the browser or show slice&amp;3D viewers).</p>
</blockquote>
</aside>
<p>I am not sure I understand it correctly. What you mean by “view layout” is the toolbar just under File/Edit/View/Help, or is it the place where you can chose different layouts for the 2D and 3D views like “Four up” “Only 3D” etc?</p>
<aside class="quote no-group" data-username="lassoan" data-post="28" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may show the favorites toolbar (using standard Qt functions or convenience methods in slicer.util) but if you know exactly which modules you want to use then you can have a simpler, more compact GUI by placing a few buttons for <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#switch-to-a-different-module" rel="noopener nofollow ugc">switching between modules</a>.</p>
</blockquote>
</aside>
<p>Yes that’s exactly what I need ! But the thing is that I didn’t manage to add a button at the same level as the DICOM Database button so that it stays there when I switch.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a8e8aa512bc694b6850c238b5fa44f5fb6bdfb0.png" alt="image" data-base62-sha1="3MVO6zrdlMsL31h9emhi4xfQ9yw" width="305" height="55"><br>
I want to add a button there, can be through Python to avoid building a higher level window with Qt…</p>

---

## Post #30 by @lassoan (2021-04-26 20:17 UTC)

<p>By view layout I mean four-up, red slice only, dicom browser, etc.</p>
<p>You don’t need the favorite toolbar, you can hide it and instead add buttons for switching between modules. If you prefer to have a tool bat then you can of course do that, too. Just make sure to set the Favorites toolbar visibility to True.</p>

---

## Post #31 by @Vincebisca (2021-04-27 07:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You don’t need the favorite toolbar, you can hide it and instead add buttons for switching between modules. If you prefer to have a tool bat then you can of course do that, too. Just make sure to set the Favorites toolbar visibility to True.</p>
</blockquote>
</aside>
<p>Yeah if I can avoid the favorite toolbar I will, the thing is I didn’t find the syntaxe to add a button at the level I showed (which doesn’t appear in Qt Designer) or the right way to right the line for the Favorites Toolbar set visible either. I am not familiar with the “old” way to create GUI elements but I feel it’s what I need for this particular button</p>

---

## Post #32 by @lassoan (2021-04-27 17:07 UTC)

<p>You can only save space if you remove all the toolbars (then the toolbar area disappears). List of toolbars are specified here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerSimpleWorkflows/blob/master/QuickSegment/QuickSegment.py#L133-L136" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSimpleWorkflows/blob/master/QuickSegment/QuickSegment.py#L133-L136" target="_blank" rel="noopener">lassoan/SlicerSimpleWorkflows/blob/master/QuickSegment/QuickSegment.py#L133-L136</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="133" style="counter-reset: li-counter 132 ;">
<li>keepToolbars = [</li>
<li>  slicer.util.findChild(slicer.util.mainWindow(), 'MainToolBar'),</li>
<li>  slicer.util.findChild(slicer.util.mainWindow(), 'ViewToolBar'),</li>
<li>  slicer.util.findChild(slicer.util.mainWindow(), 'ViewersToolBar')]</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>So, either add <code>ModuleToolBar</code> there or remove all the other toolbars and create a row of buttons using Qt designer.</p>

---

## Post #33 by @rbumm (2021-04-27 20:33 UTC)

<p>Hello.</p>
<p>I´d recommend to go<br>
 → Developer Tools → Extension Wizard</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3952cdb1bf5f87993a709cee8c6b20c6daca377f.png" alt="image" data-base62-sha1="8b6CwYB6TMbv13vtp2ECLk1A0X5" width="495" height="421"></p>
<p>This helpful tool will put up a development system within slicer and comes with a working templet of a simple extension with it´s own GUI.</p>
<p>You can edit the python code in a text editor of your coice and play around with the GUI after editing it in the in the QT designer.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed17b99f42b0eee1158b390a53def85c30a0c8d3.png" alt="image" data-base62-sha1="xPpZsoUaApjNLA2eVZw6wsp8wLx" width="637" height="89"></p>
<p>Reload the extension from within slider and directly test your changes, All basic and necessary functions for a slicer extension are included. But you will need to write some lines of code …</p>
<p>Best regards</p>
<p>Rudolf</p>

---

## Post #34 by @Vincebisca (2021-04-28 07:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="32" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>So, either add <code>ModuleToolBar</code> there or remove all the other toolbars and create a row of buttons using Qt designer.</p>
</blockquote>
</aside>
<p>Okay ModuleToolBar is indeed what I tried to find, at least I got the Favorites so it’s quite good enough for now. The next step would be to set my Slicelet to be the only module in here I guess but that’s not urgent to do. Thanks a lot anyway !!</p>

---

## Post #35 by @Vincebisca (2021-04-28 07:38 UTC)

<p>Thank you very much Rudolf ! Indeed I have seen this tool and tried it a few times ! I found more convenient to use the QuickSegment Slicelet mentionned by <a class="mention" href="/u/lassoan">@lassoan</a> tho because it was closer to what I want to achieve.</p>

---

## Post #36 by @seanchoi0519 (2021-06-25 09:45 UTC)

<p>Hey Vincebisca,</p>
<p>I’m a student who is also working on creating a custom application with a custom workflow and starting to learn everything. If it’s okay with you, could I ask you some questions before I get started? I feel a bit overwhelmed with learning everything at the moment and would love to receive some advice/help from you.</p>
<p>Many thanks</p>
<p>Sean</p>

---

## Post #37 by @Vincebisca (2021-06-25 12:38 UTC)

<p>Hello !</p>
<p>I’ve been there so I know <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"> if I can help you I will do so gladly ! I think that reading this thread might help you a great deal ! I am not a developper and all I am capable of doing is fiddling around with the extension template and slicelet template that are available. Anyway feel free to ask !</p>
<p>Vincent</p>

---

## Post #38 by @seanchoi0519 (2021-06-25 12:49 UTC)

<p>Hey Vincent! Thanks so much</p>
<p>Actually I’m not a professional developer either which is why I’m struggling too LOL<br>
Anyway, similar to your case, I’m also looking to optimize my workflow, as my project only requires specific modules (ALPACA, Model-to-model distance, and ShapePopulationViewer, and Models). So my goal would be to recreate a custom GUI using only these features.</p>
<p>How did  you go about this? Did you primarily use QtDesigner? Did you create a custom slicelet/guidelet? It’d be great if you could give an overview, and maybe if it’s okay with you, share your template with maybe a few screenshots as I have no idea where to start.</p>
<p>Thank you so much</p>

---

## Post #39 by @Vincebisca (2021-06-25 12:55 UTC)

<p>Ok just to be sure: do you want to use the modules as they are? Like you only need to show the modules in the upper toolbar? In that case you could just modify the “favorite modules” on your Slicer.</p>
<p>If you want to merge the use and create your own module that take advantage internaly of the modules you mentioned, then you should check the answer above :</p>
<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve created a small example project of a slicelet (3D Slicer running with a simplified GUI) that you might find useful. It is only for loading an image, segmenting it, and saving the result. See more details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Slicelets - Slicer Wiki </a></p>
</blockquote>
</aside>
<p>This will give you a template of Slicelet for 3D Slicer, from there you can activate the Editor Mode of 3D Slicer and modify directly the QtDesigner Interface created in the Slicelet (basically a blank one, but it’s created and linked) and you can edit the code to slowly add what you need. Using this template you have at least something that is already functionnal in terms of base settings !</p>

---

## Post #40 by @seanchoi0519 (2021-06-25 12:57 UTC)

<p>Thanks Vincent! How can I run this slicelet on my mac? I’ve downloaded the .zip file on github but not sure where to go from there. And yes I’m looking to merge the user and create my own model.</p>
<p>Btw can I ask what platform you use? MacOS or window?<br>
As I’m having trouble launching QtDesigner on my mac.</p>

---

## Post #41 by @Vincebisca (2021-06-25 13:02 UTC)

<p>Unfortunately I work on Windows and thus have not the slightest idea of how to do that on a Mac, maybe somebody will help you better on that. Anyways to launch the slicelet you should have some kind of application in the folder of the Slicelet. Then you can look something like “how to include a custom extension on 3D slicer” and you’ll find a tutorial to manually add and external offline module to your slicer. You’ll then have access to it from the main 3D Slicer application. This is very practical since you can switch between your version and the real one</p>

---

## Post #42 by @seanchoi0519 (2021-06-25 13:09 UTC)

<p>Sorry could you explain the what you mean by the “kind of application in the folder of the Slicelet”? Specifically with regards to the SlicerSimpleWorkflow project. What do I do with the .zip file once I’ve downloaded it? Any screenshot to explain the process would be great!</p>
<p>And just curious - “You’ll then have access to it from the main 3D Slicer application” - But isn’t the whole point of the slicelet to avoid having to use the full 3D slicer application?</p>
<p>And okay I have a windows laptop so I may try that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Did you have to download from <a href="https://www.qt.io/offline-installers" class="inline-onebox" rel="noopener nofollow ugc">Download Offline Installers</a> to use QtDesigner?</p>
<p>Sorry for the newbie questions</p>

---

## Post #43 by @Vincebisca (2021-06-25 13:19 UTC)

<p>Well, if I remember well (which might not be the case) once the zip downloaded, unzip it and store it somewhere on your computer (a place that you can find). Then if you open the folder you created, you should have an application called like QuickSegment or something, on windows it’s a .exe. This should allow you to open the Slicelet.</p>
<p>Yes you’re right, that’s the point of Slicelets, but being able to switch to the main application while you are in the development phase is still useful !</p>
<p>I don’t remember downloading anything to use QtDesigner but I might have forgotten</p>

---

## Post #44 by @seanchoi0519 (2021-06-25 13:27 UTC)

<p>Yeah I’m having no luck in locating the .exe file <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c84420d6bc2a84d973353bee8d9ce32d79f395b.png" data-download-href="/uploads/short-url/6lOmX1OViKOC67rn6JnknZke1GX.png?dl=1" title="capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c84420d6bc2a84d973353bee8d9ce32d79f395b.png" alt="capture2" data-base62-sha1="6lOmX1OViKOC67rn6JnknZke1GX" width="690" height="128" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture2</span><span class="informations">1174×218 9.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f14a489139cfb7b47a6ef16334cbd4d2e19d9b.png" data-download-href="/uploads/short-url/iY3Zfv99KWWftpwM6Lj2H8heZ5h.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f14a489139cfb7b47a6ef16334cbd4d2e19d9b.png" alt="Capture" data-base62-sha1="iY3Zfv99KWWftpwM6Lj2H8heZ5h" width="690" height="180" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1153×301 15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #45 by @Vincebisca (2021-06-25 13:31 UTC)

<p>Hmmm I noticed in my case it’s at the same place as the Slicer.exe (on the main folder of Slicer)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f71b07ef586eebbbc9b0789cbb9037b6cee172df.png" data-download-href="/uploads/short-url/zfZQCWVDBipqvkuAky5XTezuvrp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f71b07ef586eebbbc9b0789cbb9037b6cee172df.png" alt="image" data-base62-sha1="zfZQCWVDBipqvkuAky5XTezuvrp" width="690" height="354" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×359 18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Gotta say I don’t know how to help there, I did that once a few months  ago so it’s hard to remember exactly ^^</p>

---

## Post #46 by @seanchoi0519 (2021-06-25 13:35 UTC)

<p>Oh okay thanks anyway!<br>
Just curious where you obtained the “NumChainTest1.exe” file then? Is that the custom slicelet you created yourself?</p>
<p>Vincent if you’re okay with it I would love to set up a zoom meeting with you to learn from you. I’m more than happy to compensate you for your time. It is for my university research project. Let me know!</p>

---

## Post #47 by @ruili (2023-12-05 13:13 UTC)

<p>Hello! Do you have any idea why we can no longer see the photos you and Vinvebisca posted in this discussion? All the images are blank from my side. I will be very interested in seeing the screenshot as I am facing the same problem.</p>

---

## Post #48 by @pieper (2023-12-05 13:22 UTC)

<aside class="quote no-group" data-username="ruili" data-post="47" data-topic="17208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> ruili:</div>
<blockquote>
<p>All the images are blank from my side</p>
</blockquote>
</aside>
<p>I’ve noticed this too on some posts.  Probably it’s an issue with discourse.  <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/lassoan">@lassoan</a> let’s discuss at the dev call.  Probably we need to file an issue with discourse.</p>

---

## Post #49 by @VirOrange (2024-10-12 01:27 UTC)

<p>it’s very nice of you all to provide so many useful ideas!</p>

---
