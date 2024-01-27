@echo off
setlocal enabledelayedexpansion

REM Specify the path to your image files
set "source_path=C:\Users\rcmba\end-to-end-waste-detection\CCTV"

REM Loop through all PNG and JPEG files in the source directory
for %%F in ("%source_path%\*.png" "%source_path%\*.jpeg" "%source_path%\*.jpg") do (
    REM Build the destination path with the new JPG extension
    set "destination_path=%%~dpnF.jpg"
    
    REM Convert PNG or JPEG to JPG using ImageMagick
    magick "%%F" "!destination_path!"

    REM Optionally, keep the original file or delete it
    REM del "%%F"
)

REM Rename the resulting JPG files
for %%i in ("%source_path%\*.jpg") do ren "%%i" "new_%%~nxi"

endlocal
