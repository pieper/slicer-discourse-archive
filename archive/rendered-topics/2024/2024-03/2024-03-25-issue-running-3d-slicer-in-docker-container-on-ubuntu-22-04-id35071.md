# Issue Running 3D Slicer in Docker Container on Ubuntu 22.04 Image

**Topic ID**: 35071
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/issue-running-3d-slicer-in-docker-container-on-ubuntu-22-04-image/35071

---

## Post #1 by @SimonLBS (2024-03-25 19:53 UTC)

<p>Hello,</p>
<p>I’m working on incorporating 3D Slicer into a Docker container for a project where I need to convert DICOM folders to NIfTI files using Python scripts. I’ve set up my Dockerfile based on Ubuntu 22.04 and have installed various packages and dependencies necessary for my environment and for running 3D Slicer.</p>
<p>However, when attempting to run Slicer from within the Docker container with the command <code>./Slicer/Slicer-5.6.1-linux-amd64/Slicer --no-splash --python-script &lt;script&gt;</code>, I encounter the following error:<br>
error while loading shared libraries: libXdamage.so.1: cannot open shared object file: No such file or directory</p>
<p>Below is the relevant portion of my Dockerfile:</p>
<pre><code class="lang-auto">FROM ubuntu:22.04
# Other installations and package setups
RUN apt-get update &amp;&amp; apt-get -y upgrade &amp;&amp; apt-get -y --quiet --no-install-recommends install \
      ca-certificates \
      apt-utils \
      vim \
      curl \
      apache2 \
      apache2-utils \
      python3.10 \
      libapache2-mod-wsgi-py3 \
      tzdata \
      python3-pip \
      python3.10-venv \
      python3-dev \
      default-libmysqlclient-dev \
      build-essential \
      pkg-config \
      swig3.0  \
      libmagic1 \
      wget \
    &amp;&amp; apt-get -y autoremove \
    &amp;&amp; apt-get clean autoclean

# Slicer 
RUN apt-get -y install libpulse-dev libnss3 libglu1-mesa &amp;&amp; apt-get install --reinstall libxcb-xinerama0 &amp;&amp; apt-get -y autoremove &amp;&amp; apt-get clean autoclean

RUN wget -O "Slicer.tar.gz" https://slicer-packages.kitware.com/api/v1/item/657813b183a3201b44d4e6f7/download &amp;&amp; mkdir Slicer &amp;&amp; tar -xvzf Slicer.tar.gz -C Slicer &amp;&amp; chmod -R 777 Slicer &amp;&amp; rm Slicer.tar.gz
</code></pre>
<p>I’m wondering if my Dockerfile is missing a step or if my command to run Slicer within the container is missing.</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2024-03-25 19:58 UTC)

<p>Look at this thread for a successfully build docker image:</p><aside class="quote quote-modified" data-post="11" data-topic="22539">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/francis_chemorion/48/69748_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-docker-for-gui-via-browser/22539/11">Slicer Docker for GUI via browser</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Just in case there is anyone else looking for Docker Slicer GUI, I also have one based on Ubuntu Desktop, could not rebuild Steve’s Image 


Only change I made is to download and extract Slicer first, then place it in the folder with the dockerfile, and I also modify slicerrc.py to enable me copy and load files directly to the container so that it is open with the needed files. 
I also create volumes for sending files in and reading files out. 
Let me know if you are able to have fun with this.
  </blockquote>
</aside>


---

## Post #3 by @RafaelPalomar (2024-03-26 09:23 UTC)

