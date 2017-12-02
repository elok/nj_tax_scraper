import urllib
import re
from BeautifulSoup import BeautifulSoup


def get_page(url):
    f = urllib.urlopen(url)
    content = f.read()
    f.close()
    return content


def open_file(file):
    f = open(file, 'r')
    content = f.read()
    return content


def parse_building(file):
    file_content = open_file(file)

    soup = BeautifulSoup(file_content)
    # Get all links
    link_list = soup.findAll('a')

    # Result string
    result = ''

    header = 1

    for link in link_list:
        url = link['href']

        print
        '======================'
        print
        url

        # Get the page content
        page_text = get_page(url)
        # Get the apt content as a comma delimited text
        apt_content = parse_apt(page_text, header)
        # Save the apt content
        result = result + apt_content + '\n'
        header = 0

    return result


def parse_apt(page_text, get_header):
    soup = BeautifulSoup(page_text)
    header_list = soup.findAll('font', color="BLACK")
    content_list = soup.findAll('font', color="FIREBRICK")

    result = ''

    # Get the header
    if (get_header):
        for header in header_list:
            value = header.string.strip().replace('&nbsp', '').replace(';', '').replace(',', '')
            # Add a tab between each apt heading
            result = result + value + '\t'
        # Add a new line between the header and the apt content
        result = result + '\n'

    #  Get the content
    for cont in content_list:
        value = cont.string.strip().replace('&nbsp', '').replace(';', '').replace(',', '')
        # Add a tab between each content cell
        result = result + value + '\t'

    return result

    """"
    index_counter = 0
    for header in header_list:
        print header.string.strip().replace('&nbsp','').replace(';','')
        print content_list[index_counter].string.strip().replace('&nbsp','').replace(';','')
        print '====================='
        index_counter = index_counter + 1
    """


# blh = open_file('apt_result.html')
# result = parse_apt(blh, 0)
# print result

building_content = parse_building('CP_20130228.html')
myfile = open('CP_20130228.csv', 'w')
myfile.write(building_content)
myfile.close()
