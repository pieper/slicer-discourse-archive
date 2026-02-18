# How can I convert NIFTI files to NRRD files in command lines?

**Topic ID**: 3631
**Date**: 2018-08-02
**URL**: https://discourse.slicer.org/t/how-can-i-convert-nifti-files-to-nrrd-files-in-command-lines/3631

---

## Post #1 by @Kyu_Sung_Choi (2018-08-02 02:09 UTC)

<p>Hello,</p>
<p>I have <em>4D dynamic susceptibility contrast (DSC) dicom images (T2* with contrast agent) to analyze.</em><br>
I’ve noticed that I can convert NIFTI files to NRRD files, just by click “Save” in Slicer.<br>
<strong>However, I want to convert hundreds of NIFTI files to NRRD files, so I need to do it by command lines.</strong><br>
Could anyone please tell me how can I do it by command lines?<br>
Thank you in advance!</p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #2 by @lassoan (2018-08-02 07:45 UTC)

<p>All operations you perform on the GUI are accessible through Python scripting, too. Save/load functions are exposed using a convenient interface in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html">slicer.util package</a>. You can start a script directly from the command-line as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_slicer_operations_from_a_batch_script.3F">here</a>.</p>

---

## Post #3 by @Kyu_Sung_Choi (2018-08-02 08:26 UTC)

<p>Thank you so much.<br>
However, I don’t understand why the code below is not working.<br>
<strong>Could you please tell me what’s the problem? (e.g. option, syntax, etc.)</strong></p>
<p><em>1. I just want to load 35000671_DSC.nii.gz and save as a NRRD file with the same basename (i.e. save/load problem for a single file).</em></p>
<p>MRHead=slicer.util.loadVolume(“D:\Data\SNUH_glioma\35000671_DSC.nii.gz”, returnNode=True)<br>
head = slicer.util.getNode(‘MRHead’)<br>
slicer.util.saveNode(head, “D:\Data\SNUH_glioma\35000671_DSC.nrrd”)</p>
<p>exit()</p>
<p><em>2. Moreover, I can’t find how to load files from the folder containing all the NIFTI files (hundreds of enrolled patient’s MRI) and save as NRRD files with the same basename.</em></p>
<p><strong>Could you please tell me how to deal with this multi-files case?</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fb709cf7b7054150a949002755e31cfb5ddb381.png" alt="capture" data-base62-sha1="fWh9JzqvyxzXXciFZ1qOPgMS75v" width="674" height="196"><br>
Thank you so much!<br>
Best,<br>
Kyu Sung</p>

---

## Post #4 by @lassoan (2018-08-02 09:44 UTC)

<p>You can get filename from full path or get all files in a folder using standard Python commands. You can easily find answers on Google search and StackOverflow.</p>

---

## Post #5 by @Kyu_Sung_Choi (2018-08-02 11:33 UTC)

<p>Thank you so much for quick response!</p>
<p>However, I think it’s not the problem of Python commands.<br>
I think it’s because there’s no “slicer.py” on my Slicer folder.<br>
I think I should “import slicer” or “import slicer.util” to use those functions such as loadVolume, getNode, and saveNode. But “import slicer” in python console makes an error saying there’s no module named ‘slicer’.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/792bab264fcbfe8bdc29c65194f1da0fd80b835f.png" data-download-href="/uploads/short-url/hhVkFt17ObNVuXA7VCvHCAjNQTl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/792bab264fcbfe8bdc29c65194f1da0fd80b835f.png" alt="image" data-base62-sha1="hhVkFt17ObNVuXA7VCvHCAjNQTl" width="685" height="500" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">831×606 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Moreover, I can’t find more specific usage of “slicer.util.loadVolume” from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util" rel="noopener nofollow ugc">link</a>.<br>
For example, does the argument “filename” mean full file path - which is I understood?</p>
<p>I did it on the Slicer Python interactor, then I’ve got errors like these.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab51fde11dcfd6c8b96034d5a575278cd0f38dff.png" data-download-href="/uploads/short-url/orzjsAsS6iMMdEzKzT6L1gp7Oph.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab51fde11dcfd6c8b96034d5a575278cd0f38dff.png" alt="image" data-base62-sha1="orzjsAsS6iMMdEzKzT6L1gp7Oph" width="690" height="412" data-dominant-color="FAEBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">938×561 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please give more specific information to solve this problem?<br>
Thank you so much for your help!</p>

---

## Post #6 by @pieper (2018-08-02 11:39 UTC)

