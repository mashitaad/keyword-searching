import os
import PyPDF2
import logging

def find_keyword(keyword, folder_path='file/'):
    """
    Searches for a specified keyword in all PDF files within a given folder.
    
    Args:
        keyword (str): The keyword to search for.
        folder_path (str): The path to the folder containing PDF files.
        
    Returns:
        list: A list of tuples containing the filenames and the keyword.
    """
    results = []
    
    if not os.path.exists(folder_path):
        logging.error(f"Folder path '{folder_path}' does not exist.")
        return results

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            
            try:
                with open(file_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    found = False
                    
                    for page in reader.pages:
                        text = page.extract_text()
                        if text and keyword.upper() in text.upper():
                            found = True
                            break 
                    
                    if found:
                        results.append((filename, keyword))
                        logging.info(f"Keyword '{keyword}' found in '{filename}'")
            except Exception as e:
                logging.error(f"Error processing file '{filename}': {e}")
    
    return results
