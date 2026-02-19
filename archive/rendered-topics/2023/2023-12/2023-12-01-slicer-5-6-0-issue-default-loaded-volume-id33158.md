---
topic_id: 33158
title: "Slicer 5 6 0 Issue Default Loaded Volume"
date: 2023-12-01
url: https://discourse.slicer.org/t/33158
---

# Slicer 5.6.0 issue default loaded volume

**Topic ID**: 33158
**Date**: 2023-12-01
**URL**: https://discourse.slicer.org/t/slicer-5-6-0-issue-default-loaded-volume/33158

---

## Post #1 by @Nicolas_Tempier (2023-12-01 10:26 UTC)

<p>Dear Slicer community,<br>
i switched to 3D Slicer 5.6.0 and so reinstalled the python modules that i use, for exemple openslide.<br>
But after “coding a bit” (ill post at the end of this post what i mean by that), i restarded 3D slicer and was suprised to see this already in my python console with a loaded volume :</p>
<pre><code class="lang-auto">Level: 0, Width: 105728, Height: 77952, Downsample Factor: 1.0, Magnification: 40.0x, Resolution: 0.000442 mm/pixel
Level: 1, Width: 52864, Height: 38976, Downsample Factor: 2.0, Magnification: 20.0x, Resolution: 0.000884 mm/pixel
Level: 2, Width: 26432, Height: 19488, Downsample Factor: 4.0, Magnification: 10.0x, Resolution: 0.001768 mm/pixel
Level: 3, Width: 13216, Height: 9744, Downsample Factor: 8.0, Magnification: 5.0x, Resolution: 0.003536 mm/pixel
Level: 4, Width: 6608, Height: 4872, Downsample Factor: 16.0, Magnification: 2.5x, Resolution: 0.007072 mm/pixel
Level: 5, Width: 3304, Height: 2436, Downsample Factor: 32.0, Magnification: 1.25x, Resolution: 0.014144 mm/pixel
Level: 6, Width: 1652, Height: 1218, Downsample Factor: 64.0, Magnification: 0.625x, Resolution: 0.028288 mm/pixel
Level: 7, Width: 826, Height: 609, Downsample Factor: 128.0, Magnification: 0.3125x, Resolution: 0.056576 mm/pixel
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/nicolas.tempier/Slicer-5.6.0-linux-amd64/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/nicolas.tempier/slicer_modules/H3H/Cryoslice_loader/openslide_slicer.py", line 176, in &lt;module&gt;
    image_fullsize_level6.load_image()
  File "/home/nicolas.tempier/slicer_modules/H3H/Cryoslice_loader/openslide_slicer.py", line 66, in load_image
    voxel_spacing = tuple(i * return_vowel_spacing_from_level_in_mm(self.image_path, self.level) for i in base_voxel_spacing)
  File "/home/nicolas.tempier/slicer_modules/H3H/Cryoslice_loader/openslide_slicer.py", line 66, in &lt;genexpr&gt;
    voxel_spacing = tuple(i * return_vowel_spacing_from_level_in_mm(self.image_path, self.level) for i in base_voxel_spacing)
NameError: name 'return_vowel_spacing_from_level_in_mm' is not defined
[Qt] libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
[Qt] libpng warning: iCCP: known incorrect sRGB profile
[Qt] loadSourceAsModule - Failed to load file "/home/nicolas.tempier/slicer_modules/H3H/Cryoslice_loader/openslide_slicer.py"  as module "openslide_slicer" !
[Qt] Fail to instantiate module  "openslide_slicer"
[Qt] The following modules failed to be instantiated:
[Qt]    openslide_slicer
Loading Slicer RC file [/home/nicolas.tempier/.slicerrc.py]
</code></pre>
<p>how do i get rid of this without having to reinstall 3D slicer everytime i restart it please ?</p>
<p>PS : to install openslide i “had” to mannually copy paste<br>
“openslide” and “openslide_python-1.2.0.dist-info” to sites-packages and that could be a reason but I never managed to install it otherwise.</p>
<p>thank you in advance for your help,<br>
best,<br>
Nicolas</p>
<p>PS 2 :</p>
<p>here is what i executed before restarting :</p>
<pre><code class="lang-auto">import slicer
import numpy as np
import vtk
from vtk.util.vtkImageImportFromArray import vtkImageImportFromArray
from vtk.util import numpy_support
from PIL import Image
import timeit
import gc
import openslide

