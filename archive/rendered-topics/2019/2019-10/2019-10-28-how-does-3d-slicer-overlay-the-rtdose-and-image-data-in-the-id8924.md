# How does 3D Slicer overlay the RTDOSE and Image data in the correct position?

**Topic ID**: 8924
**Date**: 2019-10-28
**URL**: https://discourse.slicer.org/t/how-does-3d-slicer-overlay-the-rtdose-and-image-data-in-the-correct-position/8924

---

## Post #1 by @Iman_Shokatian (2019-10-28 11:45 UTC)

<p>Hello,</p>
<p>I’m currently an MS student in Medical Physics and I have a great need to be able to overlay an isodose distribution from an RTDOSE file onto a CT image from a .dcm file set.</p>
<p>I’ve managed to extract the image and the dose pixel arrays myself using pydicom and dicom_numpy, but the two arrays are not the same size! So, if I overlay the two together, the dose will not be in the correct position based on what the Elekta Gamma Plan software exported it as.</p>
<p>I’ve played around with slicerrt and it obviously is able to do this even though the arrays are not the same size. However, I think I cannot export the numerical data when using slicerrt…I can only scroll through and view it as an image. What section of the code has the algorithm for overlaying the RTDOSE to an image?</p>
<p>Thank you</p>

---

## Post #3 by @cpinter (2019-10-28 12:49 UTC)

<aside class="quote no-group" data-username="Iman_Shokatian" data-post="1" data-topic="8924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/iman_shokatian/48/5019_2.png" class="avatar"> Iman_Shokatian:</div>
<blockquote>
<p>I’ve managed to extract the image and the dose pixel arrays myself using pydicom and dicom_numpy</p>
</blockquote>
</aside>
<p>Why not just import the DICOM-RT in the DICOM browser and load it? SlicerRT takes care of the geometry and everything else.</p>

---

## Post #4 by @lassoan (2019-10-28 13:35 UTC)

<p>If you only want to use Slicer’s GUI for a few cases and do the rest of your work in batch mode without GUI that i fine, too: you can install any Python packages and run any scripts in Slicer’s Python environment. Slicer even provides a Jupyter kernel so you can access it from Jupyter notebooks.</p>

---

## Post #5 by @Iman_Shokatian (2019-10-30 15:08 UTC)

<p>Dear lassoan and cpinter,</p>
<p>Thank you for your reply,</p>
<p>I am planning to overlay the rt dose file with the CT images to feed both arrays to a neural network; however, when I try to import the rt dose file as dicom array, I will get something like this: 135,98,115.<br>
Additionally, when I import the CT images as an array I will get the following array: 70,512,512<br>
As you can see in these array shapes, neither the slice number nor the image dimension are the same, but I found out that slicerrt has the ability to overlay RT dose file with the CT images in the correct position.<br>
I am writing to ask how this module can correct the position of RT dose files.<br>
I would appreciate it if you could please send me any python script of slicerrt which you know of.</p>
<p>Kind regards,<br>
Iman Shokatian</p>

---

## Post #6 by @Iman_Shokatian (2019-11-03 06:32 UTC)

<p>Hi lassoan,</p>
<p>Did you get any clue about my question that can help me?<br>
I really need to to overlay the rt dose file with the CT images to feed both arrays to a neural network with the same shape, any help from you or others will be appreciated,</p>
<p>Thanks a lot,</p>
<p>Cheers,<br>
Iman</p>

---

## Post #7 by @lassoan (2019-11-04 01:03 UTC)

<p>You can use resample modules in Slicer to resample RTDOSE to have same geometry as the CT image.</p>

---

## Post #8 by @cpinter (2019-11-04 14:41 UTC)

<aside class="quote no-group" data-username="Iman_Shokatian" data-post="5" data-topic="8924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/iman_shokatian/48/5019_2.png" class="avatar"> Iman_Shokatian:</div>
<blockquote>
<p>try to import the rt dose file as dicom array</p>
</blockquote>
</aside>
<p>Can you please describe how you loaded the DICOM-RT dose? Just to make sure that you load it the way it is intended, because then matching overlay should be automatic.<br>
Dimensions are usually very different, so that’s normal.</p>

---

## Post #9 by @Iman_Shokatian (2019-11-04 16:29 UTC)

<p>Hi lassoan,</p>
<p>Thanks for your answer,<br>
I will try resample module and will let you know about the result,</p>
<p>cheers,<br>
Iman</p>

---

