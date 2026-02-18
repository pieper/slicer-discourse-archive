# Extracting a 2d oblique plane using itk/vtk via python, (as shown in slicer view)

**Topic ID**: 11250
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/extracting-a-2d-oblique-plane-using-itk-vtk-via-python-as-shown-in-slicer-view/11250

---

## Post #1 by @helenawill95 (2020-04-22 13:38 UTC)

<p>Hello, I am currently using Slicer to manually find a slice- but I need to automate this. I was wondering if you could share any information how slicer displays the coronal view.</p>
<p>My volume has a direction matrix [0.9713990611037072, -0.2374528670848932, 0.0, 0.2374528670848932, 0.9713990611037072, 0.0, 0.0, 0.0,1.0], so when I slice the numpy array, I do not want to simply use [:,:,i] as I then do not get the coronal view, and due to the direction matrix i can never get the 2d slice I want (it just looks like a 2d line due to the direction matrix).</p>
<p>However, in slicer it has been converted to LPS, and there I have a slice at 44mm I want to extract automatically, is there any information how slicer converts the volume into LPS coordinate system so then I can hopefully simply extract the plane via [:,i,:].</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2020-04-22 13:57 UTC)

<p>See solution in script repository:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array</a></p>

---

## Post #3 by @helenawill95 (2020-04-22 14:32 UTC)

<p>thank you, and if i wanted to recreate the view in slicer in python alone (without running slicer in the first place) i.e. the 2d plane of a volume using the direction matrix how would it best be done? I am trying to use itk/vtk but struggling to get the correct plane that slicer shows.</p>

---

## Post #4 by @lassoan (2020-04-22 14:49 UTC)

<p>You need to use <em>some</em> Python environment anyway. Slicer’s Python environment is just one of the many that you can setup/use. You can run your code directly from command line (using <code>--python-code</code> or <code>--python-script</code> argument) and might be able to hide the application GUI (using <code>--no-main-window</code>). If you want to use features that requires a rendering context then creating an application window may be required, but there are many solutions to prevent users from seeing a window (for example, run Slicer in a docker container; or hide the main window immediately after it is created).</p>

---

## Post #5 by @helenawill95 (2020-04-22 19:38 UTC)

<p>Thank you for the response. I only wanted to extract a plane from my new angled coordinate system automatically for a plane detection pipeline, I am not sure if Slicer is necessary, or whether to just use ITK/VTK to perform the final reslice as it needs to be relatively quick. I mainly need to access a specific oblique plane, based on  SetDirection() and the mid point/origin of the plane.</p>

---

## Post #6 by @lassoan (2020-04-22 20:19 UTC)

<p>The optimal solution depends on many factors. What does your system do? Is it an image-based navigation system? Where do the images and the real-time plane position/orientation come from?</p>
<p>Slicer is very well suited for implementing complete real-time processing and visualization workflows, navigation systems, etc. so there is a high chance that most of what is needed is already available and you just need to plug in your plane detection algorithm and you get a complete, full-featured system. We can also receive real-time data streams (medical imaging systems, position trackers, various sensors - see <a href="http://www.slicerigt.org">www.slicerigt.org</a>) and display results on desktop, augmented reality, or virtual reality (see <a href="http://www.slicervr.org">www.slicervr.org</a>). Slicer also provides associated device calibration, patient registration, real-time intra-operative segmentation tools, etc. Of course Slicer can do much more, I’m just guessing what could be potentially interesting for you. Let us know what you need and then we can give more specific information.</p>

---
