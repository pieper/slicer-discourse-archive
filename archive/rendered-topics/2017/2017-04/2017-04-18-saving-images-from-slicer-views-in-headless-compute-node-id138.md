# Saving images from slicer views in headless compute node

**Topic ID**: 138
**Date**: 2017-04-18
**URL**: https://discourse.slicer.org/t/saving-images-from-slicer-views-in-headless-compute-node/138

---

## Post #1 by @mike_i (2017-04-18 02:14 UTC)

<p>Hi Slicer community,</p>
<p>I am trying to perform what I thought would be a straightforward task of loading a study into slicer and saving a few images from each of the viewing panes (red, yellow, green) into PNG or jpg files. My script is based off example code here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_a_series_of_images_from_a_Slice_View" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_a_series_of_images_from_a_Slice_View</a></p>
<p>The script works when I call it from the Python Interactor window of an already launched Slicer application (in windows) using execfile, but it fails when I call it as a python script on my linux box as a headless compute node. Specifically, PNG images are saved to disk, but they are blank, and all pixels are black. I have no idea why the code behaves differently when called from the python interactor in the gui vs the --python-script parameter from the linux command line. Does anyone have any thoughts or pointers about this? I’ve spent all day on this and am probably missing something obvious. Thank you in advance.</p>
<p>Mike</p>
<pre><code>def saveThumbnails (steps, path, plane):
    pattern='%s.png'
    layoutName = 'Green'
    if plane==0:
        layoutName='Red'
    if plane==1:
        layoutName='Yellow'

    widget = slicer.app.layoutManager().sliceWidget(layoutName)
    view = widget.sliceView()
    logic = widget.sliceLogic()
    bounds = [0,]*6
    logic.GetSliceBounds(bounds)
    print(bounds)

    for step in range(steps):
        offset = bounds[4] + (step+1)/(1.*(steps+1)) * (bounds[5]-bounds[4])
        print (step+1)/(1.*(steps+1))
        logic.SetSliceOffset(offset)
        view.forceRender()
        image = qt.QPixmap.grabWidget(view).toImage()
        image.save((path+pattern) % (layoutName+str(step)))

path = '\path\to\output\folder'
steps = 2
INPUT_FILE = "\path\to\source\file\test.nrrd"

newNodeTuple = slicer.util.loadVolume(INPUT_FILE, returnNode=True)
saveThumbnails(2, path, 0)</code></pre>

---

## Post #2 by @lassoan (2017-04-18 04:11 UTC)

<p>See solution here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_Slicer_on_a_headless_compute_node.3F">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_Slicer_on_a_headless_compute_node.3F</a></p>

---

## Post #3 by @mike_i (2017-04-18 04:28 UTC)

<p>Thanks Andras for your reply. Perhaps I can do a better job of explaining my problem. I am already running slicer in a headless node using xpra. Other operations work fine, but when I execute the script containing the code above it saves PNG files, but the PNG files are blank. When I execute the same script using a standard GUI through the python interactor the PNG files are not blank and contain images of the volume. Why is it that this code generates blank PNG files when run from a headless node, and how can it be fixed?</p>
<p>Also, I’ve tried calling slicer.app.processEvents() and slicer.util.delayDisplay(“wait”, 1000) just in case the images were blank because an update was pending. No luck.</p>
<p>Thanks again in advance!</p>

---

## Post #4 by @lassoan (2017-04-18 05:35 UTC)

<p>There are a couple of ways to capture viewers. Try these:</p>
<pre><code>import ScreenCapture
l=ScreenCapture.ScreenCaptureLogic()
l.captureImageFromView(l.viewFromNode(slicer.util.getNode('vtkMRMLSliceNodeRed')), 'c:/tmp/red.png')</code></pre>

---

## Post #5 by @mike_i (2017-04-18 16:28 UTC)

