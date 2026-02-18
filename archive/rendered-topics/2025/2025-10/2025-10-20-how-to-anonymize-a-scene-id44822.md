# How to anonymize a scene

**Topic ID**: 44822
**Date**: 2025-10-20
**URL**: https://discourse.slicer.org/t/how-to-anonymize-a-scene/44822

---

## Post #1 by @lassoan (2025-10-20 15:55 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> started a discussion in the <a href="https://github.com/Slicer/Slicer/issues/8798">Slicer issue tracker on github</a>, but it is worth giving more visibility to this to the community:</p>
<blockquote>
<p>Please consider this workflow:</p>
<ul>
<li>load a DICOM volume with patient information</li>
<li>save the scene, as MRB or not</li>
<li>close the scene</li>
<li>close Slicer</li>
<li>start Slicer</li>
<li>load the scene</li>
<li>select the patient in the Data module</li>
<li>show Subject Hierarchy information</li>
</ul>
<p>Although there are no DICOM files in the saved scene but an NRRD file as scalar volume, DICOM tags are still in the <code>*.mrml </code>file, with <code>PatientName</code> and <code>PatientBirthDate</code> in particular.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a73739d558ffd78cce0a01d7eaf0a369d3b00d3d.png" data-download-href="/uploads/short-url/nRg3D0xQxWnuBGoZ7tj5V5gJRYF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a73739d558ffd78cce0a01d7eaf0a369d3b00d3d_2_345x500.png" alt="image" data-base62-sha1="nRg3D0xQxWnuBGoZ7tj5V5gJRYF" width="345" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a73739d558ffd78cce0a01d7eaf0a369d3b00d3d_2_345x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a73739d558ffd78cce0a01d7eaf0a369d3b00d3d_2_517x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a73739d558ffd78cce0a01d7eaf0a369d3b00d3d_2_690x1000.png 2x" data-dominant-color="373A3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">739×1071 81.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the patient is removed from the DICOM database, the result is the same.</p>
<p>The problem: when an MRB file is shared, there is patient data leakage. Actually, that’s how I came across this finding, with the last shared MRB file on the Discourse forum. For this reason, I won’t link that post here but can do it in private messaging on request.</p>
<p>The scene file should probably not store values of DICOM tags, at least not containing the above mentioned ones. There’s nothing DICOM related in a saved scene.</p>
<p>Of course, a user may fully anonymise his series before sharing. It just gets cumbersome and most users won’t be doing that.</p>
<p>Thank you for considering.</p>
</blockquote>
<p>Response from <a class="mention" href="/u/pieper">@pieper</a>:</p>
<blockquote>
<p>Since the MRML scene is extensible, we can’t assure that it is free of PHI, but I agree that this is a case where it would be reasonable to assume that no PHI is included.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> it looks like this can in via the subject hierarchy.  Do you have ideas about how this could be automatically removed in this kind of scenario?</p>
</blockquote>

---

## Post #2 by @lassoan (2025-10-20 16:04 UTC)

<p>For many workflows it is essential to be able to go back to the DICOM database - for fetching additional metadata or be able to export results to DICOM. In research workflows, usually the data of the patient cohort is anonymized before you load any data into Slicer. In clinical workflows, usually all patient information preserved in the data set to make sure that you work on the correct patient and to keep the connection to the patient records.</p>
<p>There is a niche but important use case: you get data of an individual patient and then you want to share with people who are not authorized to see PHI.</p>
<ul>
<li>Slicer supports a very simple, blunt tool for this: save the scene and then load the NRRD file (or other data files). This cuts all ties to the original DICOM, so it is hard to find you way back to the original data if you need it. PHI may still remain in the data via burnt-in annotations (e.g., patient name in the corner of an image in a secondary capture), recognizable face in a 3D scan, etc.</li>
<li>There are several DICOM anonymization tools that can do deidentification in a much more sophisticated way (cleans out PHI more reliably while preserving more data and offering controlled way to go map the data to the original source), which can be used outside Slicer.</li>
<li>I expect that in the not too distant future (within 1-2 years) there will be Slicer extensions for more convenient DICOM data deidentification, because machine learning is very data-hungry and Slicer will need to offer tools for making training data set building more convenient. These tools should work not just on cohorts but on individual patient data sets, too. They would not start from a Slicer scene (because it is not possible to anonymize data once it is read into the scene and accessed by arbitrary modules), but would work by processing the data before is loaded into the Slicer scene.</li>
</ul>

---

## Post #3 by @chir.set (2025-10-20 16:42 UTC)

<p>I came up with this brute force solution:</p>
<pre><code class="lang-auto"># ----------------------------------------------------------------------------
def anonymiseSubjectHierarchyFrom(startItemId):
  shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
  startItemChildrenIds = vtk.vtkIdList()
  shNode.GetItemChildren(startItemId, startItemChildrenIds)

  for i in range(startItemChildrenIds.GetNumberOfIds()):
    startItemNextChildId = startItemChildrenIds.GetId(i)
    if (shNode.GetItemLevel(startItemNextChildId) != "Patient"):
      continue
    if (shNode.HasItemAttribute(startItemNextChildId, "DICOM.PatientName")):
      shNode.SetItemAttribute(startItemNextChildId, "DICOM.PatientName", "Anonymous")
    if (shNode.HasItemAttribute(startItemNextChildId, "DICOM.PatientBirthDate")):
      shNode.SetItemAttribute(startItemNextChildId, "DICOM.PatientBirthDate", "11111111")
    
    anonymiseSubjectHierarchyFrom(startItemNextChildId)

