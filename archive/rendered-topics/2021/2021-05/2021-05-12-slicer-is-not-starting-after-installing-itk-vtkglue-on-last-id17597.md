---
topic_id: 17597
title: "Slicer Is Not Starting After Installing Itk Vtkglue On Last"
date: 2021-05-12
url: https://discourse.slicer.org/t/17597
---

# Slicer is not starting after installing itk-vtkglue on Last Stable Release

**Topic ID**: 17597
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/slicer-is-not-starting-after-installing-itk-vtkglue-on-last-stable-release/17597

---

## Post #1 by @Guglielmo_Baccani (2021-05-12 14:37 UTC)

<p>Dear slicer,</p>
<p>I would like to install “itk-vtkglue” to convert a vtk image to an itk image. My ultimate goal would be to use the MultiScaleHessianBasedMeasureImageFilter class to detect plate-like shapes inside my python scripted module (this class is not present in SimpleITK).<br>
However after installing the package from the Python Interactor with the command</p>
<pre><code class="lang-auto">slicer.util.pip_install("itk-vtkglue")</code></pre>
<p>it is no longer possible to restart slicer and the following error is reported from the terminal:</p>
<pre><code class="lang-auto">error: [/home/user/Slicer-4.11.20210226-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem</code></pre>
<p>How can I install the software correctly?<br>
Is there any way to use itk directly from a scripted module or do I need to use a CLI module as described in this post?</p><aside class="quote" data-post="2" data-topic="5468">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-use-itk-functionalities-inside-scripted-modules/5468/2">How to use ITK functionalities inside scripted modules</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can use ITK proper in CLI modules or C++ loadable modules, while in scripted modules you can use ITK via its more user-friendly <a href="http://www.simpleitk.org/" rel="noopener nofollow ugc">SimpleITK</a> interface.
  </blockquote>
</aside>


---

## Post #2 by @lassoan (2021-05-12 19:59 UTC)

<p>I would expect itk-vtkglue to be very fragile if it uses C++ interface (it can only be compatible with a specific combination of ITK and VTK versions). If it uses Python interface then you actually not need itk-vtkglue at all, because you can easily convert both ITK and VTK images to/from numpy arrays yourself. You just need to take care of passing the metadata (origin, spacing, and axis directions), because only ITK can store it in the numpy array, VTK does not support this yet.</p>

---

## Post #3 by @mau_igna_06 (2022-04-23 14:08 UTC)

<p>I would like itk-vtkGlue to work I have an itk filter I want to use on a Slicer’s volume.<br>
After doing <code>volume.GetImageData()</code> I don’t know how to do the convertion to itk image.<br>
I searched for a example doing the numpy interfaced convertion but I couldn’t find any.<br>
Could you help?</p>

---

## Post #4 by @lassoan (2022-04-24 05:48 UTC)

<p>The safest way to use ITK filters on VTK image data is to use filters in <a href="https://github.com/Slicer/Slicer/tree/master/Libs/vtkITK">vtkITK library</a>. If a filter is missing you can add it there.</p>
<p>If you want to work in Python then you may use SimpleITK and pass images to/from Slicer using <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/sitkUtils.py">sitkUtils</a>. For other data types and other Python ITK wrappings (such as ITKPython) you probably need to exchange data via files (Slicer writes to file, ITK reads it, processes it, writes to file, Slicer reads from file).</p>

---