<p>Hi <a class="mention" href="/u/kyu_sung_choi">@Kyu_Sung_Choi</a> - you need to use forward slashes for your paths in python:  “d:/file” not “d:\file”</p>
<p>HTH,<br>
Steve</p>

---

## Post #7 by @Kyu_Sung_Choi (2018-08-02 11:42 UTC)

<p>Thank you for your quick response!</p>
<p>However, both ways are seemed to be not working.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d826f301260b0cafda39b52e68b40881b89d3ad.png" data-download-href="/uploads/short-url/4d3iEEYS7IJyD0lOCf81rpx7dz7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d826f301260b0cafda39b52e68b40881b89d3ad.png" alt="image" data-base62-sha1="4d3iEEYS7IJyD0lOCf81rpx7dz7" width="690" height="403" data-dominant-color="FAECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">952×557 42.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can anyone tell me where should I save my python file not to see the error msg saying “no modules named ‘slicer’”?<br>
I can’t find “slicer.py” or “slicerrc.py” in Slicer folder.<br>
Thank you in advance!</p>

---

## Post #8 by @lassoan (2018-08-02 12:37 UTC)

<p>If you want to use Slicer from a Jupyter notebook, then you need to use the Slicer Jupyter kernel. See instructions here: <a href="https://github.com/Slicer/SlicerJupyter">https://github.com/Slicer/SlicerJupyter</a>.</p>
<p>Within Slicer’s Python interactor, slicer.util.loadVolume works well for me. Could you try to load a different image (e.g., download a Slicer sample data set, save to disk, and try to load that). Use stable or latest nightly version of Slicer. If you have any problems then attach the full application log (menu: Help / Report a bug).</p>

---

## Post #9 by @Kyu_Sung_Choi (2018-08-03 00:20 UTC)

<p>Thank you for your quick response!<br>
However, I’ve found that Python interactor works well on my workstation, not my desktop.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9dbf5b59539008c2c3ffc0489a4897492c9a29b.png" data-download-href="/uploads/short-url/sNJesF0dtVnkgAZ6naSXjpCSkTF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9dbf5b59539008c2c3ffc0489a4897492c9a29b_2_534x500.png" alt="image" data-base62-sha1="sNJesF0dtVnkgAZ6naSXjpCSkTF" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9dbf5b59539008c2c3ffc0489a4897492c9a29b_2_534x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9dbf5b59539008c2c3ffc0489a4897492c9a29b_2_801x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9dbf5b59539008c2c3ffc0489a4897492c9a29b.png 2x" data-dominant-color="F3EFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1020×954 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>As you recommended, loading sample data (i.e. MRhead) and saving in NRRD file works well within Python interactor.</em></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/638e021e0a483d037d48a86de1394e5ada52b04e.png" data-download-href="/uploads/short-url/ecHwij3yqDhvoAFIrX7wX7nxGuq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/638e021e0a483d037d48a86de1394e5ada52b04e_2_690x221.png" alt="image" data-base62-sha1="ecHwij3yqDhvoAFIrX7wX7nxGuq" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/638e021e0a483d037d48a86de1394e5ada52b04e_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/638e021e0a483d037d48a86de1394e5ada52b04e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/638e021e0a483d037d48a86de1394e5ada52b04e.png 2x" data-dominant-color="F9FCFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">891×286 54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, let me put it in this way then,</p>
<p><strong>1. Where should I save my slicer_test.py file (i.e. path)?</strong><br>
slicer_test.py is the simplest code below.</p>
<p>import slicer<br>
slicer.util.loadVolume(“/home/cndl/DSC/CBV_map/35000671_CBV.nii.gz”)</p>
<p>I saved my slicer_test.py file in /bin/Python/slicer, where util.py in which loadVolume() function is contained.<br>
However, running “python slicer_test.py” in command line gives me below error msg.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a46c55f620018d5decc021476a927e939614353.png" data-download-href="/uploads/short-url/m0N9HVuXdj45o3cj7FIgz47ann5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a46c55f620018d5decc021476a927e939614353.png" alt="image" data-base62-sha1="m0N9HVuXdj45o3cj7FIgz47ann5" width="690" height="102" data-dominant-color="38172E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×108 17.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to find “slicer.py” to import slicer module, which I couldn’t find at all.</p>
<p><strong>2. Can I use “slicer.util.loadVolume → slicer.util.getNode → saveNode” functions in a row to convert NIFTI files in NRRD files?</strong><br>
However, above code makes an error.<br>
I think I don’t understand what the “Node” is.<br>
Do I have to use “loadNodeFromFile” function instead?<br>
However, I don’t understand the argument “filetype”, which is not specific in the slicer package usage link.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c014ac6ff300918e046ed33682e8559fa9d698f3.png" alt="image" data-base62-sha1="rpdXYct9yYSvGbsKIH5JEhxXPTZ" width="614" height="112"></p>
<p>Could you please give me more specific answer?<br>
Thank you in advance!</p>
<p>Best,<br>
Kyu Sung</p>

