
# ### Feature Extraction:
# The extracted features are categorized into
# 
# 1. Address Bar based Features
# 2. Domain based Features
# 3. HTML & Javascript based Features

# ### Address Bar Based Features:

# In[8]:


# importing required packages for this section
from urllib.parse import urlparse, urlencode
import ipaddress
import re


# In[9]:


# Domain of the Url (Domain)
def getDomainUrl(url):
    try:
        if not url.startswith('http'):
            url = 'http://' + url
        domain = urlparse(url).netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain
    except ValueError:
        return None


# In[10]:


# check for having ip add. in url (Have_IP)
def has_IpAdd(url):
    try:
        ipaddress.ip_address(url)
        ip = 1
    except:
        ip = 0
    return ip


# In[11]:


# check the presence of @ in url (Have_At)
def haveAtSign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at


# In[12]:


# check for length of url, url greater than 75 charcteris consider as phishing (Url_Length)
def getLength(url):
    if len(url) > 75:
        length = 1
    else:
        length = 0
    return length


# In[13]:


# check for url depth (Url_Depth)
def getUrlDepth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in s:
        if len(j) != 0:
            depth = depth + 1
    return depth


# In[14]:


# check for url redirection "//" in the url (Redirection)
def redirection(url):
    pos = url.rfind('//')
    if pos > 6 :
        if pos > 7:
            return 1
        else:
            return 0
    else:
        return 0


# In[15]:


# check for existence of 'HTTPS' in domain (https_domain)
def httpsDomain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0


# In[16]:


#listing shortening services
shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"


# In[17]:


# check for shorting service (Tiny_Url)
def tinyUrl(url):
    match=re.search(shortening_services,url)
    if match:
        return 1
    else:
        return 0


# In[18]:


# check for prefix and suffix with this '-' symbol (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1
    else:
        return 0


# ### Domain Based feature extraction

# In[19]:

# In[20]:


# importing required packages for this section
import socket
import whois
import datetime


# In[21]:


# check for dns record
def has_dns_record(domain):
    try:
        socket.gethostbyname(domain)
        return 1
    except:
        return 0


# In[22]:


# check for domain age
def domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        today = datetime.datetime.now()
        num_days = (today - creation_date).days
        if num_days > 365 :
            return 0
        else:
            return 1
    except:
        return 1


# In[23]:


# check for domain expairation date
def domain_exp_date(domain):
    try:
        w = whois.whois(domain)
        exp_date = w.expiration_date
        today = datetime.datetime.now()
        days_left = (exp_date - today)
        if days_left > 183:
            return 0
        else:
            return 1
    except:
        return 1


# ### HTML and javascript based feature extraction

# In[24]:


# importing required package for this 
import requests
from bs4 import BeautifulSoup


# In[25]:


# check for hrml iframe
def iframe(response):
    if response == "":
        return 1
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        iframe_tag = soup.find_all("iframe")
        if not iframe_tag:
            return 0
        for iframe in iframe_tag:
            if not iframe.text.strip():
                return 1
        
    return 0


# In[26]:


# check number of time website redirects to another (website forwarding)
def forwarding(response) :
    if response == "":
        return 1
    if len(response.history) <= 2:
        return 0
    else:
        return 1


# In[27]:


# check for alter script
def check_alert_script(response):
    if response == "":
        return 1
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.find_all("script")
    
    for script in scripts:
        if script.string and 'alert(' in script.string:
            return 1
    return 0


# ### Computing Url Features

# In[28]:


# function to extract all features
def extract_features(url):
    features = []
    # Addressed based features
    #features.append(getDomainUrl(url))
    features.append(has_IpAdd(url))
    features.append(haveAtSign(url))
    features.append(getLength(url))
    features.append(getUrlDepth(url))
    features.append(redirection(url))
    features.append(httpsDomain(url))
    features.append(tinyUrl(url))
    features.append(prefixSuffix(url))
    
    # domain based features
    whois_registered = 0
    try:
        domain = whois.whois(urlparse(url).netloc)
    except:
        whois_registered = 1
        
    features.append(1 if whois_registered == 1 else has_dns_record(domain))
    features.append(1 if whois_registered == 1 else domain_age(domain))
    features.append(1 if whois_registered == 1 else domain_exp_date(domain))
    
    # Html and javascript based features
    try:
        response = requests.get(url)
    except:
        response = ""
    
    features.append(iframe(response))
    features.append(forwarding(response))
    features.append(check_alert_script(response))
    
    return features