<p><code>libXdamage.so.1</code> seems to exist in the <code>libxdamage1</code> package:</p>
<pre data-code-wrap="shell"><code class="lang-shell">apt-file find libXdamage
libxdamage-dev: /usr/lib/x86_64-linux-gnu/libXdamage.a
libxdamage-dev: /usr/lib/x86_64-linux-gnu/libXdamage.so
libxdamage1: /usr/lib/x86_64-linux-gnu/libXdamage.so.1
libxdamage1: /usr/lib/x86_64-linux-gnu/libXdamage.so.1.1.0
</code></pre>
<p>adding that package to the install command in your container definition should do it.</p>
<p>I use <code>distrobox</code> to manage development containers. You can have a look at my <code>slicer-devcontainer</code> (<a href="https://github.com/RafaelPalomar/Slicer-devcontainer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RafaelPalomar/slicer-devcontainer: Development container for 3D Slicer</a>), which I use for developing and running 3D Slicer.</p>

---

## Post #4 by @SimonLBS (2024-03-26 12:53 UTC)

<p>Thank you, muratmaga and RafaelPalomar, for your suggestions! I’ve included the additional packages from the “Slicer Docker for GUI via browser” thread and added libxdamage1 together with the others from Rafael Palomar development containers. This approach successfully resolved the libXdamage.so.1 error. Additionally, by integrating Xvfb :99 &amp; export DISPLAY=:99; into my command seems to work.</p>
<p>Below is my refined Dockerfile for the benefit of anyone looking to achieve similar functionality. While not all packages may be necessary for this setup, here’s what worked for me:</p>
<pre><code class="lang-auto">FROM ubuntu:22.04

# make apt/dpkg behave
ENV DEBIAN_FRONTEND=noninteractive

# Update + upgrade
RUN apt-get update &amp;&amp; apt-get -y upgrade

# Slicer stuff
COPY Slicer.tar.gz .
RUN apt-get install -y libpulse-dev libnss3 libglu1-mesa
RUN apt-get install -y libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-xkb1 libxkbcommon-x11-0
RUN apt-get install -y libxcb-shape0 libxcb-xinerama0 libxcb-xinerama0-dev
RUN apt-get install -y libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-randr0 libxcb-xkb-dev libxkbcommon-x11-dev
RUN apt-get install -y libxdamage1
RUN apt-get install --reinstall libxcb-xinerama0 &amp;&amp; apt-get -y autoremove &amp;&amp; apt-get clean autoclean

# Qt5 dependencies for the user interface and development
RUN apt-get install -y  qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev qtwebengine5-dev qtscript5-dev qtbase5-private-dev libqt5x11extras5-dev libxt-dev libqt5opengl5-dev

# Other essential packages for software development
RUN apt-get install -y  libssl-dev libcurl4-openssl-dev

# Python for scripting within 3D Slicer
RUN apt-get install -y  python3-dev python3-pip

# wget -O "Slicer.tar.gz" https://slicer-packages.kitware.com/api/v1/item/657813b183a3201b44d4e6f7/download &amp;&amp;
RUN mkdir Slicer &amp;&amp; tar -xvzf Slicer.tar.gz -C Slicer &amp;&amp; chmod -R 777 Slicer &amp;&amp; rm Slicer.tar.gz

RUN apt-get install -y xvfb

# Script to test if there are errors
COPY docker_slicer_test.py .

# Xvfb :99 &amp; export DISPLAY=:99; ./Slicer/Slicer-5.6.1-linux-amd64/Slicer --no-splash --python-script docker_slicer_test.py a b
CMD ["sh"]
</code></pre>
<p>And for reference, here’s the docker_slicer_test.py script:</p>
<pre><code class="lang-auto">import os
import argparse
import shutil

import slicer
from DICOMLib import DICOMUtils


def convertDICOMSeriesToNifti(inputDICOMDirectory, outputDirectory):
    print(f"Starting conversion for DICOM directory: {inputDICOMDirectory}")

    # Load DICOM files from the directory
    patientUIDs = slicer.dicomDatabase.patients()
    if len(patientUIDs):
        for patientUID in patientUIDs:
            print("patientUID:", patientUID)
    else:
        print("No ids")
    print("Conversion completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert DICOM series to compressed NIfTI format.")
    parser.add_argument("inputDICOMDirectory", help="Path to the input directory containing DICOM files.")
    parser.add_argument("outputDirectory", help="Path to the directory where compressed NIfTI files will be saved.")

    args = parser.parse_args()

    try:
        convertDICOMSeriesToNifti(args.inputDICOMDirectory, args.outputDirectory)
    except Exception as e:
        print(e)

    # Exit Slicer
    slicer.app.quit()

</code></pre>
<p>Again thanks for the help!</p>

---

## Post #5 by @SimonLBS (2024-03-26 14:16 UTC)

<p>After testing some more, I found a new problem. When running my convert script in the container, it does not save any files, but it does when running it outside.</p>
<p>I used the convert script found in: [quote=“lassoan, post:19, topic:11720”]<br>
Your first example did not contain the node saving part. The second example used the Slicer DICOM database. So, I created a new script (based on the example in the Slicer script repository + adding your node saving) and it worked well for me:<br>
[/quote]</p>
<p>My script is:</p>
<pre><code class="lang-auto">import argparse
import os

parser = argparse.ArgumentParser(description="Convert DICOM series to compressed NIfTI format.")
parser.add_argument("inputDICOMDirectory", default="test", help="Path to the input directory containing DICOM files.")
parser.add_argument("outputDirectory", default="test_out", help="Path to the directory where compressed NIfTI files will be saved.")
args = parser.parse_args()
dicomDataDir, outputDir = args.inputDICOMDirectory, args.outputDirectory
os.makedirs(outputDir, exist_ok=True)

import slicer
import re

try:
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
    from DICOMLib import DICOMUtils
    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))

    print("Found nodes:", loadedNodeIDs)
    for loadedNodeID in loadedNodeIDs:
        node = slicer.mrmlScene.GetNodeByID(loadedNodeID)
        safeFileName = re.sub(r'(?u)[^-\w.]', '', node.GetName().strip().replace(' ', '_'))
        print(f"Saving {safeFileName}...")
        slicer.util.saveNode(node, '{0}/{1}.nrrd'.format(outputDir, safeFileName))

finally:
    exit()
</code></pre>
<p>When running it outside it works:</p>
<pre><code class="lang-auto">qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
TagCacheDatabase adding table

DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
........
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.


"DICOM indexer has successfully inserted 3219 files [2.02s]"
"DICOM indexer has successfully processed 3219 files [3.18s]"
"DICOM indexer has updated display fields for 3219 files [0.43s]"
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
........
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
WARNING: In /work/Stable/Slicer-0-build/ITK/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx, line 478
ImageSeriesReader (0x5fa3390): Non uniform sampling or missing slices detected,  maximum nonuniformity:0.000992248


DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
WARNING: In /work/Stable/Slicer-0-build/ITK/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx, line 478
ImageSeriesReader (0x5fa3390): Non uniform sampling or missing slices detected,  maximum nonuniformity:0.000993976


DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /test/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /test/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x36aa840) returned failure for request: vtkInformation (0x5ca95a0)
  Debug: Off
  Modified Time: 84599
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /test/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /test/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x3651a00) returned failure for request: vtkInformation (0x2947640)
  Debug: Off
  Modified Time: 84694
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /test/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /test/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x57e4de0) returned failure for request: vtkInformation (0x5b1b140)
  Debug: Off
  Modified Time: 89880
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /test/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /test/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x3651a00) returned failure for request: vtkInformation (0x2936fa0)
  Debug: Off
  Modified Time: 89975
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Found nodes: ['vtkMRMLScalarVolumeNode1', 'vtkMRMLScalarVolumeNode2', 'vtkMRMLScalarVolumeNode3', 'vtkMRMLScalarVolumeNode4', 'vtkMRMLScalarVolumeNode5', 'vtkMRMLScalarVolumeNode6', 'vtkMRMLScalarVolumeNode7', 'vtkMRMLScalarVolumeNode8', 'vtkMRMLScalarVolumeNode9', 'vtkMRMLScalarVolumeNode10', 'vtkMRMLVectorVolumeNode1', 'vtkMRMLVectorVolumeNode2']
Saving 1_&lt;name&gt;...
Saving 3_&lt;name&gt;...
Saving 4_&lt;name&gt;...
Saving 5_&lt;name&gt;...
Saving 12_&lt;name&gt;...
Saving 13_&lt;name&gt;...
Saving 14_&lt;name&gt;...
Saving 601_&lt;name&gt;...
Saving 602_&lt;name&gt;...
Saving 999_&lt;name&gt;...
Saving 27327_&lt;name&gt;...
Saving 27328_&lt;name&gt;...
</code></pre>
<p>In my container, I get the following:</p>
<pre><code class="lang-auto">QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
TagCacheDatabase adding table

DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
........
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.

"DICOM indexer has successfully inserted 3219 files [2.67s]"
"DICOM indexer has successfully processed 3220 files [3.90s]"
"DICOM indexer has updated display fields for 3219 files [0.44s]"
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
........
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.

vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x49bb4f0)
  Debug: Off
  Modified Time: 67558
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x5028c10)
  Debug: Off
  Modified Time: 67653
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x467c940)
  Debug: Off
  Modified Time: 67758
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x49fae80)
  Debug: Off
  Modified Time: 67864
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x4fc09c0)
  Debug: Off
  Modified Time: 67969
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x15e5510)
  Debug: Off
  Modified Time: 68075
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x4fec360)
  Debug: Off
  Modified Time: 68180
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x4679360)
  Debug: Off
  Modified Time: 68286
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x49bd4a0)
  Debug: Off
  Modified Time: 68391
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x52cb7f0)
  Debug: Off
  Modified Time: 68497
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x5309470)
  Debug: Off
  Modified Time: 68602
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x4a111b0)
  Debug: Off
  Modified Time: 68708
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x4f5d180)
  Debug: Off
  Modified Time: 68813
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x4fee660)
  Debug: Off
  Modified Time: 68919
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x4a14770)
  Debug: Off
  Modified Time: 69024
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x4679360)
  Debug: Off
  Modified Time: 69130
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x4fee610)
  Debug: Off
  Modified Time: 69235
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x52cb7f0)
  Debug: Off
  Modified Time: 69341
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x34b39d0) returned failure for request: vtkInformation (0x52c7180)
  Debug: Off
  Modified Time: 69446
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x44e0be0) returned failure for request: vtkInformation (0x4fee660)
  Debug: Off
  Modified Time: 69552
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x34b39d0) returned failure for request: vtkInformation (0x4feafa0)
  Debug: Off
  Modified Time: 69657
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x44e0be0) returned failure for request: vtkInformation (0x53092e0)
  Debug: Off
  Modified Time: 69763
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x34b39d0) returned failure for request: vtkInformation (0x5021fd0)
  Debug: Off
  Modified Time: 69868
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x44e0be0) returned failure for request: vtkInformation (0x52cb7f0)
  Debug: Off
  Modified Time: 69974
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x34b39d0) returned failure for request: vtkInformation (0x49fae80)
  Debug: Off
  Modified Time: 70079
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x44e0be0) returned failure for request: vtkInformation (0x4fee660)
  Debug: Off
  Modified Time: 70185
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x34b39d0) returned failure for request: vtkInformation (0x467c4a0)
  Debug: Off
  Modified Time: 70290
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x44e0be0) returned failure for request: vtkInformation (0x52eba80)
  Debug: Off
  Modified Time: 70396
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Found nodes: []
[2]+  Exit 1                  Xvfb :99
</code></pre>
<p>From what I can see the one outside dose not have the “vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/.dcm does not exist.”<br>
on the .dcm only on the .sr.</p>
<p>I think the “DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.” comes from Danish letters like æøå in some tags.</p>
<p>Am I missing something?</p>

---

## Post #6 by @lassoan (2024-03-26 16:02 UTC)

