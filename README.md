# Google Books to PDF

Python3 script to take screenshots of each page (user defined dimensions) of a Google Book (or any other application where right_arrow flips to next page) and then converts the images to a PDF.  



#### Prerequisites

```shell
pip install pyautogui
pip install fpdf
```

#### 1. Run script

```
python3 Google_Books_To_PDF.py
or
python Google_Books_To_PDF.py
```

#### 2. Choose Window

Lists all open windows.  Choose the browser window that has the Google Book by entering the number, press enter.

#### 3. Choose Screenshot Dimensions

With the script window focused, highlight over the top left corner of the desired screenshot and press enter.  Then, do the same thing for the bottom right corner.

#### 4. Enter Number of Pages

Enter number of pages and press enter

#### 5. Change Focus to Browser Window

You will be given 3 seconds to change the focus to the browser window.  The browser window needs to keep the focus for the rest of the process, sorry.

#### 6. Wait

Wait for the process to complete.  Creating of images and cleaning up has a percentage display.  Creating of the PDF does not.  Unfortunately.  Output should be a pdf with a filename that is akin to the window title you originally chose, in a folder of the same name, in the location where the script is run from.  

