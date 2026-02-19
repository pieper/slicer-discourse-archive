---
topic_id: 782
title: "2D Views In Slicer Extremely Slow On Windows"
date: 2017-07-28
url: https://discourse.slicer.org/t/782
---

# 2D Views in Slicer extremely slow on Windows

**Topic ID**: 782
**Date**: 2017-07-28
**URL**: https://discourse.slicer.org/t/2d-views-in-slicer-extremely-slow-on-windows/782

---

## Post #1 by @mschwier (2017-07-28 22:52 UTC)

<p>Dear all,<br>
I have my own Win 10 64 bit release build of Slicer (4.7.0-2017-07-27) running and I notice some extreme lags when interacting with the 2D views. This is particularly noticeable when I load a multi-volume (but also already with the sample images).<br>
Interactions are for example: navigation through slices or frames (multi-volume); changing brightness/contrast with mouse.</p>
<p>The problem also gets worse over time until an update of the viewer takes more than a second and makes working virtually impossible. I can easily trigger this slow down e.g. by resizing the application window a lot (constantly resizing by just grabbing a corner and dragging it around the desktop for a while).</p>
<p>CPU power and RAM shouldn’t be the problem, CPU is a i7Quad@2.3GHZ and RAM is 16GB. Overall RAM usage of the whole system never exceeded 8GB and CPU is chilling at &lt;15% during any of my interactions with Slicer.<br>
Another observation: The 3D Volume Rendering runs super smooth all the time, but that goes through the GPU. However, even with CPU raycasting the time to render the HQ volume is still faster than changing the brightness in the 2D view.</p>
<p>Does anyone have similar experiences or an idea what could be the problem?</p>

---

## Post #2 by @lassoan (2017-07-28 23:35 UTC)

<p>I’ve been using Slicer on Windows for many years and I haven’t seen such a slowdown. Based on the symptoms it seems like memory leak or fragmentation, or accumulation of event observations.</p>
<p>Are you sure you it’s a Release build (not Debug)? Is performance better with the binaries that you download from <a href="http://slicer.org">slicer.org</a>?<br>
Have you installed any extensions?<br>
Do you see any change in memory usage of Slicer?<br>
Is the slowdown only happening with multi-volume?<br>
Can you reproduce it with any of simple 3D sample data sets?<br>
What compiler do you use?<br>
Which Qt version do you use?<br>
Can you record a screen capture from the point you start Slicer until you see the extreme slowdown? (you can use screen recorder in PowerPoint)</p>

---

## Post #3 by @lassoan (2017-07-30 01:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it seems like memory leak or fragmentation</p>
</blockquote>
</aside>
<p>Most likely this memory leak/fragmentation happens in the graphics driver (whenever you change your window size, the old OpenGL window is deleted and a new one is created). Try the followings:</p>
<ul>
<li>Update your graphics card driver</li>
<li>Adjust your graphics card settings: for example, enabling “threaded optimization” often causes various errors in the driver or in applications</li>
<li>Replace your graphics card</li>
</ul>

---

## Post #4 by @mschwier (2017-07-31 15:53 UTC)

<p>I can reproduce the same problem with the binary version from <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a>.<br>
I created a video showing the problem (<a href="https://www.dropbox.com/s/rr6pn5744c6ue0q/SlicerSlowDown.mp4?dl=0" rel="nofollow noopener">here</a>). To force the slowdown I “wildly” move the mouse to change the brightness/contrast for a while. Afterwards you can see how the 2D view updates are much slower, while the 3D view still works smoothly.</p>
<p>When I change the contrast/brightness by mouse drag in the 2D view the memory consumption of Slicer indeed constantly increases, so I agree that it seems to be a memory leak problem. But I am not sure if it is the graphics card driver, since the 3D view still works fine. However, I have two graphics cards, an on-board and a dedicated Nvidia, could it be that the on-board is used for the 2D view while the dedicated runs the 3D view in the same application?</p>

---

## Post #5 by @mschwier (2017-07-31 15:57 UTC)

<p>I also tried various setting changes (incl. deactivating “threaded optimization”), so far without success. Graphics card drivers seem all up to date but I will investigate more.</p>

---

## Post #6 by @lassoan (2017-08-01 03:40 UTC)

