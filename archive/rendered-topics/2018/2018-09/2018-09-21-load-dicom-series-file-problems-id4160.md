# Load Dicom series file problems

**Topic ID**: 4160
**Date**: 2018-09-21
**URL**: https://discourse.slicer.org/t/load-dicom-series-file-problems/4160

---

## Post #1 by @jiang_luo (2018-09-21 09:45 UTC)

<p>Operating system:win7<br>
Slicer version: 4.9<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,  I had created the  python script that load the series of the DICOM files. the script is follow:</p>
<p>def LoadDicomFile(path=None,NodeName=None):<br>
filelist=os.listdir(path)<br>
progress = slicer.util.createProgressDialog(parent=None, value=0, maximum=len(filelist))<br>
plugin=DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()<br>
from DICOMLib import DICOMLoadable<br>
loadable=DICOMLoadable()<br>
step=0<br>
for filename in filelist:<br>
loadable.files.append(path + ‘/’ + filename)<br>
labletext = ‘\n LoadDicomFile %s …’ % filename<br>
progress.labelText = labletext<br>
slicer.app.processEvents()<br>
progress.setValue(step)<br>
step += 1<br>
slicer.app.processEvents()<br>
try:<br>
flag = plugin.load(loadable)<br>
except:<br>
print ‘except load false …’<br>
progress.close()<br>
del plugin<br>
del loadable</p>
<p>LoadDicomFile(‘f:/data/’)<br>
but the MPR seem is not good look this… the script have any problems???</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cc7ca57d7d0d76e8a8cfdf9b286be9f43e05baa.jpeg" data-download-href="/uploads/short-url/8FGHe0815sC2LiIkTN4VtQJMN1o.jpeg?dl=1" title="%E6%97%A0%E6%A0%87%E9%A2%98" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3cc7ca57d7d0d76e8a8cfdf9b286be9f43e05baa_2_690x204.jpeg" alt="%E6%97%A0%E6%A0%87%E9%A2%98" data-base62-sha1="8FGHe0815sC2LiIkTN4VtQJMN1o" width="690" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3cc7ca57d7d0d76e8a8cfdf9b286be9f43e05baa_2_690x204.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cc7ca57d7d0d76e8a8cfdf9b286be9f43e05baa.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cc7ca57d7d0d76e8a8cfdf9b286be9f43e05baa.jpeg 2x" data-dominant-color="5D5D5D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E6%97%A0%E6%A0%87%E9%A2%98</span><span class="informations">786×233 46.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-09-21 11:43 UTC)

<p>You get the file list by calling <code>filelist=os.listdir(path)</code>, which returns the files in some random order (how they are ordered in the file system). See this topic about how to do it correctly:</p>
<aside class="quote quote-modified" data-post="1" data-topic="3257">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ben_george/48/2992_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/load-dicom-series-using-python/3257">Load DICOM series using python</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi 
I am trying to create a python script that can import a DICOM image series from a folder, however I can’t seem to find a way to make this work. 
I can load a single DICOM file (in my case an RTSTRUCT) using this code: 
contour_fn = 'contours.dcm'
	
	# Add filename to list for DICOM-RT module
	contour_vtkFileList = vtk.vtkStringArray()
	contour_vtkFileList.InsertNextValue(slicer.util.toVTKString(contour_fn))
	
	# Examine files
	contour_loadablesCollection = vtk.vtkCollection()
	slicer.modules…
  </blockquote>
</aside>


---

## Post #3 by @jiang_luo (2018-09-21 12:41 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="4160">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You get the file list by calling <code>filelist=os.listdir(path)</code> , which returns the files in some random order (how they are ordered in the file system). See this topic about how to do it correctly:</p>
<p>![|20x20](upload://oBmm92EHQmoqH4ENK3ajlRs6cpw.png <a href="https://discourse.slicer.org/t/load-dicom-series-using-python/3257">Load DICOM series using python</a> <a href="/c/support">Support</a></p>
</blockquote>
</aside>
<p>Thanks for your quickly help, i will try the Load the ordered files…</p>

---

## Post #4 by @Davide_Cester (2020-04-19 18:54 UTC)

<p>Hi! I’m experimenting with controlling 3DSlicer from Jupyter Notebook and I found the initial script useful… I want to share the Python3 version of it since others may end up here:</p>
<pre><code>import os
from glob import glob
from DICOMLib import DICOMLoadable
import DICOMScalarVolumePlugin

def load_dicom_folder(path):
    plugin = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
    loadable = DICOMLoadable()
    for file_path in sorted(glob(os.path.join(path, '*'))):
        loadable.files.append(file_path)
    try:
        flag = plugin.load(loadable)
    except Exception as e:
        print(e)

load_dicom_folder('folderPath')
</code></pre>
<p>I removed the progress dialog window, since it’s so fast It’s barely useful nowadays.</p>

---

## Post #5 by @lassoan (2020-04-19 20:44 UTC)

<p>You can also find up-to-date DICOM loading examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">script repository</a>.</p>

---

## Post #6 by @Davide_Cester (2020-04-20 07:56 UTC)

<p>I did not find found that page before… the code there is much better<br>
than mine, with the official script in the Wiki the Patient and the<br>
Study are also handled! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thank you!</p>

---