## Post #10 by @Iman_Shokatian (2019-11-04 16:32 UTC)

<p>Hi cpinter,</p>
<p>I import ct images and rt dose file into 3dslicer and then export them as nrrd file,<br>
when I read them with pynrrd library I will confront with issue that I mentioned before.</p>
<p>Cheers,<br>
Iman</p>

---

## Post #11 by @cpinter (2019-11-04 17:18 UTC)

<aside class="quote no-group" data-username="Iman_Shokatian" data-post="10" data-topic="8924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/iman_shokatian/48/5019_2.png" class="avatar"> Iman_Shokatian:</div>
<blockquote>
<p>I import ct images and rt dose file into 3dslicer</p>
</blockquote>
</aside>
<p>Please tell us exactly what steps you take to import them. I suspect that you’re not going the correct way.</p>

---

## Post #12 by @Iman_Shokatian (2019-11-04 18:06 UTC)

<p>I used the dicom button on the top left and then in the new window I use import button to import image directory then I click on patient name and select on meta data such as rt dose, rt struc and rt plan file with ct images then I click on load button,after that I click on save button and export ct images and rt dose file as nrrd format, when I open these files with python I will get different array shape</p>

---

## Post #13 by @cpinter (2019-11-04 19:06 UTC)

<p>Thanks! The method of loading seems correct. Before you save it to nrrd, I assume the CT and the dose do not align? Can you make screenshots of the Volume information section in the Volumes module for both images?</p>

---

## Post #14 by @Iman_Shokatian (2019-11-04 19:41 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3706fcdfade4172904ef0bbced6a2aa4dc42dd6.png" alt="RD" data-base62-sha1="rSW058bpPsUhGj7fBpMuCUicn9c" width="529" height="363"></p>

---

## Post #15 by @cpinter (2019-11-04 23:45 UTC)

<p>Thanks! Just trying to double check they don’t overlap. I created two volumes with exactly the same geometry as what you show in the screenshots, and they don’t match exactly, although the dose volume is inside the CT, which may be valid:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96026aac90eee03116294bea27c551b4507a0460.jpeg" data-download-href="/uploads/short-url/lp2NuIyyExSfqALqaKFSAJmW6KQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96026aac90eee03116294bea27c551b4507a0460_2_454x500.jpeg" alt="image" data-base62-sha1="lp2NuIyyExSfqALqaKFSAJmW6KQ" width="454" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96026aac90eee03116294bea27c551b4507a0460_2_454x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96026aac90eee03116294bea27c551b4507a0460_2_681x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96026aac90eee03116294bea27c551b4507a0460.jpeg 2x" data-dominant-color="443639"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">707×777 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is quite unusual if you exported them from a treatment planning system. At this point (if the dose is indeed smaller than what it’s supposed to be) it is up to you to manually fix the dose volume’s geometry so that it matches the CT.</p>
<p>You can use the Resample Scalar Volumes module (the same one I used to create these two volumes above).</p>

---

## Post #17 by @Iman_Shokatian (2019-11-05 02:46 UTC)

<p>Thanks a lot lassoan,</p>
<p>I got the same array shape via resample module, but there is another problem, when I compared new rt dose file with the original, I noticed that there is difference between resample module output and the original file, it seems that they are not the same,</p>
<p>how can I fix that problem?!</p>
<p>Cheers,<br>
Iman</p>

---

## Post #18 by @Iman_Shokatian (2019-11-05 02:48 UTC)

<p>Thanks a lot!</p>
<p>I will check that and I will inform you the result,</p>
<p>Cheers,<br>
Iman</p>

---

## Post #19 by @lassoan (2019-11-05 03:07 UTC)

<aside class="quote no-group" data-username="Iman_Shokatian" data-post="17" data-topic="8924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/iman_shokatian/48/5019_2.png" class="avatar"> Iman_Shokatian:</div>
<blockquote>
<p>I got the same array shape via resample module, but there is another problem, when I compared new rt dose file with the original, I noticed that there is difference between resample module output and the original file, it seems that they are not the same</p>
</blockquote>
</aside>
<p>Values in the original and resampled dose volumes cannot be the same as you resampled its voxels. If that’s a problem then instead you can resample the CT volume using the dose volume as reference.</p>

---

## Post #20 by @44REAM (2020-08-03 18:57 UTC)

<p>I got the same problem. I try to export RTDOSE and CT with python script but the array of the two are not the same size. I also check by manual export and it not work. Can you explain more about “Resample Scalar Volumes module”?, I check in “Python scripting doc” and got no detaill. This is My script.</p>
<p>Thank you.</p>
<pre><code>loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

