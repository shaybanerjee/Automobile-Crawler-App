from flask import Flask
from flask import request
from flask import render_template
import urllib
from bs4 import BeautifulSoup
import mechanize
from mechanize import Browser, _http

app = Flask(__name__)

def wheels(carname):
    holder = []
    for i in range(0, 3):
        url = "http://vehicles.wheels.ca/vehiclesearch.aspx?searchwidget=1&searchtype=city&searchcity=toronto&searchprovince=ontario&provinceabbr=on&distance=100&redious=100&make=" + str(carname) + '&model=&mayr=&miyr=&mapr=&mipr=&category=&newused=&certified=0&c=&transmission=&fuel=&body=&pn=' + str(
        i) + '&sort=mileagedesc'
        br = mechanize.Browser()
        br.set_handle_robots(False)
        htmltext = br.open(url)
        soup = BeautifulSoup(htmltext)
        saleitem = soup.findAll('div', {'id': 'ListingRow0'})
        saleitem2 = soup.findAll('div', {'id': 'ListingRow1'})
        finalsaleitem = saleitem + saleitem2
        holder = holder + finalsaleitem
    return holder



def kijiji(carname):
    holder = []
    for i in range(0, 3):
        url = "http://www.kijiji.ca/b-toronto/" + str(carname) + "/page-" + str(i) + "/k0l1700272/"
        br = mechanize.Browser()
        br.set_handle_robots(False)
        htmltext = br.open(url)
        soup = BeautifulSoup(htmltext)
        saleitem = soup.findAll('div', {'class', 'clearfix'})
        holder = holder + saleitem
    return holder


def carpages(carname):
    holder = []
    for i in range(0, 3):
        url = "https://www.carpages.ca/used-cars/search/?make_name=" + str(carname) + "&search_radius=100&province_code=on&city=toronto&sort=mileage_desc&ll=43.670788538081783,-79.392561526773813"
        br = mechanize.Browser()
        br.set_handle_robots(False)
        htmltext = br.open(url)
        soup = BeautifulSoup(htmltext)
        saleitem = soup.findAll('div', {'class': 'media'})
        holder = holder + saleitem
    return holder




def blank():
    holder = []
    url = "http://www.kijiji.ca/b-kitchener-waterloo/beats-dr/k0l1700212"
    br = mechanize.Browser()
    br.set_handle_robots(False)
    htmltext = br.open(url)
    soup = BeautifulSoup(htmltext)
    saleitem = soup.findAll('ul', {'class': 'more-searches'})
    holder = saleitem
    return holder

########################################################################################################################
# Location and Sorting Code + Autotrader and Craigslist Support Coming Soon

#def sort_det2(sort):
#    if sort == "newest":
#        return ""
#    elif sort == "oldest":
#        return "?sort=dateAsc"
#    elif sort == "lowest":
#        return "?sort=priceAsc"
#    else:
#        "?sort=priceDesc"



#def detloccode2(word):
#    locations = open("locations.json").read()
#    locations_data = json.loads(locations)
#    return locations_data["locations"][word.lower()]


#def search_keyw2(searchword):
#    last_result = searchword.split()
#    new_text = ""

#    for text in last_result:
#        text2 = text + "+"

#        new_text += (text2)

#    return new_text[:-1]



#def fn2(i):
#    url = "http://wwwb.autotrader.ca/cars/"
#    try:
#        conn = mysql.connector.connect(user="dbo662048622", password="1234567", host="db662048622.db.1and1.com", database="db662048622")
#        print "works"
#    except  mysql.connector.Error as e:
#        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#            print "something wrong with your user/pass"
#        elif e.errno == errorcode.ER_BAD_DB_ERROR:
#            print "Database does not exist"
#        else:
#            print e

#    cursor = conn.cursor()
#    cursor.execute("SELECT * FROM `user`")
#    last_result = cursor.fetchall()[-1]

#    url_loc = search_keyw2(str(last_result[2]))
#    url_itm = search_keyw2(str(last_result[1]))
#    url_loc_code = detloccode2(url_loc)
#    url_sort = sort_det2(str(last_result[4]))
#
#   url_search = 'http://wwwb.autotrader.ca/cars/' + url_itm + url_loc_code + '%2c+ON&sts=New-Used&hprc=True&wcp=True&inMarket=basicSearch&rcs=' + str(
#        i + 15)
#    return url_search


#def cragslst():
#    holder = []
#    for i in range(0, 2):
#        url = fn5(i)
#        br = mechanize.Browser()
#        br.set_handle_robots(False)
#        htmltext = br.open(url)
#        soup = BeautifulSoup(htmltext)
#        saleitem = soup.findAll('p', {'class': 'row'})
#        holder = holder + saleitem
#    return holder



########################################################################################################################

@app.route('/')
def first_page():
    return render_template("auto.html")

@app.route('/', methods = ['POST'])
def fn():
    carinfo = request.form['carname']
    first = blank()
    kiarray = kijiji(carinfo)
    wharray = wheels(carinfo)
    cparray = carpages(carinfo)
    len_wharr = len(wharray)
    len_kiarr = len(kiarray)
    len_cparr = len(cparray)
    new_array = first[0]
    max_len = max(len_kiarr, len_wharr, len_cparr)
    for i in range(1, max_len):
        try:
            new_array.append(kiarray[i])
        except:
            print""
        try:
            new_array.append(wharray[i])
        except:
            print""
    test = new_array
    return render_template("fullpage.html", test = test)



if __name__ == '__main__':
    app.run()
