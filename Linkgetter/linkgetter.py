from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


links = ["https://www2.assemblee-nationale.fr/sycomore/resultats/(query)/IiBTRUxFQ1QgbV9jb2RlX2RlcHV0ZSwgaWRfYWN0ZXVyX3RyaWJ1biwgbGVnX21heF90cmlidW4sIG5vbSwgbm9tX2FmZmljaGUsIHByZW5vbSwgZGF0ZV9uYWlzLCBkYXRlX2RlY2VzIEZST00gZGVwdXRlIFdIRVJFIDE9MSAgQU5EIG1fY29kZV9kZXB1dGUgSU4gKFNFTEVDVCBtX2NvZGVfZGVwdXRlIEZST00gbWFuZGF0IFdIRVJFIG1fdHlwZV9tYW5kYXQgPSAyKSBPUkRFUiBCWSBub20sIHByZW5vbSBERVNDIg",
         "https://www2.assemblee-nationale.fr/sycomore/resultats/(offset)/500/(query)/IiBTRUxFQ1QgbV9jb2RlX2RlcHV0ZSwgaWRfYWN0ZXVyX3RyaWJ1biwgbGVnX21heF90cmlidW4sIG5vbSwgbm9tX2FmZmljaGUsIHByZW5vbSwgZGF0ZV9uYWlzLCBkYXRlX2RlY2VzIEZST00gZGVwdXRlIFdIRVJFIDE9MSAgQU5EIG1fY29kZV9kZXB1dGUgSU4gKFNFTEVDVCBtX2NvZGVfZGVwdXRlIEZST00gbWFuZGF0IFdIRVJFIG1fdHlwZV9tYW5kYXQgPSAyKSBPUkRFUiBCWSBub20sIHByZW5vbSBERVNDIg",
         "https://www2.assemblee-nationale.fr/sycomore/resultats/(offset)/1000/(query)/IiBTRUxFQ1QgbV9jb2RlX2RlcHV0ZSwgaWRfYWN0ZXVyX3RyaWJ1biwgbGVnX21heF90cmlidW4sIG5vbSwgbm9tX2FmZmljaGUsIHByZW5vbSwgZGF0ZV9uYWlzLCBkYXRlX2RlY2VzIEZST00gZGVwdXRlIFdIRVJFIDE9MSAgQU5EIG1fY29kZV9kZXB1dGUgSU4gKFNFTEVDVCBtX2NvZGVfZGVwdXRlIEZST00gbWFuZGF0IFdIRVJFIG1fdHlwZV9tYW5kYXQgPSAyKSBPUkRFUiBCWSBub20sIHByZW5vbSBERVNDIg"]

f = open("liste1789.txt", "a")

for url in links:
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table").find_all("a")
    for i in table:
        f.write(i.get("href")+"\n")