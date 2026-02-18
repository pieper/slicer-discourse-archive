# Model2model distance: export values of vtk file

**Topic ID**: 15633
**Date**: 2021-01-22
**URL**: https://discourse.slicer.org/t/model2model-distance-export-values-of-vtk-file/15633

---

## Post #1 by @nabilgh (2021-01-22 16:11 UTC)

<p>I’m using Slicer 4.11 to compare the deviation between 2 dental models.<br>
I used the model2model distance extension to compare the models.<br>
The output created was VTK Output File.<br>
I would like to get the values in mm in an array so I used the following lines in the python interactor:</p>
<blockquote>
<p>modelNode = slicer.util.getNode(‘VTK Output File’)<br>
distances = slicer.util.arrayFromModelPointData(modelNode,‘testArray’)</p>
</blockquote>
<p>However I am getting the following error:</p>
<blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>distances = slicer.util.arrayFromModelPointData(modelNode,‘testArray’)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\User\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 1293, in arrayFromModelPointData<br>
narray = vtk.util.numpy_support.vtk_to_numpy(arrayVtk)<br>
File “C:\Users\User\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Lib\site-packages\vtkmodules\util\numpy_support.py”, line 216, in vtk_to_numpy<br>
typ = vtk_array.GetDataType()<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetDataType’</p>
</blockquote>
</blockquote>
</blockquote>
</blockquote>
<p>Any help is aprreciated. Thanks</p>

---

## Post #2 by @lassoan (2021-01-22 16:15 UTC)

<p>You provided an incorrect array name. In recent Slicer versions, this error message is improved: you get the list of available arrays. You can also look up the available array names in Models module / Display / Scalars.</p>

---

## Post #3 by @nabilgh (2021-01-22 16:30 UTC)

<p>thank you it worked. How do I export the array to a file / excel sheet?</p>

---

## Post #4 by @lassoan (2021-01-22 16:41 UTC)

<p>You get the values as a numpy array, so you can already do all the statistics that Excel can do using a few lines of Python code (using numpy, pandas, etc.). To browse values in a nicer environment than the plain Python console, you can use Jupyter notebooks or JupyterLab (using <a href="https://github.com/Slicer/SlicerJupyter">SlicerJupyter extension</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85564b64df6e8cf6c8331c247da456bf1c58f9ee.png" data-download-href="/uploads/short-url/j1yo6aavoLUQRl99lQWq0By9hTw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85564b64df6e8cf6c8331c247da456bf1c58f9ee_2_690x363.png" alt="image" data-base62-sha1="j1yo6aavoLUQRl99lQWq0By9hTw" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85564b64df6e8cf6c8331c247da456bf1c58f9ee_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85564b64df6e8cf6c8331c247da456bf1c58f9ee_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85564b64df6e8cf6c8331c247da456bf1c58f9ee_2_1380x726.png 2x" data-dominant-color="F8F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1772×934 70.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Anyway, you can save a numpy array into csv file format that Excel can load, for example using this command <code>pandas.DataFrame(distances).to_csv(filename)</code>.</p>

---

## Post #5 by @sfglio (2021-01-23 20:58 UTC)

<p>I am a complete newbie to python scripting however I would like to run the</p>
<p>modelNode = slicer.util.getNode(‘VTK Output File’)<br>
distances = slicer.util.arrayFromModelPointData(modelNode,‘testArray’)</p>
<p>and I always get</p>
<blockquote>
<blockquote>
<blockquote>
<p>modelNode = slicer.util.getNode(‘VTK Output File’)<br>
File “”, line 1<br>
modelNode = slicer.util.getNode(‘VTK Output File’)<br>
^<br>
SyntaxError: invalid character in identifier</p>
</blockquote>
</blockquote>
</blockquote>
<p>I have created my vtk output file,  but do I need to import it anyway?</p>

---

## Post #6 by @nabilgh (2021-01-23 22:28 UTC)

<p>I’m also a newbie in scripting but I managed to follow <a class="mention" href="/u/lassoan">@lassoan</a> instructions above. You cannot use the “testArray” name for your array. You have to go to Models section, select you VTK Output File then navigate to Display/Scalars and choose a name from the active scalar list. For me this code worked:</p>
<blockquote>
<p>modelNode = slicer.util.getNode(VTK Output File)</p>
<p>distances = slicer.util.arrayFromModelPointData(modelNode,‘PointToPointVector’)</p>
<p>pandas.DataFrame(distances).to_csv(r’C:\Users\user\Desktop\data.csv’, index=False)</p>
</blockquote>
<p>The last line of code enables the export to csv file. You’ll get 3 columns of values in the sheet. However i’m not sure if every column refers to a dimension (x,y,z).</p>

---

## Post #7 by @sfglio (2021-01-24 21:03 UTC)

<p>Thank you for your quick reply however I failed on MacOS specific spellings when copying the code, i.e.<br>
the mistake was the incorrectly converted  ’  when pasting the code.</p>
<p>modelNode = slicer.util.getNode(‘VTK Output File’)</p>
<p>and to export on mac:<br>
pandas.DataFrame(distances).to_csv(r’~/Desktop/whatever/data.csv’, index=False)</p>
<p>Anyway, the question remains whether “Signed” or “PointToPointVector” is more suitable to describe distances between to meshes (e.g. two dental models).<br>
So if I only want to describe the dimension of a vertical displacement between two models then second column (y) of the Pointtopointvector would fit best???<br>
If I am interested in the maximum deviations (regardless of the axis) then “signed” would also fit…keeping in mind that I can have a look at the distance map to see where max. deviations were found.</p>
<p>Unfortunately it makes a difference which scalar you choose in terms of “mm” (signed vs. pointtopointvector)!<br>
Other software to create distance maps where a scale bar is present seem to rely on “signed”…</p>

---

## Post #8 by @lassoan (2021-01-24 22:33 UTC)

<p>I would recommend to create a new topic to get advice on which metric to use. Add a few annotated images because it is not possible to explain what exactly you would like to quantify in plain text.</p>

---
