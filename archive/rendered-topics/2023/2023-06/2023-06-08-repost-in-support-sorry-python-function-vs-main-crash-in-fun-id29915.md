---
topic_id: 29915
title: "Repost In Support Sorry Python Function Vs Main Crash In Fun"
date: 2023-06-08
url: https://discourse.slicer.org/t/29915
---

# Repost in support (sorry) python function vs main / crash in function but not in main

**Topic ID**: 29915
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/repost-in-support-sorry-python-function-vs-main-crash-in-function-but-not-in-main/29915

---

## Post #1 by @Nicolas_Tempier (2023-06-08 10:15 UTC)

<p>Hello everyone,<br>
first of all, sorry for the repost, i posted this issue in development section instead of support …</p>
<p>i have a little problem understanding why my code crashes when i use it as a function.</p>
<p>i want to display a ndpi image, which works but i want to improve the code to make it quicker.</p>
<p>so i made a new script to load and display my image. if i use it as an “alone” code, or main like this :</p>
<pre><code class="lang-auto">
import numpy as np
import slicer
import vtk
from vtk.util import numpy_support
from PIL import Image
import openslide

volume_name = ‘image_loaded’
size = None
image_path = ‘/media/nicolas.tempier/NT_LAU_KARA/These/NDPI_treatment/H2h_TH_330_2022_04_26_16_34_57.ndpi’
level = 5
top_left_coordinates = (0, 0)

# Charger l’image NDPI

image_ndpi = openslide.OpenSlide(image_path)

# Obtenir les dimensions du niveau

dimensions = image_ndpi.level_dimensions[level]

# Obtenir le facteur de sous-échantillonnage du niveau

downsample_factor = image_ndpi.level_downsamples[level]

# Convertir les coordonnées du niveau cible en coordonnées du niveau 0

top_left_coordinates_level_0 = (int(top_left_coordinates[0] * downsample_factor),
int(top_left_coordinates[1] * downsample_factor))

# Sélectionner résolution

print(f"Résolution sélectionnée: {level}")
if size is None:
size = image_ndpi.level_dimensions[level]

# Lire l’image en utilisant les coordonnées du niveau 0

image_matrix = image_ndpi.read_region(top_left_coordinates_level_0, level, size)

# Convertir l’image en un tableau NumPy et créer un objet VTK Image

image_array = np.array(image_matrix)[:, :, :3]
image_array = np.swapaxes(image_array, 0, 1)
image_array = np.ascontiguousarray(image_array, dtype=np.uint8)

# Créer une image VTK avec 3 dimensions spatiales et 3 dimensions d’intensité pour les canaux RGB

vtk_image_rgb = vtk.vtkImageData()
vtk_image_rgb.SetDimensions(image_array.shape[1], image_array.shape[0], 1)
vtk_image_rgb.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 3)
vtk_image_rgb.SetSpacing(1, 1, 1)

# Convertir le tableau NumPy en une liste d’octets

image_list = image_array.flatten()

# Convertir la liste d’octets en un tableau VTK

vtk_array = numpy_support.numpy_to_vtk(num_array=image_list, deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)

# Associer le tableau VTK à un vtkUnsignedCharArray

rgb_array_vtk = vtk.vtkUnsignedCharArray()
rgb_array_vtk.SetNumberOfComponents(3)
rgb_array_vtk.SetArray(vtk_array, len(image_list), 1)

# Associer le tableau vtkUnsignedCharArray aux scalaires de l’image VTK

vtk_image_rgb.GetPointData().SetScalars(rgb_array_vtk)

# Ajouter l’image à un nœud de volume dans 3D Slicer

volume_node = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLVectorVolumeNode’, volume_name)
volume_node.SetSpacing(1, 1, 1)
volume_node.SetAndObserveImageData(vtk_image_rgb)
slicer.app.applicationLogic().PropagateVolumeSelection(0)
</code></pre>
<p><strong>It works !</strong> i can clic on on display, volume information etc</p>
<p>But when i modify it as a function :</p>
<pre><code class="lang-auto">
import numpy as np
import slicer
import vtk
from vtk.util.vtkImageImportFromArray import vtkImageImportFromArray
from vtk.util import numpy_support
from PIL import Image
import timeit

try:
import openslide
except:
slicer.util.pip_install(‘openslide-python’)
import openslide

def load_ndpi_image2(image_path, level, bottom_right_coordinates, size=None, volume_name=‘image_loaded’):
# Charger l’image NDPI
image_ndpi = openslide.OpenSlide(image_path)

# Obtenir les dimensions du niveau
dimensions = image_ndpi.level_dimensions[level]

# Obtenir le facteur de sous-échantillonnage du niveau
downsample_factor = image_ndpi.level_downsamples[level]

# Convertir les coordonnées du niveau cible en coordonnées du niveau 0
top_left_coordinates_level_0 = (int(bottom_right_coordinates[0] * downsample_factor),
                                int(bottom_right_coordinates[1] * downsample_factor))

