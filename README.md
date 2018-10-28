# Amazon-Product-Details
A scrapy module to find product details from the listed amazon product.
It will find product details of 5 pages.

### Prerequisites
Install all the packages mentioned in the Requirements.txt file.

### Creating Virtual Environment
create a virtual env for your project : $ virtualenv _Anyname_

Activate Virtualenv: $ source _Anyname_/bin/activate

$ cd _Anyname_

### Cloning The repository
$ git clone https://github.com/anuraggothi/Amazon-Product-Details.git

### Running the Spider
$ cd Amazon-Product-Details/amazonscrap/amazonscrap/spiders/

$ scrapy runspider amazon.py

(if you want to save the output in a csv file use this: $ scrapy runspider amazon.py -o filename.csv)

A prompt will Appear asking You to type the product name Simply type the product name.
