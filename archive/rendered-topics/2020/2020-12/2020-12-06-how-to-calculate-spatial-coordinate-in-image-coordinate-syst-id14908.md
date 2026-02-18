# How to calculate spatial coordinate in Image coordinate system by having spatial coordinate in RAS coordiane ststem?

**Topic ID**: 14908
**Date**: 2020-12-06
**URL**: https://discourse.slicer.org/t/how-to-calculate-spatial-coordinate-in-image-coordinate-system-by-having-spatial-coordinate-in-ras-coordiane-ststem/14908

---

## Post #1 by @shahrokh (2020-12-06 10:51 UTC)

<p>Hello Dear Developers and Users</p>
<p>I have a number of points (approximately 48000 points). I think that their spatial coordinates are in <strong>RAS coordinate system</strong>, for example:</p>
<p><strong>-146.4141082763672    66.66109466552734    -923.0950927734375</strong></p>
<p>Now I want to have the coordinates of these points in the <strong>Image coordinate system</strong>.</p>
<p>For example, I have shown one of these points in the following figure in the center of sphere (red color).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86a5edc61fbb36ed49661415246ebefd645e776a.jpeg" data-download-href="/uploads/short-url/jd9tShGuDS6LKrvymYjf6MvcbUu.jpeg?dl=1" title="screen2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a5edc61fbb36ed49661415246ebefd645e776a_2_690x388.jpeg" alt="screen2" data-base62-sha1="jd9tShGuDS6LKrvymYjf6MvcbUu" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a5edc61fbb36ed49661415246ebefd645e776a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a5edc61fbb36ed49661415246ebefd645e776a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a5edc61fbb36ed49661415246ebefd645e776a_2_1380x776.jpeg 2x" data-dominant-color="9E9EAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen2</span><span class="informations">1920×1080 414 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to have a row, column, and slice that is spatially positioned at this point in Python as shown in the cursor location:<br>
<strong>B CT_wholeLung (81, 294, 11)</strong></p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @timeanddoctor (2020-12-06 11:21 UTC)

<p>I think the simplest method is to create a makerup with you data and then open ‘show slice intersections’ if you just tend to get a slice window.</p>

---

## Post #3 by @shahrokh (2020-12-06 11:36 UTC)

<p>Hello Dear Li<br>
Thank you for your help.</p>
<p>Due to the large number of points (48000 points), I think I should use the functions in Python modules such as ITK to convert RAS to IJK.</p>

---

## Post #4 by @timeanddoctor (2020-12-06 12:27 UTC)

<p>sorry,<br>
ras0=[0,0,0]<br>
and you could get the coordinate values based on the obove method: d=[x,y,x]</p>
<p>if the image spacing: sX,sY,sZ=0.582,0.582,0.625<br>
then CX,CY,CZ=1/sX,1/sY,1/sZ</p>
<p>finally:<br>
if the ras=[a,b,c]<br>
then:D=[x+a<em>CX,y+b</em>CY,z+c*CZ]</p>

---

## Post #5 by @timeanddoctor (2020-12-06 12:28 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4495f4e7e33cfbb29ed2a778f7b7db9c2f190ed5.jpeg" data-download-href="/uploads/short-url/9MJKpQDo6lx5qpYg3BPibjxsjNr.jpeg?dl=1" title="492208973" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4495f4e7e33cfbb29ed2a778f7b7db9c2f190ed5_2_375x500.jpeg" alt="492208973" data-base62-sha1="9MJKpQDo6lx5qpYg3BPibjxsjNr" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4495f4e7e33cfbb29ed2a778f7b7db9c2f190ed5_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4495f4e7e33cfbb29ed2a778f7b7db9c2f190ed5_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4495f4e7e33cfbb29ed2a778f7b7db9c2f190ed5_2_750x1000.jpeg 2x" data-dominant-color="828599"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">492208973</span><span class="informations">1080×1440 85.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @timeanddoctor (2020-12-06 12:29 UTC)

<p>and you should use int() for the finally valume</p>

---

## Post #7 by @lassoan (2020-12-06 13:53 UTC)

