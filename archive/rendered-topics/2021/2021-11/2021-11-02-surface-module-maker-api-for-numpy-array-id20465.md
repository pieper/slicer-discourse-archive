# Surface module maker API for numpy array

**Topic ID**: 20465
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/surface-module-maker-api-for-numpy-array/20465

---

## Post #1 by @txuh (2021-11-02 18:58 UTC)

<p>I have a input 3D volume data (binary 0/1) . I know “surface module maker” works pretty well for me in 3D slicer. Now I am trying to build an API. The input is the numpy 3D array (0/1) and output is the surface module VTK file. Could someone advise how to achieve this or kindly share an example?</p>
<p>Thanks a lot<br>
Elliot</p>

---

## Post #2 by @lassoan (2021-11-02 19:45 UTC)

<p>I would recommend to use Segmentation module for converting binary labelmaps to 3D models (meshes). You can find full working examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>
<p>You can access and modify a segmentation as a numpy array as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">here</a>. You can also create a labelmap volume node from a numpy array and then import that into a segmentation.</p>

---

## Post #3 by @txuh (2021-11-02 20:00 UTC)

<p>Dear Iassoan,</p>
<p>Thanks for your reply. It seems I have to go to Python console in Slicer for using segmentation module. Is there a way that I can achieve this outside 3D slicer (no 3d slicer installed) or call slicer library?</p>
<p>Bests,<br>
Elliot</p>

---

## Post #4 by @lassoan (2021-11-02 20:06 UTC)

<p>You can install Slicer, or just unpack a Slicer application package somewhere, or use one of the Slicer docker images and run those Python commands in Slicer’s Python environment as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#run-python-commands-in-the-slicer-environment">here</a>.</p>
<p>If you work in Jupyter notebooks then you can use <a href="https://github.com/Slicer/SlicerJupyter">Slicer’s Jupyter kernel</a>.</p>
<p>You can also pip-install all Python packages into Slicer and run all your Python code from there.</p>

---

## Post #5 by @txuh (2021-11-08 19:54 UTC)

<p>Hi Iassoan,</p>
<p>Thanks for all your advice. I tried pyvisa and  It seems it is able to achieve this by using smooth(). However, the visualization in pyvista looks much worse than in 3D slicer, both lighting and surface. Could you please advise if any idea?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ee080a6ea11e00c69752cba62e3d6c8e74769bc.png" alt="image" data-base62-sha1="bfMeHJsulrfEcjNfWWguV2rnCWw" width="506" height="386"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86e017d86664b4234c443d0851898bbca5f4c62f.jpeg" alt="image" data-base62-sha1="jfa66dfzCW78Ecl4U6JsG8WZ9Ez" width="616" height="481"></p>
<p>Thank you<br>
Elliot</p>

---

## Post #6 by @lassoan (2021-11-08 20:11 UTC)

<p>Both Slicer and pyvista uses VTK for mesh operations. Pyvista does not add new features to VTK, it is just a thin wrapper over VTK to provide a more pythonic interface. Slicer adds thousands of higher-level features on top of VTK that are useful for medical image computing.</p>
<p>I don’t know which ones of those thousands of features were actually missing in this case. In the top image it seems that polydata normals are not computed. Computing those would remove the faceted look.</p>
<p>But this is just one small example. If you are building a medical image computing application using low-level generic tools such as VTK then you will spend most of your time reimplementing basic features from scratch that have been all figured out and solved many years ago. Instead, I would recommend to spend time with learning to use a higher-level medical image computing framework (such 3D Slicer or MITK). As you get better, you get familiar with how things work internally, learn how to extend, improve things, etc. You eventually would still learn all the ins and outs of VTK, Slicer, etc. but you would spend time with learning and developing new, relevant things and not waste your time with redeveloping existing features.</p>

---

## Post #7 by @txuh (2021-11-08 21:10 UTC)

<p>That’s great. Thanks very much for the detailed replay and advice!</p>

---
