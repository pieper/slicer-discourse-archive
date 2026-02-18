# Export model to model distances as.csv

**Topic ID**: 18506
**Date**: 2021-07-04
**URL**: https://discourse.slicer.org/t/export-model-to-model-distances-as-csv/18506

---

## Post #1 by @fred (2021-07-04 19:27 UTC)

<p>Slicer 4.11 on Mac OS X.</p>
<p>Hi everyone,<br>
I’d like to export the results of the “model to model distance” extension as an .csv file for further analysis of the 3D distances. The “mesh statistics” extension only computes Min; Max; Mean; etc… but I need the entire dataset of 3D distances between the 2 models.</p>
<p>I never used python, but found some lines in this topic: <a href="https://discourse.slicer.org/t/model2model-distance-export-values-of-vtk-file/15633" class="inline-onebox">Model2model distance: export values of vtk file</a></p>
<p>Yet the lines do not seem to work for me.</p>
<blockquote>
<blockquote>
<blockquote>
<p>modelNode = slicer.util.getNode(‘VTK Output File’)<br>
distances = slicer.util.arrayFromModelPointData(modelNode,‘Absolute_to_BBCJG_vtkMRMLModelNodeF’)<br>
pandas.DataFrame(distances).to_csv(r’~/Desktop/Model/data.csv’, index=False)</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘pandas’ is not defined</p>
</blockquote>
<p>Thank you very much in advance for your help!</p>

---

## Post #2 by @Fluvio_Lobo (2021-07-04 22:29 UTC)

<p><a class="mention" href="/u/fred">@fred</a>,</p>
<p>Regarding your code, there are few things you need to change.</p>
<ol>
<li>
<p>You need to install the <code>pandas</code> Python library or module. To do this, execute the following line in the Python Interactor: <code>slicer.util.pip_install('pandas')</code> [<a href="https://discourse.slicer.org/t/install-python-library-with-extension/10110">1</a>]</p>
</li>
<li>
<p>Then Import the <code>pandas</code> module by executing <code>import pandas</code> also in the Python Interactor</p>
</li>
</ol>
<p>Now you can enter the code above but, keep in mind that some variables may not be the same as you expect. For instance;</p>
<ol>
<li>
<p><code>modelNode = slicer.util.getNode("VTK Output File")</code> you may have named the output file to something other than <strong>VTK Output File</strong></p>
</li>
<li>
<p><code>slicer.util.arrayFromModelPointData(modelNode,"Absolute_to_BBCJG_vtkMRMLModelNodeF")</code> I am not sure what <code>Absolute_to_BBCJG_vtkMRMLModelNodeF</code> is but you may need to change this to one of the variables in the VTK structure, such as: <code>PointToPointVector</code> or <code>PointToPointAlongX</code> and so on…</p>
</li>
<li>
<p>Finally, make sure you have the correct path here <code>pandas.DataFrame(distances).to_csv(r"~/Desktop/Model/data.csv", index=False)</code></p>
</li>
</ol>
<p>Also, I had to change all of the single quotations <code>'</code> to double <code>"</code>, I think this is a Windows/Linux thing. I am using a Windows!</p>
<p>Another trick that may work for you is to inspect the <strong>VTK Output File</strong> manually. You can always save the file as a ASCii or decompressed version of the file and open it with a text reader.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efe5e149260ee0726e50a9a466d7948735d13184.png" data-download-href="/uploads/short-url/yeeD806JuibQaTn6vrqiZlYUmmU.png?dl=1" title="ascii_version" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efe5e149260ee0726e50a9a466d7948735d13184_2_517x143.png" alt="ascii_version" data-base62-sha1="yeeD806JuibQaTn6vrqiZlYUmmU" width="517" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efe5e149260ee0726e50a9a466d7948735d13184_2_517x143.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efe5e149260ee0726e50a9a466d7948735d13184_2_775x214.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efe5e149260ee0726e50a9a466d7948735d13184.png 2x" data-dominant-color="4C4B4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ascii_version</span><span class="informations">908×252 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @fred (2021-07-05 06:23 UTC)

<p>Thank you Fluvio_Lobo !</p>
<p>I had to install Pandas first, so the 2 first lines you provided did the job.<br>
Regarding the names for the output file and the variable, I used the ones I was actually working on, so everything was fine.<br>
And thank you for the trick with the decompressed file!</p>

---
