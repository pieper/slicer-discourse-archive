# Click and connect two separated segments of a vessel segmentation

**Topic ID**: 33161
**Date**: 2023-12-01
**URL**: https://discourse.slicer.org/t/click-and-connect-two-separated-segments-of-a-vessel-segmentation/33161

---

## Post #1 by @ruili (2023-12-01 13:07 UTC)

<p>Hi all,</p>
<p>I am working on a project where I generate the segmentation of blood vessels in the brain using some other software and compute their centrelines using the SlicerVMTK extension. However, a common problem with the segmentation is that the same vessel may get segmented into multiple disconnected segments. I cannot come up with a very good way to connect these fragmented segments together automatically, so I wanted to implement a module/extension on 3D slicer where the user can click two segments and then run some algorithms to connect these two segments or just connect their centerlines. I am labelling disconnected islands in a segmentation using different integers first, so that when I load it into 3D slicer, different islands will have different colors. I want to ask how I can make it interactive so that the user can toggle-select two islands? I want some effect that is similar to selecting the endpoints/fiducial points in 3D slicer.</p>
<p>Thank you very much!</p>

---

## Post #2 by @chir.set (2023-12-01 13:51 UTC)

<aside class="quote no-group" data-username="ruili" data-post="1" data-topic="33161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> ruili:</div>
<blockquote>
<p>some other software</p>
</blockquote>
</aside>
<p>I assume you are referring to arteries of the circle of Willis from CT scans.</p>
<p>Have you tried segmenting the same structures with Slicer? Usually ‘Grow from seeds’ effect of the ‘Segment editor’ gives nice results. You may ease the process by extracting the brain first (TotalSegmentator, Swiss skull stripper, HD-BET…), apply ‘Split volume’ or ‘Mask volume’ and increase the resolution of the resulting volume with ‘Resample scalar volume’. ‘Grow from seeds’ should then play nicely. The quality of the master input is always of great import.</p>
<p>If you are working with MRI, ‘Grow from seeds’ still performs well.</p>
<p>I’m suggesting here a simple pre-processing to avoid a complex post-processing.</p>

---

## Post #3 by @ruili (2023-12-01 14:00 UTC)

<p>Thank you for the suggestions. I am actually working with MR angiography data and we are looking at very small brain vessels, which is a much more challenging task than segmenting the large arteries. We are using a deep learning model for segmentation, which does a good job, but the same vessel still often get segmented into disconnected parts. This is also due to the poor signal from the small vessels themselves. Thus, we are hoping to add some user-correction in the post-processing stage.</p>

---

## Post #4 by @mikebind (2023-12-01 16:55 UTC)

<p>You can create a python module which creates a markups node and observes it.  When the user places a point of that node by clicking, you can identify the closest vessel segment, and use this point placement as your “selection” mechanism. When two different segments have been selected by this method, you could connect the closest ends of the centerlines of those two to create a new, combined centerline.   To add a simple segmentation connecting the two ends, you could use the Draw Tube effect from SegmentEditorExtraEffects extension to make a cylindrical linkage.  The radius for that cylinder could be based on the vessel radius at the two ends from VMTK. Then you could merge the original two vessel segments and the linkage segment to make one unified vessel segment.  The old segments could be discarded or hidden and the selection markups control points could be discarded, and you would be ready to select more segments to join.</p>

---

## Post #5 by @ruili (2023-12-05 11:06 UTC)

<p>Thank you very much for your kind suggestions Mike! What you described is exactly what I need. However, although I am proficient in python, I am very new to coding with 3D Slicer, and I have just started learning how to create a new module and the concepts of the widget and logic functions. I wonder if you mind giving me some hint on how to achieve those steps in your suggestion and possibly some code example? For instance, should I code a logic function that creates a markup node? How to “observe” it? How can I make a function to wait a user to select two segments and then execute something else?</p>
<p>Sorry if these questions are two basic or broad, but I am really struggling to get my head around how the module code works and to find the right functions from slicer to call, so I will really appreciate some help with this.</p>

---

## Post #6 by @mikebind (2023-12-05 23:07 UTC)

