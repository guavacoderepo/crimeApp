import multiprocessing
from src.sahara import sahara_scrape_all_documents, sahara_scrape_one_page
from src.dailytrust import dailytrust_scrape_all_docx, dailytrust_scrape_one_page
from src.guardian import guardian_scrape_all_document, guardian_scrape_one_page
from src.nigeriawatch import nigeriawatch_scrape_all_document, nigeriawatch_scrape_new_document


def scrape_all():
    # creating processes
    p1 = multiprocessing.Process(target=sahara_scrape_all_documents)
    p2 = multiprocessing.Process(target=dailytrust_scrape_all_docx)
    p3 = multiprocessing.Process(target=guardian_scrape_all_document)
    p4 = multiprocessing.Process(target=nigeriawatch_scrape_all_document)

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # starting process 3
    p3.start()

    # starting process 4
    p4.start()

    # wait until process 1 is finished
    p1.join()
    p2.join()
    p3.join()
    p4.join()


def scrape_one():
    # creating processes
    p1 = multiprocessing.Process(target=sahara_scrape_one_page)
    p2 = multiprocessing.Process(target=dailytrust_scrape_one_page)
    p3 = multiprocessing.Process(target=guardian_scrape_one_page)
    p4 = multiprocessing.Process(target=nigeriawatch_scrape_new_document)

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
    # starting process 3
    p3.start()
    # starting process 4
    p4.start()

    # wait until process 1 is finished
    p1.join()
    p2.join()
    p3.join()
    p4.join()
