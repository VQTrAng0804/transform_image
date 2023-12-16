import cv2
import numpy
from rembg import remove


def reflection(image):

    # Return relection image
    return  cv2.flip(image,1) # 1 denotes horizontal flip


def grayscale(image):

    # Return grayscale image
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  

def sepia(image):

    # Convert the input image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize the grayscale image to a range of [0, 1]
    normalized_gray = numpy.array(gray, numpy.float32) / 255

    # Create a sepia filter matrix with predefined intensity values
    sepia = numpy.ones(image.shape)
    sepia[:, :, 0] *= 153  # B
    sepia[:, :, 1] *= 204  # G
    sepia[:, :, 2] *= 255  # R

    # Multiply the sepia filter with the normalized grayscale image
    sepia = numpy.multiply(sepia, normalized_gray[:, :, numpy.newaxis])

    # Convert the resulting sepia image back to uint8 format
    sepia = numpy.array(sepia, numpy.uint8)

    # Return sepia image
    return sepia


def deep_pencil_sketch(image):
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    invert_grayscale = cv2.bitwise_not(grayscale_image)

    # Apply Gaussian blur to the inverted image 
    blur = cv2.GaussianBlur(invert_grayscale, (251,251), 0)

    # Invert the blurred image 
    invert_blur = cv2.bitwise_not(blur)

    # Return the blending the original color image with the inverted and blurred image 
    return cv2.divide(grayscale_image, invert_blur, scale=256.0)


def paler_pencil_sketch(image):

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    invert_grayscale = cv2.bitwise_not(grayscale_image)

    # Apply Gaussian blur to the inverted image 
    blur = cv2.GaussianBlur(invert_grayscale, (51,51), 0)

    # Invert the blurred image 
    invert_blur = cv2.bitwise_not(blur)

    # Return the blending the original color image with the inverted and blurred image 
    return cv2.divide(grayscale_image, invert_blur, scale=256.0)


def paler_blur(image):

    # Return blur image
    return cv2.GaussianBlur(image, (51,51), 0)


def deep_blur(image):

    # Return blur image
    return cv2.GaussianBlur(image, (251,251), 0)


def delete_back(image):
    
    # Return remove background
    return remove(image)


def negative(image):

    # Return negative image
    return 255 - image


def vintage(image):

    # Define the vintage filter matrix
    vintage_filter = numpy.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    # Apply the vintage filter to the image
    sepia_image = cv2.transform(image, vintage_filter)

    # Clip values to be in the valid range [0, 255]
    vintage_image = numpy.clip(sepia_image, 0, 255).astype(numpy.uint8)

    # Return vintage image
    return vintage_image


def fresh(image):

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Increase the saturation for a more vibrant look
    hsv_image[:, :, 1] = numpy.clip(hsv_image[:, :, 1] * 1.5, 0, 255)

    # Increase the value (brightness) to brighten the colors
    hsv_image[:, :, 2] = numpy.clip(hsv_image[:, :, 2] * 1.2, 0, 255)

    # Convert the image back to BGR color space
    fresh_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    # Return fresh image
    return fresh_image


def edges(image):
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Canny edge detection
    edges_image = cv2.Canny(blurred_image, 50, 150)

    # Convert edges image to BGR color space
    edges_image_bgr = cv2.cvtColor(edges_image, cv2.COLOR_GRAY2BGR)

    # Combine the edges with the original image
    edges_effect_image = cv2.addWeighted(image, 0.7, edges_image_bgr, 0.3, 0)
    return edges_effect_image


def bland(image):

    # Return bland image
    return  cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

