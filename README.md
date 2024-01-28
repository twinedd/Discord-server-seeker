
# this utility uses Scraper api -- https://www.scraperapi.com/. Launch with version.txt in folder
### When you register, you will be given 5,000 free requests, and there is no rate limit for you.


### How it works?
The program sends a request to the discord api with a random invite link, and the discord api returns either a 404 status code (not found) or a status code 200 (OK)
But there is a problem that cloudflare blocks invalid requests if there are many of them, and your IP may be banned for the whole day. But Scraper api uses a proxy server and you do not use your IP to make the request, and the program can thus work even in five threads



### Tutorial
You need to insert a link to your webhook into the hook variable so that the script can send a working invite. You need to insert your key into the scraper API, you will find it on the site when you register, it’s free, if you need more requests, you can buy more requests
Enjoy

![Tutorial](https://cdn.discordapp.com/attachments/1194739385787224175/1201105898936991774/Screenshot_2024-01-28_125510.png?ex=65c89c09&is=65b62709&hm=be88d259bb766886544dc567c240cda18acf059cf34607102ca6b0f069de81a5&)

Here you can change the number of characters in the invite; if you want to find unknown, private servers, then simply put the number 8.
Like for i in range(8):
![+](https://cdn.discordapp.com/attachments/1194739385787224175/1201123761500471296/Screenshot_2024-01-28_141532.png?ex=65c8acac&is=65b637ac&hm=46b49568089d638760a3532793d844f4578e6f727e3389906fd816c0d286a5b2&)


![+](https://cdn.discordapp.com/attachments/1194739385787224175/1201105899255771156/Screenshot_2024-01-28_130431.png?ex=65c89c09&is=65b62709&hm=9feab4d72fc5c0f7b4b8cb98509b76bd170db1127e6bd8a3ab34567f290c090f&)
