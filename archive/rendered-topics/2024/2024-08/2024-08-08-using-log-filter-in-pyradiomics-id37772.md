# Using LoG filter in PyRadiomics

**Topic ID**: 37772
**Date**: 2024-08-08
**URL**: https://discourse.slicer.org/t/using-log-filter-in-pyradiomics/37772

---

## Post #1 by @arflores (2024-08-08 09:40 UTC)

<p>Hello all,</p>
<p>I am trying to use the LoG filter in Pyradiomics. I have been successful with the other filters using the enableImageTypeByName (imageType, enabled=True). But when I use ‘LoG’, I do not get the LoG results, just the original (no filter) ones. The output for the print(Enabled features) reports both original and LoG are enabled. No errors or issues are reported. But again, just the original (no filter) results are the output. Below is the code. Any help?</p>
<pre data-code-wrap="python"><code class="lang-python">import os
from radiomics.featureextractor import RadiomicsFeatureExtractor
import SimpleITK as sitk

# Define paths to your image and mask
source = '/Users/alexflores/Desktop/Mrn_1/Mrn_1_source.nii.gz'
mask = '/Users/alexflores/Desktop/Mrn_1/Mrn_1_T1tmask.nii.gz'

# Load images
image = sitk.ReadImage(source)
mask_image = sitk.ReadImage(mask)

# Initialize the feature extractor
extractor = RadiomicsFeatureExtractor()

# Enable specific image types
try:
    extractor.enableImageTypeByName('LoG', enabled=True)
except Exception as e:
    print(f"Error enabling LoG image type: {e}")

# Print settings to confirm changes
print('Extraction parameters:\n\t', extractor.settings)
print('Enabled filters:\n\t', extractor.enabledImagetypes)
print('Enabled features:\n\t', extractor.enabledFeatures)

# Extract features from the image and mask
try:
    result = extractor.execute(source, mask)
    print('Result type:', type(result))

    # Print calculated features
    print('Calculated features:')
    for key, value in result.items():
        print('\t', key, ':', value)

except Exception as e:
    print('An error occurred:', e)

# Convertfeaturevaluestonumpyarray
import numpy as np
import csv


# Define the CSV file path
csv_file_path = '/Users/alexflores/Desktop/features.csv'

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header (column names)
    writer.writerow(['Feature', 'Value'])

    # Write each feature and its value
    for key, value in result.items():
        # Handle dictionary values (convert to string)
        if isinstance(value, dict):
            value = str(value)
        writer.writerow([key, value])

print(f"Data has been written to {csv_file_path}")
</code></pre>

---

## Post #2 by @arflores (2024-08-08 21:51 UTC)

<p>In followup to the above post, I have since discovered the likely issue was that the output of the getLoGImage seems to be a generator. Which I have been able to convert to a sitk image but still I cannot get the feature values from this LoG filtered imaged.</p>
<h1><a name="p-114959-log-1" class="anchor" href="#p-114959-log-1" aria-label="Heading link"></a><span class="hashtag-raw">#LoG</span></h1>
<p>import os<br>
import SimpleITK as sitk<br>
from radiomics.imageoperations import getLoGImage<br>
from radiomics.featureextractor import RadiomicsFeatureExtractor<br>
import csv</p>
<h1><a name="p-114959-define-paths-to-your-image-and-mask-2" class="anchor" href="#p-114959-define-paths-to-your-image-and-mask-2" aria-label="Heading link"></a>Define paths to your image and mask</h1>
<p>source = ‘/Users/alexflores/Desktop/Mrn_1/Mrn_1_source.nii.gz’<br>
mask = ‘/Users/alexflores/Desktop/Mrn_1/Mrn_1_T1tmask.nii.gz’</p>
<h1><a name="p-114959-load-images-3" class="anchor" href="#p-114959-load-images-3" aria-label="Heading link"></a>Load images</h1>
<p>image = sitk.ReadImage(source)<br>
mask_image = sitk.ReadImage(mask)</p>
<h1><a name="p-114959-parameters-for-the-log-filter-4" class="anchor" href="#p-114959-parameters-for-the-log-filter-4" aria-label="Heading link"></a>Parameters for the LoG filter</h1>
<p>kwargs = {‘sigma’: [1.0]}  # Example sigma value</p>
<h1><a name="p-114959-apply-the-log-filter-5" class="anchor" href="#p-114959-apply-the-log-filter-5" aria-label="Heading link"></a>Apply the LoG filter</h1>
<p>try:<br>
log_image_generator = getLoGImage(inputImage=image, inputMask=mask_image, **kwargs)</p>
<pre><code># Check contents of the generator
log_images = list(log_image_generator)
print(f"Number of items in generator: {len(log_images)}")

if log_images:
    first_item = log_images[0]
    print(f"Type of first item in generator: {type(first_item)}")
    print(f"First item content: {first_item}")

    # Unpack the tuple if needed
    if isinstance(first_item, tuple):
        # Assume the first item is the SimpleITK Image
        log_image = first_item[0]  # Adjust based on actual content of tuple

        if isinstance(log_image, sitk.Image):
            print(f"Successfully obtained LoG image.")
            print(f"Image size: {log_image.GetSize()}")

            # Initialize the feature extractor
            extractor = RadiomicsFeatureExtractor()
            extractor.enableImageTypeByName('LoG', enabled=True)

            # Extract features from the image and mask
            result = extractor.execute(log_image, mask_image)

            # Print the type of result
            print('Result type:', type(result))

            # Print and save calculated features
            csv_file_path = '/Users/alexflores/Desktop/features.csv'

            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Feature', 'Value'])

                for key, value in result.items():
                    if isinstance(value, dict):
                        value = str(value)
                    writer.writerow([key, value])

            print(f"Data has been written to {csv_file_path}")

        else:
            print("No valid LoG image was obtained from the generator.")
    else:
        print("The generator did not produce a tuple with a SimpleITK image.")
</code></pre>
<p>except Exception as e:<br>
print(f"An error occurred: {e}")</p>

---
