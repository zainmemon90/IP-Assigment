import requests,json
response = requests.get('https://api.github.com')
response.content.decode('utf-8')
api_key = "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"
# simple request with auth token in header
# this returns user personal informations
headers={
 'Authorization': 'token '+api_key
}
response = requests.get('https://api.github.com/user',headers=headers)
response.content.decode('utf-8')
print(response)

json_string = {
  "kind": "books#volume",
  "id": "9MS9BQAAQBAJ",
  "etag": "A4CkO1PcDjM",
  "selfLink": "https://content-books.googleapis.com/books/v1/volumes/9MS9BQAAQBAJ",
  "volumeInfo": {
    "title": "Black Hat Python",
    "subtitle": "Python Programming for Hackers and Pentesters",
    "authors": [
      "Justin Seitz"
    ],
    "publisher": "No Starch Press",
    "publishedDate": "2014-12-21",
    "description": "When it comes to creating powerful and effective hacking tools, Python is the language of choice for most security analysts. But just how does the magic happen?\u003cbr\u003e\u003cbr\u003eIn \u003ci\u003eBlack Hat Python\u003c/i\u003e, the latest from Justin Seitz (author of the best-selling \u003ci\u003eGray Hat Python\u003c/i\u003e), you’ll explore the darker side of Python’s capabilities—writing network sniffers, manipulating packets, infecting virtual machines, creating stealthy trojans, and more.\u003cbr\u003e\u003cbr\u003eYou’ll learn how to:\u003cbr\u003e–Create a trojan command-and-control using GitHub\u003cbr\u003e–Detect sandboxing and automate com\u00admon malware tasks, like keylogging and screenshotting\u003cbr\u003e–Escalate Windows privileges with creative process control\u003cbr\u003e–Use offensive memory forensics tricks to retrieve password hashes and inject shellcode into a virtual machine\u003cbr\u003e–Extend the popular Burp Suite web-hacking tool\u003cbr\u003e–Abuse Windows COM automation to perform a man-in-the-browser attack\u003cbr\u003e–Exfiltrate data from a network most sneakily\u003cbr\u003e\u003cbr\u003eInsider techniques and creative challenges throughout show you how to extend the hacks and how to write your own exploits.\u003cbr\u003e\u003cbr\u003eWhen it comes to offensive security, your ability to create powerful tools on the fly is indispensable. Learn how in \u003ci\u003eBlack Hat Python\u003c/i\u003e.\u003cbr\u003e\u003cbr\u003e\u003cb\u003eUses Python 2\u003c/b\u003e",
    "industryIdentifiers": [
      {
        "type": "ISBN_10",
        "identifier": "1593275900"
      },
      {
        "type": "ISBN_13",
        "identifier": "9781593275907"
      }
    ],
    
  }
}
json_data = json.loads(json_string)
print(json_string)