# Doc-Scanner
I am early on in my computer vision journey, but this is the first project I attempted to demonstrate the knowledge I have learned from online courses. I decided, what better way to learn OpenCV than to build something that already exists? Hence, I decided to rebuild a barebones version of the popular document scanning feature that Apple developed.

### How it works

The script utilizes OpenCV, a popular library used in robotics for image processing. First the script reads in an image from a local directory and converts the image to grayscale to reduce the size and detail of the image. 

<img src="./images/original.png"
     style="marginLefet: 10%;width: 25%; height: 25%" />

Next, I used canny edge detection to find important images that define the feature of the image and display them against a black background

<img src="./images/cannyedges.png"
     style="marginLefet: 10%;width: 25%; height: 25%" />