<p>The beauty of homogeneous coordinates is that you transform all your points from RAS to IJK coordinate system by putting your points into a 4xN matrix and multiply it from the left using  IJKToRAS matrix.</p>
<p>Normally you store this many points in a model node and then apply all kinds of operations on them in bulk. Where are your points coming from? What do you plan to do with them?</p>

---

## Post #8 by @shahrokh (2020-12-09 15:02 UTC)

<p><strong>Hello</strong><br>
<strong>Dear Andras and Li</strong></p>
<p>Thank you very much for your guidance and sorry for the late reply.<br>
I want to use the particles system resulting from <strong>Chest Imaging Platform</strong> (<strong>CIP</strong>) in classification based on particles properties. These properties can indicate the features of the blood vessels of the lungs.</p>
<p>The output of CIP is in <strong>vtk</strong> format, which contains the following properties for each particle.<br>
1- scale<br>
2- val<br>
3- eigenvalue<br>
4- eigenvector<br>
5- Hessian elements<br>
6- Spatial coordinates</p>
<p>Comment: At first, I convert <strong>vtk</strong> formt to <strong>vtp</strong> format.<br>
I want to transfer this information (particle properties) from the vtp (xml structure) to 3D matrices (the same size as the CT image matrix) or tensors. The end result will be, for example, files with the following names:<br>
scaleMatrix.nrrd , valMatrix.nrrd, eignevalueMatrix.nrrd,  eignevectorTensor.nrrd and …</p>
<p>These files must contain matrices or tensors in which the voxels, in the particle position, have values such as scale, val, eigenvalue, and … .<br>
I think that the coordinate system of CT images in nrrd format is the same as the coordinate system in ITK that is <strong>LPS</strong>. Is it true?<br>
Accordingly, I used the <em>space origin</em> item in the <em>header</em> section of the CT.nrrd file to create a <strong>transform matrix</strong>.</p>
<p>I enter the following commands:</p>
<pre><code>sn@MP:~$ ipython
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: # Load modules 
   ...: import numpy as np 
   ...: import nrrd 
   ...: import vtk  
   ...: import os                                                                                                                                                                                           

In [2]: # Load CT (nrrd file) 
   ...: filenameCT = '/home/sn/testCIP/result1/WholeLung01/wholeLung/CT_wholeLung.nrrd' 
   ...: CT, headerCT = nrrd.read(filenameCT) 
   ...: itemsHeaderCT = list(headerCT.items()) 
   ...: print("items in CT header")  
   ...: for i in range(len(itemsHeaderCT)):  
   ...:  print(i, itemsHeaderCT[i][0], itemsHeaderCT[3][1]) 
   ...:                                                                                                                                                                                                     
items in CT header
0 type [509 347 629]
1 dimension [509 347 629]
2 space [509 347 629]
3 sizes [509 347 629]
4 space directions [509 347 629]
5 kinds [509 347 629]
6 endian [509 347 629]
7 encoding [509 347 629]
8 space origin [509 347 629]

In [3]: print("items header of nnd file CT",  itemsHeaderCT[3])                                                                                                                                             
items header of nnd file CT ('sizes', array([509, 347, 629]))

In [4]: scaleMatrix = np.zeros((itemsHeaderCT[3][1]))                                                                                                                                                       

In [5]: print("matrix size scaleMatrix", scaleMatrix.shape)                                                                                                                                                 
matrix size scaleMatrix (509, 347, 629)

In [6]: print("matrix size CT:", CT.shape)                                                                                                                                                                  
matrix size CT: (509, 347, 629)

In [7]: # Load particles system (vtp file) 
   ...: filenameParticles = "/home/sn/testCIP/result1/WholeLung01/wholeLungVesselParticles.vtp"; 
   ...: readerDataVTP = vtk.vtkXMLPolyDataReader(); 
   ...: readerDataVTP.SetFileName(filenameParticles);  
   ...: readerDataVTP.Update();  
   ...: polydata = readerDataVTP.GetOutput();                                                                                                                                                               

In [8]: # Get particles coordinate 
   ...: particlesCoordinates = polydata.GetPoints();  
   ...: numberOfParticles = readerDataVTP.GetNumberOfPoints();  
   ...: print("number of particles:", numberOfParticles) 
   ...: print("Type of particles coordinates in vtp file: ", type(particlesCoordinates.GetPoint(0)))                                                                                                        
