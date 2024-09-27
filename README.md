# Setup Instructions
## **1. Clone the Repository**
```
git clone <repository_url>
```

## **2. Install Dependencies**
Ensure that Python is installed on your system. Then, use the following command to install required packages:
```
pip install -r requirements.txt
```

## **3. Place PDF Files**
Add any PDF files you want to search within the `file/` directory.

## **4. Run the Program**
You can run the main script by entering the following command:
```
python main.py
```
You will be prompted to input a keyword. The program will search for this keyword in the PDF files located in the `file/` folder. If found, the results will be saved to an Excel file in the `output/` folder.

Example:
- Input a keyword like `Input a keyword like: BRANCH OUTLET MECH X FNPT DI GALV EPDM`
- The program will search all PDFs in the `file/` folder for this keyword.
- If matches are found, the results will be saved to `output/BRANCH OUTLET MECH X FNPT DI GALV EPDM.xlsx `with a well-formatted layout.

## **5. Results**
The search results will be stored in an Excel file with alternating row colors, bold headers, and custom column widths. The file will be placed in the `output/` folder with the name of the keyword (sanitized for filesystem compatibility).