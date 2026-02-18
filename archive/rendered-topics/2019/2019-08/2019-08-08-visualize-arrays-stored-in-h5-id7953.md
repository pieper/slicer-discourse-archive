# Visualize arrays stored in h5

**Topic ID**: 7953
**Date**: 2019-08-08
**URL**: https://discourse.slicer.org/t/visualize-arrays-stored-in-h5/7953

---

## Post #1 by @rogertrullo (2019-08-08 21:43 UTC)

<p>Hi,<br>
I know that hdf5 is just a container as discussed in <a href="https://discourse.slicer.org/t/regarding-h5-file-format/4172/2">here</a> , however I think it can be a greate feature to have some kind of option to display 3d arrays in 3D slicer. The format is widely used in the machine learning community and I find my self duplicating data to common formats just to visualize it. As an example, there is also the xdmf format which can read the data array from h5 files and which can be visualized in paraview. Would it be difficult to add support for this?<br>
Otherwise, is it possible to make a python pluggin for this purpose; if so what would be an example to start with?<br>
Thanks!</p>
<p>Roger</p>

---

## Post #2 by @pieper (2019-08-09 00:25 UTC)

<p>Hi Roger -</p>
<p>Sure, that sounds pretty useful and doable in a few lines of python.  I believe you can easily get a numpy array with contents of the h5 file and you can populate a <code>vtkMRMLScalarVolumeNode</code> with the data.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>

---