from DICOMLib import DICOMUtils

def pathFromNode(node):

    storageNode=node.GetStorageNode()

    if storageNode is not None: # loaded via drag-drop

        filepath=storageNode.GetFullNameFromFileName()

    else: # loaded via DICOM browser

        instanceUIDs=node.GetAttribute('DICOM.instanceUIDs').split()

        filepath=slicer.dicomDatabase.fileForInstance(instUids[0])

    return filepath

with DICOMUtils.TemporaryDICOMDatabase() as db:

    DICOMUtils.importDicom(dicomDataDir, db)

    patientUIDs = db.patients()

    for patientUID in patientUIDs:

        studyList=db.studiesForPatient(patientUID)

        for study in studyList:

            node = slicer.util.getNode(study)

            slicer.util.saveNode(node , '/tmp/output.nrrd')</code></pre>

---

## Post #21 by @lassoan (2020-08-03 19:21 UTC)

<p>You can use " Resample Scalar/Vector/DWI Volume" to resample a volume using another volume’s geometry.</p>
<p>You can get the list of parameters as described in “<em>Get list of parameter names</em>” section on this page:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---

## Post #22 by @44REAM (2020-08-04 18:08 UTC)

<p>Thank a lot , I use " Resample Scalar/Vector/DWI Volume" module in slicer and it work perfectly. But how I can do this in python script?</p>

---

## Post #23 by @lassoan (2020-08-04 18:56 UTC)

<p>See this page for information about how to run CLI module from a Python script: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---

## Post #24 by @44REAM (2020-08-05 07:11 UTC)

<p>It work now, thank you</p>

---

## Post #25 by @strider_hunter (2023-09-18 12:54 UTC)

<p>Posting here a script I made using pydicom and SimpleITK by inputting CT and RTDOSE .dcms. <a href="https://i.imgur.com/DLVjhJF.png" rel="noopener nofollow ugc">Sample Output</a></p>
<pre><code class="lang-python">"""
Step 1 - Read Dose and CT .dcm files
Step 2 - Resample dose to CT
Step 2.1 - Shift dose to match CT
Step 3 - Plot
"""
import pdb
import pydicom
import traceback
import numpy as np
import SimpleITK as sitk
from pathlib import Path