<p>The details of how to achieve this are too big for a quick response here, but I’ll try to get you pointed in some helpful directions and you can always come back and ask for help when you are getting stuck.</p>
<p>At a high level, the idea behind dividing the widget and logic into separate classes is that the widget manages all interaction with GUI elements, while the logic carries out all the functionality (the working-with and modifying data stuff) you want your module to have.  The major benefit of this division is that outside code (i.e. modules that other people write) can use the functionality you provide without having to instantiate your widget GUI.  Maybe this will be an easy to understand concept for you since it sounds like you have a solid programming background, but this was something I struggled with at first (deciding how functions should be structured).  The good news is that, as you are learning, nothing bad happens if you put functionality in the widget class that properly belongs in the logic class.  And, as you get used to it, it will steadily become clearer what belongs where.</p>
<p>Some recommendations, steps to take, and resources:</p>
<ul>
<li>Enable <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#developer-mode">developer mode</a> in your Slicer settings (Edit menu → Application Settings → Developer → Enable developer mode checkbox).  This will show some helpful extra buttons on all python scripted modules which will be very helpful while developing your module. The “Reload” button reloads the module from the source code, which is very helpful when you are actively making and testing changes (usually there’s no need to restart Slicer to test changes).  The “Edit” button opens the module source code in your default editor. This can be very useful for looking at other modules’ code as well as your own.  The “Edit UI” button launches Qt Designer and allows you to edit the GUI elements of your module in a reasonably intuitive way.</li>
<li>I highly recommend using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html">Extension Wizard</a> module and starting from there with your first module.  The template code there is a simple working module which allows thresholding an input volume.  As a minimal first example, I would recommend trying to add a new button to this module and make it do something like add one to all voxel values of the input.  In order to do this, you’ll need to look closely at the template code and try to mimic what is done for the existing Apply button. You’ll need to create the button in Qt Designer, connect the button click signal to a callback in your widget’s setup function, write the callback function to gather any needed inputs, pass those inputs to a logic function which does the actual work of taking the input volume node, getting the voxel values, adding one, and either updating the original input volume or creating a new output volume with the new values. This should be a very educational exercise, and by the time you’ve accomplished it, you’ll have a better sense of how Slicer modules typically work and pass around data.</li>
<li>Next, start thinking about what inputs your functions will need.  You will need a selector to choose the segmentation node which contains all your vessel segments, and you will also need the ability to place markups points.  For the first, in Qt Designer, you want to add a qMRMLNodeComboBox and set the nodeTypes it allows you to select to be “vtkMRMLSegmentationNode”.  For the second, a handy widget is qSlicerMarkupsPlaceWidget.  Lastly, you probably want a button which you click once you’ve identified the two segments you want to link and which triggers carrying out the actual linkage.</li>
<li>That’s probably all you really need on the GUI side.  When you click the button, the selected segmentation node and markups node should be passed to a logic function which is supposed to carry out all of the work. You can start off with a stub function there which just lets you know it has been called by printing something out (print statements or logging statements show up in the python interactor in Slicer as well as in the Error Log window (Ctrl-0 or the X in the lower right of the status bar)).</li>
<li>The rest of the work is actually implementing what you want to happen, given the inputs.  The good news is that this is just pure python coding <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Here are the pieces I see that you will need:
<ul>
<li>A function finding the closest segment centerline endpoint to a markups point. I’m not sure what format your centerline data is in after your initial processing, but at minimum, you will need some way of keeping track of which segment goes with which centerline.  To find the closest centerline endpoint to your first clicked point, I would just make a list of all the centerline endpoints and calculate the distance to the clicked markups point, and find the one with the minimum distance.  For any markups node, you can get control point positions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-to-markups-point-list-properties">like this</a>.</li>
<li>A function to take two centerlines and link them at the ends you specify.  You can access the coordinates of each centerline point as in the previous section; so the only real complication is getting them in the right order.  All of the points from one of the centerlines come first, and then all of the points from the other centerline, either in the original order or reversed, depending on which end is supposed to be connected.</li>
<li>A function to take two endpoints which are to be newly connected and which creates a new  segment connecting them.  If you want to base the radius of this segment on reported radii from VMTK, you also need a way of extracting that data (maybe look <a href="https://github.com/vmtk/vmtk/issues/356">here</a>, that isn’t something I have done myself before).  With a radius and endpoints, you can draw a cylindrical tube using the “Draw tube” segment editor effect. The new segment can then be merged with the two existing segments which are to be joined using logical operators “Add” segmentation effect.  Some helpful code examples for logical operations can be found in <a href="https://discourse.slicer.org/t/how-to-programmatically-use-logical-operator-add-function-from-segment-editor/16581">this forum thread</a>.</li>
<li>Then you would need to do whatever bookkeeping is needed (deleting the old versions of the merged segments and centerlines and updating with the new merged version)</li>
</ul>
</li>
<li>Very helpful code snippets for all kinds of things in Slicer can be found in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>, this is one of the first places you should look when trying to figure out how to do something in Slicer using python.</li>
<li>There is also a LOT of information available in the Slicer <a href="https://slicer.readthedocs.io/en/latest/developer_guide/index.html">Developer Guide</a> documentation.  It may be helpful to peruse areas of that site, though there’s far too much there to read and digest all in one go.</li>
</ul>

---

## Post #7 by @ruili (2023-12-06 00:31 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="6" data-topic="33161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>With a radius and endpoints, you can draw a cylindrical tube using the “Draw tube” segment editor effect.</p>
</blockquote>
</aside>
<p>Thank you so much for such a detailed reply! This is really really helpful, and I will go through these in details. I already played around with the “Draw Tube” effect today, but one thing I noticed is that inside the effect I always have to define new control points to draw the tube instead of just connecting two endpoints that are pre-defined. I now think that it might be easiest for me to firstly extract the endpoints of each segments and just let the user select which two endpoints to join by drawing a tube. Do you have any suggestion on how I may use existing fudicial/control points as input to the “Draw Tube” effect? Or does this mean I will need to implement it in my custom module?</p>

---

## Post #8 by @mikebind (2023-12-06 00:59 UTC)

<p>You can use segment editor effects from python.  There are several good examples <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-segment-editor-effects-from-script-qmrmlsegmenteditorwidget">linked from the script repository</a>, though none of those is for Draw Tube (because Draw Tube is from SegmentEditorExtraEffects extension, not core Slicer). However, you can see an example of how to use Draw tube from python in one of its self test functions here <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorDrawTube/SegmentEditorDrawTube.py#L48">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorDrawTube/SegmentEditorDrawTube.py#L48</a></p>

---
