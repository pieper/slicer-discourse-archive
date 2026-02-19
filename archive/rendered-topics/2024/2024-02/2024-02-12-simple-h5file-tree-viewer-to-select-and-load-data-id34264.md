---
topic_id: 34264
title: "Simple H5File Tree Viewer To Select And Load Data"
date: 2024-02-12
url: https://discourse.slicer.org/t/34264
---

# Simple h5file tree viewer to select and load data

**Topic ID**: 34264
**Date**: 2024-02-12
**URL**: https://discourse.slicer.org/t/simple-h5file-tree-viewer-to-select-and-load-data/34264

---

## Post #1 by @Michael_Hsi (2024-02-12 19:24 UTC)

<p>Hello,</p>
<p>My data (3d uint8/uint16/fp32 array) are stored in h5 files, under the ‘data’ key. the h5file is created in python, using h5py and hdf5plugin (for zstd compression/decompression). is there anyway we can implement a tree viewer for users to select a key and load the array?</p>
<p>can help with implementing this feature.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2024-02-12 21:17 UTC)

<p>What data would you like to store in the HDF5 file? Images, segmentations, meshes, annotations, additional metadata, …? HDF5 is just a container and does not specify a format to store any of these data sets.</p>
<p>There are well-established file formats for all these (e.g., nrrd, nifti, metaio, vtk for images; ply, obj, stl, vtk for meshes…). Redefining a new file format from scratch would be a lot of work and would cut you off from the rest of the world, so it is probably not the best solution. There are many HDF5-based image file formats, such as the old MINC2 (which never really took off) or the new OME-NGFF (which has not really taken off yet). There are readers already implemented for these formats in ITK, which you can use in Slicer.</p>
<p>If you are interested in HDF5 to store multiple files in a single file then again there may be simpler and more standard solutions. If you store your data on a server then you can use its protocol to load data (dicom/dicomweb, flywheel, xnat, etc.). If you don’t want to use a server and just use a local file then you can simply zip the files and drag-and-drop the zip file into Slicer. If you load an entire folder structure into Slicer then you can right-click the subject hierarchy root (in Data module) to recreate the directory structure in the subject hierarchy tree.</p>
<p>There are just so many standard, well-established, well-supported solutions that could be used that I think we should step back and consider what we can reuse before jumping into developing yet another thing that needs to be maintained.</p>
<p>Could you write a bit about your use case, what is your ultimate goal? What is the clinical problem you want to solve and what is the approach that you are currently considering?</p>

---

## Post #3 by @Michael_Hsi (2024-02-12 21:31 UTC)

<p>Hi, thanks for the clarification! I agree that jumping into a new standard is very cumbersome and not the best solution.</p>
<p>the h5 files stores the data i need for my neural network.</p>
<p>My network is currently training for a pretext task, which means with any give 3d ct array (1k by1k by 1k image), it only loads a 7 by 256 by 256 small patch. making traditional tiff, nrrd, nitfi extremely inefficient. depending on the axis, the patch can be one of 7x256x256 or 256x7x256 or 256x256x7, so using 2d tiff sequence is also not possible, as that will require 3x storage space for each scan.</p>
<p>the h5file not only contains the 3d CT image under the name ‘data’, there are also other processed images, like uint8 segmentation, or uint16 segments from some superpixel procedures. I am only looking for a convinent way to visualize them.</p>
<p>perhaps the best approach is for me to write a simple python extension for my very specific use case? if thats the case, can you point me to some tutorials on creating a plugin?</p>
<p>Currently the only way to visualize is to use python to export the data in h5 to tiff sequences, making visualization very annoying.</p>
<p>i have explored with plugin in Fiji and ImageJ, it wont open.</p>

---

## Post #4 by @muratmaga (2024-02-13 01:33 UTC)

<p>So the use case of keeping all associated (segmentation, original intensity images, different resolutions, etc) is usually accomplished thru MRB bundle in Slicer. It is a simple zip based archive that keeps all the data together and if you need to open parts of it in a fiji l, you simply unzip the bundle and load the data. To me that seems better data management than writing an extension for opening your custom h5.</p>
<p>As for training, are you doing this using Slicer’s python or outside? It is true that NRRD does not support multiscale data, however ZARR does. You can possibly use zarr for your image patches. There is some support for zarr in slicer.</p>
<p>Alternatively you can keep your patches numpy arrays and load them.</p>

---
