# Writing Algorithms for a loadable Module

**Topic ID**: 13812
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/writing-algorithms-for-a-loadable-module/13812

---

## Post #1 by @Anish_Basnet (2020-10-02 08:58 UTC)

<p>Hello Everyone,<br>
I have read somewhere in the Internet that I can implement any algorithms inside the vtkSlicerMY_MODULE_NAMELogic.cxx file. Is it true? If so, how do I access it from the qSlicerMY_MODULE_NAMEWidget.cxx file? Any help would be appreciated!</p>
<p>Best regards,<br>
Anish</p>

---

## Post #2 by @cpinter (2020-10-02 09:03 UTC)

<p>Certainly, you can do that.</p>
<p>Please see the corresponding section in the developer’s manual:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Loadable_Modules" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Loadable_Modules" target="_blank" rel="noopener">Documentation/Nightly/Developers/Modules - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I’d strongly suggest looking at examples, basically any Slicer module does this:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable" target="_blank" rel="noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/324362?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable" target="_blank" rel="noopener">Slicer/Slicer</a></h3>

<p>Multi-platform, free open source software for visualization and image computing. - Slicer/Slicer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