<p>An application always uses one graphics card for rendering all windows. On desktop computers typically all applications use the dedicated GPU (unless you remove the graphics card or disable it in UEFI/BIOS), on laptops you can sometimes choose which one to use.</p>
<p>I couldn’t reproduce the issue on two computers.</p>
<p>Can you reproduce the problem without enabling volume rendering?<br>
Can you reproduce it by changing W/L programmatically, using this script?</p>
<pre><code>v=getNode('CTChest')
dn=v.GetDisplayNode()
for i in range(1000):
   dn.SetWindowLevel(dn.GetWindow(),-dn.GetLevel())
   slicer.app.processEvents()
</code></pre>
<p>Can you reproduce the problem using latest nightly version of Slicer?<br>
Can you reproduce the problem on another computer?<br>
Can you reproduce the problem if you remove/disable the dedicated GPU?<br>
What Nvidia GPU do you use? What is the NVidia driver version? How much RAM do you have?</p>

---

## Post #7 by @mschwier (2017-08-01 17:19 UTC)

<p>Hey Andras, thank you for your help so far.</p>
<p>I can reproduce the problem without enabling volume rendering (also tried to use a layout with only one 2d view, same happens, but it takes longer until it is really slow, which makes sense, since I have 3 render areas less)</p>
<p>I can also reproduce the problem with the script you send.<br>
I can also reproduce it on the latest nightly build.<br>
The Win 10 computer of a colleague does not show this problem.<br>
I started the application with the integrated graphics card and with the NVidia (using the right-click context menu). Both have the problem. However, since it is a laptop, I am not sure if the NVidia always partly goes through the integrated card!?<br>
My system is a Dell Precision M3800 notebook with 16GB RAM, with an Intel HD Graphics 4600 integrated and a NVIDIA Quadro K1100M with 2GB dedicated RAM. I just installed the latest NVidia driver (385.08). I also updated the driver for the Intel HD Graphics.</p>
<p>I also think everything indicates to some trouble with my system/drivers, I am just wondering since I have worked on this computer for a few years and never had problems with other applications, also image processing/visualization and OpenGL-based …</p>
<p>Btw. I also tried an old Slicer 32 Bit (4.3.0). Same problem, even crashes pretty quickly after changing the W/L a bit.</p>

---

## Post #8 by @lassoan (2017-08-02 03:33 UTC)

<p>Could you please try to disable the Quadro card in the device manager and restart your computer to see if the problem is still there?</p>
<p>You may check out drivers and BIOS updates on Dell support website. You can also search on the web if other had similar problem with similar laptops and see if any of the proposed solution works.</p>

---

## Post #9 by @mschwier (2017-08-02 21:15 UTC)

<p>With the Quadro disabled the problem still remains.</p>
<p>I already installed the newest drives and BIOS updates as well. However, I found this, not sure if it is a lead:<br>
<a href="https://software.intel.com/en-us/forums/graphics-driver-bug-reporting/topic/610376" class="onebox" target="_blank" rel="nofollow noopener">https://software.intel.com/en-us/forums/graphics-driver-bug-reporting/topic/610376</a></p>
<p>So the guy there even wrote a small program to show his problem under DirectX, and Intel claims they fixed it (in a new driver version, which I have). So I tried this program: Running it with the Internal Intel Graphics chip works. Running it with the Quadro fails (also showing constantly rising memory). Adding context-Flush() to the loop also fixes the problem when running on the Quadro. So this could be a bug in the Quadro driver (I’ll see if I can post a bug report to NVidia). However, for Slicer the problem appears on the Internal and the Quadro. So I am wondering, if maybe this bug is not fixed for OpenGL!? Does smth similar happen in Slicers 2d Viewer OpenGL code as in the DirectX sample code i.e. many creations and releases of buffers/textures?</p>

---

## Post #10 by @lassoan (2017-08-03 02:25 UTC)

<aside class="quote no-group" data-username="mschwier" data-post="9" data-topic="782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschwier/48/394_2.png" class="avatar"> mschwier:</div>
<blockquote>
<p>many creations and releases of buffers/textures?</p>
</blockquote>
</aside>
<p>Yes, I think so. Slices are rendered using textures and each time the image changes the texture is updated.</p>
<p>Considering history of problems with this laptop model (<a href="https://www.amazon.com/Dell-Precision-M3800-Touchscreen-Notebook/product-reviews/B00HVW3JLW/ref=cm_cr_getr_d_paging_btm_2?ie=UTF8&amp;filterByStar=one_star&amp;reviewerType=all_reviews&amp;pageNumber=2#reviews-filter-bar">2.6 stars rating on Amazon</a>), it’s low current value (around $1000), and that the issue might come up with other applications as well, I would recommend to upgrade to a new laptop instead of spending too much time with investigation. If you cannot get a new device then you may find workarounds, such as save scene and restart when it’s starting to get too slow.</p>