number of particles: 48425
Type of particles coordinates in vtp file:  &lt;class 'tuple'&gt;

In [9]: # Convert and get first particle coordinate from tuple to numpy array 
   ...: particleCoordinates = np.asarray(particlesCoordinates.GetPoint(0)) 
   ...: print("The coordinates of first particle: ", particleCoordinates)                                                                                                                                   
The coordinates of first particle:  [-146.41410828   66.66109467 -923.09509277]

In [10]: # Convert and get end particle coordinate from tuple to numpy array 
    ...: particleCoordinates = np.asarray(particlesCoordinates.GetPoint(numberOfParticles-1)) 
    ...: print("The coordinates of ",  numberOfParticles, " particle: ", particleCoordinates)                                                                                                               
The coordinates of  48425  particle:  [ -74.92162323   13.57623863 -547.72540283]

In [11]: # Get scales particles 
    ...: pointData = polydata.GetPointData() 
    ...: scaleData = pointData.GetArray(0)                                                                                                                                                                  

In [12]: # Get number of particles 
    ...: print("The number of particles based on scale: ", scaleData.GetNumberOfTuples())                                                                                                                   
The number of particles based on scale:  48425

In [13]: # Get the scale of first particles 
    ...: scaleParticle = scaleData.GetComponent(0,0)                                                                                                                                                        

In [14]: print("The scale of first particles: ", scaleParticle)                                                                                                                                             
The scale of first particles:  1.5849934816360474

In [15]: # Get the scale of 273 particle 
    ...: scaleParticle = scaleData.GetComponent(273,0) 
    ...: print("The scale of 273 particle: ", scaleParticle)                                                                                                                                                
The scale of 273 particle:  1.9540350437164307

In [16]: # Create scale matrix 
    ...: scaleMatrix = np.zeros((itemsHeaderCT[3][1])) 
    ...: print("The size of scale matrix: ", scaleMatrix.shape)                                                                                                                                             
The size of scale matrix:  (509, 347, 629)

In [17]: # Get space origin item in header nrrd CT file for creating transform matrix 
    ...: spaceOrigin = np.array([itemsHeaderCT[8][1][0],itemsHeaderCT[8][1][1] ,itemsHeaderCT[8][1][2]]) 
    ...: rowIndex = np.int(np.round(np.absolute(spaceOrigin[0]))) 
    ...: columnIndex = np.int(np.round(np.absolute(spaceOrigin[1]))) 
    ...: sliceIndex = np.int(np.round(np.absolute(spaceOrigin[2])))                                                                                                                                         

In [18]: # Create Transform matrix for converting the particle coordinates to voxel index in scale matrix 
    ...: transferLat, transferVert, transferLong = ((1, 0, 0, columnIndex), (0, 1, 0, rowIndex), (0, 0, 1, sliceIndex)) 
    ...: transformMatrix = np.array([transferLat, transferVert, transferLong]) 
    ...: print("Transfer Matrix: ", '\n', transformMatrix)                                                                                                                                                  
Transfer Matrix:  
 [[  1   0   0 118]
 [  0   1   0 190]
 [  0   0   1 925]]

In [19]: # Set voxel index 
    ...: indexParticle = 1 
    ...: for indexParticle in range(numberOfParticles): 
    ...:  particleCoordsTmp = np.asarray(particlesCoordinates.GetPoint(indexParticle)) 
    ...:  particleCoordinates = np.array([[particleCoordsTmp[0], particleCoordsTmp[1], particleCoordsTmp[2], 1]]).T 
    ...:  voxelIndex = (np.absolute(np.round(transformMatrix.dot(particleCoordinates)))).astype(int) 
    ...:  scaleMatrix[np.int(voxelIndex[2,0])][np.int(voxelIndex[0,0])][np.int(voxelIndex[1,0])] = scaleData.GetComponent(indexParticle, 0) 
    ...:                                                                                                                                                                                                    

In [20]: # Save scale matrix 
    ...: nrrd.write('scaleMatrix.nrrd', scaleMatrix, headerCT)                                                                                                                                              

