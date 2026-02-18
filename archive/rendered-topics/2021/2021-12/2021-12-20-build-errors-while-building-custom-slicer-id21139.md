# Build Errors while building custom Slicer

**Topic ID**: 21139
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/build-errors-while-building-custom-slicer/21139

---

## Post #1 by @Karthik (2021-12-20 04:19 UTC)

<p>OS: Ubuntu 20.04<br>
Hi. I have built Slicer (v4.11.20210226) before successfully.<br>
Now, I want to build a custom Slicer with change in logo, style, etc. So, I followed the instructions given in <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a>  to customize the application. Then, I followed the general Slicer build instructions given in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#pre-requisites" class="inline-onebox" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a></p>
<p>At the end of the build process, I am getting the following errors. Hence, I am unable to locate or run the executable file.</p>
<p>– Configuring incomplete, errors occurred!<br>
See also “/home/karthik/Custom-Slicer/CTFFR-rel/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
See also “/home/karthik/Custom-Slicer/CTFFR-rel/Slicer-build/CMakeFiles/CMakeError.log”.<br>
make[2]: *** [slicersources-build/CMakeFiles/Slicer.dir/build.make:127: slicersources-build/Slicer-prefix/src/Slicer-stamp/Slicer-configure] Error 1<br>
make[1]: *** [CMakeFiles/Makefile2:173: slicersources-build/CMakeFiles/Slicer.dir/all] Error 2<br>
make: *** [Makefile:84: all] Error 2</p>
<p>I am attaching the log files for reference.</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1_Dfnv7A_TIDaNpqqzlSoFKOX6RpOgmau/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1_Dfnv7A_TIDaNpqqzlSoFKOX6RpOgmau/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh4.googleusercontent.com/ajQ2MQbgDh7h6z6b7IkVDy1U92JKtp1ZbEW21Vk39_pYxclG1zDjvyEq2_i2LdphUgw=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1_Dfnv7A_TIDaNpqqzlSoFKOX6RpOgmau/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">CMakeError.txt</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1F8xST7uk7PdGCQZHp4EdgucNlVcyou2d/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1F8xST7uk7PdGCQZHp4EdgucNlVcyou2d/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh3.googleusercontent.com/vxsge2sSPi2v0rAjnb5HfuY03Ul049E5pvPlxcuoufgZzQlb6UPhlgExPXZDuxv6X6E=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1F8xST7uk7PdGCQZHp4EdgucNlVcyou2d/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">CMakeOutput.txt</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please help me understand what these errors mean. My custom template directory is named CTFFR and the build directory is named CTFFR-rel.</p>
<p>Also, please give suggestions/instructions to build custom 3D Slicer.</p>

---

## Post #2 by @Sam_Horvath (2021-12-20 14:01 UTC)

<p>This line:</p>
<pre><code class="lang-auto">c++: error: unrecognized command line option ‘-features=no%anachronisms’
</code></pre>
<p>indicates that there is some issue with your c++ compiler.  Have you built cmake based applications on this machine before?</p>

---

## Post #3 by @Karthik (2021-12-21 01:21 UTC)

<p>Yes. I have built 3D Slicer v4.11.20210226 and v4.13. It has been built successfully. The executable works. I have also built extensions on it and packaged them. They all work. But, when I followed the custom template to create a custom 3D Slicer with different logo and style, I am getting these errors.</p>
<p>Are the instructions given here <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#pre-requisites" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a> correct? Are there any other references?</p>

---