class ImageLoader:
    def __init__(self, image_path, level, size=None, somewhere_coordinates=(0, 0), volume_name='image_loaded'):
        self.image_path = image_path
        self.level = level
        self.size = size
        self.somewhere_coordinates = somewhere_coordinates
        self.volume_name = volume_name

    def load_image(self):
        # Charger l'image NDPI
        self.image_ndpi = openslide.OpenSlide(self.image_path)

        # Obtenir le facteur de sous-échantillonnage du niveau
        self.downsample_factor = self.image_ndpi.level_downsamples[self.level]

        # Convertir les coordonnées du niveau cible en coordonnées du niveau 0
        somewhere_coordinates_level_0 = (int(self.somewhere_coordinates[1] * self.downsample_factor),
                                        int(self.somewhere_coordinates[0] * self.downsample_factor))

        # Sélectionner résolution
        # print(f"Level selectionné : {self.level}")
        if self.size is None:
            self.size = self.image_ndpi.level_dimensions[self.level]

        # Lire l'image en utilisant les coordonnées du niveau 0
        self.image_matrix = self.image_ndpi.read_region(somewhere_coordinates_level_0, self.level, self.size)

        # Convertir l'image en un tableau NumPy et créer un objet VTK Image
        self.image_array = np.array(self.image_matrix)[:, :, :3] 
        self.image_array = np.swapaxes(self.image_array, 0, 1)
        self.image_array = np.ascontiguousarray(self.image_array, dtype=np.uint8)

        # Créer une image VTK avec 3 dimensions spatiales et 3 dimensions d'intensité pour les canaux RGB
        self.vtk_image_rgb = vtk.vtkImageData()
        self.vtk_image_rgb.SetDimensions(self.image_array.shape[1], self.image_array.shape[0], 1)
        self.vtk_image_rgb.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 3)
        self.vtk_image_rgb.SetSpacing(1, 1, 1)

        # Convertir le tableau NumPy en une liste d'octets
        self.image_list = self.image_array.flatten()

        # Convertir la liste d'octets en un tableau VTK
        self.vtk_array = numpy_support.numpy_to_vtk(num_array=self.image_list, deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)

        # Associer le tableau VTK à un vtkUnsignedCharArray
        self.rgb_array_vtk = vtk.vtkUnsignedCharArray()
        self.rgb_array_vtk.SetNumberOfComponents(3)
        self.rgb_array_vtk.SetArray(self.vtk_array, len(self.image_list), 1)

        # Associer le tableau vtkUnsignedCharArray aux scalaires de l'image VTK
        self.vtk_image_rgb.GetPointData().SetScalars(self.rgb_array_vtk)

        # Ajouter l'image à un nœud de volume dans 3D Slicer
        self.volume_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLVectorVolumeNode', self.volume_name)    
        base_voxel_spacing = (1, 1, 1)  
        voxel_spacing = tuple(i * return_vowel_spacing_from_level_in_mm(self.image_path, self.level) for i in base_voxel_spacing)

        self.volume_node.SetSpacing(voxel_spacing)
        self.volume_node.SetAndObserveImageData(self.vtk_image_rgb)
        slicer.app.applicationLogic().PropagateVolumeSelection(0)

        # remettre le volume au bon endroit si somewhere_coordinates n'est pas (0,0)
        if self.somewhere_coordinates != (0,0):     
            self.volume_node.SetOrigin(self.somewhere_coordinates[0]*voxel_spacing[0],self.somewhere_coordinates[1]*voxel_spacing[0],0)

    def remove_node(self):
        node = slicer.mrmlScene.GetFirstNodeByName(self.volume_name)
        if node is not None:
            slicer.mrmlScene.RemoveNode(node)


    def return_vowel_spacing_from_level_in_mm(image_path, level):
        # Charger l'image NDPI
        slide = openslide.OpenSlide(image_path)

        # Suppose que le grossissement au niveau 0 est de 40x
        magnification_at_level_0 = 40

        # Résolution au niveau 0 en nm/pixel
        resolution_at_level_0_nm_per_pixel = 442
        resolution_at_target_level_mm_per_pixel = resolution_at_level_0_nm_per_pixel/1e6 * slide.level_downsamples[level]
        return resolution_at_target_level_mm_per_pixel
        

    def clear_memory(self):
        # Libérer la mémoire des objets
        # del self.image_ndpi
        # del self.image_matrix
        # del self.image_array
        # del self.image_list
        del self.vtk_array
        del self.rgb_array_vtk
        gc.collect()