<p>Thanks for the suggestion Andras,</p>
<p>Unfortunately, it didn’t work. The output image file is blank, as you can see from this image below. This is the same as it has been for several other methods I have tried. <a href="https://drive.google.com/open?id=0Bxp6kJSQ1E77ZDJaeTR3WGY1QmM" rel="nofollow noopener">https://drive.google.com/open?id=0Bxp6kJSQ1E77ZDJaeTR3WGY1QmM</a></p>
<p>I took a screencapture of the entire slicer window to see what was going on using:</p>
<pre><code>image = qt.QPixmap.grabWidget(slicer.util.mainWindow()).toImage()
image.save(filename)
</code></pre>
<p>And this is what is shown: <a href="https://drive.google.com/open?id=0Bxp6kJSQ1E77YnJEMml4SEZtb1U" rel="nofollow noopener">https://drive.google.com/open?id=0Bxp6kJSQ1E77YnJEMml4SEZtb1U</a></p>
<p>As you can see the individual panes are empty, even though the volume is loaded. I know that the volume was successfully loaded because I received command line output confirming the load:</p>
<pre><code>Loaded volume from file: /home/ubuntu/Documents/test.nrrd. Dimensions: 512x512x48. Number of components: 1. Pixel type: short.
"Volume" Reader has successfully read the file "test.nrrd" "[0.31s]"
</code></pre>
<p>I’ve tried about 4 or 5 different ways to capture the slice panels now, and they all show the same thing - a blank image, and the main window screen capture shows that the individual panels are blank. I am beginning to wonder if the problem is the way that things are displayed with a headness node. On my windows machine (with a monitor) as soon as the volume is loaded it displays in the red, green, and yellow slice panes. But on the headless linux machine (without a monitor) it appears to not be rendering, at least based on the main window screen capture. I am using the xpra dummy graphics monitor that Steve Pieper described in this post (<a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2015/017317.html" rel="nofollow noopener">http://massmail.spl.harvard.edu/public-archives/slicer-devel/2015/017317.html</a>), which is a great solution from running headless but maybe this breaks the regular graphics display. Or maybe the common screenshot functions rely on a working gui to function properly. Answering questions like this requires deep knowledge of the application architecture and is beyond me. Does anybody have any thoughts about this?</p>
<p>My task seems relatively simple, but is proving difficult. I need to get a few slice shots as thumbnail images of a volume using the command line from a headless linux server.</p>
<p>Thank you in advance.</p>

---

## Post #6 by @pieper (2017-04-18 17:01 UTC)

<p>Hi Mike - What happens if you connect to the xpra dummy server (e.g. by running x11vnc)?  If you’re not sure how to do that I can send you the command lines.</p>
<p>-Steve</p>

---

## Post #7 by @mike_i (2017-04-18 17:17 UTC)

<p>Here is my command line call:<br>
<code>env DISPLAY=:11 ../../Slicer-4.6.2-linux-amd64/Slicer --no-splash --python-script ./slicer_makethumbs.py</code></p>
<p>This is after starting xpra on :11. Is this what you are referring to?<br>
Mike</p>

---

## Post #8 by @pieper (2017-04-18 17:37 UTC)

<p>right - once you’ve done that, you can run a command like:</p>
<p>x11vnc -forever -usepw -display :11</p>
<p>You’ll need to get and install x11vnc[1], which isn’t too hard.  You can<br>
then use any vnc client to connect to it.   I typically use noVNC[2], but<br>
any vnc client should work.</p>
<p>[1] <a href="https://en.wikipedia.org/wiki/X11vnc">https://en.wikipedia.org/wiki/X11vnc</a></p>
<p>[2] <a href="https://github.com/novnc/noVNC">https://github.com/novnc/noVNC</a></p>

---

## Post #9 by @pieper (2017-04-19 15:27 UTC)

<p>(Edited the previous post to use display :11 rather than :1 to match Mike’s use case)</p>

---

## Post #10 by @mike_i (2017-04-19 19:29 UTC)

<p>Thanks very much for the advice. Unfortunately, my project requires the linux machine to run automatically without a VNC connection to it. However, you did help me find a solution using a different method through an old post you made:</p>
<p><a href="https://sourceforge.net/p/teem/mailman/message/27766556/" class="onebox" target="_blank" rel="nofollow noopener">https://sourceforge.net/p/teem/mailman/message/27766556/</a></p>
<p>I think that approach is going to work. So thanks to you (and your older self from 6 years ago) I think the problem is solved! I’ll keep you updated on my progress.</p>
<p>Mike</p>

---

## Post #11 by @pieper (2017-04-19 20:35 UTC)

<aside class="quote no-group" data-username="mike_i" data-post="10" data-topic="138">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/65b543/48.png" class="avatar"> mike_i:</div>
<blockquote>
<p>So thanks to you (and your older self from 6 years ago</p>
</blockquote>
</aside>
<p>Fair enough!</p>
<p>If it turns out you need to solve the other problem, for example extracting rendered 3D views from a headless Slicer I checked and a docker image that exposes a vnc connection for Xdummy works for me (you don’t need to connect to it, just running the server seems to be enough).</p>

---
