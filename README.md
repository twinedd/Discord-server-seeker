# This utility uses Scraper api -- https://www.scraperapi.com/.
### When you register, you will be given 5,000 free requests, and there is no rate limit for you.


### How it works?
The program sends a request to the discord api with a random invite link, and the discord api returns either a 404 status code (not found) or a status code 200 (OK)
But there is a problem that cloudflare blocks invalid requests if there are many of them, and your IP may be banned for the whole day. But Scraper api uses a proxy server and you do not use your IP to make the request, and the program can thus work even in five threads



### Tutorial
You need to insert a link to your webhook into the hook variable so that the script can send a working invite. You need to insert your key into the scraper API, you will find it on the site when you register, it’s free, if you need more requests, you can buy more requests
Enjoy