if __name__ == "__main__":

    try:
        
        pathCT     = Path('...', '{CTFolder}')
        pathDoseA5 = Path('...', '{RTDOSE}.dcm')
        sliceId = 94 # [77, 94, 115]

        if Path(pathCT).exists() and Path(pathDoseA5).exists():
            
            doseArray, ctArray     = [], []
            doseSpacing, ctSpacing = [], []
            doseImagePositionPatient, ctImagePositionPatientMin, ctImagePositionPatientMax = [], [], []

            # Step 1.1 - Read Dose .dcm
            try:
                dsDose      = pydicom.dcmread(pathDoseA5)
                doseArray   = dsDose.pixel_array * dsDose.DoseGridScaling
                doseSpacing = [float(each) for each in dsDose.PixelSpacing] + [float(dsDose.SliceThickness)]
                assert doseArray.shape[0] == float(dsDose.NumberOfFrames)
                doseImagePositionPatient = [float(each) for each in dsDose.ImagePositionPatient]
            except:
                traceback.print_exc()
                pdb.set_trace()
            
            # Step 1.2 - Read CT .dcms
            try:
                dsCTs = []
                for pathCTDicom in Path(pathCT).iterdir(): dsCTs.append(pydicom.dcmread(pathCTDicom))
                ctSpacing = [float(each) for each in dsCTs[0].PixelSpacing] + [float(dsCTs[0].SliceThickness)]
                dsCTs.sort(key=lambda x: x.InstanceNumber)
                ctImagePositionPatientMin = [float(each) for each in dsCTs[0].ImagePositionPatient]
                ctImagePositionPatientMax = [float(each) for each in dsCTs[-1].ImagePositionPatient]
                for dsCT in dsCTs:
                    ctArray.append(dsCT.pixel_array * dsCT.RescaleSlope + dsCT.RescaleIntercept)
                ctArray = np.array(ctArray[::-1])
            except:
                traceback.print_exc()
                pdb.set_trace()
            
            if len(doseArray) and len(ctArray):
                print ('')
                print (f' - doseArray  : {doseArray.shape} | ctArray: {ctArray.shape} ') # [Slices,H,W]
                print (f' ---- Dose Max: {np.max(doseArray)} | Dose Min: {np.min(doseArray)} ')
                print (f' - doseSpacing: {doseSpacing} | ctSpacing: {ctSpacing} ') # [H,W,Slices]
                print (f' - doseImagePositionPatient: {doseImagePositionPatient} ')
                print (f' - ctImagePositionPatientMin: {ctImagePositionPatientMin}, ctImagePositionPatientMax: {ctImagePositionPatientMax}')
                print ('')
                
                # Step 2 - Resample dose to CT
                doseImage = sitk.GetImageFromArray(doseArray)
                doseImage.SetSpacing(doseSpacing)
                resampler = sitk.ResampleImageFilter()
                resampler.SetOutputSpacing(ctSpacing)
                resampler.SetSize(ctArray.shape[::-1]) # SimpleITK convention: [H,W,Slices], numpy convention: [Slices,H,W]
                resampled_image = resampler.Execute(doseImage)
                doseArrayResampled = sitk.GetArrayFromImage(resampled_image)
                print (f' - doseArrayResampled  : {doseArrayResampled.shape} | ctArray: {ctArray.shape} ')

                # Step 2.1 - Shift dose to match CT
                dx, dy, dz = ((np.array(doseImagePositionPatient) - np.array(ctImagePositionPatientMax)) / np.array(ctSpacing)).astype(int)
                print (f' - dx, dy, dz: {dx, dy, dz} ')
                from scipy.ndimage.interpolation import shift
                doseArrayResampled = shift(doseArrayResampled, (dz, dy, dx))
                
                # Step 3 - Plot
                import matplotlib.pyplot as plt
                import matplotlib.colors as mcolors
                boundaries = [0      , 13.56       , 27.12        , 37.97        , 43.40      , 48.82    , 51.54     , 54.25   , 58.05        , 66.50        , 70.00      , 74.90]
                rgbColors = np.array([[0,0,0,0], [192,192,192,128], [192,192,255,128], [128,128,255,128], [64,64,192,128], [0,0,128,128], [0,255,0,128], [0,128,0,128], [255,255,255,128], [255,255,128,128], [255,192,0,128], [255,0,0,128]])/255.0
                cmap = mcolors.ListedColormap(rgbColors)
                norm = mcolors.BoundaryNorm(boundaries, cmap.N, clip=True)

                sliceDoseA = doseArrayResampled[sliceId-1]
                sliceCTA   = ctArray[sliceId-1]
                sliceDoseB = doseArrayResampled[sliceId]
                sliceCTB   = ctArray[sliceId]
                sliceDoseC = doseArrayResampled[sliceId+1]
                sliceCTC   = ctArray[sliceId+1]

                X = np.linspace(0, sliceDoseA.shape[1]-1, sliceDoseA.shape[1])
                Y = np.linspace(0, sliceDoseA.shape[0]-1, sliceDoseA.shape[0])
                X, Y = np.meshgrid(X, Y)
                
                f,axarr = plt.subplots(1,3)
                axarr[0].imshow(sliceCTA, cmap='gray', interpolation='bicubic')
                axarr[0].contourf(X,Y,sliceDoseA, levels=boundaries, colors=rgbColors)
                axarr[0].set_title(f'Slice={sliceId}')
                
                axarr[1].imshow(sliceCTB, cmap='gray', interpolation='bicubic')
                axarr[1].contourf(X,Y,sliceDoseB, levels=boundaries, colors=rgbColors)
                axarr[1].set_title(f'Slice={sliceId+1}')

                axarr[2].imshow(sliceCTC, cmap='gray', interpolation='bicubic')
                doseIm = axarr[2].contourf(X,Y,sliceDoseC, levels=boundaries, colors=rgbColors)
                axarr[2].set_title(f'Slice={sliceId+2}')
                
                from mpl_toolkits.axes_grid1 import make_axes_locatable
                divider = make_axes_locatable(axarr[2])
                cax = divider.append_axes("right", size="5%", pad=0.05)
                f.colorbar(doseIm, cax=cax, boundaries=boundaries, norm=norm, ticks=boundaries)

                plt.show(block=False)
                pdb.set_trace()

        else:
            print (f' - ERROR: pathCT: {Path(pathCT).exists()} | pathDoseA5: {Path(pathDoseA5).exists()} ')
            pdb.set_trace()
    
    except:
        traceback.print_exc()
        pdb.set_trace()
</code></pre>

---
