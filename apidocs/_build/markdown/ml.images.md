# ml.images package

## Submodules

## ml.images.conversion module

The conversion module allows users to transform images freely


### ml.images.conversion.crop(image: numpy.array, x: int, y: int, width: int, height: int)
Crops an image based on the specified size
:param image: The array representation of the image to crop
:type image: np.array
:param x: The x coordinate of the rectangle to keep (horizontal position from the left)
:type x: int
:param y: The y coordinate of the rectangle to keep (vertical position from the top)
:type y: int
:param width: The width of the cropped image
:type width: int
:param height: The height of the cropped image
:type height: int


* **Returns**

    A numpy array that represents the cropped part of the image



* **Return type**

    np.array



### ml.images.conversion.get_fragments(image: numpy.array, stride: tuple = (1, 1), fragment_size: tuple = (1, 1), rectangle=None)
Scans an image and return the resulted parts as a list of image sections
:param image: The array representation of the image to scan
:type image: np.array
:param stride: The steps to move over the image
:type stride: tuple
:param fragment_size: The size of the fragments to take from the image
:type fragment_size: tuple
:param rectangle: The rectangle in the image to scan (if only a part of the image should be scanned.  Form: (x, y, width, height)
:type rectangle: np.array


* **Returns**

    A numpy array that contains all fragments as images



* **Return type**

    np.array



### ml.images.conversion.imread(filename, )
.   @brief Loads an image from a file.
.
.   @anchor imread
.
.   The function imread loads an image from the specified file and returns it. If the image cannot be
.   read (because of missing file, improper permissions, unsupported or invalid format), the function
.   returns an empty matrix ( Mat::data==NULL ).
.
.   Currently, the following file formats are supported:
.
.   -   Windows bitmaps - \*.bmp, \*.dib (always supported)
.   -   JPEG files - \*.jpeg, \*.jpg, \*.jpe (see the *Note* section)
.   -   JPEG 2000 files - \*.jp2 (see the *Note* section)
.   -   Portable Network Graphics - \*.png (see the *Note* section)
.   -   WebP - \*.webp (see the *Note* section)
.   -   Portable image format - \*.pbm, \*.pgm, \*.ppm \*.pxm, \*.pnm (always supported)
.   -   PFM files - \*.pfm (see the *Note* section)
.   -   Sun rasters - \*.sr, \*.ras (always supported)
.   -   TIFF files - \*.tiff, \*.tif (see the *Note* section)
.   -   OpenEXR Image files - \*.exr (see the *Note* section)
.   -   Radiance HDR - \*.hdr, \*.pic (always supported)
.   -   Raster and Vector geospatial data supported by GDAL (see the *Note* section)
.
.   @note
.   -   The function determines the type of an image by the content, not by the file extension.
.   -   In the case of color images, the decoded images will have the channels stored in **B G R** order.
.   -   When using IMREAD_GRAYSCALE, the codec’s internal grayscale conversion will be used, if available.
.       Results may differ to the output of cvtColor()
.   -   On Microsoft Windows\* OS and MacOSX\*, the codecs shipped with an OpenCV image (libjpeg,
.       libpng, libtiff, and libjasper) are used by default. So, OpenCV can always read JPEGs, PNGs,
.       and TIFFs. On MacOSX, there is also an option to use native MacOSX image readers. But beware
.       that currently these native image loaders give images with different pixel values because of
.       the color management embedded into MacOSX.
.   -   On Linux\*, BSD flavors and other Unix-like open-source operating systems, OpenCV looks for
.       codecs supplied with an OS image. Install the relevant packages (do not forget the development
.       files, for example, “libjpeg-dev”, in Debian\* and Ubuntu\*) to get the codec support or turn
.       on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.
.   -   In the case you set *WITH_GDAL* flag to true in CMake and @ref IMREAD_LOAD_GDAL to load the image,
.       then the [GDAL]([http://www.gdal.org](http://www.gdal.org)) driver will be used in order to decode the image, supporting
.       the following formats: [Raster]([http://www.gdal.org/formats_list.html](http://www.gdal.org/formats_list.html)),
.       [Vector]([http://www.gdal.org/ogr_formats.html](http://www.gdal.org/ogr_formats.html)).
.   -   If EXIF information is embedded in the image file, the EXIF orientation will be taken into account
.       and thus the image will be rotated accordingly except if the flags @ref IMREAD_IGNORE_ORIENTATION
.       or @ref IMREAD_UNCHANGED are passed.
.   -   Use the IMREAD_UNCHANGED flag to keep the floating point values from PFM image.
.   -   By default number of pixels must be less than 2^30. Limit can be set using system
.       variable OPENCV_IO_MAX_IMAGE_PIXELS
.
.   @param filename Name of file to be loaded.
.   @param flags Flag that can take values of cv::ImreadModes


### ml.images.conversion.prepare(image: numpy.array, image_size=None, convert_to_grey: bool = False, keep_3d_shape=False)
Takes an image and applies preformatting
:param image: The array representation of the image to process
:type image: np.array
:param image_size: The image size can be passed as tuple (W, H) or as int (W=H)
:type image_size: tuple
:param convert_to_grey: This would reduce the size (and shape) of the image in making it a greyscale
:type convert_to_grey: bool
:param keep_3d_shape: Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
:type keep_3d_shape: bool


* **Returns**

    A numpy array that represents the preprocessed image



* **Return type**

    np.array



### ml.images.conversion.to_blackwhite(image_list: numpy.array, threshold=128, keep_3d_shape=False)
Transforms an image to a black & white image
:param image_list: A numpy array that contains all selected images represented as np.array
:type image_list: np.array
:param threshold: The threshold (between 0 and 255) that decides a pixel will be 0 or 255 (W/B)
:type threshold: int


* **Returns**

    A numpy array that contains all black & white images represented as np.array



* **Return type**

    np.array


## ml.images.explorer module

The image explorer module provides standard helper functions to explore and visualize images


### ml.images.explorer.imread(filename, )
.   @brief Loads an image from a file.
.
.   @anchor imread
.
.   The function imread loads an image from the specified file and returns it. If the image cannot be
.   read (because of missing file, improper permissions, unsupported or invalid format), the function
.   returns an empty matrix ( Mat::data==NULL ).
.
.   Currently, the following file formats are supported:
.
.   -   Windows bitmaps - \*.bmp, \*.dib (always supported)
.   -   JPEG files - \*.jpeg, \*.jpg, \*.jpe (see the *Note* section)
.   -   JPEG 2000 files - \*.jp2 (see the *Note* section)
.   -   Portable Network Graphics - \*.png (see the *Note* section)
.   -   WebP - \*.webp (see the *Note* section)
.   -   Portable image format - \*.pbm, \*.pgm, \*.ppm \*.pxm, \*.pnm (always supported)
.   -   PFM files - \*.pfm (see the *Note* section)
.   -   Sun rasters - \*.sr, \*.ras (always supported)
.   -   TIFF files - \*.tiff, \*.tif (see the *Note* section)
.   -   OpenEXR Image files - \*.exr (see the *Note* section)
.   -   Radiance HDR - \*.hdr, \*.pic (always supported)
.   -   Raster and Vector geospatial data supported by GDAL (see the *Note* section)
.
.   @note
.   -   The function determines the type of an image by the content, not by the file extension.
.   -   In the case of color images, the decoded images will have the channels stored in **B G R** order.
.   -   When using IMREAD_GRAYSCALE, the codec’s internal grayscale conversion will be used, if available.
.       Results may differ to the output of cvtColor()
.   -   On Microsoft Windows\* OS and MacOSX\*, the codecs shipped with an OpenCV image (libjpeg,
.       libpng, libtiff, and libjasper) are used by default. So, OpenCV can always read JPEGs, PNGs,
.       and TIFFs. On MacOSX, there is also an option to use native MacOSX image readers. But beware
.       that currently these native image loaders give images with different pixel values because of
.       the color management embedded into MacOSX.
.   -   On Linux\*, BSD flavors and other Unix-like open-source operating systems, OpenCV looks for
.       codecs supplied with an OS image. Install the relevant packages (do not forget the development
.       files, for example, “libjpeg-dev”, in Debian\* and Ubuntu\*) to get the codec support or turn
.       on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.
.   -   In the case you set *WITH_GDAL* flag to true in CMake and @ref IMREAD_LOAD_GDAL to load the image,
.       then the [GDAL]([http://www.gdal.org](http://www.gdal.org)) driver will be used in order to decode the image, supporting
.       the following formats: [Raster]([http://www.gdal.org/formats_list.html](http://www.gdal.org/formats_list.html)),
.       [Vector]([http://www.gdal.org/ogr_formats.html](http://www.gdal.org/ogr_formats.html)).
.   -   If EXIF information is embedded in the image file, the EXIF orientation will be taken into account
.       and thus the image will be rotated accordingly except if the flags @ref IMREAD_IGNORE_ORIENTATION
.       or @ref IMREAD_UNCHANGED are passed.
.   -   Use the IMREAD_UNCHANGED flag to keep the floating point values from PFM image.
.   -   By default number of pixels must be less than 2^30. Limit can be set using system
.       variable OPENCV_IO_MAX_IMAGE_PIXELS
.
.   @param filename Name of file to be loaded.
.   @param flags Flag that can take values of cv::ImreadModes


### ml.images.explorer.show_image(image: numpy.array, hide_grid: bool = True, grid_size=None, silent_mode: bool = False)
Visualizes an image
:param image: the image to visualize, represented as numpy array
:type image: np.array
:param hide_grid: indicating if the grid (with the pixel positions) should be hidden
:type hide_grid: bool
:param grid_size: the size of the grid to plot the images in.  By default auto size is being applied
:type grid_size: (int, int)
:param silent_mode: indicates if the image has to be plotted, or just returned
:type silent_mode: bool


### ml.images.explorer.visualize(image_sets: dict, image_count: int = 10, randomize: bool = True, grid_size=None, hide_grid: bool = True, silent_mode: bool = False)
Visualizes the images in the image_sets in a grid
:param image_sets: a dictionary of type (str, list) that indicates the name of an images set and the actual images
:type image_sets: dict
:param image_count: the amount of images to visualize from an image set
:type image_count: int
:param randomize: if True, images will be selected randomly from the imageset, if False, the first n images will be taken
:type randomize: bool
:param grid_size: the size of the grid to plot the images in.  By default auto size is being applied
:type grid_size: (int, int)
:param hide_grid: indicates if the grid with pixellocations should be hidden
:type hide_grid: bool
:param silent_mode: indicates if the image has to be plotted, or just returned
:type silent_mode: bool

### Example

image_sets = {‘predicted’: y_pred, ‘actuals’: y_test}

visualize(image_sets, 6, False)


### ml.images.explorer.visualize_classes(image_set: numpy.array, classes: numpy.array, image_count: int = 10, randomize: bool = True, grid_size=None, silent_mode: bool = False)
Visualizes the images from the image_set in a grid and print the corresponding class on the charts


* **Parameters**

    
    * **image_set** (*np.array*) – an array of images to pick from


    * **classes** (*np.array*) – the corresponding labels of the classes for the images


    * **image_count** (*int*) – the amount of images to visualize from an image set


    * **randomize** (*bool*) – if True, images will be selected randomly from the imageset, if False, the first n images will be taken


    * **grid_size** (*(**int**, **int**)*) – the size of the grid to plot the images in.  By default auto size is being applied


    * **silent_mode** (*bool*) – indicates if the image has to be plotted, or just returned


### Example

image_sets = {‘predicted’: y_pred, ‘actuals’: y_test}

visualize(image_sets, 6, False)

## ml.images.io module

The io module provides standard helper functions to load images from disk


### ml.images.io.imdecode(buf, flags)
.   @brief Reads an image from a buffer in memory.
.
.   The function imdecode reads an image from the specified buffer in the memory. If the buffer is too short or
.   contains invalid data, the function returns an empty matrix ( Mat::data==NULL ).
.
.   See cv::imread for the list of supported formats and flags description.
.
.   @note In the case of color images, the decoded images will have the channels stored in **B G R** order.
.   @param buf Input array or vector of bytes.
.   @param flags The same flags as in cv::imread, see cv::ImreadModes.


### ml.images.io.imread(filename, )
.   @brief Loads an image from a file.
.
.   @anchor imread
.
.   The function imread loads an image from the specified file and returns it. If the image cannot be
.   read (because of missing file, improper permissions, unsupported or invalid format), the function
.   returns an empty matrix ( Mat::data==NULL ).
.
.   Currently, the following file formats are supported:
.
.   -   Windows bitmaps - \*.bmp, \*.dib (always supported)
.   -   JPEG files - \*.jpeg, \*.jpg, \*.jpe (see the *Note* section)
.   -   JPEG 2000 files - \*.jp2 (see the *Note* section)
.   -   Portable Network Graphics - \*.png (see the *Note* section)
.   -   WebP - \*.webp (see the *Note* section)
.   -   Portable image format - \*.pbm, \*.pgm, \*.ppm \*.pxm, \*.pnm (always supported)
.   -   PFM files - \*.pfm (see the *Note* section)
.   -   Sun rasters - \*.sr, \*.ras (always supported)
.   -   TIFF files - \*.tiff, \*.tif (see the *Note* section)
.   -   OpenEXR Image files - \*.exr (see the *Note* section)
.   -   Radiance HDR - \*.hdr, \*.pic (always supported)
.   -   Raster and Vector geospatial data supported by GDAL (see the *Note* section)
.
.   @note
.   -   The function determines the type of an image by the content, not by the file extension.
.   -   In the case of color images, the decoded images will have the channels stored in **B G R** order.
.   -   When using IMREAD_GRAYSCALE, the codec’s internal grayscale conversion will be used, if available.
.       Results may differ to the output of cvtColor()
.   -   On Microsoft Windows\* OS and MacOSX\*, the codecs shipped with an OpenCV image (libjpeg,
.       libpng, libtiff, and libjasper) are used by default. So, OpenCV can always read JPEGs, PNGs,
.       and TIFFs. On MacOSX, there is also an option to use native MacOSX image readers. But beware
.       that currently these native image loaders give images with different pixel values because of
.       the color management embedded into MacOSX.
.   -   On Linux\*, BSD flavors and other Unix-like open-source operating systems, OpenCV looks for
.       codecs supplied with an OS image. Install the relevant packages (do not forget the development
.       files, for example, “libjpeg-dev”, in Debian\* and Ubuntu\*) to get the codec support or turn
.       on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.
.   -   In the case you set *WITH_GDAL* flag to true in CMake and @ref IMREAD_LOAD_GDAL to load the image,
.       then the [GDAL]([http://www.gdal.org](http://www.gdal.org)) driver will be used in order to decode the image, supporting
.       the following formats: [Raster]([http://www.gdal.org/formats_list.html](http://www.gdal.org/formats_list.html)),
.       [Vector]([http://www.gdal.org/ogr_formats.html](http://www.gdal.org/ogr_formats.html)).
.   -   If EXIF information is embedded in the image file, the EXIF orientation will be taken into account
.       and thus the image will be rotated accordingly except if the flags @ref IMREAD_IGNORE_ORIENTATION
.       or @ref IMREAD_UNCHANGED are passed.
.   -   Use the IMREAD_UNCHANGED flag to keep the floating point values from PFM image.
.   -   By default number of pixels must be less than 2^30. Limit can be set using system
.       variable OPENCV_IO_MAX_IMAGE_PIXELS
.
.   @param filename Name of file to be loaded.
.   @param flags Flag that can take values of cv::ImreadModes


### ml.images.io.load_image_from_disk(path: str, image_size=None, convert_to_grey: bool = False, keep_3d_shape=False)
Loads an image from file, applying preformatting
:param path: The filename of the image to load
:type path: str
:param image_size: The image size can be passed as tuple (W, H) or as int (W=H)
:type image_size: tuple
:param convert_to_grey: This would reduce the size (and shape) of the image in making it a greyscale
:type convert_to_grey: bool
:param keep_3d_shape: Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
:type keep_3d_shape: bool


* **Returns**

    A numpy array that represents the image



* **Return type**

    np.array



### ml.images.io.load_image_from_url(image_url: str, http_headers: Optional[dict] = None, image_size=None, convert_to_grey: bool = False, keep_3d_shape=False, cache_location: Optional[str] = None, file_name: Optional[str] = None, force_download: bool = False)
Loads an image from a given url, applying preformatting and supporting file caching
:param image_url: The url to download the image.
:type image_url: str
:param http_headers: The http headers to pass with the request as a dictionary
:type http_headers: dict
:param image_size: The image size can be passed as tuple (W, H) or as int (W=H)
:type image_size: tuple
:param convert_to_grey: This would reduce the size (and shape) of the image in making it a greyscale
:type convert_to_grey: bool
:param keep_3d_shape: Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
:type keep_3d_shape: bool
:param cache_location: When provided, the image will be cached to this folder location on disk
:type cache_location: str
:param file_name: The file name of the image to be cached
:type file_name: str
:param force_download: When true, the image will always be redownloaded and not retrieved from cache
:type force_download: bool


* **Returns**

    A numpy array that represents the image



* **Return type**

    np.array



### ml.images.io.load_images(path: str, image_size=None, max_images: int = - 1, valid_extensions: numpy.array = ['.jpg', '.jpeg', '.gif', '.png'], convert_to_grey: bool = False, keep_3d_shape=False)
Loads the images from a specific folder
:param path: The path or folder name to load images from.  This can be a relative or fully qualified path
:type path: str
:param image_size: The image size can be passed as tuple (W, H) or as int (W=H)
:type image_size: tuple
:param max_images: The maximum amount of images to load from the folder.  If 0 or smaller, all images will be returned
:type max_images: int
:param valid_extensions: The file extensions that should be filtered.  Defaults to jpg, jpeg, gif and png
:type valid_extensions: np.array
:param convert_to_grey: This would reduce the size (and shape) of the image in making it a greyscale
:type convert_to_grey: bool
:param keep_3d_shape: Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
:type keep_3d_shape: bool


* **Returns**

    A numpy array that contains all selected images represented as np.array



* **Return type**

    np.array



### ml.images.io.load_images_from_dataframe(df: pandas.core.frame.DataFrame, image_column_name: str, target_column_name: str, image_size=None, max_images: int = -1, target_as_image: bool = False, convert_to_grey: bool = False, keep_3d_shape=False) -> (<built-in function array>, <built-in function array>)
Loads a set images from disk, based on the file name in a Data Frame.
And returns a related array (target) that can contain values from another column, or also images from disk


* **Parameters**

    
    * **df** (*pd.DataFrame*) – the DataFrame, containing the references to the image


    * **image_column_name** (*str*) – The name of the column that contains the image reference


    * **target_column_name** (*str*) – The name of the column that contains the related target data


    * **image_size** (*tuple*) – The image size can be passed as tuple (W, H) or as int (W=H)


    * **max_images** (*int*) – The maximum amount of images to load from the folder.  If 0 or smaller, all images will be returned


    * **target_as_image** (*bool*) – Defines if the target column contains file names that should be loaded as image.  If not, the column data will be used in the target array


    * **convert_to_grey** (*bool*) – This would reduce the size (and shape) of the image in making it a greyscale


    * **keep_3d_shape** (*bool*) – Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case



* **Returns**

    np.array: A numpy array that contains all selected images represented as np.array
    np.array: A numpy array that represents all targets that were asked



* **Return type**

    a tuple with the following objects


## Module contents
