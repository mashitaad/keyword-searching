from services.pdf_parser import find_keyword
from services.file_handler import export_results, format_filename
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    keyword_input = input("Enter the keyword: ").strip()
    
    if not keyword_input:
        logging.error("No keyword entered. Exiting.")
    else:
        search_results = find_keyword(keyword_input)
        
        if search_results:
            export_results(search_results, keyword_input)
            print(f"Search completed. Results saved to '{format_filename(keyword_input)}.xlsx'.")
        else:
            logging.info("No results found.")