# test1 = int(input('crash ? 1 '))


# Sélectionner résolution
print(f"Résolution sélectionnée: {level}")
if size is None:
    size = image_ndpi.level_dimensions[level]

# Lire l'image en utilisant les coordonnées du niveau 0
image_matrix = image_ndpi.read_region(top_left_coordinates_level_0, level, size)

# Convertir l'image en un tableau NumPy et créer un objet VTK Image
image_array = np.array(image_matrix)[:, :, :3] 
image_array = np.swapaxes(image_array, 0, 1)
image_array = np.ascontiguousarray(image_array, dtype=np.uint8)

# test2 = int(input('crash ? 2 '))


# Créer une image VTK avec 3 dimensions spatiales et 3 dimensions d'intensité pour les canaux RGB
vtk_image_rgb = vtk.vtkImageData()
vtk_image_rgb.SetDimensions(image_array.shape[1], image_array.shape[0], 1)
vtk_image_rgb.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 3)
vtk_image_rgb.SetSpacing(1, 1, 1)

# Convertir le tableau NumPy en une liste d'octets
image_list = image_array.flatten()

# Convertir la liste d'octets en un tableau VTK
vtk_array = numpy_support.numpy_to_vtk(num_array=image_list, deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)

# test3 = int(input('crash ? 3 '))


# Associer le tableau VTK à un vtkUnsignedCharArray
rgb_array_vtk = vtk.vtkUnsignedCharArray()
rgb_array_vtk.SetNumberOfComponents(3)
rgb_array_vtk.SetArray(vtk_array, len(image_list), 1)

# Associer le tableau vtkUnsignedCharArray aux scalaires de l'image VTK
vtk_image_rgb.GetPointData().SetScalars(rgb_array_vtk)

# test4 = int(input('crash ? 4 '))


# Ajouter l'image à un nœud de volume dans 3D Slicer
volume_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLVectorVolumeNode', volume_name)
volume_node.SetSpacing(1, 1, 1)
volume_node.SetAndObserveImageData(vtk_image_rgb)
slicer.app.applicationLogic().PropagateVolumeSelection(0)

image_path = “ilovedealingwithcrashes.ndpi”
load_ndpi_image2(“/media/nicolas.tempier/NT_LAU_KARA/These/NDPI_treatment/H2h_TH_330_2022_04_26_16_34_57.ndpi”, 6, (0,0), volume_name=‘image_lowres_time_2’)

</code></pre>
<p>( till there it works great i can see the image was created)</p>
<p>but if i click on it to display it or if i want to see the volume informations, it crashes …</p>
<p>i tried using python to display it to :</p>
<pre><code class="lang-auto">volume_node = slicer.util.getNode(‘image_lowres_time_2’)
slicer.app.layoutManager().sliceWidget(“Red”).sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(volume_node.GetID())
</code></pre>
<p>but it crashes too.</p>
<p>the images at this level of zoom are not that big (1600,1900) and RGB but still, it works when i’m not using it as a function …</p>
<p>Thanks you all in advance if you can find me some help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Best,<br>
Nicolas</p>

---

## Post #2 by @pieper (2023-06-08 15:05 UTC)

<p>Without looking too closely guess would be that there’s a memory management issue between openslide, numpy, and vtk, such that when a python variable goes out of scope the memory is freed but you have dangling pointers from one class or another.  This would be different when you paste the code into the python console where the variables would stay around in the global scope.</p>
<p>You can try saving a global dictionary or similar to hold all the references, or even better you could try to trace the ownership of the memory and make sure to avoid ambiguities over when and where memory should be valid.</p>
<p>If you are still having trouble, try to make the shortest possible code snippet that reproduces the issue.</p>

---

## Post #3 by @Nicolas_Tempier (2023-06-09 08:14 UTC)

<p>Dear Mr Pieper,<br>
thank you for your answer, it seems indeed that it is a memory issue because it crashes only when i try to load large parts of the image…<br>
i’ve increase the swap memory to see wether it makes a difference but it did not.<br>
But i modified the code to use a class for the image and i am pretty impressed because it works…<br>
with the 50000 x 58000 x 1 RGB images …<br>
i made a “clear memory” function in the class but it does not seem to be needed …</p>
<p>if you have an explanation for the difference, that using a class makes in stead of a simple variable and function, i would be glad to hear it.</p>
<p>Best,<br>
Nicolas</p>

---

## Post #4 by @pieper (2023-06-09 13:43 UTC)

<p>It’s hard to say - as I mentioned, you could make an easily reproducible example and maybe someone would be able to help you debug.  Something like <a href="http://sscce.org/">what’s described here</a>.</p>
<p>You could also have a look at this code. <a href="https://github.com/gaoyi/SlicerBigImage" class="inline-onebox">GitHub - gaoyi/SlicerBigImage: Large (GB and above) scale microscopic image computing using 3D Slicer</a></p>

---
