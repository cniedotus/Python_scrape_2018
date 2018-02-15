# crawl_UTD_reviews
# Author: Cheng Nie
# Email: cheng@chengnie.com
# Date: Feb 15, 2018

from urllib.request import urlopen

# the number of pages needs to be updated to relfect the current total pages
num_pages = 4
reviews_per_page = 20
# the file we will save the rating and date
out_file = open('UTD_reviews.csv', 'w')
# the url that we need to locate the page for UTD reviews
url = 'http://www.yelp.com/biz/university-of-texas-at-dallas-richardson?start={start_number}'

# the string patterns to locate relevant information
review_start_pattern = '<div class="review-wrapper">'

rating_start_pattern = '<div class="i-stars i-stars--regular-'
rating_end_pattern = 'rating-large" title="'

date_start_pattern = '<span class="rating-qualifier">'
date_end_pattern = '<'

reviews_count = 0

for page in range(num_pages):

    print('processing page', page)

    # open the url and save the source code string to page_content
    html = urlopen(url.format(start_number=page * reviews_per_page))
    page_content = html.read().decode('utf-8')

    # locate the beginning of an individual review
    review_start = page_content.find(review_start_pattern)

    while review_start != -1:
        # it means there at least one more review to be crawled
        reviews_count += 1

        # get the rating
        cut_front = page_content.find(
            rating_start_pattern, review_start) + len(rating_start_pattern)
        cut_end = page_content.find(rating_end_pattern, cut_front)
        rating = page_content[cut_front:cut_end]
        rating = rating.strip()  # remove white spaces around

        # get the date
        cut_front = page_content.find(
            date_start_pattern, cut_end) + len(date_start_pattern)
        cut_end = page_content.find(date_end_pattern, cut_front)
        date = page_content[cut_front:cut_end]
        date = date.strip()  # remove white spaces around

        # save the data into out_file
        out_file.write(','.join([rating, date]) + '\n')
        review_start = page_content.find(review_start_pattern, cut_end)

    print('crawled', reviews_count, 'reviews so far')

print("Program finished!")

out_file.close()