def display_downsample_factors(image_path):
    # Charger l'image NDPI
    slide = openslide.OpenSlide(image_path)

    # Suppose que le grossissement au niveau 0 est de 40x
    magnification_at_level_0 = 40

    # Résolution au niveau 0 en nm/pixel
    resolution_at_level_0_nm_per_pixel = 442

    for i in range(slide.level_count):
        width, height = slide.level_dimensions[i]
        downsample = slide.level_downsamples[i]
        magnification = magnification_at_level_0 / downsample
        # Convertir la résolution de nm/pixel à mm/pixel
        resolution_at_level_mm_per_pixel = (resolution_at_level_0_nm_per_pixel * downsample) / 1e6
        print(f'Level: {i}, Width: {width}, Height: {height}, Downsample Factor: {downsample}, Magnification: {magnification}x, Resolution: {resolution_at_level_mm_per_pixel} mm/pixel')
       
def set_voxel_spacing(volume_name, voxel_spacing):
    volume_node = slicer.util.getNode(volume_name)
    if volume_node is not None:
        volume_node.SetSpacing(voxel_spacing)
 
def display_image_levels_and_sizes(image_path):
    # Charger l'image NDPI
    image_ndpi = openslide.OpenSlide(image_path)

    # Obtenir le nombre de niveaux de l'image
    num_levels = len(image_ndpi.level_dimensions)

    # Afficher les niveaux de grossissement et les tailles d'image correspondantes
    print("Niveau de grossissement et tailles d'image correspondantes :")
    for i in range(num_levels):
        level_dimensions = image_ndpi.level_dimensions[i]
        downsample_factor = image_ndpi.level_downsamples[i]
        print(f"Niveau {i}: facteur de sous-échantillonnage = {downsample_factor}, dimensions = {level_dimensions}")

def ask_for_coordinates():
    user_input = input("Entrez les coordonnées x et y du premier point, séparées par une virgule : ")
    x1, y1 = map(int, user_input.split(','))
    user_input = input("Entrez les coordonnées x et y du deuxième point, séparées par une virgule : ")
    x2, y2 = map(int, user_input.split(','))
    return (x1, y1), (x2, y2)

def get_corresponding_coords(image_path, low_res_level, high_res_level, x, y):
    slide = openslide.OpenSlide(image_path)

    # Récupère le facteur de sous-échantillonnage pour chaque niveau
    low_res_downsample = slide.level_downsamples[low_res_level]
    high_res_downsample = slide.level_downsamples[high_res_level]

    # Convertit les coordonnées au niveau de résolution basse en coordonnées au niveau 0
    x_at_level_0 = x * low_res_downsample
    y_at_level_0 = y * low_res_downsample

    # Convertit les coordonnées au niveau 0 en coordonnées au niveau de résolution haute
    x_at_high_res_level = x_at_level_0 / high_res_downsample
    y_at_high_res_level = y_at_level_0 / high_res_downsample

    return x_at_high_res_level, y_at_high_res_level



# setup
image_path = "/network/lustre/iss02/lau-karachi/data_raw/Human/HYPOTHALAMUS-SANO/Homme/H3h/tests_ChAT/ChAT_Tests/NicolasTempier/H3h 440 ChAT_Test - 2023-11-28 20.28.02.ndpi"
display_downsample_factors(image_path)

# image_fullsize_level7.remove_node()  # remove the node when done

# on veut charger l'image au level 6 taille entiere 
image_fullsize_level6 = ImageLoader(image_path, 6, somewhere_coordinates=(0, 0), volume_name='image_fullsize_level6')
image_fullsize_level6.load_image()

</code></pre>

---

## Post #2 by @jamesobutler (2023-12-02 04:39 UTC)

<p>The error message comes from your code and describing an issue with <code>return_vowel_spacing_from_level_in_mm</code>. Based on your indentation you have created it as a method of the class <code>ImageLoader</code>, but you also haven’t defined <code>self</code> as the first argument like you have done for the other methods in the class.</p>

---