---

## Post #10 by @lassoan (2018-08-03 09:49 UTC)

<p>It does not matter where you put your .py file. However, it is important to run it using Slicer.exe and not using Python.exe. Some features work with PythonSlicer.exe, too.</p>
<p>You can load volume using slicer.util.loadVolume(‘my filename.nrrd’)</p>

---

## Post #11 by @Kyu_Sung_Choi (2018-08-03 10:36 UTC)

<p>Oh, I see. What a mistake!<br>
Refering below link, I wrote the code below and solve it by entering the below command in the command line.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file</a></p>
<p>import slicer<br>
[success, loadedVolumeNode] = slicer.util.loadVolume("/home/cndl/DSC/CBV_map/35000671_CBV.nii.gz", returnNode=True)<br>
slicer.util.saveNode(loadedVolumeNode, “/home/cndl/DSC/CBV_map/35000671_CBV.nrrd”)</p>
<p>./Slicer --no-main-window --no-splash --python-script slicer_test.py</p>
<p><strong>However, I’ve noticed I have to load 4D DSC images, which cannot be done by util.loadVolume() function.</strong><br>
Should I use MultiVolumeImporter then?<br>
However, I can’t find any function by that name on the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html" rel="nofollow noopener">link</a> you posted.<br>
<strong>Please let me know what function should I use to load 4D DSC images in Python script?</strong><br>
So sorry to bother you.<br>
Thank you so much!</p>

---

## Post #12 by @fedorov (2018-08-03 21:42 UTC)

<p><a class="mention" href="/u/kyu_sung_choi">@Kyu_Sung_Choi</a> please see this post for the answer to your last question: <a href="https://discourse.slicer.org/t/how-can-i-import-nifti-files-to-dscmrianalysis-module/3645/2">How can I import NIFTI files to DSCMRIAnalysis module?</a></p>

---

## Post #13 by @fuentesdt (2020-10-12 15:52 UTC)

<p>Hi, Is it possible to convert 4D dicom images to a single nrrd file using the slicer/python command line?  I want to loop over a collection of 4d data and convert each to nrrd or nifti for analysis.</p>
<p>I tried slicer.util.LoadVolume but am trying to split the data across the acquisition time. Is there an equivalent multivolumeimporter python call ?</p>
<p>for key,value in fileDict.items():<br>
if ( value[‘SeriesModality’] == ‘MR’):<br>
node=slicer.util.loadVolume(value[‘dcmfile’],returnNode=True);<br>
outputdir = ‘tmpconvert/%04d%03d/’ % (int(value[‘PatientNumber’]) ,value[‘StudyNumber’])<br>
print( outputdir )<br>
os.system('mkdir -p %s ’ % outputdir  )<br>
slicer.util.saveNode(node[1], ‘%s/%s.nii.gz’ % (outputdir,value[‘seriesanonuid’] )  )<br>
exit()</p>
<p>thanks!</p>

---

## Post #14 by @lassoan (2020-10-12 22:15 UTC)

<aside class="quote no-group" data-username="fuentesdt" data-post="13" data-topic="3631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fuentesdt/48/9361_2.png" class="avatar"> fuentesdt:</div>
<blockquote>
<p>I tried slicer.util.LoadVolume but am trying to split the data across the acquisition time.</p>
</blockquote>
</aside>
<p><code>slicer.util.LoadVolume</code> supports very basic DICOM image import, but it is generally not recommended for loading DICOM data. It cannot load 4D data sets.</p>
<aside class="quote no-group" data-username="fuentesdt" data-post="13" data-topic="3631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fuentesdt/48/9361_2.png" class="avatar"> fuentesdt:</div>
<blockquote>
<p>Is it possible to convert 4D dicom images to a single nrrd file using the slicer/python command line?</p>
</blockquote>
</aside>
<p>Yes, this should be no problem at all. You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">load a 4D volume from DICOM</a> and then <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_can_I_convert_DICOM_to_NRRD_on_the_command_line.3F">save it as nrrd</a>.</p>
<p>If you really just need to convert images from DICOM to nrrd then you can also use standalone command-line tools, such as dcm2niix.</p>

---
