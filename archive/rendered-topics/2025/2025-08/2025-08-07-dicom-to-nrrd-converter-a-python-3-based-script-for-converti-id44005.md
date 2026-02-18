# [DICOM to NRRD Converter] A Python 3 - based script for converting DICOM to nrrd

**Topic ID**: 44005
**Date**: 2025-08-07
**URL**: https://discourse.slicer.org/t/dicom-to-nrrd-converter-a-python-3-based-script-for-converting-dicom-to-nrrd/44005

---

## Post #1 by @Unicom (2025-08-07 15:32 UTC)

<h3><a name="p-127466-dicom-to-nrrd-converter-a-python-3-based-script-for-converting-dicom-to-nrrd-1" class="anchor" href="#p-127466-dicom-to-nrrd-converter-a-python-3-based-script-for-converting-dicom-to-nrrd-1" aria-label="Heading link"></a>[DICOM to NRRD Converter] A Python 3 - based script for converting DICOM to nrrd</h3>
<p>Currently, there are no very good methods or extensions available for efficient loading of large-size DICOM data. Spending some time converting it into a single-file nrrd format is one feasible approach. However, this only alleviates the loading process; rotation or cropping operations during the actual segmentation process are still very laggy.</p>
<h4><a name="p-127466-test-process-information-2" class="anchor" href="#p-127466-test-process-information-2" aria-label="Heading link"></a><strong>Test process information</strong></h4>
<hr>
<ul>
<li>
<p>Data size</p>
<ul>
<li>Source volume: 2GB</li>
<li>Converted nrrd file: 900MB</li>
</ul>
</li>
<li>
<p>Loading time</p>
<ul>
<li>DICOM: 4 min</li>
<li>nrrd: 8 seconds</li>
</ul>
</li>
<li>
<p>Loading result</p>
<ul>
<li>Error, half of the volume did not load</li>
<li>No problem</li>
</ul>
</li>
</ul>
<h4><a name="p-127466-dicom2nrrdpy-source-code-python-3-3" class="anchor" href="#p-127466-dicom2nrrdpy-source-code-python-3-3" aria-label="Heading link"></a><strong>dicom2nrrd.py Source code (Python 3)</strong></h4>
<hr>
<pre data-code-wrap="python"><code class="lang-python"># -*- coding: utf-8 -*-
# DICOM_to_NRRD.py
"""
Batch transform DICOM images to NRRD images
Dependencies:
- Python Library: pydicom, pynrrd, tqdm (optional, for better progress bars)
- Third party softwares: gdcm (accessible via command line)

Usage:
python DICOM_to_NRRD.py -i /path/to/input/folder -o /path/to/output/folder
"""

import glob
import subprocess
import sys
import os
import getopt
import numpy
import tempfile
import time # For timing
from datetime import datetime # For timestamp in summary

# Try importing tqdm for better progress bars
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    print("Info: 'tqdm' library not found. Install it with 'pip install tqdm' for better progress bars.")

# Updated import for pydicom
try:
    import pydicom as dicom
except ImportError:
    print("Error: pydicom library is required. Install it using 'pip install pydicom'")
    sys.exit(1)

# Ensure pynrrd is installed
try:
    import nrrd
except ImportError:
    print("Error: pynrrd library is required. Install it using 'pip install pynrrd'")
    sys.exit(1)


