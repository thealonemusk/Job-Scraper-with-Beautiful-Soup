from bs4 import BeautifulSoup
# the basic scrapping for the extremely easy website
with open('file.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'html.parser')
    # tags = soup.find_all('h5')
    # for tag in tags:
    #     print(tag.text)

    course_cards = soup.find_all('div', class_='card')
    # filtering the div with class card adding _ is because class is a keyword in python
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
# the scrapping for the website with a little bit of complexity
