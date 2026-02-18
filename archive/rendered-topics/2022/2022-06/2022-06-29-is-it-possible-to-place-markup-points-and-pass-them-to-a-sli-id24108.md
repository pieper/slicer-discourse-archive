# Is it possible to place markup points and pass them to a slicer executable module I have created?

**Topic ID**: 24108
**Date**: 2022-06-29
**URL**: https://discourse.slicer.org/t/is-it-possible-to-place-markup-points-and-pass-them-to-a-slicer-executable-module-i-have-created/24108

---

## Post #1 by @Kevin.Kn (2022-06-29 20:06 UTC)

<p>I currently have been using ITK to generate automated segmentations using command line inputs that include seed point regions of interest, to create a more efficient version of outdated matlab code that my lab is using.</p>
<p>I have also been messing around with the slicer execution models and ITK, and realized that I could create an all encompassing package for this segmentation script. But, I am stuck on how (or if it is possible) to get markup fiducials as variables to my scripts.</p>
<p>I have experience with SEM and basic usage using filters and image processing pipelines using ITK, but getting the information out of slicer for these markups is something I have zero experience with.</p>
<p>Any help or suggestions would be greatly appreciated.</p>

---

## Post #2 by @mau_igna_06 (2022-06-30 00:01 UTC)

<p>I think you would need to search on how to create a Python Scripted Module (or c++ if it corresponds)</p>

---

## Post #3 by @Kevin.Kn (2022-06-30 02:22 UTC)

<p>I did a little bit of searching around and I found some vtk python examples that somewhat resemble what I would like to do in c++.</p>
<p>I am currently building vtk and will see if I can get it to work as a c++ executable through slicer. From what I saw, as long as I know the name of the fiducials (which the user can edit before running the script), I should be able to pull those from slicer when hitting ‘run’ using vtk in some way.</p>
<p>Ill post an update If I find something that works well.</p>

---

## Post #4 by @pieper (2022-06-30 18:46 UTC)

<p>If you have a look at the Execution Model Tour module you can try multiple seeds.  You need to select two volumes and then make a fiducial list with multiple points and the clicking apply creates this command line.</p>
<pre><code class="lang-auto">/Applications/Slicer-5.0.2.app/Contents/lib/Slicer-5.0/cli-modules/ExecutionModelTour --returnparameterfile /private/var/folders/cn/kmqx4dm17gx4hrllqrmnkbp00000gn/T/Slicer-pieper/75803_gmSXgOTLvY.params --integer 30 --double 30 -f 1.3,2,-14 --string_vector foo,bar,foobar --enumeration Bill --boolean1 --directory1 . --seed 70.5805,36.6095,0 --seed 31.6623,30.6728,0 --seed 41.5567,2.30871,0 --seed 112.797,-57.058,0 --seed 130.607,-34.6306,0 --seed 155.013,-4.2876,0 --seed 158.311,15.5013,0 --seed 149.736,19.4591,0 --seed 131.266,20.7784,0 /private/var/folders/cn/kmqx4dm17gx4hrllqrmnkbp00000gn/T/Slicer-pieper/HFIAD_vtkMRMLScalarVolumeNodeB.nrrd /private/var/folders/cn/kmqx4dm17gx4hrllqrmnkbp00000gn/T/Slicer-pieper/HFIAD_vtkMRMLScalarVolumeNodeB.nrrd 
</code></pre>

---

## Post #5 by @Kevin.Kn (2022-06-30 20:36 UTC)

<p>Thank you, Ill take a look at that. Unfortunately something happened to my machine so that I cannot build my projects properly, but I will look into this when It that build issue solved.</p>
<p>I took a look at ways to implement using the built in python package with slicer, and found the ways to get the markup node physical positioning information and the volume file information from a loaded node. With the nodes and that file name I can just create a sitk implementation of my script to run directly through the slicer python interpreter. The only adjustment that I need to make is converting the RAS coordinates to LPS for itk.</p>
<p>The added benefit of doing this through python is that other lab members already have access to slicer and would not need to go through a slow process of getting our technology services to install cmake and other tools I use. slicer already has access or can install the packages needed without administrator rights.</p>

---

## Post #6 by @Kevin.Kn (2022-06-30 20:53 UTC)

<p>Just for reference this is the start to the python script after figuring a bit out about the python interpreter in slicer. Its a little rough and making assumptions on use case.</p>
<pre><code class="lang-auto">#####################################
## Get Markup Physical Coordinates ##
#####################################

NoduleNode=slicer.util.getNode("Nod_Seeds")
BackgroundNode=slicer.util.getNode("BG_Seeds")

NoduleSeedLocations=slicer.util.arrayFromMarkupsControlPoints(NoduleNode)
BackgroundSeedLocations=slicer.util.arrayFromMarkupsControlPoints(BackgroundNode)

## Example output of NoduleSeedLocations with 4 randomly placed markup points in RAS physical space
## [ [ 10.1329359   24.94261144   0.        ]
##   [-53.78250591   9.35347929   0.        ]
##   [ 30.39880769   1.55891321   0.        ]
##   [ 89.30380263   0.703125   -55.56418023]]

## The same can be done with the background points of interest.
## Can now use these arrays of physical points later with sITK, but need to transform to LPS space




#####################################
## Get Filename from volume node   ##
#####################################

VolumeNodes = slicer.util.getNodesByClass("vtkMRMLModelVolumeNode")
ImageNode= VolumeNodes[0]
StorageNode= ImageNode.GetStorageNode()
ImageFilename = StorageNode.GetFileName()
print(ImageFilename)
# ImageFilename is pathtofile/TestImage.nii.gz

# I now have the image filename to load the image for processing in sitk, and the corresponding markup points of interest to input to an algorithm.


</code></pre>

---