---

## Post #11 by @mschwier (2017-08-04 14:05 UTC)

<p>I’ll see if I can live with the workaround for now <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=5" title=":confused:" class="emoji" alt=":confused:"> That notebook actually served me very well for development and image processing (e.g. MeVisLab) for a couple of years, never had issues like this …</p>

---

## Post #12 by @lassoan (2017-08-05 03:41 UTC)

<p>I am sorry I could not be more helpful. We were probably just unlucky that how Slicer used the graphics card exposed errors.</p>

---

## Post #13 by @AJ_ZHU (2017-08-07 13:38 UTC)

<p>Hi all,<br>
I just guess you guys need check the units there while you are using CT<br>
data since you need reset the units to “um”.<br>
I did get the same issue while I record some slice-view movies. while after<br>
reset mm to “um”, then it is fixed.</p>
<p>PS:<br>
Set up custom units in slice view ruler</p>
<p>For microscopy or micro-CT images you may want to switch unit to micrometer<br>
instead of the default mm. To do that, 1. change the unit in Application<br>
settings / Units and 2. update ruler display settings using the script<br>
below (it can be copied to your Application startup script):</p>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
for sliceViewName in lm.sliceViewNames():
  sliceView = lm.sliceWidget(sliceViewName).sliceView()
  displayableManagerCollection = vtk.vtkCollection()
  sliceView.getDisplayableManagers(displayableManagerCollection)
  for dmIndex in xrange(displayableManagerCollection.GetNumberOfItems()):
    displayableManager = displayableManagerCollection.GetItemAsObject(dmIndex)
    if not displayableManager.IsA("vtkMRMLRulerDisplayableManager"):
      continue
    displayableManager.RemoveAllRulerScalePresets()
    displayableManager.AddRulerScalePreset(   0.001, 5, 2, "nm", 1000.0)
    displayableManager.AddRulerScalePreset(   0.010, 5, 2, "nm", 1000.0)
    displayableManager.AddRulerScalePreset(   0.100, 5, 2, "nm", 1000.0)
    displayableManager.AddRulerScalePreset(   0.500, 5, 1, "nm", 1000.0)
    displayableManager.AddRulerScalePreset(   1.0,   5, 2, "um",    1.0)
    displayableManager.AddRulerScalePreset(   5.0,   5, 1, "um",    1.0)
    displayableManager.AddRulerScalePreset(  10.0,   5, 2, "um",    1.0)
    displayableManager.AddRulerScalePreset(  50.0,   5, 1, "um",    1.0)
    displayableManager.AddRulerScalePreset( 100.0,   5, 2, "um",    1.0)
    displayableManager.AddRulerScalePreset( 500.0,   5, 1, "um",    1.0)
    displayableManager.AddRulerScalePreset(1000.0,   5, 2, "mm",    0.001)
</code></pre>
<p>Aijun</p>

---

## Post #14 by @mschwier (2017-08-10 14:21 UTC)

<p>Thanks Aijun,</p>
<p>unfortunately this didn’t change anything in my case. I agree with Andras that it’s most likely an unlucky combination of how Slicer uses OpenGL and the driver not handling this well.</p>
<p><span class="mention">@Andras</span>: Can you hint me to the OpenGL code in Slicer that handles the 2D view? I’m curious if I would be able to create a minimal example (like the Directd3D code I tried)  that reproduces the error (if I find the time)!?</p>

---

## Post #15 by @pieper (2017-08-10 14:38 UTC)

<p><a class="mention" href="/u/mschwier">@mschwier</a> what happens if you try running VTK examples?  Slicer uses standard VTK for all the rendering.</p>

---

## Post #16 by @lassoan (2017-08-15 04:22 UTC)

<p>Slicer will switch to the latest VTK and its new rendering backend in a couple of weeks. There is a good chance that your problem will go away, because OpenGL will be used very differently.</p>

---

## Post #17 by @mschwier (2017-08-15 05:35 UTC)

<p><span class="mention">@Andras</span>: Thanks for the info. That would be great. I’ll let you know how it turns out.<br>
<span class="mention">@Steve</span>: Thanks for the tip, I’ll still try the VTK example idea, as soon as I find some time.</p>

---
