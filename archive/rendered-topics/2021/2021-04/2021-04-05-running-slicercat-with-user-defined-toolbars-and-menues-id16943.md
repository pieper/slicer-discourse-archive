# Running SlicerCAT with user defined toolbars and menues

**Topic ID**: 16943
**Date**: 2021-04-05
**URL**: https://discourse.slicer.org/t/running-slicercat-with-user-defined-toolbars-and-menues/16943

---

## Post #1 by @oren (2021-04-05 05:28 UTC)

<p>Hi<br>
I am trying to define the Slicer toolbar (‘Favorites’ toolbar)<br>
I have edit ‘CMakeLists.txt’:<br>
set(Slicer_DEFAULT_FAVORITE_MODULES “Crop Volume, SegmentEditor”)</p>
<p>as described in</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://blog.kitware.com/wp-content/uploads/2017/04/xExternalFavicon.png.pagespeed.ic.BxFzGTIFZT.png" class="site-icon" width="16" height="16">
      <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" target="_blank" rel="noopener nofollow ugc" title="03:11PM - 18 October 2019">Kitware Blog – 18 Oct 19</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:130/83;"><img src="https://blog.kitware.com/wp-content/uploads/2019/10/SlicerCATSplash2.png" class="thumbnail" width="130" height="83"></div>

<h3><a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" target="_blank" rel="noopener nofollow ugc">SlicerCAT: Creating custom applications based on 3D Slicer - Kitware Blog</a></h3>

<p>This blog presents a framework for making custom applications based on 3D Slicer. What is 3D Slicer? 3D Slicer is a software platform for the ... Read More</p>

  <p><span class="label1">Est. reading time: 6 minutes</span>
    </p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I have build the project using visual studio  (Windows)<br>
and run the executable:<br>
&lt;Slicer_BUILD&gt;/Slicer-build/Slicer.exe</p>
<p>but the SlicerCAT was just the same as before<br>
‘Favorites’ tool bar just did not changed - It has all the default modules !</p>
<p>what am I missing ?<br>
It looks like changing  ‘CMakeLists.txt’ and qCustomAppNameAppMainWindow.cxx has no affect on the display of the SlicerCAT</p>
<p>thanks<br>
Oren</p>

---

## Post #2 by @Sam_Horvath (2021-04-05 12:30 UTC)

<p>Hi:</p>
<p>Did you reconfigure and re-run the top level build after changing the CMakeLists file?</p>
<p>Also, if you have already run the application before changing it, it may have stored the favorite modules in the settings, and used the user settings instead of the default modules list.  From the window menu, got to Edit-&gt;Application Settings-&gt;Modules, and click the ‘restore defaults’ button at the bottom of the window.</p>

---

## Post #3 by @oren (2021-04-05 17:29 UTC)

<p>I think you have solved my problem<br>
It looks like SlicerCAT have read the setting from the old user setting file</p>
<p>thank you !</p>

---