# ----------------------------------------------------------------------------
def anonymiseScene():
  shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
  sceneItemId = shNode.GetSceneItemID()
  anonymiseSubjectHierarchyFrom(sceneItemId)
</code></pre>
<p>Two suggestions:</p>
<ol>
<li>Add an option to anonymise the subject hierarchy in the <code>Save dialog</code>.</li>
<li>Add an option in the <code>DICOM module</code> to load a series as anonymous.</li>
</ol>

---

## Post #4 by @pieper (2025-10-20 16:44 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="44822">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Add an option in the <code>DICOM module</code> to load a series as anonymous</p>
</blockquote>
</aside>
<p>I like this option.  It’s clean and sounds more broadly useful.</p>

---

## Post #5 by @lassoan (2025-10-20 17:28 UTC)

<p>DICOM loading plugins require the data to be in the DICOM database. Therefore, it is not possible to anonymize during DICOM <em>loading</em> without major rework or the DICOM plugins or switching to a temporary database.</p>
<p>It would be much simpler and cleaner to anonymize during <em>import</em> (could be activated in the “Import DICOM files” window) and/or during <em>export</em> (could be activated in “Export to files” window). It is also necessary to be able to do batch processing - anonymizing all data in a folder. All these require integration of an open-source DICOM anonymizer tool with a simple GUI for configuring and running the processing.</p>

---

## Post #6 by @pieper (2025-10-20 17:59 UTC)

<p>Anonymize on import also makes sense.  But what I took <a class="mention" href="/u/chir.set">@chir.set</a> to be suggesting would be to give the plugins the option of not putting PHI into the mrml scene when loading.  Often it’s hard for a generic deidentifier to know what the tags mean, while the plugins are specific to the type of data and probably have a better chance of knowing which contain PHI and generating deidentified variants.</p>

---

## Post #7 by @chir.set (2025-10-20 18:09 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="44822">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>not putting PHI into the mrml scene</p>
</blockquote>
</aside>
<p>Yes, that’s what I meant. The DICOM database can have patient information since it is not a shared object.</p>

---

## Post #8 by @lassoan (2025-10-21 12:50 UTC)

<blockquote>
<p>Anonymize on import also makes sense. But what I took <a class="mention" href="/u/chir.set">@chir.set</a> to be suggesting would be to give the plugins the option of not putting PHI into the mrml scene when loading.</p>
</blockquote>
<p>I agree that this would work for some workflows. However, it would break some modules.</p>
<p>The problem: There are a number of modules in several extensions (for example in SlicerHeart, SlicerCIP, probably also in SlicerRT, QuantitativeReporting and others) that would break if the DICOM instance UIDs were changed or skipped when loading the DICOM files. The instance UIDs are used for looking up additional DICOM fields in the database that are needed for certain operations. The DICOM plugin developers don’t know what additional metadata various modules in other extension will need.</p>
<p>Proposed solution: If data was anonymized during DICOM import or export (and not during loading) then there would be always valid database entries associated with the loaded data. Therefore, all the modules would still work well, while there was no PHI in the scene or in the exported files. These solutions also have the advantage that DICOM plugin developers would not need to know how to do DICOM anonymization properly, which is actually a very complex topic.</p>
<p>A relatively easy immediate solution (until more convenient solution is offered within Slicer) could be to anonymize the DICOM files before loading into Slicer. There are several tools already, for example:</p>
<ul>
<li><a href="https://github.com/pydicom/deid" class="inline-onebox">GitHub - pydicom/deid: best effort anonymization for medical images using python</a></li>
<li><a href="https://github.com/KitwareMedical/dicom-anonymizer" class="inline-onebox">GitHub - KitwareMedical/dicom-anonymizer: Tool to anonymize DICOM files according to the DICOM standard</a></li>
<li><a href="https://github.com/RSNA/anonymizer" class="inline-onebox">GitHub - RSNA/anonymizer: RSNA DICOM Anonymizer</a></li>
<li><a href="https://github.com/blairconrad/dicognito" class="inline-onebox">GitHub - blairconrad/dicognito: A library and command line tool for anonymizing DICOM files</a></li>
<li><a href="https://github.com/UAMS-DBMI/PosdaTools" class="inline-onebox">GitHub - UAMS-DBMI/PosdaTools</a></li>
<li><a href="https://github.com/bebbi/dicom-curate" class="inline-onebox">GitHub - bebbi/dicom-curate: Organize and de-identify DICOM part 10 files per a configuration.</a></li>
<li><a href="https://github.com/microsoft/Tools-for-Health-Data-Anonymization/blob/master/docs/DICOM-anonymization.md" class="inline-onebox">Tools-for-Health-Data-Anonymization/docs/DICOM-anonymization.md at master · microsoft/Tools-for-Health-Data-Anonymization · GitHub</a></li>
<li><a href="https://github.com/valab-certh/meddisc">https://github.com/valab-certh/meddisc</a></li>
<li><a href="https://mircwiki.rsna.org/index.php?title=MIRC_CTP" class="inline-onebox">MIRC CTP - MircWiki</a></li>
</ul>
<p>Their feature set varies. Some of them have GUI. Most people would find that one of these work for them with little or no change in anonymization parameters.</p>

---

## Post #9 by @chir.set (2025-10-21 19:27 UTC)

<p>I have included the functions above in an online <a href="https://gitlab.com/chir-set/Tools7/-/blob/9d7307c2d6a60ac45dd7916331f63e1414986ad4/ManyThingsToolBar/ManyThingsToolBar.py#L721" rel="noopener nofollow ugc">module</a> for easy use in the GUI, until a built-in solution appears.</p>

---
