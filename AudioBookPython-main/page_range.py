# In this function we get first and last page, which we want the software to read
def get_text(value):

    string = value
    string = string.strip()
    if "-" in string:
        first_page_number = int(string.split("-")[0])
        last_page_number = int(string.split("-")[1])
    else:
        first_page_number = int(string)
        last_page_number = 0

    return first_page_number,last_page_number