<blockquote>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-/20240326_140057_TempDICOMDatabase/.dcm does not exist.</p>
</blockquote>
<p>Maybe Slicer does not have write acces to the <code>tmp</code> folder? The <code>/tmp/Slicer-</code> folder looks odd, too. I would recommend to connect to the Slicer GUI via your web browser to test file loading, DICOM import, etc. using the GUI.</p>
<p>Have you replaced the actual name by <code>&lt;name&gt;</code>? Does the name contain special characters?</p>
<p>The other messages should be OK to ignore, but just a few notes:</p>
<blockquote>
<p>DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.</p>
</blockquote>
<p>This is a very rare encoding that Slicer and other commonly used DICOM software does not support (see <a href="https://github.com/commontk/CTK/pull/968" class="inline-onebox">BUG: Remove invalid characters from DICOM strings with unsupported character encoding by lassoan · Pull Request #968 · commontk/CTK · GitHub</a>). To avoid this error, you would need to switch to a different encoding when the DICOM data is exported.</p>
<blockquote>
<p>ImageSeriesReader (0x5fa3390): Non uniform sampling or missing slices detected,  maximum nonuniformity:0.000992248</p>
</blockquote>
<p>This most likely indicates poor implementation of the software that generates the DICOM data (most likely they use 4 digits to save a floating-point number into a decimal string in the DICOM file). We cannot do anything about it in Slicer.</p>
<blockquote>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /test/.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /test/.sr</p>
</blockquote>
<p>Reading of structured report requires installation of QuantitativeReporting extension. There are many kinds of structured reports, so it might not fix the error. If you only want to extract images then you can let the scalar volume plugin trying to get some image information out of the SR.</p>

---

## Post #7 by @SimonLBS (2024-03-27 08:25 UTC)

<p>Hi Lasso, thanks for your answer!</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe Slicer does not have write acces to the <code>tmp</code> folder? The <code>/tmp/Slicer-</code> folder looks odd, too.</p>
</blockquote>
</aside>
<p>I changed the <code>TemporaryDICOMDatabase</code> to <code>DICOMUtils.TemporaryDICOMDatabase("db_temp")</code> and ensured that there is read/write access:</p>
<pre><code class="lang-auto">root@5afaf174a8f5:/# ls -la
total 92
drwxr-xr-x   1 root root     4096 Mar 27 07:51 .
drwxr-xr-x   1 root root     4096 Mar 27 07:51 ..
-rwxr-xr-x   1 root root        0 Mar 27 07:51 .dockerenv
drwxrwxrwx   1 root root     4096 Mar 26 12:27 Slicer
lrwxrwxrwx   1 root root        7 Feb 27 15:59 bin -&gt; usr/bin
drwxr-xr-x   2 root root     4096 Apr 18  2022 boot
drwxrwxrwx   1 root root     4096 Mar 27 07:52 db_temp
drwxr-xr-x   5 root root      360 Mar 27 07:51 dev
-rw-rw-r--   1 root root     1512 Mar 27 07:43 docker_slicer_test.py
drwxr-xr-x   1 root root     4096 Mar 27 07:51 etc
drwxr-xr-x   2 root root     4096 Apr 18  2022 home
lrwxrwxrwx   1 root root        7 Feb 27 15:59 lib -&gt; usr/lib
lrwxrwxrwx   1 root root        9 Feb 27 15:59 lib32 -&gt; usr/lib32
lrwxrwxrwx   1 root root        9 Feb 27 15:59 lib64 -&gt; usr/lib64
lrwxrwxrwx   1 root root       10 Feb 27 15:59 libx32 -&gt; usr/libx32
drwxr-xr-x   2 root root     4096 Feb 27 15:59 media
drwxr-xr-x   2 root root     4096 Feb 27 15:59 mnt
drwxrwxrwx   2 root root     4096 Mar 27 07:51 niiout
drwxr-xr-x   2 root root     4096 Feb 27 15:59 opt
dr-xr-xr-x 808 root root        0 Mar 27 07:51 proc
drwx------   1 root root     4096 Mar 27 07:51 root
drwxr-xr-x   1 root root     4096 Mar 26 12:26 run
lrwxrwxrwx   1 root root        8 Feb 27 15:59 sbin -&gt; usr/sbin
drwxr-xr-x   2 root root     4096 Feb 27 15:59 srv
dr-xr-xr-x  13 root root        0 Mar 27 07:51 sys
drwxr-xr-x   3 root www-data 4096 Jan 23 12:45 test
drwxrwxrwt   1 root root     4096 Mar 27 07:51 tmp
drwxr-xr-x   1 root root     4096 Feb 27 15:59 usr
drwxr-xr-x   1 root root     4096 Feb 27 16:02 var
</code></pre>
<p>The output seems the same:</p>
<pre><code class="lang-auto">QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
"DICOM indexer has successfully inserted 3219 files [2.79s]"
"DICOM indexer has successfully processed 3219 files [4.03s]"
"DICOM indexer has updated display fields for 3219 files [0.44s]"
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x47aafd0)
  Debug: Off
  Modified Time: 67547
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x1b547b0)
  Debug: Off
  Modified Time: 67642
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x47a5a10)
  Debug: Off
  Modified Time: 67747
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x46fa190)
  Debug: Off
  Modified Time: 67853
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x3d1b530)
  Debug: Off
  Modified Time: 67958
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x4ac7440)
  Debug: Off
  Modified Time: 68064
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x47bb2b0)
  Debug: Off
  Modified Time: 68169
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x3d1b4e0)
  Debug: Off
  Modified Time: 68275
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x4af95b0)
  Debug: Off
  Modified Time: 68380
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x47c64b0)
  Debug: Off
  Modified Time: 68486
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x47c3570)
  Debug: Off
  Modified Time: 68591
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x47c3870)
  Debug: Off
  Modified Time: 68697
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x4a5fc80)
  Debug: Off
  Modified Time: 68802
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x4ac7440)
  Debug: Off
  Modified Time: 68908
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x1b547b0)
  Debug: Off
  Modified Time: 69013
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x47c39f0)
  Debug: Off
  Modified Time: 69119
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x4af90a0)
  Debug: Off
  Modified Time: 69224
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x4a98de0)
  Debug: Off
  Modified Time: 69330
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x468b410) returned failure for request: vtkInformation (0x5122610)
  Debug: Off
  Modified Time: 69435
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x3430330) returned failure for request: vtkInformation (0x4a57b90)
  Debug: Off
  Modified Time: 69541
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x468b410) returned failure for request: vtkInformation (0x4709a60)
  Debug: Off
  Modified Time: 69646
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x3430330) returned failure for request: vtkInformation (0x47c39f0)
  Debug: Off
  Modified Time: 69752
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x468b410) returned failure for request: vtkInformation (0x3d1b4e0)
  Debug: Off
  Modified Time: 69857
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x3430330) returned failure for request: vtkInformation (0x4a2f530)
  Debug: Off
  Modified Time: 69963
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x468b410) returned failure for request: vtkInformation (0x4b2c1e0)
  Debug: Off
  Modified Time: 70068
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x3430330) returned failure for request: vtkInformation (0x4af8c80)
  Debug: Off
  Modified Time: 70174
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x468b410) returned failure for request: vtkInformation (0x47c22d0)
  Debug: Off
  Modified Time: 70279
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/test/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x3430330) returned failure for request: vtkInformation (0x4a52ac0)
  Debug: Off
  Modified Time: 70385
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Found nodes: []
[2]+  Exit 1                  Xvfb :99
</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to connect to the Slicer GUI via your web browser to test file loading, DICOM import, etc. using the GUI.</p>
</blockquote>
</aside>
<p>How can I do that?</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you replaced the actual name by <code>&lt;name&gt;</code>? Does the name contain special characters?</p>
</blockquote>
</aside>
<p>Yes, I renamed it to <code>&lt;name&gt;</code> the real names are something like:<br>
<code>1.23.456789101112131415161718192021222324252/6272e829-3bb0-31e3-ba32-b33c3435dc3a/6.37.383940414243444546474849505152535455565.dcm</code></p>
<p>I have also tried the script on the SlicerDICOMTutorial data from <a href="https://spujol.github.io/SlicerDICOMTutorial/" rel="noopener nofollow ugc">https://spujol.github.io/SlicerDICOMTutorial/</a>:</p>
<pre><code class="lang-auto">QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
E: DcmElement: CommandField (0000,0100) larger (828667202) than remaining bytes in file
Could not load  "SlicerDICOMTutorialData/dataset1_TorsoCT/.DS_Store" 
DCMTK says:  I/O suspension or premature end of stream
Could not read DICOM file:SlicerDICOMTutorialData/dataset1_TorsoCT/.DS_Store
E: DcmElement: CommandField (0000,0100) larger (828667202) than remaining bytes in file
Could not load  "SlicerDICOMTutorialData/dataset2_BreastMRI/.DS_Store" 
DCMTK says:  I/O suspension or premature end of stream
Could not read DICOM file:SlicerDICOMTutorialData/dataset2_BreastMRI/.DS_Store
"DICOM indexer has successfully inserted 1299 files [0.54s]"
"DICOM indexer has successfully processed 1301 files [0.77s]"
Failed to find patient with PatientsName= and PatientID=
"DICOM indexer has updated display fields for 1299 files [0.15s]"
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset1_TorsoCT/IM-0001-0291.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x7bd8a8c4c0a0) returned failure for request: vtkInformation (0x5dd1390)
  Debug: Off
  Modified Time: 67317
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset1_TorsoCT/IM-0001-0291.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x5da74f0)
  Debug: Off
  Modified Time: 67412
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 769, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examine(fileLists)
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMImageSequencePlugin.py", line 54, in examine
    loadables += self.examineFiles(files)
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMImageSequencePlugin.py", line 173, in examineFiles
    ds = dicom.read_file(cineMriInstanceNumberToFilenameIndex[next(iter(cineMriInstanceNumberToFilenameIndex))], stop_before_pixels=True)
  File "/Slicer/Slicer-5.6.1-linux-amd64/lib/Python/lib/python3.9/site-packages/pydicom/filereader.py", line 1002, in dcmread
    fp = open(fp, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: '/db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/401.000000-STIR SENSE-35251/000018.dcm'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/301.000000-T2WTSE SENSE-80453/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x7bd8a8c4c0a0) returned failure for request: vtkInformation (0x5dc5650)
  Debug: Off
  Modified Time: 67688
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/301.000000-T2WTSE SENSE-80453/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x5fbf760)
  Debug: Off
  Modified Time: 67794
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/401.000000-STIR SENSE-35251/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x7bd8a8c4c0a0) returned failure for request: vtkInformation (0x5c13b00)
  Debug: Off
  Modified Time: 67899
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/401.000000-STIR SENSE-35251/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x3156d50)
  Debug: Off
  Modified Time: 68005
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5ff9520) returned failure for request: vtkInformation (0x604d740)
  Debug: Off
  Modified Time: 68206
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x5dbdc30)
  Debug: Off
  Modified Time: 68312
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x6088dd0)
  Debug: Off
  Modified Time: 68503
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x5dbdb90)
  Debug: Off
  Modified Time: 68609
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x602b890)
  Debug: Off
  Modified Time: 68787
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x3156d50)
  Debug: Off
  Modified Time: 68893
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x5fffbc0)
  Debug: Off
  Modified Time: 69075
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x3156510)
  Debug: Off
  Modified Time: 69181
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x5fc0cc0)
  Debug: Off
  Modified Time: 69364
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x5ff7b40)
  Debug: Off
  Modified Time: 69470
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x6273bc0)
  Debug: Off
  Modified Time: 69602
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x3156d50)
  Debug: Off
  Modified Time: 69708
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x5fc1100)
  Debug: Off
  Modified Time: 69853
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x3156510)
  Debug: Off
  Modified Time: 69959
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x6261050)
  Debug: Off
  Modified Time: 70100
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x5ff7b40)
  Debug: Off
  Modified Time: 70206
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x62630a0)
  Debug: Off
  Modified Time: 70347
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x6067c20)
  Debug: Off
  Modified Time: 70453
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5fc3270) returned failure for request: vtkInformation (0x60d6350)
  Debug: Off
  Modified Time: 70597
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/SlicerDICOMTutorialData/dataset2_BreastMRI/11-11-2008-MRI BREAST BILATERAL WITH T WITHOUT CONTRAST-28651/801.000000-AX BLISSAUTO SENSE-06146/000000.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x5c47c30) returned failure for request: vtkInformation (0x6260650)
  Debug: Off
  Modified Time: 70703
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Traceback (most recent call last):
  File "/Slicer/Slicer-5.6.1-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 654, in load
    parentTransformNode = frame.GetParentTransformNode()
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'

