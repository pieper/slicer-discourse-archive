# Control DICOMUtils.loadPatientByUID

**Topic ID**: 10425
**Date**: 2020-02-25
**URL**: https://discourse.slicer.org/t/control-dicomutils-loadpatientbyuid/10425

---

## Post #1 by @Alex_Vergara (2020-02-25 13:31 UTC)

<p>Currently when loading patients in a test environment I do as:</p>
<pre data-code-wrap="python"><code class="lang-python">def setupDICOM():
    '''
    Setup a complex environment based on the loaded dicom files
    '''
    logger = logging.getLogger('Dosimetry4D.testbuilder')
    dicomValues = DicomValues()

    try:
        openDICOMDatabase()
    except:
        raise

    try:
        ok = DICOMUtils.loadPatientByName(dicomValues.patientName)
    except:
        logger.error('Could not load dicom files from database')
        raise Error('Unable to load series from database')

    shNode = vtkmrmlutils.getSubjectHierarchyNode()
    studyID = vtkmrmlutils.getStudyIDs()[0]
    itemIDs = vtkmrmlutils.getAllFolderChildren(studyID)

    return itemIDs
</code></pre>
<p>However, this fails since I got the following:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f3bea5cd3a4187ca3c5290c8fd01ac30b5d727.png" data-download-href="/uploads/short-url/7Q80fzUU1x06VjeWiT92X4ADVB5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f3bea5cd3a4187ca3c5290c8fd01ac30b5d727_2_689x348.png" alt="image" data-base62-sha1="7Q80fzUU1x06VjeWiT92X4ADVB5" width="689" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f3bea5cd3a4187ca3c5290c8fd01ac30b5d727_2_689x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f3bea5cd3a4187ca3c5290c8fd01ac30b5d727_2_1033x522.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f3bea5cd3a4187ca3c5290c8fd01ac30b5d727.png 2x" data-dominant-color="4A6A7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1194×603 73.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This can be solved graphically by doing<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30653639e75b9a7ca7e7f391f47a1d89724b7399.png" data-download-href="/uploads/short-url/6U7LmsG5JTibAOBXWd6aSam4csx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30653639e75b9a7ca7e7f391f47a1d89724b7399_2_689x353.png" alt="image" data-base62-sha1="6U7LmsG5JTibAOBXWd6aSam4csx" width="689" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30653639e75b9a7ca7e7f391f47a1d89724b7399_2_689x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30653639e75b9a7ca7e7f391f47a1d89724b7399_2_1033x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30653639e75b9a7ca7e7f391f47a1d89724b7399.png 2x" data-dominant-color="4A697E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1207×619 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then check the missing volumes.</p>
<p>My problem is how to do this from python in the test environment? I need to load ONLY the Scalar Volumes and ALL of them.</p>

---

## Post #2 by @lassoan (2020-02-25 16:24 UTC)

<p>You need to use lower-level functions of DICOMUtils, which allow specifying which plugins to use. You can specify list of plugin class names in <code>getLoadablesFromFileLists</code>.</p>

---

## Post #3 by @Alex_Vergara (2020-02-27 10:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10425">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>getLoadablesFromFileLists</p>
</blockquote>
</aside>
<p>I have solved with</p>
<pre data-code-wrap="python"><code class="lang-python">from DICOMScalarVolumePlugin import DICOMScalarVolumePluginClass

def setupDICOM():
    '''
    Setup a complex environment based on the loaded dicom files
    '''
    logger = logging.getLogger('Dosimetry4D.testbuilder')
    dicomValues = DicomValues()

    try:
        openDICOMDatabase()
    except:
        raise

    try:
        slicer.modules.dicomPlugins
    except:
        slicer.modules.dicomPlugins = {}

    if slicer.modules.dicomPlugins:
        oldPluginList = slicer.modules.dicomPlugins
        slicer.modules.dicomPlugins = {}
    else:
        oldPluginList = {}

    slicer.modules.dicomPlugins['DICOMScalarVolumePlugin'] = DICOMScalarVolumePluginClass

    try:
        _ = DICOMUtils.loadPatientByName(dicomValues.patientName)
    except:
        logger.error('Could not load dicom files from database')
        raise Error('Unable to load series from database')

    studyID = vtkmrmlutils.getStudyIDs()[0]
    itemIDs = vtkmrmlutils.getAllFolderChildren(studyID)

    slicer.modules.dicomPlugins = oldPluginList

    return itemIDs
</code></pre>

---
