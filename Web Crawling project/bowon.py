import requests
from bs4 import BeautifulSoup


def IpoCrawling():
    URL='https://finance.naver.com/sise/ipo.nhn'

    response=requests.get(URL)
    soup=BeautifulSoup(response.text,'html.parser')

    ipos=soup.select('.item_area')
    result=[]

    for ipo in ipos:
        ipo_name=ipo.select_one('.item_name').text
        ipo_price=ipo.select_one('.area_price span').text.strip()
        ipo_sup=ipo.select_one('.area_sup').text.split()[1]
        ipo_private=ipo.select_one('.area_private').text.split()[1]
        ipo_list=ipo.select_one('.area_list').text.split()[1]
        # ipo_detail=

        result.append([ipo_name,ipo_price,ipo_sup,ipo_private,ipo_list])

    return result



# def main():
#     IpoCrawling()

# if __name__=='__main__':
#     main()