Found nodes: ['vtkMRMLSequenceNode1', 'vtkMRMLSequenceNode2', 'vtkMRMLSequenceNode3', 'vtkMRMLSequenceNode4', 'vtkMRMLSequenceNode5']
Saving 801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_TriggerTime...
bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const IOProperties&amp;, vtkMRMLMessageCollection*, vtkMRMLScene*) error: No writer found to write file "niiout/801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_TriggerTime.nrrd" of type "SequenceFile"
Saving 801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_AcquisitionTime...
bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const IOProperties&amp;, vtkMRMLMessageCollection*, vtkMRMLScene*) error: No writer found to write file "niiout/801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_AcquisitionTime.nrrd" of type "SequenceFile"
Saving 801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_ContentTime...
bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const IOProperties&amp;, vtkMRMLMessageCollection*, vtkMRMLScene*) error: No writer found to write file "niiout/801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_ContentTime.nrrd" of type "SequenceFile"
Saving 801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_AcquisitionTime_1...
bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const IOProperties&amp;, vtkMRMLMessageCollection*, vtkMRMLScene*) error: No writer found to write file "niiout/801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_AcquisitionTime_1.nrrd" of type "SequenceFile"
Saving 801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_InstanceNumber...
bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const IOProperties&amp;, vtkMRMLMessageCollection*, vtkMRMLScene*) error: No writer found to write file "niiout/801_MR_AX_BLISS_AUTO_SENSE_-_10_frames_Volume_Sequence_by_InstanceNumber.nrrd" of type "SequenceFile"