In [21]: exit                                                                                                                                                                                               
sn@MP:~$ 
</code></pre>
<p>After executing these commands, I noticed that the scale property of all particles has not been transferred into the scaleMatrix. Also, its directions are not the same as CT.</p>
<p>If possible, please guide me.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #9 by @lassoan (2020-12-09 16:26 UTC)

<p>Does the VTK file contain a surface mesh? If yes, then it would be very sparse to put that into a volume (you would have about 99% of your voxels undefined). Why would you like to store point data in a volume? Can you upload an example vtk file somewhere and post the link here?</p>

---

## Post #10 by @shahrokh (2020-12-11 07:43 UTC)

<p>Hello Dear Andras</p>
<p>At first, I should mention that the CIP outputs includes the following files:<br>
1- A vtk file containing the particles system (for example wholeLungVesselParticles.vtk),<br>
2- nrrd files containing val, eigenvalues, eigenvectors, Hessian elements and … with the following names:<br>
val.nrrd, hmode.nrrd, hess.nrrd, heval[0-2].nrrd and hevec[0-2].nrrd</p>
<p>As mentioned in the previous message, I converted the particles system file to vtp format by using MIRTK. Then I executed the mentioned commands.</p>
<p>About this question that “<strong>Does the VTK file contain a surface mesh?</strong>”, I did not find the word <strong>mesh</strong> in the file of particles system (wholeLungVesselParticles.vtk).</p>
<p>Also, about this question that “<strong>Why would you like to store point data in a volume?</strong>”, I have to say that I want to give this information to a <strong>deep learning algorithm</strong> (<strong>CNN</strong>) in structures such as matrix or tensor.</p>
<p>Also I must mention that I want to use the following features to classify pulmonary vessels into healthy and diseased groups.</p>
<p>Features:<br>
1- val(HU unit in the location of particle sampled),<br>
2- scale( vessel size avaiable at the file of wholeLungVesselParticles.vtk)<br>
3- eigenvectors (hevec[0-2])<br>
4- eigenvalues (heval[0-2])<br>
5- hess (Hessian matrix)</p>
<p><strong>Comments:</strong> I believe all the information contained in output files (val.nrrd, hmode.nrrd, hess.nrrd, heval[0-2].nrrd and hevec[0-2].nrrd) is inculded in the vtk file of particles system (wholeLungVesselParticles.vtk).</p>
<p>I send the download link of the following files with WeTransfer:<br>
<a href="https://we.tl/t-BTHCrarOAQ" rel="noopener nofollow ugc">wholeLungVesselParticles.vtk</a><br>
<a href="https://we.tl/t-pG16vZpnTG" rel="noopener nofollow ugc">hmode.nrrd</a><br>
<a href="https://we.tl/t-5QbOxygIyC" rel="noopener nofollow ugc">val.nrrd</a><br>
<a href="https://we.tl/t-vogDBbjiJe" rel="noopener nofollow ugc">hess.nrrd</a><br>
<a href="https://we.tl/t-XrjfRjakWq" rel="noopener nofollow ugc">heval0.nrrd</a><br>
<a href="https://we.tl/t-g7smEDHL54" rel="noopener nofollow ugc">heval1.nrrd</a><br>
<a href="https://we.tl/t-dyMiLJ2GnU" rel="noopener nofollow ugc">heval2.nrrd</a><br>
<a href="https://we.tl/t-u7SKMl7XNx" rel="noopener nofollow ugc">hevec0.nrrd</a><br>
<a href="https://we.tl/t-12VJqMVoIm" rel="noopener nofollow ugc">hevec1.nrrd</a><br>
<a href="https://we.tl/t-iJyskqqpHt" rel="noopener nofollow ugc">hevec2.nrrd</a><br>
<a href="https://we.tl/t-0KezUy5K5Q" rel="noopener nofollow ugc">hmode.nrrd</a></p>
<p>I’m so glad that you guide me doing it.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #11 by @shahrokh (2020-12-13 13:09 UTC)

