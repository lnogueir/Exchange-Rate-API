# Exchange-Rate-API
Created a simple to use API that retrieves currency exchange rates using Python and BeautifulSoup.
## How to use:
First make sure you have checked the dependencies on the requirements.txt file. If you are missing some requirements, just type on your terminal:
1. pip install beautifulsoup4
2. pip install lxml
3. pip install requests
4. pip install flask

These are the libraries used.

Once you have those, you will be able to run exchange\_rate\_api.py file.
This runs a flask server with a single end point -- /rate.
On this end point you are allowed to make post requests.
It is important to make sure you are sending what currencies you are converting,USD to CAD for example.

The example program should be enough to make you confortable with the api. Feel free to use this example for yourself.

Before trying to run the example code read below.

## Things to notice:

⋅⋅* Both example_program1.py and example_program2 will only work if ran while exchange_rate_api.py file is being executed.
⋅⋅* In order to run the example\_program2, you must first set up the EmailAccount.py file. You just need to put your email account as user, your password and the receiver.  
⋅⋅* If you find problems connecting to your email check this [link.](https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python) 
⋅⋅* When setting up your desired currencies you must follow the currency codes according to the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
⋅⋅* It doesn't work some non-relevant currencies. 



 