</code></pre>
<p>It seems to at least find some nodes but it cant write them either. The output folder is <code>drwxrwxrwx   2 root root     4096 Mar 27 07:51 niiout</code></p>
<p>My current dockerfile:</p>
<pre><code class="lang-auto">FROM ubuntu:22.04

# make apt/dpkg behave
ENV DEBIAN_FRONTEND=noninteractive

# Update + upgrade
RUN apt-get update &amp;&amp; apt-get -y upgrade

# Slicer stuff
COPY Slicer.tar.gz .
RUN apt-get install -y libpulse-dev libnss3 libglu1-mesa
RUN apt-get install -y libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-xkb1 libxkbcommon-x11-0
RUN apt-get install -y libxcb-shape0 libxcb-xinerama0 libxcb-xinerama0-dev
RUN apt-get install -y libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-randr0 libxcb-xkb-dev libxkbcommon-x11-dev
RUN apt-get install -y libxdamage1
RUN apt-get install --reinstall libxcb-xinerama0 &amp;&amp; apt-get -y autoremove &amp;&amp; apt-get clean autoclean

# Qt5 dependencies for the user interface and development
RUN apt-get install -y  qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev qtwebengine5-dev qtscript5-dev qtbase5-private-dev libqt5x11extras5-dev libxt-dev libqt5opengl5-dev

# Other essential packages for software development
RUN apt-get install -y  libssl-dev libcurl4-openssl-dev

# Python for scripting within 3D Slicer
RUN apt-get install -y  python3-dev python3-pip

# wget -O "Slicer.tar.gz" https://slicer-packages.kitware.com/api/v1/item/657813b183a3201b44d4e6f7/download &amp;&amp;
RUN mkdir Slicer &amp;&amp; tar -xvzf Slicer.tar.gz -C Slicer &amp;&amp; chmod -R 777 Slicer &amp;&amp; rm Slicer.tar.gz

RUN apt-get install -y xvfb

# Script to test if there are errors
COPY docker_slicer_test.py .
COPY --chown=:www-data --chmod=755 test-1 test
COPY --chown=:www-data --chmod=755 SlicerDICOMTutorialData SlicerDICOMTutorialData
RUN mkdir db_temp &amp;&amp; chmod -R a+rwx db_temp
RUN mkdir niiout &amp;&amp; chmod -R a+rwx niiout

# Xvfb :99 &amp; export DISPLAY=:99; ./Slicer/Slicer-5.6.1-linux-amd64/Slicer --no-main-window --python-script docker_slicer_test.py test niiout
# Xvfb :99 &amp; export DISPLAY=:99; ./Slicer/Slicer-5.6.1-linux-amd64/Slicer --no-main-window --python-script docker_slicer_test.py SlicerDICOMTutorialData niiout
CMD ["sh"]
</code></pre>
<p>The docker_slicer_test.py script:</p>
<pre><code class="lang-auto">import argparse
import os
import uuid

parser = argparse.ArgumentParser(description="Convert DICOM series to compressed NIfTI format.")
parser.add_argument("inputDICOMDirectory", default="test", help="Path to the input directory containing DICOM files.")
parser.add_argument("outputDirectory", default="test_out",
                    help="Path to the directory where compressed NIfTI files will be saved.")
args = parser.parse_args()
dicomDataDir, outputDir = args.inputDICOMDirectory, args.outputDirectory
os.makedirs(outputDir, exist_ok=True)

import slicer
import re

temp_db = os.path.abspath("db_temp")
if not os.path.exists(temp_db):
    print("Temp database does not exist")
    exit()