<p>Hello Dear Andras</p>
<p>I wanted to inform that the problem was solved with the following programs.</p>
<blockquote>
<p><span class="hashtag-raw">#Load</span> modules<br>
import numpy as np<br>
import nrrd<br>
import vtk<br>
import os</p>
<p><span class="hashtag-raw">#Load</span> CT (nrrd file)<br>
filenameCT = ‘/home/sn/testCIP/result1/WholeLung01/wholeLung/CT_wholeLung.nrrd’<br>
CT, headerCT = nrrd.read(filenameCT)<br>
itemsHeaderCT = list(headerCT.items())<br>
print(“items in CT header”,‘\n’)<br>
for i in range(len(itemsHeaderCT)):<br>
print(i, itemsHeaderCT[i][0], itemsHeaderCT[3][1])<br>
print(‘\n’)<br>
print(“items header of nnd file CT”,  itemsHeaderCT[3], ‘\n’)<br>
scaleMatrix = np.zeros((itemsHeaderCT[3][1]))<br>
print(“matrix size scaleMatrix”, scaleMatrix.shape, ‘\n’)<br>
print(“matrix size CT:”, CT.shape, ‘\n’)</p>
<p><span class="hashtag-raw">#Load</span> particles system (vtp file)<br>
filenameParticles = “/home/sn/testCIP/result1/WholeLung01/wholeLungVesselParticles.vtp”;<br>
readerDataVTP = vtk.vtkXMLPolyDataReader();<br>
readerDataVTP.SetFileName(filenameParticles);<br>
readerDataVTP.Update();<br>
polydata = readerDataVTP.GetOutput();</p>
<p><span class="hashtag-raw">#Get</span> particles coordinate<br>
particlesCoordinates = polydata.GetPoints();<br>
numberOfParticles = readerDataVTP.GetNumberOfPoints();<br>
print(“number of particles:”, numberOfParticles, ‘\n’)<br>
print("Type of particles coordinates in vtp file: ", type(particlesCoordinates.GetPoint(0)),‘\n’)<br>
<span class="hashtag-raw">#Convert</span> and get first particle coordinate from tuple to numpy array<br>
particleCoordinates = np.asarray(particlesCoordinates.GetPoint(0))<br>
print("The coordinates of first particle: ", particleCoordinates)<br>
<span class="hashtag-raw">#Convert</span> and get end particle coordinate from tuple to numpy array<br>
particleCoordinates = np.asarray(particlesCoordinates.GetPoint(numberOfParticles-1))<br>
print("The coordinates of ",  numberOfParticles, " particle: ", particleCoordinates)</p>
<p><span class="hashtag-raw">#Get</span> scales particles<br>
pointData = polydata.GetPointData()<br>
scaleData = pointData.GetArray(0)<br>
<span class="hashtag-raw">#Get</span> number of particles<br>
print("The number of particles based on scale: ", scaleData.GetNumberOfTuples())<br>
<span class="hashtag-raw">#Get</span> the scale of first particles<br>
scaleParticle = scaleData.GetComponent(0,0)<br>
print("The scale of first particles: ", scaleParticle)<br>
<span class="hashtag-raw">#Get</span> the scale of 273 particle<br>
scaleParticle = scaleData.GetComponent(273,0)<br>
print("The scale of 273 particle: ", scaleParticle)</p>
<p><span class="hashtag-raw">#Create</span> scale matrix<br>
scaleMatrix = np.zeros([itemsHeaderCT[3][1][0], itemsHeaderCT[3][1][1], itemsHeaderCT[3][1][2]])<br>
print("The size of scale matrix: ", scaleMatrix.shape)</p>
<p><span class="hashtag-raw">#Get</span> space origin item in header nrrd CT file for creating transform matrix<br>
spaceOrigin = np.array([itemsHeaderCT[8][1][0],itemsHeaderCT[8][1][1] ,itemsHeaderCT[8][1][2]])<br>
rowIndex = np.int(np.round(np.absolute(spaceOrigin[0])))<br>
columnIndex = np.int(np.round(np.absolute(spaceOrigin[1])))<br>
sliceIndex = np.int(np.round(np.absolute(spaceOrigin[2])))</p>
<p><span class="hashtag-raw">#Create</span> Transform matrix for converting the particle coordinates to voxel index in scale matrix<br>
transferLat, transferVert, transferLong = ((1, 0, 0, rowIndex), (0, 1, 0, columnIndex), (0, 0, 1, sliceIndex))<br>
transformMatrix = np.array([transferLat, transferVert, transferLong])<br>
print("Transfer Matrix: ", ‘\n’, transformMatrix)</p>
<p><span class="hashtag-raw">#Set</span> voxel index<br>
indexParticle = 1<br>
for indexParticle in range(numberOfParticles):<br>
particleCoordsTmp = np.asarray(particlesCoordinates.GetPoint(indexParticle))<br>
particleCoordinates = np.array([[particleCoordsTmp[0], particleCoordsTmp[1], particleCoordsTmp[2], 1]]).T<br>
voxelIndex = np.floor(transformMatrix.dot(particleCoordinates)/0.6250495910644531).astype(int)<br>
<span class="hashtag-raw">#print</span>("Particle Coordinate: ", particleCoordsTmp, " Voxel Index: ", voxelIndex.T,‘\n’)<br>
<span class="hashtag-raw">#print</span>("Voxel Index: ", voxelIndex.T)<br>
scaleMatrix[np.int(voxelIndex[0,0])][np.int(voxelIndex[1,0])][np.int(voxelIndex[2,0])] = scaleData.GetComponent(indexParticle, 0)</p>
<p>nrrd.write(‘scaleMatrix.nrrd’, scaleMatrix, headerCT)</p>
</blockquote>
<p>The result is shown in the following figure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b39f852a117ffb5136b5bf646ba9c764a4d65a44.jpeg" data-download-href="/uploads/short-url/pD1eJlXz8uuUdfx63KFVhz7SKqw.jpeg?dl=1" title="a" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b39f852a117ffb5136b5bf646ba9c764a4d65a44_2_690x388.jpeg" alt="a" data-base62-sha1="pD1eJlXz8uuUdfx63KFVhz7SKqw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b39f852a117ffb5136b5bf646ba9c764a4d65a44_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b39f852a117ffb5136b5bf646ba9c764a4d65a44_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b39f852a117ffb5136b5bf646ba9c764a4d65a44_2_1380x776.jpeg 2x" data-dominant-color="848493"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a</span><span class="informations">1920×1080 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Dear Andras I’m sorry, but I’ve got it right now. You said in the previous message that “<strong>Does the VTK file contain a surface mesh? If yes, then it would be very sparse to put that into a volume (you would have about 99% of your voxels undefined).</strong>”</p>
<p>At now I realized that maybe I should work with <strong>projecting points on a 2D plane that looks</strong> like the following figure.<br>
This is done by selecting <strong>Projection</strong> mode in <strong>Model</strong> module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/1116a1c4fc747003ee058036d53055e1fa586fc5.jpeg" data-download-href="/uploads/short-url/2raBy6hy4UROSsdwtf7CyWdDeUB.jpeg?dl=1" title="b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1116a1c4fc747003ee058036d53055e1fa586fc5_2_690x388.jpeg" alt="b" data-base62-sha1="2raBy6hy4UROSsdwtf7CyWdDeUB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1116a1c4fc747003ee058036d53055e1fa586fc5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1116a1c4fc747003ee058036d53055e1fa586fc5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1116a1c4fc747003ee058036d53055e1fa586fc5_2_1380x776.jpeg 2x" data-dominant-color="7B7C7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b</span><span class="informations">1920×1080 473 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What do you suggest me to do it (Project 3D model to 2D plane, for example a 2D matrix)?<br>
Please guide me.<br>
Shahrokh</p>

---

## Post #12 by @lassoan (2020-12-14 04:14 UTC)

<p>Since you have all your attributes defined at vessel points, it may be more appropriate to run the deep learning on arrays created from these attributes directly (instead of painting into a volume). You could create an attribute array for each vessel point from attributes of that point and nearby points.</p>
<p>I would recommend to do some literature search to see how others classify trees or point sets and do a lot of experiments to see what works.</p>

---

## Post #13 by @shahrokh (2020-12-19 11:38 UTC)

<p>Dear Andras</p>
<p>Thank you very much. As you guide me, I want to use these properties (24 features) in classification by creating an <strong>attribute array</strong> for each case (number of rows equal to the number of particles sampled and number of columns equal to the number of particle properties).</p>
<p>Best regards.<br>
Shahrokh</p>

---
