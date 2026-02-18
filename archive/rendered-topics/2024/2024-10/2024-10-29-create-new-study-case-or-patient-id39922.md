# Create new study case or patient

**Topic ID**: 39922
**Date**: 2024-10-29
**URL**: https://discourse.slicer.org/t/create-new-study-case-or-patient/39922

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-10-29 14:57 UTC)

<p>Hi to everyone, a very quick question:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6efae29274a2dfeca9d3f777088f328c2e514ff.png" data-download-href="/uploads/short-url/wWXkw1jO1vVYPuhhtw9socWDrQj.png?dl=1" title="Captura de pantalla 2024-10-29 155540" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6efae29274a2dfeca9d3f777088f328c2e514ff.png" alt="Captura de pantalla 2024-10-29 155540" data-base62-sha1="wWXkw1jO1vVYPuhhtw9socWDrQj" width="459" height="197"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-10-29 155540</span><span class="informations">459×197 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone how to put the name (for example P40_val) to the patient symbol using python? It also works to me change the notebook icon name using python.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2024-10-29 15:32 UTC)

<p>These icons are specified in this plugin. I don’t think you can easily customize that without creating a new plugin</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/SubjectHierarchyPlugins/qSlicerSubjectHierarchyDICOMPlugin.cxx#L87-L88">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/SubjectHierarchyPlugins/qSlicerSubjectHierarchyDICOMPlugin.cxx#L87-L88" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/SubjectHierarchyPlugins/qSlicerSubjectHierarchyDICOMPlugin.cxx#L87-L88" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/SubjectHierarchyPlugins/qSlicerSubjectHierarchyDICOMPlugin.cxx#L87-L88</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="87" style="counter-reset: li-counter 86 ;">
          <li>this-&gt;PatientIcon = QIcon(":Icons/Patient.png");</li>
          <li>this-&gt;StudyIcon = QIcon(":Icons/Study.png");</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @SANTIAGO_PENDON_MING (2024-10-30 07:44 UTC)

<p>I think I did not explain me well. I don’t want to modify the icons. I want to change the ‘‘node’’ (in fact I think this is not a usual node) name that we see in the previous picture.</p>
<p>For example:</p>
<p>· P40_val → P123_new</p>
<p>· No study description (20240828) → First Study (30/10/2024)</p>
<p>The function I trying to find is the node.SetName(‘NewName’) that usual nodes have.</p>
<p>Thanks for the answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @cpinter (2024-10-30 09:41 UTC)

<p>Subject hierarchy items are not nodes, they are managed differently.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---