try:
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
    from DICOMLib import DICOMUtils

    with DICOMUtils.TemporaryDICOMDatabase(temp_db) as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))

    print("Found nodes:", loadedNodeIDs)
    for loadedNodeID in loadedNodeIDs:
        node = slicer.mrmlScene.GetNodeByID(loadedNodeID)
        safeFileName = re.sub(r'(?u)[^-\w.]', '', node.GetName().strip().replace(' ', '_'))
        print(f"Saving {safeFileName}...")
        slicer.util.saveNode(node, '{0}/{1}.nrrd'.format(outputDir, safeFileName))
except Exception as e:
    print("Exception occurred:", e)

finally:
    exit()

</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is a very rare encoding that Slicer and other commonly used DICOM software does not support (see <a href="https://github.com/commontk/CTK/pull/968" rel="noopener nofollow ugc">BUG: Remove invalid characters from DICOM strings with unsupported character encoding by lassoan · Pull Request #968 · commontk/CTK · GitHub</a>). To avoid this error, you would need to switch to a different encoding when the DICOM data is exported.</p>
</blockquote>
</aside>
<p>Thanks I will have a look!</p>
<p>Again thanks for the help!</p>

---

## Post #8 by @lassoan (2024-03-27 13:00 UTC)

<aside class="quote no-group quote-modified" data-username="SimonLBS" data-post="7" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonlbs/48/67638_2.png" class="avatar"> SimonLBS:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to connect to the Slicer GUI via your web browser to test file loading, DICOM import, etc. using the GUI.</p>
</blockquote>
</aside>
<p>How can I do that?</p>
</blockquote>
</aside>
<p>See instructions <a href="https://github.com/pieper/SlicerDockers">here</a>. In short, do not specify <code>--no-main-window</code> and then open Slicer in your web browser at the address: <code>localhost:8080</code></p>
<p>It would be useful to know if the file actually there and readable.</p>
<p>Are you using the latest Slicer Stable Release (Slicer-5.6.1) or a Slicer Preview Release (Slicer-5.7.0)? There have been significant DICOM import changes in the preview release.</p>

---

## Post #9 by @SimonLBS (2024-03-28 15:48 UTC)

<p>Hi Lasso, thanks for your help!</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>See instructions <a href="https://github.com/pieper/SlicerDockers" rel="noopener nofollow ugc">here </a>. In short, do not specify <code>--no-main-window</code> and then open Slicer in your web browser at the address: <code>localhost:8080</code></p>
<p>It would be useful to know if the file actually there and readable.</p>
</blockquote>
</aside>
<p>I could not get the gui via web browser to work in my docker file but got x11 to work and it looks like loading the dicom works when using the GUI (Slicer-5.6.1):</p>
<p>It was missing a db when I open it but used the same folder as the one in the script<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f09bfb38807ce118642a4a4b299cf0a106372ba0.png" data-download-href="/uploads/short-url/ykwMrzRCaMTe0R5nye0x4SAH3sA.png?dl=1" title="Screenshot from 2024-03-28 15-59-51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09bfb38807ce118642a4a4b299cf0a106372ba0_2_517x292.png" alt="Screenshot from 2024-03-28 15-59-51" data-base62-sha1="ykwMrzRCaMTe0R5nye0x4SAH3sA" width="517" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09bfb38807ce118642a4a4b299cf0a106372ba0_2_517x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09bfb38807ce118642a4a4b299cf0a106372ba0_2_775x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09bfb38807ce118642a4a4b299cf0a106372ba0_2_1034x584.png 2x" data-dominant-color="EFEFEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-03-28 15-59-51</span><span class="informations">1853×1048 68.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After that the dicom load normally and I can open it in the volume viewer and save it as a NIfTI:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e106da26479e6f11465bd4043ced7c1015780018.png" data-download-href="/uploads/short-url/w6G6UDlcPo5inFJOYFRrDVVWGmY.png?dl=1" title="Screenshot from 2024-03-28 16-03-29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e106da26479e6f11465bd4043ced7c1015780018_2_517x292.png" alt="Screenshot from 2024-03-28 16-03-29" data-base62-sha1="w6G6UDlcPo5inFJOYFRrDVVWGmY" width="517" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e106da26479e6f11465bd4043ced7c1015780018_2_517x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e106da26479e6f11465bd4043ced7c1015780018_2_775x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e106da26479e6f11465bd4043ced7c1015780018_2_1034x584.png 2x" data-dominant-color="E8ECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-03-28 16-03-29</span><span class="informations">1853×1048 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The SlicerDICOMTutorial data also worked:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd0705746c6b8774c31f0cab00d4ec68b6e3926.png" data-download-href="/uploads/short-url/oEMHAxBqAqSmlXEDr7NGN2qnIzk.png?dl=1" title="Screenshot from 2024-03-28 16-43-48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd0705746c6b8774c31f0cab00d4ec68b6e3926_2_517x292.png" alt="Screenshot from 2024-03-28 16-43-48" data-base62-sha1="oEMHAxBqAqSmlXEDr7NGN2qnIzk" width="517" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd0705746c6b8774c31f0cab00d4ec68b6e3926_2_517x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd0705746c6b8774c31f0cab00d4ec68b6e3926_2_775x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd0705746c6b8774c31f0cab00d4ec68b6e3926_2_1034x584.png 2x" data-dominant-color="EFF3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-03-28 16-43-48</span><span class="informations">1853×1048 86.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="35071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are you using the latest Slicer Stable Release (Slicer-5.6.1) or a Slicer Preview Release (Slicer-5.7.0)? There have been significant DICOM import changes in the preview release.</p>
</blockquote>
</aside>
<p>Before I was using Slicer-5.6.1 but here is the Slicer-5.7.0-2024-03-25-linux-amd64 output:</p>
<pre><code class="lang-auto">QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
...
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.

Could not load  "/db_temp/testdata/test-1/&lt;name&gt;.dcm" 
DCMTK says:  No such file or directory
File /db_temp/testdata/test-1/&lt;name&gt;.dcm could not be initialized.
....
Could not load  "/db_temp/testdata/test-1/&lt;name_n&gt;.dcm" 
DCMTK says:  No such file or directory
File /db_temp/testdata/test-1/&lt;name_n&gt;.dcm could not be initialized.

vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/testdata/test-1/&lt;name&gt;.dcm does not exist.


Algorithm vtkITKArchetypeImageSeriesScalarReader (0x7730cbd773a0) returned failure for request: vtkInformation (0x58d9670)
  Debug: Off
  Modified Time: 70392
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0

...
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /db_temp/testdata/test-1/&lt;name&gt;.sr does not exist.


Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7730cb9ea310) returned failure for request: vtkInformation (0x58dccb0)
  Debug: Off
  Modified Time: 73230
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Found nodes: []
</code></pre>
<p>Again thanks!</p>