class DICOM_to_NRRD:
    def __init__(self):
        self.BACKGROUND = -2048
        self.AIR = -1024
        # Removed KEY_WORD_FOLDER and KEY_WORD_FILE as they are no longer needed

    def batch_dicom_to_nrrd(self, dicom_root, nrrd_root):
        """Iteratively convert all dicom data in dicom_root to nrrd.
        Processes each subdirectory within dicom_root.
        """
        print("--- Batch DICOM to NRRD Conversion Started ---")
        start_time = time.time()
        processed_folders = []
        failed_folders = []

        # Use os.path.join for better cross-platform compatibility
        dicom_files_dirs = glob.glob(os.path.join(dicom_root, '*'))
        total_folders = len([d for d in dicom_files_dirs if os.path.isdir(d)])
        print(f"Found {total_folders} subject folder(s) to process.")

        # Use tqdm if available for overall progress, otherwise simple counter
        if TQDM_AVAILABLE:
            folder_iterator = tqdm(dicom_files_dirs, desc="Processing Folders", unit="folder")
        else:
            folder_iterator = dicom_files_dirs
            processed_count = 0

        for dicom_subject_path in folder_iterator:
            if os.path.isdir(dicom_subject_path):
                subject_folder_name = os.path.basename(dicom_subject_path)
                if not subject_folder_name:
                    print(f"Warning: Could not determine folder name for {dicom_subject_path}. Skipping.")
                    failed_folders.append(dicom_subject_path)
                    continue

                nrrd_subject = os.path.join(nrrd_root, subject_folder_name)
                try:
                    success = self.dicom_to_nrrd(dicom_subject_path, nrrd_subject)
                    if success:
                        processed_folders.append(nrrd_subject)
                    else:
                        failed_folders.append(dicom_subject_path)
                except Exception as e:
                    print(f"\nError during conversion of {dicom_subject_path}: {e}")
                    failed_folders.append(dicom_subject_path)
                
                # Update tqdm description or simple counter
                if TQDM_AVAILABLE:
                    # tqdm handles this automatically
                    pass
                else:
                    processed_count += 1
                    print(f"  Progress: {processed_count}/{total_folders} folders processed.")

        end_time = time.time()
        duration = end_time - start_time
        self._print_summary(processed_folders, failed_folders, duration, nrrd_root)
        print("--- Batch DICOM to NRRD Conversion Finished ---")

    def _print_summary(self, processed_folders, failed_folders, duration, output_root):
        """Prints a formatted summary of the conversion process."""
        print("\n" + "="*50)
        print("         CONVERSION SUMMARY")
        print("="*50)
        print(f"Start Time:     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Duration:       {duration:.2f} seconds")
        print(f"Output Root:    {output_root}")
        print("-" * 50)
        print(f"Successful:     {len(processed_folders)} folder(s)")
        for path in processed_folders:
            print(f"  - {path}")
        print("-" * 50)
        print(f"Failed:         {len(failed_folders)} folder(s)")
        for path in failed_folders:
            print(f"  - {path}")
        print("="*50 + "\n")


    def batch_preprocess(self, input_folder, output_folder, padding=20):
        """Pad all images in the input folder.
        This function processes .nrrd files and can modify data.
        """
        input_files = glob.glob(os.path.join(input_folder, '*.nrrd'))
        for input_path in input_files:
            filename = os.path.basename(input_path)
            output_path = os.path.join(output_folder, filename)
            try:
                data, options = nrrd.read(input_path)
                data, options = self.filter_background_to_air(data, options)
                # Padding is disabled by default here to preserve CT range.
                # data, options = self.pad_upper(data, options, padding)
                print(f'Writing {output_path}')
                nrrd.write(output_path, data, options)
            except Exception as e:
                print(f"Error processing {input_path}: {e}")


    def dicom_to_nrrd(self, dicom_root_dir, nrrd_files_dir):
        """Transfer dicom volume into nrrd format"""
        # Use tempfile for safer temporary file handling
        with tempfile.NamedTemporaryFile(delete=False, suffix='.dcm') as tmp_file:
            TEMP_FILE = tmp_file.name
        try:
            SYSTEM_COMMAND = 'gdcmconv -w {0} {1}'

            parent_dir_name = os.path.basename(os.path.normpath(dicom_root_dir))

            potential_dicom_items = glob.glob(os.path.join(dicom_root_dir, '*'))
            has_subfolders = any(os.path.isdir(item) for item in potential_dicom_items)

            folders_to_process = []
            if has_subfolders:
                folders_to_process = [item for item in potential_dicom_items if os.path.isdir(item)]
            else:
                folders_to_process = [dicom_root_dir]

            # --- Handle single folder vs multiple subfolders ---
            if len(folders_to_process) == 1 and folders_to_process[0] == dicom_root_dir:
                 # Process the main folder directly
                 folders_to_iterate = [(0, dicom_root_dir)] # (index, path)
                 base_name_for_files = parent_dir_name
            else:
                 # Process subfolders
                 folders_to_iterate = list(enumerate(folders_to_process))
                 base_name_for_files = parent_dir_name
            # --- End Handle ---

            success_flag = True # Flag to indicate if at least one file was processed successfully

            for i, subject_folder in folders_to_iterate:
                
                # --- Determine output filename ---
                if subject_folder == dicom_root_dir and len(folders_to_process) == 1:
                    # Processing main folder directly
                    nrrd_file = os.path.join(nrrd_files_dir, f"{base_name_for_files}_{i+1:02d}.nrrd")
                else:
                    # Processing a subfolder
                    subfolder_name = os.path.basename(subject_folder)
                    nrrd_file = os.path.join(nrrd_files_dir, f"{base_name_for_files}_{subfolder_name}_{i+1:02d}.nrrd")
                # --- End Determine ---
                
                print(f'\nProcessing {nrrd_file}')

                if not os.path.exists(nrrd_files_dir):
                    os.makedirs(nrrd_files_dir)

                data_3d = None
                # --- MODIFIED FILE SELECTION LOGIC ---
                dicom_files = [
                    f for f in glob.glob(os.path.join(subject_folder, '*'))
                    if (not os.path.splitext(f)[1] and not f.lower().endswith('.nrrd')) or f.lower().endswith('.dcm')
                ]
                if not dicom_files:
                    dicom_files = [f for f in glob.glob(os.path.join(subject_folder, '*')) if not f.lower().endswith('.nrrd')]

                dicom_files = sorted(dicom_files)
                # --- END MODIFIED FILE SELECTION LOGIC ---

                if not dicom_files:
                    print(f"Warning: No files found in {subject_folder}")
                    success_flag = False # Mark as not successful if no files
                    continue

                total_files = len(dicom_files)
                # --- PROGRESS BAR ---
                if TQDM_AVAILABLE:
                    file_pbar = tqdm(total=total_files, desc="  Slices", unit="slice", leave=False)
                else:
                    print(f"  Slices: 0/{total_files}", end='', flush=True)
                # --- END PROGRESS BAR ---

                for j, dicom_file in enumerate(dicom_files):
                    # --- PROGRESS UPDATE ---
                    if TQDM_AVAILABLE:
                        file_pbar.update(1)
                    else:
                        # Simple text progress update
                        print(f"\r  Slices: {j+1}/{total_files}", end='', flush=True)
                    # --- END PROGRESS UPDATE ---

                    try:
                        result = subprocess.run(
                            SYSTEM_COMMAND.format(dicom_file, TEMP_FILE).split(),
                            check=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                    except subprocess.CalledProcessError as e:
                        print(f"\nError: gdcmconv failed for {dicom_file}.")
                        print(f"Command: {e.cmd}")
                        # print(f"Error output: {e.stderr}") # Optional verbose error
                        success_flag = False
                        continue
                    except FileNotFoundError:
                        print(f"\nError: gdcmconv command not found. Please ensure GDCM is installed and accessible.")
                        success_flag = False
                        # sys.exit(1) # Or continue with other folders?
                        continue
                    except Exception as e:
                        print(f"\nUnexpected error running gdcmconv for {dicom_file}: {e}")
                        success_flag = False
                        continue

                    try:
                        ds = dicom.dcmread(TEMP_FILE)
                        data = ds.pixel_array
                        data_3d = self.concatenate_layers(data_3d, data)
                    except Exception as e:
                        print(f"\nError reading DICOM file {TEMP_FILE} (from {dicom_file}): {e}")
                        success_flag = False
                        continue

                # --- FINAL PROGRESS UPDATE TO 100% ---
                if not TQDM_AVAILABLE and total_files &gt; 0:
                    print(f"\r  Slices: {total_files}/{total_files} (100%)") # Force 100%
                elif TQDM_AVAILABLE:
                    file_pbar.close() # Close the file progress bar
                # --- END FINAL PROGRESS ---

                if data_3d is None:
                    print(f"\nWarning: No valid DICOM data loaded for {subject_folder}. Skipping NRRD creation.")
                    success_flag = False
                    continue

                try:
                    options = self.load_dicom_options(TEMP_FILE, len(dicom_files))
                except Exception as e:
                    print(f"\nError loading DICOM options from {TEMP_FILE}: {e}")
                    success_flag = False
                    continue

                data_3d = numpy.swapaxes(data_3d, 0, 1)
                data_3d = data_3d[:, :, ::-1]

                # CT value modification and padding are disabled by default here.
                # data_3d, options = self.filter_background_to_air(data_3d, options)
                # data_3d, options = self.pad_upper(data_3d, options, padding_value)

                try:
                    nrrd.write(nrrd_file, data_3d, options)
                    print(f"  -&gt; Saved {nrrd_file}")
                except Exception as e:
                    print(f"\nError writing NRRD file {nrrd_file}: {e}")
                    success_flag = False

            return success_flag # Return overall success for this dicom_root_dir

        finally:
            if os.path.exists(TEMP_FILE):
                os.remove(TEMP_FILE)


    def load_dicom_options(self, file_name, number_of_dicoms):
        ds = dicom.dcmread(file_name)
        options = dict()
        options['type'] = 'short'
        options['dimension'] = 3
        options['space'] = 'left-posterior-superior'
        
        pixel_spacing = getattr(ds, 'PixelSpacing', [1.0, 1.0])
        try:
            pixel_spacing = [float(p) for p in pixel_spacing]
        except (ValueError, TypeError):
            print(f"Warning: Invalid PixelSpacing {pixel_spacing}. Using defaults [1.0, 1.0]")
            pixel_spacing = [1.0, 1.0]

        slice_thickness = float(getattr(ds, 'SliceThickness', 1.0))

        options['space directions'] = [
            [pixel_spacing[0], 0, 0],
            [0, pixel_spacing[1], 0],
            [0, 0, slice_thickness]
        ]
        options['kinds'] = ['domain', 'domain', 'domain']
        # options['encoding'] = 'gzip'
        
        image_position = getattr(ds, 'ImagePositionPatient', [0.0, 0.0, 0.0])
        try:
            image_position = [float(p) for p in image_position]
        except (ValueError, TypeError):
            print(f"Warning: Invalid ImagePositionPatient {image_position}. Using defaults [0.0, 0.0, 0.0]")
            image_position = [0.0, 0.0, 0.0]
        options['space origin'] = image_position

        if hasattr(ds, 'Rows') and hasattr(ds, 'Columns'):
            options['sizes'] = [ds.Columns, ds.Rows, number_of_dicoms]
        else:
            print("Warning: Could not determine DICOM dimensions from metadata.")

        return options

    def concatenate_layers(self, data_3d, data):
        """Concatenates 2D slices into a 3D volume with robust error handling."""
        try:
            if data_3d is None:
                if data.ndim == 2:
                    return data[:, :, numpy.newaxis]
                else:
                    print(f"Warning: First slice is not 2D (ndim={data.ndim}). Attempting to use as-is.")
                    return data

            if data.ndim != 2:
                 print(f"Warning: Slice is not 2D (ndim={data.ndim}). Attempting to stack.")
                 if data.ndim == 1:
                     print(f"Error: Cannot stack 1D slice. Skipping.")
                     return data_3d
                 try:
                     data = data[..., 0]
                     if data.ndim != 2:
                         raise ValueError("Extracted slice is still not 2D")
                 except Exception:
                     print(f"Error: Could not extract 2D data from &gt;2D slice. Skipping.")
                     return data_3d
            
            data_to_stack = data[:, :, numpy.newaxis]
            return numpy.concatenate((data_3d, data_to_stack), axis=2)

        except Exception as e:
            print(f"\nWarning during concatenation: {e}. Skipping slice.")
            return data_3d


    def filter_background_to_air(self, data, options):
        """Change value -2048 (background) to -1024 (air)"""
        data[data &lt;= self.BACKGROUND] = self.AIR
        return (data, options)

    def pad_upper(self, data, options, padding):
        """Padding functionality warning."""
        print(f"Warning: pad_upper called with padding={padding}, but is disabled by default.")
        print("         To enable, modify the pad_upper method implementation.")
        return (data, options)
        # --- OLD IMPLEMENTATION (FOR REFERENCE IF RE-ENABLING) ---
        # if padding &lt;= 0:
        #     return (data, options)
        # if data.ndim != 3:
        #     print(f"Warning: pad_upper expects 3D data, got {data.ndim}D. Skipping padding.")
        #     return (data, options)
        # rows, columns, depths = data.shape
        # padding_layer = numpy.full((rows, columns), self.AIR, dtype=data.dtype)
        # padding_volume = numpy.repeat(padding_layer[:, :, numpy.newaxis], padding, axis=2)
        # data = numpy.concatenate((data, padding_volume), axis=2)
        # if 'sizes' in options and len(options['sizes']) == 3:
        #     options['sizes'][2] += padding
        # return (data, options)
        # --- END OLD IMPLEMENTATION ---


def main(argv):
    # --- PRINT BASIC INFO ---
    print("=" * 60)
    print("DICOM to NRRD Converter")
    print("=" * 60)
    print(f"Python Version: {sys.version}")
    print(f"Script Path:    {os.path.abspath(__file__)}")
    print(f"Start Time:     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    # --- END PRINT BASIC INFO ---

    dicom_root = ''
    nrrd_root = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('DICOM_to_NRRD.py -i &lt;input_folder&gt; -o &lt;output_folder&gt;')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('DICOM_to_NRRD.py -i &lt;input_folder&gt; -o &lt;output_folder&gt;')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            dicom_root = arg
        elif opt in ("-o", "--ofile"):
            nrrd_root = arg

    if not dicom_root or not nrrd_root:
        print('Both input (-i) and output (-o) folders are required.')
        print('DICOM_to_NRRD.py -i &lt;input_folder&gt; -o &lt;output_folder&gt;')
        sys.exit(2)

    if not os.path.isdir(dicom_root):
        print(f"Error: Input folder '{dicom_root}' does not exist or is not a directory.")
        sys.exit(1)

    converter = DICOM_to_NRRD()
    converter.batch_dicom_to_nrrd(dicom_root, nrrd_root)

if __name__ == "__main__":
    main(sys.argv[1:])

</code></pre>
<h4><a name="p-127466-prepare-the-environment-4" class="anchor" href="#p-127466-prepare-the-environment-4" aria-label="Heading link"></a><strong>Prepare the environment</strong></h4>
<hr>
<pre><code class="lang-auto">Install Python 3
pip install pydicom pynrrd numpy tqdm
install GDCM
put dicom2nrrd.py into GDCM-x.x.xx-Windows-x86_64\bin folder
</code></pre>
<h4><a name="p-127466-running-snapshot-gif-animation-5" class="anchor" href="#p-127466-running-snapshot-gif-animation-5" aria-label="Heading link"></a><strong>Running snapshot (gif animation)</strong></h4>
<hr>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/662d86380cdfaeb9cecacc92e2b8650045d58e31.gif" alt="dicom2nrrd" data-base62-sha1="ezUeIj9i4wYh5gkOEBVmV93OFjP" width="690" height="466" class="animated"></p>
<h4><a name="p-127466-note-6" class="anchor" href="#p-127466-note-6" aria-label="Heading link"></a><strong>Note</strong></h4>
<hr>
<p>There is still room for further development in areas such as NRRD compression, batch processing of patients, and format validation. This is just a concept provided as a reference for those encountering the same issues.</p>

---

## Post #2 by @muratmaga (2025-08-07 16:32 UTC)

<p>Thank you for sharing these.</p>
<p>I don’t work with DICOM datasets routinely nowadays, but when I do, my experience is that most of the issue is not due to the lack of tools, but rather incorrect implementation of the standard by the vendors (or whoever did the image to dicom conversion) and what to do about it.</p>
<p>I was part of a group which just finished a paper in which the primary author demonstrated  that an incorrectly specified dicom tag and how that is handled by the software (and the user) can generate measurement errors as large as 15%. I will share it once it is public.</p>
<p>The main issue is how you want to handle these exception (typical choices are: ignore it, silently apply a fix that you think corrects the issue, report to user and let them sort it out), along with potential privacy concerns. In my experience that usually the real bottleneck when you are trying to convert large number of DICOMs.</p>
<p>I personnally liked [DCM2NIIX](<a href="https://github.com/rordenlab/dcm2niix" class="inline-onebox">GitHub - rordenlab/dcm2niix: dcm2nii DICOM to NIfTI converter: compiled versions available from NITRC</a>) as a tool to do batch conversions of DICOM files into NRRD. It does generate an output that you can see if there are issues during the conversion, and if any, what fixes has applied. I haven’t used it a few years, but it was also very fast during the conversion (though I did not try with a 2GB DICOM sequence).</p>

---

## Post #3 by @pieper (2025-08-07 17:05 UTC)

<p>Thanks <a class="mention" href="/u/unicom">@Unicom</a> for sharing your code as a reference for others.</p>
<p>I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a> that incorrectly encoded DICOM files from vendors is a problem, particularly for microCT and other non-medical sources, but also valid DICOM files can come in a wide variety for configurations that require careful analysis and processing in order to correctly make use of them.  This is partly due to the wide variety of ways people collect images (e.g. CT vs MR or volumetric vs time series) and things you want to encode (segmentations, transformations, etc).  Also NRRD itself if pretty flexible in terms of what can be represented so there’s no one-size-fits-all conversion option.</p>

---

## Post #4 by @Unicom (2025-08-08 02:24 UTC)

<h2><a name="p-127494-thank-you-1" class="anchor" href="#p-127494-thank-you-1" aria-label="Heading link"></a>Thank you</h2>
<hr>
<p>Thank you very much for your guidance; it has been a great help to me. It’s like you opened a door for me, revealing a treasure trove of knowledge inside.<br>
The existing tools can fully solve the problems my script needs to address, and they are more efficient and multifunctional.</p>
<p>Below is my test information shared for others who encounter the same issues:</p>
<h2><a name="p-127494-dcm2niixexe-2" class="anchor" href="#p-127494-dcm2niixexe-2" aria-label="Heading link"></a>dcm2niix.exe</h2>
<hr>
<pre><code class="lang-auto">dcm2niix.exe -v 3 -z y -o D:\\Temp\\output-folder D:\\Temp\\input-folder
</code></pre>
<p>By placing the pigz.exe parallel compression program in the same directory as dcm2niix.exe, the overall DICOM conversion speed is very fast; a 2GB DICOM can be converted to nii.gz in just 35 seconds. However, it does not support conversion to the nrrd format.</p>
<h2><a name="p-127494-plastimatchexe-3" class="anchor" href="#p-127494-plastimatchexe-3" aria-label="Heading link"></a>plastimatch.exe</h2>
<hr>
<pre><code class="lang-auto">plastimatch.exe convert --input “D:\\Temp\\input-folder” --output-img “D:\\Temp\\output-folder\\image.nrrd”
</code></pre>
<p>This can convert DICOM to nrrd, and the speed is very fast.</p>
<h2><a name="p-127494-githubcomrordenlabdcm2niix-4" class="anchor" href="#p-127494-githubcomrordenlabdcm2niix-4" aria-label="Heading link"></a><code>github.com/rordenlab/dcm2niix</code></h2>
<hr>
<pre><code class="lang-auto">https://github.com/rordenlab/dcm2niix
</code></pre>
<p>This page contains an introduction to dcm2niix, and there are many DICOM-related tools available, very comprehensive.</p>

---

## Post #5 by @muratmaga (2025-08-08 04:09 UTC)

<aside class="quote no-group" data-username="Unicom" data-post="4" data-topic="44005">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/unicom/48/15532_2.png" class="avatar"> Unicom:</div>
<blockquote>
<p>However, it does not support conversion to the nrrd format.</p>
</blockquote>
</aside>
<p>I believe all you have to do is to name the output file nrrd. This is from the DCM2NIIX documentation:</p>
<pre><code class="lang-auto">Note, recent versions of dcm2niix can directly convert DICOM images to NRRD.
</code></pre>

---

## Post #6 by @Unicom (2025-08-08 05:40 UTC)

<p>Thank you again.</p>
<h2><a name="p-127499-uncompressed-nrrd-1" class="anchor" href="#p-127499-uncompressed-nrrd-1" aria-label="Heading link"></a>uncompressed nrrd</h2>
<hr>
<p>Convert dicom to uncompressed nrrd format, 2GB converted volume is 430MB:</p>
<pre><code class="lang-auto">dcm2niix.exe -v 2 -o -e y D:\Temp\output-folder D:\Temp\input-folder
</code></pre>
<p>export file：</p>
<ul>
<li>ST000001_Head_lung_ChestPainECG.nrrd</li>
</ul>
<h2><a name="p-127499-compressed-nrrd-2" class="anchor" href="#p-127499-compressed-nrrd-2" aria-label="Heading link"></a>compressed nrrd</h2>
<hr>
<p>Convert dicom to compressed nrrd format, 2GB converted volume is 240MB:</p>
<pre><code class="lang-auto">dcm2niix.exe -v 3 -z y -e y -o D:\Temp\output-folder D:\Temp\input-folder
</code></pre>
<ul>
<li>ST000001_Head_lung_ChestPainECG.raw.gz</li>
<li>ST000001_Head_lung_ChestPainECG.nhdr</li>
</ul>
<h2><a name="p-127499-dcm2niix-parameters-3" class="anchor" href="#p-127499-dcm2niix-parameters-3" aria-label="Heading link"></a>dcm2niix parameters:</h2>
<hr>
<pre><code class="lang-auto">Chris Rorden's dcm2niiX version v1.0.20250505  (JP2:OpenJPEG) (JP-LS:CharLS) MSC1942  (64-bit Windows)
usage: dcm2niix.exe [options] &lt;in_folder&gt;
 Options :
  -1..-9 : gz compression level (1=fastest..9=smallest, default 6)
  -a : adjacent DICOMs (images from same series always in same folder) for faster conversion (n/y, default n)
  -b : BIDS sidecar (y/n/o [o=only: no NIfTI], default y)
   -ba : anonymize BIDS (y/n, default y)
  -c : comment stored in NIfTI aux_file (up to 24 characters e.g. '-c VIP', empty to anonymize e.g. 0020,4000 e.g. '-c ""')
  -d : directory search depth. Convert DICOMs in sub-folders of in_folder? (0..9, default 5)
  -e : export as NRRD (y) or MGH (o) or JSON/JNIfTI (j) or BJNIfTI (b) instead of NIfTI (y/n/o/j/b, default n)
  -f : filename (%a=antenna (coil) name, %b=basename, %c=comments, %d=description, %e=echo number, %f=folder name, %g=accession number, %i=ID of patient, %j=seriesInstanceUID, %k=studyInstanceUID, %m=manufacturer, %n=name of patient, %o=mediaObjectInstanceUID, %p=protocol, %r=instance number, %s=series number, %t=time, %u=acquisition number, %v=vendor, %x=study ID; %z=sequence name; default '%f_%p_%t_%s')
  -g : generate defaults file (y/n/o/i [o=only: reset and write defaults; i=ignore: reset defaults], default n)
  -h : show help
  -i : ignore derived, localizer and 2D images (y/n, default n)
  -l : losslessly scale 16-bit integers to use dynamic range (y/n/o [yes=scale, no=no, but uint16-&gt;int16, o=original], default o)
  -m : merge 2D slices from same series regardless of echo, exposure, etc. (n/y or 0/1/2, default 2) [no, yes, auto]
  -n : only convert this series CRC number - can be used up to 16 times (default convert all)
  -o : output directory (omit to save to input folder)
  -p : Philips precise float (not display) scaling (y/n, default y)
  -q : only search directory for DICOMs (y/l/n, default y) [y=show number of DICOMs found, l=additionally list DICOMs found, n=no]
  -r : rename instead of convert DICOMs (y/n, default n)
  -s : single file mode, do not convert other images in folder (y/n, default n)
  -v : verbose (n/y or 0/1/2, default 0) [no, yes, logorrheic]
  -w : write behavior for name conflicts (0,1,2, default 2: 0=skip duplicates, 1=overwrite, 2=add suffix)
  -x : crop 3D acquisitions (y/n/i, default n, use 'i'gnore to neither crop nor rotate 3D acquisitions)
  -z : gz compress images (y/i/n/3, default n) [y=pigz, i=internal:zlib, n=no, 3=no,3D]
  --big-endian : byte order (y/n/o, default o) [y=big-end, n=little-end, o=optimal/native]
  --progress : report progress (y/n, default n)
  --ignore_trigger_times : disregard values in 0018,1060 and 0020,9153
  --terse : omit filename post-fixes (can cause overwrites)
  --version : report version
  --xml : Slicer format features
 Defaults stored in Windows registry

</code></pre>

---

## Post #7 by @Fernando (2025-08-12 19:37 UTC)

<p>You might be interested in this little wrapper of dcm2niix I wrote recently with the most commonly used parameters (by me). You can install it with <code>pip install dcm2niiw</code>, or just run it with <a href="https://docs.astral.sh/uv/" rel="noopener nofollow ugc">uv</a>:</p>
<pre data-code-wrap="shell"><code class="lang-shell">uvx dcm2niiw --help
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/877d78fd70fb9201105e545c08c563d207f49ce8.jpeg" data-download-href="/uploads/short-url/jkBhvmFzCqLXfqis7ZRJLIKNCtO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877d78fd70fb9201105e545c08c563d207f49ce8_2_494x500.jpeg" alt="image" data-base62-sha1="jkBhvmFzCqLXfqis7ZRJLIKNCtO" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877d78fd70fb9201105e545c08c563d207f49ce8_2_494x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877d78fd70fb9201105e545c08c563d207f49ce8_2_741x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877d78fd70fb9201105e545c08c563d207f49ce8_2_988x1000.jpeg 2x" data-dominant-color="31313C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1706×1724 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Unicom (2025-08-13 03:20 UTC)

<p>Thank you Fernando, very good tool. <a href="https://github.com/fepegar/dcm2niiw" rel="noopener nofollow ugc">https://github.com/fepegar/dcm2niiw</a></p><aside class="onebox githubrepo" data-onebox-src="https://github.com/fepegar/dcm2niiw">
  <header class="source">

      <a href="https://github.com/fepegar/dcm2niiw" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/bd276ae31b296f711e744b1dbad3a842/fepegar/dcm2niiw" class="thumbnail">

  <h3><a href="https://github.com/fepegar/dcm2niiw" target="_blank" rel="noopener nofollow ugc">GitHub - fepegar/dcm2niiw: Thin wrapper of dcm2niix with Python and CLI...</a></h3>

    <p><span class="github-repo-description">Thin wrapper of dcm2niix with Python and CLI interfaces.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h2><a name="p-127611-running-information-1" class="anchor" href="#p-127611-running-information-1" aria-label="Heading link"></a>Running Information</h2>
<hr>
<pre><code class="lang-auto">C:\Users\user&gt;uvx dcm2niiw --compression-level 9 -e nrrd D:\input D:\output
2025-0x-xx xx:xx:01 | DEBUG    | The following command will be run:
2025-0x-xx xx:xx:01 | DEBUG    |
C:\Users\user\AppData\Local\uv\cache\archive-v0\vWH0nAjhCJlcZFOkjHL0k\Lib\site-packages\dcm2niix\dcm2niix \
  -a n \
  -d 5 \
  -e y \
  -f %j \
  -i n \
  -v 0 \
  -z y \
  -w 1 \
  -9 \
  -o D:\output \
  D:\input
2025-0x-xx xx:xx:02 | DEBUG    | Chris Rorden's dcm2niiX version v1.0.20250505  MSC1943  (64-bit Windows)
2025-0x-xx xx:xx:02 | INFO     | Found 861 DICOM file(s)
2025-0x-xx xx:xx:02 | WARNING  | Issue797: Check slice timing range 0..27.7812, TA= 27.7812, TR=0 ms)
2025-0x-xx xx:xx:02 | INFO     | Convert 861 DICOM as D:\output\1.3.12.2.1107.5.1.4.64134.xx (512x512x861x1)
2025-0x-xx xx:xx:02 | SUCCESS  | Conversion required 60.678001 seconds.
</code></pre>

---