---

## Post #10 by @lassoan (2024-03-28 16:09 UTC)

<p>To narrow down the issue, you can run the script using the GUI (copy-paste it to the Python console in Slicer), you can run the script without creating a temporary DICOM database, etc.</p>

---

## Post #11 by @SimonLBS (2024-03-28 17:25 UTC)

<p>It works in the GUI’s python console:</p>
<pre><code class="lang-auto">X Error: BadAccess (attempt to access private resource denied) 10
  Extension:    130 (MIT-SHM)
  Minor opcode: 1 (X_ShmAttach)
  Resource id:  0x10f
X Error: BadShmSeg (invalid shared segment parameter) 128
  Extension:    130 (MIT-SHM)
  Minor opcode: 5 (X_ShmCreatePixmap)
  Resource id:  0x2200009
X Error: BadDrawable (invalid Pixmap or Window parameter) 9
  Major opcode: 62 (X_CopyArea)
  Resource id:  0x220000a
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
MESA: error: Failed to query drm device.
libGL error: glx: failed to create dri3 screen
libGL error: failed to load driver: iris
Switch to module:  "Welcome"
Switch to module:  "DICOM"
Database folder does not contain ctkDICOM.sql file: /root/Documents/SlicerDICOMDatabase
TagCacheDatabase adding table

DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
...
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
"DICOM indexer has successfully inserted 3219 files [7.19s]"
"DICOM indexer has successfully processed 3219 files [9.76s]"
"DICOM indexer has updated display fields for 3219 files [1.25s]"
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
...
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
WARNING: In /work/Stable/Slicer-0-build/ITK/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx, line 478
ImageSeriesReader (0x9b23c30): Non uniform sampling or missing slices detected,  maximum nonuniformity:0.000992248


DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
WARNING: In /work/Stable/Slicer-0-build/ITK/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx, line 478
ImageSeriesReader (0x9b23c30): Non uniform sampling or missing slices detected,  maximum nonuniformity:0.000993976


DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /testdata/test-1/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /testdata/test-1/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x3e5a040) returned failure for request: vtkInformation (0xdd6c640)
  Debug: Off
  Modified Time: 395884
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /testdata/test-1/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /testdata/test-1/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x920f350) returned failure for request: vtkInformation (0xdb55290)
  Debug: Off
  Modified Time: 395979
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 100). Using ASCII encoding.
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /testdata/test-1/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /testdata/test-1/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0xd1f1c30) returned failure for request: vtkInformation (0xdb55330)
  Debug: Off
  Modified Time: 439171
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /testdata/test-1/&lt;name&gt;.sr. ITK exception info: error in unknown:  Could not create IO object for reading file /testdata/test-1/&lt;name&gt;.sr
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x920f350) returned failure for request: vtkInformation (0x9ac4e20)
  Debug: Off
  Modified Time: 439266
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Found nodes: ['vtkMRMLScalarVolumeNode1', 'vtkMRMLScalarVolumeNode2', 'vtkMRMLScalarVolumeNode3', 'vtkMRMLScalarVolumeNode4', 'vtkMRMLScalarVolumeNode5', 'vtkMRMLScalarVolumeNode6', 'vtkMRMLScalarVolumeNode7', 'vtkMRMLScalarVolumeNode8', 'vtkMRMLScalarVolumeNode9', 'vtkMRMLScalarVolumeNode10', 'vtkMRMLVectorVolumeNode1', 'vtkMRMLVectorVolumeNode2']
Saving 1_&lt;name&gt;...
...
Saving 27328_&lt;name&gt;...
</code></pre>
<p>Also if I first open Slicer, create a database in the dicom view, then close Slicer and then run the script with no temp db with the command <code>./Slicer/Slicer-5.6.1-linux-amd64/Slicer --no-main-window --python-script</code> it works but if I run the one with a temp db it does not work.</p>
<p>The one without temp db also does’t work if I have not first opened Slicer and created a db.</p>

---

## Post #12 by @lassoan (2024-03-31 04:03 UTC)

<p>Yes, you need to have a valid DICOM database.</p>
<p><code>DICOMUtils.TemporaryDICOMDatabase(temp_db)</code> should create a new database, so I’m not sure why that is not working.</p>
<p>You can have a look how <a href="https://github.com/Slicer/Slicer/blob/35ac3f451ee2c2a085596a78dd08d535f9568f99/Modules/Scripted/DICOM/DICOM.py#L520C9-L544">here</a> it is created when the application GUI is not disabled. If you don’t use a GUI then you can check the source code of the called methods (everything is on github) and call those methods in Python.</p>

---
